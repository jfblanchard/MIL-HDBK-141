"""Fig 21.5: flow conditions at the (nu-1)th and nu-th layers of a stratified medium. Forward flow tau
(rightward, along the direction of incidence), backward flow r, and the boundary ratio rho = r / tau."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

xs = [0.0, 20.0, 44.0]
fig, ax = canvas(TEXT_WIDTH * 0.8, (-14, 62), (-22, 20))
for x in xs:
    line(ax, P(x, -14), P(x, 14), color=INK, linewidth=1.0)
for i, (x0, x1, nm) in enumerate(((xs[0], xs[1], r"\nu-1"), (xs[1], xs[2], r"\nu"))):
    xm = (x0 + x1) / 2
    ray(ax, [P(x0 + 3, 6), P(x1 - 3, 6)], AXIAL, arrows=(0.5,))
    ray(ax, [P(x1 - 3, -6), P(x0 + 3, -6)], AXIAL, arrows=(0.5,))
    text(ax, "$\\tau_{%s}$" % nm, P(xm, 9.0))
    text(ax, "$r_{%s}$" % nm, P(xm, -9.0))
    text(ax, "layer $%s$" % nm, P(xm, 17), size=7)
    dim(ax, P(x0, -17), P(x1, -17), "$d_{%s}$" % nm, size=7)
    line(ax, P(x0, -14.5), P(x0, -18), **THIN)
    line(ax, P(x1, -14.5), P(x1, -18), **THIN)
ray(ax, [P(-13, 0), P(-2, 0)], AXIAL, arrows=(0.6,))
text(ax, "direction of\nincidence", P(-13, 3.2), ha="left", size=7)
text(ax, "layer $\\nu+1$", P(54, 17), size=7)
ray(ax, [P(xs[2] + 3, 6), P(xs[2] + 11, 6)], AXIAL, arrows=(0.5,))
text(ax, "$\\tau_{\\nu+1}$", P(xs[2] + 7, 9.0))
done(fig, HERE)
readme(HERE, "Fig 21.5: flow conditions at the (nu-1)th and nu-th layers", lines=["Notation diagram: parallel boundary planes, forward and backward flow arrows.",
       "Labels from the spec: direction of incidence, layers nu-1, nu, nu+1, thicknesses d_{nu-1}, d_nu, tau and r in each layer.",
       "FLAG-PARTIAL: the spec also lists the boundary ratios rho = r/tau drawn with angled ray vectors; those angled vectors are not reproduced, only the flow arrows and layer geometry."])
