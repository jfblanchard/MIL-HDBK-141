"""Fig 16.7: amplitude reflection and transmission at an interface (Snell geometry, arbitrary n0 < n1)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

n0, n1, i0 = 1.0, 1.5, 40.0
i1 = np.degrees(np.arcsin(n0 * np.sin(np.radians(i0)) / n1))
L = 26.0
fig, ax = canvas(TEXT_WIDTH * 0.55, (-34, 34), (-24, 25))
line(ax, P(0, -22), P(0, 22), color=INK, linewidth=1.0)
dash(ax, P(-L - 4, 0), P(L + 4, 0))
din = P(np.sin(np.radians(i0)), -np.cos(np.radians(i0)))
inc = [P(0, 0) - din * L, P(0, 0)]
ax.plot([-L * np.cos(np.radians(i0))], [0], alpha=0)
inc = [P(-L * np.cos(np.radians(i0)), L * np.sin(np.radians(i0))), P(0, 0)]
refl = [P(0, 0), P(-L * np.cos(np.radians(i0)), -L * np.sin(np.radians(i0)))]
tr = [P(0, 0), P(L * np.cos(np.radians(i1)), -L * np.sin(np.radians(i1)))]
ray(ax, inc, AXIAL, arrows=(0.5,))
ray(ax, refl, AXIAL, arrows=(0.55,))
ray(ax, tr, AXIAL, arrows=(0.55,))
arc(ax, P(0, 0), 10, 180 - i0, 180, "$i_0$", rt=1.3, size=7)
arc(ax, P(0, 0), 10, 180, 180 + i0, "$i_0$", rt=1.3, size=7)
arc(ax, P(0, 0), 12, -i1, 0, "$i_1$", rt=1.4, size=7)
text(ax, "$A_0$", inc[0] + P(-1, 2.2), ha="right")
text(ax, "$rA_0$", refl[1] + P(-1, -2.2), ha="right")
text(ax, "$tA_0$", tr[1] + P(1.5, -2.2), ha="left")
text(ax, "$n_0$", P(-27, 18), size=9)
text(ax, "$n_1$", P(27, 18), size=9)
text(ax, "normal", P(33, 0), ha="left", size=6.5)
done(fig, HERE)
readme(HERE, "Fig 16.7: transmittance and reflectance at a translucent interface",
       lines=["Construction schematic. Angles follow Snell's law for an illustrative n0 = 1.0, n1 = 1.5 (not printed on the figure; the book prints only the symbols).",
              "Labels: n0, n1, i0, i1, A0, rA0, tA0, surface normal."])
