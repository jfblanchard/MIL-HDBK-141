"""Fig 25.25: schematic demonstration of the sensitivity of Foucault testing. A surface element at O tilted by theta
from the reference sphere turns the reflected ray through 2 theta, displacing the focus from F to F'."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

R, s, th = 70.0, 3.5, np.radians(2.2)
fig, ax = canvas(TEXT_WIDTH * 0.9, (-8, 96), (-22, 18))
tt = np.radians(np.linspace(-12, 12, 60))
ax.plot(R - R * np.cos(tt), R * np.sin(tt), color=INK, linewidth=1.0, zorder=3)
O = P(0, 0)
S, F = P(R, s), P(R, -s)
d_in = unit(O - S)
nrm = P(1.0, 0.0)
d_ref = reflect(d_in, nrm)
Fp = hit_x(O, rot(d_ref, 2 * np.degrees(th)), R)
tilt = P(-np.sin(th), np.cos(th))
line(ax, O - 6 * tilt, O + 6 * tilt, color=INK, linewidth=1.8, zorder=4)
ray(ax, [S, O], AXIAL, arrows=(0.5,))
ray(ax, [O, F], AXIAL, arrows=(0.55,))
ray(ax, [O, Fp], DASH, arrows=(0.55,))
dot(ax, S, ms=2.4); dot(ax, F, ms=2.4); dot(ax, Fp, ms=2.4)
arc(ax, O, 24, np.degrees(np.arctan2(*(F - O)[::-1])), np.degrees(np.arctan2(*(Fp - O)[::-1])), r"$2\theta$", rt=1.5, size=8)
dim(ax, F, Fp, "", size=7, off=7.0)
text(ax, "$O$", P(-3.2, 1.6))
text(ax, "$F$", F + P(2.5, 0.6), ha="left")
text(ax, "$F'$", Fp + P(2.5, 0.0), ha="left")
text(ax, "pinhole", S + P(2.5, 0.8), ha="left", size=7)
lab(ax, r"slope error $\theta$", O + P(-0.3, 5.0), P(18, 14), ha="left", size=7)
text(ax, "reference sphere", P(-7.0, -15.5), ha="left", size=7)
done(fig, HERE)
readme(HERE, "Fig 25.25: schematic demonstration of the sensitivity of Foucault testing", lines=["Construction schematic: a surface element tilted by theta deviates the reflected ray by 2 theta; angles exaggerated.",
       "Labels from the figure: O, theta, 2 theta, F, F', pinhole. No numbers printed."])
