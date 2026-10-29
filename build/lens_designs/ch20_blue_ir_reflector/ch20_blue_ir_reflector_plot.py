from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.86: measured spectral transmittance of a multilayer reflecting the blue and near infrared (Fish-Schurman), traced."""
c = load_trace(HERE / "trace.csv")
fig, ax = figure(4.4, 2.8)
ax.plot(*c["phi0"], **CURVE)
ax.plot(*c["phi45"], **DASHED)
axes_setup(ax, "Wavelength in millimicrons", "Transmittance", (400, 1200), (0, 1.0), range(400, 1201, 100),
           [0, 0.2, 0.4, 0.6, 0.8, 1.0], yfmt=lambda v: f"{v:.1f}".lstrip("0") if 0 < v < 1 else f"{v:.1f}" if v else "0",
           minor=(50, 0.1))
ax.tick_params(right=False, which="both")
sec = ax.secondary_yaxis("right", functions=(lambda t: 1 - t, lambda r: 1 - r))
sec.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
sec.set_yticklabels(["0", ".2", ".4", ".6", ".8", "1.0"])
sec.yaxis.set_minor_locator(__import__("matplotlib.ticker", fromlist=["MultipleLocator"]).MultipleLocator(0.1))
sec.tick_params(direction="in", which="both")
sec.set_ylabel("Reflectance")
note(ax, r"$\phi = 0^\circ$", (765, 0.625), (850, 0.71), ha="left", size=8)
note(ax, r"$\phi = 45^\circ$", (733, 0.41), (640, 0.34), ha="right", size=8)
finish(fig, HERE, "Fig 20.86: measured spectral transmittance of a multilayer which reflects the blue and near infrared",
       ["Measured data (Fish-Schurman), no formula: traced from docs/scans/ch20.pdf page 66 (400 dpi) with `ch20_blue_ir_reflector_trace.py`.",
        "Ticks but no grid: affine fit to 17 ticks (digitize.tick_axes), residual 3 mu in x and 0.005 in T, so the curves are good to",
        "about 0.5 percent of either axis span (`trace.csv`). Where the two curves tangle (480-530 mu) the guides were read from a 5x zoom",
        "of the scan; through 600-700 mu the two curves lie on top of each other at T about .92 and are not separable to better than .01.",
        "phi = 0 degrees solid, phi = 45 degrees dashed, labels as printed. Right-hand axis as printed: Reflectance = 1 - T, 0 at the top.",
        "Axes as printed: 400-1200 mu, T 0 to 1.0.",
        "Spec correction: gap_pages_figure_specs.md gives 350-1000 mu and a single curve; the scan has two curves (phi = 0 and 45 degrees)",
        "on 400-1200 mu, and a second transmission band rising again beyond 1000 mu."])
