"""Fig 25.5: basic diagram for measuring distortion with a nodal slide. A ray through the nodal point of Lx at
semi-field angle beta meets the flat focal plane at y = f tan(beta), a distance f sec(beta) along the ray."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

f, b = 44.0, np.radians(24.0)
fig, ax = canvas(TEXT_WIDTH * 0.62, (-10, 70), (-10, 28))
axis_line(ax, P(-6, 0), P(f + 6, 0))
line(ax, P(0, -9), P(0, 9), color=INK, linewidth=2.2)
line(ax, P(f, -9), P(f, 26), color=INK, linewidth=0.8)
Y = f * np.tan(b)
ray(ax, [P(-6, -6 * np.tan(b)), P(0, 0), P(f, Y)], AXIAL, arrows=(0.2, 0.62), segs=(0, 1))
dim(ax, P(0, -5), P(f, -5), "$f$", size=7)
line(ax, P(0, -4), P(0, -6.5), **THIN)
line(ax, P(f, -4), P(f, -6.5), **THIN)
dim(ax, P(f + 6, 0), P(f + 6, Y), "$y = f\\,\\tan\\beta$", size=7, tpos=0.5)
line(ax, P(f, Y), P(f + 7, Y), **THIN)
line(ax, P(f, 0), P(f + 7, 0), **THIN)
arc(ax, P(0, 0), 14, 0, 24, r"$\beta$", rt=1.4, size=8)
text(ax, r"$f\,\sec\beta$", P(f / 2 - 3.0, f * np.tan(b) / 2 + 3.8), size=8)
text(ax, "$L_x$", P(-2.6, 10.5))
text(ax, "focal plane", P(f, 28), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.5: basic diagram for measurement of distortion by nodal slide", lines=["Geometry figure drawn from the figure's own relations: y = f tan(beta), ray length f sec(beta).",
       "beta is drawn at 24 degrees (illustrative); no numeric values are printed."])
