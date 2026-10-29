"""Fig 16.14: arrangement for Newton's rings. A source and collimating lens send a beam to a 45 degree semi-reflecting plate; it is
turned down onto a long-radius plano-convex lens resting, curved side down, on an optical flat. The air film has thickness
t = r^2 / 2R; the rings (dark centre) are seen through a microscope above the plate. Inset: the ring pattern, radii proportional to sqrt(k)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

xc, w = 34.0, 3.0
R = 90.0
fig, ax = canvas(TEXT_WIDTH * 0.66, (-8, 86), (-44, 50))
dot(ax, P(0, 0), ms=3.4)
tlens(ax, P(12, 0), 7)
splitter(ax, P(xc, 0), 14, 135)
ax.add_patch(plt.Rectangle((xc - 6, 20), 12, 26, facecolor="0.97", edgecolor=INK, linewidth=0.6, zorder=1))
tlens(ax, P(xc, 24), 4.0, 0)
tlens(ax, P(xc, 42), 4.0, 0)
y = np.linspace(-14, 14, 80)
sg = R - np.sqrt(R ** 2 - y ** 2)
poly = np.column_stack([np.r_[y + xc, xc + 14, xc - 14], np.r_[-30 - sg + 0, -22, -22]])
ax.add_patch(plt.Polygon(poly, closed=True, **LENS))
plate(ax, P(xc, -33.0), 40, 4.0, 0, **LENS)
line(ax, P(xc - 20, -31.0), P(xc + 20, -31.0), color=INK, linewidth=0.9, zorder=3)
dot(ax, P(xc, -31.0), ms=1.8)
for yy, o in ((w, True), (-w, False)):
    xh = xc - yy
    ray(ax, [P(12, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if o else ())
    ray(ax, [P(0, 0), P(12, yy)], OFFAXIS, arrows=())
    ray(ax, [P(xh, yy), P(xh, -31.0)], AXIAL, arrows=(0.5,) if o else ())
    ray(ax, [P(xh, -31.0), P(xh, 22)], AXIAL, arrows=() if o else (0.5,))
cx = P(72.0, -10.0)
for k in range(1, 6):
    ax.add_patch(plt.Circle(cx, 2.4 * np.sqrt(k), fill=False, edgecolor=INK, linewidth=0.5, zorder=2))
ax.add_patch(plt.Circle(cx, 0.9, facecolor=INK, edgecolor=INK, zorder=3))
text(ax, "Newton's rings", cx + P(0, -9.5), size=6.5)
text(ax, "source", P(0, -4.5), size=7)
text(ax, "microscope", P(xc + 9, 34), size=7, ha="left")
lab(ax, "semi-reflecting\nplate", P(xc + 3.5, 3.5), P(xc + 17, 13), ha="left", size=7)
lab(ax, "plano-convex lens", P(xc - 13, -26.0), P(xc - 28, -16), ha="center", size=7)
lab(ax, "optical flat", P(xc - 16, -33.0), P(xc - 28, -40.0), ha="center", size=7)
lab(ax, "air film", P(xc + 9, -30.2), P(xc + 24, -38.0), ha="left", size=7)
done(fig, HERE)
readme(HERE, "Fig 16.14: arrangement for Newton's rings or Newton's fringes", lines=["Construction schematic: ideal lens, 45 degree plate, lens of exaggerated curvature on a flat, microscope drawn as a tube with two ideal lenses.",
       "Labels from the spec: source, semi-reflecting plate, microscope, plano-convex lens, optical flat, air film, ring pattern inset (radii proportional to sqrt(k), dark centre). No numbers printed."])
