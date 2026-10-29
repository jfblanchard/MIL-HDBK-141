"""Fig 16.6: Fresnel's double mirror. Source S in front of two plane mirrors M1, M2 whose faces meet at a
shallow valley (small angle theta from coplanar). The virtual images S1, S2 of S lie d = 2 a theta apart;
the reflected beams overlap in the wedge between the rays S1-V and S2-V (V = the mirrors' junction)."""
from pathlib import Path
import sys
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from schem import *  # noqa: E402,F403

th, a, L, xs = np.radians(8.0), 20.0, 13.0, -78.0
S, V = P(-a, 0), P(0, 0)
t1, t2 = P(-np.sin(th), np.cos(th)), P(-np.sin(th), -np.cos(th))
n1, n2 = P(-np.cos(th), -np.sin(th)), P(-np.cos(th), np.sin(th))      # face normals toward the source
e1, e2 = V + L * t1, V + L * t2
S1 = S - 2 * np.dot(S - V, n1) * n1
S2 = S - 2 * np.dot(S - V, n2) * n2
fig, ax = canvas(TEXT_WIDTH * 0.82, (-88, 36), (-27, 27))
mirror(ax, e2, V, side=1, lw=1.4)
mirror(ax, V, e1, side=1, lw=1.4)
line(ax, P(xs, -26), P(xs, 26), color=INK, linewidth=0.8)
dot(ax, S)
dot(ax, S1, mfc="white")
dot(ax, S2, mfc="white")
edge = []
for (e, n, Si) in ((e1, n1, S1), (e2, n2, S2)):
    d = unit(V - S)
    r = reflect(d, n)
    Q = hit_x(V, r, xs)
    edge.append(Q)
    ray(ax, [V, Q], AXIAL, arrows=(0.5,))
    dash(ax, V, Si)
    for s, sty in ((1.6, AXIAL), (8.0, AXIAL)):                     # two more rays from each mirror
        M = V + s * (e - V) / L
        r = reflect(unit(M - S), n)
        ray(ax, [S, M], sty, arrows=(0.45,))
        ray(ax, [M, hit_x(M, r, xs)], sty, arrows=(0.5,))
        dash(ax, M, Si)
ray(ax, [S, V], AXIAL, arrows=(0.5,))
lo, hi = sorted(q[1] for q in edge)
for yy in (lo, hi):
    line(ax, P(xs - 4, yy), P(xs, yy), **THIN)
dim(ax, P(xs - 4, lo), P(xs - 4, hi), "", size=7)
text(ax, "region of\ninterference", P(xs - 6, 0), ha="right", size=7)
text(ax, "$S$", S + P(-1.0, 2.6), ha="right")
text(ax, "$S_1$", S1 + P(1.4, 1.8), ha="left")
text(ax, "$S_2$", S2 + P(1.4, -1.8), ha="left")
text(ax, "$M_1$", e1 + P(-2.4, 1.4))
text(ax, "$M_2$", e2 + P(-2.4, -1.4))
dim(ax, S2 + P(7, 0), S1 + P(7, 0), "$d$", size=7)
line(ax, S1, S1 + P(7.5, 0), **THIN)
line(ax, S2, S2 + P(7.5, 0), **THIN)
lab(ax, r"$\theta$ between mirror faces" + "\nand coplanar", V + P(0.3, 0.0), P(8, -17), ha="left", size=7)
text(ax, "screen", P(xs, 27.5), size=7)
done(fig, HERE)
readme(HERE, "Fig 16.6: Fresnel's mirror interferometer", lines=["Construction schematic: ideal plane mirrors, reflections computed from the geometry.",
       "Symbols as named by the figure: S, M1, M2, S1, S2, theta, d (= 2 a theta). theta is drawn at 8 degrees for legibility; no numbers are printed.",
       "The rays through the junction V bound the overlap region; dashed lines are the virtual extensions back to S1 and S2."])
