from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.96: measured transmittance of band pass filters using both multilayer and glass absorption filters (Balzers)."""
c = load_trace(HERE / "trace.csv")
DASHDOT = dict(color=INK, linewidth=0.7, dashes=(5, 1.5, 1, 1.5))
style = {"1": DASHDOT, "2": DOTTED, "3": DASHDOT, "4": DASHED, "5": DASHDOT, "6": DOTTED, "7": CURVE}
fig, ax = figure(4.2, 2.7)
for k, st in style.items():
    ax.plot(*c[k], **st)
axes_setup(ax, "Wavelength in millimicrons", "Transmittance", (350, 775), (0, 1.0), [400, 500, 600, 700],
           [0, 0.2, 0.4, 0.6, 0.8, 1.0], yfmt=lambda v: "0" if v < 0.01 else f"{v:.2f}".lstrip("0") if v < 0.99 else "1.00",
           minor=(25, 0.1))
for k, x in zip("1234567", (411, 442, 484, 536, 594, 640, 708)):
    ax.text(x, 0.53, k, ha="center", va="center", fontsize=7.5, style="italic")
finish(fig, HERE, "Fig 20.96: measured transmittance of band pass filters using both multilayer and glass absorption filters",
       ["Measured data (Balzers), no formula. Source docs/scans/ch20.pdf page 72 (400 dpi), script `ch20_bandpass_balzers_trace.py`.",
        "HAND-READ, not snapped: the seven curves interleave dot for dot on a heavy grid, so automatic snapping jumped between them.",
        "Control points were read off 2x zooms, mapped through an affine fit to 144 grid intersections (residual 3.5 mu, 0.011 in T)",
        "and joined with a PCHIP interpolant; drawn back on the scan they sit on the ink. Accuracy about 1.5 percent of either span;",
        "worst where curves overlap near T = 0 (the feet between filters 1-3), where which foot belongs to which filter is ambiguous.",
        "Line styles follow the scan: 1, 3, 5 dash-dot; 2, 6 dotted; 4 dashed; 7 solid. Curve numbers as printed.",
        "Axes as printed: 350-775 mu (labels 400-700), T 0 to 1.00. The scan's graph-paper grid is not redrawn.",
        "Spec correction: gap_pages_figure_specs.md gives 300-1100 mu; the scan reads 350-775 mu, seven filters, peaks .73 to .92."])
