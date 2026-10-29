"""Fig 23.20: path of light through a shearing and a double-focus system. In both, a birefringent plate in the condenser
splits the beam into two (object and reference). Shearing: the two foci lie side by side in the object plane. Double focus:
they lie one above the other on the axis. A second birefringent plate in the objective recombines the beams."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.85, (-6, 100), (-8, 62))
def panel(x0, shear, dz, title):
    plate(ax, P(x0, 0), 22, 3.0, 0, **LENS)
    plate(ax, P(x0, 56), 22, 3.0, 0, **LENS)
    line(ax, P(x0 - 13, 27), P(x0 + 13, 27), color=INK, linewidth=0.8)
    fo = P(x0 + shear / 2, 27)                                    # object focus (on the object plane)
    fr = P(x0 - shear / 2, 27 + dz)                               # reference focus
    for foc, sty in ((fo, AXIAL), (fr, DASH)):
        for xi in (-8, 8):
            a = P(x0 + xi, 1.5)
            ray(ax, [a, foc], sty, arrows=(0.5,))
            d = unit(foc - a)
            b = hit(foc, d, P(x0 - 12, 54.5), P(x0 + 12, 54.5))
            ray(ax, [foc, b], sty, arrows=(0.5,))
    dot(ax, fo, ms=2.2)
    dot(ax, fr, ms=2.2, mfc="white")
    text(ax, title, P(x0, -6.5), size=8)
    return fo, fr
fo1, fr1 = panel(24.0, 8.0, 0.0, "shearing system")
fo2, fr2 = panel(76.0, 0.0, 10.0, "double-focus system")
lab(ax, "object focus", fo1, P(2.0, 40.0), ha="center", size=7)
lab(ax, "object focus", fo2, P(98.0, 33.0), ha="left", size=7)
lab(ax, "reference focus", fr2, P(98.0, 42.0), ha="left", size=7)
text(ax, "object plane", P(36.5, 24.0), ha="left", size=6.5)
done(fig, HERE)
readme(HERE, "Fig 23.20: path of light through a shearing and a double-focus system", lines=["Construction schematic: two birefringent plates (condenser and objective) and the two foci; solid rays = object beam, dashed = reference beam.",
       "Labels from the spec: shearing system, double-focus system, object focus, reference focus, object plane. Shear and focal separation are drawn exaggerated; no numbers printed.",
       "FLAG-PARTIAL: the recombination into one collinear beam above the upper plate is shown only to the plate."])
