"""Fig 21.2: notation for Fresnel's coefficients at oblique incidence. Plane XZ is the plane of incidence;
the interface is the X axis (vertical here, at Z = 0); media (n0, K0) and (n1, K1); angles i0, i1; p = sin i0, q = cos i0."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

n0, n1, i0 = 1.0, 1.5, 38.0
i1 = np.degrees(np.arcsin(n0 * np.sin(np.radians(i0)) / n1))
L = 24.0
fig, ax = canvas(TEXT_WIDTH * 0.55, (-34, 36), (-26, 31))
line(ax, P(0, -24), P(0, 24), color=INK, linewidth=1.0)
ray(ax, [P(0, -24), P(0, 28)], dict(color=INK, linewidth=0), arrows=())
head(ax, P(0, 28), P(0, 1), THIN, 1.4)
line(ax, P(0, 24), P(0, 28), **THIN)
ray(ax, [P(-26, 0), P(33, 0)], dict(color=INK, linewidth=0), arrows=())
line(ax, P(-26, 0), P(33, 0), **THIN)
head(ax, P(33, 0), P(1, 0), THIN, 1.4)
dash(ax, P(-L - 2, 0), P(-1, 0))
inc = [P(-L * np.cos(np.radians(i0)), L * np.sin(np.radians(i0))), P(0, 0)]
tr = [P(0, 0), P(L * np.cos(np.radians(i1)), -L * np.sin(np.radians(i1)))]
ray(ax, inc, AXIAL, arrows=(0.45,))
ray(ax, tr, AXIAL, arrows=(0.55,))
arc(ax, P(0, 0), 11, 180 - i0, 180, "$i_0$", rt=1.3, size=7)
arc(ax, P(0, 0), 12, -i1, 0, "$i_1$", rt=1.4, size=7)
text(ax, "$X$", P(1.8, 28.5), ha="left")
text(ax, "$Z$", P(33.5, -2.2), ha="left")
text(ax, "$O$", P(1.4, -2.0), ha="left")
text(ax, r"$(n_0,\ K_0)$", P(-18, -16), size=8)
text(ax, r"$(n_1,\ K_1)$", P(20, 15), size=8)
text(ax, "$p = \\sin i_0$\n$q = \\cos i_0$", P(-32, 25), ha="left", va="top", size=8)
lab(ax, "direction of incidence", P(-17, 13.5), P(-33, 8), ha="left", size=7)
text(ax, "plane of incidence: $XZ$", P(33, -23), ha="right", size=7)
done(fig, HERE)
readme(HERE, "Fig 21.2: notation for Fresnel's coefficients at oblique incidence", lines=["Notation diagram; the refraction angle follows Snell's law for an illustrative n0 = 1.0, n1 = 1.5 (not printed).",
       "Labels from the figure: X, Z, O, (n0, K0), (n1, K1), i0, i1, p = sin i0, q = cos i0, direction of incidence, plane XZ."])
