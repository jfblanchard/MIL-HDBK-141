"""Fig 25.2: measurement of focal length with a visual nodal slide. S sits at the focus of the collimating
system Lc; the system under test Lx is turned about a vertical axis through its rear nodal point N2; when the
axis passes through N2 the image of the distant object stays fixed while Lx rotates."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.85, (-8, 100), (-24, 21))
axis_line(ax, P(-4, 0), P(88, 0))
dot(ax, P(0, 0))
tlens(ax, P(16, 0), 8)
tlens(ax, P(44, 0), 6.5)
xN = 48.0
dash(ax, P(xN, -15), P(xN, 12))
dot(ax, P(xN, 0), ms=2)
hatch_block(ax, xN - 9, -14.5, xN + 9, -9.5, hatch="||||")
line(ax, P(xN - 9, -9.5), P(xN + 9, -9.5), color=INK, linewidth=0.8)
line(ax, P(xN, -9.5), P(xN, -0.0), **THIN)
dim(ax, P(xN - 12, -19), P(xN + 12, -19), "", size=7)
th = np.radians(np.linspace(205, 335, 40))
ax.plot(xN + 9 * np.cos(th), 12.5 + 5 * np.sin(th) * 0 + 4 * np.sin(th) + 4.0, color=INK, linewidth=0.6)
head(ax, P(xN + 9 * np.cos(th[-1]), 12.5 + 4 * np.sin(th[-1]) + 4.0), P(0.6, 0.35), AXIAL)
head(ax, P(xN + 9 * np.cos(th[0]), 12.5 + 4 * np.sin(th[0]) + 4.0), P(-0.6, 0.35), AXIAL)
for y in (-5.5, 0, 5.5):
    ray(ax, [P(0, 0), P(16, y)], OFFAXIS if y else AXIAL, arrows=(0.5,))
    ray(ax, [P(16, y), P(44, y), P(78, 0)], AXIAL, arrows=(0.4,), segs=(0, 1) if y else (0,))
dot(ax, P(78, 0), ms=2.6)
eye(ax, P(92, 0), 180, 1.8)
text(ax, "$S$", P(0, 3.6))
text(ax, "$L_c$", P(16, 10.5))
text(ax, "$L_x$", P(40, 9.5))
text(ax, "$N_2$", P(xN + 3.4, 3.0))
text(ax, "eye", P(90, 6.5), size=7)
text(ax, "rotation about vertical axis\nthrough rear nodal point", P(xN, 20.0), size=7)
text(ax, "slide adjustment", P(xN, -22.8), size=7)
text(ax, "collimating system", P(16, -11.5), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.2: measurement of focal length by use of a visual nodal slide", lines=["Construction schematic: ideal thin lenses; the rotating table is a hatched block with a vertical axis through the rear nodal point N2.",
       "Legend from the figure: Lc = collimating system, Lx = system under test. Labels: S, Lc, Lx, N2, eye, slide adjustment. No numbers printed."])
