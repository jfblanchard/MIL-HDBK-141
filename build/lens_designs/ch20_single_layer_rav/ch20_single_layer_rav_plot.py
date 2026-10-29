from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.22: Rav versus angle for uncoated glass (ns = 1.52) and the minimum Rav of the same glass coated with n = 1.35."""
n1, ns = 1.35, 1.52
phi = np.linspace(0, 90, 361)
g = np.linspace(0.4, 2.5, 1050)
unc = np.array([thinfilm.reflectance(1.0, [], ns, 1.0, p, "av") for p in phi])
low = []
for p in phi:
    low.append(thinfilm.reflectance(1.0, [(n1, 1 / 4 / n1)], ns, 1 / g, p, "av").min())
fig, ax = figure(3.4, 3.6)
ax.plot(phi, unc, **CURVE)
ax.plot(phi, low, **CURVE)
axes_setup(ax, r"$\phi$, angle of incidence in air", "Average Reflectivity", (0, 90), (0, 0.30), [0, 20, 40, 60, 80],
           np.arange(0, 0.31, 0.05), yfmt=lambda v: f"{v:.2f}".lstrip("0") if v else "0", minor=(10, 0.025))
ax.set_xticklabels(["0", "20$^\\circ$", "40$^\\circ$", "60$^\\circ$", "80$^\\circ$"])
note(ax, "Uncoated Glass", (55, unc[220]), (30, 0.075), size=7.5)
note(ax, "Single Layer", (phi[280], low[280]), (88, 0.06), ha="right", size=7.5)
layer_inset(ax, (0.08, 0.6, 0.5, 0.2), coated=False, ns=ns, sub="Uncoated Glass", ray_label=r"$\phi$")
layer_inset(ax, (0.08, 0.34, 0.5, 0.24), n1=n1, ns=ns, sub="Glass Substrate", ray_label=r"$\phi$")
finish(fig, HERE, "Fig 20.22: R_av versus angle of incidence for uncoated and single-layer-coated glass",
       ["Uncoated curve: Fresnel R_av = (Rs + Rp)/2 of glass ns = 1.52 (0.0426 at normal incidence). Coated curve: the minimum over wavelength",
        "(g = lambda0/lambda from 0.4 to 2.5, quarter-wave layer n1 = 1.35 at lambda0) of the characteristic-matrix R_av at each angle, as the caption defines it.",
        "Both reach 1 at 90 degrees; the plot is clipped at 0.30 as printed. Indices n = 1.35, ns = 1.52 are those on the scan's two insets.",
        "Judgement call: the book does not say over which wavelength range the minimum was taken; the minimum sits near g = 1 at small angles and moves to larger g with angle."])

