from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.19: MgF2-type layer n1 = 1.38 on glass ns = 1.51, lambda0 = 550 mu, phi = 0 and 45 deg; Rav versus wavelength."""
n1, ns, lam0 = 1.38, 1.51, 550.0
lam = np.linspace(400, 700, 600)
fig, ax = figure(3.3, 2.7)
for p in (0, 45):
    ax.plot(lam, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, lam, p, "av"), **CURVE)
axes_setup(ax, "Wavelength in millimicrons", "Reflectivity", (400, 700), (0, 0.03), [400, 500, 600, 700],
           np.arange(0, 0.031, 0.01), yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0", minor=(50, 0.005))
note(ax, r"$\phi = 45^\circ$", (470, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, 470, 45, "av")), (430, 0.0265), size=7.5)
note(ax, r"$\phi = 0^\circ$", (540, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, 540, 0, "av")), (590, 0.0045), size=7.5)
layer_inset(ax, (0.02, 1.03, 0.62, 0.42), n1=n1, ns=ns, sub="Glass", lam_note=r"$n_1t_1=\lambda_0/4$" + "\n" + r"$\lambda_0=550$ m$\mu$")
finish(fig, HERE, "Fig 20.19: computed spectral reflectivity of a single layer at phi = 0 and 45 degrees (ns = 1.51)",
       ["Characteristic-matrix computation for the scan's stack: quarter-wave layer at lambda0 = 550 millimicrons, n1 = 1.38, glass ns = 1.51.",
        "Curves are R_av = (Rs + Rp)/2 at phi = 0 and 45 degrees; constant indices, lossless. Normal-incidence minimum 0.0133 at 550 mu (closed form agrees).",
        "Ordinate 0 to 0.03 and abscissa 400 to 700 mu as printed (reflectivity as a fraction, not percent as the Gemini spec said).",
        "The inset (ray, layer, substrate) is redrawn schematically; the polarisation plotted is not named on the scan, R_av assumed."])

