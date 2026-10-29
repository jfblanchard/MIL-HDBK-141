#!/usr/bin/env python
"""Layer 0 OCR pipeline for MIL-HDBK-141.
Converts a scanned chapter PDF -> clean per-chapter Markdown.

Strategy:
  For each page:
    1. Rasterize to high-DPI PNG.
    2. Detect large non-text regions (figures, tables) with OpenCV -> emit [FIGURE]/[TABLE] placeholders.
    3. OCR the text regions with tesseract (psm 6).
    4. Detect math-like lines (dense symbols, low confidence) -> [EQUATION] placeholder.

Usage:
  python ocr_pipeline.py <chapter.pdf> [outdir] [-f first_page -l last_page]
"""
import sys, os, re, glob, subprocess, tempfile
import numpy as np
import cv2
import pytesseract
from PIL import Image, ImageFilter

# Tool locations: found on PATH by default; override with TESSERACT_CMD / PDFTOPPM.
pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_CMD', 'tesseract')
PDFTOPPM = os.environ.get('PDFTOPPM', 'pdftoppm')

# ---------------------------------------------------------------------------
# figure/table region detection
# ---------------------------------------------------------------------------
def find_regions(img_nd, img_small):
    """Return list of (x,y,w,h, kind) bounding boxes for figures/tables.
    Figures = large connected ink clusters separated by whitespace.
    Tables = dense gridline structures.
    kind: 'figure' or 'table'
    """
    # work on binarized, downscaled image for speed
    h, w = img_nd.shape
    # invert so ink=white
    _, bw = cv2.threshold(img_nd, 150, 255, cv2.THRESH_BINARY_INV)
    # morphological close to merge nearby strokes into blobs
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    closed = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel, iterations=2)
    # find connected components
    n, labels, stats, cents = cv2.connectedComponentsWithStats(closed, connectivity=8)
    regions = []
    page_area = w * h
    for i in range(1, n):
        x, y, cw, ch, area = stats[i]
        # a figure/table is a blob spanning a meaningful fraction of the page
        if cw > 0.15 * w and ch > 0.10 * h and area > 0.005 * page_area:
            regions.append((x, y, cw, ch))
    # dedupe heavily overlapping bboxes
    merged = []
    for r in sorted(regions, key=lambda r: -r[3] * r[2]):
        if all(not overlap_ratio(r, m) > 0.5 for m in merged):
            merged.append(r)
    # classify figure vs table via gridline density
    result = []
    for (x, y, cw, ch) in merged:
        sub = bw[y:y + ch, x:x + cw]
        sobel = cv2.Sobel(sub, cv2.CV_64F, 1, 1, ksize=3)
        score = float(np.mean(np.abs(sobel)))
        kind = 'table' if score > 6 else 'figure'
        result.append((x, y, cw, ch, kind))
    return result

def overlap_ratio(a, b):
    ix = max(0, min(a[0]+a[2], b[0]+b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[1]+a[3], b[1]+b[3]) - max(a[1], b[1]))
    inter = ix * iy
    return inter / min(a[2]*a[3], b[2]*b[3]) if min(a[2]*a[3], b[2]*b[3]) else 0

# ---------------------------------------------------------------------------
# math line detection on OCR text
# ---------------------------------------------------------------------------
MATH_RE = re.compile(r'[=≈≤≥≠±÷×·∫∑√πθφμλ]')

def is_math_line(line):
    """Strict test: a line is a display-equation placeholder only if it is a SHORT
    line dominated by math operators/variables with few real words."""
    t = line.strip()
    if not (3 <= len(t) <= 90):
        return False
    # define 'real words': tokens with >=3 consecutive letters (prose / prose-with-digit)
    def real_words(s):
        return len(re.findall(r'[A-Za-z]{3,}', s))
    words = real_words(t)
    has_op = bool(MATH_RE.search(t))
    # numbered display equation signature: ends with a bare "(NN)" or "(NNb)" 
    numbered = re.search(r'\(\s*\d+[a-z]?\s*\)\s*$', t) is not None
    # math if: short + has operator + few words; OR explicitly numbered + short
    if numbered and len(t) <= 70 and words <= 4:
        return True
    if has_op and words <= 2 and len(t) <= 60:
        # avoid prose that contains an = sign in a sentence
        if any(' ' in w and len(w) > 12 for w in t.split()):
            return False
        return True
    return False

# ---------------------------------------------------------------------------
def rasterize(pdf, outdir, first=1, last=None):
    args = [PDFTOPPM, '-png', '-r', '300']
    if last:
        args += ['-f', str(first), '-l', str(last)]
    args += [pdf, os.path.join(outdir, 'page')]
    subprocess.run(args, check=True)
    return sorted(glob.glob(os.path.join(outdir, 'page-*.png')))

def ocr_page(png, region_map, page_no):
    """OCR a page, returning markdown lines. region_map: placeholders to inject."""
    img = Image.open(png).convert('L')
    data = np.array(img)
    md = []
    # Inject placeholders for detected figure/table regions (top-to-bottom)
    ph_lines = sorted(region_map, key=lambda r: r[1])  # sort by y
    # OCR full page text (psm 6), then we post-process
    text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    return text, ph_lines, page_no

def main():
    pdf = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(pdf)
    os.makedirs(outdir, exist_ok=True)
    first = last = None
    if '-f' in sys.argv:
        first = int(sys.argv[sys.argv.index('-f') + 1])
    if '-l' in sys.argv:
        last = int(sys.argv[sys.argv.index('-l') + 1])

    pages = rasterize(pdf, outdir, first, last)
    print(f"[ocr] rasterized {len(pages)} pages", file=sys.stderr)

    chapter_md = []
    eq_counter = 0
    for p in pages:
        pno = os.path.basename(p).split('-')[1].split('.')[0]
        img = Image.open(p).convert('L')
        data = np.array(img)
        regions = find_regions(data, None)
        text, _, _ = ocr_page(p, regions, pno)
        # placeholder insertion with math-line detection
        page_lines = []
        for raw in text.split('\n'):
            line = raw.strip()
            if not line:
                page_lines.append('')
            elif is_math_line(line):
                eq_counter += 1
                page_lines.append(f">[EQUATION {eq_counter}: {line}] — OCR unreliable; needs manual/LaTeX entry")
            else:
                page_lines.append(line.rstrip())
        # strip running manuscript headers (MIL-HDBK-141) and lone page-number footers
        page_lines = [l for l in page_lines if 'MIL-HDBK' not in l.replace(' ', '') and l.strip()]
        page_lines = [l for l in page_lines if not re.fullmatch(r'\s*\d+\s*-\s*\d+\s*', l)]
        chapter_md.append(f"<!-- === PAGE {pno} === -->")
        # inject figure/table placeholders positioned by original y (top-first already)
        for (x, y, cw, ch, kind) in sorted(regions, key=lambda r: r[1]):
            marker = 'TABLE' if kind == 'table' else 'FIGURE'
            chapter_md.append(f">[{marker}: page {pno}, {cw}x{ch}px — needs manual extraction]")
        chapter_md.extend(page_lines)

    md_name = os.path.splitext(os.path.basename(pdf))[0] + '.md'
    with open(os.path.join(outdir, md_name), 'w', encoding='utf-8') as f:
        f.write("\n".join(chapter_md))
    print(f"[ocr] wrote {md_name} ({eq_counter} equation placeholders)", file=sys.stderr)
    return os.path.join(outdir, md_name)

if __name__ == '__main__':
    main()