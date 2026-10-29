"""Trace Fig 20.121 off ch20 scan page 90 (400 dpi) into trace.csv: measured transmittance of a nine layer band pass filter at
normal incidence and phi = 30, 45 degrees.

The plot has an L-shaped axis with ticks hanging below the x axis and left of the y axis, so it is calibrated here directly.
Guides were read on a 1/1.35 preview (D), and on 3x (A) and 2x (B) zooms of the pass band; all are converted to page px."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

img = page_image("ch20", 90)
D = lambda pts: [(300 + 1.35 * x, 2150 + 1.35 * y) for x, y in pts]
A = lambda pts: [(1780 + x / 3, 2580 + y / 3) for x, y in pts]
B = lambda pts: [(1620 + x / 2, 2880 + y / 2) for x, y in pts]

# calibration: ticks 6-14 microns below the x axis, .10-1.00 left of the y axis
axis_col = rule_center(img, 702, 2900, False, half=20)
pix, data = [], []
for xv, cg in zip(range(6, 15), (817, 1060, 1306, 1553, 1801, 2048, 2295, 2541, 2791)):
    c = rule_center(img, cg, 3500, False, half=5, search=15)
    r = rule_center(img, c + 25, 3482 + (c - 702) * 13 / 2100, True, half=10, search=12)
    pix.append((c, r))
    data.append((xv, 0.0))
fx = np.polyfit([p[0] for p in pix], [d[0] for d in data], 1)
x_axis = np.polyval(fx, axis_col)
for yv, rg in zip(np.arange(1.0, 0.05, -0.1), (2255, 2380, 2504, 2627, 2747, 2868, 2990, 3111, 3237, 3358)):
    r = rule_center(img, axis_col - 12, rg, True, half=5, search=15)
    if np.isfinite(r):
        pix.append((axis_col, r))
        data.append((x_axis, round(yv, 2)))
ax = AffineAxes(pix, data)
print(f"calibration: {len(pix)} ticks, y axis at {x_axis:.3f} micron, residual x {ax.resid[0]:.3g}, y {ax.resid[1]:.3g}")

# feet near T = 0, read in page px off 3x and 4x zooms of the scan
foot = {"c_fall": [(1220, 3225), (1225, 3250), (1232, 3300), (1240, 3350), (1248, 3400), (1257, 3427), (1273, 3450),
                   (1300, 3463)],
        "b_fall": [(1233, 3163), (1240, 3200), (1250, 3250), (1255, 3300), (1263, 3350), (1272, 3400), (1283, 3433),
                   (1300, 3453), (1313, 3463)],
        "base_fall": [(1258, 3100), (1265, 3150), (1272, 3200), (1277, 3250), (1280, 3300), (1285, 3350), (1290, 3400),
                      (1297, 3437), (1310, 3457), (1333, 3467), (1367, 3470)],
        "rise1": [(1615, 3472), (1650, 3460), (1675, 3445), (1700, 3422), (1722, 3395), (1739, 3350), (1750, 3300), (1760, 3250)],
        "rise2": [(1645, 3471), (1675, 3465), (1700, 3455), (1720, 3437), (1742, 3400), (1757, 3350), (1772, 3300), (1784, 3250)],
        "rise3": [(1675, 3471), (1700, 3467), (1725, 3457), (1745, 3440), (1762, 3400), (1780, 3350), (1792, 3300), (1804, 3250)],
        "fall1": [(2087, 3250), (2095, 3300), (2107, 3350), (2130, 3400), (2155, 3437), (2180, 3457), (2212, 3475)],
        "fall2": [(2107, 3250), (2120, 3300), (2135, 3350), (2160, 3400), (2187, 3437), (2217, 3457), (2250, 3477)],
        "fall3": [(2131, 3250), (2142, 3300), (2160, 3350), (2187, 3400), (2220, 3445), (2250, 3465), (2277, 3477)]}
guides = {
    "base": D([(300, 900), (320, 910), (335, 900), (345, 850), (355, 795), (370, 790), (385, 810), (400, 812), (410, 790),
               (420, 750), (440, 742), (455, 760), (475, 782), (500, 790), (520, 800), (540, 830), (565, 845), (580, 830),
               (595, 740), (610, 685), (625, 685), (640, 730), (650, 790), (660, 830), (672, 828), (685, 760), (695, 690),
               (703, 673)]) + foot["base_fall"],
    "fall_b": D([(692, 748)]) + foot["b_fall"],
    "fall_c": D([(683, 797)]) + foot["c_fall"],
    "band_1": foot["rise1"] + B([(345, 350), (375, 150), (395, 0)])
              + A([(120, 900), (145, 750), (165, 600), (185, 400), (220, 300), (260, 235), (300, 190), (350, 160), (400, 155),
                   (450, 175), (520, 205), (590, 215), (650, 205), (700, 175), (760, 150), (790, 200), (820, 300), (840, 400),
                   (860, 550), (880, 700), (895, 850), (905, 950)])
              + B([(920, 0), (935, 200), (950, 400)]) + foot["fall2"],
    "band_2": foot["rise2"] + B([(375, 450), (395, 300), (420, 150), (440, 0)])
              + A([(175, 950), (190, 800), (210, 650), (225, 500), (245, 330), (270, 300), (310, 230), (350, 175), (380, 135),
                   (420, 105), (470, 95), (510, 105), (560, 140), (610, 180), (650, 195), (690, 165), (740, 150), (790, 140),
                   (830, 135), (870, 150), (910, 190), (935, 250), (950, 350), (965, 500), (980, 650), (990, 800), (1000, 950)])
              + B([(985, 0), (993, 200), (1005, 400)]) + foot["fall3"],
    "band_3": foot["rise3"] + B([(410, 450), (435, 300), (455, 150), (470, 0)])
              + A([(220, 950), (225, 900), (240, 750), (255, 600), (270, 480), (290, 330), (300, 275), (350, 300), (450, 318),
                   (520, 305), (600, 278), (650, 280), (700, 310), (730, 350), (750, 450), (770, 550), (790, 700), (810, 850),
                   (820, 950)])
              + B([(865, 0), (880, 200), (900, 400)]) + foot["fall1"],
}
trace_figure(HERE, 90, [], [], guides, (708, 2230, 2850, 3474),
             "Fig 20.121 traced from docs/scans/ch20.pdf p90 (x microns, y transmittance)", ax=ax, tol=5, smooth=9,
             masks=[(1818, 2685, 1852, 2712), (1795, 2750, 1854, 2779), (1778, 2801, 1832, 2827), (1735, 3030, 1842, 3060),
                    (2122, 3035, 2185, 3062), (1447, 3365, 1495, 3474), (1970, 2230, 1978, 3474), (2456, 2230, 2464, 3474)])
# printed annotation anchors (page px): label arrows, half-width arrows, the T = .005 pointer, label centres, axis end
anchors = {"normal_tip": (1850, 2700), "normal_tail": (1690, 2700), "phi30_tip": (1852, 2765), "phi30_tail": (1717, 2765),
           "phi45_tip": (1830, 2815), "phi45_tail": (1690, 2815), "hw_left_tip": (1840, 3045), "hw_left_tail": (1735, 3045),
           "hw_right_tip": (2117, 3047), "hw_right_tail": (2224, 3047), "t005_tip": (1454, 3478), "t005_tail": (1488, 3372),
           "normal_text": (1593, 2697), "phi30_text": (1603, 2758), "phi45_text": (1603, 2814), "t005_text": (1508, 3345),
           "hw_text": (2245, 3048), "hwr_text": (2240, 3140), "axis_end": (2850, 3493)}
with open(HERE / "trace.csv", "a") as f:
    for k, (pc, pr) in anchors.items():
        x, y = ax.data([pc], [pr])
        f.write(f"{k},{x[0]:.5g},{y[0]:.5g}\n")
