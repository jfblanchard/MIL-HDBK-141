"""Fig 16.32: convention for the integral statement of Huygens' principle, drawn in the plane containing the source point P0,
the surface element d(sigma) and the observation point P: surface sigma, outward normal n, vectors r0 (P0 to d sigma) and r
(d sigma to P), angles theta0 and theta measured from the normal. Obliquity factor chi = (cos theta0 + cos theta)/2."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

P0, Pp = P(-4.0, 20.0), P(80.0, 26.0)
fig, ax = canvas(TEXT_WIDTH * 0.8, (-12, 92), (-22, 34))
yy = np.linspace(-20, 24, 120)
xs_ = 36.0 + 0.012 * (yy - 2) ** 2 * -1 + 0.0
ax.plot(xs_, yy, color=INK, linewidth=1.2)
ys = 3.0
O = P(36.0 + 0.0, ys)
tang = unit(P(-0.024 * (ys - 2) * -1 * -1, 1.0))
n = unit(P(1.0, 0.024 * (ys - 2) * 0.0 + 0.0))
n = rot(tang, -90)
if n[0] < 0:
    n = -n
line(ax, O - 4 * tang, O + 4 * tang, color=INK, linewidth=3.0, solid_capstyle="butt", zorder=4)
ray(ax, [P0, O], AXIAL, arrows=(0.5,))
ray(ax, [O, Pp], AXIAL, arrows=(0.5,))
ray(ax, [O - n * 10, O + n * 16], THIN, arrows=())
head(ax, O + n * 16, n, THIN, 1.2)
dot(ax, P0, ms=3.0)
dot(ax, Pp, ms=3.0)
a0 = np.degrees(np.arctan2(*(-(P0 - O))[::-1]))
a_n = np.degrees(np.arctan2(n[1], n[0]))
a1 = np.degrees(np.arctan2(*(Pp - O)[::-1]))
arc(ax, O, 12, a0, a_n, "$\\theta_0$", rt=1.5, size=7.5)
arc(ax, O, 9, a_n, a1, "$\\theta$", rt=1.65, size=7.5)
text(ax, "$P_0$", P0 + P(-1.5, 2.8), ha="right")
text(ax, "$P$", Pp + P(2.0, 2.4), ha="left")
text(ax, "$r_0$", (P0 + O) / 2 + P(0, 3.0))
text(ax, "$r$", (O + Pp) / 2 + P(0, 3.0))
text(ax, "$\\vec{n}$", O + n * 19.5 + P(1.5, 0.0), size=8)
lab(ax, "$d\\sigma$", O + P(0.4, -3.5), P(30, -15), size=8)
text(ax, "$\\sigma$", P(34.0, -21), size=9)
done(fig, HERE)
readme(HERE, "Fig 16.32: convention for the integral statement of Huygens' principle", lines=["Geometry drawn in the plane through P0, d sigma and P: surface sigma, normal n, vectors r0 and r, angles theta0 and theta from the normal.",
       "Labels from the spec: P0, P, r0, r, theta0, theta, n, d sigma, sigma. The obliquity factor in the spec is an equation, not a drawn label, and is not printed. No numbers printed.",
       "FLAG-NOTE: the spec says the angle theta0 is taken against the inward normal (or n); here both angles are drawn against the outward normal n."])
