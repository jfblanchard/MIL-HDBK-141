"""Fig 16.11: method for obtaining Fizeau fringes. Pinhole at the focus of L1, collimated beam turned
down by a 45 degree plate onto a small air wedge between S1 and S2 (wedge angle alpha, exaggerated),
reflected light returns up through the plate to the viewing lens L2 and the eye."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

w, xc = 3.0, 38.0
fig, ax = canvas(TEXT_WIDTH * 0.62, (-8, 70), (-44, 38))
splitter(ax, P(xc, 0), 14, 135)
tlens(ax, P(14, 0), 6.5, 90)
tlens(ax, P(xc, 20), 6.5, 0)
eye(ax, P(xc, 31), 90, 1.8)
for s in (1, -1):
    line(ax, P(0, s * 0.5), P(0, s * 6), color=INK, linewidth=1.8, solid_capstyle="butt")
dot(ax, P(0, 0), ms=2)
# wedge: S1 upper horizontal, S2 lower inclined
plate(ax, P(xc, -30.0), 24, 2.0, 0, **LENS)
xs = np.array([xc - 12, xc + 12])
ax.add_patch(plt.Polygon([(xs[0], -33.5), (xs[1], -31.5 + 0.0), (xs[1], -36), (xs[0], -36)], closed=True, **LENS))
line(ax, P(xs[0], -33.5), P(xs[1], -31.5), color=INK, linewidth=0.8, zorder=3)
lab(ax, "$S_1$", P(xc + 12, -31.0), P(xc + 17, -26.5), ha="left")
lab(ax, "$S_2$", P(xc + 6, -32.8), P(xc + 17, -33.5), ha="left")
lab(ax, "$\\alpha$", P(xc + 10, -32.1), P(xc + 17, -40), size=8)
for yy, dn in ((w, True), (-w, False)):
    xh = xc + yy
    ray(ax, [P(14, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if dn else ())
    ray(ax, [P(0, 0), P(14, yy)], AXIAL, arrows=(0.5,))
    down = [P(xh, yy), P(xh, -29)]
    ray(ax, down, AXIAL, arrows=(0.55,) if dn else ())
    ray(ax, down[::-1], AXIAL, arrows=() if dn else (0.55,))
    ray(ax, [P(xh, yy), P(xh, 20), P(xc, 29.4)], AXIAL, arrows=(0.75,))
text(ax, "pinhole", P(0, -10), size=7)
text(ax, "$L_1$", P(14, 9))
text(ax, "$L_2$", P(xc + 8.5, 20))
text(ax, "eye", P(xc + 4.5, 31), ha="left", size=7)
lab(ax, "45\u00b0 plate", P(xc + 4, -4), P(xc + 17, -9), ha="left", size=7)
lab(ax, "Fizeau fringes", P(xc - 6, -32), P(xc - 17, -42), ha="center", size=7)
done(fig, HERE)
readme(HERE, "Fig 16.11: method for obtaining Fizeau fringes", lines=["Construction schematic: ideal thin lenses, 45 degree semi-reflecting plate, small air wedge.",
       "Symbols as named by the figure spec: pinhole, L1, L2, S1, S2, wedge angle alpha. The wedge angle is exaggerated; no numbers are printed."])
