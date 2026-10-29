"""Fig 25.16: end mirror M1 relocated to B, above the prism, for testing a right-angle prism in the Twyman-Green
interferometer; B' is the in-line position it would have for a plate (dashed arc = the relocation)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

c0, w, px, s = P(40, 0), 3.0, 62.0, 7.0
fig, ax = canvas(TEXT_WIDTH * 0.85, (-6, 98), (-36, 40))
tg_common(ax, c0, w=w, ref_y=30.0, view_y=-20.0, x_src=-2.0, x_col=16.0)
ax.add_patch(plt.Polygon([(px, -s), (px, s), (px + 2 * s, s)], closed=True, **LENS))
mid = P(px + s, 0)
mirror(ax, P(px + s - 6, 2 * s + 2), P(px + s + 6, 2 * s + 2), side=1, lw=1.3)
B, Bp = P(px + s, 2 * s + 2), P(px + s + 2 * s + 2, 0)
mirror(ax, P(Bp[0], -6), P(Bp[0], 6), side=-1, lw=0.8, ticks=False)
line(ax, P(Bp[0], -6), P(Bp[0], 6), color=INK, linewidth=0.8, dashes=(3, 2))
rad = 2 * s + 2
th = np.radians(np.linspace(0, 90, 40))
ax.plot(mid[0] + rad * np.cos(th), rad * np.sin(th), **DASH)
head(ax, mid + rad * P(np.cos(th[-1]), np.sin(th[-1])), P(-0.3, 0.05), DASH)
for yy, o in ((w, True), (-w, False)):
    xh = px + s + (yy + s)  - s
    xh_hyp = px + (yy + s)
    a2 = [P(c0[0] + yy, yy), P(px, yy), P(xh_hyp, yy), P(xh_hyp, 2 * s + 2)]
    ray(ax, a2, AXIAL, arrows=(0.2,) if o else ())
    ray(ax, a2[::-1], AXIAL, arrows=() if o else (0.2,))
text(ax, "$B$", B + P(9.0, 0.0))
text(ax, "$B'$", Bp + P(4.0, 0.0))
text(ax, "$M_1$", B + P(-9.0, 0.0))
text(ax, "prism", P(px + 4.5, -s - 3.0), size=7)
text(ax, "$M_2$", P(c0[0] + 12.0, 30.0))
text(ax, "$A$", P(c0[0] - 12.5, 30.0))
text(ax, "$O$", c0 + P(-6.0, -3.8), size=8)
text(ax, "collimator", P(16, 10.0), size=7)
lab(ax, "beamsplitter", c0 + P(-3.5, 3.5), P(c0[0] - 13, 13), ha="right", size=7)
text(ax, "telescope", P(c0[0] + 9.5, -20), size=7, ha="left")
done(fig, HERE)
readme(HERE, "Fig 25.16: end mirror relocated for testing prisms in the Twyman-Green interferometer", lines=["Construction schematic: right-angle prism turning the beam 90 degrees by total reflection on its hypotenuse; M1 at B returns it.",
       "B' marks the in-line position; the dashed quarter circle is the relocation. Labels from the figure: collimator, beamsplitter, O, M2, A, prism, M1, B, B', telescope. No numbers printed."])
