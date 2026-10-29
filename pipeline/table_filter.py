#!/usr/bin/env python3
"""Filter MIL-HDBK-141 TABLE placeholders into real-data-tables vs likely-noise.

The 2544px-wide scan pages render most real data tables taller than ~900px. Short,
wide rows are usually OCR gridline/axis misreads or caption marginal lines. This
script lists ch16's tables with pixel dims, auto-flags short/wide as probable noise,
and emits the clean transcribe list. Run per chapter: `python3 table_filter.py ch16`.
"""
import re, sys

def main(charg):
    ch = charg if charg.lower().startswith('ch') else f'ch{charg}'
    path = f'ocr_output/{ch}.md'
    txt = open(path).read()
    tbls = re.findall(r'\[TABLE: page (\d+), (\d+)x(\d+)px — needs manual extraction\]', txt)
    n = len(tbls)
    # Heuristic: real data table on a 2544px scan is usually >= 900px tall; short
    # (<= 700px) wide rows are likely caption lines / gridline noise. The 701-899
    # band is ambiguous and flagged for manual check. Buckets are disjoint.
    noise, gray, real = [], [], []
    for page, w, h in tbls:
        h = int(h); w = int(w)
        row = (int(page), w, h)
        if h >= 900:
            real.append(row)
        elif h <= 700:
            noise.append(row)
        else:
            gray.append(row)
    print(f'== {ch}: {n} table placeholders ==')
    print(f'  REAL (>=900, transcribe):          {len(real)}')
    print(f'  GRAY (701-899, manual check):      {len(gray)}')
    print(f'  PROBABLE NOISE (<=700):            {len(noise)}  (gridline/caption misreads)')
    # the 701-899 gray zone (computed inline now)
    if gray:
        print(f'  GRAY ZONE pages: {[p for p,_,_ in gray]}')
    print('\n-- REAL tables (pages) --')
    print(' '.join(str(p) for p,_,_ in sorted(real)) or '(none)')
    print('\n-- PROBABLE NOISE rows (pages, H px) --')
    for p, w, h in sorted(noise):
        print(f'  p{p}: {w}x{h}px')
    print('\n-- GRAY ZONE (pages, H px) --')
    for p, w, h in sorted(gray):
        print(f'  p{p}: {w}x{h}px')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '16')