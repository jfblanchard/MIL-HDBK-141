"""Fig 20.99: illuminating the Fabry-Perot with collimated light so it acts as an optical filter. Pinhole at
the focus of L1; the collimated beam crosses the plates at normal incidence; L2 focuses the filtered light on an exit aperture."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

f = 16.0
fig, ax = canvas(TEXT_WIDTH * 0.85, (-6, 82), (-14, 14))
axis_line(ax, P(-4, 0), P(80, 0))
for s in (1, -1):
    line(ax, P(0, s * 0.5), P(0, s * 6), color=INK, linewidth=1.8, solid_capstyle="butt")
dot(ax, P(0, 0), ms=2)
tlens(ax, P(f, 0), 7)
for x in (38, 42):
    plate(ax, P(x, 0), 15, 1.8, 90, **LENS)
    line(ax, P(x + (0.9 if x == 38 else -0.9), -7.5), P(x + (0.9 if x == 38 else -0.9), 7.5), color=INK, linewidth=1.0, zorder=3)
tlens(ax, P(64, 0), 7)
for s in (1, -1):
    line(ax, P(80, s * 0.6), P(80, s * 5), color=INK, linewidth=1.8, solid_capstyle="butt")
for yy in (-5, 5):
    ray(ax, [P(0, 0), P(f, yy)], AXIAL, arrows=(0.5,))
    ray(ax, [P(f, yy), P(64, yy), P(80, 0)], AXIAL, arrows=(0.3, 0.8), segs=(0, 1))
text(ax, "$L_1$", P(f, 9.2))
text(ax, "$L_2$", P(64, 9.2))
text(ax, "pinhole", P(0, -9), size=7)
text(ax, "Fabry-Perot", P(40, 10.2), size=7)
text(ax, "exit aperture", P(80, -9), size=7)
done(fig, HERE)
readme(HERE, "Fig 20.99: collimated illumination of a Fabry-Perot filter", lines=["Construction schematic: ideal lenses with the pinhole and the exit aperture at their focal planes.",
       "Labels: pinhole, L1, Fabry-Perot, L2, exit aperture. No numbers printed."])
