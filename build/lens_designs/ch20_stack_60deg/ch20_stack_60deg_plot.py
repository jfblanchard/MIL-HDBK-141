from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.60: Glass (LH)^4 Air at phi = 60 degrees, layers matched n t cos(theta) = lambda0/4 at 60 degrees."""
nL, nH, ns = 1.38, 2.30, 1.51
s60 = np.sin(np.radians(60))
d = lambda n: 0.25 / (n * np.sqrt(1 - (s60 / n) ** 2))
air_to_glass = [(nH, d(nH)), (nL, d(nL))] * 4
g = np.linspace(0.0005, 2.0, 4000)
R = {k: thinfilm.reflectance(1.0, air_to_glass, ns, 1 / g, 60, k) for k in ("s", "av", "p")}
fig, ax = figure(5.2, 3.6)
ax.fill_between(g, 0, R["s"], where=(g >= 0.78) & (g <= 1.22), facecolor="none", edgecolor=INK, hatch="//////", linewidth=0)
ax.fill_between(g, 0, R["s"], where=(g >= 0.89) & (g <= 1.11), facecolor="white", edgecolor=INK, hatch="xxxxxx", linewidth=0)
for k in R:
    ax.plot(g, R[k], **CURVE)
axes_setup(ax, r"$g=\lambda_c/\lambda$", "Reflectivity", (0, 2.0), (0, 1.0), np.arange(0.2, 2.01, 0.2),
           np.arange(0, 1.01, 0.1), xfmt=lambda v: f"{v:.1f}".replace("0.", ".") if v < 1 else f"{v:.1f}",
           yfmt=lambda v: (f"{v:.1f}".replace("0.", ".") if v < 1 else f"{v:.1f}") if v else "0")
ax.set_xticklabels([f"{v:.1f}".replace("0.", ".") if v < 1 else f"{v:.1f}" for v in np.arange(0.2, 2.01, 0.2)])
sec = ax.secondary_yaxis("right", functions=(lambda r: 1 - r, lambda t: 1 - t))
sec.set_ylabel("Transmission")
sec.set_yticks(np.arange(0, 1.01, 0.1))
sec.set_yticklabels(["0"] + [f"{v:.1f}".replace("0.", ".") if v < 1 else "1.0" for v in np.arange(0.1, 1.01, 0.1)])
sec.tick_params(direction="in")
at = lambda k, x: (x, R[k][np.argmin(abs(g - x))])
note(ax, r"$R_s$", at("s", 1.2), (1.38, 0.93), size=8)
note(ax, r"$R_{average}$", at("av", 1.16), (1.45, 0.78), size=8)
note(ax, r"$R_p$", at("p", 1.1), (1.5, 0.64), size=8)
ax.text(1.97, 0.985, "Angle of Incidence\n" + r"$\phi$ is $60^\circ$", fontsize=7.5, ha="right", va="top")
ax.text(0.04, 0.9, "Glass $(LH)^4$ Air\n$n_s=1.51$\n\nindex of L is 1.38\nindex of H is 2.30\n\nThe H and L layers\nare \"matched\" at $\\phi=60^\\circ$\n"
        r"$n_Lt_L=n_Ht_H=$" + "\n" + r"   $\lambda_0/4$ at $\phi=60^\circ$", fontsize=7, ha="left", va="top", linespacing=1.4)
finish(fig, HERE, "Fig 20.60: computed Rp, Rs and Rav of an eight-layer quarter-wave stack at phi = 60 degrees",
       ["Characteristic-matrix computation: Glass (LH)^4 Air, ns = 1.51, nL = 1.38, nH = 2.30, phi = 60 degrees in air. Thicknesses are chosen so",
        "n t cos(theta) = lambda0/4 for both materials at phi = 60 degrees ('matched'), so each layer is a quarter-wave at g = 1 for both polarisations.",
        "g = lambda_c/lambda from 0 to 2.0. R_av = (Rs + Rp)/2. Centre values 0.99 / 0.87 / 0.75 for Rs / Rav / Rp agree with the scan (about 1.0 / 0.88 / 0.76).",
        "The hatched bands are drawn between the g values read off the scan (0.78 to 1.22 and 0.89 to 1.11); what the book defines them to mark is not stated.",
        "Right ordinate is Transmission = 1 - R, as the scan prints it (increasing downward)."])

