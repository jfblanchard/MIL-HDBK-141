from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.100: Fabry-Perot transmission against wave number, t_g = 0.0025 cm: T = Tmax (1-A)^2 / [(1-A)^2 + 4A sin^2(2 pi sigma t_g)]."""
tg, A, Tmax = 0.0025, 0.70, 0.94
fsr = 1 / (2 * tg)
sig = np.linspace(19700, 20500, 6000)
T = Tmax * (1 - A) ** 2 / ((1 - A) ** 2 + 4 * A * np.sin(2 * np.pi * sig * tg) ** 2)
fig, ax = figure(4.6, 2.9)
ax.plot(sig, T, **CURVE)
ax.set_xlim(19700, 20500)
ax.set_ylim(0, 1.2)
axes_setup(ax, r"Wave number, $\sigma$ in cm$^{-1}$", r"$T_f$", (19700, 20500), (0, 1.2), [19800, 20000, 20200, 20400],
           [0.2, 0.4, 0.6, 0.8, 1.0], xfmt=lambda v: f"{v:,.0f}", yfmt=lambda v: f"{v:.1f}".replace("0.", "."), minor=(100, 0.1))
for a, b in zip((19800, 20000, 20200), (20000, 20200, 20400)):
    ax.annotate("", (b, 1.05), (a, 1.05), arrowprops=dict(arrowstyle="<|-|>,head_length=0.3,head_width=0.12", color=INK, lw=0.5, shrinkA=0, shrinkB=0))
    ax.text((a + b) / 2, 1.065, r"$\sigma_f$", ha="center", va="bottom", fontsize=8)
for x in (19800, 20000, 20200, 20400):
    ax.plot([x, x], [Tmax, 1.05], color=INK, lw=0.35)
finish(fig, HERE, "Fig 20.100: transmission of a Fabry-Perot interferometer as a function of wave number, t_g = 0.0025 cm",
       ["Airy transmission T(sigma) = T_max (1-A)^2 / [(1-A)^2 + 4 A sin^2(2 pi sigma t_g)] with t_g = 0.0025 cm (given in the caption), so the free spectral range",
        "sigma_f = 1/(2 t_g) = 200 cm^-1 and the peaks sit at multiples of 200 cm^-1 (19,800 / 20,000 / 20,200 / 20,400), as on the scan.",
        "Parameters NOT printed in the book and read from the scan's peak shape: A = 0.70 (half-width about 23 cm^-1, i.e. 2w about 0.11 of an order) and T_max = 0.94.",
        "They fix the peak sharpness and height only; the order spacing is exact. Axes as printed: sigma 19,700 to 20,500, T_f up to 1.0."])

