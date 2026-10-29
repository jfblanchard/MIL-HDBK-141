"""Fig 25.14: Michelson's interferometer as a method of Fizeau fringes. With OA = OB the observer sees S2 as if it
were at S2', so the fringes are those of S1 and S2' in close contact (a thin air wedge)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

c0, OA = P(30, 0), 28.0
fig, ax = canvas(TEXT_WIDTH * 0.7, (-6, 80), (-26, 40))
splitter(ax, c0, 13, 45)
tilt = np.radians(4.0)
S1c = c0 + P(OA, 0)
def seg(c, ang, h):
    d = P(np.cos(ang), np.sin(ang))
    return c - h * d, c + h * d
a, b = seg(S1c, np.pi / 2, 8)
mirror(ax, a, b, side=-1, lw=1.3)
a, b = seg(c0 + P(0, OA), 0.0, 8)
mirror(ax, a, b, side=1, lw=1.3)
a, b = seg(S1c + P(-0.0, 0), np.pi / 2 + tilt, 8)
a2, b2 = seg(S1c + P(-4.5, 0), np.pi / 2 + tilt * 2.2, 8)
dash(ax, a2, b2)
for yy, o in ((2.5, True), (-2.5, False)):
    xh = 30 + yy
    ray(ax, [P(0, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if o else ())
    r2 = [P(xh, yy), P(S1c[0], yy)]
    ray(ax, r2, AXIAL, arrows=(0.5,) if o else ())
    ray(ax, r2[::-1], AXIAL, arrows=() if o else (0.5,))
    r1 = [P(xh, yy), P(xh, OA)]
    ray(ax, r1, AXIAL, arrows=(0.5,) if o else ())
    ray(ax, r1[::-1], AXIAL, arrows=() if o else (0.5,))
    ray(ax, [P(xh, yy), P(xh, -18)], AXIAL, arrows=(0.4,))
dot(ax, P(0, 0), ms=3)
text(ax, "source", P(0, -3.8), size=7)
text(ax, "$O$", c0 + P(-4.2, -4.0), size=8)
text(ax, "$A$", P(30 - 3.6, OA + 3.2))
text(ax, "$B$", P(S1c[0] + 3.2, 7.2))
text(ax, "$S_2$", P(30 + 7.0, OA + 2.2))
text(ax, "$S_1$", P(S1c[0] + 3.4, -1.6))
text(ax, "$S_2'$", P(S1c[0] - 8.0, 8.8))
dim(ax, c0 + P(0, 0.0), c0 + P(0, OA), "$OA$", size=7, off=-8.0)
dim(ax, c0 + P(6.0, -9), c0 + P(OA, -9), "$OB$", size=7)
eye(ax, P(34 - 4 + 0, -22.0), 90, 1.8)
text(ax, "eye", P(34 + 2.0, -22.0), ha="left", size=7)
done(fig, HERE)
readme(HERE, "Fig 25.14: Michelson's interferometer as a method of Fizeau fringes", lines=["Construction schematic: equal arms OA = OB; the image S2' of the reference surface is drawn dashed, slightly tilted against S1 (wedge exaggerated).",
       "Labels from the figure: source, O, A, B, S1, S2, S2', OA, OB, eye. No numbers printed."])
