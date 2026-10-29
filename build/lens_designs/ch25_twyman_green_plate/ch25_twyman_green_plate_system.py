"""Fig 25.15: Twyman-Green interferometer for inspecting a glass plate P. Monochromatic source, condenser, filter and
pinhole H feed the collimator; the beam-splitting surface at O divides it; reference flat M2 (surface S2, adjustable, screws L2)
at A; plate P in front of end mirror M1 (surface S1, screws L1) at B; telescope, aperture and eye or camera view the fringes."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

c0, w = P(52, 0), 3.0
fig, ax = canvas(TEXT_WIDTH * 0.95, (-12, 104), (-40, 42))
tg_common(ax, c0, w=w, ref_y=32.0, view_y=-20.0, x_src=14.0, x_col=30.0)
dot(ax, P(-6, 0), ms=3.6)
tlens(ax, P(2, 0), 5.0)
line(ax, P(8, -5), P(8, 5), color=INK, linewidth=1.0)
ray(ax, [P(-6, 0), P(2, 4.0), P(14, 0.0)], OFFAXIS, arrows=(0.3,), segs=(0,))
ray(ax, [P(-6, 0), P(2, -4.0), P(14, 0.0)], OFFAXIS, arrows=(0.3,), segs=(0,))
mirror(ax, P(88, -8), P(88, 8), side=-1, lw=1.3)
plate(ax, P(70, 0), 15, 2.0, 90, **LENS)
for yy, o in ((w, True), (-w, False)):
    a2 = [P(c0[0] + yy, yy), P(88, yy)]
    ray(ax, a2, AXIAL, arrows=(0.3,) if o else ())
    ray(ax, a2[::-1], AXIAL, arrows=() if o else (0.3,))
for dx in (-4.5, 4.5):
    line(ax, P(c0[0] + dx, 33.5), P(c0[0] + dx, 36.0), color=INK, linewidth=0.8)
    line(ax, P(88 + 1.6, dx), P(91.2, dx), color=INK, linewidth=0.8)
text(ax, "source", P(-6, -4.2), size=7)
text(ax, "condenser", P(-1.0, 8.5), size=7, ha="center")
text(ax, "filter", P(9.5, 8.5), size=7)
text(ax, "$H$", P(14, -4.5))
text(ax, "collimator", P(30, 10.5), size=7)
lab(ax, "beam-splitting\nsurface", c0 + P(-0.5, 0.0), P(58.5, 14.5), ha="left", size=7)
text(ax, "$O$", c0 + P(-6.0, -3.8), size=8)
text(ax, "$M_2$, $S_2$", P(c0[0] + 14.5, 32.0), ha="left", size=7.5)
text(ax, "$L_2$", P(c0[0] + 7.0, 36.0), size=8)
text(ax, "$A$", P(c0[0] - 12.0, 32.0))
text(ax, "adjustable", P(c0[0] - 12.5, 38.5), size=7)
text(ax, "$P$", P(70, 11))
text(ax, "$M_1$, $S_1$", P(88, 12.5), size=7.5)
text(ax, "$L_1$", P(95.5, -5.0), size=8)
text(ax, "$B$", P(94.5, 3.5))
text(ax, "telescope", P(c0[0] + 9.5, -20), size=7, ha="left")
for s_ in (1, -1):
    line(ax, P(c0[0] + s_ * 0.9, -28.0), P(c0[0] + s_ * 4.0, -28.0), color=INK, linewidth=1.4)
lab(ax, "aperture", P(c0[0] + 4.0, -28.0), P(c0[0] + 12, -26.5), ha="left", size=7)
text(ax, "eye or camera", P(c0[0] + 5.0, -37.0), size=7, ha="left")
done(fig, HERE)
readme(HERE, "Fig 25.15: Twyman-Green interferometer for inspecting a glass plate P", lines=["Construction schematic: ideal lenses, 45 degree splitter, plane mirrors with screw feet, the plate P in the test arm.",
       "Labels from the figure: source, condenser, filter, H, collimator, beam-splitting surface, O, M2, S2, L2, A, P, M1, S1, L1, B, telescope, aperture, eye or camera. No numbers printed."])
