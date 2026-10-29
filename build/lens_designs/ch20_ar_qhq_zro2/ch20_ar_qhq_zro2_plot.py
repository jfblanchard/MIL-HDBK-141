from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.44: measured reflectance of a quarter-half-quarter AR coating MgF2 + ZrO2 + CeF3 on glass (ref. 31), traced."""
c = load_trace(HERE / "trace.csv")
fig, ax = figure(4.2, 2.5)
ax.plot(*c["reflectance"], **CURVE)
ax.plot(*c["absorption"], color=INK, linewidth=0.7, dashes=(2, 1.2))
ax.plot(*c["uncoated"], **DASHED)
axes_setup(ax, "Wavelength in millimicrons", "Reflectance", (400, 900), (0, 0.05), range(400, 901, 100),
           [0, 0.01, 0.02, 0.03, 0.04, 0.05], yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0", minor=(50, 0.005))
note(ax, "Uncoated glass", (650, 0.0445), size=7)
note(ax, "Absorption in coating", (428, 0.0049), (500, 0.0085), ha="left", size=7)
finish(fig, HERE, "Fig 20.44: measured reflectance of a quarter-half-quarter antireflection coating, MgF2 + ZrO2 + CeF3 on glass",
       ["Measured data (ref. 31), no formula: traced from docs/scans/ch20.pdf page 38 (400 dpi) with `ch20_ar_qhq_zro2_trace.py`",
        "(digitize.py: affine pixel-to-data fit to 40 grid intersections, which absorbs the scan's tilt; hand-read guide snapped onto the ink).",
        "Fit residual 2.3 mu in x and 0.0002 in R, so the curves are good to about 0.5 percent of either axis span; the trace is in `trace.csv`.",
        "Three curves as printed: the coating's reflectance (solid), absorption in the coating (short dashed curve, 400-450 mu) and the",
        "uncoated-glass level (dashed, a flat R = 0.041). The reflectance touches zero from about 700 to 755 mu and runs along the frame there. Axes as printed: 400-900 mu, R 0 to .05. The scan's graph-paper grid is not redrawn.",
        "Spec correction: gap_pages_figure_specs.md gives 400-750 mu and R in percent to 2.0; the scan reads 400-900 mu and R to .05."])
