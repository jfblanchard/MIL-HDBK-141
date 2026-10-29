from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403
from matplotlib.patches import Arc, Circle  # noqa: E402

"""Fig 20.101: measured spectral transmittance of a Fabry-Perot type multilayer filter (Dr. C. Alley), traced; with the
parallel resonant circuit drawn below it as on the scan."""
c = load_trace(HERE / "trace.csv")
x, y = c["transmittance"]
l0, hy = c["lambda0"][0][0], c["halfwidth_level"][1][0]
fig = plt.figure(figsize=(3.4, 4.9))
ax = fig.add_axes([0.2, 0.38, 0.72, 0.58])
ax.plot(x, y, **CURVE)
axes_setup(ax, "Wavelength in millimicrons", "Measured Transmittance", (780, 820), (0, 1.0), [780, 790, 800, 810, 820],
           np.arange(0, 1.01, 0.1), yfmt=lambda v: "" if v < 0.05 else "1.0" if v > 0.95 else f"{v:.1f}".lstrip("0"))
i = np.argmax(y)
ax.plot([x[i] + 0.6, x[i] + 6.5], [y[i], y[i]], color=INK, lw=0.5)
ax.text(x[i] + 7, y[i], r"T$_{\rm max}$", ha="left", va="center", fontsize=8)
xl, xr = np.interp(hy, y[:i], x[:i]), np.interp(hy, y[i:][::-1], x[i:][::-1])
arrow = dict(arrowstyle="-|>,head_length=0.4,head_width=0.15", color=INK, lw=0.5, shrinkA=0, shrinkB=0)
ax.annotate("", (xl, hy), (xl - 5.5, hy), arrowprops=arrow)
ax.annotate("", (xr, hy), (xr + 5.5, hy), arrowprops=arrow)
ax.text(xr + 6, hy, r"$\Delta\lambda_{1/2}$", ha="left", va="center", fontsize=8)
ax.plot([l0, l0], [0, 0.045], color=INK, lw=0.6)
ax.text(l0 + 0.4, 0.075, r"$\lambda_0$", ha="center", va="bottom", fontsize=8)

# parallel resonant circuit (scan: terminals top and bottom left, capacitor and inductor in parallel)
ca = fig.add_axes([0.2, 0.02, 0.72, 0.22])
ca.set_xlim(0, 10)
ca.set_ylim(0, 4)
ca.set_aspect("equal")
ca.axis("off")
w = dict(color=INK, lw=0.7, solid_capstyle="butt")
for yy in (3.6, 0.4):
    ca.add_patch(Circle((3.0, yy), 0.13, fill=False, ec=INK, lw=0.6))
ca.plot([3.13, 4.7, 4.7], [3.6, 3.6, 3.0], **w)
ca.plot([3.13, 4.7, 4.7], [0.4, 0.4, 1.0], **w)
ca.plot([3.6, 5.8], [3.0, 3.0], **w)
ca.plot([3.6, 5.8], [1.0, 1.0], **w)
ca.plot([3.6, 3.6, None, 3.6, 3.6], [3.0, 2.08, None, 1.92, 1.0], **w)
ca.plot([3.25, 3.95], [2.08, 2.08], **w)
ca.plot([3.25, 3.95], [1.92, 1.92], **w)
ca.plot([5.8, 5.8], [3.0, 2.75], **w)
ca.plot([5.8, 5.8], [1.0, 1.25], **w)
for k in range(3):
    ca.add_patch(Arc((5.8, 2.58 - 0.5 * k), 0.75, 0.5, theta1=-90, theta2=90, color=INK, lw=0.7))
ca.text(3.0, 2.0, "Capacitor", ha="right", va="center", fontsize=8)
ca.text(6.45, 2.0, "Inductor", ha="left", va="center", fontsize=8)
finish(fig, HERE, "Fig 20.101: measured spectral transmittance of a Fabry-Perot type multilayer filter, and a parallel resonant circuit",
       ["Measured data (Dr. C. Alley), no formula: traced from docs/scans/ch20.pdf page 75 (400 dpi) with `ch20_fp_multilayer_trace.py`.",
        "Ticks but no grid: affine fit to 14 ticks (digitize.tick_axes), residual 0.14 mu in x and 0.0015 in T, so the curve is good to",
        "about 0.5 percent of either span (`trace.csv`). From the trace: T_max = .845 at 796.9 mu, half width about 5.7 mu (794.0-799.8).",
        "The printed lambda_0 tick (796.5 mu, inside the bottom edge), the T_max leader and the Delta lambda_1/2 arrows (at T = .42) are",
        "placed where the scan has them. Outside 788-809 mu the curve lies on the frame's zero line and is not redrawn.",
        "The circuit is the scan's own schematic (the caption's 'A parallel resonant circuit'): two terminals feeding a capacitor and",
        "an inductor in parallel, labelled as printed; it is a symbol drawing, not to scale. Axes as printed: 780-820 mu, T 0 to 1.0."])
