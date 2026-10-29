"""Fig 16.36: notation for objectives with axial symmetry and circular apertures of radius a. The spherical reference wavefront W
(radius R) leaves the exit pupil and converges on the geometrical focus O'; (x', y', z') are coordinates in the focal region, P' an
observation point there, R' the distance from a pupil element to P'."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

a, Rr = 14.0, 70.0
Op = P(Rr, 0)
fig, ax = canvas(TEXT_WIDTH * 0.85, (-10, 112), (-24, 28))
axis_line(ax, P(-6, 0), P(104, 0))
stop_bars(ax, 0.0, a, a + 6.0)
th = np.arcsin(a / Rr)
ph = np.linspace(-th, th, 60)
ax.plot(Rr - Rr * np.cos(ph), Rr * np.sin(ph), color=INK, linewidth=1.0)
for y_ in (a, a / 2, 0, -a / 2, -a):
    X = P(Rr - np.sqrt(Rr ** 2 - y_ ** 2), y_)
    ray(ax, [X, Op], AXIAL, arrows=(0.5,))
for s_ in (1, -1):
    line(ax, P(0, s_ * a), P(0, s_ * a), **THIN)
dim(ax, P(-5, 0), P(-5, a), "$a$", size=7.5)
line(ax, P(-6, a), P(0, a), **THIN)
line(ax, P(-6, 0), P(0, 0), **THIN)
dot(ax, Op, ms=2.8)
Pq = Op + P(14.0, 16.0)
dot(ax, Pq, ms=2.6)
for v, nm in ((P(1, 0), "$z'$"), (P(0, 1), "$y'$"), (unit(P(-0.8, -0.7)), "$x'$")):
    e = Op + v * 24
    line(ax, Op, e, color=INK, linewidth=0.6)
    head(ax, e, v, AXIAL, 0.9)
    text(ax, nm, e + v * 3.4)
Pe = P(0.0, a * 0.62)
ray(ax, [Pe, Pq], THIN, arrows=())
head(ax, (Pe + Pq) / 2, Pq - Pe, THIN, 1.0)
text(ax, "$R'$", (Pe + Pq) / 2 + P(-1.0, 6.2))
text(ax, "$P'$", Pq + P(3.0, 2.8), ha="left")
text(ax, "$O'$", Op + P(-3.0, -4.2))
text(ax, "$W$", P(Rr - Rr * np.cos(th) + 5.0, a + 4.5), size=9)
dim(ax, P(0, -a - 6), P(Rr, -a - 6), "$R$", size=7.5)
line(ax, P(0, -a - 5), P(0, -a), **THIN)
line(ax, P(Rr, -a - 5), P(Rr, -3), **THIN)
text(ax, "exit pupil", P(0, a + 10.5), size=7)
done(fig, HERE)
readme(HERE, "Fig 16.36: notation for objectives with axial symmetry and circular apertures", lines=["Construction schematic: ideal converging spherical wavefront W (radius R) from a pupil of radius a onto O'; focal-region axes drawn at O'.",
       "Labels from the spec: a, W, R, O', (x', y', z'), P', R'. x' is drawn as an oblique axis for the third dimension. No numbers printed."])
