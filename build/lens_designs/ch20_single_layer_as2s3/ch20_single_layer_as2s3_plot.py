from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.23: n1 = 1.55 on As2S3 glass ns = 2.40, lambda0 = 3.00 mu, phi = 0 and 45 deg; Rav versus wavelength 1.5 to 5.0 mu."""
n1, ns, lam0 = 1.55, 2.40, 3.00
lam = np.linspace(1.5, 5.0, 700)
R = lambda p, l: thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, l, p, "av")
fig, ax = figure(3.4, 2.5)
for p in (0, 45):
    ax.plot(lam, R(p, lam), **CURVE)
axes_setup(ax, "Wavelength in microns", "Reflectivity", (1.5, 5.0), (0, 0.20), [1.5, 2.0, 3.0, 4.0, 5.0],
           np.arange(0, 0.21, 0.05), xfmt=lambda v: f"{v:.1f}", yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0",
           minor=(0.5, 0.01))
note(ax, r"$\phi = 0^\circ$", (2.1, R(0, 2.1)), (2.55, 0.145), size=7.5)
note(ax, r"$\phi = 45^\circ$", (3.6, R(45, 3.6)), (3.9, 0.02), size=7.5)
layer_inset(ax, (0.0, 1.04, 0.7, 0.5), n1=n1, ns=ns, sub=r"As$_2$S$_3$ glass substrate", lam_note=r"$n_1t_1=\lambda_0/4$" + "\n" + r"$\lambda_0=3.00\,\mu$")
finish(fig, HERE, "Fig 20.23: computed spectral reflectivity of a single layer on As2S3 glass at phi = 0 and 45 degrees",
       ["Characteristic-matrix computation for the scan's stack: quarter-wave layer at lambda0 = 3.00 microns, n1 = 1.55, As2S3 glass ns = 2.40.",
        "R_av = (Rs + Rp)/2 at phi = 0 and 45 degrees, constant indices, lossless. Normal-incidence minimum is essentially zero near 3 microns because n1^2 = 2.40 = ns.",
        "Axes as printed: 1.5 to 5.0 microns, 0 to 0.20. The Gemini spec for 20.23 was only the table caption and generic; stack data are from the scan's inset.",
        "Polarisation drawn is not named on the figure; R_av assumed (the book's convention in the same series)."])

