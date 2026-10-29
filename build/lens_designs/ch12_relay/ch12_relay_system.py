"""ch12 lens relay systems (Figures 12.1 and 12.2), drawn and re-traced in OptiLand as FIRST-ORDER systems.

ch12 gives no glass prescription: the relay "lenses" are unspecified telescope doublets. What it does
give is first-order data, and that is what is modelled here with ideal thin (paraxial) lenses:
  single relay (12.3.3): two f = 35 cm doublets with parallel light between them, D = 70 cm,
    u_o = 0.14, lens diameter about 10 cm, magnification -1;
  double relay (12.6): same D and u_o, relays of half the focal length, a field lens f = D/8 at the
    intermediate image, all lenses limited to 5 cm.
The field is the Erfle eyepiece's object height of 1.32 cm (12.6.6), i.e. +-6.6 mm.
"""
import sys
from pathlib import Path

import matplotlib.patches
import numpy as np
from optiland import optic

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from common import (AXIAL, CHIEF, D_LINE, INK, LEADER, TEXT_WIDTH, book_axes, dimension, draw_rays,  # noqa: E402
                    number_surfaces, rays, row, save_book, scale_bar, thin_lens, trace, write_readme)

D, U0, H = 700.0, 0.14, 6.6


def relay(lenses, name, stop):
    """lenses: [(z, f)] along 0..D; object at z = 0, image surface at z = D."""
    o = optic.Optic(name=name)
    o.surfaces.add(index=0, thickness=lenses[0][0])
    for k, (z, f) in enumerate(lenses, start=1):
        nxt = lenses[k][0] if k < len(lenses) else D
        o.surfaces.add(index=k, surface_type="paraxial", f=f, thickness=nxt - z, is_stop=(k == stop))
    o.surfaces.add(index=len(lenses) + 1)
    o.set_aperture(aperture_type="objectNA", value=U0)
    o.fields.set_type(field_type="object_height")
    for h in (0.0, H / 2, H):
        o.fields.add(y=h)
    o.wavelengths.add(value=D_LINE, is_primary=True)
    return o


def single():
    return relay([(350.0, 350.0), (350.0 + 1e-6, 350.0)], "single relay, MIL-HDBK-141 Fig 12.1", stop=1)


def double():
    f = 175.0
    return relay([(175.0, f), (175.0 + 1e-6, f), (350.0, D / 8), (525.0, f), (525.0 + 1e-6, f)],
                 "double relay, MIL-HDBK-141 Fig 12.2", stop=1)


def first_order(o):
    """Magnification, clear diameters (|marginal| + |chief| at each lens), chief-ray height at each lens."""
    z0 = float(np.ravel(o.surfaces.positions)[0])
    ym, um = rays(o, 0.0, U0, z0)
    yc, uc = rays(o, H, -H / float(np.ravel(o.surfaces.positions)[1] - z0), z0)   # chief ray aimed at lens 1 centre
    m = yc[-1] / H
    lens = slice(1, len(ym) - 1)
    return dict(m=m, diam=2 * (np.abs(ym[lens]) + np.abs(yc[lens])), chief=yc[lens], img_axial=ym[-1])


def object_arrow(ax, z, y):
    """An object or image: a hairline plane with an arrow from the axis to height y."""
    ax.plot([z, z], [-1.35 * abs(y), 1.35 * abs(y)], **LEADER)
    ax.annotate("", (z, y), (z, 0), arrowprops=dict(arrowstyle="-|>,head_length=0.35,head_width=0.14",
                color=INK, linewidth=0.6, shrinkA=0, shrinkB=0))


def draw_relay(o, path, groups, sym, scale_mm, scale_text, arrow_at, u_at):
    """Fig 12.1 / 12.2 redrawn: ideal lenses as plane symbols, axial pair and chief ray from the
    traced system, surfaces numbered as in single()/double(). groups: [(z, [surfaces], name)];
    sym: (object text, image text, object height sign, image height sign)."""
    z0, z1 = [float(np.ravel(o.surfaces.positions)[k]) for k in (0, -1)]
    za, ya = trace(o, 0.0, [-1, 1])
    zc, yc = trace(o, 1.0, [0.0])
    h = 1.06 * float(np.nanmax(np.abs(ya)))
    x0, x1 = z0 - 26 * (z1 - z0) / 468, z1 + 26 * (z1 - z0) / 468              # 26 pt either end
    pt = (x1 - x0) / (TEXT_WIDTH * 72)
    y_num, y_name = h + 8 * pt, -h - 10 * pt
    y_dim = y_name - 36 * pt
    fig, ax = book_axes(TEXT_WIDTH, (x0, x1), (y_dim - 14 * pt, y_num + 12 * pt))
    draw_rays(ax, za, ya, AXIAL, arrow_at=arrow_at)
    draw_rays(ax, zc, yc, CHIEF, arrow_at=arrow_at)
    object_arrow(ax, z0, H * sym[2])
    object_arrow(ax, z1, H * sym[3])
    edges = {0: (z0, 1.35 * H), len(np.ravel(o.surfaces.positions)) - 1: (z1, 1.35 * H)}
    for zl, surfs, name in groups:
        thin_lens(ax, zl, h)
        edges.update({s: (zl, h) for s in surfs})
        ax.plot([zl, zl], [-h, y_name + 3 * pt], **LEADER)
        ax.text(zl, y_name, name, ha="center", va="top", linespacing=1.1)
    number_surfaces(ax, edges, y_num, min_sep=11 * pt)
    ax.text(z0 - 5 * pt, 2.2 * H, sym[0], ha="right", va="center")
    ax.text(z1 + 5 * pt, 2.2 * H * sym[3], sym[1], ha="left", va="center")
    r = 55 * pt                                                             # u_o: the angle at the object point
    ax.add_patch(matplotlib.patches.Arc((z0, 0), 2 * r, 2 * r, theta1=0, theta2=np.degrees(np.arctan(U0)), color=INK, linewidth=0.4))
    ax.text(z0 + u_at * pt, 0.6 * U0 * u_at * pt, "$u_o$", ha="center", va="center")
    dimension(ax, z0, z1, y_dim, "$D$", ext=[(z0, -1.35 * H), (z1, -1.35 * H)], gap=4 * pt)
    for k, (name, style) in enumerate((("marginal ray", AXIAL), ("chief ray", CHIEF))):
        ax.plot([z0 + 6 * pt, z0 + 26 * pt], [y_name - k * 11 * pt] * 2, **style)
        ax.text(z0 + 30 * pt, y_name - k * 11 * pt, name, va="center")
    scale_bar(ax, z1 - 6 * pt - scale_mm, y_name - 3 * pt, scale_mm, scale_text)
    save_book(fig, path)


if __name__ == "__main__":
    s, d = single(), double()
    S, Dd = first_order(s), first_order(d)
    lines = [row("single relay magnification", -1.0, S["m"], "", "{:.4f}"),
             row("single relay axial image error at D (mm)", 0.0, S["img_axial"], "", "{:.2e}"),
             row("single relay lens clear diameter", 100.0, S["diam"].max(), " mm", "{:.1f}"),
             row("double relay magnification", 1.0, Dd["m"], "", "{:.4f}"),
             f"double relay: field lens f = D/8 = {D / 8:.1f} mm puts the chief ray through the second relay at height "
             f"{Dd['chief'][3]:.2e} mm (book: it images the first relay onto the second)",
             row("double relay largest clear diameter", 50.0, Dd["diam"].max(), " mm", "{:.1f}")]
    print("\n".join(lines))
    draw_relay(s, HERE / "ch12_single_relay_layout.png", [(0.0, [1, 2], "relay lens\n(two f = 35 cm doublets)")],
               ("$\\bar{y}_o$", "$\\bar{y}_k$", 1, -1), 100.0, "10 cm", arrow_at=175.0, u_at=100)
    draw_relay(d, HERE / "ch12_double_relay_layout.png",
               [(0.0, [1, 2], "first relay lens"), (175.0, [3], "field lens\nf = D/8"), (350.0, [4, 5], "second relay lens")],
               ("A", "B", 1, 1), 50.0, "5 cm", arrow_at=90.0, u_at=70)
    write_readme(HERE / "README.md", [
        "# ch12 lens relay systems (first-order)",
        "- **Source:** MIL-HDBK-141 (1962) ch12, Sections 12.3.3 and 12.6, Figures 12.1 and 12.2 (pp.12-1 to 12-3).",
        "- **Input:** no glass prescription exists in ch12 (the relays are unspecified telescope doublets), so none was invented; ideal thin lenses from the book's first-order numbers: D = 700 mm, u_o = 0.14, f = 350 mm pair (single), f = 175 mm pairs + field lens f = D/8 (double), field +-6.6 mm.",
        "- **Drawn** (book style, `BOOK_QUALITY_RECIPE.md`; vector `.pdf` + 600 dpi `.png`): `ch12_single_relay_layout` (Fig 12.1) and `ch12_double_relay_layout` (Fig 12.2), both at 6.5 in and true scale: ideal lenses as plane symbols (no glass exists in ch12), axial marginal pair at u_o = 0.14 and the chief ray from the 6.6 mm field edge, object and image planes with their arrows, D, surfaces numbered as in `single()`/`double()` (0 = object, last = image), ray key, 10 cm / 5 cm bar. Petzval and secondary colour need real glass and are not recomputed.",
        "- **OptiLand vs book:** " + "; ".join(lines) + ".",
    ])
