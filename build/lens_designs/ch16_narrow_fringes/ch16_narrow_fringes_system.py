"""Fig 16.26: appearance of the narrow fringes when the film (below the edge AB) is a small fraction of a wavelength thick.

Line drawing at the scan's own layout (drawing units = scan pixels / 100 on a 1/1.4 preview of ch16 p40, y up): narrow
fringes of order nu, nu+1, nu+2 above the film edge AB, the same orders below it shifted by Delta x, equal spacings h."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

Q = lambda x, y: P(x / 100, -y / 100)
FR = dict(color=INK, linewidth=1.1, solid_capstyle="butt", zorder=3)
fig, ax = canvas(4.4, (-0.6, 14.8), (-8.7, -0.35))
ye, top, bot, r = -4.58, -1.30, -7.70, 0.15
xs_up = np.array([4.63, 7.80, 10.97])
dx = 0.52
xs_dn = xs_up + dx
line(ax, P(1.10, ye), P(14.50, ye), color=INK, linewidth=1.4, solid_capstyle="butt", zorder=3)
th = np.linspace(np.pi, 1.5 * np.pi, 20)
for x in xs_up:     # each narrow fringe turns into the edge with a small rounded corner, as drawn
    ax.plot([x, x], [top, ye + r], **FR)
    ax.plot(x + r + r * np.cos(th), ye + r + r * np.sin(th), **FR)
for x in xs_dn:
    ax.plot([x, x], [ye, bot], **FR)
dash(ax, P(xs_dn[0], ye), P(xs_dn[0], -2.55), linewidth=0.6, dashes=(3.5, 2.5))
for (a, b), y in ((xs_up[:2], -2.15), (xs_up[1:], -2.15), (xs_dn[:2], -6.85), (xs_dn[1:], -6.85)):
    dim(ax, P(a, y), P(b, y), "$h$", size=8.5)
arr = dict(arrowstyle=ARROW, color=INK, lw=0.5, shrinkA=0, shrinkB=0)
ax.annotate("", P(xs_up[0], -3.65), P(xs_up[0] - 1.25, -3.65), arrowprops=arr)
ax.annotate("", P(xs_dn[0], -3.65), P(xs_dn[0] + 0.9, -3.65), arrowprops=arr)
text(ax, r"$\Delta x$", P((xs_up[0] + xs_dn[0]) / 2, -3.38), size=8)
for xs, y, va in ((xs_up, -1.70, "center"), (xs_dn, -7.40, "center")):
    for x, s in zip(xs, (r"$\nu$", r"$\nu+1$", r"$\nu+2$")):
        text(ax, s, P(x + 0.1, y), ha="left", va=va, size=8.5)
text(ax, "$A$", Q(370, 432), size=8.5)
text(ax, "$B$", Q(1153, 440), size=8.5)
text(ax, "narrow fringe\n" + r"of order $\nu$", Q(450, 75), size=8, linespacing=1.1)
text(ax, "shifted fringe\n" + r"of order $\nu$", Q(495, 822), size=8, linespacing=1.1)
text(ax, "edge of\nfilm", Q(40, 565), ha="left", size=8, linespacing=1.1)
done(fig, HERE)
readme(HERE, "Fig 16.26: appearance of the narrow fringes when the film thickness is a small fraction of a wavelength", lines=[
    "Line drawing at the scan's own layout (docs/scans/ch16.pdf page 40): the film edge AB, narrow fringes of order nu, nu+1, nu+2 above",
    "it (each turning into the edge with a small rounded corner, as printed), the same orders below the edge shifted by Delta x, a",
    "dashed extension of the shifted order-nu fringe, and the equal fringe spacings h above and below. Labels as printed (sentence",
    "case, as in the other ch16 schematics). The shift Delta x is drawn at the scan's proportion (about h/6); no numbers are printed.",
    "The caption's relation Delta x / h = 2t / lambda (step height from the fringe shift) is in the text, not on the figure, and is not",
    "added. Caption typo 'expiramental' is the book's (sic). Spec correction: the spec calls this a 'rectangular field' with hatched",
    "fringes; the scan has no frame and draws each fringe as a single line."])
