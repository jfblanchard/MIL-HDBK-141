"""ch15 Table 15.1 complete 10X telescope, drawn and re-traced in OptiLand.

Book (Section 15, Tables of requirements and 15.1): MP 10X, exit pupil 0.5 cm, eye relief at least
2.0 cm, apparent field 30 deg half angle (true field tan a = tan 30/10, about 3.3 deg), objective
f = 25 cm, D = 5.0 cm. The Porro prism system is entered unfolded, as the table gives it: an 11.6 cm
glass block, n 1.5725. The table ends at the last eyepiece surface; the image plane here is placed
at the paraxial exit pupil so the drawing ends where the eye goes.
"""
import math
import sys
from pathlib import Path

import numpy as np
import optiland.backend as be
from optiland import optic

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from common import (AXIAL, CHIEF, D_LINE, LEADER, TEXT_WIDTH, broken_axes, clear_apertures, dimension,  # noqa: E402
                    draw_lenses, draw_rays, elements, glass, label, number_surfaces, rays, row, save_book,
                    scale_bar, stop_bars, trace, write_readme)

# (c [1/cm], t [cm] after, (n_d, V_d) or None)
ROWS = [(0.07080, 0.80, (1.517, 64.5)), (-0.06874, 0.05, None), (-0.07165, 0.40, (1.689, 30.9)),
        (-0.02413, 15.00, None), (0.0, 11.60, (1.5725, 57.4)), (0.0, 3.0186, None),
        (-0.21670, 0.254, (1.649, 33.8)), (0.35000, 1.8796, (1.620, 55.5)), (-0.25000, 0.1015, None),
        (0.15350, 0.8840, (1.620, 55.5)), (-0.10000, 0.1015, None), (0.35000, 1.2294, (1.517, 64.5)),
        (-0.27500, 0.12190, (1.617, 36.6)), (0.00000, None, None)]
BOOK = dict(mp=10.0, xpd=5.0, eye_relief_min=20.0, f_obj=250.0, D_obj=50.0, half_field=math.degrees(math.atan(math.tan(math.radians(30)) / 10)))


def build(eye_relief=0.0):
    o = optic.Optic(name="10X telescope, MIL-HDBK-141 Table 15.1")
    o.surfaces.add(index=0, radius=be.inf, thickness=be.inf)
    for k, (c, t, g) in enumerate(ROWS, start=1):
        o.surfaces.add(index=k, radius=be.inf if c == 0 else 10 / c, thickness=eye_relief if t is None else t * 10,
                       material=glass(*g) if g else "air", is_stop=(k == 1))
    o.surfaces.add(index=len(ROWS) + 1, comment="exit pupil")
    o.set_aperture(aperture_type="EPD", value=BOOK["D_obj"])
    o.fields.set_type(field_type="angle")
    for f in (0.0, 2.2, BOOK["half_field"]):
        o.fields.add(y=f)
    o.wavelengths.add(value=D_LINE, is_primary=True)
    return o


def first_order():
    o = build()
    ym, um = rays(o, 25.0, 0.0)                              # marginal ray, 2.5 cm high
    a = math.radians(BOOK["half_field"])
    yc, uc = rays(o, 0.0, math.tan(a), 0.0)                  # chief ray through the objective centre
    mp = abs(ym[1] / ym[-2])        # beam height ratio; sign is - because the unfolded prism block omits the erecting reflections
    residual_u = um[-2]
    er = -yc[-2] / uc[-2]                                     # chief ray crosses the axis: exit pupil
    beta = math.degrees(math.atan(abs(uc[-2])))
    ang_mp = abs(uc[-2]) / math.tan(a)
    # objective alone: parallel ray through surfaces 1-4, focus behind surface 4
    obj = optic.Optic()
    obj.surfaces.add(index=0, radius=be.inf, thickness=be.inf)
    for k, (c, t, g) in enumerate(ROWS[:4], start=1):
        obj.surfaces.add(index=k, radius=be.inf if c == 0 else 10 / c, thickness=(t * 10) if k < 4 else 100.0,
                         material=glass(*g) if g else "air", is_stop=(k == 1))
    obj.surfaces.add(index=5)
    obj.set_aperture(aperture_type="EPD", value=50.0)
    obj.fields.add(y=0)
    obj.wavelengths.add(value=D_LINE, is_primary=True)
    f_obj = float(obj.paraxial.f2())
    # eyepiece alone (surfaces 7-14), parallel light from the eye side as ch14 traces it
    ep = optic.Optic()
    ep.surfaces.add(index=0, radius=be.inf, thickness=be.inf)
    ep.surfaces.add(index=1, radius=be.inf, thickness=20.0, is_stop=True)
    rev = ROWS[6:]
    for k in range(len(rev)):
        c = -rev[len(rev) - 1 - k][0]
        g = rev[len(rev) - 2 - k][2] if k < len(rev) - 1 else None
        t = rev[len(rev) - 2 - k][1] * 10 if k < len(rev) - 1 else 30.0
        ep.surfaces.add(index=k + 2, radius=be.inf if c == 0 else 10 / c, thickness=t, material=glass(*g) if g else "air")
    ep.surfaces.add(index=len(rev) + 2)
    ep.set_aperture(aperture_type="EPD", value=5.0)
    ep.fields.add(y=0)
    ep.wavelengths.add(value=D_LINE, is_primary=True)
    f_ep = float(ep.paraxial.f2())
    return dict(mp=mp, ang_mp=ang_mp, residual_u=residual_u, er=er, beta=beta, xpd=2 * abs(ym[-2]), f_obj=f_obj, f_ep=f_ep)


def draw_telescope(o, path):
    """The whole telescope at one true scale with the 15 cm tube cut out: objective, Porro block
    (unfolded), Erfle eyepiece; axial pair and the chief ray of the full field to the eyepoint.
    Surfaces are numbered as in build() (1-4 objective, 5-6 prism block, 7-14 eyepiece, 15 exit pupil)."""
    za, ya = trace(o, 0.0, [-1, 1])
    zc, yc = trace(o, 1.0, [0.0])
    zo, yo = trace(o, 1.0, [-1, 1])
    semi = clear_apertures(o, [ya, yc, yo], pad=1.06, extra=0.4)
    semi[5] = semi[6] = 14.5                                           # Porro block aperture, 2.9 cm (15.4.1)
    pos = np.asarray(o.surfaces.positions, dtype=float).ravel()
    top = semi[1:5].max()
    seg = [(-4.0, pos[4] + 3.5), (pos[5] - 5.0, pos[15] + 6.0)]
    pt = sum(b - a for a, b in seg) / ((TEXT_WIDTH - 0.18) * 72)       # mm per printed point
    y_num, y_r1, y_r2 = top + 8 * pt, -top - 10 * pt, -top - 24 * pt
    fig, (a1, a2) = broken_axes(TEXT_WIDTH, seg, (y_r2 - 30 * pt, y_num + 12 * pt))
    r_pupil = float(np.max(np.abs(ya[15])))
    e1, e2 = {}, {}
    for ax in (a1, a2):
        edges = draw_lenses(ax, o, 1, 14, semi)
        draw_rays(ax, za, ya, AXIAL)
        draw_rays(ax, zc, yc, CHIEF)
        e1, e2 = {k: v for k, v in edges.items() if k <= 4}, {k: v for k, v in edges.items() if k > 4}
    draw_rays(a2, za, ya, {**AXIAL, "linewidth": 0}, arrow_at=293.0)
    draw_rays(a2, zc, yc, {**CHIEF, "linewidth": 0}, arrow_at=293.0)
    stop_bars(a2, pos[15], r_pupil, r_pupil + 2.0)
    e2[15] = (pos[15], r_pupil + 2.0)
    for e in (e1, e2):                                                 # cemented rims coincide: keep numbers in surface order
        ks = sorted(e)
        for a, b in zip(ks, ks[1:]):
            if e[b][0] <= e[a][0]:
                e[b] = (e[a][0] + 0.4, e[b][1])
    number_surfaces(a1, e1, y_num, min_sep=7 * pt)
    number_surfaces(a2, e2, y_num, min_sep=8 * pt)
    groups = elements(o, 1, 14)
    mid = lambda g: np.mean([edges[k][0] for k in g])
    label(a1, "objective", (mid(groups[0] + groups[1]), -semi[1]), (mid(groups[0] + groups[1]), y_r1 - 3 * pt))
    label(a2, "Porro prisms (unfolded)", (mid(groups[2]), semi[5]), (mid(groups[2]), semi[5] + 10 * pt))
    dimension(a2, pos[5], pos[6], -semi[5] - 7 * pt, "11.6 cm", ext=[(pos[5], -semi[5]), (pos[6], -semi[5])], gap=3 * pt)
    for g, name, y in zip(groups[3:], ("field lens", "singlet", "eye lens"), (y_r1, y_r2, y_r1)):
        label(a2, name, (mid(g), -edges[g[0]][1]), (mid(g), y - 3 * pt))
    label(a2, "eyepoint", (pos[15], -(r_pupil + 2.0)), (pos[15] - 6 * pt, y_r2 - 3 * pt))
    zk = pos[5] + 6 * pt
    for k, (name, style) in enumerate((("axial ray", AXIAL), ("chief ray, full field", CHIEF))):
        a2.plot([zk, zk + 22 * pt], [y_r2 - 3 * pt - k * 11 * pt] * 2, **style)
        a2.text(zk + 26 * pt, y_r2 - 3 * pt - k * 11 * pt, name, va="center")
    scale_bar(a2, pos[6] - 50.0 - 6 * pt, y_r1 - 3 * pt, 50.0, "5 cm")
    save_book(fig, path)


if __name__ == "__main__":
    r = first_order()
    o = build(eye_relief=r["er"])
    lines = [row("MP (beam heights 50/xpd)", BOOK["mp"], r["mp"], "", "{:.4f}"),
             row(f"MP (angles, tan b/tan a at a = {BOOK['half_field']:.2f} deg)", BOOK["mp"], r["ang_mp"], "", "{:.4f}"),
             f"afocal: emerging marginal slope {r['residual_u']:.1e} rad",
             row("exit pupil diameter", BOOK["xpd"], r["xpd"], " mm"),
             f"eye relief book >= {BOOK['eye_relief_min']:.1f} mm / OptiLand {r['er']:.2f} mm",
             row("apparent half field", 30.0, r["beta"], " deg", "{:.2f}"),
             row("objective EFL (first-order target 25 cm)", BOOK["f_obj"], r["f_obj"], " mm", "{:.2f}"),
             f"eyepiece EFL (book >= 25 mm) OptiLand {r['f_ep']:.2f} mm, so f_o/f_e = {r['f_obj'] / r['f_ep']:.4f}"]
    print("\n".join(lines))
    draw_telescope(o, HERE / "ch15_telescope_10x_layout.png")
    write_readme(HERE / "README.md", [
        "# ch15 10X telescope",
        "- **Source:** MIL-HDBK-141 (1962) ch15, Table 15.1 (p.15-4) and the design requirements of Section 15.2-15.3.",
        "- **Input:** all 14 surfaces of Table 15.1 (objective doublet, 11.6 cm Porro block unfolded, Erfle-type eyepiece), n_d/V_d as printed; mm in the model.",
        "- **Drawn** (book style, `BOOK_QUALITY_RECIPE.md`; vector `.pdf` + 600 dpi `.png`): `ch15_telescope_10x_layout`, the whole telescope at one true scale at 6.5 in with the 15 cm tube cut out: objective, Porro block (unfolded, 2.9 cm aperture and 11.6 cm thick as the book states), Erfle eyepiece, axial pair and the chief ray of the full 30 deg apparent field to the eyepoint; surfaces numbered as in `build()` (1-4 objective, 5-6 prism block, 7-14 eyepiece, 15 exit pupil), ray key, 5 cm bar.",
        "- **OptiLand vs book:** " + "; ".join(lines) + ".",
    ])
