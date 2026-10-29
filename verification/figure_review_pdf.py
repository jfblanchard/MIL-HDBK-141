#!/usr/bin/env python3
"""Side-by-side figure review PDF: scan original (auto-cropped) next to the rebuilt figure.

One page per figure: left = crop of the 1962 scan page, right = the rebuilt PNG from
build/lens_designs/. Sections: DONE schematics, DONE plots, FLAGGED, halftone (scan-only),
3D-coordinate (scan-only), tables. Each page is titled 'Figure X.Y - scan chNN pM' plus a
one-line note (flag reason, partial-build note, or bucket) so a human can flip through and
mark anything that does not match.

Figure regions are located with the same connected-component detector as the OCR pipeline
(pipeline/ocr_pipeline.py find_regions, ported to scipy): ink threshold, 9x9 morphological
close, connected components, size filter, figure-vs-table classification by edge density.
Which detected box belongs to a figure is decided by its printed caption: tesseract (TSV)
locates the word 'Figure X.Y' on the page and the crop is the figure box immediately above
that caption; fallback order is the [FIGURE:] placeholder index, the single box, the union
of boxes, and finally the whole page. A small bottom pad keeps the caption in the crop.

Usage:  python3 verification/figure_review_pdf.py [out.pdf]
Run with the optiland env (needs scipy, PIL, matplotlib): no cv2, no fitz - pages are
rasterized with pdftoppm at 150 dpi into a temp dir.
"""
import re, sys, tempfile, subprocess
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

ROOT = Path(__file__).resolve().parents[1]
SCAN = ROOT / "docs" / "scans"
OCR = ROOT / "ocr_output"
LD = ROOT / "build" / "lens_designs"
DPI = 150

# --------------------------------------------------------------------------
# figure region detection (port of pipeline/ocr_pipeline.py find_regions)
# --------------------------------------------------------------------------
def find_regions(img):
    """[(x,y,w,h,kind)] ink blobs spanning a meaningful fraction of the page."""
    h, w = img.shape
    bw = img < 150
    closed = ndimage.binary_closing(bw, structure=np.ones((9, 9)), iterations=2)
    lab, n = ndimage.label(closed, structure=np.ones((3, 3)))
    stats = ndimage.find_objects(lab)
    regions = []
    for i, sl in enumerate(stats):
        if sl is None:
            continue
        ys, xs = sl
        cw, ch = xs.stop - xs.start, ys.stop - ys.start
        area = (lab[sl] == i + 1).sum()
        if cw > 0.15 * w and ch > 0.10 * h and area > 0.005 * w * h:
            regions.append((xs.start, ys.start, cw, ch))
    merged = []
    for r in sorted(regions, key=lambda r: -r[3] * r[2]):
        if all(not overlap_ratio(r, m) > 0.5 for m in merged):
            merged.append(r)
    out = []
    for (x, y, cw, ch) in merged:
        sub = bw[y:y + ch, x:x + cw].astype(float)
        score = float(np.mean(np.abs(ndimage.sobel(sub, axis=0)) + np.abs(ndimage.sobel(sub, axis=1))))
        out.append((x, y, cw, ch, "table" if score > 12 else "figure"))
    return out


def overlap_ratio(a, b):
    ix = max(0, min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0]))
    iy = max(0, min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1]))
    inter = ix * iy
    return inter / min(a[2] * a[3], b[2] * b[3]) if min(a[2] * a[3], b[2] * b[3]) else 0


# --------------------------------------------------------------------------
# figure -> scan page mapping
# --------------------------------------------------------------------------
def spec_pages():
    """figure id -> (chapter, scan page) from the three spec files."""
    out = {}
    for name in ("gap_pages_figure_specs.md", "ch22_25_figure_specs.md",
                 "last2_gap_pages_figure_specs.md"):
        p = ROOT / "verification" / name
        if not p.exists():
            continue
        for m in re.finditer(r"FIGURE\s+(?:ch)?(\d+)[-.](\d+)\s*\(on page (ch\w+)\s*p(\d+)\)",
                             p.read_text()):
            out[f"{m.group(1)}.{m.group(2)}"] = (m.group(3), int(m.group(4)))
    return out


def ocr_figure_pages():
    """figure id -> (chapter, transcript page, index among that page's FIGURE placeholders)
    from the [FIGURE: ...] blocks in ocr_output/."""
    out, per_page = {}, {}
    fig_pat = re.compile(r"Figure\s+(\d+\.\d+)")
    for md in sorted(OCR.glob("ch*.md")):
        ch = md.stem
        page = None
        for ln in md.read_text(errors="replace").splitlines():
            m = re.match(r"<!-- === PAGE (\d+) === -->", ln)
            if m:
                page = int(m.group(1))
                continue
            if ln.startswith(">[FIGURE:") and page is not None:
                fm = fig_pat.search(ln)
                idx = per_page.setdefault((ch, page), 0)
                per_page[(ch, page)] = idx + 1
                if fm and fm.group(1) not in out:
                    out[fm.group(1)] = (ch, page, idx)
    return out


# --------------------------------------------------------------------------
# manifest -> work items
# --------------------------------------------------------------------------
def manifest_items():
    """[(fig_id, folder, status, note)] for every row of the manifest tables."""
    txt = (ROOT / "verification" / "OPTiLAND_BATCH_MANIFEST.md").read_text()
    items = []
    for m in re.finditer(r"^\|\s*([\d.]+|Table\s[\d.]+)\s*\|\s*`(\w+)`\s*\|.*?\|\s*(DONE|FLAGGED|TODO)\b:?\s*([^\n|]*)",
                         txt, re.M):
        fig, folder, status = m.group(1).strip(), m.group(2), m.group(3)
        note = m.group(4).strip() if status == "FLAGGED" else ""
        items.append((fig, folder, status, note))
    return items


EXTRA_FOLDERS = {  # built outside the manifest's 104 targets; fig id per PNG
    "ch12_relay": [("12.1", "ch12_single_relay_layout.png"), ("12.2", "ch12_double_relay_layout.png")],
    "ch14_huygenian": [("14.1", "ch14_huygenian_layout.png")],
    "ch14_ramsden": [("14.4", "ch14_ramsden_layout.png")],
    "ch15_telescope_10x": [("15 (telescope)", "ch15_telescope_10x_layout.png")],
    "ch23_microscope": [("23.7", "ch23_objective_layout.png"), ("23 (microscope)", "ch23_microscope_layout.png")],
}

BUCKETS = {  # non-DONE sections, from the manifest
    "HALFTONE": ["24.1", "25.1", "25.6", "25.7", "25.21", "25.23", "25.26", "25.31", "25.32", "25.34", "25.35"],
    "3D-COORD": ["16.1", "16.33", "16.34", "25.19", "25.22"],
}
TABLES = {"Table 20.1": ("ch20", 15), "Table 20.3": ("ch20", 26)}


def page_png(pdf, pno, tmpdir):
    """Render one scan page at DPI; cache in tmpdir."""
    out = Path(tmpdir) / f"{pdf.stem}_p{pno:03d}.png"
    if not out.exists():
        subprocess.run(["pdftoppm", "-f", str(pno), "-l", str(pno), "-r", str(DPI),
                        "-png", str(pdf), str(out.with_suffix(""))], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cand = sorted(Path(tmpdir).glob(f"{pdf.stem}_p{pno:03d}-*.png"))
        if cand:
            cand[0].rename(out)
    return out


_tsv_cache = {}


def _tsv_rows(png):
    """Word rows (x, y, w, h, text, block, par, line) from tesseract TSV, cached."""
    if png not in _tsv_cache:
        r = subprocess.run(["tesseract", str(png), "stdout", "tsv"],
                           capture_output=True, text=True)
        rows = []
        for ln in r.stdout.splitlines()[1:]:
            f = ln.split("\t")
            if len(f) >= 12 and f[11].strip():
                try:
                    rows.append((int(f[6]), int(f[7]), int(f[8]), int(f[9]),
                                 f[11], int(f[2]), int(f[3]), int(f[4])))
                except ValueError:
                    pass
        _tsv_cache[png] = rows
    return _tsv_cache[png]


def page_captions(png):
    """Every real printed caption on the page: [{'num', 'x', 'y', 'text'}].
    'Figure' counts only as the first word of a line inside a short block (<= 4
    lines) - this filters body-text 'Figure' references out of the caption list."""
    from collections import defaultdict
    rows = _tsv_rows(png)
    lines = defaultdict(list)
    block_lines = defaultdict(set)
    for r in rows:
        lines[(r[5], r[6], r[7])].append(r)
        block_lines[(r[5], r[6])].add(r[7])
    caps = []
    for (blk, par, _ln), ws in lines.items():
        ws.sort(key=lambda r: r[0])
        if not ws[0][4].lower().startswith("fig"):
            continue
        if len(block_lines[(blk, par)]) > 4:
            continue
        num, joined = "", ""
        for w in ws[1:4]:
            d = re.sub(r"\D", "", w[4])
            joined += d
            if not num and d:
                num = d
        if not num:
            continue
        caps.append({"num": num, "joined": joined,
                     "x": ws[0][0], "y": ws[0][1] + ws[0][3] // 2,
                     "text": " ".join(w[4] for w in ws)})
    return caps


def find_caption(png, fig):
    """The printed caption whose number matches fig, or None."""
    target = re.sub(r"\D", "", fig.split(" ")[0])  # '25.6' -> '256'
    if not target:
        return None
    for c in page_captions(png):
        if c["num"] == target or c["joined"].startswith(target):
            return c
    return None


def crop_for(ch, pno, fig_index, tmpdir, fig=None):
    """Crop the figure region (with caption pad) from the scan page PNG.
    Returns (image_array, caption_text_or_None)."""
    png = page_png(SCAN / f"{ch}.pdf", pno, tmpdir)
    img = np.array(Image.open(png).convert("L"))
    h, w = img.shape
    figs = sorted([r for r in find_regions(img) if r[4] == "figure"], key=lambda r: r[1])

    # primary: the figure box immediately above the printed caption
    cap = find_caption(png, fig) if fig else None
    anchor = (cap["x"], cap["y"]) if cap else None
    if anchor is not None and figs:
        ax_, ay_ = anchor
        cands = [r for r in figs if r[1] + r[3] <= ay_ + 0.02 * h
                 and r[0] - 0.06 * w <= ax_ <= r[0] + r[2] + 0.06 * w]
        if cands:
            x, y, cw, ch = max(cands, key=lambda r: r[1] + r[3])[:4]  # nearest above
        else:
            x, y, cw, ch = min(figs, key=lambda r: abs((r[1] + r[3]) - ay_))[:4]
    elif not figs:
        return img, cap["text"] if cap else None  # whole page fallback
    elif fig_index is None or fig_index >= len(figs):
        if len(figs) == 1:
            x, y, cw, ch = figs[0][:4]
        else:  # unknown which box -> union them all so nothing is missed
            x = min(r[0] for r in figs); y = min(r[1] for r in figs)
            cw = max(r[0] + r[2] for r in figs) - x
            ch = max(r[1] + r[3] for r in figs) - y
    else:
        x, y, cw, ch, _kind = figs[fig_index]

    x0, x1 = max(0, x - int(0.02 * w)), min(w, x + cw + int(0.02 * w))
    y0 = max(0, y - int(0.015 * h))
    if cap:
        # start below the *previous* printed caption (kills two-figure crops)
        prev = [c for c in page_captions(png) if c["y"] < cap["y"] - int(0.01 * h)]
        if prev:
            y0 = max(y0, max(prev, key=lambda c: c["y"])["y"] + int(0.025 * h))
        y1 = min(h, cap["y"] + int(0.045 * h))  # caption line + wrap line
    else:
        y1 = min(h, y + ch + int(0.09 * h))
    if y1 <= y0 + 10:  # degenerate -> fall back to the raw box
        y0 = max(0, y - int(0.015 * h)); y1 = min(h, y + ch + int(0.09 * h))
    return img[y0:y1, x0:x1], cap["text"] if cap else None


def pair_page(pdf_out, fig, left, right, note, sec, scan_cap=None):
    """One landscape page: scan crop left, rebuild right."""
    f = plt.figure(figsize=(11.69, 8.27))
    f.suptitle(f"Figure {fig}   —   {sec}", fontsize=13, fontweight="bold")
    axl, axr = f.subplots(1, 2)
    for ax, img, cap2 in ((axl, left, "1962 scan"), (axr, right, "rebuilt")):
        if img is not None:
            ax.imshow(img, cmap="gray", vmin=0, vmax=255)
        else:
            ax.text(0.5, 0.5, "(no scan crop)" if ax is axl else "(not built)",
                    ha="center", va="center", transform=ax.transAxes)
        ax.set_title(cap2, fontsize=10)
        ax.axis("off")
    axl.text(0.5, -0.015, scan_cap or "(printed caption not found on page)",
             transform=axl.transAxes, ha="center", va="top", fontsize=8, style="italic")
    axl.set_title("1962 scan", fontsize=10)
    if note:
        f.text(0.5, 0.03, note, ha="center", fontsize=9, wrap=True)
    f.tight_layout(rect=(0, 0.05, 1, 0.94))
    pdf_out.savefig(f)
    plt.close(f)


def divider(pdf_out, title, lines):
    f = plt.figure(figsize=(11.69, 8.27))
    f.text(0.5, 0.72, title, ha="center", fontsize=20, fontweight="bold")
    for i, ln in enumerate(lines):
        f.text(0.5, 0.62 - i * 0.05, ln, ha="center", fontsize=11)
    pdf_out.savefig(f)
    plt.close(f)


def main():
    out_pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "build" / "figure_review.pdf"
    specp, ocrp = spec_pages(), ocr_figure_pages()
    items = manifest_items()

    # figure -> scan page: spec file first, then ocr placeholders
    def locate(fig):
        if fig in specp:
            return (*specp[fig], 0)
        hit = ocrp.get(fig)
        return (hit[0], hit[1], hit[2]) if hit else (None, None, 0)

    # placeholder index within the page for multi-figure pages (None = unknown)
    def index_on_page(fig):
        hit = ocrp.get(fig)
        return hit[2] if hit else None

    tmp = tempfile.mkdtemp(prefix="figrev_")
    done = [(f, d, n) for f, d, s, n in items if s == "DONE"]
    flag = [(f, d, n) for f, d, s, n in items if s == "FLAGGED"]
    todo = [(f, d, n) for f, d, s, n in items if s == "TODO"]
    issues = []  # figures whose printed caption was not found on the scan page

    with PdfPages(out_pdf) as pp:
        divider(pp, "MIL-HDBK-141 figure review", [
            "Left: crop of the 1962 scan (auto-detected figure region + caption).",
            "Right: the rebuilt figure from build/lens_designs/.",
            f"{len(done)} rebuilt figures, then {len(flag)} flagged, "
            f"{len(BUCKETS['HALFTONE'])} halftone (scan only), "
            f"{len(BUCKETS['3D-COORD'])} 3D-coordinate (scan only), 2 tables.",
            "Mark any page where the rebuild does not match the scan.",
        ])
        divider(pp, "Rebuilt figures", ["scan vs rebuild, one per page"])
        for fig, folder, _ in done:
            ch, pno, idx = locate(fig)
            idx = index_on_page(fig)
            pngs = sorted((LD / folder).glob("*.png"))
            scan_img, cap = crop_for(ch, pno, idx, tmp, fig=fig) if ch else (None, None)
            if cap is None:
                issues.append(fig)
            for png in pngs:
                pair_page(pp, fig, scan_img,
                          np.array(Image.open(png).convert("L")),
                          f"{folder}  |  scan {ch or '?'} p{pno or '?'}", "DONE", cap)
        # extra folders not in the manifest rows
        for folder, lst in EXTRA_FOLDERS.items():
            for fig, png in lst:
                ch, pno, _ = locate(fig)
                scan_img, cap = (crop_for(ch, pno, index_on_page(fig), tmp, fig=fig)
                                 if ch else (None, None))
                pair_page(pp, fig, scan_img,
                          np.array(Image.open(LD / folder / png).convert("L")),
                          f"{folder}  |  scan {ch or '?'} p{pno or '?'}", "DONE (layout)", cap)
        divider(pp, "Flagged - not built", ["spec under-determines the geometry; scan shown so you can judge"])
        for fig, folder, note in flag:
            ch, pno, _ = locate(fig)
            scan_img, cap = (crop_for(ch, pno, index_on_page(fig), tmp, fig=fig)
                             if ch else (None, None))
            pair_page(pp, fig, scan_img, None, f"FLAGGED: {note}", "FLAGGED", cap)
        for sec, figs in (("HALFTONE PHOTO (scan only)", BUCKETS["HALFTONE"]),
                          ("3D-COORDINATE (scan only)", BUCKETS["3D-COORD"])):
            divider(pp, sec, ["no rebuild - decide whether to crop the scan or regenerate"])
            for fig in figs:
                ch, pno, _ = locate(fig)
                scan_img, cap = (crop_for(ch, pno, index_on_page(fig), tmp, fig=fig)
                                 if ch else (None, None))
                pair_page(pp, fig, scan_img, None, "", sec, cap)
        divider(pp, "Tables", ["transcribed into ocr_output/ch20.md - scan shown for checking"])
        for tname, (ch, pno) in TABLES.items():
            scan_img, cap = crop_for(ch, pno, 0, tmp, fig=tname)
            pair_page(pp, tname, scan_img, None,
                      "transcribed - compare values against scan", "TABLE", cap)
        divider(pp, "Auto-detected issues", [
            f"{len(issues)} rebuilt figures had no printed caption found on the scan page",
            "(crop may show the wrong figure - check these first):",
            "  ".join(issues) or "none",
        ])
    print(f"wrote {out_pdf}  |  captions not found: {issues}")


if __name__ == "__main__":
    main()
