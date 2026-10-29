"""Fig 25.24: experimental arrangement for a Foucault test of a mirror at its centre of curvature. Lamp and pinhole
(with a small prism) form a point source beside the centre of curvature C; the mirror returns its image F on the
other side; the knife edge K, on a transverse micrometer slide, cuts into the image while the eye behind it looks at the mirror."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

R = 70.0
s = 3.0
fig, ax = canvas(TEXT_WIDTH * 0.9, (-6, 110), (-31, 36))
axis_line(ax, P(-4, 0), P(R + 18, 0))
th = np.radians(np.linspace(-20, 20, 80))
ax.plot(R - R * np.cos(th), R * np.sin(th), color=INK, linewidth=1.4, zorder=3)
for t_ in np.radians(np.linspace(-19.5, 19.5, 17)):
    p0 = P(R - R * np.cos(t_), R * np.sin(t_))
    line(ax, p0, p0 + 2.6 * P(-np.cos(t_), np.sin(t_)) + P(0, 0.9), color=INK, linewidth=0.3)
S, F = P(R, s), P(R, -s)
dot(ax, S, ms=2.4)
dot(ax, F, ms=2.4)
for tt in (16, 8, -8, -16):
    M = P(R - R * np.cos(np.radians(tt)), R * np.sin(np.radians(tt)))
    ray(ax, [S, M, F], AXIAL, arrows=(0.45, 0.8), segs=(0, 1))
xp = R + 6.0
ax.add_patch(plt.Polygon([(xp - 4, s - 4), (xp + 4, s + 4), (xp - 4, s + 4)], closed=True, **LENS))
ax.add_patch(plt.Rectangle((xp - 7, 22), 14, 12, fill=False, edgecolor=INK, linewidth=0.5, linestyle=(0, (4, 2)), zorder=1))
ax.add_patch(plt.Circle((xp, 27), 3.0, facecolor="white", edgecolor=INK, linewidth=0.8, zorder=2))
ray(ax, [P(xp, 24), P(xp, s), S], AXIAL, arrows=(0.3, 0.85), segs=(0, 1))
for s_ in (1, -1):
    line(ax, P(R - 0.0, s + s_ * 1.0), P(R - 0.0, s + s_ * 1.0), color=INK, linewidth=0.5)
line(ax, P(R, F[1]), P(R, -12.0), color=INK, linewidth=2.4, solid_capstyle="butt")
line(ax, P(R - 8, -14.0), P(R + 20, -14.0), color=INK, linewidth=0.8)
for x in np.linspace(R - 8, R + 20, 12):
    line(ax, P(x, -14.0), P(x - 1.2, -15.8), color=INK, linewidth=0.3)
eye(ax, P(R + 12, F[1]), 180, 1.8)
text(ax, "$F$", F + P(-2.8, -1.8))
lab(ax, "knife edge, $K$", P(R, -9.5), P(R + 10, -9.0), ha="left", size=7)
lab(ax, "pinhole", S + P(0.4, 0.0), P(R + 12, 6.5), ha="left", size=7)
text(ax, "lamp", P(xp + 9.5, 27), size=7, ha="left")
text(ax, "eye", P(R + 14, F[1] + 4.2), size=7, ha="left")
text(ax, "concave mirror under test", P(8, -26), size=7, ha="left")
text(ax, "micrometer slide", P(R + 6, -20.0), size=7)
done(fig, HERE)
readme(HERE, "Fig 25.24: experimental arrangement for a Foucault test of a mirror", lines=["Construction schematic: spherical mirror of radius R (centre of curvature at R), pinhole source and knife edge either side of C (separation exaggerated).",
       "Labels from the figure: concave mirror, lamp, pinhole, F, knife edge K, eye, micrometer slide. No numbers printed."])
