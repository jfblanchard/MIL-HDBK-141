"""Fig 23.15: elements of a slit ultramicroscope. A arc, B condensing lens, C cross slit (inset: normal and rotated
position), D projection objective forming a demagnified ribbon of light in the cell E, F microscope viewing the Tyndall
scattering from above, at right angles to the illuminating beam."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.85, (-10, 104), (-24, 52))
axis_line(ax, P(-6, 0), P(92, 0))
dot(ax, P(0, 0), ms=4.0)
tlens(ax, P(14, 0), 8)
for s in (1, -1):
    line(ax, P(30, s * 0.5), P(30, s * 8), color=INK, linewidth=2.0, solid_capstyle="butt")
for k, x in enumerate((46, 49.5, 53)):
    biconvex(ax, x, 5.5, 2.4, 14.0)
ax.add_patch(plt.Rectangle((68, -6), 12, 12, facecolor="0.97", edgecolor=INK, linewidth=0.7, zorder=1))
line(ax, P(66, 0), P(82, 0), color=INK, linewidth=2.2, zorder=3)
for y in (-6.0, 6.0):
    ray(ax, [P(0, 0), P(14, y)], OFFAXIS, arrows=(0.5,))
    ray(ax, [P(14, y), P(30, y * 0.55 * 0 + 0.7 * np.sign(y)), P(49.5, y * 0.8)], AXIAL, arrows=(0.5,))
    ray(ax, [P(49.5, y * 0.8), P(74, 0)], AXIAL, arrows=(0.6,))
ax.add_patch(plt.Rectangle((66, 8), 16, 38, facecolor="0.97", edgecolor=INK, linewidth=0.6, zorder=1))
tlens(ax, P(74, 13), 5.0, 0)
tlens(ax, P(74, 40), 5.0, 0)
text(ax, "$A$", P(0, -4.5), size=8)
text(ax, "$B$", P(14, 11), size=8)
text(ax, "$C$", P(30, 11), size=8)
text(ax, "$D$", P(49.5, 10.5), size=8)
text(ax, "$E$", P(86, -2.0), size=8)
text(ax, "$F$", P(88, 30), size=8)
lab(ax, "Tyndall scattering", P(74, 3.0), P(94, 11), ha="left", size=6.5)
leg = ["$A$  arc", "$B$  condensing lens", "$C$  cross slit", "$D$  objective", "$E$  cell", "$F$  microscope"]
ax.add_patch(plt.Rectangle((-10, 30), 41, 21, fill=False, edgecolor=INK, linewidth=0.6))
for k, s_ in enumerate(leg):
    text(ax, s_, P(-8.0, 48.0 - 3.3 * k), ha="left", size=6.5)
done(fig, HERE)
readme(HERE, "Fig 23.15: elements of a slit ultramicroscope", lines=["Construction schematic: ideal condensing lens, cross slit (two bars), a 3-element objective drawn as three thin biconvex sections (no prescription in the book), cell and viewing microscope.",
       "Labels and legend from the figure: A arc, B condensing lens, C cross slit, D objective, E cell, F microscope.",
       "FLAG-PARTIAL: the circular slit inset (normal / rotated position) shown in the book is not reproduced."])
