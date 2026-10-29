from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.120: measured spectral transmittance of a narrow band-pass filter with a nearly rectangular pass band (Eastman Kodak)."""
c = load_trace(HERE / "trace.csv")
x, y = c["transmittance"]
(x43, x47), top = c["reject"][0], c["reject"][1][0]
a08, a15, xr = c["arrow08"][1][0], c["arrow15"][1][0], c["edge"][0][0]
i = np.argmax(y)
side = lambda t: (np.interp(t, y[:i], x[:i]), np.interp(t, y[i:][::-1], x[i:][::-1]))
fig, ax = figure(3.9, 3.9)
ax.plot(x, y, **CURVE)
axes_setup(ax, "Wavelength in microns", "Transmittance", (4.2, xr), (0, 0.6), np.arange(4.2, 4.71, 0.1),
           np.arange(0, 0.61, 0.1), xfmt=lambda v: f"{v:.2f}", yfmt=lambda v: "0" if v < 0.05 else f"{v:.1f}".lstrip("0"))
arrow = dict(arrowstyle="-|>,head_length=0.4,head_width=0.15", color=INK, lw=0.5, shrinkA=0, shrinkB=0)
both = dict(arrowstyle="<|-|>,head_length=0.4,head_width=0.15", color=INK, lw=0.5, shrinkA=0, shrinkB=0)
ax.annotate("", (x[i], y[i]), (x[i], 0.65), arrowprops=arrow, annotation_clip=False)
ax.text(x[i], 0.655, r"$\lambda_0 = 4.5\mu \pm .05\mu$", ha="center", va="bottom", fontsize=8)
ax.annotate("", (x[i] - 0.005, y[i]), (4.39, y[i]), arrowprops=arrow)
ax.text(4.385, y[i], r"T$_{\rm max}$ = .51", ha="right", va="center", fontsize=8)
l, r = side(a08)
ax.annotate("", (r, a08), (l, a08), arrowprops=both)
ax.text((l + r) / 2, a08 + 0.012, r".08$\mu$", ha="center", va="bottom", fontsize=7.5)
note(ax, r"$\Delta\lambda_{1/2}$", (l, a08), (4.33, 0.33), ha="center", size=8)
l, r = side(a15)
ax.annotate("", (r, a15), (l, a15), arrowprops=both)
ax.text((l + r) / 2, a15 + 0.012, r".15$\mu$", ha="center", va="bottom", fontsize=7.5)
note(ax, "Base Band\nWidth\nT = .05", (r, a15), (4.665, 0.37), ha="center", size=7.5, linespacing=1.1)
for xx, sgn, ha in ((x43, -1, "right"), (x47, 1, "left")):
    ax.plot([xx, xx], [0, top], color=INK, lw=0.6, dashes=(3, 1.5))
    ax.annotate("", (xx + sgn * 0.065, 0.025), (xx, 0.025), arrowprops=arrow)
    ax.text(xx + sgn * 0.03, 0.105, "Rejection\nRegion", rotation=90, ha="center", va="center", fontsize=7, linespacing=1.0)
ax.text(4.30, 0.235, r"$\lambda < 4.3\,\mu$" + "\n" + r"T $<$ .001", ha="center", va="center", fontsize=7.5)
ax.text(4.70, 0.235, r"$\lambda > 4.7\,\mu$" + "\n" + r"T $<$ .01", ha="center", va="center", fontsize=7.5)
finish(fig, HERE, "Fig 20.120: measured spectral transmittance of a narrow band-pass filter with a nearly rectangular pass band",
       ["Measured data (Eastman Kodak), no formula: traced from docs/scans/ch20.pdf page 90 (400 dpi) with `ch20_narrow_bandpass_kodak_trace.py`.",
        "Ticks but no grid: affine fit to 9 ticks (digitize.tick_axes), residual 0.0003 micron in x and 0.0007 in T: the curve is good to",
        "about 0.5 percent of either span (`trace.csv`). Peak T = .51 at 4.50 micron, as printed. The widths do NOT match their labels:",
        f"traced {side(a08)[1] - side(a08)[0]:.3f} micron at T = {a08:.2f} (printed .08) and {side(a15)[1] - side(a15)[0]:.3f} micron at T = .05 (printed .15).",
        "The scan's own arrows measure 0.086 and 0.164 micron on its own axis, so the 1962 drawing is about 10 percent wider than its",
        "labels (sic, as printed); the curve is kept as drawn and the labels as printed.",
        "Every annotation is the scan's own: lambda_0 arrow, T_max, Delta lambda_1/2 and base band width arrows at their traced levels,",
        "the dashed rejection limits at 4.30 and 4.70 micron with their arrows and 'Rejection Region' labels, and the rejection specs.",
        "Axes as printed: 4.20 micron to the frame edge at 4.765, T 0 to .6.",
        "Spec correction: gap_pages_figure_specs.md gives 500-700 mu, T to 100 percent and a flat top near 80 percent; the scan is",
        "an infrared filter on 4.20-4.76 micron with a .51 peak and a sloping top."])
