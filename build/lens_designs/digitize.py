"""Trace printed curves off a scan page (the measured-data figures of ch20 have no formula behind them).

Workflow per figure: render the page (`page_image`), pick the plot box and two reference ticks per axis in
pixel coordinates, mask printed text/arrows, strip the graph-paper grid, then follow each curve from a seed
point. Output is a short CSV of data-space points (`save_trace`), which the figure's `_plot.py` redraws in
book style. The scan is the only data source, so accuracy is about 1 percent of the axis span.
"""
from pathlib import Path
import subprocess

import numpy as np
from PIL import Image

SCANS = Path(__file__).resolve().parents[2] / "docs" / "scans"
CACHE = Path("/tmp/mil_scan_cache")


def page_image(chapter, page, dpi=400):
    CACHE.mkdir(exist_ok=True)
    stem = CACHE / f"{chapter}_{page}_{dpi}"
    png = Path(str(stem) + f"-{page:02d}.png")
    if not png.exists():
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi), "-png",
                        str(SCANS / f"{chapter}.pdf"), str(stem)], check=True)
        png = next(CACHE.glob(f"{stem.name}-*.png"))
    return np.array(Image.open(png).convert("L"))


class Axes:
    """Linear (or log) pixel to data map from two reference ticks per axis."""

    def __init__(self, px, xv, py, yv):
        self.px, self.xv, self.py, self.yv = px, xv, py, yv

    def x(self, p):
        return self.xv[0] + (np.asarray(p) - self.px[0]) * (self.xv[1] - self.xv[0]) / (self.px[1] - self.px[0])

    def y(self, p):
        return self.yv[0] + (np.asarray(p) - self.py[0]) * (self.yv[1] - self.yv[0]) / (self.py[1] - self.py[0])


def dark_mask(img, box, thresh=120, masks=(), strip_grid=True, grid_frac=0.6):
    """Binary dark mask of the plot box; `masks` are (x0, y0, x1, y1) pixel rectangles to blank (text, arrows,
    legends). Long straight rows/columns (graph-paper grid, frame, ticks) are removed when strip_grid."""
    x0, y0, x1, y1 = box
    m = img[y0:y1, x0:x1] < thresh
    if strip_grid:
        rows = m.mean(axis=1) > grid_frac
        cols = m.mean(axis=0) > grid_frac
        for i in np.where(rows)[0]:
            m[max(i - 1, 0):i + 2, :] = False
        for j in np.where(cols)[0]:
            m[:, max(j - 1, 0):j + 2] = False
    for a, b, c, d in masks:
        m[max(b - y0, 0):max(d - y0, 0), max(a - x0, 0):max(c - x0, 0)] = False
    return m


def clusters(col):
    """Centres and thicknesses of runs of True in a 1-D column."""
    idx = np.where(col)[0]
    if idx.size == 0:
        return []
    splits = np.where(np.diff(idx) > 1)[0] + 1
    return [(g.mean(), g.size) for g in np.split(idx, splits)]


def follow(mask, seed, max_jump=6, max_gap=60):
    """Follow a curve through `mask` from seed=(col, row) in both directions; returns arrays (cols, rows) in
    mask coordinates. Gaps (dashes, grid cut-outs, crossings) up to max_gap columns are bridged linearly."""
    h, w = mask.shape
    near = sorted((abs(rc - seed[1]), rc) for rc, t in clusters(mask[:, int(seed[0])]))
    if not near or near[0][0] > 60:
        raise ValueError(f"no curve pixels near seed {seed}")
    seed = (seed[0], near[0][1])
    out = {int(seed[0]): float(seed[1])}
    for step in (1, -1):
        c, r = int(seed[0]), float(seed[1])
        slope, last_good, gap = 0.0, c, 0
        while 0 <= c + step < w:
            c += step
            cand = [(abs(rc - (r + slope)), rc) for rc, t in clusters(mask[:, c])]
            cand = [k for k in cand if k[0] <= max_jump + abs(slope)]
            if cand:
                rc = min(cand)[1]
                if gap:
                    for cc in range(last_good + step, c, step):
                        out[cc] = r + (rc - r) * (cc - last_good) / (c - last_good)
                    slope = 0.0
                else:
                    slope = 0.5 * slope + 0.5 * (rc - r)
                r, last_good, gap = rc, c, 0
                out[c] = r
            else:
                gap += 1
                if gap > max_gap:
                    break
    cols = np.array(sorted(out))
    return cols, np.array([out[c] for c in cols])


def to_data(cols, rows, box, ax):
    return ax.x(cols + box[0]), ax.y(rows + box[1])


def decimate(x, y, n=120):
    xs = np.linspace(x.min(), x.max(), n)
    return xs, np.interp(xs, x, y)


def save_trace(path, columns, header):
    arr = np.column_stack(columns)
    np.savetxt(path, arr, delimiter=",", header=header, fmt="%.5g", comments="# ")


def overlay(img, box, ax_pix_curves, path, scale=1.0):
    """Debug image: traced curves in red on the scan crop."""
    x0, y0, x1, y1 = box
    rgb = np.stack([img[y0:y1, x0:x1]] * 3, axis=-1).copy()
    for cols, rows in ax_pix_curves:
        for c, r in zip(cols, rows):
            r = int(round(r))
            if 0 <= r < rgb.shape[0] and 0 <= c < rgb.shape[1]:
                rgb[max(r - 1, 0):r + 2, c] = (255, 0, 0)
    Image.fromarray(rgb).save(path)


# --- guided tracing (added for the measured-curve batch) ------------------------------------------------------
# The scans are slightly rotated and the curves run through graph-paper grids, cross each other and turn vertical
# at filter edges, so column-wise following is not enough. Instead: a hand-read guide polyline (a few pixel points
# per curve) is snapped onto the printed ink by searching along the guide's normal, with the known grid rules
# blanked out. The pixel-to-data map is a least-squares affine fit to grid intersections, which absorbs the tilt.

class AffineAxes:
    """Pixel (col, row) to data (x, y) by least-squares affine fit to reference points; ylog/xlog fit log10."""

    def __init__(self, pix, data, xlog=False, ylog=False):
        pix, data = np.asarray(pix, float), np.asarray(data, float).copy()
        self.xlog, self.ylog = xlog, ylog
        if xlog:
            data[:, 0] = np.log10(data[:, 0])
        if ylog:
            data[:, 1] = np.log10(data[:, 1])
        a = np.column_stack([pix, np.ones(len(pix))])
        self.m, *_ = np.linalg.lstsq(a, data, rcond=None)
        self.inv, *_ = np.linalg.lstsq(np.column_stack([data, np.ones(len(data))]), pix, rcond=None)
        self.resid = np.abs(a @ self.m - data).max(axis=0)

    def data(self, c, r):
        v = np.column_stack([c, r, np.ones(np.size(c))]) @ self.m
        x, y = v[:, 0], v[:, 1]
        return (10 ** x if self.xlog else x), (10 ** y if self.ylog else y)

    def pix(self, x, y):
        x = np.log10(x) if self.xlog else np.asarray(x, float)
        y = np.log10(y) if self.ylog else np.asarray(y, float)
        v = np.column_stack([np.broadcast_to(x, np.broadcast(x, y).shape).ravel(),
                             np.broadcast_to(y, np.broadcast(x, y).shape).ravel(), np.ones(np.broadcast(x, y).size)]) @ self.inv
        return v[:, 0], v[:, 1]


def rule_center(img, c, r, horizontal, half=30, search=15, thresh=150):
    """Refine a hand-read grid rule / frame edge near pixel (c, r): centre of the dark band across a short strip."""
    if horizontal:
        strip = img[int(r) - search:int(r) + search + 1, int(c) - half:int(c) + half + 1] < thresh
        prof = strip.mean(axis=1)
        off = int(r) - search
    else:
        strip = img[int(r) - half:int(r) + half + 1, int(c) - search:int(c) + search + 1] < thresh
        prof = strip.mean(axis=0)
        off = int(c) - search
    w = np.where(prof > 0.5 * prof.max())[0]
    return off + w.mean() if w.size else np.nan


def rule_mask(shape, ax, xs=(), ys=(), xr=(0, 1), yr=(0, 1), width=4.0):
    """Boolean page-shaped mask of the grid rules at data values xs (vertical) and ys (horizontal); xr / yr are any
    two data values along the other axis (used only to get each rule's direction on the tilted scan)."""
    rr, cc = np.mgrid[0:shape[0], 0:shape[1]]
    out = np.zeros(shape, bool)
    for x in xs:
        (c0, c1), (r0, r1) = ax.pix([x, x], list(yr))
        out |= np.abs(cc - (c0 + (rr - r0) * (c1 - c0) / (r1 - r0))) <= width
    for y in ys:
        (c0, c1), (r0, r1) = ax.pix(list(xr), [y, y])
        out |= np.abs(rr - (r0 + (cc - c0) * (r1 - r0) / (c1 - c0))) <= width
    return out


def snap(ink, guide, tol=12, step=1.0, prefer="near", smooth=21):
    """Snap a guide polyline [(c, r), ...] (page px) onto ink (boolean page mask): walk the guide by arc length,
    search +-tol px along the local normal, take the centre of the ink run nearest the guide (or nearest the
    previous offset, for continuity). Unfound samples are interpolated. Returns (cols, rows, found_fraction)."""
    g = np.asarray(guide, float)
    seg = np.hypot(*np.diff(g, axis=0).T)
    s = np.concatenate([[0], np.cumsum(seg)])
    ss = np.arange(0, s[-1], step)
    pc, pr = np.interp(ss, s, g[:, 0]), np.interp(ss, s, g[:, 1])
    tc, tr = np.gradient(pc), np.gradient(pr)
    nrm = np.hypot(tc, tr)
    nc, nr = -tr / nrm, tc / nrm
    offs = np.arange(-tol, tol + 0.01, 0.5)
    h, w = ink.shape
    found, prev = np.full(ss.size, np.nan), 0.0
    for i in range(ss.size):
        cc = np.clip(np.round(pc[i] + offs * nc[i]).astype(int), 0, w - 1)
        rr = np.clip(np.round(pr[i] + offs * nr[i]).astype(int), 0, h - 1)
        hit = ink[rr, cc]
        runs = clusters(hit)
        if runs:
            centres = [offs[0] + 0.5 * cidx for cidx, _ in runs]
            ref = prev if prefer == "prev" else 0.0
            found[i] = min(centres, key=lambda v: abs(v - ref))
            prev = found[i]
    frac = np.isfinite(found).mean()
    ok = np.isfinite(found)
    found = np.interp(ss, ss[ok], found[ok]) if ok.any() else np.zeros_like(ss)
    from scipy.ndimage import median_filter, uniform_filter1d
    found = uniform_filter1d(median_filter(found, smooth, mode="nearest"), 5, mode="nearest")
    return pc + found * nc, pr + found * nr, frac


def overlay_paths(img, box, paths, path, guides=()):
    """Debug image: snapped paths in red, guides in blue, on the scan crop (box = x0, y0, x1, y1 page px)."""
    x0, y0, x1, y1 = box
    rgb = np.stack([img[y0:y1, x0:x1]] * 3, axis=-1).copy()
    for col, (cs, rs) in [((255, 0, 0), p) for p in paths] + [((0, 90, 255), (np.asarray(g)[:, 0], np.asarray(g)[:, 1]))
                                                                for g in guides]:
        for c, r in zip(np.asarray(cs) - x0, np.asarray(rs) - y0):
            c, r = int(round(c)), int(round(r))
            if 1 <= r < rgb.shape[0] - 1 and 1 <= c < rgb.shape[1] - 1:
                rgb[r - 1:r + 2, c - 1:c + 2] = col
    Image.fromarray(rgb).save(path)


def calibrate(img, vrules, hrules, xlog=False, ylog=False, search=15, skip=()):
    """AffineAxes from printed grid rules. vrules = [(x_value, col_guess)], hrules = [(y_value, row_guess)]; every
    intersection is measured locally (rules sampled 40 px off the crossing) so the scan's tilt is absorbed. Pairs in
    `skip` ((x_value, y_value)) are left out, e.g. where a curve lies on the rule. Prints the fit residual."""
    pix, data = [], []
    for xv, cg in vrules:
        for yv, rg in hrules:
            if (xv, yv) in skip:
                continue
            dr = 40 if rg + 40 < img.shape[0] else -40
            c = rule_center(img, cg, rg + dr, False, half=12, search=search)
            r = rule_center(img, cg + 40, rg, True, half=12, search=search)
            if np.isfinite(c) and np.isfinite(r):
                pix.append((c, r))
                data.append((xv, yv))
    ax = AffineAxes(pix, data, xlog, ylog)
    print(f"calibrate: {len(pix)} intersections, max residual x {ax.resid[0]:.4g}, y {ax.resid[1]:.4g} (data units)")
    return ax


def trace_figure(here, page, vrules, hrules, guides, box, header, chapter="ch20", flat=(), tol=12, smooth=21,
                 thresh=140, rule_width=4, skip=(), crop=None, xlog=False, ylog=False, keep=None, masks=(), every=3, ax=None,
                 search=15):
    """One figure end to end: calibrate on the grid rules, blank them, snap each guide, write `trace.csv` (rows:
    curve, x, y) in `here` and a debug overlay in CACHE. `flat` names straight printed reference lines kept as their
    median level; `keep` = {name: (xmin, xmax)} trims a curve where the snap runs into lettering; `masks` are page-px
    rectangles to blank (labels, leaders). A plot with ticks but no grid passes a ready `ax` (see tick_axes) and
    empty rule lists. Returns the AffineAxes."""
    img = page_image(chapter, page)
    sub = np.zeros(img.shape, bool)
    x0, y0, x1, y1 = box
    sub[y0:y1, x0:x1] = True
    ink = (img < thresh) & sub
    if ax is None:
        ax = calibrate(img, vrules, hrules, xlog, ylog, search=search, skip=skip)
        xs, ys = [v for v, _ in vrules], [v for v, _ in hrules]
        ink &= ~rule_mask(img.shape, ax, xs, ys, xr=(xs[0], xs[-1]), yr=(ys[0], ys[-1]), width=rule_width)
    for a, b, c, d in masks:
        ink[b:d, a:c] = False
    paths, rows = [], []
    for name, g in guides.items():
        c, r, frac = snap(ink, g, tol=tol, smooth=smooth)
        x, y = ax.data(c, r)
        paths.append((c, r))
        if name in flat:
            x, y = np.array([x.min(), x.max()]), np.full(2, np.median(y))
        elif keep and name in keep:
            k = (x >= keep[name][0]) & (x <= keep[name][1])
            x, y = x[k], y[k]
        print(f"{name}: {frac:.0%} of samples on ink, x {x.min():.4g} to {x.max():.4g}")
        step = 1 if x.size <= 2 else every
        rows += [f"{name},{a:.5g},{b:.5g}" for a, b in zip(x[::step], y[::step])]
    overlay_paths(img, box, paths, str(CACHE / f"{Path(here).name}_overlay.png"), guides.values())
    (Path(here) / "trace.csv").write_text(f"# {header}; curve, x, y\n" + "\n".join(rows) + "\n")
    return ax


def tick_axes(img, frame, xticks, yticks, xlog=False, ylog=False, inside=25):
    """AffineAxes for a framed plot with tick marks but no grid. frame = (left col, bottom row, right col) guesses;
    xticks = [(x_value, col_guess)] on the bottom edge, first and last at the left and right frame edges;
    yticks = [(y_value, row_guess, side)], side 'l' or 'r', first one the bottom edge. Each tick is refined on the
    ink: the tick mark gives its own coordinate, the frame edge the other one."""
    left, bottom, right = frame
    y_bottom, x_edge = yticks[0][0], {"l": xticks[0][0], "r": xticks[-1][0]}
    pix, data = [], []
    for xv, cg in xticks:
        c = rule_center(img, cg, bottom - inside // 2 - 4, False, half=inside // 2 - 4, search=12)
        if not np.isfinite(c):
            print(f"tick_axes: x tick {xv} not found, skipped")
            continue
        r = rule_center(img, c + (20 if c < right - 30 else -20), bottom, True, half=8, search=12)
        pix.append((c, r))
        data.append((xv, y_bottom))
    for yv, rg, sd in yticks[1:]:
        edge = {"l": left, "r": right}[sd]
        r = rule_center(img, edge + (inside // 2 + 4) * (1 if sd == "l" else -1), rg, True, half=inside // 2 - 4, search=12)
        if not np.isfinite(r):
            print(f"tick_axes: y tick {yv} ({sd}) not found, skipped")
            continue
        c = rule_center(img, edge, r + 20, False, half=8, search=12)
        pix.append((c, r))
        data.append((x_edge[sd], yv))
    ax = AffineAxes(pix, data, xlog, ylog)
    print(f"tick_axes: {len(pix)} ticks, max residual x {ax.resid[0]:.4g}, y {ax.resid[1]:.4g} (data units)")
    return ax
