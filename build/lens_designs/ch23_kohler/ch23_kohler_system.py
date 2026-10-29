"""Fig 23.4: Koehler illumination, unfolded. Ideal thin lenses placed so the two conjugate sets hold:
  illuminating (aperture) set, dashed: lamp filament -> substage iris -> rear focal point of the objective -> eye pupil;
  image-forming (field) set, solid: lamp iris -> specimen -> eyepiece field diaphragm -> retina.
The substage iris sits in the front focal plane of the substage condenser; lamp condenser and objective are
placed to give those images (thin-lens equation); all values are drawing units."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403


def thin(lenses, y, u, x0, x_end):
    """Paraxial polyline from (x0, y) with slope u through thin lenses [(x, f)] to x_end."""
    pts, x = [P(x0, y)], x0
    for xl, f in lenses:
        if xl <= x0 or xl >= x_end:
            continue
        y += u * (xl - x)
        x = xl
        pts.append(P(x, y))
        u -= y / f
    pts.append(P(x_end, y + u * (x_end - x)))
    return pts


xs = dict(src=0.0, lamp=14.0, liris=22.0, siris=48.0, cond=62.0, spec=83.5, obj=94.0, rfp=102.0, fd=134.0, eye=144.0, pupil=157.0)
f_lamp, f_cond, f_obj, f_eye = 9.92, 14.0, 8.0, 10.0
lenses = [(xs["lamp"], f_lamp), (xs["cond"], f_cond), (xs["obj"], f_obj), (xs["eye"], f_eye)]
fig, ax = canvas(TEXT_WIDTH, (-12, 176), (-28, 27))
axis_line(ax, P(-8, 0), P(172, 0))
th = np.radians(np.linspace(-55, 55, 40))
ax.plot(-3 - 6 * np.cos(th) + 6, 6.5 * np.sin(th) * 1.2, color=INK, linewidth=1.0, zorder=3)
dot(ax, P(0, 0), ms=3.0)
for k, (name, h) in enumerate((("lamp", 8.0), ("cond", 9.0), ("obj", 7.0), ("eye", 7.0))):
    tlens(ax, P(xs[name], 0), h)
stop_bars(ax, xs["liris"], 3.2, 9.0)
stop_bars(ax, xs["siris"], 6.0, 11.0)
stop_bars(ax, xs["fd"], 3.6, 9.0)
line(ax, P(xs["spec"], -4.5), P(xs["spec"], 4.5), color=INK, linewidth=1.6)
ax.plot([xs["rfp"]], [0], "+", color=INK, markersize=4, zorder=4)
eye(ax, P(xs["pupil"] + 5, 0), 180, 2.2)
for u in (-0.40, 0.40):                                            # aperture set (dashed): filament point
    ray(ax, thin(lenses, 0.0, u, 0.0, xs["pupil"]), DASH, arrows=(0.16, 0.55), segs=(0, 2))
for y0 in (3.2, -3.2):                                             # field set (solid): lamp-iris edge
    for u in (-0.16, 0.16):
        ray(ax, thin(lenses, y0, u, xs["liris"], xs["pupil"]), AXIAL, arrows=(0.1, 0.5), segs=(0, 1)) if u > 0 and y0 > 0 else ray(ax, thin(lenses, y0, u, xs["liris"], xs["pupil"]), AXIAL, arrows=())
names = [("spherical\nreflector", P(-4.0, 6.0), P(-4.0, 16.0)),
         ("lamp\ncondenser", P(xs["lamp"], 8.0), P(xs["lamp"] - 4, 22.0)),
         ("lamp iris\ndiaphragm", P(xs["liris"], 9.0), P(xs["liris"] + 10, 15.0)),
         ("substage\ncondenser", P(xs["cond"], 9.0), P(xs["cond"] + 2, 16.0)),
         ("objective", P(xs["obj"], 7.0), P(xs["obj"] + 6, 15.0)),
         ("eyepiece field\ndiaphragm", P(xs["fd"], 9.0), P(xs["fd"] - 6, 16.0)),
         ("light source", P(0, -0.8), P(2, -12.5)),
         ("substage iris\ndiaphragm", P(xs["siris"], -11.0), P(xs["siris"] - 2, -16.0)),
         ("specimen", P(xs["spec"], -4.5), P(xs["spec"] - 6, -12.5)),
         ("rear focal point\nof objective", P(xs["rfp"], -0.8), P(xs["rfp"] + 12, -13.5)),
         ("eyepiece", P(xs["eye"], -7.0), P(xs["eye"] + 2, -13.5))]
for s_, xy, xt in names:
    lab(ax, s_, xy, xt, size=6.5)
text(ax, "eye", P(xs["pupil"] + 8, 7.0), size=7)
k0 = P(118, -21.0)
line(ax, k0, k0 + P(10, 0), **AXIAL)
text(ax, "image-forming rays", k0 + P(12, 0), ha="left", size=6.5)
line(ax, k0 + P(0, -4), k0 + P(10, -4), **DASH)
text(ax, "illuminating rays", k0 + P(12, -4), ha="left", size=6.5)
done(fig, HERE)
readme(HERE, "Fig 23.4: Koehler illumination, schematic diagram", lines=["Construction schematic: thin lenses placed by the thin-lens equation so that the two conjugate sets of the figure hold (lamp iris - specimen - field diaphragm - retina; filament - substage iris - rear focal point of the objective - eye pupil).",
       "Labels from the spec: spherical reflector, light source, lamp condenser, lamp iris diaphragm, substage iris diaphragm, substage condenser, specimen, objective, rear focal point of objective, eyepiece field diaphragm, eyepiece, eye. Solid rays: image-forming; dashed: illuminating. No numbers printed.",
       "FLAG-NOTE: the objective and eyepiece here are ideal thin lenses, not the ch23 microscope prescription."])
