"""Fig 16.12: Michelson interferometer. Collimated beam from S through L1, splitter M0 at 45 degrees,
compensator C in the transmitted arm, fixed mirror M1 (distance d1), movable mirror M2 (distance d2),
recombined beam through L2 to the eye. Beam drawn by two edge rays; each arm is traversed out and back."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

w, c0 = 3.0, P(40, 0)
fig, ax = canvas(TEXT_WIDTH * 0.72, (-8, 92), (-40, 42))
splitter(ax, c0, 14, 45)
plate(ax, P(56, 0), 12, 1.0, 45, **LENS)
mirror(ax, P(34, 34), P(50, 34), side=1, lw=1.3)
mirror(ax, P(80, -8), P(80, 8), side=-1, lw=1.3)
line(ax, P(0, -5), P(0, 5), color=INK, linewidth=2.2)
tlens(ax, P(12, 0), 6.5, 90)
tlens(ax, P(40, -20), 6.5, 0)
eye(ax, P(40, -33), 90, 1.8)
for yy, out_arrow in ((w, True), (-w, False)):
    xh = 40 + yy                       # where the edge ray meets the splitter
    pin = [P(14, yy), P(xh, yy)]
    ray(ax, [P(12, yy), P(xh, yy)], AXIAL, arrows=(0.6,) if out_arrow else ())
    # transmitted arm: to M2 and back
    arm2 = [P(xh, yy), P(80, yy)]
    ray(ax, arm2, AXIAL, arrows=(0.45,) if out_arrow else ())
    ray(ax, arm2[::-1], AXIAL, arrows=() if out_arrow else (0.45,))
    # reflected arm: up to M1 and back
    arm1 = [P(xh, yy), P(xh, 34)]
    ray(ax, arm1, AXIAL, arrows=(0.5,) if out_arrow else ())
    ray(ax, arm1[::-1], AXIAL, arrows=() if out_arrow else (0.5,))
    # recombined beam down to L2, converge on the eye
    ray(ax, [P(xh, yy), P(xh, -20), P(40, -31.5)], AXIAL, arrows=(0.35,) if out_arrow else (0.35,))
text(ax, "$S$", P(-3, 0), ha="right")
text(ax, "$L_1$", P(12, 9))
text(ax, "$M_0$", P(47.5, 7.0))
text(ax, "$C$", P(56, 8))
text(ax, "$M_1$", P(52.5, 36))
text(ax, "$M_2$", P(85, 0))
text(ax, "$L_2$", P(50.5, -20))
text(ax, "observer", P(47, -33), ha="left", size=7)
dim(ax, P(30, 0), P(30, 34), "$d_1$", size=7)
line(ax, P(29, 0), P(40, 0), **THIN); line(ax, P(29, 34), P(34, 34), **THIN)
dim(ax, P(40, -10.5), P(80, -10.5), "$d_2$", size=7)
line(ax, P(40, -0.5), P(40, -11.5), **THIN); line(ax, P(80, -8.5), P(80, -11.5), **THIN)
done(fig, HERE)
readme(HERE, "Fig 16.12: Michelson's interferometer", lines=["Construction schematic: ideal thin lenses, 45 degree splitter and compensator, plane mirrors.",
       "Symbols as named by the figure: S, L1, M0, C, M1, M2, L2, observer, d1, d2. Beam shown by its two edge rays, outbound arrow on one, return arrow on the other."])
