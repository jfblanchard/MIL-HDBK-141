from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.45: measured reflectance of a quarter-half-quarter AR coating MgF2 + Nd2O3 + CeF3 on glass (ref. 31), traced."""
c = load_trace(HERE / "trace.csv")
fig, ax = figure(4.2, 2.5)
ax.plot(*c["reflectance"], **CURVE)
ax.plot([0.7, 1.7], c["uncoated"][1], **DASHED)
axes_setup(ax, "Wavelength in microns", "Reflectance", (0.7, 1.7), (0, 0.05), np.arange(0.7, 1.71, 0.1),
           [0, 0.01, 0.02, 0.03, 0.04, 0.05], xfmt=lambda v: f"{v:.1f}", yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0",
           minor=(0.05, 0.005))
note(ax, "Uncoated glass", (1.2, 0.0445), size=7)
finish(fig, HERE, "Fig 20.45: measured reflectance of a quarter-half-quarter antireflection coating, MgF2 + Nd2O3 + CeF3 on glass",
       ["Measured data (ref. 31), no formula: traced from docs/scans/ch20.pdf page 38 (400 dpi) with `ch20_ar_qhq_nd2o3_trace.py`",
        "(digitize.py: affine pixel-to-data fit to 40 grid intersections, absorbing the scan's tilt; hand-read guide snapped onto the ink).",
        "Fit residual 0.004 micron in x and 0.00013 in R: the curve is good to about 0.5 percent of either axis span (`trace.csv`).",
        "Curves as printed: the coating's reflectance (solid) and the uncoated-glass level (dashed, flat at R = 0.041).",
        "Axes as printed: 0.7-1.7 microns, R 0 to .05. The scan's graph-paper grid is not redrawn.",
        "Spec correction: gap_pages_figure_specs.md gives 400-750 mu and R in percent to 2.0; the scan reads 0.7-1.7 microns and R to .05."])
