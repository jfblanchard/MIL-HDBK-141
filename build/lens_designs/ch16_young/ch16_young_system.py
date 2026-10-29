"""Fig 16.3: Young's pinhole experiment. Construction at the geometry the figure defines:
S0 on the axis, pinholes S1/S2 a distance d apart, screen at D >> d, point P at x."""
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
import sys
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

d, D, X = 8.0, 60.0, 17.0
S0, S1, S2, P_ = P(0, 0), P(20, d / 2), P(20, -d / 2), P(20 + D, X)
fig, ax = canvas(TEXT_WIDTH * 0.8, (-6, 100), (-17, 22))
axis_line(ax, P(-4, 0), P(98, 0))
for a, b in (((20, -14), (20, -d / 2 - 0.7)), ((20, -d / 2 + 0.7), (20, d / 2 - 0.7)), ((20, d / 2 + 0.7), (20, 14))):
    line(ax, a, b, color=INK, linewidth=1.6, solid_capstyle="butt")
line(ax, P(80, -14), P(80, 20), color=INK, linewidth=0.8)
for p in (S0, S1, S2):
    dot(ax, p)
ray(ax, [S0, S1], AXIAL, arrows=(0.5,))
ray(ax, [S0, S2], AXIAL, arrows=(0.5,))
ray(ax, [S1, P_], AXIAL, arrows=(0.5,))
ray(ax, [S2, P_], AXIAL, arrows=(0.5,))
u = unit(P_ - S2)
F = S2 + np.dot(S1 - S2, u) * u
dash(ax, S1, F)
ax.plot(*F, "|", color=INK, markersize=0)
text(ax, "$S_0$", (-3, 0), ha="right")
text(ax, "$S_1$", S1 + P(-1.2, 1.4), ha="right")
text(ax, "$S_2$", S2 + P(-1.2, -1.4), ha="right")
text(ax, "$P$", P_ + P(-1.5, 1.3), ha="right")
text(ax, "$O$", P(81.5, -1.6), ha="left")
text(ax, "$r_1$", (S1 + P_) / 2 + P(0, 1.8))
text(ax, "$r_2$", (S2 + P_) / 2 + P(1.2, -2.0))
lab(ax, r"$\Delta = r_2 - r_1 \approx xd/D$", (S2 + F) / 2 + P(0, 0), P(46, -11), ha="left")
dim(ax, P(20, -14.5), P(80, -14.5), "$D$", size=7)
dim(ax, P(14.5, -d / 2), P(14.5, d / 2), "$d$", size=7)
line(ax, P(14, -d / 2), P(19, -d / 2), **THIN)
line(ax, P(14, d / 2), P(19, d / 2), **THIN)
dim(ax, P(86, 0), P(86, X), "$x$", size=7)
line(ax, P(80, 0), P(87, 0), **THIN)
line(ax, P(80, X), P(87, X), **THIN)
w = 11.0
yy = np.linspace(-14, 20, 300)
ax.plot(80 - 0 * yy + 0.0, yy, alpha=0)
ax.plot(94 - 6 * np.cos(np.pi * yy / w) ** 2 * 0 + 0 * yy, yy, alpha=0)
ax.plot(92 + 6 * np.cos(np.pi * yy / w) ** 2, yy, color=INK, linewidth=0.5)
line(ax, P(92, -14), P(92, 20), **THIN)
dim(ax, P(98.5, 0), P(98.5, w), r"$\lambda D/d$", size=6.5)
text(ax, "screen", P(80, 21.5), size=7)
text(ax, "pinholes", P(20, 16), size=7)
text(ax, "fringe\nintensity", P(95, -17), size=7)
done(fig, HERE)
readme(HERE, "Fig 16.3: Young's pinhole experiment",
       lines=["Construction schematic of ideal pinholes (no OptiLand prescription: the book gives symbols only).",
              "Labels are the symbols the figure names: S0, S1, S2, d, D, P, x, r1, r2, path difference, fringe width lambda D/d.",
              "Distances are drawn exaggerated for legibility (D >> d in the physical arrangement); no numeric values are printed."])
