"""Trace Fig 20.46 off ch20 scan page 38 (400 dpi) into trace.csv: measured reflectance and the uncoated-glass level."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

xs = [round(0.08 + 0.01 * i, 2) for i in range(11)]
ys = [0.05, 0.04, 0.03, 0.02, 0.01, 0.0]
trace_figure(HERE, 38, list(zip(xs, [1250, 1350, 1452, 1552, 1652, 1755, 1855, 1958, 2060, 2163, 2265])),
             list(zip(ys, [1302, 1407, 1510, 1612, 1714, 1817])),
             {"reflectance": [(1255, 1535), (1290, 1565), (1320, 1620), (1350, 1700), (1390, 1760), (1450, 1790),
                              (1550, 1800), (1650, 1802), (1750, 1798), (1850, 1793), (1950, 1775), (2050, 1735),
                              (2150, 1670), (2262, 1580)],
              "uncoated": [(1260, 1395), (1700, 1398), (2255, 1403)]},
             (1235, 1285, 2285, 1835), "Fig 20.46 traced from docs/scans/ch20.pdf p38 (x microns as printed, y reflectance)",
             flat={"uncoated"}, smooth=41, skip={(x, y) for x in xs for y in (0.04, 0.0)})
