"""Fig 25.11: arrangement of the interferometer surfaces S1 and S2 for Newton's fringes: a block Q with a convex
spherical lower surface S1 rests on the second surface S2 and touches it at O; the air film has thickness d at
radial distance r from O. Light falls normally from above; black felt base.
FLAG-NOTE: the spec says the lower surface is 'concave spherical (or flat test glass)'; it is drawn flat."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

R, hq, r = 70.0, 24.0, 15.0
fig, ax = canvas(TEXT_WIDTH * 0.5, (-34, 40), (-17, 33))
y = np.linspace(-hq, hq, 90)
s = R - np.sqrt(R ** 2 - y ** 2)
poly = np.column_stack([np.r_[y, hq, -hq], np.r_[s, 18, 18]])
ax.add_patch(plt.Polygon(poly, closed=True, **LENS))
plate(ax, P(0, -4.5), 70, 6.0, 0, **LENS)
line(ax, P(-35, -1.5), P(35, -1.5), color=INK, linewidth=0.9, zorder=3)
hatch_block(ax, -38, -13.5, 38, -9.5, hatch="xxxx")
dot(ax, P(0, 0.0), ms=2)
for x in (-12, -4, 4, 12):
    ray(ax, [P(x, 31), P(x, 20)], AXIAL, arrows=(0.5,))
dim(ax, P(r, 0), P(r, R - np.sqrt(R ** 2 - r ** 2)), "", size=7)
text(ax, "$d$", P(r + 3.0, 0.8 + 1.5), size=7)
text(ax, "$Q$", P(-22, 14))
lab(ax, "$S_1$", P(-17, (R - np.sqrt(R ** 2 - 17 ** 2))), P(-29, 5), ha="right")
lab(ax, "$S_2$", P(-28, -1.5), P(-31, -6.0), ha="right")
lab(ax, "$O$", P(0, -0.2), P(0, -7.2), size=8)
text(ax, "black felt", P(0, -16), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.11: surfaces S1 and S2 arranged for Newton's fringes", flag="FLAG-NOTE: the spec describes S2 as a concave spherical surface or a flat test glass; drawn as the flat alternative.",
       lines=["Construction schematic: spherical lower surface of Q on a flat plate; the radius is exaggerated in curvature for legibility (not to scale).",
              "Labels from the figure: Q, S1, S2, O, d, black felt, normal incident light. No numbers printed."])
