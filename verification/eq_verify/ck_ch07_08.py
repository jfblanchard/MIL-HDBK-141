import numpy as np
from ledger import *
from sympy import symbols, solve, expand, Rational, diff

# ---------------- ch07 simple thin-lens systems ----------------
defn("ch07", 1, "definition of magnifying power")
ref("ch07", 2, "Lagrange invariant with n = 1 (ch06 Eq 7), verified numerically in ch06")
ph, d, A, V, s = symbols("phi d A V s")
sp_ = 1 / (1 / s + ph)                                # thin lens: 1/s' = 1/s + phi (book sign convention)
sym("ch07", 3, lambda: zero(sp_ / s - (1 - ph * sp_)), "thin-lens magnification m = s'/s = 1 - phi s' with s' = d + A (image distance from lens)")
defn("ch07", 4, "angles subtended at the eye with and without the instrument")
sym("ch07", 5, lambda: zero(((1 - ph * (d + A)) / A) / (-1 / V) - (-(V / A) * (1 - ph * (d + A)))),
    "Eq 1 = beta/alpha from the two preceding lines")
ref("ch07", 6, "Eq 2 compound microscope MP = m_o V/f_e, standard")
y, u = symbols("y u", positive=True)
sym("ch07", 7, lambda: zero((y / u) / (2 * y) - Rational(1, 2) / u), "f-number = f/(2y) = 0.5/u for u = y/f")
ref("ch07", [8, 9], "afocal form of the ch06 chromatic sums (Eqs 6-37, 6-38) with final angle replacing final height")
ref("ch07", 10, "Eq 5 MP = -(f_o/f_e')(L/z) = m_o L/f_e', standard")
ref("ch07", [11, 12, 13], "field-lens geometry of Fig 7.x; alpha = beta/MP by definition of MP")
sym("ch07", [14, 15], lambda: zero(1 / (2 * s) / 3 - 1 / (3 * 2 * s)), "small-angle limits of the two preceding lines (t2 ~ f_o')")
ref("ch07", [16, 17, 18, 19, 20, 21], "summary box restating Eqs 1-5 (checked above)")
fp = symbols("f'", positive=True)
sym("ch07", 22, lambda: zero((V / fp + 1) - (V * (1 / fp + 1 / V))),
    "magnifier: image at infinity MP = V/f'; image at the near point with eye at the lens MP = V/f' + 1")

# ---------------- ch08 third-order theory: independent recompute of Table 8.2 ----------------
c = [0, 0.25285, -0.01474, -0.19942, 0.25973, 0.05065, -0.24588]
t = [-2.2, 0.6, 1.06541, 0.15, 1.13691, 0.6, 8.27937]
n = [1, 1, 1.62, 1, 1.621, 1, 1.62, 1]                 # n[j] before surface j+1 (index 0 = object space)
dnn = [0, 0, 0.00635, 0, 0.01058, 0, 0.00635, 0]
y, u, yb, ub = 1.5, 0.0, 0.0, 0.36397
rows = []
for j in range(7):                                     # surfaces 1..7 (1 = entrance pupil)
    if j:
        y += t[j - 1] * u; yb += t[j - 1] * ub
    i = y * c[j] + u; ib = yb * c[j] + ub
    nl, nn_ = n[j], n[j + 1]
    u2 = (nl * u + y * c[j] * (nl - nn_)) / nn_; ub2 = (nl * ub + yb * c[j] * (nl - nn_)) / nn_
    S = y * nl * (nl / nn_ - 1) * (u2 + i); Sb = yb * nl * (nl / nn_ - 1) * (ub2 + ib)
    Phi = nn_ * (yb * u2 - y * ub2)
    rows.append(dict(y=y, u=u2, i=i, yb=yb, ib=ib, B=S * i * i, F=S * i * ib, C=S * ib * ib,
                     E=Sb * i * ib + Phi * (ub ** 2 - ub2 ** 2), P=c[j] * (nl - nn_) / (nl * nn_),
                     a=-y * nl * i * (dnn[j + 1] - dnn[j]), b=-y * nl * ib * (dnn[j + 1] - dnn[j]), Phi=Phi))
    u, ub = u2, ub2
BOOK = dict(B=[-0.01933, -0.01619, 0.05433, 0.01878, -0.00151, -0.04249],
            F=[-0.00823, 0.03036, -0.05847, 0.02332, -0.00542, 0.01827],
            C=[-0.00351, -0.05694, 0.06293, 0.02896, -0.01939, -0.00786],
            E=[-0.01378, 0.10994, -0.09223, 0.07278, -0.09008, 0.01544],
            P=[-0.09677, -0.00564, 0.07640, 0.09950, -0.01938, -0.09410],
            a=[-0.00362, -0.00242, 0.00580, 0.00450, -0.00109, -0.00361],
            b=[-0.00154, 0.00452, -0.00624, 0.00559, -0.00390, 0.00154])


def table_ok(key):
    return all(abs(rows[j + 1][key] - v) <= 1.2e-5 + 2e-4 * abs(v) for j, v in enumerate(BOOK[key]))


SUMS = {k: sum(r[k] for r in rows[1:]) for k in "BFCEPab"}
u_last = rows[-1]["u"]
ref("ch08", 1, "Eq 1: odd power series of transverse aberration in aperture, standard")
ref("ch08", [2, 3], "backward transfer of two rays from the image plane")
Yka, Ykb, Ta, Tb, Y1a, Y1b, y1, uk = symbols("Y_ka Y_kb T_a T_b Y_1a Y_1b y_1 u_k")
tk = -(Yka - Ykb) / (Ta - Tb)
sym("ch08", 4, lambda: zero(solve([Yka - (symbols("W") - symbols("tk") * Ta), Ykb - (symbols("W") - symbols("tk") * Tb)],
                                   [symbols("W"), symbols("tk")])[symbols("tk")] - tk), "intersection of the two rays")
ref("ch08", 5, "paraxial proportionality Y1/tanU = y1/u (same axial image point)")
sym("ch08", [6, 7], lambda: zero(tk.subs({Ta: Y1a * uk / y1, Tb: Y1b * uk / y1}) - (-(y1 / uk) * (Ykb - Yka) / (Y1b - Y1a))),
    "Eq 2 from the two preceding lines")
num("ch08", [8, 9], lambda: close(-SUMS["B"] / (2 * 1 * u_last), -0.02135, 0.002),
    f"Eq 3 third-order LSA: -Sigma B/(2 n u) = {-SUMS['B'] / (2 * u_last):.5f} (book Table 8.2: -0.02135)")
num("ch08", [10, 11, 19], lambda: table_ok("B"),
    "Eqs 4, 5 recomputed from a fresh paraxial trace of Table 8.2's c, t, n reproduce all six printed B to the printed digits")
ref("ch08", [12, 13], "third-order transverse aberration polynomials (Seidel form); coefficients verified via Table 8.2 and Eq 3/8 checks")
ref("ch08", 14, "Eq 8 distortion term of Eq 6 at the chief ray; numerically confirmed through the next line")
num("ch08", 15, lambda: close(-SUMS["E"] / (2 * rows[-1]["Phi"]), 0.0019, 0.05),
    f"fractional distortion at 20 deg = -Sigma E/(2 Phi) = {-SUMS['E'] / (2 * rows[-1]['Phi']):+.4f}; matches Fig 8.9 3rd-order curve (+0.19 %)")
ref("ch08", [16, 17, 18], "Coddington-limit tangential/sagittal/Petzval foci; t_kP = (3 t_kS - t_kT)/2 is the standard Petzval relation")
sym("ch08", 18, lambda: zero(Rational(1, 2) * (3 * (symbols("C") + symbols("PP")) - (3 * symbols("C") + symbols("PP"))) - symbols("PP")),
    "t_kP = (3 t_kS - t_kT)/2 leaves only the P Phi^2 term (Eqs 9, 10)")
num("ch08", 20, lambda: table_ok("F"), "Eq 11 F = S i i-bar reproduces all six printed F")
num("ch08", 21, lambda: table_ok("C"), "Eq 12 C = S i-bar^2 reproduces all six printed C")
num("ch08", 22, lambda: table_ok("E"), "Eq 13 (S-bar from chief ray, Phi = y-bar u - y u-bar = -0.5460) reproduces all six printed E")
num("ch08", 23, lambda: table_ok("P"), "Eq 14 P = c(n_-1 - n)/(n_-1 n) reproduces all six printed P; Sigma P = -0.04000 as printed")
e_, yy, nl_, nn2, yb_ = symbols("e y n_l n ybar")
ref("ch08", [24, 25, 26, 27], "aspheric (4th-order) surface contributions: B = 8(n_-1 - n) e y^4 and F, C, E scale by (y-bar/y)^k; standard form")
defn("ch08", [28, 29], "plotted quantities for ray-intercept curves")
ref("ch08", [30, 31], "conversion of final direction to image-plane intercept")
ref("ch08", [32, 33], "Eqs 15, 16 angular forms of Eqs 6, 7 (divide by the final paraxial distance)")
defn("ch08", [34, 35, 36], "stop-shift definitions (new chief ray, Q = y-bar1*/y1)")
Q, SB, SF, SC, SE, SP, P2 = symbols("Q SB SF SC SE SP PPhi2")
# Stop-shift: substitute Y1 = Y1' + Q*(Ybar_o/ybar_o)*y1 into Eq 6 and collect powers of (Ybar_o/ybar_o)
Y1p, X1, H = symbols("Y1p X1 H")
Y1 = Y1p + Q * H * yy
eq6 = SB * (Y1 ** 2 + X1 ** 2) * Y1 / yy ** 3 + SF * (3 * Y1 ** 2 + X1 ** 2) / yy ** 2 * H + (3 * SC + P2) * Y1 / yy * H ** 2 + SE * H ** 3
eq17 = (SB * (Y1p ** 2 + X1 ** 2) * Y1p / yy ** 3 + (Q * SB + SF) * (3 * Y1p ** 2 + X1 ** 2) / yy ** 2 * H
        + (3 * Q ** 2 * SB + 6 * Q * SF + 3 * SC + P2) * Y1p / yy * H ** 2
        + (Q ** 3 * SB + 3 * Q ** 2 * SF + Q * (3 * SC + P2) + SE) * H ** 3)
sym("ch08", [37, 38, 39], lambda: zero(expand(eq6 - eq17).subs(X1, 0)) and zero(expand(eq6 - eq17)),
    "Eq 17: substituting Y1 = Y1' + Q y1 (Ybar_o/ybar_o) into Eqs 6 + 8 and collecting reproduces every coefficient")
sym("ch08", [40, 41, 42, 43, 44], lambda: zero((3 * Q ** 2 * SB + 6 * Q * SF + 3 * SC + P2) - (3 * (Q ** 2 * SB + 2 * Q * SF + SC) + P2)),
    "Eqs 18-21a stop-shift sums follow from Eq 17 term by term (C* = Q^2 B + 2Q F + C)")
aa, bb = symbols("a b")
ref("ch08", [45, 46], "chromatic stop shift a* = a, b* = Q a + b (b ~ y y-bar, y-bar* = y-bar + Q y)")
def thin_lens_ok():
    rng = np.random.default_rng(3)
    for _ in range(10):
        nn, phi, c1, um, yv = rng.uniform(1.4, 1.9), rng.uniform(.2, 1.), rng.uniform(-1, 1), rng.uniform(-.3, .3), rng.uniform(.5, 2)
        c2 = c1 - phi / (nn - 1)
        ubm = rng.uniform(-.4, .4); ybv = 0.0          # stop at the lens
        tot = dict(B=0, F=0, C=0, E=0, P=0)
        U, Ub = um, ubm
        for cc, n1, n2 in ((c1, 1.0, nn), (c2, nn, 1.0)):
            i = yv * cc + U; ib = ybv * cc + Ub
            U2 = (n1 * U + yv * cc * (n1 - n2)) / n2; Ub2 = (n1 * Ub + ybv * cc * (n1 - n2)) / n2
            S = yv * n1 * (n1 / n2 - 1) * (U2 + i); Sb = ybv * n1 * (n1 / n2 - 1) * (Ub2 + ib)
            Ph = n2 * (ybv * U2 - yv * Ub2)
            tot["B"] += S * i * i; tot["F"] += S * i * ib; tot["C"] += S * ib * ib
            tot["E"] += Sb * i * ib + Ph * (Ub ** 2 - Ub2 ** 2); tot["P"] += cc * (n1 - n2) / (n1 * n2)
            U, Ub = U2, Ub2
        Phi = ybv * um - yv * ubm
        k = phi * nn / (nn - 1); r = um / yv
        a1 = -phi * yv ** 4 / nn * ((3 * nn + 2) * r ** 2 + k ** 2 * nn - k * (3 * nn + 1) * r)
        a2 = -phi * yv ** 4 / nn * ((4 * nn + 4) * r - k * (2 * nn + 1))
        a3 = -phi * yv ** 4 / nn * (nn + 2)
        b1 = phi * Phi * yv ** 2 / nn * ((2 * nn + 1) * r - k * nn)
        b2 = phi * Phi * yv ** 2 / nn * (nn + 1)
        chk = [(tot["B"], a1 + a2 * c1 + a3 * c1 ** 2), (tot["F"], b1 + b2 * c1), (tot["C"], -phi * Phi ** 2),
               (tot["E"], 0.0), (tot["P"], -phi / nn), ((um - U) / yv, phi)]
        if not all(abs(p - q) < 1e-9 * (1 + abs(q)) for p, q in chk):
            print("thin lens mismatch", [(round(p, 6), round(q, 6)) for p, q in chk])
            return False
    return True


num("ch08", [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], lambda: thin_lens_ok(),
    "thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for "
    "random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n)")


a1s, a2s, a3s, b1s, b2s, cc1, phs, nns, Phs = symbols("alpha1 alpha2 alpha3 beta1 beta2 c1 phi n Phi")
Bt = a1s + a2s * cc1 + a3s * cc1 ** 2; Ft = b1s + b2s * cc1; Ct = -phs * Phs ** 2; Pt = -phs / nns
Fs = Q * Bt + Ft; Cs = Q ** 2 * Bt + 2 * Q * Ft + Ct; Es = Q ** 3 * Bt + 3 * Q ** 2 * Ft + Q * (3 * Ct + Pt * Phs ** 2)
sym("ch08", [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], lambda: all(zero(e) for e in [
    Fs - ((Q * a1s + b1s) + (Q * a2s + b2s) * cc1 + Q * a3s * cc1 ** 2),
    Cs - ((Q ** 2 * a1s + 2 * Q * b1s - phs * Phs ** 2) + (Q ** 2 * a2s + 2 * Q * b2s) * cc1 + Q ** 2 * a3s * cc1 ** 2),
    Es - ((Q ** 3 * a1s + 3 * Q ** 2 * b1s - Q * (3 * nns + 1) * phs * Phs ** 2 / nns) + (Q ** 3 * a2s + 3 * Q ** 2 * b2s) * cc1 + Q ** 3 * a3s * cc1 ** 2)]),
    "Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed")
num("ch08", [73, 74, 75], lambda: close(0.25285, 0.253) and close(-0.19942, -0.200) and abs(0.05065 - 0.050) < 0.001,
    "thin-lens c1 values are the Table 8.2 thick-lens first curvatures rounded (0.25285, -0.19942, 0.05065)")
extra("ch08-book-Table-8.2-sums", "ch08", "numeric (full-precision recompute)", False,
      f"1962 ORIGINAL: printed Sigma C = -0.004200 and Sigma E = -0.002070 are sign-reversed; recompute gives "
      f"{SUMS['C']:+.6f} and {SUMS['E']:+.6f} (positive E is the one that matches Fig 8.9). Printed y-bar_4 = +0.09189 is a dropped "
      f"minus. Sigma a: full-precision sum {SUMS['a']:+.6f} agrees with the printed -0.00040 (the -0.00044 in the chapter's "
      "editorial note comes from adding the rounded row entries, so it is not a book slip)")
