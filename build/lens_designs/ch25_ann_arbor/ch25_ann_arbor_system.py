"""Fig 25.20: the Ann Arbor tester, an autocollimation Ronchi test. The tester's ruling and light source lie at the
focal plane F of the lens under test; light passes the lens, is returned by a plane mirror, passes the lens again and
re-forms the ruling at F, viewed through a right-angle prism and eyepiece at P."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

xl, f = 30.0, 24.0
xF = xl + f
fig, ax = canvas(TEXT_WIDTH * 0.9, (-8, 96), (-24, 24))
axis_line(ax, P(-4, 0), P(xF, 0))
mirror(ax, P(0, -14), P(0, 14), side=1, lw=1.3)
ax.add_patch(plt.Rectangle((xl - 5, -12), 10, 24, fill=False, edgecolor=INK, linewidth=0.5, linestyle=(0, (4, 2)), zorder=1))
biconvex(ax, xl - 1.8, 8.5, 3.0, 40.0)
biconvex(ax, xl + 1.8, 8.5, 3.0, 40.0)
dash(ax, P(xF, -14), P(xF, 14))
ax.add_patch(plt.Rectangle((xF, -7), 26, 14, facecolor="0.97", edgecolor=INK, linewidth=0.8, zorder=1))
line(ax, P(xF, -2.6), P(xF, 2.6), color=INK, linewidth=2.2)
ax.add_patch(plt.Polygon([(xF + 14, 7), (xF + 21, 7), (xF + 21, 14)], closed=True, **LENS))
eye(ax, P(xF + 17.5, 20.0), -90, 1.6)
y0 = 1.2
for y_l in (5.0, -5.0):
    y_m = y_l - xl * y0 / f
    y_b = y_l - 2 * xl * y0 / f
    ray(ax, [P(xF, y0), P(xl, y_l), P(0, y_m), P(xl, y_b), P(xF, -y0)], AXIAL, arrows=(0.06, 0.62, 0.95), segs=(0, 2, 3))
text(ax, "plane mirror", P(0, -17.5), size=7)
text(ax, "lens under test", P(xl, -17.0), size=7)
text(ax, "$F$", P(xF, 17.5))
lab(ax, "Ann Arbor tester", P(xF + 13, -7), P(xF + 13, -14.5), size=7)
lab(ax, "ruling and light source", P(xF, 0.0), P(xF - 12, -21.5), size=7)
text(ax, "$P$", P(xF + 22.5, 20.0), size=8)
done(fig, HERE)
readme(HERE, "Fig 25.20: the Ann Arbor tester", lines=["Construction schematic: ideal double pass through the lens under test (drawn as two thin elements in a dashed enclosure, as the figure shows), plane autocollimating mirror, tester with ruling at F.",
       "Labels from the figure: plane mirror, lens under test, F (focal plane of the lens), Ann Arbor tester, P (observer position). No numbers printed."])
