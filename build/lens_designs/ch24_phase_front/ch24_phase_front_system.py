"""Fig 24.2: determination of the constant-phase front from ray-tracing data. Rays start on the reference plane P-P (points
K, D, B, F, C), travel as parallel rays to the entrance pupil plane E-E, cross the optical system, and leave as an aberrated
fan. The surface of equal optical path (K', D', B', F', C') is drawn as the parallel surface of the exit wavefront, so every ray is
normal to it. The aberrated fan here has primary spherical aberration of illustrative size."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

f, k, x0 = 44.0, 0.004, 52.0
ys = np.array([13.0, 6.5, 0.0, -6.5, -13.0])
names = ["K", "D", "B", "F", "C"]
slope = lambda y: -y / (f - k * y ** 2)
zW = lambda y: -(1 / (2 * k)) * np.log(f - k * y ** 2) + (1 / (2 * k)) * np.log(f)     # sag so that rays are normal to W
fig, ax = canvas(TEXT_WIDTH * 0.95, (-8, 116), (-20, 22))
axis_line(ax, P(-6, 0), P(112, 0))
line(ax, P(0, -17), P(0, 17), color=INK, linewidth=0.8)
line(ax, P(22, -17), P(22, 17), color=INK, linewidth=0.8, dashes=(5, 2))
ax.add_patch(plt.Rectangle((30, -17), 18, 34, facecolor="0.95", edgecolor=INK, linewidth=0.8, zorder=1))
text(ax, "OPTICAL\nSYSTEM", P(39, 0), size=7)
for y, n in zip(ys, names):
    ray(ax, [P(0, y), P(30, y)], AXIAL, arrows=(0.5,))
    pt = P(x0 + zW(y), y)
    d = unit(P(1.0, slope(y)))
    ray(ax, [P(48, y), pt], OFFAXIS, arrows=())
    ray(ax, [pt, pt + d * 52], AXIAL, arrows=(0.28,))
    text(ax, n, P(-2.2, y), ha="right")
    wp = pt + d * 14.0
    dot(ax, wp, ms=2.2)
    text(ax, n + "'", wp + P(2.8, 1.8), ha="left")
yy = np.linspace(-13.0, 13.0, 120)
pts = np.array([P(x0 + zW(y), y) + unit(P(1.0, slope(y))) * 14.0 for y in yy])
ax.plot(pts[:, 0], pts[:, 1], color=INK, linewidth=0.9, zorder=3)
text(ax, "$P$-$P$", P(0, 19.0), size=7.5)
text(ax, "$E$-$E$", P(22, 19.0), size=7.5)
text(ax, "reference plane", P(0, -19.5), size=6.5)
text(ax, "entrance pupil", P(22, -19.5), size=6.5)
lab(ax, "surface of equal\noptical path", pts[0] + P(0, 0), P(100, 18.0), ha="center", size=7)
done(fig, HERE)
readme(HERE, "Fig 24.2: determination of constant phase front from ray tracing data", lines=["Construction schematic: aberrated fan with illustrative primary spherical aberration; the equal-optical-path surface is the parallel surface of the exit wavefront, so rays are normal to it.",
       "Labels from the spec: P-P, E-E, K D B F C, K' D' B' F' C', OPTICAL SYSTEM. No numbers printed.",
       "FLAG-PARTIAL: the spec lists ray-length labels 'u', 'Pr', 'L' whose placement is not recoverable from the text; they are not drawn."])
