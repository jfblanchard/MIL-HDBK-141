"""Fig 20.1: colour-selective beam splitter. A 45 degree plate with a multilayer coating on its front face
reflects red and green downward and transmits blue."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.55, (-6, 52), (-34, 12))
c = P(26, 0)
plate(ax, c, 22, 2.2, -45, **LENS)
d = np.array([np.cos(np.radians(-45)), np.sin(np.radians(-45))])
n = np.array([-d[1], d[0]])
line(ax, c - d * 11 - n * 1.1, c + d * 11 - n * 1.1, color=INK, linewidth=1.4, zorder=3)
ray(ax, [P(0, 0), c], AXIAL, arrows=(0.5,))
ray(ax, [c, P(48, 0)], AXIAL, arrows=(0.6,))
ray(ax, [c, P(26, -30)], AXIAL, arrows=(0.6,))
text(ax, "white light", P(1, 2.6), ha="left", size=7.5)
text(ax, "blue", P(48, 2.6), ha="right", size=7.5)
text(ax, "red + green", P(28.5, -28), ha="left", size=7.5)
lab(ax, "multilayer coating", c + P(-4.2, 3.8), P(5, 8), ha="left", size=7)
done(fig, HERE)
readme(HERE, "Fig 20.1: colour-selective beam splitter", lines=["Construction schematic: a 45 degree coated plate; reflected beam at 90 degrees.",
       "Labels from the figure: white light, blue (transmitted), red + green (reflected), coating on the front face."])
