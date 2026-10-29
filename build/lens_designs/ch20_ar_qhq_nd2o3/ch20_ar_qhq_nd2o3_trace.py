"""Trace Fig 20.45 off ch20 scan page 38 (400 dpi) into trace.csv: measured reflectance and the uncoated-glass level."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

xs = [round(0.7 + 0.1 * i, 1) for i in range(11)]
ys = [0.05, 0.04, 0.03, 0.02, 0.01, 0.0]
trace_figure(HERE, 38, list(zip(xs, [2000, 2100, 2203, 2305, 2408, 2510, 2612, 2715, 2818, 2920, 3025])),
             list(zip(ys, [402, 505, 609, 712, 815, 918])),
             {"reflectance": [(2005, 700), (2050, 770), (2100, 845), (2150, 890), (2200, 912), (2300, 918), (2400, 898),
                              (2500, 892), (2620, 895), (2710, 880), (2810, 830), (2910, 760), (2980, 690), (3022, 645)],
              "uncoated": [(2010, 492), (2300, 494), (2900, 500), (3015, 502)]},
             (1980, 380, 3045, 935), "Fig 20.45 traced from docs/scans/ch20.pdf p38 (x microns, y reflectance)",
             flat={"uncoated"}, smooth=41, skip={(x, y) for x in xs for y in (0.04, 0.0)})
