#!/usr/bin/env python
"""Cross-method diff: compare Claude vision transcript vs tesseract output for
the 6 verified pages of MIL-HDBK-141 ch06.

Outputs per-page discrepancy report: spots where the two independent methods
disagree, which are candidates for a third opinion / human check.
"""
import re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.environ.get("VERIFY_DIR", HERE)
PILOT = os.environ.get("PILOT_MD", os.path.join(HERE, "..", "ocr_output", "ch06.md"))

def load_chapter_md():
    with open(PILOT, encoding='utf-8') as f:
        return f.read()

def split_pages(md):
    """Split the tesseract chapter md into per-page dicts by <!-- === PAGE NN === -->."""
    pages = {}
    cur = None
    for line in md.split('\n'):
        m = re.search(r'<!-- === PAGE (\d+) === -->', line)
        if m:
            cur = int(m.group(1))
            pages[cur] = []
        elif cur is not None:
            pages[cur].append(line)
    # drop placeholder-only markers for text comparison (keep a tally)
    return pages

def clean_text(lines):
    """Remove placeholders and header/footer chrome so we compare prose only."""
    out = []
    for ln in lines:
        if ln.strip().startswith('>['):       # figure/table/equation placeholders
            continue
        if re.match(r'^(i |\| )', ln):        # OCR gutter artifacts
            ln = re.sub(r'^(i |\| )', '', ln)
        # drop lone page numbers & running headers
        if re.fullmatch(r'\s*[\d-]+[.\s]*\s*', ln):
            continue
        out.append(ln.strip())
    return out

def main():
    md = load_chapter_md()
    pages = split_pages(md)
    # load claude transcript
    with open(os.path.join(D, 'claude_transcript.md'), encoding='utf-8') as f:
        ct = f.read()
    # per-page claude sections
    claude_pages = {}
    cur = None
    for line in ct.split('\n'):
        m = re.match(r'## PAGE (\d+)', line)
        if m:
            cur = int(m.group(1))
            claude_pages[cur] = []
        elif cur is not None:
            claude_pages[cur].append(line)

    # tokenize claude text words for comparison per page
    def words(txt):
        return set(re.findall(r"[A-Za-z][A-Za-z'-]{2,}", txt))

    # filter out claude's structural section labels
    STRUCT = {'text','equations','figures','tables','flags','diagrams','uncertainty',
              'none','some','several','note','page','pages','summary','annotations',
              'unclear','column','columns','row','rows','label','labels','value','values'}
    def content_words(wset):
        return {w for w in wset if w.lower() not in STRUCT and len(w) > 3}

    pages_of_interest = sorted(claude_pages.keys())
    print("=== CROSS-METHOD DIFF (tesseract vs Claude vision) ===\n")
    print("Method: two independent transcribers of the SAME scanned pages.")
    print("Agreement = shared content tokens (strong reliability signal).")
    print("Disagreement = claude-only content = CANDIDATES for third-opinion/human check.\n")
    for pg in pages_of_interest:
        tst_words = words(" ".join(clean_text(pages.get(pg, []))))
        cl_words = words(" ".join(claude_pages.get(pg, [])))
        common = content_words(tst_words) & content_words(cl_words)
        only_tst = content_words(tst_words) - content_words(cl_words)
        only_cl  = content_words(cl_words) - content_words(tst_words)
        print(f"-- PAGE {pg:>02}: shared content tokens = {len(common)} "
              f"({len(common)/max(len(content_words(cl_words)),1)*100:.0f}% of claude's content)")
        if only_cl:
            print(f"    claude-only content (diff candidate): {sorted(only_cl)[:15]}")
        if only_tst:
            print(f"    tesseract-only content (diff candidate): {sorted(only_tst)[:15]}")

def clean_pages_for_numeric():
    pass

if __name__ == '__main__':
    main()