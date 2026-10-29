"""Fig 23.5: vertical (incident-light) illumination. Source, field iris, condensers with the aperture diaphragm between them,
a 45 degree semi-reflector, and the objective, which is also its own condenser; the reflecting specimen returns the light
up through the objective and the semi-reflector to the image."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

xr, fo = 20.0, 14.0
fig, ax = canvas(TEXT_WIDTH * 0.7, (-6, 100), (-34, 48))
splitter(ax, P(xr, 0), 12, 45)
tlens(ax, P(xr, -16), 6.5, 0)
line(ax, P(xr - 5, -16 - fo), P(xr + 5, -16 - fo), color=INK, linewidth=1.8)
dot(ax, P(88, 0), ms=3.6)
tlens(ax, P(70, 0), 7)
stop_bars(ax, 58, 3.5, 8.0)
tlens(ax, P(46, 0), 7)
stop_bars(ax, 76, 2.5, 7.0)
w = 3.5
for yy, o in ((w, True), (-w, False)):
    xh = xr + yy
    ray(ax, [P(88, 0), P(70, yy * 1.3), P(46, yy)], AXIAL, arrows=(0.2,)) if o else ray(ax, [P(88, 0), P(70, yy * 1.3), P(46, yy)], AXIAL, arrows=())
    ray(ax, [P(46, yy), P(xh, yy)], AXIAL, arrows=(0.5,) if o else ())
    down = [P(xh, yy), P(xh, -16), P(xr, -16 - fo)]
    ray(ax, down, AXIAL, arrows=(0.3,) if o else (), segs=(0,))
    ray(ax, down[::-1], AXIAL, arrows=() if o else (0.3,))
    ray(ax, [P(xh, yy), P(xh, 36)], AXIAL, arrows=(0.5,) if not o else ())
head(ax, P(xr, 42), P(0, 1), AXIAL, 1.2)
text(ax, "to image", P(xr + 3, 42), ha="left", size=7)
text(ax, "light source", P(88, -4.5), size=7)
text(ax, "field iris\ndiaphragm", P(76, 10.5), size=7)
text(ax, "condensers", P(58, 11.5), size=7)
lab(ax, "aperture\ndiaphragm", P(58, -8.0), P(58, -15.5), size=7)
lab(ax, "45\u00b0 semi-reflector", P(xr + 4, 3.5), P(xr + 18, 14), ha="left", size=7)
text(ax, "objective", P(xr + 13, -16), size=7, ha="left")
text(ax, "specimen", P(xr + 10, -16 - fo), size=7, ha="left")
done(fig, HERE)
readme(HERE, "Fig 23.5: vertical illumination", lines=["Construction schematic: ideal condensers and objective; the objective focuses the source image on the specimen and collects the reflected light.",
       "Labels from the spec: light source, field iris diaphragm, condensers, aperture diaphragm, 45 degree semi-reflector, objective, specimen, to image. No numbers printed."])
