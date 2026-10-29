"""Fig 25.13: a modified Michelson interferometer. Gas-discharge source with filter F; splitter and
compensator at 45 degrees about O; reference flat S2 (P2) at A with adjusting screws L; test flat S1 (P1) lying
horizontally on support Q at B (it rests under gravity); a 45 degree mirror M sends the beam to the observer. H is the rigid casing."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

w, c0 = 3.0, P(34, 0)
fig, ax = canvas(TEXT_WIDTH * 0.8, (-16, 92), (-34, 40))
ax.add_patch(plt.Rectangle((-3, -28), 78, 62, fill=False, edgecolor=INK, linewidth=0.5, linestyle=(0, (6, 2)), zorder=1))
ax.add_patch(plt.Rectangle((-14, -4.5), 8, 9, facecolor="0.92", edgecolor=INK, linewidth=0.7, zorder=2))
line(ax, P(8, -6), P(8, 6), color=INK, linewidth=1.0)
splitter(ax, c0, 14, 45)
plate(ax, P(50, 0), 12, 1.0, 45, **LENS)
mirror(ax, P(70, -7), P(70, 7), side=-1, lw=1.3)
plate(ax, P(34, 28), 20, 1.6, 0, **LENS)
hatch_block(ax, 24, 25.0, 27.5, 27.2, hatch="////")
hatch_block(ax, 40.5, 25.0, 44, 27.2, hatch="////")
plate(ax, P(34, -24), 12, 1.0, -45, **LENS)
line(ax, *[P(34 - 4.2, -24 + 4.2), P(34 + 4.2, -24 - 4.2)], color=INK, linewidth=1.3, zorder=3)
for yy, o in ((w, True), (-w, False)):
    xh = 34 + yy
    ray(ax, [P(-6, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if o else ())
    a2 = [P(xh, yy), P(70, yy)]
    ray(ax, a2, AXIAL, arrows=(0.5,) if o else ())
    ray(ax, a2[::-1], AXIAL, arrows=() if o else (0.5,))
    a1 = [P(xh, yy), P(xh, 27.2)]
    ray(ax, a1, AXIAL, arrows=(0.5,) if o else ())
    ray(ax, a1[::-1], AXIAL, arrows=() if o else (0.5,))
    ray(ax, [P(xh, yy), P(xh, -24 - (xh - 34)), P(92, -24 - (xh - 34))], AXIAL, arrows=(0.3, 0.88), segs=(0, 1))
text(ax, "light\nsource", P(-10, 8.2), size=7)
text(ax, "$F$", P(8, 8.5))
text(ax, "$O$", P(41.5, -1.6), size=8)
text(ax, "compensator", P(50, 8.8), size=7)
lab(ax, "beamsplitter", P(31, 3.5), P(19, 12.5), size=7)
text(ax, "$A$", P(74.5, -3.0))
text(ax, "$S_2$ or $P_2$", P(77, 3.0), ha="left", size=7.5)
text(ax, "$L$", P(70, -10.5), size=8)
text(ax, "$B$", P(47, 31.8))
text(ax, "$S_1$ or $P_1$", P(49, 28), ha="left", size=7.5)
text(ax, "$Q$", P(21.8, 26.0))
text(ax, "$M$", P(26.0, -27.0))
text(ax, "to observer", P(92, -21 - 3.0), ha="right", size=7)
text(ax, "$H$", P(-1, 32), size=8)
done(fig, HERE)
readme(HERE, "Fig 25.13: a modified Michelson interferometer", lines=["Construction schematic: 45 degree splitter and compensator, plane mirrors, horizontal test flat on a support, 45 degree viewing mirror, casing H.",
       "Labels from the figure: H, light source, F, O, beamsplitter, compensator, A (S2 or P2, screws L), B (S1 or P1 on support Q), M, to observer. No numbers printed."])
