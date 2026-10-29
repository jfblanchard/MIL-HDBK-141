from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.24: n1 = 1.90 on germanium ns = 4.05, lambda0 = 3.00 mu, phi = 0 and 45 deg."""
n1, ns, lam0 = 1.90, 4.05, 3.00
lam = np.linspace(1.5, 5.0, 700)
R = lambda p, l: thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, l, p, "av")
fig, ax = figure(3.4, 3.6)
for p in (0, 45):
    ax.plot(lam, R(p, lam), **CURVE)
axes_setup(ax, "Wavelength in microns", "Reflectivity", (1.5, 5.0), (0, 0.40), [1.5, 2.0, 3.0, 4.0, 5.0],
           np.arange(0, 0.41, 0.05), xfmt=lambda v: f"{v:.1f}", yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0",
           minor=(0.5, 0.025))
note(ax, r"$\phi = 45^\circ$", (3.75, R(45, 3.75)), (3.0, 0.17), size=7.5)
note(ax, r"$\phi = 0^\circ$", (4.2, R(0, 4.2)), (4.35, 0.055), size=7.5)
layer_inset(ax, (0.0, 1.03, 0.72, 0.4), n1=n1, ns=ns, sub="Germanium", lam_note=r"$n_1t_1=\lambda_0/4$" + "\n" + r"$\lambda_0=3.00\,\mu$")
finish(fig, HERE, "Fig 20.24: computed spectral reflectivity of a single layer on germanium at phi = 0 and 45 degrees",
       ["Characteristic-matrix computation for the scan's stack: quarter-wave layer at lambda0 = 3.00 microns, n1 = 1.90, germanium ns = 4.05.",
        "R_av = (Rs + Rp)/2 at phi = 0 and 45 degrees, constant indices (germanium dispersion and absorption neglected), lossless.",
        "Axes as printed: 1.5 to 5.0 microns, 0 to 0.40. The scan's graph-paper grid is not reproduced (house style: no grid).",
        "The small layer sketch above the plot is the scan's inset, redrawn. Polarisation drawn is not named on the figure; R_av assumed."])

