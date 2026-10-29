"""Fig 16.24: microscope for viewing reflected fringes under vertical illumination.
A lateral source is collimated by a lens, passed through a monochromatic filter and the
pin-hole H, and turned down the vertical axis by a 45 degree beamsplitter. The objective
sends the beam onto the test surfaces S1/S2 of the specimen plates P1/P2; the reflected
light passes back up through the beamsplitter and objective to the images H0, H1, H2 of
the pin-hole, then to the reticle at the image plane of the micrometer eyepiece."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.62, (-46, 40), (-78, 58))
axis_line(ax, P(0, -74), P(0, 40))

# --- specimen: two plates in contact, gap faces are S1 (bottom of P1) and S2 (top of P2)
plate(ax, P(0, -56), 18, 3.4, 0)
plate(ax, P(0, -62), 18, 3.4, 0)
text(ax, "$P_1$", P(12.5, -55), size=8)
text(ax, "$P_2$", P(12.5, -63), size=8)
text(ax, "$S_1$", P(12.5, -59), size=8)
text(ax, "$S_2$", P(-12.5, -60), ha="right", size=8)

# --- objective, beamsplitter ------------------------------------------------
line(ax, P(-9, -38), P(9, -38), color=INK, linewidth=1.4, solid_capstyle="butt", zorder=3)
text(ax, "OBJECTIVE", P(19, -38), size=7)
splitter(ax, P(0, -12), 13, 45)
text(ax, "BEAMSPLITTER", P(14, -16), size=7)

# --- illumination arm: source, lens, filter, pin-hole H ----------------------
line(ax, P(-38, -13.2), P(-38, -10.8), color=INK, linewidth=1.6, solid_capstyle="butt")
dot(ax, P(-38, -12), ms=2)
text(ax, "SOURCE", P(-38, -6), size=7)
tlens(ax, P(-31, -12), 5, 90)
text(ax, "LENS", P(-31, -22), size=7)
plate(ax, P(-25.5, -12), 6.5, 1.1, 90)
text(ax, "FILTER FOR\nMONOCHROMATIC\nLIGHT", P(-25.5, -1.5), size=6.5)
for s in (1, -1):
    line(ax, P(-20.5, -12 + s * 0.6), P(-20.5, -12 + s * 2.6), color=INK, linewidth=1.4, solid_capstyle="butt")
dot(ax, P(-20.5, -12), ms=2)
text(ax, "PIN-\nHOLE\nH", P(-17.5, -20), ha="left", size=6.5)

# --- pin-hole images and image plane -----------------------------------------
for yy, s in ((-4.5, "$H_0$"), (-2.5, "$H_1$"), (-0.5, "$H_2$")):
    dot(ax, P(0, yy), ms=1.8)
    text(ax, s, P(3.2, yy), ha="left", size=7)
line(ax, P(-10, 18), P(10, 18), color=INK, linewidth=1.0, zorder=3)
for xx in np.linspace(-1.5, 1.5, 7):                       # reticle ticks
    line(ax, P(xx, 18), P(xx, 18.9), color=INK, linewidth=0.5)
text(ax, "IMAGE\nPLANE", P(-19, 18), ha="right", size=7)
text(ax, "RETICLE", P(14, 16), size=7)
line(ax, P(-7, 30), P(7, 30), color=INK, linewidth=1.0, zorder=3)
line(ax, P(-7, 30), P(-4.5, 27.4), color=INK, linewidth=1.0)
line(ax, P(7, 30), P(4.5, 27.4), color=INK, linewidth=1.0)
text(ax, "MICROMETER\nEYEPIECE", P(-19, 30), ha="right", size=7)

# --- rays ---------------------------------------------------------------------
# illumination: source -> lens -> pin-hole H, then on to the beamsplitter
for e in (-4.4, 4.4):
    ray(ax, [P(-38, -12), P(-31, -12 + e), P(-20.5, -12)], AXIAL, arrows=(0.5,))
for hgt in (-11.0, -13.0):
    hh = hit(P(-20.5, hgt), P(1, 0), P(0, -12) - unit(P(1, -1)) * 6.5,
             P(0, -12) + unit(P(1, -1)) * 6.5)
    ray(ax, [P(-20.5, hgt), hh], AXIAL, arrows=(0.6,))
    ray(ax, [hh, hh + P(0, -46)], AXIAL, arrows=(0.45,))          # down to specimen
    ray(ax, [hh + P(0, -46), hh], AXIAL, arrows=(0.5,))           # reflected return
# return rays through the splitter converge at the image plane, continue to eyepiece
for xx in (-1.0, 1.0):
    ray(ax, [P(xx, -58), P(0, 18)], AXIAL, arrows=(0.72,))
    ray(ax, [P(0, 18), P(-xx * 0.42, 30)], AXIAL)
# dashed virtual continuations below the specimen
for xx in (-1.0, 1.0):
    dash(ax, P(xx, -58), P(xx + np.sign(xx) * 0.8, -74))

done(fig, HERE)
readme(HERE, "Fig 16.24: microscope for reflected fringes under vertical illumination",
       lines=["Construction schematic: lateral source + lens + monochromatic filter + pin-hole H,",
              "45 degree beamsplitter, objective, specimen plates P1/P2 with test faces S1/S2,",
              "pin-hole images H0/H1/H2, reticle at the image plane, micrometer eyepiece.",
              "Ideal elements only; no prescription is printed on the figure."])
