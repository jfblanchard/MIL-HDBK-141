"""Drawing kit for the construction schematics (interferometers, test benches, illuminators).

These figures have no lens prescription in the book: they are layouts of ideal elements (thin lenses,
plane/spherical mirrors, plates, splitters) at the geometry the figure defines. Rays are computed
from that geometry; the look comes from common.py (BOOK_RC, AXIAL/CHIEF/OFFAXIS styles, LENS/MEDIUM
fills, thin_lens, stop_bars, scale conventions). Units are arbitrary drawing units ("du"); aspect is 1:1.
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from common import (AXIAL, CHIEF, INK, LEADER, LENS, MEDIUM, OFFAXIS, TEXT_WIDTH, book_axes,  # noqa: E402,F401
                    label, save_book, stop_bars, thin_lens, write_readme)

DASH = dict(color=INK, linewidth=0.45, dashes=(4, 2), zorder=2.5)       # virtual rays, construction lines
THIN = dict(color=INK, linewidth=0.4, zorder=2)                          # dimension / construction hairlines
SOLID = dict(color=INK, linewidth=0.55, zorder=3)
ARROW = "-|>,head_length=0.35,head_width=0.14"


def canvas(width, xlim, ylim):
    """Frameless 1:1 axes with no centre line; ax.pt = drawing units per printed point."""
    fig, ax = book_axes(width, xlim, ylim)
    plt.rcParams["hatch.linewidth"] = 0.3
    ax.lines[0].remove()
    ax.pt = (xlim[1] - xlim[0]) / (width * 72)
    return fig, ax


def P(*a):
    return np.array(a, dtype=float)


def unit(v):
    v = np.asarray(v, dtype=float)
    return v / np.hypot(*v)


def rot(v, deg):
    c, s = np.cos(np.radians(deg)), np.sin(np.radians(deg))
    return np.array([c * v[0] - s * v[1], s * v[0] + c * v[1]])


def head(ax, p, d, style, size=1.0):
    """Small arrowhead at p pointing along d."""
    d = unit(d)
    ax.annotate("", p + d * 1e-3, p, arrowprops=dict(arrowstyle=ARROW.replace("0.35", f"{0.35 * size}").replace("0.14", f"{0.14 * size}"),
                color=style.get("color", INK), linewidth=0, shrinkA=0, shrinkB=0))


def ray(ax, pts, style=AXIAL, arrows=(0.5,), segs=None):
    """Polyline through pts. arrows: fractions of total length at which one arrowhead sits (in the
    direction of travel). segs: restrict arrows to these segment indices (default: any)."""
    pts = [np.asarray(p, dtype=float) for p in pts]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], solid_capstyle="butt", **style)
    L = np.array([np.hypot(*(b - a)) for a, b in zip(pts, pts[1:])])
    cum = np.r_[0, np.cumsum(L)]
    for f in arrows:
        s = f * cum[-1]
        k = min(np.searchsorted(cum, s, side="right") - 1, len(L) - 1)
        if segs is not None and k not in segs:
            continue
        t = (s - cum[k]) / L[k]
        head(ax, pts[k] + t * (pts[k + 1] - pts[k]), pts[k + 1] - pts[k], style)


def reflect(d, n):
    n = unit(n)
    return d - 2 * np.dot(d, n) * n


def hit(p, d, a, b):
    """Point where the ray p + t d meets segment line a-b (t > 0), or None."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    m = np.array([d, a - b]).T
    if abs(np.linalg.det(m)) < 1e-12:
        return None
    t, s = np.linalg.solve(m, a - p)
    return p + t * d if t > 1e-9 else None


def hit_x(p, d, x):
    """Point where the ray p + t d reaches the vertical line X = x."""
    return p + (x - p[0]) / d[0] * d


def line(ax, a, b, style=THIN, **kw):
    ax.plot([a[0], b[0]], [a[1], b[1]], **{**style, **kw})


def dash(ax, a, b, **kw):
    line(ax, a, b, DASH, **kw)


def axis_line(ax, a, b):
    from common import AXIS
    line(ax, a, b, AXIS)


def text(ax, s, xy, ha="center", va="center", size=8, **kw):
    ax.text(xy[0], xy[1], s, ha=ha, va=va, fontsize=size, **kw)


def lab(ax, s, xy, xytext, ha="center", va="center", **kw):
    label(ax, s, xy, xytext, ha=ha, va=va, **kw)


def mirror(ax, a, b, side=1, tick=None, lw=1.0, ticks=True):
    """A reflecting surface a-b, hatched on the back (side = +1 left of a->b, -1 right)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    line(ax, a, b, color=INK, linewidth=lw, solid_capstyle="butt", zorder=3)
    if not ticks:
        return
    L = np.hypot(*(b - a))
    tick = tick or 0.06 * L
    d = unit(b - a)
    n = side * np.array([-d[1], d[0]])
    for t in np.linspace(0.04, 0.96, max(int(L / (tick * 0.9)), 4)):
        p = a + t * (b - a)
        line(ax, p, p + (n + d) * tick * 0.7, color=INK, linewidth=0.3)


def spherical_mirror(ax, c, R, ang0, ang1, side=1, tick=None, lw=1.0):
    """Arc of radius R about centre c from ang0 to ang1 (deg), hatched on the outside (side=+1)."""
    th = np.radians(np.linspace(ang0, ang1, 80))
    pts = np.column_stack([c[0] + R * np.cos(th), c[1] + R * np.sin(th)])
    ax.plot(pts[:, 0], pts[:, 1], color=INK, linewidth=lw, solid_capstyle="butt", zorder=3)
    tick = tick or 0.08 * R
    for t in np.radians(np.linspace(ang0, ang1, 14)[1:-1]):
        r = np.array([np.cos(t), np.sin(t)])
        p = c + R * r
        tang = np.array([-r[1], r[0]])
        line(ax, p, p + side * r * tick + tang * tick * 0.5, color=INK, linewidth=0.3)


def plate(ax, c, length, thick, ang, fill=True, **style):
    """A flat plate (rectangle) of the given length, centred at c, long side at angle ang (deg)."""
    d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    n = np.array([-d[1], d[0]])
    h, t = length / 2, thick / 2
    xy = np.array([c - h * d - t * n, c + h * d - t * n, c + h * d + t * n, c - h * d + t * n])
    ax.add_patch(plt.Polygon(xy, closed=True, **{**(MEDIUM if fill else dict(fill=False, edgecolor=INK, linewidth=0.5, zorder=2)),
                                                  **style}))


def splitter(ax, c, length, ang=45, thick=None):
    """A half-silvered plate: glass outline plus a heavier line on its front face."""
    thick = thick or 0.06 * length
    plate(ax, c, length, thick, ang, **LENS)
    d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    line(ax, c - d * length / 2, c + d * length / 2, color=INK, linewidth=0.9, zorder=3, dashes=(5, 1.2))


def tlens(ax, c, h, ang=90.0, lw=0.7):
    """Ideal thin lens at c, plane at angle ang (deg, 90 = vertical), outward arrowheads."""
    d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    line(ax, c - h * d, c + h * d, color=INK, linewidth=lw, solid_capstyle="butt", zorder=2)
    for s in (1, -1):
        ax.annotate("", c + s * h * d, c + s * 0.93 * h * d, arrowprops=dict(
            arrowstyle="-|>,head_length=0.55,head_width=0.2", color=INK, linewidth=0, shrinkA=0, shrinkB=0))


def biconvex(ax, z, h, t, R, vertical=False, **style):
    """Real thin biconvex lens section (axis along x, or y when vertical)."""
    y = np.linspace(-h, h, 61)
    s = R - np.sqrt(R ** 2 - y ** 2)
    xs = np.r_[z - t / 2 + s, (z + t / 2 - s)[::-1]]
    ys = np.r_[y, y[::-1]]
    xy = np.column_stack([ys, xs]) if vertical else np.column_stack([xs, ys])
    ax.add_patch(plt.Polygon(xy, closed=True, **{**LENS, **style}))


def dot(ax, p, r=0.012, **kw):
    ax.plot([p[0]], [p[1]], "o", color=INK, markersize=kw.pop("ms", 2.6), zorder=4, **kw)


def arc(ax, c, r, a0, a1, s=None, rt=1.35, size=7, both=False, **kw):
    th = np.radians(np.linspace(a0, a1, 40))
    ax.plot(c[0] + r * np.cos(th), c[1] + r * np.sin(th), **{**THIN, **kw})
    if both:
        for a, b in ((a1, a1 - 1), (a0, a0 + 1)):
            head(ax, c + r * np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]),
                 r * (np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]) - np.array([np.cos(np.radians(b)), np.sin(np.radians(b))])), THIN, 0.8)
    if s:
        m = np.radians((a0 + a1) / 2)
        ax.text(c[0] + rt * r * np.cos(m), c[1] + rt * r * np.sin(m), s, ha="center", va="center", fontsize=size)


def dim(ax, a, b, s, off=0.0, size=7, side=1, ext=True, tpos=0.5):
    """Dimension line between a and b, shifted off (du) to its left (side=+1) / right, text centred."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = unit(b - a)
    n = side * np.array([-d[1], d[0]])
    a2, b2 = a + n * off, b + n * off
    if ext and off:
        line(ax, a + n * 0.15 * np.sign(off), a2 + n * 0.3 * np.sign(off), **THIN)
        line(ax, b + n * 0.15 * np.sign(off), b2 + n * 0.3 * np.sign(off), **THIN)
    ax.annotate("", b2, a2, arrowprops=dict(arrowstyle="<|-|>,head_length=0.35,head_width=0.14",
                color=INK, linewidth=0.4, shrinkA=0, shrinkB=0))
    m = a2 + tpos * (b2 - a2)
    if s:
        ax.text(m[0], m[1], s, ha="center", va="center", fontsize=size,
                bbox=dict(facecolor="white", edgecolor="none", pad=0.6))


def eye(ax, p, ang=0.0, s=1.0):
    """A small schematic eye whose front vertex is at p, looking along ang (deg): globe, cornea, iris."""
    d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    n = np.array([-d[1], d[0]])
    th = np.linspace(0, 2 * np.pi, 120)
    c = p - d * s
    ax.plot(c[0] + s * np.cos(th), c[1] + s * np.sin(th), color=INK, linewidth=0.5, zorder=4)
    ct = np.linspace(-0.55, 0.55, 20)
    cc = p - d * 0.45 * s
    ax.plot(cc[0] + 0.45 * s * (np.cos(ct) * d[0] - np.sin(ct) * n[0]) * 1.0 + 0.0,
            cc[1] + 0.45 * s * (np.cos(ct) * d[1] - np.sin(ct) * n[1]), color=INK, linewidth=0.5, zorder=4)
    for sgn in (1, -1):
        line(ax, p - d * 0.35 * s + sgn * n * 0.18 * s, p - d * 0.35 * s + sgn * n * 0.42 * s, color=INK, linewidth=1.2, zorder=4)


def hatch_block(ax, x0, y0, x1, y1, hatch="//////", **kw):
    """A hatched rectangle (mechanical support, table top, black felt)."""
    ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, hatch=hatch, edgecolor=INK,
                               linewidth=0.5, zorder=1, **kw))


def lamp_housing(ax, c, w=8.0, ang=0.0):
    """Reflector R (back arc), lamp L (dot) and ground glass G (dotted line) for a lamp whose beam goes
    along ang (deg). c is the lamp position."""
    d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    n = np.array([-d[1], d[0]])
    th = np.radians(np.linspace(-70, 70, 40))
    pts = c[None, :] + (-w * 0.1 - w * 0.9 * np.cos(th))[:, None] * d[None, :] + (w * 0.9 * np.sin(th))[:, None] * n[None, :]
    ax.plot(pts[:, 0], pts[:, 1], color=INK, linewidth=1.0, zorder=3)
    ax.plot([c[0]], [c[1]], "o", color=INK, markersize=3.2, zorder=4)
    g0, g1 = c + d * w * 0.9 - n * w * 0.8, c + d * w * 0.9 + n * w * 0.8
    line(ax, g0, g1, color=INK, linewidth=0.9, dashes=(1.5, 1.2), zorder=3)
    return c + d * w * 0.9


def tg_common(ax, c0, w=3.0, ref_y=30.0, view_y=-20.0, x_src=0.0, x_col=14.0, ref_half=8.0):
    """The part every Twyman-Green layout shares: pinhole source, collimator, 45 degree splitter at c0,
    flat reference mirror above (reference arm out and back), viewing lens and eye below. Beam drawn by
    two edge rays (outbound arrows on the +w ray, return arrows on the -w ray). Returns the splitter point."""
    c0 = np.asarray(c0, float)
    for s in (1, -1):
        line(ax, P(x_src, s * 0.5), P(x_src, s * 6), color=INK, linewidth=1.8, solid_capstyle="butt")
    dot(ax, P(x_src, 0), ms=2)
    tlens(ax, P(x_col, 0), 6.5, 90)
    splitter(ax, c0, 14, 45)
    mirror(ax, P(c0[0] - ref_half, ref_y), P(c0[0] + ref_half, ref_y), side=1, lw=1.3)
    tlens(ax, P(c0[0], view_y), 6.5, 0)
    eye(ax, P(c0[0], view_y - 9.5), 90, 1.8)
    for yy, o in ((w, True), (-w, False)):
        xh = c0[0] + yy
        ray(ax, [P(x_src, 0), P(x_col, yy)], AXIAL, arrows=(0.5,)) if o else ray(ax, [P(x_src, 0), P(x_col, yy)], AXIAL, arrows=(0.5,))
        ray(ax, [P(x_col, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if o else ())
        ref = [P(xh, yy), P(xh, ref_y)]
        ray(ax, ref, AXIAL, arrows=(0.5,) if o else ())
        ray(ax, ref[::-1], AXIAL, arrows=() if o else (0.5,))
        ray(ax, [P(xh, yy), P(xh, view_y), P(c0[0], view_y - 8.0)], AXIAL, arrows=(0.4,))
    return c0


def readme(here, title, flag=None, lines=()):
    out = [f"# {title}", ""]
    if flag:
        out += [f"**{flag}**", ""]
    out += list(lines)
    write_readme(Path(here) / "README.md", out)


def done(fig, here):
    save_book(fig, Path(here) / Path(here).name)
