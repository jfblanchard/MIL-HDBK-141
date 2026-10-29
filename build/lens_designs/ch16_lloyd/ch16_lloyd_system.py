"""Fig 16.4: Lloyd's mirror. S1 at height h above a front-surface mirror, virtual source S2 at -h,
screen at D; direct and reflected beams overlap between the mirror plane and the grazing limit."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

h, xm0, xm1, xs = 6.0, 9.0, 60.0, 64.0
S1, S2 = P(0, h), P(0, -h)
fig, ax = canvas(TEXT_WIDTH * 0.75, (-9, 84), (-17, 17))
mirror(ax, P(xm0, 0), P(xm1, 0), side=-1, lw=1.4)
line(ax, P(xs, -0.5), P(xs, 16), color=INK, linewidth=0.8)
dot(ax, S1)
dot(ax, S2, mfc="white")
for yq in (2.0, 5.0, 12.5):
    ray(ax, [S1, P(xs, yq)], AXIAL, arrows=(0.45,))
for yq in (2.0, 5.0):
    Q = P(xs, yq)
    M = hit(S2, unit(Q - S2), P(xm0, 0), P(xm1, 0))
    ray(ax, [S1, M, Q], AXIAL, arrows=(0.3,))
    dash(ax, S2, M)
edge = hit_x(S2, unit(P(xm1, 0) - S2), xs)
dash(ax, S2, P(xm1, 0))
text(ax, "$S_1$", S1 + P(-1.5, 0.8), ha="right")
text(ax, "$S_2$", S2 + P(-1.5, -0.8), ha="right")
text(ax, "$M$", P(4, -2.4))
dim(ax, P(-6, 0), P(-6, h), "$h$", size=7)
dim(ax, P(-6, 0), P(-6, -h), "$h$", size=7)
line(ax, P(-5.5, h), P(-1, h), **THIN)
line(ax, P(-5.5, -h), P(-1, -h), **THIN)
line(ax, P(-5.5, 0), P(8, 0), **THIN)
dim(ax, P(0, -11), P(xs, -11), "$D$", size=7)
line(ax, P(0, -7.5), P(0, -12), **THIN)
line(ax, P(xs, -0.5), P(xs, -12), **THIN)
head(ax, P(xs + 4, 9.5), P(0, 1), THIN)
line(ax, P(xs + 4, edge[1]), P(xs + 4, 9.5))
line(ax, P(xs, edge[1]), P(xs + 4, edge[1]), **THIN)
text(ax, "region of\ninterference", P(xs + 6, 6), ha="left", size=7)
lab(ax, "dark fringe at mirror plane\n($\\pi$ phase change on reflection)", P(xs, 0.0), P(27, -7.2), ha="center", size=7)
text(ax, "screen", P(xs, 17.5), size=7)
done(fig, HERE)
readme(HERE, "Fig 16.4: Lloyd's mirror", lines=["Construction schematic (ideal front-surface mirror; the book gives symbols only).",
       "Symbols as named by the figure: S1, S2, M, h, D, interference region on the screen, pi phase change at the mirror plane.",
       "h and D are drawn to a convenient scale; no numeric values are printed."])
