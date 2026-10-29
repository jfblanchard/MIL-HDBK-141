"""Fig 22.3: examples of basic scanning systems: (a) single detector, (b) linear detector array, (c) mosaic detector array.
Each panel shows the field, the objective, and the detector side; fields of view are drawn as the figure describes them."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

fig, ax = canvas(TEXT_WIDTH * 0.8, (-4, 112), (-146, 8))
def field(x0, y0, w, h):
    ax.add_patch(plt.Rectangle((x0, y0), w, h, fill=False, edgecolor=INK, linewidth=0.7, linestyle=(0, (4, 2)), zorder=1))
def rect(x0, y0, w, h, fc="white"):
    ax.add_patch(plt.Rectangle((x0, y0), w, h, facecolor=fc, edgecolor=INK, linewidth=0.7, zorder=2))
def curved(cx, cy, r, a0, a1):
    th = np.radians(np.linspace(a0, a1, 30))
    ax.plot(cx + r * np.cos(th), cy + r * np.sin(th), color=INK, linewidth=0.6)
    for a, s in ((a1, 1), (a0, -1)):
        t = np.radians(a)
        head(ax, P(cx + r * np.cos(t), cy + r * np.sin(t)), s * P(-np.sin(t), np.cos(t)), AXIAL, 0.9)
# (a) single detector
y = -14.0
field(0, y - 12, 26, 24)
rect(11.5, y - 1.3, 2.6, 2.6, fc=INK)
tlens(ax, P(50, y), 9)
curved(50, y, 12.5, 100, 140)
curved(50, y, 12.5, -140, -100)
line(ax, P(74, y - 8), P(74, y + 8), color=INK, linewidth=1.6)
tlens(ax, P(86, y), 5)
rect(96, y - 3, 7, 6, fc=INK)
for s in (1, -1):
    ray(ax, [P(26, y + s * 1.3), P(50, y + s * 6), P(74, y)], OFFAXIS, arrows=())
    ray(ax, [P(74, y), P(86, y + s * 4), P(96, y + s * 1.5)], OFFAXIS, arrows=())
text(ax, "total field scanned", P(13, y + 15), size=6.5)
lab(ax, "instantaneous\nfield of view", P(14.2, y - 1.0), P(36, y - 20), size=6.5)
text(ax, "objective", P(50, y - 14.5), size=6.5)
text(ax, "vertical scanning\nmotion", P(50, y + 19.5), size=6.5)
text(ax, "reticle", P(74, y + 11), size=6.5)
text(ax, "field lens", P(86, y + 9), size=6.5)
text(ax, "detector", P(99.5, y - 8.5), size=6.5)
text(ax, "(a)", P(-3, y + 23), size=8, ha="left")
# (b) linear array
y = -68.0
field(0, y - 14, 20, 28)
rect(8.5, y - 14, 3.0, 28, fc="0.6")
tlens(ax, P(50, y), 9)
for k in range(7):
    rect(92, y - 11 + k * 3.4, 3.0, 2.6, fc=INK)
for s in (1, -1):
    ray(ax, [P(11.5, y + s * 13), P(50, y + s * 6), P(92, y + s * 11)], OFFAXIS, arrows=())
text(ax, "total field scanned", P(10, y + 17.5), size=6.5)
lab(ax, "instantaneous\nfield of view", P(10, y - 8), P(30, y - 21), size=6.5)
text(ax, "objective", P(50, y - 13.5), size=6.5)
text(ax, "linear detector array", P(93.5, y - 17.5), size=6.5)
text(ax, "(b)", P(-3, y + 23), size=8, ha="left")
# (c) mosaic array
y = -120.0
field(0, y - 11, 24, 22)
for i in range(4):
    for j in range(4):
        line(ax, P(0 + i * 6, y - 11), P(0 + i * 6, y + 11), color=INK, linewidth=0.3)
        line(ax, P(0, y - 11 + j * 5.5), P(24, y - 11 + j * 5.5), color=INK, linewidth=0.3)
tlens(ax, P(50, y), 9)
for i in range(4):
    for j in range(4):
        rect(88 + i * 3.6, y - 7.2 + j * 3.6, 2.8, 2.8, fc=INK)
for s in (1, -1):
    ray(ax, [P(24, y + s * 11), P(50, y + s * 6), P(88, y + s * 7)], OFFAXIS, arrows=())
text(ax, "instantaneous and\ntotal field of view", P(12, y + 17.0), size=6.5)
text(ax, "objective", P(50, y - 13.5), size=6.5)
text(ax, "mosaic detector array", P(95.5, y - 12.5), size=6.5)
text(ax, "(c)", P(-3, y + 23), size=8, ha="left")
done(fig, HERE)
readme(HERE, "Fig 22.3: examples of basic scanning systems", lines=["Construction schematic: three panels (a) single detector, (b) linear detector array, (c) mosaic detector array; ideal objective, fields of view as dashed rectangles.",
       "Labels from the spec: total field scanned, instantaneous field of view, objective, vertical and azimuth scanning motion, reticle, field lens, detector, linear/mosaic detector array. No numbers printed.",
       "FLAG-PARTIAL: the double-headed scan arrow of panel (b) and the lead wires on the detector elements are not reproduced."])
