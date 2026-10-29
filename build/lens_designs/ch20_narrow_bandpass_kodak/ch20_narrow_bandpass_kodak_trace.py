"""Trace Fig 20.120 off ch20 scan page 90 (400 dpi) into trace.csv: measured transmittance of a narrow band pass filter."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

img = page_image("ch20", 90)
ax = tick_axes(img, (1192, 1505, 2220), [(4.2, 1192), (4.4, 1555), (4.5, 1740), (4.6, 1920)],
               [(0.0, 1505, "l"), (0.1, 1350, "l"), (0.2, 1195, "l"), (0.3, 1038, "l"), (0.4, 880, "l"), (0.5, 723, "l")],
               inside=20)
o = np.array([1000, 300])
guide = np.array([(475, 1200), (520, 1185), (560, 1150), (600, 1100), (630, 1040), (650, 950), (658, 850), (665, 750),
                  (680, 650), (695, 500), (705, 440), (720, 410), (738, 402), (760, 415), (790, 440), (810, 460), (818, 500),
                  (822, 600), (825, 700), (828, 800), (835, 900), (850, 1000), (870, 1080), (890, 1135), (920, 1170),
                  (970, 1195), (1000, 1202)]) + o
trace_figure(HERE, 90, [], [], {"transmittance": guide}, (1200, 570, 2212, 1498),
             "Fig 20.120 traced from docs/scans/ch20.pdf p90 (x microns, y transmittance)", ax=ax, tol=6, smooth=9,
             masks=[(1600, 694, 1716, 707), (1733, 530, 1747, 697), (1672, 1092, 1822, 1108), (1500, 975, 1655, 1098),
                    (1588, 1421, 1878, 1438), (1890, 960, 1980, 1420)])
# printed annotation geometry: the two dashed rejection limits (their top), the .08 and .15 micron arrow levels
x43 = ax.data([rule_center(img, 1370, 1350, False, half=30)], [1505])[0][0]
x47 = ax.data([rule_center(img, 2102, 1350, False, half=30)], [1505])[0][0]
top = ax.data([1370], [1212])[1][0]
a08 = ax.data([1745], [rule_center(img, 1745, 1100, True, half=20)])[1][0]
a15 = ax.data([1745], [rule_center(img, 1745, 1430, True, half=20)])[1][0]
xr = ax.data([rule_center(img, 2220, 1000, False, half=20)], [1505])[0][0]
with open(HERE / "trace.csv", "a") as f:
    f.write(f"reject,{x43:.5g},{top:.5g}\nreject,{x47:.5g},{top:.5g}\narrow08,0,{a08:.5g}\narrow15,0,{a15:.5g}\nedge,{xr:.5g},0.6\n")
print(x43, x47, top, a08, a15, xr)
