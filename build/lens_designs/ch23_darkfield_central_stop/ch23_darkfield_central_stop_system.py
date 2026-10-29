"""Fig 23.12: refracting condenser with a central stop for dark-field illumination. The stop blocks the axial rays; the
remaining hollow cone is brought to the specimen on the slide at an angle steeper than the objective accepts, so only
light diffracted or scattered by the specimen enters the objective."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

ys, yl = 0.0, -22.0
fig, ax = canvas(TEXT_WIDTH * 0.5, (-28, 40), (-44, 30))
line(ax, P(-7, -34), P(7, -34), color=INK, linewidth=2.6, solid_capstyle="butt")
biconvex(ax, -24.0, 12.0, 4.0, 60.0, vertical=True)
th = np.linspace(np.pi, 2 * np.pi, 60)
phi = np.linspace(np.pi, 2 * np.pi, 60)
dome = np.column_stack([11 * np.cos(phi), -12.0 + 11 * np.sin(phi) * 0.9 + 0 * phi])
ax.add_patch(plt.Polygon(np.vstack([dome, [[11, -12.0], [-11, -12.0]]]), closed=True, **LENS))
plate(ax, P(0, -7.0), 40, 2.2, 0, **LENS)
dot(ax, P(0, -6.0 + 0.0), ms=1.8)
tlens(ax, P(0, 8.0), 4.0, 0)
spec = P(0, -6.0)
for xi in (6.0, 9.0, -6.0, -9.0):
    xe = xi * 0.55
    ray(ax, [P(xi, -34.0 + 0.0), P(xi, -22.0), spec], AXIAL, arrows=(0.2, 0.8), segs=(0, 1))
    d = unit(spec - P(xi, -22.0))
    ray(ax, [spec, spec + d * 24], AXIAL, arrows=(0.5,))
ray(ax, [spec, P(1.2, 8.0), P(0.8, 14.0)], DASH, arrows=(0.5,))
ray(ax, [spec, P(-1.2, 8.0), P(-0.8, 14.0)], DASH, arrows=(0.5,))
c = P(22.0, -34.0)
ax.add_patch(plt.Circle(c, 6.5, facecolor="white", edgecolor=INK, linewidth=0.6, zorder=2))
ax.add_patch(plt.Circle(c, 2.6, facecolor=INK, edgecolor=INK, zorder=3))
text(ax, "central stop\n(top view)", c + P(0, -10.0), size=7)
lab(ax, "central stop", P(0, -34.0), P(-20, -41.5), size=7)
lab(ax, "condenser", P(-7, -25.0), P(-22, -26.0), ha="right", size=7)
lab(ax, "slide", P(18, -7.0), P(26, 4.0), ha="left", size=7)
lab(ax, "specimen", spec, P(24, -13.0), ha="left", size=7)
text(ax, "objective", P(0, 18.5), size=7)
text(ax, "direct rays miss\nthe objective", P(-14, 14), ha="right", size=7)
done(fig, HERE)
readme(HERE, "Fig 23.12: refracting condenser with a central stop for dark-field illumination", lines=["Construction schematic: ideal hollow-cone illumination; the condenser is drawn as a lens plus a plano-convex dome (no prescription in the book).",
       "Labels from the spec: central stop (with top view), condenser, slide, specimen, objective. Dashed rays: light scattered by the specimen. No numbers printed."])
