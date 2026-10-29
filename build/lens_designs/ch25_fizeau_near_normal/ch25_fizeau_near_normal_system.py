"""Fig 25.10: the usual way of illuminating the interferometer: lamp housing (R, L, G) and eye side by side above
the plates, fringes between S1 and S2 observed at near-normal incidence (no beam-splitting plate needed)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

xc = 22.0
fig, ax = canvas(TEXT_WIDTH * 0.52, (-14, 62), (-26, 40))
Gp = lamp_housing(ax, P(0, 26), w=9.0, ang=-90.0)
eye(ax, P(14, 31), -90, 1.8)
plate(ax, P(xc, -7.0), 30, 3.0, 0, **LENS)
plate(ax, P(xc, -11.9), 30, 3.0, 0, **LENS)
line(ax, P(xc - 15, -8.5), P(xc + 15, -8.5), color=INK, linewidth=0.9, zorder=3)
line(ax, P(xc - 15, -10.4), P(xc + 15, -10.4), color=INK, linewidth=0.9, zorder=3)
dot(ax, P(xc + 14.2, -9.45), ms=1.8)
hatch_block(ax, xc - 19, -19.0, xc + 19, -15.0, hatch="xxxx")
for dx in (-4, 4):
    hit_pt = P(xc + dx, -8.5)
    ray(ax, [P(0.0 + dx * 0.6, 17.5), hit_pt], AXIAL, arrows=(0.45,))
    ray(ax, [hit_pt, P(14 + dx * 0.1, 27.5)], AXIAL, arrows=(0.5,))
text(ax, "$R$", P(-8.5, 34))
text(ax, "$L$", P(-4, 26))
text(ax, "$G$", P(12.5, 13.5))
text(ax, "eye", P(21, 31), ha="left", size=7)
lab(ax, "$S_1$", P(xc + 12, -8.5), P(xc + 22, -4), ha="left")
lab(ax, "$S_2$", P(xc + 12, -10.4), P(xc + 22, -13), ha="left")
text(ax, "$d$", P(xc - 17.5, -9.45), size=7)
lab(ax, "dust, etc.", P(xc + 14.2, -9.45), P(xc + 23.5, -19.5), ha="left", size=7)
text(ax, "black felt", P(xc, -22.5), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.10: most common illumination of the interferometer (near-normal observation)", lines=["Construction schematic; the beam geometry (small angle between illuminating and viewing rays) is exaggerated.",
       "Labels from the figure: R, L, G, eye, S1, S2, d, dust etc., black felt. No numbers printed."])
