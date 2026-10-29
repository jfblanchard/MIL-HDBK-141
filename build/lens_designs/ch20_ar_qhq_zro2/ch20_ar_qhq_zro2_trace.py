"""Trace Fig 20.44 off ch20 scan page 38 (400 dpi) into trace.csv: measured reflectance, absorption, uncoated glass."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from digitize import *  # noqa: E402,F403

img = page_image("ch20", 38)
xs, ys = range(400, 901, 50), [0.05, 0.04, 0.03, 0.02, 0.01, 0.0]
ax = calibrate(img, list(zip(xs, [597, 697, 798, 900, 1004, 1106, 1211, 1312, 1412, 1512, 1612])),
               list(zip(ys, [387, 486, 593, 693, 797, 903])), skip={(x, 0.04) for x in xs} | {(x, 0.0) for x in xs})
ink = (img < 140) & ~rule_mask(img.shape, ax, xs, ys[:-1], xr=(400, 900), yr=(0, 0.05), width=4)
guides = {
    "reflectance": [(600, 645), (620, 760), (640, 830), (660, 860), (690, 882), (720, 888), (810, 875), (910, 865),
                    (1010, 872), (1110, 887), (1210, 898), (1260, 903), (1305, 905), (1360, 885), (1420, 860), (1480, 825),
                    (1520, 790)],
    "absorption": [(602, 790), (630, 820), (660, 845), (690, 870)],
    "uncoated": [(605, 473), (1595, 481)],
}
paths, out = [], []
for name, g in guides.items():
    c, r, frac = snap(ink, g, tol=12, smooth=41)
    x, y = ax.data(c, r)
    paths.append((c, r))
    print(f"{name}: {frac:.0%} of samples on ink, x {x.min():.0f}-{x.max():.0f}")
    if name == "uncoated":  # straight dashed rule; the snap catches the lettering above it, so keep the median level
        y = np.full_like(y, np.median(y))
        x = np.array([400.0, 900.0]); y = y[:2]
    if name == "absorption":  # past 439 mu the snap runs into the label's leader line
        keep = x <= 439
        x, y = x[keep], y[keep]
    out.append((name, x, y))
overlay_paths(img, (560, 360, 1640, 930), paths, "/tmp/mil_scan_cache/f2044_overlay.png", guides.values())
with open(HERE / "trace.csv", "w") as f:
    f.write("# Fig 20.44 traced from docs/scans/ch20.pdf p38; curve, wavelength_mu, reflectance\n")
    for name, x, y in out:
        for a, b in zip(x[::3] if x.size > 2 else x, y[::3] if y.size > 2 else y):
            f.write(f"{name},{a:.1f},{b:.5f}\n")
