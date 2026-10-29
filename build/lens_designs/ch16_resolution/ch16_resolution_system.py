"""Fig 16.37: resolution of two distant self-luminous points O and P by an objective of aperture D = 2a,
focal length f; images O', P' separated by f theta at the focal plane."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

th, f, a = np.radians(9.0), 40.0, 11.0
fig, ax = canvas(TEXT_WIDTH * 0.8, (-40, 62), (-19, 17))
axis_line(ax, P(-36, 0), P(58, 0))
tlens(ax, P(0, 0), a)
Fp = P(f, 0)
Pp = P(f, -f * np.tan(th))
line(ax, P(f, -12), P(f, 12), color=INK, linewidth=0.8)
dO, dP = P(1, 0), P(np.cos(th), -np.sin(th))
for y in (-a * 0.9, 0, a * 0.9):
    ray(ax, [P(-34, y), P(0, y), Fp], AXIAL, arrows=(0.2,))
for y in (-a * 0.9, 0, a * 0.9):
    p0 = P(0, y) - dP * 34 / np.cos(th) * 0 
    start = P(-34, y + 34 * np.tan(th))
    ray(ax, [start, P(0, y), Pp], OFFAXIS, arrows=(0.2,))
dot(ax, Fp)
dot(ax, Pp)
text(ax, "$O'$", Fp + P(2, 2), ha="left")
text(ax, "$P'$", Pp + P(2, -1.6), ha="left")
text(ax, "$O$", P(-37, 0), ha="right")
text(ax, "$P$", P(-37, 34 * np.tan(th)), ha="right")
arc(ax, P(0, 0), 14, -9, 0, "$\\theta$", rt=1.35, size=7)
dim(ax, P(0, -a - 3), P(f, -a - 3), "$f$", size=7)
dim(ax, P(-6, -a), P(-6, a), "$D = 2a$", size=7, tpos=0.12)
dim(ax, P(f + 6, 0), P(f + 6, -f * np.tan(th)), "$\\Delta y' = f\\theta$", size=7)
line(ax, P(f, 0), P(f + 7, 0), **THIN)
line(ax, P(f, -f * np.tan(th)), P(f + 7, -f * np.tan(th)), **THIN)
text(ax, "objective", P(0, a + 2.5), size=7)
text(ax, "image plane", P(f, 14), size=7)
done(fig, HERE)
readme(HERE, "Fig 16.37: resolution of two self-luminous points", lines=["Construction schematic: ideal thin objective, source points at infinity.",
       "Labels are the figure's symbols: O, P, O', P', theta, D = 2a, f, delta y' = f theta. theta is drawn exaggerated (9 degrees); no numeric values are printed."])
