from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.87: measured spectral transmittance of a multilayer heat reflecting filter (Balzers), traced."""
c = load_trace(HERE / "trace.csv")
fig, ax = figure(4.4, 2.7)
ax.plot(*c["transmittance"], **CURVE)
axes_setup(ax, "Wavelength in millimicrons", "Transmittance", (350, 1200), (0, 1.0), range(400, 1101, 100),
           np.arange(0, 1.01, 0.1), yfmt=lambda v: "0" if v < 0.05 else "1.0" if v > 0.95 else f"{v:.1f}".lstrip("0"),
           minor=(50, 0.05))
finish(fig, HERE, "Fig 20.87: measured spectral transmittance of a multilayer heat reflecting filter",
       ["Measured data (Balzers), no formula: traced from docs/scans/ch20.pdf page 66 (400 dpi) with `ch20_heat_filter_balzers_trace.py`.",
        "Affine pixel-to-data fit to 144 grid intersections; the graph paper is hand-ruled and uneven, so the residual is 6 mu in x and",
        "0.01 in T: the curve is good to about 1 percent of either axis span (`trace.csv`). The ripple band (400-720 mu) was guided from",
        "4x zooms of the scan. From 850 to 1050 mu the curve lies on the frame's zero line (T under .01) and is drawn there.",
        "Axes as printed: 350-1200 mu (labels 400-1100), T 0 to 1.0. The scan's graph-paper grid is not redrawn.",
        "Spec correction: gap_pages_figure_specs.md says low IR transmittance through 1200 mu; the scan shows T rising again past",
        "1100 mu to about .5 at the 1200 mu frame edge."])
