"""Trace Fig 20.101 off ch20 scan page 75 (400 dpi) into trace.csv: measured transmittance of a Fabry-Perot multilayer filter."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

img = page_image("ch20", 75)
ax = tick_axes(img, (2282, 3033, 2926), [(780, 2282), (790, 2445), (800, 2608), (810, 2767), (820, 2926)],
               [(0.0, 3033, "l")] + [(round(0.1 * k, 1), r, "l") for k, r in
                                     zip(range(1, 10), (2943, 2850, 2758, 2665, 2572, 2480, 2385, 2292, 2200))], inside=20)
o = np.array([1850, 1950])
guide = np.array([(560, 1075), (600, 1055), (625, 1000), (640, 900), (650, 800), (658, 700), (665, 550), (672, 400),
                  (685, 310), (697, 298), (710, 320), (722, 400), (735, 550), (745, 680), (755, 780), (770, 880), (790, 980),
                  (810, 1045), (850, 1070), (900, 1076)]) + o
trace_figure(HERE, 75, [], [], {"transmittance": guide}, (2290, 2112, 2920, 3026),
             "Fig 20.101 traced from docs/scans/ch20.pdf p75 (x millimicrons, y transmittance)", ax=ax, tol=10, smooth=9,
             masks=[(2540, 2975, 2556, 3030), (2415, 2633, 2496, 2657), (2607, 2633, 2697, 2657), (2562, 2232, 2660, 2254)])
# lambda_0 tick (printed inside the bottom edge) and the half-width arrows' level
lx = ax.data([rule_center(img, 2547, 3005, False, half=10)], [3033])[0][0]
hy = ax.data([2400], [rule_center(img, 2455, 2645, True, half=20)])[1][0]
with open(HERE / "trace.csv", "a") as f:
    f.write(f"lambda0,{lx:.5g},0\nhalfwidth_level,0,{hy:.5g}\n")
print("lambda0", lx, "arrow level", hy)
