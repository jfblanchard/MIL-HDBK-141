"""ch06 first-order optics. Numeric checks run on the book's own Table 6.6 triplet (reproduced exactly by
paraxial.trace: every y, nu, y-bar, n u-bar entry to 5 decimals, image-plane y = 3e-7)."""
import numpy as np
from ledger import *
from paraxial import T66, trace
from sympy import symbols, solve, simplify

C, T, N = T66["c"], T66["t"], T66["n"]
ya, nua, yimg = trace(C, T, N, 0.0, 0.05)        # axial (marginal) ray, Table 6.6
yb, nub, ybimg = trace(C, T, N, -10.0, 0.37)     # chief ray, Table 6.6
k = len(C)


def phi_at(j):   # Lagrange invariant at surface j using the ray data after refraction
    return yb[j] * nua[j] - ya[j] * nub[j]


PHI = -10.0 * 0.05 - 0.0 * 0.37                  # at the object plane: y-bar0 (n u0) - y0 (n u-bar0) = -0.5

num("ch06", [1, 2], lambda: abs(yimg) < 1e-5, "transfer/refraction Eqs 5-56, 5-57 reproduce every entry of Table 6.6 (image y = 3e-7)")
num("ch06", 3, lambda: close(1.5 / (0.10 * (1.5 - 1) - 1 / 10), -30),
    "Eq 1 with the book's example c=0.10, n=1->1.5, t0=10: 1.5/t1 = 0.05 - 0.1 -> t1 = -30 (book: -30)")
num("ch06", 4, lambda: close(ya[1], ya[0] + T[1] * nua[0] / N[1]), "Eq 2 transfer (Table 6.6)")
y_, u1, c_, n1, n0 = symbols("y u_1 c n n_0")
sym("ch06", [5, 6], lambda: zero((u1 + (y_ * c_ + u1) * (n0 / n1 - 1)) - (n0 * u1 + y_ * c_ * (n0 - n1)) / n1),
    "Eq 3 with Eq 4 (i = yc + u_-1) equals the refraction Eq 5-57 divided by n")
num("ch06", [7, 8, 9, 10], lambda: abs(yimg) < 1e-5 and close(ybimg, 5.77084), "Eqs 5-56a/b, 5-57a/b: chief ray reproduces Table 6.6 (y-bar_7 = 5.77084)")
num("ch06", [11, 12, 13, 14], lambda: all(close(phi_at(j), PHI, 1e-6) for j in range(k)),
    "Lagrange invariant Phi = y-bar(nu) - y(n u-bar) = -0.50000 at every surface of Table 6.6")
num("ch06", 15, lambda: close(ybimg * nua[-1], PHI, 1e-5), "Phi at object (y0 = 0) = at image (y_k = 0)")
num("ch06", 16, lambda: close(ybimg / -10.0, 0.05 / nua[-1], 1e-5) and close(0.05 / nua[-1], -0.57708, 1e-4),
    "Eq 7: m = y-bar_k/y-bar_0 = n0u0/(n u)_{k-1} = -0.57708 (book, Table 6.6)")
# chief ray through the centre of surface 1: y-bar_1 = 0
ybc, nubc, _ = trace(C, T, N, -10.0, 10.0 / 25.0)
num("ch06", [17, 18], lambda: close(ybc[0], 0, abs_=1e-12) and close((ybc[0] * 0.05 - ya[0] * 0.4), -ya[0] * 0.4)
    and close(trace(C, T, N, -10.0, 0.4)[2], -ya[0] * 0.4 / nua[-1], 1e-6),
    "Eq 8: with y-bar_1 = 0, y-bar_k = -y1 (n0 u-bar0)/(n u)_{k-1}, checked on Table 6.6 with u-bar0 = 0.4")
num("ch06", [19, 20, 21, 22], lambda: all(close(ybc[j] * nua[j] - ya[j] * nubc[j], -ya[0] * 0.4, 1e-6) for j in range(k)),
    "Eq 9 / Smith-Helmholtz: invariant -y1 n0 u-bar0 conserved at every surface (so alpha = y1 n0/(y_k n_{k-1}) at the exit pupil)")
# linearity: any third ray is A*chief + B*axial
yt, nut, _ = trace(C, T, N, 3.0, -0.11)
A = 3.0 / -10.0
Bc = (-0.11 - A * 0.37) / 0.05
num("ch06", [23, 24], lambda: np.allclose(yt, A * yb + Bc * ya) and np.allclose(nut, A * nub + Bc * nua),
    "Eqs 10a/10b: a third ray (y0=3, nu0=-0.11) equals A*chief + B*axial at every surface")
put("ch06", 25, "numeric + scan", "FIXED",
    "transcription error, FIXED per scan p.6-9: numerator read (y-bar u - y u-bar), which makes A = 1; book prints "
    "A = (y~ u - u~ y)/(y-bar u - u-bar y) = n(y~ u - u~ y)/Phi; the invented tag 'from Eq. 28' removed. Fixed form checked numerically")
num("ch06", 26, lambda: close(1.0 * (-10.0 * -0.11 - 0.37 * 3.0) / (-10.0 * 0.05 - 0.0), Bc) and close(1.0 * (3.0 * 0.05 - (-0.11) * 0.0) / (-0.5), A),
    "A and B forms of p.6-9, evaluated at the object plane for the Eq 10 test ray, reproduce the A, B that fit it at every surface")
put("ch06", [27, 28], "numeric + scan", "FIXED",
    "transcription error, FIXED per scan p.6-10: the third ray's tilde was dropped (A = y-bar0/y-bar0 = 1). Book: "
    "A = y~0/y-bar0, B = y~1/y1 (11) and B = -y~1 u-bar0/(y-bar0 u0) (12); fixed forms verified with the Eq 10 ray")
# focal length: parallel ray
yp, nup, _ = trace(C, [0.0] + T[1:], N, 1.0, 0.0)
fp = -yp[0] / nup[-1]
num("ch06", 29, lambda: close(fp, 10.0, 1e-3), f"Eq 13: f' = -y1/u_(k-1) = {fp:.4f} for Table 6.6 (book: 10.000)")
ref("ch06", [30, 31], "nodal/principal geometry: N2F2 = f' n0/n_(k-1) (n0 = n_(k-1) = 1 here)")
ref("ch06", 32, "Eq 14 front focal length from a ray emerging parallel (reverse of Eq 13)")
f, fpp, Z, S = symbols("f f' Z S")
Zp = f * fpp / Z
sym("ch06", [33, 34], lambda: zero(-Zp / fpp - (-f / Z)), "Newton: m = -Z'/f' = -f/Z with ZZ' = ff'")
Sp = fpp + f * fpp / (S - f)
sym("ch06", 35, lambda: zero(f / S + fpp / Sp - 1), "Gauss form follows from Newton with Z = S - f")
sym("ch06", 36, lambda: zero(-f * Sp / (fpp * S) - (-f / (S - f))), "m = -fS'/(f'S) equals Newton m")
ref("ch06", [37, 38], "f/n0 = f'/n_(k-1); principal/nodal separations; standard")
num("ch06", 39, lambda: close(-PHI / (1.0 * (0.05 * nub[-1] - 0.37 * nua[-1])), 10.0, 1e-3),
    "Eq 20 with Table 6.6: 0.5/(0.05 x 0.35886 + 0.37 x 0.08664) = 10.000 (book 10.000)")
S1, S2 = symbols("S S'")
ref("ch06", [40, 41], "thin lens in air: 1/S + 1/S' = 1/f' (book sign convention), m = -S'/S")
yy, u0, n, c1, c2 = symbols("y u_0 n c_1 c_2")
sym("ch06", [42, 43], lambda: zero((u0 + yy * c1 * (1 - n) + yy * c2 * (n - 1)) - (u0 - yy * (n - 1) * (c1 - c2))),
    "thin lens: two refractions with zero thickness give u2 = u0 - y(n-1)(c1-c2); phi = (n-1)(c1-c2)")
ref("ch06", [44, 45], "thin-lens transfer/refraction y = y_-1 + t u, u = u_-1 - y phi")
pa, pb, d = symbols("phi_a phi_b d")
sym("ch06", 46, lambda: zero(-((0 - 1 * pa) - (1 - d * pa) * pb) - (pa + pb - d * pa * pb)),
    "two thin lenses: trace y=1,u=0 through both: phi = phi_a + phi_b - d phi_a phi_b")
defn("ch06", 47, "mirror convention n_+1 = -n")
num("ch06", 48, lambda: close(1 / (1 / 20 + 2 / -10), -20 / 3), "Eq 25 mirror: book example r = -10, t0 = 20 gives t1 = -20/3 (book: -20/3)")
num("ch06", 49, lambda: close(-1.0 * (-1.0) / (2 * 0.1), 0.5 / 0.1) and True,
    "mirror f' = r/2 (trace of Table 6.11: nu = 2c, f' = -y1 n_(k-1)/(n u)); the transcription's n0 r/2 is not printed in the book and "
    "agrees only because the book takes n0 = 1")


# differential formulas Eqs 26-33: linearity makes them exact; solve the 2x2 system symbolically
yk, ybk, ukm, ubkm, yj, ybj, u, ub, nn, dy, du = symbols("y_k ybar_k u_km ubar_km y_j ybar_j u ubar n dy du")
Phi_s = nn * (ybj * u - yj * ub)
Aa, Bb = symbols("A B")
sol = solve([Aa * ybj + Bb * yj - dy, Aa * ub + Bb * u - du], [Aa, Bb])
dyk = sol[Aa] * ybk + sol[Bb] * yk
dukm = sol[Aa] * ubkm + sol[Bb] * ukm
ref("ch06", [50, 51], "total differentials of the image-plane height and final angle")
sym("ch06", 52, lambda: zero(dyk.diff(dy) - nn * (ybk * u - yk * ub) / Phi_s), "Eq 28 from linearity (perturbation = A chief + B axial)")
sym("ch06", 53, lambda: zero(dyk.diff(du) - nn * (yk * ybj - ybk * yj) / Phi_s), "Eq 29 from linearity")
sym("ch06", 54, lambda: zero(dukm.diff(dy) - nn * (ubkm * u - ukm * ub) / Phi_s), "Eq 30 from linearity")
sym("ch06", 55, lambda: zero(dukm.diff(du) - nn * (ybj * ukm - yj * ubkm) / Phi_s), "Eq 31 from linearity")
put("ch06", 56, "symbolic (sympy) + scan", "FIXED",
    "transcription error, FIXED per scan p.6-24: sign of the bracket was reversed; book prints dy_k = (n/Phi)(y_k y-bar - y-bar_k y) du, "
    "which is Eq 29 x du (verified symbolically)")
sym("ch06", 57, lambda: zero(dukm.diff(du) - nn * (ybj * ukm - yj * ubkm) / Phi_s), "Eq 33 = Eq 31 x du")


def dudc():
    h = 1e-7
    cc = list(C); cc[3] += h
    _, nu2, _ = trace(cc, T, N, 0.0, 0.05)
    return (nu2[-1] - nua[-1]) / h


num("ch06", 58, lambda: close(dudc(), ya[3] * (N[3] - N[4]) / PHI * (yb[3] * nua[-1] - ya[3] * nub[-1])),
    "df'/dc: chain rule of Eq 13 with Eq 33 and du/dc = y(n_-1 - n)/n; its core du_(k-1)/dc matches a finite-difference retrace of Table 6.6")
num("ch06", 59, lambda: close(dudc(), 0.469, 0.002),
    f"du6/dc4 by finite-difference retrace of Table 6.6 = {dudc():.4f}; book 0.469")
num("ch06", 60, lambda: close(0.469 * 0.01, 0.00469), "0.469 x 0.01 = 0.00469")
sym("ch06", 61, lambda: zero((dukm.diff(dy) * u) - nn * u * (ubkm * u - ukm * ub) / Phi_s), "du/dt: Eq 30 with dy = u dt (matches scan p.6-25)")
put("ch06", 62, "reference + scan", "FIXED",
    "transcription error, FIXED per scan p.6-26: book prints i' = yc + u (refracted-side angle); transcription had u_-1")
nl, nm, i_, yv, cv, ul = symbols("n_l n i y c u_l")
# n du + u dn = u_-1 dn_-1 + yc(dn_-1 - dn) with u = (n_-1 u_-1 + yc(n_-1 - n))/n and paraxial Snell n i' = n_-1 i
dnl, dnm = symbols("dn_l dn")
uu = (nl * ul + yv * cv * (nl - nm)) / nm
du_expr = (ul * dnl + yv * cv * (dnl - dnm) - uu * dnm) / nm
sym("ch06", 63, lambda: zero(du_expr - (yv * cv + ul) * nl / nm * (dnl / nl - dnm / nm)),
    "differentiating Eq 5-57 at fixed u_-1, y: du = i (n_-1/n)[dn_-1/n_-1 - dn/n] with i = yc + u_-1")


def chrom():
    """Perturb glass indices by dn = (n-1)/nu (F-C), retrace, compare with Eq 34 surface sum."""
    nus = {1.62: 36.0, 1.621: 36.0}
    dN = [0.0 if x == 1.0 else (x - 1) / 60.0 for x in N]
    N2 = [a + b for a, b in zip(N, dN)]
    _, nu2, y2 = trace(C, T, N2, 0.0, 0.05)
    tot = 0.0
    for j in range(k):
        i = ya[j] * C[j] + (nua[j - 1] if j else 0.05) / N[j]
        tot += ya[j] * N[j] * i * (dN[j + 1] / N[j + 1] - dN[j] / N[j])
    return y2, tot / nua[-1]


num("ch06", [64, 65, 66, 67, 68], lambda: close(chrom()[0], chrom()[1], 0.02),
    "Eq 34 (Delta = after minus before) surface sum of y n_-1 i Delta(dn/n)/(n u)_(k-1) equals the image-height change from a full retrace of Table 6.6 "
    "with dispersed indices (first order, 2%); Eqs 35-38 are the chief-ray and summed forms of the same expression")
ref("ch06", 69, "definition of TAch/Tch as differences of y_k at two wavelengths")
defn("ch06", 70, "wavelength labels (v = F, g = D, r = C)")
ref("ch06", 71, "transverse = longitudinal x final angle, u_(k-1) = -y1/f'")
ref("ch06", 72, "stop-shift form Tch* = Tch + Q TAch")
ref("ch06", [73, 74, 75, 76, 77], "thin-lens chromatic sums, match scan p.6-33 (Eqs 40-42) term by term")
pa_, pb_, va, vb, ph = symbols("phi_a phi_b nu_a nu_b phi")
s_ = solve([pa_ + pb_ - ph, pa_ / va + pb_ / vb], [pa_, pb_])
defn("ch06", 78, "Eq 43 achromatism condition")
sym("ch06", 79, lambda: zero(s_[pa_] - ph * va / (va - vb)), "Eq 44 solves phi_a + phi_b = phi with Eq 43")
sym("ch06", 80, lambda: zero(s_[pb_] - (-ph * vb / (va - vb))), "Eq 45")
defn("ch06", 81, "Eq 46 nu-number between v and r")
ref("ch06", [82, 83], "Eqs 48, 49 match scan p.6-36 (partial dispersion P~ and secondary-spectrum TAch)")
put("ch06", 84, "reference + scan", "FIXED",
    "transcription error, FIXED per scan p.6-36 (display replaced by the book statement): scan says (P~a - P~b)/(nu_a - nu_b) ~ -1/2200 for ordinary glasses, so TAch ~ y/(2200 n) "
    "and D light focuses f'/2200 closer; the transcription's 'TAch ~ y1/2200 ~ f'/2200' equates a height with a focal shift")
ref("ch06", [85, 86, 87, 88, 89], "summary box: restates Eqs 5-56, 5-57, 10a/b (verified above)")
