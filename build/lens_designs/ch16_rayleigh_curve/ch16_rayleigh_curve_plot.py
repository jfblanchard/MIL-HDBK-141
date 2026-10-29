from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from plotkit import *  # noqa: E402,F401,F403

"""Table 16.1: Rayleigh limit. Airy pattern [2 J1(u)/u]^2 with u = 3.8317 r (r in Airy units, first dark ring at r = 1)."""
from scipy.special import j1
u0 = 3.831706
I = lambda r: np.where(np.abs(r) < 1e-9, 1.0, (2 * j1(u0 * np.abs(r) + 1e-12) / (u0 * np.abs(r) + 1e-12)) ** 2)
r = np.linspace(-2.5, 3.5, 3000)
fig, ax = figure(5.2, 3.0)
ax.plot(r, I(r), **DASHED)
ax.plot(r, I(r - 1), **DOTTED)
ax.plot(r, I(r) + I(r - 1), **CURVE)
axes_setup(ax, "$r$, in Airy units", "Energy density", (-2.5, 3.5), (0, 1.2), np.arange(-2, 3.1, 1),
           [0.2, 0.4, 0.6, 0.8, 1.0], yfmt=lambda v: f"{v:.1f}".replace("0.", "."))
ax.set_xticklabels(["$-2$", "$-1$", "0", "1", "2", "3"])
ax.set_xticks([0.5], minor=True)
dip = float(I(0.5) * 2)
note(ax, r"$O'$", (0, 0.4), size=8)
note(ax, r"$P'$", (1, 0.4), size=8)
note(ax, "COMBINED ENERGY DENSITY", (0.22, float(I(0.22) + I(-0.78))), (0.5, 1.12), size=7)
finish(fig, HERE, "Table 16.1: physical situation at the limit of resolution (Rayleigh's criterion)",
       ["Airy intensity I(r) = [2 J1(u)/u]^2, u = 3.8317 r, r in Airy units so the first dark ring is at r = 1 (the Rayleigh separation 0.61 lambda / NA).",
        "Dashed: image O' centred at 0; dotted: P' centred at 1 Airy unit; solid: their sum, I(r) + I(r - 1). Peak of P' falls on the first zero of O'.",
        f"Computed midpoint value at 0.5 Airy unit: {dip:.4f} of the peak of one curve (the classic 0.735 Rayleigh dip, a 26 percent drop), against the spec's 0.735.",
        "The spec text gives the dip as 'approximately 19%' and '81% of peak' in one sentence and 0.735 in another; the Airy formula gives 0.735, so that is what is plotted.",
        "Printed as 'Table 16.1' in the book although it is a graph. Ordinate runs 0 to 1.0, abscissa -2.5 to 3.5 Airy units."])

