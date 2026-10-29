"""Shared helpers for the MIL-HDBK-141 OptiLand lens drawings.

All systems are entered in millimetres (the book's cm values x 10) at the d line, 587.6 nm.
Run each <name>/<name>_system.py with `env -u PYTHONPATH python` (a foreign venv on PYTHONPATH
shadows this interpreter's numpy).
"""
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from optiland.materials import AbbeMaterial  # noqa: E402

warnings.filterwarnings("ignore", category=FutureWarning)

D_LINE = 0.5876


def glass(nd, vd):
    """Glass from n_d and V_d (Buchdahl dispersion model)."""
    return AbbeMaterial(n=nd, abbe=vd, model="buchdahl")


def code(c):
    """Glass from a 6-digit code: 517645 -> n_d 1.517, V_d 64.5."""
    c = str(c)
    return glass(1 + int(c[:3]) / 1000, int(c[3:]) / 10)


def petzval(o):
    """Petzval sum  sum c (n' - n)/(n n')  over the refracting surfaces, in 1/mm."""
    r = np.asarray(o.surfaces.radii, dtype=float).ravel()
    n = np.asarray(o.surfaces.n(D_LINE), dtype=float).ravel()
    return sum((n[k] - n[k - 1]) / (r[k] * n[k] * n[k - 1]) for k in range(1, len(r)) if np.isfinite(r[k]) and n[k] != n[k - 1])


def rays(o, y, u, z=None):
    """Paraxial trace of one ray (height y, slope u) from z mm before surface 1: per-surface (y, u)."""
    z = -1.0 if z is None else z
    ys, us = o.paraxial.trace_generic(y, u, z, D_LINE)
    return np.asarray(ys, dtype=float).ravel(), np.asarray(us, dtype=float).ravel()


def save_layout(o, path, title, **kw):
    fig, ax = o.draw(title=title, figsize=kw.pop("figsize", (10, 4)), **kw)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------------------------
# Book-quality drawing (see BOOK_QUALITY_RECIPE.md). Geometry comes from the OptiLand prescription
# (radii, vertex positions), ray paths from OptiLand's real-ray trace; everything visual is set here
# so every figure in the edition looks the same: B/W line art at final print size, no axes, no grid.
# ---------------------------------------------------------------------------------------------
TEXT_WIDTH = 6.5        # in, the PDF's text block (letter, 1 in margins)
DPI = 600               # line-art print resolution for the PNG; the PDF beside it is vector

BOOK_RC = {
    "font.family": "serif",
    "font.serif": ["Latin Modern Roman", "CMU Serif", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "font.size": 8,
    "axes.unicode_minus": False,
    "axes.grid": False,
    "savefig.dpi": DPI,
    "pdf.fonttype": 42,
}
INK = "black"
LENS = dict(facecolor="0.92", edgecolor=INK, linewidth=0.6, joinstyle="miter", zorder=2)
MEDIUM = dict(facecolor="0.97", edgecolor=INK, linewidth=0.4, zorder=1)     # cover glass, oil, slabs
AXIS = dict(color="0.45", linewidth=0.35, dashes=(8, 2, 1.5, 2), zorder=0)  # centre line
AXIAL = dict(color=INK, linewidth=0.55, zorder=3)                             # axial (marginal) rays
CHIEF = dict(color=INK, linewidth=0.55, dashes=(4, 2), zorder=3)              # chief ray
OFFAXIS = dict(color="0.55", linewidth=0.4, zorder=2.5)                       # rest of the field bundle
LEADER = dict(color=INK, linewidth=0.35)


def book_axes(width, xlim, ylim, margin=(0.05, 0.05)):
    """A frameless, true-scale axis sized so 1 mm in z and y print the same length."""
    plt.rcParams.update(BOOK_RC)
    (x0, x1), (y0, y1) = xlim, ylim
    height = width * (y1 - y0) / (x1 - x0)
    fig = plt.figure(figsize=(width + 2 * margin[0], height + 2 * margin[1]))
    ax = fig.add_axes((margin[0] / fig.get_figwidth(), margin[1] / fig.get_figheight(),
                       width / fig.get_figwidth(), height / fig.get_figheight()))
    _frameless(ax, xlim, ylim)
    return fig, ax


def broken_axes(width, segments, ylim, gap=0.18, margin=(0.05, 0.05)):
    """Side-by-side true-scale panels with one shared scale, for long systems (a microscope tube):
    each (z0, z1) segment keeps its real length, the empty stretches between them are cut out and
    marked with break lines. Returns fig, [axes]."""
    plt.rcParams.update(BOOK_RC)
    spans = [z1 - z0 for z0, z1 in segments]
    scale = (width - gap * (len(segments) - 1)) / sum(spans)          # in per mm
    height = scale * (ylim[1] - ylim[0])
    fig = plt.figure(figsize=(width + 2 * margin[0], height + 2 * margin[1]))
    W, H = fig.get_figwidth(), fig.get_figheight()
    axes, x = [], margin[0]
    for seg, span in zip(segments, spans):
        ax = fig.add_axes((x / W, margin[1] / H, span * scale / W, height / H))
        _frameless(ax, seg, ylim)
        axes.append(ax)
        x += span * scale + gap
    for a, b in zip(axes, axes[1:]):                                   # break marks across the gap
        xa, xb = a.get_position().x1, b.get_position().x0
        for yf in (0.12, 0.88):
            for xc in (xa + 0.25 * (xb - xa), xa + 0.75 * (xb - xa)):
                fig.add_artist(plt.Line2D([xc - 0.012, xc + 0.012], [yf - 0.08, yf + 0.08],
                                          transform=fig.transFigure, color=INK, linewidth=0.5))
        mid = margin[1] / H + height / H * (0 - ylim[0]) / (ylim[1] - ylim[0])
        fig.add_artist(plt.Line2D([xa, xb], [mid, mid], transform=fig.transFigure,
                                  **{k: v for k, v in AXIS.items() if k != "zorder"}))
    return fig, axes


def _frameless(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_axis_off()
    ax.axhline(0, **AXIS)


def trace(o, hy, py, wl=D_LINE):
    """Real-ray meridional fan: hy = normalized field, py = pupil coordinates. Returns z, y arrays
    of shape (n_surfaces, n_rays) in global mm; failed rays are NaN."""
    o.trace_generic(0.0, float(hy), 0.0, np.asarray(py, dtype=float), wl)
    return np.asarray(o.surfaces.z, dtype=float).copy(), np.asarray(o.surfaces.y, dtype=float).copy()


def draw_rays(axes, z, y, style, first=0, last=None, arrow_at=None, reverse=False):
    """Polylines through surfaces first..last. arrow_at = z where a small direction arrowhead goes
    (pointing toward -z when reverse, for light that travels right to left, as in an eyepiece)."""
    sl = slice(first, None if last is None else last + 1)
    for ax in np.atleast_1d(axes):
        for k in range(z.shape[1]):
            zk, yk = z[sl, k], y[sl, k]
            ok = np.isfinite(zk) & np.isfinite(yk)
            ax.plot(zk[ok], yk[ok], solid_capstyle="butt", **style)
            if arrow_at is not None and zk[ok][0] < arrow_at < zk[ok][-1]:
                ya = np.interp(arrow_at, zk[ok], yk[ok])
                yb = np.interp(arrow_at + 1e-3, zk[ok], yk[ok])
                tip, tail = ((arrow_at, ya), (arrow_at + 1e-3, yb)) if reverse else ((arrow_at + 1e-3, yb), (arrow_at, ya))
                ax.annotate("", tip, tail,
                            arrowprops=dict(arrowstyle="-|>,head_length=0.35,head_width=0.14",
                                            color=style.get("color", INK), linewidth=0, shrinkA=0, shrinkB=0))


def sag(r, h):
    """Sag of a spherical surface of radius r (inf = plane) at heights h."""
    if not np.isfinite(r):
        return np.zeros_like(h)
    c = 1.0 / r
    return c * h ** 2 / (1 + np.sqrt(np.clip(1 - (c * h) ** 2, 0, None)))


def clear_apertures(o, fans, pad=1.06, extra=0.0):
    """Per-surface semi-aperture from traced fans (list of y arrays): max |y| x pad + extra,
    never more than 0.99 |R| so a hemisphere stays a hemisphere."""
    ymax = np.nanmax(np.abs(np.hstack(fans)), axis=1) * pad + extra
    r = np.abs(np.asarray(o.surfaces.radii, dtype=float).ravel())
    return np.minimum(ymax, np.where(np.isfinite(r), 0.99 * r, np.inf))


def elements(o, first, last):
    """Glass elements between surfaces first..last as lists of surface indices; cemented groups
    (glass on both sides of a surface) come back as one group: [[2, 3], [5, 6, 7], ...]."""
    n = np.asarray(o.surfaces.n(D_LINE), dtype=float).ravel()       # n[k]: index after surface k
    groups, cur = [], []
    for k in range(first, last):
        if n[k] > 1.0001:
            cur = cur or [k]
            cur.append(k + 1)
        elif cur:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    return groups


def draw_lenses(axes, o, first, last, semi):
    """Every glass element from surface first to last, as filled sections with flat edges.
    A cemented group shares one diameter. Returns {surface: (z_edge, h_edge)} for labelling."""
    z0 = np.asarray(o.surfaces.positions, dtype=float).ravel()
    r = np.asarray(o.surfaces.radii, dtype=float).ravel()
    edges = {}
    for grp in elements(o, first, last):
        H = max(semi[s] for s in grp)
        prof = {}
        for s in grp:
            h_s = min(H, 0.99 * abs(r[s])) if np.isfinite(r[s]) else H
            h = np.linspace(-h_s, h_s, 121)
            zs = z0[s] + sag(r[s], h)
            if h_s < H:                                                # flat step out to the rim
                zs = np.r_[zs[0], zs, zs[-1]]
                h = np.r_[-H, h, H]
            prof[s] = (zs, h)
            edges[s] = (zs[-1], H)
        for a, b in zip(grp, grp[1:]):
            (za, ha), (zb, hb) = prof[a], prof[b]
            xy = np.column_stack([np.r_[za, zb[::-1]], np.r_[ha, hb[::-1]]])
            for ax in np.atleast_1d(axes):
                ax.add_patch(plt.Polygon(xy, closed=True, **LENS))
    return edges


def draw_slab(ax, z0, z1, h, **style):
    ax.add_patch(plt.Rectangle((z0, -h), z1 - z0, 2 * h, **{**MEDIUM, **style}))


def number_surfaces(ax, edges, y, min_sep, size=6.5, numbers=None):
    """Surface numbers in one row at height y, spread to min_sep (mm) so none collide, each tied
    to its surface's upper rim by a hairline leader. edges: {surface: (z_rim, h_rim)}."""
    keys = sorted(edges, key=lambda s: edges[s][0])
    want = np.array([edges[s][0] for s in keys])
    x = want.copy()
    for _ in range(200):                                              # relax pairwise overlaps
        moved = False
        for i in range(len(x) - 1):
            d = x[i + 1] - x[i]
            if d < min_sep:
                x[i] -= (min_sep - d) / 2
                x[i + 1] += (min_sep - d) / 2
                moved = True
        if not moved:
            break
    for s, xi in zip(keys, x):
        zr, hr = edges[s]
        lab = str(s if numbers is None else numbers[s])
        ax.plot([zr, zr, xi], [hr, hr + 0.35 * (y - hr), y - 0.15 * (y - hr)], **LEADER)
        ax.text(xi, y, lab, ha="center", va="bottom", fontsize=size)


def label(ax, text, xy, xytext, ha="center", va="center", **kw):
    """A component label with a hairline leader to the thing it names (no arrowhead)."""
    ax.annotate(text, xy, xytext, ha=ha, va=va, arrowprops=dict(arrowstyle="-", shrinkA=1.5,
                shrinkB=0, **LEADER), **kw)


def scale_bar(ax, z, y, length, text=None):
    """A true-scale bar (the drawing has no axes)."""
    ax.plot([z, z + length], [y, y], color=INK, linewidth=0.8, solid_capstyle="butt")
    for zz in (z, z + length):
        ax.plot([zz, zz], [y - 0.04 * length, y + 0.04 * length], color=INK, linewidth=0.5)
    ax.text(z + length / 2, y - 0.12 * length, text or f"{length:g} mm", ha="center", va="top")


def stop_bars(ax, z, inner, outer, width=1.4):
    """A diaphragm: two short thick bars at +-inner..outer (the aperture lies between them)."""
    for s in (1, -1):
        ax.plot([z, z], [s * inner, s * outer], color=INK, linewidth=width, solid_capstyle="butt")


def dimension(ax, z0, z1, y, text, ext=(), gap=0.5, **kw):
    """A dimension line with small arrowheads and its text centred below. ext: [(z, y_from)] extension
    lines running from the feature at (z, y_from) down to the dimension line."""
    for ze, ye in ext:
        ax.plot([ze, ze], [ye, y - 0.3], **LEADER)
    ax.annotate("", (z1, y), (z0, y), arrowprops=dict(arrowstyle="<|-|>,head_length=0.35,head_width=0.14",
                color=INK, linewidth=0.4, shrinkA=0, shrinkB=0))
    ax.text((z0 + z1) / 2, y - gap, text, ha="center", va="top", **kw)


def thin_lens(ax, z, h, lw=0.7):
    """Ideal positive thin lens, drawn as a plane with outward arrowheads at both ends."""
    ax.plot([z, z], [-h, h], color=INK, linewidth=lw, solid_capstyle="butt", zorder=2)
    for s in (1, -1):
        ax.annotate("", (z, s * h), (z, s * 0.95 * h), arrowprops=dict(
            arrowstyle="-|>,head_length=0.55,head_width=0.2", color=INK, linewidth=0, shrinkA=0, shrinkB=0))


def save_book(fig, path):
    """Vector PDF (for the book) + 600 dpi PNG (for review), both cropped tight."""
    path = Path(path)
    for ext in (".pdf", ".png"):
        fig.savefig(path.with_suffix(ext), bbox_inches="tight", pad_inches=0.02, facecolor="white")
    plt.close(fig)


def write_readme(path, lines):
    Path(path).write_text("\n".join(lines) + "\n")


def row(name, book, trace, unit="", fmt="{:.3f}"):
    """One comparison line: book vs OptiLand, with the difference."""
    b = fmt.format(book) if isinstance(book, (int, float)) else book
    t = fmt.format(trace)
    d = f" (diff {trace - book:+.3g}{unit})" if isinstance(book, (int, float)) else ""
    return f"{name} book {b}{unit} / OptiLand {t}{unit}{d}"


def ch14_eyepiece(rows, exit_pupil_cm, name):
    """A ch14 eyepiece in the book's own orientation (Section 14.2.1): parallel light enters through
    the exit pupil (the stop, 5 mm), rows are (c [1/cm], t [cm] after the surface, glass code or None)
    listed from the eye side, and the last t runs to the field stop. Fields 0/10/15 deg as in the
    book's aberration plots."""
    import optiland.backend as be
    from optiland import optic

    o = optic.Optic(name=name)
    o.surfaces.add(index=0, radius=be.inf, thickness=be.inf)
    o.surfaces.add(index=1, radius=be.inf, thickness=exit_pupil_cm * 10, is_stop=True, comment="exit pupil")
    for k, (c, t, g) in enumerate(rows, start=2):
        o.surfaces.add(index=k, radius=be.inf if c == 0 else 10 / c, thickness=t * 10,
                       material=code(g) if g else "air")
    o.surfaces.add(index=len(rows) + 2, comment="field stop")
    o.set_aperture(aperture_type="EPD", value=5.0)
    o.fields.set_type(field_type="angle")
    for f in (0, 10, 15):
        o.fields.add(y=f)
    o.wavelengths.add(value=D_LINE, is_primary=True)
    return o


def draw_ch14_eyepiece(o, path, ray_last, pupil, stop, width=4.8, field_name="center"):
    """A ch14 eyepiece (built by ch14_eyepiece) in the book's orientation: exit pupil left, objective
    right, light travelling toward the eye. Axial pair plus the 15 deg chief ray (the book's maximum
    field), lenses numbered by OptiLand surface (1 = exit pupil, 2-5 lenses, 6 = field stop).
    ray_last: last surface the rays are drawn to (the Huygenian's virtual-focus stop lies before the
    field lens, so its rays end at 5). pupil/stop: (text, surface a, surface b), the distances the
    book prints for the figure, between those two surfaces' vertices (the stop's z is its plane)."""
    pos = np.asarray(o.surfaces.positions, dtype=float).ravel()
    za, ya = trace(o, 0.0, [-1, 1])
    zc, yc = trace(o, 1.0, [0.0])
    zo, yo = trace(o, 1.0, [-1, 1])
    semi = clear_apertures(o, [ya, yc, yo], pad=1.06, extra=0.15)
    top = semi[2:6].max()
    z_stop = pos[6]
    r_stop = yc[6, 0] if ray_last == 6 else np.interp(z_stop, zc[1:ray_last + 1, 0], yc[1:ray_last + 1, 0])
    r_pupil = float(np.max(np.abs(ya[1])))
    x0, x1 = za[0, 0] - 0.2, max(pos[5], z_stop) + 0.9
    pt = (x1 - x0) / (width * 72)                                    # mm per printed point
    y_num, y_dim, y_name = top + 8 * pt, -top - 12 * pt, -top - 34 * pt
    fig, ax = book_axes(width, (x0, x1), (y_name - 24 * pt, y_num + 12 * pt))
    edges = draw_lenses(ax, o, 2, 5, semi)
    draw_rays(ax, za, ya, AXIAL, first=0, last=ray_last, arrow_at=(pos[3] + pos[4]) / 2, reverse=True)
    draw_rays(ax, zc, yc, CHIEF, first=0, last=ray_last, arrow_at=(pos[3] + pos[4]) / 2, reverse=True)
    out = 0.8 * semi[2]
    out_stop = max(1.0, min(out, top - r_stop))                      # field-stop bars stay inside the lens height
    stop_bars(ax, 0.0, r_pupil, r_pupil + out)
    stop_bars(ax, z_stop, r_stop, r_stop + out_stop)
    edges[1] = (0.0, r_pupil + out)
    edges[6] = (z_stop, r_stop + out_stop)
    number_surfaces(ax, edges, y_num, min_sep=3.2 * (x1 - x0) / 40)
    for (text, a, b) in (pupil, stop):
        za_, zb_ = (0.0 if a == 1 else pos[a]), (z_stop if b == 6 else pos[b])
        dimension(ax, za_, zb_, y_dim, text, size=6.5, gap=3 * pt,
                  ext=[(za_, -(r_pupil + out) if a == 1 else -edges[a][1]), (zb_, -(r_stop + out_stop) if b == 6 else -edges[b][1])])
    mid = lambda s: np.mean([edges[k][0] for k in s])
    groups = elements(o, 2, 5)
    for grp, name in zip(groups, ("eye lens", "field lens")):
        zl = mid(grp) if (name == "eye lens" or field_name == "center") else edges[grp[0]][0] + 0.15
        ax.plot([zl] * 2, [-edges[grp[0]][1], y_name + 5 * pt], **LEADER)
        ax.text(zl + (0.3 if zl != mid(grp) else 0), y_name, name, ha="center" if zl == mid(grp) else "right", va="top")
    ax.plot([0, 0], [y_dim, y_name + 5 * pt], **LEADER)
    ax.text(0.3, y_name, "exit pupil\n(eyepoint)", ha="right", va="top", linespacing=1.1)
    ax.plot([z_stop] * 2, [y_dim, y_name + 5 * pt], **LEADER)
    ax.text(z_stop + 0.3, y_name, "field stop", ha="right", va="top")
    zk, yk = pos[3] + 3.0, -r_pupil - 10 * pt
    for k, (name, style) in enumerate((("axial ray", AXIAL), ("chief ray, 15\u00b0", CHIEF))):
        ax.plot([zk, zk + 28 * pt], [yk - k * 11 * pt] * 2, **style)
        ax.text(zk + 33 * pt, yk - k * 11 * pt, name, va="center")
    ax.text(zk, yk - 2 * 11 * pt, "distances in cm", va="center")
    scale_bar(ax, (x0 + x1) / 2, y_name - 4 * pt, 5.0)
    save_book(fig, path)
