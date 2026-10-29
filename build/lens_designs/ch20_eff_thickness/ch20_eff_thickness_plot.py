from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Fig 20.8: cos(theta) = [1 - (n0/n)^2 sin^2 phi]^(1/2), n0 = 1.00, for the nine... seven indices printed on the scan."""
ns_ = [4.045, 3.48, 2.30, 2.10, 1.68, 1.50, 1.38]
phi = np.linspace(0, 90, 361)
fig, ax = figure(4.8, 3.6)
lab = {4.045: "4.045", 3.48: "3.48", 2.30: "2.30", 2.10: "2.10", 1.68: "1.68", 1.50: "1.50", 1.38: "1.38"}
ends = []
for n in ns_:
    c = np.sqrt(1 - np.sin(np.radians(phi)) ** 2 / n ** 2)
    ax.plot(phi, c, **CURVE)
    ends.append(c[-1])
axes_setup(ax, r"$\phi$, angle of incidence in air (degrees)", r"$\cos\,\theta$", (0, 90), (0.68, 1.0),
           np.arange(0, 91, 10), [0.7, 0.8, 0.9, 1.0], yfmt=lambda v: f"{v:.1f}".lstrip("0") if v < 1 else "1.0",
           minor=(5, 0.02))
ax.set_xticklabels([f"{v}$^\\circ$" if v else "0" for v in range(0, 91, 10)])
for n, y in zip(ns_, spread(ends, 0.016)):
    ax.text(91.2, y, f"$n = {lab[n]}$", fontsize=7, va="center", ha="left", clip_on=False)
ax.text(8, 0.775, r"$\cos\,\theta=\left[1-\left(\frac{n_0}{n}\right)^{2}\sin^{2}\phi\right]^{1/2}$" + "\n" + r"for $n_0 = 1.00$",
        fontsize=7.5, ha="left", va="center", bbox=dict(fc="white", ec=INK, lw=0.5, pad=3))
finish(fig, HERE, "Fig 20.8: effective thickness versus angle of incidence in air",
       ["Plot of the formula printed on the figure, cos(theta) = [1 - (n0/n)^2 sin^2(phi)]^(1/2) with n0 = 1.00, for the seven film indices",
        "the scan labels: n = 1.38, 1.50, 1.68, 2.10, 2.30, 3.48, 4.045. Exact, no fitting; y-axis 0.7 to 1.0 as printed.",
        "Note: the Gemini spec listed a different index set (1.46, 2.00, 4.00) and a 0 to 1 axis; both were wrong against the scan, which is followed here.",
        "Axis is cos(theta) normalised to 1 at normal incidence, which is the same quantity as n d cos(theta) / (n d)_0."])

