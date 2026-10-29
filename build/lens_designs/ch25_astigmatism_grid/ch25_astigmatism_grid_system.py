"""Fig 25.4: measurement of astigmatism with a grid reticle. R (grid) at the focus of the collimating lens Lc;
Lx (tilted, as in the off-axis test) images it; the travelling microscope M, on a longitudinal slide, is focused
on the sagittal and then the tangential image lines; eye at the eyepiece."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.92, (-8, 122), (-17, 17))
axis_line(ax, P(-4, 0), P(110, 0))
for k in (-3, 0, 3):
    line(ax, P(0, k), P(0, k), **THIN)
ax.add_patch(plt.Rectangle((-1.2, -5), 2.4, 10, facecolor="white", edgecolor=INK, linewidth=0.8, zorder=2))
for k in (-2.5, 0, 2.5):
    line(ax, P(-1.2, k), P(1.2, k), color=INK, linewidth=0.4, zorder=3)
tlens(ax, P(18, 0), 8)
tlens(ax, P(52, 0), 7, 80)
for y in (-5.5, 0, 5.5):
    ray(ax, [P(0, 0), P(18, y)], OFFAXIS if y else AXIAL, arrows=(0.5,))
    ray(ax, [P(18, y), P(52, y), P(78, 0)], AXIAL, arrows=(0.3,), segs=(0, 1) if y else (0,))
ax.add_patch(plt.Rectangle((72, -5), 34, 10, facecolor="0.97", edgecolor=INK, linewidth=0.7, zorder=1))
tlens(ax, P(75, 0), 4.0)
tlens(ax, P(102, 0), 4.0)
ray(ax, [P(78, 0), P(102, 0)], AXIAL, arrows=())
line(ax, P(70, -9.5), P(112, -9.5), color=INK, linewidth=1.0)
for x in np.linspace(72, 110, 14):
    line(ax, P(x, -9.5), P(x - 1.5, -11.5), color=INK, linewidth=0.3)
dim(ax, P(74, -13.5), P(104, -13.5), "", size=7)
eye(ax, P(115.0, 0), 180, 1.7)
text(ax, "$R$", P(0, 8))
text(ax, "$L_c$", P(18, 11))
text(ax, "$L_x$", P(52, 10.5))
text(ax, "$M$", P(88, 8.2))
text(ax, "eye", P(114, 6.0), size=7)
text(ax, "micrometer slide", P(88, -16.3), size=7)
text(ax, "grid reticle", P(0, -9), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.4: measurement of astigmatism with a grid reticle", lines=["Construction schematic: ideal lenses; Lx is drawn tilted; the microscope M is a tube with objective and eyepiece on a slide.",
       "Labels from the figure: R, Lc, Lx, M, eye. Rays are shown for one reticle point only. No numbers printed."])
