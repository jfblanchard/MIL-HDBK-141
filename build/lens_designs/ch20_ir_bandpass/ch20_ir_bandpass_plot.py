from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.97: measured spectral transmittance of some infrared band pass filters, complete with auxiliaries (Bausch and Lomb)."""
c = load_trace(HERE / "trace.csv")
fig, ax = figure(3.8, 2.9)
for k in ("f8", "f9", "f10", "f11", "f12"):
    ax.plot(*c[k], **CURVE)
axes_setup(ax, "Wavelength in microns", "Transmittance", (6, 14), (0, 1.0), range(6, 15), [0, 0.2, 0.4, 0.6, 0.8, 1.0],
           yfmt=lambda v: "0" if v < 0.01 else f"{v:.2f}".lstrip("0") if v < 0.99 else "1.00", minor=(0.5, 0.1))
finish(fig, HERE, "Fig 20.97: measured spectral transmittance of some infrared band pass filters, complete with auxilliaries (sic)",
       ["Measured data (Bausch and Lomb), no formula: traced from docs/scans/ch20.pdf page 72 (400 dpi) with `ch20_ir_bandpass_trace.py`.",
        "Ticks but no grid: affine fit to 16 ticks (digitize.tick_axes; the 10-micron tick is too faint to find and was skipped),",
        "residual 0.03 micron in x and 0.007 in T, so the curves are good to about 0.5 percent of either span (`trace.csv`).",
        "Five filters as printed, all solid, unlabelled on the scan; peaks about .57 (8.1 microns), .51 (8.9), .47 (10.0), .38 (10.9)",
        "and .33 (12.0). A faint dotted fold line in the scan at 10.43 microns is masked; the curves crossing it are bridged. The scan's in-figure heading 'Measured transmittance of a series of band pass filters complete with",
        "auxiliaries' repeats the caption and is dropped (house style: no in-figure title). Axes as printed: 6-14 microns, T 0 to 1.00.",
        "Spec correction: gap_pages_figure_specs.md gives 1-5 microns and T to 80 percent; the scan reads 6-14 microns, T to 1.00."])
