"""Fig 25.17: method for obviating the surface flatness of the test plate P: P sits between two good plane parallel
plates E and F, the gaps filled with oil of matching index, so only the plate's homogeneity is measured."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

c0, w = P(34, 0), 3.0
fig, ax = canvas(TEXT_WIDTH * 0.8, (-6, 96), (-34, 36))
tg_common(ax, c0, w=w, ref_y=28.0, view_y=-18.0, x_src=-2.0, x_col=12.0)
xE, xP, xF = 54.0, 62.0, 70.0
h = 10.0
plate(ax, P(xE, 0), 2*h, 2.4, 90, **LENS)
plate(ax, P(xF, 0), 2*h, 2.4, 90, **LENS)
for x0, x1 in ((xE + 1.2, xP - 2.0), (xP + 2.0, xF - 1.2)):
    ax.add_patch(plt.Rectangle((x0, -h), x1 - x0, 2*h, facecolor="0.97", edgecolor=INK, linewidth=0.3, hatch="....", zorder=1))
plate(ax, P(xP, 0), 2*h, 4.0, 90, **LENS)
mirror(ax, P(86, -8), P(86, 8), side=-1, lw=1.3)
for yy, o in ((w, True), (-w, False)):
    a2 = [P(c0[0] + yy, yy), P(86, yy)]
    ray(ax, a2, AXIAL, arrows=(0.25,) if o else ())
    ray(ax, a2[::-1], AXIAL, arrows=() if o else (0.25,))
text(ax, "$E$", P(xE, 13.5)); text(ax, "$P$", P(xP, 13.5)); text(ax, "$F$", P(xF, 13.5))
text(ax, "plane parallel\nplates", P((xE + xF) / 2, 20.5), size=7)
lab(ax, "oil", P((xE + xP) / 2, -7.0), P(xE - 2, -15), size=7)
lab(ax, "oil", P((xP + xF) / 2, -7.0), P(xF + 2, -15), size=7)
text(ax, "$M_2$", P(c0[0] + 12.0, 28.0)); text(ax, "$A$", P(c0[0] - 12.0, 28.0)); text(ax, "$M_1$", P(86, 11.5)); text(ax, "$B$", P(91.5, 3.5))
text(ax, "$O$", c0 + P(-6.0, -3.8), size=8)
lab(ax, "beamsplitter", c0 + P(-3.5, 3.5), P(c0[0] - 14, 12), ha="right", size=7)
text(ax, "telescope", P(c0[0] + 9.5, -18), size=7, ha="left")
done(fig, HERE)
readme(HERE, "Fig 25.17: oil-immersion method for the test plate", lines=["Construction schematic: three plates in the test arm with oil-filled (stippled) gaps; the beam retraces at the end mirror.",
       "Labels from the figure: beamsplitter, O, plane parallel plates E and F, test plate P, oil, M1, B, telescope. No numbers printed."])
