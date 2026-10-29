"""Fig 25.9: simple interferometer for viewing Fizeau or Newton fringes at normal incidence. Lamp L with reflector R
and ground glass G; a 45 degree glass plate P turns the light down onto the plates P1, P2 whose facing surfaces S1, S2
enclose an air gap d (with a dust particle as spacer, plates resting on black felt); the eye sees the fringes through P."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

xc, w = 34.0, 3.0
fig, ax = canvas(TEXT_WIDTH * 0.6, (-14, 74), (-42, 30))
Gp = lamp_housing(ax, P(0, 0), w=9.0, ang=0.0)
plate(ax, P(xc, 0), 14, 1.4, 135, **LENS)
eye(ax, P(xc, 21), 90, 1.8)
plate(ax, P(xc, -25.5), 28, 3.0, 0, **LENS)
plate(ax, P(xc, -30.4), 28, 3.0, 0, **LENS)
line(ax, P(xc - 14, -27.0), P(xc + 14, -27.0), color=INK, linewidth=0.9, zorder=3)
line(ax, P(xc - 14, -28.9), P(xc + 14, -28.9), color=INK, linewidth=0.9, zorder=3)
dot(ax, P(xc + 13.2, -27.95), ms=1.8)
hatch_block(ax, xc - 18, -37.5, xc + 18, -33.5, hatch="xxxx")
for yy, dn in ((w, True), (-w, False)):
    xh = xc - yy
    ray(ax, [P(Gp[0], yy), P(xh, yy)], AXIAL, arrows=(0.5,) if dn else ())
    ray(ax, [P(xh, yy), P(xh, -27.0)], AXIAL, arrows=(0.5,) if dn else ())
    ray(ax, [P(xh, -27.0), P(xh, 17)], AXIAL, arrows=() if dn else (0.5,))
text(ax, "$R$", P(-8, 9.5))
text(ax, "$L$", P(0, -3.5))
text(ax, "$G$", P(9.5, 9.5))
text(ax, "$P$", P(xc + 7.5, 5.2))
text(ax, "eye", P(xc + 4.5, 21), ha="left", size=7)
text(ax, "$P_1$", P(xc - 17, -25.5), ha="right")
text(ax, "$P_2$", P(xc - 17, -30.4), ha="right")
lab(ax, "$S_1$", P(xc + 12, -27.0), P(xc + 21, -22.5), ha="left")
lab(ax, "$S_2$", P(xc + 12, -28.9), P(xc + 21, -32.0), ha="left")
dim(ax, P(xc - 10.5, -27.0), P(xc - 10.5, -28.9), "", size=7)
text(ax, "$d$", P(xc - 12.2, -28.0), size=7)
lab(ax, "dust, etc.", P(xc + 13.2, -27.95), P(xc + 21, -37.5), ha="left", size=7)
text(ax, "black felt", P(xc, -40.5), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.9: simple interferometer for Fizeau or Newton fringes at normal incidence", lines=["Construction schematic: 45 degree plate, two plates with an air gap held by a dust particle, black felt base.",
       "Labels from the figure: R, L, G, P, P1, P2, S1, S2, d, dust etc., black felt, eye. The gap d is exaggerated; no numbers printed."])
