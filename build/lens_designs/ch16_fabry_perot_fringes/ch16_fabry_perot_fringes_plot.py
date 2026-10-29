from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 16.19: W(alpha) = B^2 / [(1-A)^2 + 4A sin^2(alpha/2)], A = 0.9; two adjacent orders, half-width geometry."""
A = 0.9
alpha = np.linspace(-0.45, 1.5, 4000) * 2 * np.pi
W = lambda a: 1 / ((1 - A) ** 2 + 4 * A * np.sin(a / 2) ** 2) * (1 - A) ** 2
x = alpha / (2 * np.pi)
dal = 2 * np.arcsin((1 - A) / (2 * np.sqrt(A)))
fig, ax = figure(5.4, 2.9)
ax.plot(x, W(alpha), **CURVE)
xl = (-0.45, 1.5)
ax.set_xlim(*xl)
ax.set_ylim(-0.24, 1.28)
ax.axis("off")
ax.annotate("", (xl[1] + 0.02, 0), (xl[0], 0), arrowprops=dict(arrowstyle="-|>,head_length=0.5,head_width=0.2", color=INK, lw=0.6))
ax.annotate("", (xl[0], 1.25), (xl[0], 0), arrowprops=dict(arrowstyle="-|>,head_length=0.5,head_width=0.2", color=INK, lw=0.6))
ax.plot(xl, [1, 1], color=INK, lw=0.45)
ax.plot(xl, [0.5, 0.5], color=INK, lw=0.45)
ax.text(xl[0] - 0.02, 1.0, r"$W_{max}$", ha="right", va="center", fontsize=8)
ax.text(xl[0] - 0.02, 0.5, r"$\frac{W_{max}}{2}$", ha="right", va="center", fontsize=8)
ax.text(xl[0] - 0.02, 1.25, r"$W$", ha="right", va="center", fontsize=8)
ax.text(xl[1] + 0.03, 0, r"$\alpha$", ha="left", va="center", fontsize=8)
hw = dal / (2 * np.pi) / 2
arr = lambda **k: dict(arrowstyle=k.get("st", "<|-|>,head_length=0.3,head_width=0.12"), color=INK, lw=0.5, shrinkA=0, shrinkB=0)
ax.plot([1, 1], [0, 0.03], color=INK, lw=0.5)
ax.text(1, -0.08, r"$(\nu+1)\,2\pi$", ha="center", va="center", fontsize=8)
for xc in (0, 1):
    for sgn in (-1, 1):
        ax.plot([xc + sgn * hw], [0.5], "o", color=INK, ms=3)
for sgn in (-1, 1):
    ax.plot([sgn * hw] * 2, [-0.215, 0.5], color=INK, lw=0.5, dashes=(3, 2))
ax.plot([0], [0], "o", color=INK, ms=3)
ax.text(-0.03, -0.075, r"$\nu\,2\pi$", ha="right", va="center", fontsize=8)
ax.annotate("", (0, 1.13), (1, 1.13), arrowprops=arr())
ax.text(0.5, 1.18, r"$2\pi$", ha="center", va="bottom", fontsize=8)
for xc in (0, 1):
    ax.plot([xc, xc], [1.0, 1.15], color=INK, lw=0.35)
ax.annotate("", (hw, -0.075), (0, -0.075), arrowprops=arr())
ax.text(hw + 0.03, -0.075, r"$\Delta\alpha$", ha="left", va="center", fontsize=7.5)
ax.annotate("", (-hw, -0.17), (-hw - 0.05, -0.17), arrowprops=arr(st="-|>,head_length=0.3,head_width=0.12"))
ax.annotate("", (hw, -0.17), (hw + 0.05, -0.17), arrowprops=arr(st="-|>,head_length=0.3,head_width=0.12"))
ax.text(hw + 0.08, -0.17, r"$2w=\Delta\alpha/\pi$", ha="left", va="center", fontsize=7.5)
ax.text(0.04, 1.07, r"$\nu^{th}$ SPECTRAL ORDER", fontsize=7.5, ha="left", va="center")
finish(fig, HERE, "Fig 16.19: the sharpness quality of multiple-beam interference fringes",
       ["Airy distribution W(alpha) = B^2 / [(1 - A)^2 + 4 A sin^2(alpha/2)] (the spec's Fabry-Perot formula), plotted as W / W_max for two adjacent orders",
        "nu and nu+1 with A = 0.9, the value the chapter text uses for a sharp fringe. Half-power points at W_max/2 mark delta-alpha, the half-width in phase angle:",
        "2 arcsin[(1 - A)/(2 sqrt A)] = 0.105 rad for A = 0.9, so the full width 2w = delta-alpha/pi is about 0.033 of the 2 pi order spacing, as the spec notes.",
        "The curve minimum is W_max (1-A)^2/(1+A)^2 = 0.003 W_max, drawn on the axis as the figure does. The figure carries no numeric ticks, only the symbols above.",
        "Spec text said delta-alpha spans 'peak centre to the right half-power point'; the scan puts the dimension on one half-width, drawn that way here."])

