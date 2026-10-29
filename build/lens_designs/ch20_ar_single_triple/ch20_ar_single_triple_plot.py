from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.47: measured spectral reflectivity of single (quarter-wave MgF2) and triple-layer AR coatings (Fish-Schurman), traced."""
c = load_trace(HERE / "trace.csv")
fig, ax = figure(3.6, 3.6)
ax.plot(*c["triple"], **CURVE)
ax.plot(*c["mgf2"], **DASHED)
ax.plot(*c["uncoated"], **CURVE)
axes_setup(ax, "Wavelength in millimicrons", "Reflectance", (400, 750), (0, 0.0425), [400, 500, 600, 700],
           [0, 0.01, 0.02, 0.03, 0.04], yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0", minor=(50, 0.005))
note(ax, "Uncoated glass", (560, 0.0405), (560, 0.0355), size=7.5)
note(ax, r"$\lambda/4$ MgF$_2$", (520, 0.0136), (510, 0.0190), size=7.5)
note(ax, "Triple layer", (560, 0.0008), (555, 0.0058), size=7.5)
finish(fig, HERE, "Fig 20.47: measured spectral reflectivity of single and triple-layer antireflection coatings",
       ["Measured data (Fish-Schurman), no formula: traced from docs/scans/ch20.pdf page 38 (400 dpi) with `ch20_ar_single_triple_trace.py`.",
        "This plot has tick marks but no grid, so the pixel-to-data map is an affine fit to 16 ticks (digitize.tick_axes, residual",
        "0.4 mu in x and 0.0002 in R); the curves are good to about 0.5 percent of either axis span (`trace.csv`).",
        "Three curves as printed: triple layer (solid), quarter-wave MgF2 (dashed) and the uncoated-glass reflectance (solid, near the top,",
        "falling slightly from .0415 to .040 across the band). Labels and leaders as on the scan; the scan's 'Uncoated Class' is a misprint",
        "of 'Uncoated Glass' and is printed corrected. Axes as printed: 400-750 mu (labels every 100, ticks every 50), R 0 to .04.",
        "Spec correction: gap_pages_figure_specs.md gives R in percent to 5 and 4000-7000 A; the scan reads R to .04 and 400-750 mu,",
        "and the MgF2 minimum is about .0135, not 1.25 percent at 5500 A as the spec words it (close, but in different units)."])
