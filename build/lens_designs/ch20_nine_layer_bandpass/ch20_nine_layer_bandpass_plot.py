from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.121: measured spectral transmittance of a nine layer band-pass filter with a nearly rectangular pass band (Bausch and Lomb)."""
c = load_trace(HERE / "trace.csv")
P = lambda k: (c[k][0][0], c[k][1][0])
x0, xe = 5.547, P("axis_end")[0]
fig, ax = figure(TEXT_WIDTH, 3.6)
for k in ("base", "fall_b", "fall_c", "band_1", "band_2", "band_3"):
    ax.plot(*c[k], **CURVE)
axes_setup(ax, "Wavelength in microns", "Measured Transmittance", (x0, xe), (0, 1.0), range(6, 15), np.arange(0, 1.01, 0.1),
           yfmt=lambda v: "0" if v < 0.05 else f"{v:.2f}".lstrip("0") if v < 0.99 else "1.00")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.tick_params(direction="out", top=False, right=False)
arrow = dict(arrowstyle="-|>,head_length=0.5,head_width=0.18", color=INK, lw=0.6, shrinkA=0, shrinkB=0)
for k, txt in (("normal", "Normal"), ("phi30", r"$\phi$ = 30"), ("phi45", r"$\phi$ = 45")):
    ax.annotate("", P(k + "_tip"), P(k + "_tail"), arrowprops=arrow)
    ax.text(P(k + "_tail")[0] - 0.05, P(k + "_text")[1], txt, ha="right", va="center", fontsize=8)
for k in ("hw_left", "hw_right"):
    ax.annotate("", P(k + "_tip"), P(k + "_tail"), arrowprops=arrow)
ax.text(*P("hw_text"), r"$\Delta\lambda_{1/2}$ = .12$\mu$", ha="left", va="center", fontsize=8)
ax.text(*P("hwr_text"), r"$\Delta\lambda_{1/2}/\lambda_0$ = .11", ha="left", va="center", fontsize=8)
ax.annotate("", P("t005_tip"), P("t005_tail"), arrowprops=arrow)
ax.text(P("t005_tail")[0], P("t005_tail")[1] + 0.035, "T = .005", ha="center", va="bottom", fontsize=8)
finish(fig, HERE, "Fig 20.121: measured spectral transmittance of a narrow band-pass filter with a nearly rectangular pass band",
       ["Measured data (Bausch and Lomb), no formula: traced from docs/scans/ch20.pdf page 90 (400 dpi) with `ch20_nine_layer_bandpass_trace.py`.",
        "L-shaped axis with outside ticks, calibrated directly on 19 ticks (residual 0.011 micron in x and 0.003 in T): the curves are good",
        "to about 0.5 percent of either span (`trace.csv`). Guides for the three-curve pass band and the feet were read off 2-4x zooms.",
        "Three measurements as printed (normal incidence, phi = 30 and 45 degrees), all solid. The scan's 'Normal', 'phi = 30' and",
        "'phi = 45' arrows all end on the leftmost rising edge, so which curve is which is not decidable from the figure; the arrows are",
        "reproduced exactly where printed and the curves are not otherwise labelled. Where the three cross in the pass band they are split",
        "consistently; since all are solid, the split does not change the drawing. Between 8.3 and 9.3 microns the curves lie on the",
        "axis (the printed 'T = .005' pointer marks that level) and are not redrawn there.",
        "(sic, as printed) 'Delta lambda_1/2 = .12 mu': the half-width arrows are 1.12 micron apart at T = .36, and the printed",
        "Delta lambda_1/2 / lambda_0 = .11 also implies about 1.2 micron, so '.12' is probably a misprint for 1.2; kept as printed.",
        "The scan's in-figure heading 'Measured Transmittance of a Nine Layer Band Pass Filter' is dropped (house style: no in-figure",
        "title). Axes as printed: 5.55 to 14.25 microns, T 0 to 1.00.",
        "Spec correction: gap_pages_figure_specs.md gives 550-700 mu; the scan reads 6-14 microns with a pass band near 10.7 microns."])
