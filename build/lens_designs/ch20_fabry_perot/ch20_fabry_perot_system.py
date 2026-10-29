"""Fig 20.98: essential parts of a Fabry-Perot interferometer. Two parallel semi-reflecting plates a gap t_g
apart; a ray at angle theta is multiply reflected, the emerging parallel rays are brought together by a lens
at P in its focal plane (the fringe ring system)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

th, g, xa = np.radians(14.0), 11.0, 20.0
xb, xlens, f = xa + g, 66.0, 22.0
T = np.tan(th)
y0 = -9.0
fig, ax = canvas(TEXT_WIDTH * 0.85, (-6, 100), (-17, 35))
for x in (xa, xb):
    plate(ax, P(x - 1.6 if x == xa else x + 1.6, 7), 44, 3.2, 90, **LENS)
    line(ax, P(x, -15), P(x, 29), color=INK, linewidth=1.3, zorder=3)
cy = y0 + (xlens - xa) * T + 3 * 2 * g * T / 2 + 2 * g * T
axis_y = 8.0
tlens(ax, P(xlens, axis_y), 17)
Pp = P(xlens + f, axis_y + f * T)
dot(ax, Pp)
ray(ax, [P(0, y0 - xa * T), P(xa, y0)], AXIAL, arrows=(0.5,))
ray(ax, [P(xa, y0), P(xb, y0 + g * T)], AXIAL, arrows=(0.5,))
n_exit = 4
for k in range(n_exit):
    ya = y0 + (2 * k + 1) * g * T
    if k < n_exit - 1:
        ray(ax, [P(xb, ya), P(xa, ya + g * T), P(xb, ya + 2 * g * T)], DASH, arrows=())
    x_end = xlens
    ye = ya + (x_end - xb) * T
    ray(ax, [P(xb, ya), P(x_end, ye), Pp], AXIAL, arrows=(0.3,), segs=(0,))
dim(ax, P(xa, -13), P(xb, -13), "$t_g$", size=7)
line(ax, P(xa, -12), P(xa, -14.5), **THIN); line(ax, P(xb, -12), P(xb, -14.5), **THIN)
arc(ax, P(xa, y0), 9, 0, 14, "$\\theta$", rt=1.55, size=7)
dash(ax, P(xa - 6, y0), P(xa + 12, y0))
text(ax, "$P$", Pp + P(1.8, 2.0), ha="left")
text(ax, "plates", P((xa + xb) / 2, 31.5), size=7)
text(ax, "lens", P(xlens, 27), size=7)
text(ax, "focal plane", P(xlens + f, 22.5 + 1), size=7)
line(ax, P(xlens + f, axis_y - 10), P(xlens + f, axis_y + 22), color=INK, linewidth=0.5, dashes=(2, 2))
done(fig, HERE)
readme(HERE, "Fig 20.98: Fabry-Perot interferometer", lines=["Construction schematic: ideal lens, two parallel semi-reflecting plates; the internal zigzag (dashed) follows the geometry.",
       "Symbols: t_g (plate gap), theta (incidence angle), P (focus of the emerging parallel rays). theta and t_g are drawn exaggerated; no numbers printed."])
