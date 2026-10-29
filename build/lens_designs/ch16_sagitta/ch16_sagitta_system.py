"""Fig 16.15: the sagitta method when the reference surface S2 is a sphere. Test surface S1 (radius R1) and spherical reference S2
(radius R2) touch on the axis; at radial height y their sags are s1 = y^2/2R1 and s2 = y^2/2R2, leaving an air gap of s1 - s2."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

R1, R2, ym = 60.0, 100.0, 30.0
fig, ax = canvas(TEXT_WIDTH * 0.6, (-40, 52), (-6, 40))
y = np.linspace(-ym - 4, ym + 4, 120)
s1 = R1 - np.sqrt(R1 ** 2 - y ** 2)
s2 = R2 - np.sqrt(R2 ** 2 - y ** 2)
ax.plot(y, s1, color=INK, linewidth=1.1)
ax.plot(y, s2, color=INK, linewidth=1.1)
line(ax, P(0, -4), P(0, 38), color="0.45", linewidth=0.35, dashes=(8, 2, 1.5, 2), zorder=0)
S1y, S2y = R1 - np.sqrt(R1 ** 2 - ym ** 2), R2 - np.sqrt(R2 ** 2 - ym ** 2)
dash(ax, P(0, S1y), P(ym + 5, S1y))
dash(ax, P(0, S2y), P(ym + 5, S2y))
dim(ax, P(ym + 4, 0), P(ym + 4, S2y), "$s_2$", size=7)
dim(ax, P(ym + 4, S2y), P(ym + 4, S1y), "$\\Delta s$", size=7)
dim(ax, P(ym + 12, 0), P(ym + 12, S1y), "$s_1$", size=7)
line(ax, P(ym, 0), P(ym + 13, 0), **THIN)
dim(ax, P(-ym, S1y + 5), P(0, S1y + 5), "", size=7)
dim(ax, P(0, S1y + 5), P(ym, S1y + 5), "$y$", size=7)
line(ax, P(ym, S1y), P(ym, S1y + 6), **THIN)
line(ax, P(0, S1y), P(0, S1y + 6), **THIN)
dot(ax, P(0, 0), ms=2.4)
text(ax, "$O$", P(2.6, -2.2))
lab(ax, "$S_1$ ($R_1$)", P(-18, R1 - np.sqrt(R1 ** 2 - 18 ** 2)), P(-34, 22), size=7.5, ha="center")
lab(ax, "$S_2$ ($R_2$)", P(-20, R2 - np.sqrt(R2 ** 2 - 20 ** 2)), P(-34, 4.0), size=7.5, ha="center")
done(fig, HERE)
readme(HERE, "Fig 16.15: the sagitta method when the reference surface S2 is a sphere", lines=["Geometry drawn from the figure's own relations s = y^2/2R (radii R1 = 60 and R2 = 100 drawing units, illustrative only).",
       "Labels from the spec: S1 (R1), S2 (R2), y, s1, s2, delta s. No numbers are printed on the figure."])
