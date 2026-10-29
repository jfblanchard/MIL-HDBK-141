import math
from ledger import *
from sympy import symbols, solve, sqrt, pi

# ---------------- ch09 method of lens design ----------------
ref("ch09", [1, 2, 3, 4, 5, 6, 7], "first-order Taylor expansion of each aberration sum in the construction parameters")
defn("ch09", [8, 9, 10, 11], "finite-difference estimates of the differential coefficients")
defn("ch09", 12, "Airy pattern argument Z = pi Y_e d/(lambda l') (d = diameter measured across the pattern)")
num("ch09", 13, lambda: close(3.8317 / math.pi, 1.22, 0.001),
    "first zero of J1 at Z = 3.832: d = 3.832/pi (lambda l'/Y_e) = 1.2197 lambda l'/Y_e, i.e. the Airy DIAMETER "
    "(radius 0.61 lambda/NA); book's 3.83 and 1.22 are the rounded values")
ref("ch09", 14, "root-sum-square combination of geometric and diffraction blur (empirical rule)")
ref("ch09", [15, 16, 17, 18, 19, 20], "restated ch05/ch06 paraxial equations (verified numerically on Table 6.6)")
ref("ch09", [21, 22], "restated ch06 Eqs 34/35 in the Table 8.2 sign convention (reproduce Table 8.2 a, b rows)")
ref("ch09", [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    "restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08)")

# ---------------- ch10 triplet design ----------------
ya, yb_a, pa, na, yc, yb_c, pc, nc = symbols("y_a ybar_a phi_a nu_a y_c ybar_c phi_c nu_c")
ref("ch10", 1, "ch06 Eq 41 thin-lens lateral colour, three elements")
defn("ch10", 2, "design condition Tch = 0")
ref("ch10", 3, "stop at lens b (y-bar_b = 0) removes the middle term")
defn("ch10", 4, "definition of R")
R = ya * pa / (yc * pc)
sym("ch10", 5, lambda: zero(solve(ya * yb_a * pa / na + yc * yb_c * pc / nc, yb_a)[0] / yb_c - (-(1 / R) * na / nc)),
    "solving the Tch = 0 condition for y-bar_a/y-bar_c")
ref("ch10", 6, "chief ray through the centre of lens b: y-bar_a/y-bar_c = -t3/t5 (thin-lens, small angles)")
sym("ch10", 7, lambda: zero((-(1 / R) * na / nc).subs(nc, na) + 1 / R), "equal nu for lenses a and c")
ref("ch10", [8, 9, 10, 11], "Eqs 1-4 third-order targets for the three thin lenses (stop at b)")
ref("ch10", [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
    "Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0")
defn("ch10", 23, "Eq 16 second curvature from the lens power (c_a = phi_a/(n_a - 1))")
ref("ch10", 24, "Eq 17 parabolic fit of 3Y_k versus bending (B is quadratic in c, ch08 Eq 24)")
for k_, cv, roots in ((25, 0.3380, (0.249, 0.427)), (26, -0.2057, (-0.295, -0.116)), (27, 0.0780, (-0.011, 0.167))):
    num("ch10", k_, lambda cv=cv, roots=roots: all(abs(r - (cv + s * math.sqrt(0.016 / 2.0))) < 0.0015 for r, s in zip(roots, (-1, 1))),
        f"roots of 0 = -2.0(c - {cv})^2 + 0.016: {cv - math.sqrt(0.008):.4f}, {cv + math.sqrt(0.008):.4f} (book {roots[0]}, {roots[1]})")
defn("ch10", 28, "ray data for the design")
defn("ch10", [29, 30, 32, 33, 34, 35], "design targets (Eqs 18-24)")
P, Ph = symbols("P Phi")
sym("ch10", 31, lambda: zero(3 * (-P * Ph ** 2 / 3) + P * Ph ** 2),
    "Eq 20 target makes 3C + P Phi^2 = 0, i.e. a flat tangential field (ch08 Eq 9)")
sym("ch10", 36, lambda: zero(1 / R - yc * pc / (ya * pa)), "restatement of t3/t5 = 1/R")
ref("ch10", 37, "restatement of Eq 17")
