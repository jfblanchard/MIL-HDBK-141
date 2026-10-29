"""Fig 16.27: movement of an interference fringe x to x + dx by the introduction of a film of thickness t. Wedge of angle alpha
between a reference flat and the substrate; fringes lie where the air gap is d = m lambda / 2; over the film the gap is smaller by t,
so the same gap is reached further along the wedge, at x + dx."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

al = np.radians(7.0)
xe, t, d_ = 48.0, 4.0, 6.0
gap = lambda x: 2.0 + x * np.tan(al)
fig, ax = canvas(TEXT_WIDTH * 0.82, (-6, 100), (-30, 20))
line(ax, P(0, 0), P(96, 0), color=INK, linewidth=1.1)
hatch_block(ax, 0, 1.2, 96, 3.4)
xs = np.array([0.0, xe, xe, 96.0])
ys = np.array([-gap(0), -gap(xe), -gap(xe) + t, -gap(96) + t])
sub = np.column_stack([xs, ys])
ax.add_patch(plt.Polygon(np.vstack([sub, [[96, -26], [0, -26]]]), closed=True, **LENS))
ax.plot(xs, ys, color=INK, linewidth=1.1)
x1 = (d_ - 2.0) / np.tan(al)
x2 = (d_ - 2.0 + t) / np.tan(al)
for x_ in (x1, x2):
    line(ax, P(x_, 0), P(x_, -(d_ if x_ == x1 else d_ - t) - 0.0), color=INK, linewidth=0.5, dashes=(3, 2))
line(ax, P(x1, 0), P(x1, -d_), color=INK, linewidth=0.5, dashes=(3, 2))
line(ax, P(x2, 0), P(x2, -d_), color=INK, linewidth=0.5, dashes=(3, 2))
dim(ax, P(x1, 5.5), P(x2, 5.5), "$\\Delta x$", size=7)
line(ax, P(x1, 1.0), P(x1, 6.5), **THIN)
line(ax, P(x2, 1.0), P(x2, 6.5), **THIN)
text(ax, "$x$", P(x1, 9.5), size=8)
text(ax, "$x + \\Delta x$", P(x2 + 3.0, 9.5), size=8)
line(ax, P(xe, -gap(xe)), P(xe, -gap(xe) + t), color=INK, linewidth=0.5)
dim(ax, P(xe - 3.5, -gap(xe)), P(xe - 3.5, -gap(xe) + t), "", size=7)
text(ax, "$t$", P(xe - 7.5, -gap(xe) + t / 2), size=8)
lab(ax, "$\\alpha$", P(8, -gap(8) + 0.0), P(8, -20), size=8)
lab(ax, "film", P(xe + 10, -gap(xe + 10) + t * 0.5), P(xe + 14, -20), size=7)
text(ax, "reference flat", P(10, 7.0), size=7)
text(ax, "substrate", P(70, -24), size=7)
text(ax, "$d = m\\lambda/2$", P(x1 - 3, -d_ * 0.5), ha="right", size=7.5)
done(fig, HERE)
readme(HERE, "Fig 16.27: movement of an interference fringe by the introduction of a film", lines=["Geometry drawn from the figure's relations: gap d = m lambda/2 at x, same gap reached at x + dx over the film of thickness t. Wedge angle exaggerated (7 degrees).",
       "Labels from the spec: alpha, t, x, x + delta x, d = m lambda/2, reference flat, substrate, film. No numbers printed. Caption typo is only in the caption text, not the figure."])
