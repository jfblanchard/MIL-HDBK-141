"""ch23 microscope: the 1.8 mm fluorite oil objective of Figure 23.7 with the 10X Huygenian eyepiece of
Figure 23.8, drawn and re-traced in OptiLand.

Figure 23.7 (p.23-9) prints every radius, thickness and glass but no signs; signs are read from the
drawing and validated below by the book's own image distance (174.90 mm), which only this reading
reproduces. The meniscus front radius is 8.16 mm as printed (a ~1-2 mm reading, suggested by the
drawn curvature, gives a virtual image). Not in the book, assumed: immersion oil n 1.515, cover glass
n 1.52 (0.18 mm cover, 0.111 mm oil), stop at the rear lens.

Figure 23.8 (p.23-10): field lens R 19.006 / 4.50, eye lens R 9.791 / 3.0, both plano-convex, convex
toward the objective, glass 1.523/58.6, 24.895 mm from the field lens's plane face to the eye lens;
focal plane 17.17 mm before the eye lens, shoulder 11.28 mm past the focal plane; exit pupil at 8 mm.
"""
import sys
from pathlib import Path

import numpy as np
import optiland.backend as be
from optiland import optic

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from common import (AXIAL, CHIEF, D_LINE, INK, OFFAXIS, TEXT_WIDTH, book_axes, broken_axes,  # noqa: E402
                    clear_apertures, draw_lenses, draw_rays, draw_slab, glass, label, number_surfaces,
                    rays, row, save_book, scale_bar, trace, write_readme)

OIL, COVER = glass(1.515, 41.0), glass(1.52, 58.0)
# (radius mm or None, thickness after, material)
OBJECTIVE = [(None, 0.98, glass(1.517, 64.5)), (-0.816, 0.02, "air"), (-8.16, 1.14, glass(1.511, 63.5)),
             (-2.04, 0.251, "air"), (329.2, 0.70, glass(1.56749, 49.2)), (5.40, 1.44, glass(1.43385, 95.4)),
             (-3.72, 0.09, "air"), (-43.7, 1.10, glass(1.621, 36.3)), (4.09, 1.80, glass(1.43385, 95.4)),
             (-4.96, None, "air")]
EYEPIECE = [(19.006, 4.50, glass(1.523, 58.6)), (None, 24.895, "air"), (9.791, 3.0, glass(1.523, 58.6)), (None, None, "air")]
BOOK = dict(f_obj=1.8, image=174.90, na=1.25, f_ep=25.0, focal_plane=17.17, eyepoint=8.0, tube=160.0,
            obj_shoulder=27.13, ep_shoulder=11.28, collar=0.251)
FIELD = (0.0, 0.03, 0.06)   # object heights, mm (the 11.08 mm diaphragm at ~90x is about +-0.06 mm)


def build(gap=None, eye=None, collar=BOOK["collar"], na=BOOK["na"]):
    """Objective alone if gap is None (image at the paraxial image), else objective + eyepiece."""
    o = optic.Optic(name="MIL-HDBK-141 Fig 23.7 objective" + ("" if gap is None else " + Fig 23.8 eyepiece"))
    o.surfaces.add(index=0, radius=be.inf, thickness=0.18, material=COVER)
    o.surfaces.add(index=1, radius=be.inf, thickness=0.111, material=OIL, comment="cover glass")
    k = 2
    for r, t, m in OBJECTIVE:
        t = collar if (r == -2.04) else t
        if t is None:
            t = 150.0 if gap is None else gap
        o.surfaces.add(index=k, radius=be.inf if r is None else r, thickness=t, material=m, is_stop=(r == -4.96))
        k += 1
    if gap is not None:
        for r, t, m in EYEPIECE:
            o.surfaces.add(index=k, radius=be.inf if r is None else r, thickness=eye if t is None else t, material=m)
            k += 1
    o.surfaces.add(index=k, comment="image" if gap is None else "exit pupil")
    o.set_aperture(aperture_type="objectNA", value=na)
    o.fields.set_type(field_type="object_height")
    for h in FIELD:
        o.fields.add(y=h)
    o.wavelengths.add(value=D_LINE, is_primary=True)
    return o


def z_object(o):
    return float(np.ravel(o.surfaces.positions)[0])


def image_distance(collar):
    """Paraxial image distance behind the objective's rear vertex, for an axial object point."""
    o = build(collar=collar)
    y, u = rays(o, 0.0, 0.1, z_object(o))
    return -y[-2] / u[-2]


def eyepiece_alone():
    """Eyepiece EFL, parallel light from the objective side."""
    o = optic.Optic()
    o.surfaces.add(index=0, radius=be.inf, thickness=be.inf)
    for k, (r, t, m) in enumerate(EYEPIECE, start=1):
        o.surfaces.add(index=k, radius=be.inf if r is None else r, thickness=20.0 if t is None else t, material=m, is_stop=(k == 1))
    o.surfaces.add(index=len(EYEPIECE) + 1)
    o.set_aperture(aperture_type="EPD", value=5.0)
    o.fields.add(y=0)
    o.wavelengths.add(value=D_LINE, is_primary=True)
    return float(o.paraxial.f2())


def afocal_gap():
    """Objective-to-field-lens air gap that sends the final image to infinity (secant solve)."""
    def slope(g):
        o = build(gap=g, eye=10.0)
        return rays(o, 0.0, 0.1, z_object(o))[1][-2]
    a, b = 140.0, 170.0
    for _ in range(60):
        fa, fb = slope(a), slope(b)
        a, b = b, b - fb * (b - a) / (fb - fa)
        if abs(b - a) < 1e-9:
            break
    return b


def config(gap):
    """Objective + eyepiece at a given objective-to-field-lens gap: book-comparable first-order data."""
    o = build(gap=gap, eye=10.0)
    ym, um = rays(o, 0.0, 0.1, z_object(o))                       # axial ray
    z = np.asarray(o.surfaces.positions, dtype=float).ravel()
    i_stop, i_field_flat, i_eye, i_last = 11, 13, 14, 15
    focal_plane = z[i_eye] - (z[i_field_flat] - ym[i_field_flat] / um[i_field_flat])
    final_image = -ym[i_last] / um[i_last] if abs(um[i_last]) > 1e-12 else float("inf")   # < 0: virtual, before the eye lens
    ys, us = o.paraxial.trace_generic(0.0, 0.01, z[i_stop], D_LINE, skip=i_stop)          # chief ray from the stop centre
    ys, us = np.ravel(ys), np.ravel(us)
    eyepoint = -ys[-2] / us[-2]                                    # arrays start at the stop: [-2] is the eye lens's plane face
    tube = (z[i_eye] - focal_plane + BOOK["ep_shoulder"]) - (z[i_stop] + BOOK["obj_shoulder"])
    return dict(focal_plane=focal_plane, eyepoint=eyepoint, tube=tube, final_image=final_image)


def book_gap():
    """Gap that puts the intermediate image 17.17 mm before the eye lens, as Fig 23.8 prints it."""
    a, b = 150.0, 165.0
    for _ in range(60):
        fa, fb = config(a)["focal_plane"] - BOOK["focal_plane"], config(b)["focal_plane"] - BOOK["focal_plane"]
        a, b = b, b - fb * (b - a) / (fb - fa)
        if abs(b - a) < 1e-9:
            break
    return b


def legend(ax, z, y, dy):
    """Two-line ray key drawn in data units (a matplotlib legend box would be chartjunk here)."""
    for k, (name, style) in enumerate((("axial ray", AXIAL), ("chief ray", CHIEF))):
        ax.plot([z, z + 3 * dy], [y - k * dy] * 2, **style)
        ax.text(z + 3.6 * dy, y - k * dy, name, va="center")


def draw_objective(path):
    """Fig 23.7 redrawn: the objective alone at N.A. 1.25, surfaces numbered as in build()."""
    o = build()
    z, y = trace(o, 0.0, [-1, -0.5, 0, 0.5, 1])
    semi = clear_apertures(o, [y], pad=1.06, extra=0.06)
    top = semi[2:12].max()
    fig, ax = book_axes(4.8, (-2.4, 10.6), (-top - 1.25, top + 1.15))
    draw_slab(ax, -0.18, 0.0, top + 0.35)                                          # cover glass
    draw_slab(ax, 0.0, 0.111, semi[2] + 0.3, facecolor="0.85", linewidth=0.3)     # oil film
    edges = draw_lenses(ax, o, 2, 11, semi)
    edges[1] = (0.0, top + 0.35)
    draw_rays(ax, z, y, AXIAL, first=0, last=11)
    zr = np.asarray(o.surfaces.positions, dtype=float).ravel()[11]
    ze = 10.4
    for k in range(z.shape[1]):                                                    # rear rays, toward the image
        draw_rays(ax, np.array([[z[11, k]], [ze]]), np.array([[y[11, k]], [y[11, k] + (ze - z[11, k]) *
                  (y[12, k] - y[11, k]) / (z[12, k] - z[11, k])]]), AXIAL,
                  arrow_at=None if abs(y[11, k]) < 1e-9 else 9.4)
    number_surfaces(ax, edges, top + 0.55, min_sep=0.42)
    label(ax, "N.A. 1.25", (-0.09, 0.13), (-1.3, 1.3))
    label(ax, "specimen", (-0.18, 0.0), (-1.3, -0.9))
    label(ax, "cover glass", (-0.09, -1.9), (-1.3, -2.4))
    label(ax, "oil", (0.055, semi[2] + 0.1), (-1.3, 2.5))
    ax.annotate("", (ze, 0), (zr + 0.25, 0), arrowprops=dict(arrowstyle="-|>,head_length=0.4,head_width=0.15",
                color=INK, linewidth=0.4, shrinkA=0, shrinkB=0))
    ax.text((zr + ze) / 2 + 0.2, 0.12, "174.90 to\nimage plane", ha="center", va="bottom", linespacing=1.1)
    scale_bar(ax, 7.6, -top - 0.55, 2.0)
    save_book(fig, path)


def draw_microscope(path, gap, eye):
    """The whole instrument, eye relaxed (afocal): true scale throughout, the empty tube cut out."""
    o = build(gap=gap, eye=eye)
    za, ya = trace(o, 0.0, [-1, 1])                    # axial ray pair, N.A. 1.25
    zc, yc = trace(o, 1.0, [0.0])                      # chief ray from the 0.06 mm field edge
    zo, yo = trace(o, 1.0, [-1, 1])                    # the rest of that field bundle
    semi = clear_apertures(o, [ya, yc, yo], pad=1.05, extra=0.1)
    pos = np.asarray(o.surfaces.positions, dtype=float).ravel()
    field, eye_lens, pupil = pos[12], pos[14], pos[16]
    focal = eye_lens - config(gap)["focal_plane"]
    h = semi[12:16].max()
    fig, (a1, a2) = broken_axes(TEXT_WIDTH, [(-0.9, 9.4), (field - 9.0, pupil + 3.5)], (-h - 2.3, h + 2.3))
    for ax in (a1, a2):
        draw_lenses(ax, o, 2, 11, semi)
        draw_slab(ax, -0.18, 0.0, semi[2:12].max() + 0.3)
        draw_rays(ax, zo, yo, OFFAXIS)
        draw_rays(ax, za, ya, AXIAL)
        draw_rays(ax, zc, yc, CHIEF)
    edges = draw_lenses(a2, o, 12, 15, semi)
    number_surfaces(a2, edges, h + 0.55, min_sep=1.2)
    for s in (1, -1):                                                         # Fig 23.8's 11.08 mm diaphragm
        a2.plot([focal, focal], [s * 5.54, s * (5.54 + 0.9)], color=INK, linewidth=1.4, solid_capstyle="butt")
    draw_rays(a2, za, ya, {**AXIAL, "linewidth": 0}, first=0, arrow_at=field - 5.0)
    oh = semi[2:12].max()
    label(a1, "1.8 mm objective\n(Fig. 23.7)", (4.4, -oh), (4.4, -h - 1.35), linespacing=1.1)
    label(a1, "specimen", (-0.18, 0.0), (-0.3, h + 0.6))
    label(a2, "field lens", (field + 1.5, -semi[12]), (field + 1.5, -h - 1.3))
    label(a2, "diaphragm\n(focal plane)", (focal, -6.44), (focal, -h - 1.35), linespacing=1.1)
    label(a2, "eye lens", (eye_lens + 1.2, -semi[14]), (eye_lens + 1.2, -h - 1.3))
    label(a2, "eyepoint", (pupil, 0.0), (pupil + 1.6, -2.6), ha="left")
    a2.text((field + eye_lens) / 2 + 2, h + 1.7, "10X Huygenian eyepiece (Fig. 23.8)", ha="center", va="bottom")
    legend(a2, field - 8.6, h - 0.4, 1.0)
    scale_bar(a2, focal + 6.0, -h - 0.9, 5.0)
    save_book(fig, path)


if __name__ == "__main__":
    img = image_distance(BOOK["collar"])
    fine = np.linspace(0.20, 0.30, 10001)
    collar_fit = fine[np.argmin([abs(image_distance(c) - BOOK["image"]) for c in fine])]
    f_obj = float(build().paraxial.f2())
    f_ep = eyepiece_alone()
    ga, gb = afocal_gap(), book_gap()
    A, B = config(ga), config(gb)
    lines = [row("objective image distance behind rear vertex (collar .251)", BOOK["image"], img, " mm", "{:.2f}"),
             f"collar setting that gives 174.90 mm: {collar_fit:.4f} mm (printed .251, 'Adjustable')",
             row("objective EFL (nominal)", BOOK["f_obj"], f_obj, " mm"),
             row("eyepiece EFL (10X = 250/f)", BOOK["f_ep"], f_ep, " mm", "{:.2f}"),
             f"eye focused at infinity: focal plane {A['focal_plane']:.2f} mm before the eye lens (book 17.17), eyepoint "
             f"{A['eyepoint']:.2f} mm (book 8), tube {A['tube']:.1f} mm (book 160)",
             f"focal plane set to the printed 17.17 mm: virtual image {-B['final_image']:.0f} mm before the eye lens (the book allows "
             f"10 in to infinity), eyepoint {B['eyepoint']:.2f} mm (book 8), tube {B['tube']:.1f} mm (book 160)"]
    print("\n".join(lines))
    draw_microscope(HERE / "ch23_microscope_layout.png", ga, A["eyepoint"])
    draw_objective(HERE / "ch23_objective_layout.png")
    write_readme(HERE / "README.md", [
        "# ch23 microscope: 1.8 mm fluorite objective + 10X Huygenian eyepiece",
        "- **Source:** MIL-HDBK-141 (1962) ch23, Figure 23.7 (objective, p.23-9) and Figure 23.8 (eyepiece, p.23-10); N.A. 1.25 from Section 23.3.4.",
        "- **Input:** radii/thicknesses/glasses as printed (signs from the drawing, validated by the 174.90 mm image distance; meniscus front 8.16 mm as printed); assumed, not in the book: oil 1.515, cover 1.52, stop at the rear lens.",
        "- **Drawn** (book style, `BOOK_QUALITY_RECIPE.md`; vector `.pdf` + 600 dpi `.png`): `ch23_microscope_layout`, the whole microscope focused for a relaxed eye (afocal), true scale with the empty tube cut out, axial ray pair at N.A. 1.25 and the chief ray from the 0.06 mm field edge to the eyepoint, diaphragm 11.08 mm at the traced focal plane; `ch23_objective_layout`, Fig 23.7 redrawn, the objective alone with its axial bundle at N.A. 1.25. Surface numbers are the OptiLand surface indices of `build()` (0 = specimen, 1 = cover/oil, 2-11 objective, 12-15 eyepiece).",
        "- **OptiLand vs book:** " + "; ".join(lines) + ".",
    ])
