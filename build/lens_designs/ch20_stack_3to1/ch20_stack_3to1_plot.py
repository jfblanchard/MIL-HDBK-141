from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.59: Glass (LLLH)^4 Air: four H quarter-waves alternating with four L layers three quarter-waves thick (8 layers)."""
nL, nH, ns, lam0 = 1.38, 2.30, 1.51, 1.0
q = lam0 / 4
air_to_glass = [(nH, q / nH), (nL, 3 * q / nL)] * 4
lam = np.linspace(0.4, 4.0, 4000)
T = 1 - thinfilm.reflectance(1.0, air_to_glass, ns, lam, 0, "s")
fig, ax = figure(5.2, 2.9)
ax.plot(lam, T, **CURVE)
axes_setup(ax, "Wavelength in microns", "Transmission", (0.4, 4.0), (0, 1.1), np.arange(0.4, 4.01, 0.4),
           [0.2, 0.4, 0.6, 0.8, 1.0], xfmt=lambda v: f"{v:.1f}".replace("0.", ".") if v < 1 else f"{v:.1f}",
           yfmt=lambda v: f"{v:.1f}".replace("0.", ".") if v < 1 else f"{v:.1f}", minor=(0.2, 0.1))
for tag, x, tx, ty in (("(1)", 2.0, 2.18, 0.075), ("(2)", 1.0, 1.28, 0.025), ("(3)", 0.667, 0.56, 0.11), ("(5)", 0.4, 0.5, 0.42)):
    y = T[np.argmin(abs(lam - x))] if tag != "(5)" else 0.5
    note(ax, tag, (x, y), (tx, ty), size=7.5)
ax.text(2.95, 0.66, "Glass $(LLLH)^4$ Air\n$n_s=1.51$\nIndex of H is 2.30\nIndex of L is 1.38\n"
        r"$n_Lt_L=n_Ht_H=\lambda_0/4$" + "\n" + r"$\lambda_0=1.0\,\mu$", fontsize=7, ha="left", va="center", linespacing=1.5)
finish(fig, HERE, "Fig 20.59: computed spectral transmission of an eight-layer 3:1 stack",
       ["Characteristic-matrix computation at normal incidence, T = 1 - R (lossless). Stack as printed on the scan, Glass (LLLH)^4 Air, read from the glass:",
        "each L is three adjacent quarter-waves (3 lambda0/4 of optical thickness), each H one quarter-wave, repeated four times = eight physical layers.",
        "ns = 1.51, nH = 2.30, nL = 1.38, lambda0 = 1.0 micron; 0.4 to 4.0 microns as printed. Dispersion neglected.",
        "Stop bands fall where the 1.0-lambda0 period is a half-wave multiple: lambda = 2.0 (1), 1.0 (2), 0.667 (3) and 0.4 (5); the fourth order (0.5) is",
        "suppressed by the 3:1 thickness ratio, which is why the scan labels (1), (2), (3), (5) and no (4). Computed T at those bands: 0.14, 0.04, 0.14, matching the scan's depths.",
        "The tag (5) points at the narrow band at the left edge, where the band is under-resolved at the scan's own scale."])

