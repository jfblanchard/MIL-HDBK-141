from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 25.27: isophotal lines and intensity distribution for a true mirror under the Foucault test, knife edge central (after Linfoot).

With the knife edge through the focus (edge along y), Linfoot's eq. (11) for a uniformly lit circular mirror gives the image
field (1/2)[A - i H_x A], H_x the Hilbert transform across the edge. For the unit circle the chord at height y has half-width
a = sqrt(1 - y^2), so
    I(x, y) = (1/4) [ A(x, y)^2 + (1/pi^2) ln^2 |(x + a) / (x - a)| ]   for |y| < 1,  and 0 for |y| >= 1,
with A = 1 inside the mirror. The bright rim at A, A' is the logarithmic singularity at the mirror edge."""
K = 42.0            # the book's intensity scale is arbitrary; K puts the centre value at 10.5, as read off the scan


def intensity(x, y):
    a = np.sqrt(np.clip(1 - y ** 2, 0, None))
    with np.errstate(divide="ignore", invalid="ignore"):
        lg = np.log(np.abs((x + a) / (x - a)))
    inside = (np.abs(x) < a).astype(float)
    return np.where(np.abs(y) < 1, 0.25 * (inside + (lg / np.pi) ** 2), 0.0) * K


# isophote levels: the crossings of the horizontal diameter read off the scan (x in mirror radii), converted to levels
outside = [3.08, 2.30, 1.83, 1.46]
inside = [0.33, 0.52, 0.675, 0.86]
levels = sorted(float(intensity(np.array([x]), np.array([0.0]))[0]) for x in outside + inside)

fig = plt.figure(figsize=(4.6, 4.3))
top = fig.add_axes([0.08, 0.56, 0.84, 0.40])
x = np.linspace(-3.15, 3.15, 1601)
y = np.linspace(-0.999, 0.999, 801)
X, Y = np.meshgrid(x, y)
Z = intensity(X, Y)
top.contour(X, Y, np.clip(Z, 0, 200), levels=levels, colors=INK, linewidths=0.6, linestyles=[(0, (3.5, 2))] * 8)
top.plot([-3.2, 3.2], [0, 0], color=INK, lw=0.5)
top.plot([0, 0], [-1.12, 1.12], color=INK, lw=0.5)
top.set_xlim(-3.25, 3.25)
top.set_ylim(-1.25, 1.25)
top.set_aspect("equal")
top.axis("off")
top.text(0.06, 1.13, "$B$", ha="left", va="center", fontsize=8)
top.text(0.06, -1.15, "$B'$", ha="left", va="center", fontsize=8)
top.text(0.07, 0.1, "$O$", ha="left", va="bottom", fontsize=8)

ax = fig.add_axes([0.08, 0.08, 0.84, 0.40])
xs = np.concatenate([np.linspace(-3.0, -1.0005, 1500), np.linspace(-0.9995, 0.9995, 3000), np.linspace(1.0005, 3.0, 1500)])
I = intensity(xs, np.zeros_like(xs))
ax.plot(xs, I, **CURVE)
for e in (-1, 1):
    ax.plot([e, e], [0, 28], color=INK, lw=0.8)
ax.set_xlim(-3.05, 3.05)
ax.set_ylim(0, 28)
ax.set_xticks([-1, 0, 1])
ax.set_xticklabels(["$A'$", "$O$", "$A$"])
ax.set_yticks([0, 10, 20])
ax.tick_params(right=True, labelright=True, top=False)
for s in ("top",):
    ax.spines[s].set_visible(False)
ax.text(-3.0, 26.5, "$I$", ha="left", va="center", fontsize=8.5)
finish(fig, HERE, "Fig 25.27: isophotal lines and intensity distribution for a mirror under the Foucault test, knife edge central (after Linfoot)",
       ["COMPUTED, not traced. Linfoot's eq. (11) (book 25.10.2.2) applied to a perfect, uniformly lit circular mirror with the knife edge",
        "through the focus gives the image field (1/2)[A - i H_x A], H_x the Hilbert transform across the edge; for the unit circle",
        "I = (1/4)[A^2 + (1/pi^2) ln^2|(x+a)/(x-a)|], a = sqrt(1 - y^2) (x, y in mirror radii, A = 1 inside the mirror, I = 0 for |y| >= 1).",
        "Check against the scan's intensity curve (docs/scans/ch25.pdf page 27), with the book's arbitrary scale fitted by one factor",
        "K = 42 so the centre O sits at 10.5 as printed: x = 0.5 gives 11.8 (scan about 12.3), x = 0.9 gives 19.7 (about 21), two radii",
        "outside the rim gives 1.3 (about 1.3). The rim A, A' is a logarithmic singularity, drawn as the scan does with vertical lines at",
        "the edge; the plot is clipped at 28.",
        "Isophotes: the book does not give the contour levels. They are the formula's values at the eight crossings of the horizontal",
        "diameter read off the scan (x = 0.33, 0.52, 0.675, 0.86 inside, 1.46, 1.83, 2.30, 3.08 outside); each level also has its partner",
        "contour on the other side of the rim. As on the scan, the outer isophotes close at B and B' (the top and bottom of the mirror,",
        "where the chord vanishes) and the inner ones crowd toward the rim. Axes and labels as printed: B, B', O; A', O, A; I with 0, 10, 20",
        "on both sides. The two captions under each panel are the book's and stay in the text."])
