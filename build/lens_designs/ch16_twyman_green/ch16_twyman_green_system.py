"""Fig 16.16: Newton's fringes with a Twyman-Green interferometer testing a lens. Pinhole at the focus of
L1, splitter M0 at 45 degrees, flat reference mirror in one arm, test lens LT with a spherical mirror whose
centre of curvature is LT's focus in the other, recombined beams through L2 to the eye."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

w, c0, f = 3.0, P(36, 0), 14.0
Fx, Rm = 54 + f, 12.0
fig, ax = canvas(TEXT_WIDTH * 0.82, (-8, 100), (-40, 40))
splitter(ax, c0, 14, 45)
tlens(ax, P(14, 0), 6.5, 90)
tlens(ax, P(54, 0), 6.5, 90)
tlens(ax, P(36, -18), 6.5, 0)
eye(ax, P(36, -30), 90, 1.8)
mirror(ax, P(28, 30), P(44, 30), side=1, lw=1.3)
spherical_mirror(ax, P(Fx, 0), Rm, -30, 30, side=1, lw=1.3)
for s in (1, -1):
    line(ax, P(0, s * 0.5), P(0, s * 6), color=INK, linewidth=1.8, solid_capstyle="butt")
dot(ax, P(0, 0), ms=2)
for yy, o in ((w, True), (-w, False)):
    xh = 36 + yy
    ray(ax, [P(14, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if o else ())
    ref = [P(xh, yy), P(xh, 30)]
    ray(ax, ref, AXIAL, arrows=(0.5,) if o else ())
    ray(ax, ref[::-1], AXIAL, arrows=() if o else (0.5,))
    # test arm: collimated to LT, converge to focus, diverge to the sphere (normal incidence), and back
    tst = [P(xh, yy), P(54, yy), P(Fx, 0)]
    far = P(Fx, 0) + Rm * unit(P(Fx, 0) - P(54, yy))
    tst2 = tst + [far]
    ray(ax, tst2, AXIAL, arrows=(0.2,) if o else ())
    ray(ax, tst2[::-1], AXIAL, arrows=() if o else (0.2,))
    ray(ax, [P(xh, yy), P(xh, -18), P(36, -28.2)], AXIAL, arrows=(0.4,))
text(ax, "pinhole", P(0, -10), size=7)
text(ax, "$L_1$", P(14, 9))
text(ax, "$M_0$", c0 + P(-6.0, 5.2))
text(ax, "reference\nmirror", P(36, 36), size=7)
text(ax, "$L_T$", P(54, 9.5))
text(ax, "spherical\nmirror", P(Fx + 14, 12.5), size=7, ha="left")
text(ax, "$L_2$", P(43.5, -18))
text(ax, "eye", P(43, -30), ha="left", size=7)
done(fig, HERE)
readme(HERE, "Fig 16.16: Newton's fringes with a Twyman-Green interferometer", lines=["Construction schematic: ideal lenses and mirrors; the spherical mirror is centred on the focus of the test lens LT so rays retrace.",
       "Symbols as named by the figure spec: pinhole, L1, M0, reference mirror, LT, spherical mirror, L2, eye. No numbers are printed."])
