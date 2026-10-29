#!/usr/bin/env python3
"""Reconcile MIL-HDBK-141: find every 'Table N.M' reference and check if it's transcribed.

Strategy (agreed 2026-10-03): the ~150 [TABLE] placeholders are mostly figure/gridline noise.
The book's REAL data tables are referenced in prose as "Table N.M". So:
  Step 1: collect every "Table N.M" / "TABLE N-M" reference across all ocr_output/ch*.md
  Step 2: for each, determine whether a proper markdown table (rows starting '|') exists
          on/near that page.
  Step 3: a table that is referenced but has NO markdown table anywhere in the chapter
          (excluding the noise placeholders) = a genuine gap worth a vision pass.
"""
import re, sys, glob

# --- collect distinct chapter files ---
files = sorted(glob.glob('ocr_output/ch*.md'))
print(f"scanning {len(files)} chapter files")

# gather: chapter -> {table_ref: [page numbers]}  and  chapter -> {page: had_markdown_table?}
def chapter_pages(fname):
    txt = open(fname).read()
    parts = re.split(r'<!-- === PAGE (\d+) === -->', txt)
    pages = {}
    for i in range(1, len(parts)-1, 2):
        pages[int(parts[i])] = parts[i+1]
    return pages, len(txt)

all_refs = {}        # (chapter, table_id) -> set(page numbers with prose/heading ref)
ref_kind = {}        # (chapter, table_id) -> 'heading'|'prose'
md_table_pages = {}  # chapter -> set of pages containing a markdown table

for f in files:
    mch = re.search(r'ch(\d+[^.]*)\.md', f)
    ch = mch.group(1) if mch else re.sub(r'\.md$', '', re.sub(r'^ocr_output/', '', f))
    pages, _ = chapter_pages(f)
    md_pages = set()
    refs = {}
    for pno, body in pages.items():
        # markdown table present if a '|' header row + '| --- |' separator + data rows
        if re.search(r'^\|.*\|.*\|\s*$', body, re.M) and re.search(r'^\|[-: |]+\|\s*$', body, re.M):
            md_pages.add(pno)
        # "Table 20.1" or "Table 21-14" references (title case + words Table/TABLE)
        for m in re.finditer(r'\b(?:Table|TABLE)\s+(\d+)[.\-](\d+)\b', body):
            tid = f"{m.group(1)}.{m.group(2)}"
            # heading if line-start (printed table title), else prose
            line_start = m.start() == 0 or body[:m.start()].endswith('\n')
            if (ch, tid) not in refs:
                refs[(ch, tid)] = set()
            refs[(ch, tid)].add(pno)
            # heading marker takes precedence
            if line_start:
                ref_kind[(ch, tid)] = 'heading'
            else:
                ref_kind.setdefault((ch, tid), 'prose')
    all_refs[ch] = refs
    md_table_pages[ch] = md_pages

# --- check each ref: does a markdown table exist ANYWHERE in chapter? ---
print("\n=== RECONCILE: referenced tables vs transcribed markdown tables ===")
gap = []
for ch in sorted(all_refs):
    md_pages = md_table_pages[ch]
    rows = []
    for (c, tid), pnos in sorted(all_refs[ch].items()):
        kind = ref_kind.get((c, tid), 'prose')
        # a table is 'covered' if the chapter has ANY markdown table (on a referenced page or not)
        has_md = bool(md_pages)
        status = "HAS-MD" if has_md else "**MISSING**"
        rows.append((status, pnos, kind, tid))
    if not rows:
        print(f"\n  ch{ch}: no Table refs found")
        continue
    print(f"\n  ch{ch}: {len(rows)} table reference(s)  (markdown-table pages in ch: {sorted(md_pages)})")
    for status, pnos, kind, tid in rows:
        mark = "   " if status == "HAS-MD" else ">>>"
        print(f"    {mark} {status:9} Table {tid:8} ({kind:7}) referenced on page(s) {sorted(pnos)}")
        if status == "**MISSING**":
            gap.append((ch, tid, sorted(pnos)))

print("\n\n=== GENUINE GAPS (referenced but no markdown table in chapter) ===")
if gap:
    for ch, tid, pnos in gap:
        print(f"  ch{ch} Table {tid} on page(s) {pnos}")
else:
    print("  NONE — every referenced table appears covered by at least one markdown table")