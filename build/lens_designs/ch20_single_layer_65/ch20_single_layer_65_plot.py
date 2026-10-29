from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.21: Rs, Rp, Rav at phi = 65 degrees, n1 = 1.38 on glass ns = 1.51; ordinate scale doubles below 0.02."""
n1, ns, lam0 = 1.38, 1.51, 550.0
lam = np.linspace(400, 700, 600)
fig, ax = figure(3.4, 3.7)
R = {k: thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, lam, 65, k) for k in ("s", "av", "p")}
for k in R:
    ax.plot(lam, R[k], **CURVE)
fwd = lambda r: np.where(r <= 0.02, r / 0.01, 2 + (r - 0.02) / 0.02)
inv = lambda s: np.where(s <= 2, s * 0.01, 0.02 + (s - 2) * 0.02)
ax.set_yscale("function", functions=(fwd, inv))
ticks = [0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22, 0.24]
axes_setup(ax, "Wavelength in millimicrons", "Reflectivity", (400, 700), (0, 0.25), [400, 500, 600, 700], ticks,
           yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0")
ax.set_yticklabels([f"{v:.2f}".lstrip("0") if v else "0" for v in ticks])
ax.plot([400, 408], [0.02, 0.02], color=INK, lw=0.5)
ax.annotate("scale changes\nat 0.02", (700, 0.02), (660, 0.036), fontsize=6.5, ha="center", va="center", arrowprops=LEAD)
i_s, i_a, i_p = np.argmin(R["s"]), np.argmin(R["av"]), np.argmax(R["p"])
note(ax, r"$R_s$", (lam[100], R["s"][100]), (430, 0.15), size=8)
note(ax, r"$R_{av}$", (lam[100], R["av"][100]), (430, 0.095), size=8)
note(ax, r"$R_p$", (lam[100], R["p"][100]), (440, 0.011), size=8)
note(ax, "minimum", (lam[i_s], R["s"][i_s]), (500, 0.113), size=7)
note(ax, "minimum", (lam[i_a], R["av"][i_a]), (500, 0.063), size=7)
note(ax, "maximum", (lam[i_p], R["p"][i_p]), (560, 0.0125), size=7)
layer_inset(ax, (0.0, 0.73, 0.62, 0.26), n1=n1, ns=ns, sub="Glass", ray_label=r"$65^\circ$")
finish(fig, HERE, "Fig 20.21: computed Rs, Rp and Rav at phi = 65 degrees",
       ["Characteristic-matrix computation: quarter-wave layer at 550 mu, n1 = 1.38, glass ns = 1.51, phi = 65 degrees, constant indices.",
        "Rs, Rp and R_av = (Rp + Rs)/2 as the caption defines them. The ordinate is piecewise linear: twice as expanded below 0.02 as above it",
        "(0.01 and 0.02 are as far apart as 0.02 and 0.04 on the scan), reproduced with a function scale; a short tick bar marks the change at 0.02.",
        "'minimum'/'maximum' tags are the scan's own words for where each curve turns (Rs and Rav have minima, Rp a maximum)."])

