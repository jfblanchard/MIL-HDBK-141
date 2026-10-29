"""Fig 20.2: a cold mirror and a heat reflector reduce the heat reaching the film in a projector. Lamp at the
focus of a paraboloidal cold mirror; visible light is reflected forward through the condenser, the infrared
passes out the back; the heat-reflecting filter returns what is left of the infrared."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

p_, xl, xf = 8.0, 38.0, 74.0
fig, ax = canvas(TEXT_WIDTH * 0.85, (-34, 84), (-24, 23))
y = np.linspace(-17, 17, 60)
ax.plot(y ** 2 / (4 * p_) - p_, y, color=INK, linewidth=1.5, zorder=3)
for yy in np.linspace(-15, 15, 13):
    x0 = yy ** 2 / (4 * p_) - p_
    nrm = unit(P(-1.0, yy / (2 * p_)))
    tng = unit(P(yy / (2 * p_), 1.0))
    line(ax, P(x0, yy), P(x0, yy) + 2.6 * (nrm + 0.5 * tng), color=INK, linewidth=0.3)
dot(ax, P(0, 0))
tlens(ax, P(xl, 0), 15)
line(ax, P(60, -8), P(60, 8), color=INK, linewidth=1.0)
line(ax, P(xf, -3.5), P(xf, 3.5), color=INK, linewidth=2.0)
for yy in (-10, -5, 5, 10):
    x0 = yy ** 2 / (4 * p_) - p_
    ray(ax, [P(0, 0), P(x0, yy), P(xl, yy), P(xf, 0)], AXIAL, arrows=(0.17, 0.62), segs=(1, 2))
ray(ax, [P(0, 0), P(-6.5, 0.0)], DASH, arrows=())
ray(ax, [P(0, 1), P(-30, 6)], DASH, arrows=(0.8,))
ray(ax, [P(0, -1), P(-30, -6)], DASH, arrows=(0.8,))
ray(ax, [P(xl, 1.8), P(60, 3.0), P(46, 14.5)], DASH, arrows=(0.5,))
text(ax, "infrared (heat)", P(-33, 9), ha="left", size=7)
lab(ax, "cold mirror", P(-5.8, 12.5), P(-22, 19), size=7)
text(ax, "lamp", P(3.5, -3.8), size=7)
text(ax, "condenser", P(xl, -18), size=7)
lab(ax, "heat-reflecting\nfilter", P(60, -7), P(59, -17.5), size=7)
lab(ax, "film", P(xf, -3.5), P(xf + 3, -11), size=7, ha="left")
done(fig, HERE)
readme(HERE, "Fig 20.2: cold mirror and heat reflector in a projection system", lines=["Construction schematic: paraboloidal reflector (lamp at its focus), ideal condenser focusing on the film gate.",
       "Solid rays: visible light. Dashed rays: infrared, transmitted by the cold mirror and reflected back by the heat-reflecting filter. No numbers printed."])
