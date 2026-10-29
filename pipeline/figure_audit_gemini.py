#!/usr/bin/env python3
"""MIL-HDBK-141 figure audit via google/gemini-3.1-flash-lite-image (cheap-VLM pass).

Parses every [FIGURE ...] block across ocr_output/chNN.md (all 3 format variants), determines each
figure's scan page (in-block 'page NN' if present else nearest '=== PAGE NN ===' marker), renders
each UNIQUE figure page from docs/scans/chNN.pdf ONCE, and asks gemini-3.1-lite to verify every
figure title on that page against the actual drawing. Classifies KEPT / REWRITTEN / UNVERIFIED.

Writes verification/FIGURE_AUDIT.md. Resume-safe (state in /tmp/mil_figaudit_state.json).
Cost: ~1.3K img tok + ~150 text tok per unique page; ~60 unique pages ≈ pennies.

Requires OPENROUTER_API_KEY. Needs pdftoppm + convert (ImageMagick).
"""
import base64, os, re, json, subprocess, sys, time, urllib.request

KEY = os.environ.get("OPENROUTER_API_KEY", "")
if not KEY:
    print("NO OPENROUTER_API_KEY in env"); sys.exit(1)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OCR = os.path.join(REPO, "ocr_output")
SCAN = os.path.join(REPO, "docs", "scans")
OUT = os.path.join(REPO, "verification", "FIGURE_AUDIT.md")
STATE = "/tmp/mil_figaudit_state.json"
MODEL = "google/gemini-3.1-flash-lite-image"
TMPIMG = "/tmp/mil_figaudit_pages"
os.makedirs(TMPIMG, exist_ok=True)

def _write(results, total, out=OUT):
    from collections import Counter
    c = Counter(r[4] for r in results)
    lines = ["# MIL-HDBK-141 Figure Audit (gemini-3.1-flash-lite-image)\n",
             f"- Total blocks: {total}. KEPT {c['KEPT']} · REWRITTEN {c['REWRITTEN']} · "
             f"UNVERIFIED {c['UNVERIFIED']}\n",
             "- Note: UNVERIFIED = render/API failure or 'no figure on page' — needs Claude/manual check.\n\n"]
    lines.append("| fig | ch | page | status | title/correction | reason |\n|---|---|---|---|---|---|\n")
    for fn, page, fid, title, status, newt, reason in results:
        m = re.match(r"ch(\d+)", fn)
        chnum = m.group(1) if m else "?"
        disp = (newt or title).replace("|", "/")[:80]
        lines.append(f"| {fid} | {chnum} | {page} | {status} | {disp} | {reason or ' '} |\n")
    open(out, "w").write("".join(lines))

done = set()
if os.path.exists(STATE):
    try: done = set(json.load(open(STATE)))
    except Exception: done = set()

# ---------------- parsing ----------------
def parse_figures(fn):
    """Return list of (fig_id, page, title). Page = in-block 'page NN' else nearest marker."""
    text = open(os.path.join(OCR, fn), encoding="utf-8").read()
    figs = []
    marker = None
    # split into segments at each page marker, track running page from markers for blocks w/o page
    for line in text.splitlines():
        m = re.search(r"PAGE\s*(\d+)", line)
        if m:
            marker = int(m.group(1)); continue
    # sequential scan: figure blocks may span lines; use a regex over whole text
    marker_pages = [(m.start(), int(m.group(1))) for m in re.finditer(r"PAGE\s*(\d+)", text)]
    for m in re.finditer(r"\[FIGURE[:\s]*(.*?)\]", text, re.S):
        inner = m.group(1)
        start = m.start()
        # strip leading 'page NN' + optional (top/bottom) + dimensions before the fig number
        tail = inner
        ib = re.match(r"\s*page\s*(\d+)\s*(?:\((?:top|bottom|upper|lower)\))?\s*,\s*", tail)
        if ib:
            page = int(ib.group(1))
            tail = tail[ib.end():]
        else:
            page = next((p for pos, p in reversed(marker_pages) if pos < start), None)
        # drop a leading dimension token like '2544x3244px' or '~480×320px' (dims not the fig id)
        tail = re.sub(r"^[~\s]*(?:\d+)\s*[x×]\s*\d+px?[\s,]*", "", tail)
        # fig id: 'Figure X.Y' anywhere near front, else a leading 'X.Y' token
        fm = re.search(r"\b(?:Figure\s+)?([\d]+\.[\d]+[a-z]?)", tail)
        if fm:
            fig_id = fm.group(1)
            # title = after the '—' or ':' that introduces the description
            sep = re.search(r"[/—:,]\s*", tail[fm.end():])
            title = ("Figure " + fig_id + " — " + tail[fm.end()+sep.end():].strip()
                     if sep else tail[fm.end():].strip())
        else:
            # bare 'needs manual extraction' block — placeholder, not a real figure desc
            fig_id = None
            title = tail.strip()
        figs.append((fig_id, page, title))
    return figs

def collect_all():
    allf = []
    for fn in sorted(os.listdir(OCR)):
        if fn.startswith("ch") and fn.endswith(".md"):
            if fn in ("ch00_toc.md", "ch28_idx.md"):  # TOC/index — no real content figures
                continue
            try:
                for tup in parse_figures(fn):
                    allf.append((fn, *tup))
            except Exception as e:
                print(f"  parse error {fn}: {e}", file=sys.stderr)
    return allf

# ---------------- rendering: per unique chapter+page ----------------
_render_cache = {}
def render_page(ch, page):
    key = f"ch{ch}_p{page}"
    if key in _render_cache:
        return _render_cache[key]
    pdf = os.path.join(SCAN, f"ch{ch}.pdf")
    if not os.path.exists(pdf):
        _render_cache[key] = None
        return None
    png = os.path.join(TMPIMG, key + ".png")
    if not (os.path.exists(png) and os.path.getsize(png) > 15000):
        r = subprocess.run(["pdftoppm","-png","-r","150","-f",str(page),"-l",str(page),
                            "-singlefile",pdf,png[:-4]], capture_output=True)
    if not os.path.exists(png):
        _render_cache[key] = None
        return None
    # cap image size to keep tokens reasonable; keep re-rendering down if too big
    for _ in range(2):
        sz = os.path.getsize(png)
        if sz > 2500000:
            subprocess.run(["convert",png,"-resize","80%",png], capture_output=True)
        else:
            break
    _render_cache[key] = png if os.path.getsize(png) > 12000 else None
    return _render_cache[key]

# ---------------- gemini ----------------
PROMPT = (
"This is a page from the 1962 US military handbook 'Optical Design' (MIL-HDBK-141). "
"Below are ONE OR MORE figure descriptions from our corpus, each tagged with an id. "
"Look at the ACTUAL FIGURE(S) drawn on the page and for EACH id answer whether the existing "
"description matches the figure, and if not give the best 1-line corrected title. "
"Respond with ONLY a JSON array, one object per id, in the same order:\n"
'[{"id": "...", "match": true/false, "correct_title": "<1-line title if mismatch, else null>", '
'"reason": "<<=10 words>", "page_has_figure": true/false}]\n'
"If a described figure is NOT on this page, set match=false, reason='not on this page'. "
"If the page has no figure at all, set page_has_figure=false. Be concise and accurate.")

def ask_gemini(png, figlist):
    b64 = base64.b64encode(open(png,"rb").read()).decode()
    descs = "\n".join(f"[{fid}] {title[:350]}" for fid, title in figlist)
    payload = {"model":MODEL,"messages":[{"role":"user","content":[
        {"type":"image_url","image_url":{"url":f"data:image/png;base64,{b64}"}},
        {"type":"text","text":PROMPT + "\n\nFIGURES TO VERIFY:\n" + descs}]}],"max_tokens":2000}
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode(),
        headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
    for a in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            txt = d["choices"][0]["message"]["content"].strip()
            txt = re.sub(r"^```(json)?|```$","",txt.strip()).strip()
            j = json.loads(txt)
            if isinstance(j, dict):  # normalize single-object response
                j = [j]
            return j
        except Exception as e:
            if a == 2:
                return None
            time.sleep(2*(a+1))
    return None

# ---------------- main ----------------
allf = collect_all()
# optional chapter filter for targeted re-runs: MIL_FIG_CHAPTERS="20,21,25"
_ch_filter = os.environ.get("MIL_FIG_CHAPTERS", "")
if _ch_filter:
    want = set(_ch_filter.split(","))
    def _chnum(t): 
        m = re.match(r"ch(\d+)", t[0]); return m.group(1) if m else None
    allf = [t for t in allf if _chnum(t) in want]
    print(f"Chapter filter {sorted(want)} -> {len(allf)} figure blocks retained")
total = len(allf)
print(f"Parsed {total} figure blocks from {len(set(f for f,_,_,_ in allf))} chapters")

# group by (ch,page) but keep order + each fig's (fn,fig_id,title)
groups = {}
for fn, fig_id, page, title in allf:
    ch = re.match(r"ch(\d+)", fn).group(1)
    groups.setdefault((ch, page), []).append((fig_id, title))

results = []  # (fn, page, fig_id, title, status, new_title, reason)
processed = 0
# Bare placeholders (fig_id None) are flagged UNVERIFIED immediately, no API call.
for (ch, page) in list(groups):
    bare = [(fid, t) for fid, t in groups[(ch, page)] if fid is None]
    if bare:
        for fid, title in bare:
            results.append((f"ch{ch}.md", page, fid, title, "UNVERIFIED",
                            None, "bare placeholder (needs manual extraction)"))
        groups[(ch, page)] = [(fid, t) for fid, t in groups[(ch, page)] if fid is not None]
    if not groups[(ch, page)]:
        del groups[(ch, page)]

_limit = int(os.environ.get("MIL_FIG_LIMIT_PAGES", "0"))  # smoke-test: only first N pages
for idx, ((ch, page), figlist) in enumerate(groups.items()):
    if _limit and idx >= _limit:
        break
    pg_key = f"ch{ch}_p{page}"
    # page-level resume: skip if all fig ids on page already done
    if all(f"{pg_key}_{fid}" in done for fid, _ in figlist):
        processed += len(figlist)
        continue
    png = render_page(ch, page)
    if not png:
        for fid, title in figlist:
            results.append((f"ch{ch}.md", page, fid, title, "UNVERIFIED", None, "render failed/no pdf"))
            done.add(f"{pg_key}_{fid}")
        processed += len(figlist)
        continue
    ans = ask_gemini(png, figlist)
    byid = {}
    if ans:
        for o in ans:
            if isinstance(o, dict) and "id" in o:
                byid[str(o["id"])] = o
    for fid, title in figlist:
        o = byid.get(fid)
        key = f"{pg_key}_{fid}"
        if not o:
            status, newt, reason = "UNVERIFIED", None, "no API response"
        elif not o.get("page_has_figure", True):
            status, newt, reason = "UNVERIFIED", None, "no figure on page"
        elif o.get("match") is True:
            status, newt, reason = "KEPT", None, None
        else:
            status, newt = "REWRITTEN", o.get("correct_title")
            reason = o.get("reason")
        results.append((f"ch{ch}.md", page, fid, title, status, newt, reason))
        done.add(key)
    json.dump(list(done), open(STATE,"w"))
    processed += len(figlist)
    # incremental write every 5 pages
    if len(groups) and (list(groups).index((ch,page)) % 5 == 4):
        _write(results, total)
        print(f"  ...{processed}/{total} processed", flush=True)

_write(results, total)
# hard coverage guarantee: every parsed figure must have a row
_missing = total - len(results)
if _missing:
    print(f"WARNING: {_missing} figure blocks missing from results (coverage {len(results)}/{total})",
          file=sys.stderr)
from collections import Counter
c = Counter(r[4] for r in results)
print(f"DONE: {total} figures | KEPT {c['KEPT']} | REWRITTEN {c['REWRITTEN']} | UNVERIFIED {c['UNVERIFIED']}")
print(f"Wrote {OUT}")