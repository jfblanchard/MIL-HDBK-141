"""Fig 25.18: Twyman-Green interferometer adapted to the spherical aberration of a lens L. A convex spherical mirror M1
(vertex B) sits before the focal centre C with its centre of curvature at C; the dashed concave mirror M1' is the
alternative beyond focus. The beam retraces, so the fringes show the lens's wavefront aberration."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

c0, w = P(34, 0), 3.0
xL, Cx, Rm1, Rm2 = 52.0, 76.0, 10.0, 12.0
fig, ax = canvas(TEXT_WIDTH * 0.9, (-8, 104), (-36, 38))
tg_common(ax, c0, w=w, ref_y=28.0, view_y=-18.0, x_src=-4.0, x_col=12.0)
biconvex(ax, xL, 7.0, 3.4, 26.0)
C = P(Cx, 0)
spherical_mirror(ax, C, Rm1, 150, 210, side=-1, lw=1.3)
th = np.radians(np.linspace(-32, 32, 50))
ax.plot(Cx + Rm2 * np.cos(th), Rm2 * np.sin(th), **DASH)
for yy, o in ((w, True), (-w, False)):
    xm = Cx - np.sqrt(Rm1 ** 2 - (yy * Rm1 / (Cx - xL)) ** 2)
    ym = yy * (Cx - xm) / (Cx - xL)
    a2 = [P(c0[0] + yy, yy), P(xL, yy), P(xm, ym)]
    ray(ax, a2, AXIAL, arrows=(0.2,) if o else (), segs=(0,))
    ray(ax, a2[::-1], AXIAL, arrows=() if o else (0.2,))
    ray(ax, [P(xm, ym), P(Cx, 0)], DASH, arrows=())
dot(ax, C, ms=2.6)
text(ax, "$C$", C + P(1.5, 3.2))
text(ax, "$B$", P(Cx - Rm1 - 3.0, -3.2))
text(ax, "$M_1$", P(Cx - Rm1 - 1.0, 8.0))
text(ax, "$M_1'$", P(Cx + Rm2 + 4.0, 0.0))
text(ax, "$e$", P(xL + 3.0, w + 2.0)); text(ax, "$f$", P(xL + 3.0, -w - 2.0))
text(ax, "objective, $L$", P(xL, 12.0), size=7)
text(ax, "$O$", c0 + P(-6.0, -3.8), size=8)
text(ax, "$A$", P(c0[0] - 12.0, 28.0))
text(ax, "$M_2$", P(c0[0] + 12.0, 28.0))
lab(ax, "beamsplitter", c0 + P(-3.5, 3.5), P(c0[0] - 14, 12), ha="right", size=7)
text(ax, "telescope", P(c0[0] + 9.5, -18), size=7, ha="left")
done(fig, HERE)
readme(HERE, "Fig 25.18: Twyman-Green adapted to the spherical aberration of a lens", lines=["Construction schematic: lens L drawn as a biconvex section (no prescription in the book; shape is illustrative), convex return mirror M1 centred on C.",
       "Labels from the figure: pinhole source, collimator, beamsplitter, O, M2, A, objective L, e, f, C, B, M1, M1' (dashed concave alternative), telescope, eye. No numbers printed."])
