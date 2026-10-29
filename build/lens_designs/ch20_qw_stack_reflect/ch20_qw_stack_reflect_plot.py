from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.95: measured reflectivity of quarter-wave stacks with 5, 7, 9 layers and a 15-layer ZnS/cryolite broad-band reflector (B)."""
c = load_trace(HERE / "trace.csv")
ylo = 0.775
fig, ax = figure(TEXT_WIDTH, 3.2)
for k in ("n5", "n7", "n9", "B"):
    ax.plot(*c[k], **CURVE)
ax.plot(*c["circle"], "o", ms=3.2, mfc="white", mec=INK, mew=0.6, zorder=3)
axes_setup(ax, "Wavelength in millimicrons", "Reflectance", (378, 762), (ylo, 1.0), [400, 500, 600, 700], [0.8, 0.9, 1.0],
           yfmt=lambda v: f"{v:.1f}", minor=(50, 0.05))
for txt, xy in (("(B)", (655, 0.917)), ("(9)", (614, 0.892)), ("(7)", (583, 0.862)), ("(5)", (573, 0.835))):
    note(ax, txt, xy, size=8)
finish(fig, HERE, "Fig 20.95: measured spectral reflectivity of 5, 7 and 9 layer quarter-wave stacks and a 15-layer broad-band reflector",
       ["Measured data (ref. 49), no formula: traced from docs/scans/ch20.pdf page 72 (400 dpi) with `ch20_qw_stack_reflect_trace.py`",
        "(digitize.py: affine fit to the printed grid intersections, which absorbs the scan's tilt; hand-read guides snapped onto the ink).",
        "Four curves as printed, labelled (5), (7), (9) and (B) for the 15-layer ZnS/cryolite reflector; (B)'s open circles are the scan's",
        "own measured points, placed where they are printed. Axes as printed: R from the frame at about .775 up to 1.0 (labels 0.8, 0.9,",
        "1.0), wavelength 400-750 mu with the frame running a little past both ends. The scan's grid is not redrawn.",
        "Spec correction: gap_pages_figure_specs.md gives R 0-100 percent and peaks of 90/96/99 percent; the scan is a suppressed-zero",
        "plot (.775-1.0) with peaks of about .87 (5), .95 (7), .98 (9), and (B) rippling between .93 and .96."])
