from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.18: quarter-wave single layer (n1 = 1.38) on glass ns = 1.68, phi = 0, 45, 65 degrees; Rav versus g = lambda0/lambda."""
n1, ns, g = 1.38, 1.68, np.linspace(0.0005, 2.0, 800)
fig, ax = figure(4.8, 3.5)
lam0 = 1.0
for p in (0, 45, 65):
    ax.plot(g, thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, lam0 / g, p, "av"), **CURVE)
axes_setup(ax, r"$g=\lambda_0/\lambda$", "Reflectivity", (0, 2.0), (0, 0.16), np.arange(0, 2.01, 0.2), np.arange(0, 0.15, 0.02),
           xfmt=lambda v: f"{v:.1f}".replace("0.", ".") if v < 1 else f"{v:.1f}", yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0",
           minor=(0.1, 0.01))
Rg = lambda p, g0: thinfilm.reflectance(1.0, [(n1, lam0 / 4 / n1)], ns, lam0 / g0, p, "av")
note(ax, r"$\phi = 65^\circ$", (0.5, Rg(65, 0.5)), (0.22, 0.095), size=7.5)
note(ax, r"$\phi = 45^\circ$", (0.7, Rg(45, 0.7)), (0.95, 0.088), size=7.5)
note(ax, r"$\phi = 0^\circ$", (0.45, Rg(0, 0.45)), (0.2, 0.012), size=7.5)
layer_inset(ax, (0.46, 0.64, 0.5, 0.34), n1=n1, ns=ns, sub="Glass substrate", lam_note=r"$n_1t_1=\lambda_0/4$")
finish(fig, HERE, "Fig 20.18: computed spectral reflectivity of a single-layer antireflection coating at various angles",
       ["Characteristic-matrix (Abeles) computation for the stack on the scan's inset: quarter-wave layer n1 t1 = lambda0/4, n1 = 1.38, glass ns = 1.68.",
        "Curves are R_av = (Rs + Rp)/2 (unpolarised light) at phi = 0, 45, 65 degrees, plotted against g = lambda0/lambda from 0 to 2.0 as printed.",
        "Dispersion neglected (constant indices), lossless layers. Normal-incidence minimum equals ((n1^2 - ns)/(n1^2 + ns))^2 = 0.0039 at g = 1 (checked).",
        "Differences from the Gemini spec: ns is 1.68 on the scan (spec said 1.52), phi values are 0/45/65 (spec said 0/30/45/60), ordinate runs to 0.14 as 0 to 1 reflectivity, not percent.",
        "Which polarisation the book drew is not printed on this figure; R_av is the book's own convention elsewhere (Figs 20.21, 20.22)."])

