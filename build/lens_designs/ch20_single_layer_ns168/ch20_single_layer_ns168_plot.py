from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.20: as Fig 20.19 for glass ns = 1.68."""
n1, ns, lam0 = 1.38, 1.68, 550.0
lam = np.linspace(400, 700, 600)
fig, ax = figure(3.3, 2.7)
for p in (0, 45):
    ax.plot(lam, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, lam, p, "av"), **CURVE)
axes_setup(ax, "Wavelength in millimicrons", "Reflectivity", (400, 700), (0, 0.03), [400, 500, 600, 700],
           np.arange(0, 0.031, 0.01), yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0", minor=(50, 0.005))
note(ax, r"$\phi = 45^\circ$", (440, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, 440, 45, "av")), (500, 0.0255), size=7.5)
note(ax, r"$\phi = 0^\circ$", (620, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, 620, 0, "av")), (640, 0.0042), size=7.5)
layer_inset(ax, (0.02, 1.03, 0.62, 0.42), n1=n1, ns=ns, sub="Glass", lam_note=r"$n_1t_1=\lambda_0/4$" + "\n" + r"$\lambda_0=550$ m$\mu$")
finish(fig, HERE, "Fig 20.20: computed spectral reflectivity of a single layer at phi = 0 and 45 degrees (ns = 1.68)",
       ["Same computation as Fig 20.19 with the higher-index glass the scan prints for this panel: n1 = 1.38, ns = 1.68, lambda0 = 550 mu.",
        "R_av = (Rs + Rp)/2, constant indices, lossless. Normal-incidence minimum 0.0039 at 550 mu (closed form agrees).",
        "Ordinate 0 to 0.03 as printed (the Gemini spec said 0 to 6 percent and a different substrate; the scan was followed)."])

