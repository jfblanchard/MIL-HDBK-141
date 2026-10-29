"""Trace Fig 20.85 off ch20 scan page 66 (400 dpi) into trace.csv: solid measured curve and its dashed continuation."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

img = page_image("ch20", 66)
ax = tick_axes(img, (455, 1805, 1582),
               [(0.4, 455), (0.5, 605), (0.6, 753), (0.7, 902), (0.8, 1055), (0.9, 1200), (1.0, 1350), (1.1, 1502)],
               [(0.0, 1805, "l"), (0.1, 1645, "l"), (0.2, 1487, "l"), (0.3, 1327, "l"), (0.4, 1167, "l"), (0.5, 1008, "l"),
                (0.6, 848, "l"), (0.7, 688, "l"), (0.8, 522, "l")])
o = np.array([150, 280])
solid = np.array([(312, 240), (330, 170), (370, 130), (405, 90), (435, 110), (460, 100), (485, 88), (540, 122), (580, 112),
                  (595, 120), (605, 200), (625, 285), (650, 240), (680, 208), (695, 250), (700, 405), (710, 700), (718, 1045),
                  (725, 1250), (745, 1330), (770, 1390), (800, 1440), (850, 1480), (900, 1500), (950, 1505)]) + o
dashed = np.array([(955, 1505), (1000, 1495), (1050, 1470), (1100, 1420), (1150, 1350), (1180, 1250), (1200, 1050),
                   (1220, 800), (1240, 500), (1255, 400), (1280, 375), (1300, 390), (1320, 500), (1335, 650), (1350, 710),
                   (1375, 715), (1400, 650), (1420, 590), (1428, 570)]) + o
trace_figure(HERE, 66, [], [], {"solid": solid, "dashed": dashed}, (462, 370, 1576, 1798),
             "Fig 20.85 traced from docs/scans/ch20.pdf p66 (x microns, y transmittance)", ax=ax, tol=13, smooth=15,
             masks=[(480, 730, 838, 950), (500, 1280, 830, 1430)])
# the three circled points printed on the curve (T = .70, the .30 cut-off, and the knee near .05), and the right frame edge
mx, my = ax.data([850, 872, 950], [685, 1327, 1720])
redge = ax.data([rule_center(img, 1582, 1100, False, half=8)], [1805])[0][0]
with open(HERE / "trace.csv", "a") as f:
    f.write("".join(f"marker,{a:.5g},{b:.5g}\n" for a, b in zip(mx, my)) + f"edge,{redge:.5g},0\n")
