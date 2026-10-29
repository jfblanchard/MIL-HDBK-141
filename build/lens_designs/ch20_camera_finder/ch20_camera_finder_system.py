"""Fig 20.88: a beam splitter in a camera deflects part of the image into the view finder. The objective
forms its image on the film; the 45 degree splitter sends a second image, at equal path length, to a ground glass
seen through a field lens and eyepiece."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

F, xs, yg = P(48, 0), 26.0, 22.0
fig, ax = canvas(TEXT_WIDTH * 0.55, (-12, 66), (-14, 60))
tlens(ax, P(0, 0), 10)
splitter(ax, P(xs, 0), 11, 45)
line(ax, P(48, -7), P(48, 7), color=INK, linewidth=2.0)
line(ax, P(xs - 7, yg), P(xs + 7, yg), color=INK, linewidth=0.9, dashes=(1.5, 1.2))
tlens(ax, P(xs, 31), 6, 0)
tlens(ax, P(xs, 41), 6, 0)
eye(ax, P(xs, 53.5), 90, 1.6)
for yy in (-7, 7):
    xh = (xs + yy) / (1 + yy / 48)
    H = P(xh, xh - xs)
    r = reflect(unit(F - P(0, yy)), P(-1, 1))
    G = H + r * (yg - H[1]) / r[1]
    ray(ax, [P(-11, yy), P(0, yy), H], AXIAL, arrows=(0.1,), segs=(0,))
    ray(ax, [H, F], AXIAL, arrows=(), segs=())
    ray(ax, [H, G], AXIAL, arrows=(0.5,))
    s = np.sign(yy)
    ray(ax, [P(xs, yg), P(xs + 4.2 * s, 31), P(xs + 3.0 * s, 41), P(xs + 3.0 * s, 50), P(xs, 52.0)], AXIAL, arrows=(0.2, 0.7))
text(ax, "objective", P(0, -12.5), size=7)
text(ax, "film", P(48, -9.5), size=7)
lab(ax, "beam splitter", P(xs + 3.4, 3.4), P(xs + 14, 11), ha="left", size=7)
lab(ax, "ground glass", P(xs + 7, yg), P(xs + 17, yg + 2), ha="left", size=7)
lab(ax, "field lens", P(xs + 6, 31), P(xs + 16, 31), ha="left", size=7)
lab(ax, "eyepiece", P(xs + 6, 41), P(xs + 16, 40), ha="left", size=7)
done(fig, HERE)
readme(HERE, "Fig 20.88: beam splitter in a camera, view-finder deflection", lines=["Construction schematic: ideal lenses, 45 degree splitter; film and ground glass are at equal path length from the splitter.",
       "Labels from the spec: objective, beam splitter, film, ground glass, field lens, eyepiece. No numbers printed."])
