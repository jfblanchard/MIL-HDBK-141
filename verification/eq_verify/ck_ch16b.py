import math
import cmath
from ledger import *
from sympy import (symbols, sin, cos, sqrt, pi, series, solve, simplify, exp, I, Abs, expand, re as Re, im as Im, conjugate, factorial, Sum, oo)

lam, R, d0, mu = symbols("lambda R delta0 mu", positive=True)
r_ = symbols("r", positive=True)
defn("ch16", 91, "dark-fringe condition")
sym("ch16", [92, 93], lambda: zero(solve((-pi + 2 * pi * r_ ** 2 / (lam * R) - mu * pi), r_)[0] - sqrt(lam * R * (mu + 1) / 2)),
    "with delta0 = pi: r_mu^2 = lambda R (mu + 1)/2")
aa, bb, th, t1, t2, m1, m2 = symbols("a b theta theta1 theta2 m1 m2", real=True)
Z = aa + I * bb
defn("ch16", [94, 95], "complex number and conjugate")
sym("ch16", [96, 97, 98], lambda: zero((Z + conjugate(Z)) / 2 - aa) and zero((Z - conjugate(Z)) / (2 * I) - bb) and zero(expand(Z * conjugate(Z)) - aa ** 2 - bb ** 2),
    "real/imaginary parts and |Z|^2")
sym("ch16", [99, 100, 101, 102], lambda: zero(exp(I * th).rewrite(cos) - (cos(th) + I * sin(th))), "Euler form; a = |Z| cos, b = |Z| sin, tan = b/a")
xx = symbols("x")
sym("ch16", [103, 104, 105, 106], lambda: zero(series(cos(xx), xx, 0, 8).removeO() - (1 - xx ** 2 / 2 + xx ** 4 / 24 - xx ** 6 / 720))
    and zero(series(sin(xx), xx, 0, 8).removeO() - (xx - xx ** 3 / 6 + xx ** 5 / 120 - xx ** 7 / 5040))
    and zero(series(exp(I * xx), xx, 0, 5).removeO() - sum((I * xx) ** j / factorial(j) for j in range(5))),
    "Maclaurin series of cos, sin, exp(i theta)")
sym("ch16", [107, 108, 109], lambda: zero(m1 * exp(I * t1) * m2 * exp(I * t2) - m1 * m2 * exp(I * (t1 + t2)))
    and zero(m1 * exp(I * t1) / (m2 * exp(I * t2)) - m1 / m2 * exp(I * (t1 - t2))), "products/quotients of polar forms; conjugate")
put("ch16", 110, "symbolic + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-28): the amplitude a is dropped from the sine term; a e^{i(phi - wt)} = a[cos + i sin]")
sym("ch16", [111, 112], lambda: zero(expand(aa * exp(I * th) * aa * exp(-I * th)) - aa ** 2), "|E|^2 = E E-bar = a^2")
defn("ch16", 113, "complex transmittance (printed e^{ind}: the wave number k is implied in the exponent)")
defn("ch16", 114, "transmitted wave")
put("ch16", 115, "reference + scan", "FLAG", "1962 ORIGINAL (sic, scan p.16-28): amplitude a dropped, as in Eq 94; E' = rho a e^{i(...)}")
defn("ch16", [116, 117, 118, 119, 120], "Snell through the plate; round-trip phase alpha; successive transmitted amplitudes")
ref("ch16", 121, "sum of transmitted amplitudes")
defn("ch16", 122, "round-trip amplitude factor A")
A, al, N = symbols("A alpha N", positive=True)
sym("ch16", 123, lambda: zero(simplify(sum((A * exp(I * al)) ** j for j in range(6)) - (1 - (A * exp(I * al)) ** 6) / (1 - A * exp(I * al)))),
    "finite geometric series (checked for N = 5)")
ref("ch16", 124, "Eq 102 with Eq 104")
num("ch16", 125, lambda: all(abs(abs((1 - Av ** 6 * cmath.exp(6j * av)) / (1 - Av * cmath.exp(1j * av))) ** 2
                                  - (1 - 2 * Av ** 6 * math.cos(6 * av) + Av ** 12) / (1 - 2 * Av * math.cos(av) + Av ** 2)) < 1e-12
                              for Av, av in ((0.3, 0.7), (0.9, 2.1), (0.55, 4.0))),
    "|Eq 105|^2 equals Eq 106 (N = 5, three test points)")
sym("ch16", 126, lambda: zero(((1 - 0) / (1 - 2 * A * cos(al) + A ** 2)) - 1 / (1 - 2 * A * cos(al) + A ** 2)), "N -> infinity with A < 1")
defn("ch16", 127, "maxima")
sym("ch16", 128, lambda: zero(series(1 / (1 - 2 * A * cos(al)), A, 0, 2).removeO() - (1 + 2 * A * cos(al))), "weak reflection: first order in A")
ref("ch16", 129, "Eq 107 at alpha = 2 pi nu: 2W = tau^2/(1-A)^2 (B^2 = half the numerator)")
defn("ch16", 130, "offset from a peak")
da = symbols("Delta", positive=True)
sym("ch16", [131, 132], lambda: zero(solve((1 - A) ** 2 + A * da ** 2 - 2 * (1 - A) ** 2, da)[0] - (1 - A) / sqrt(A)),
    "half-maximum: 1 - 2A cos(da) + A^2 = 2(1-A)^2 with cos(da) ~ 1 - da^2/2 gives da = (1-A)/sqrt(A)")
defn("ch16", [133, 134, 135, 136], "successive reflected amplitudes")
put("ch16", 137, "reference + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-32): exponent printed e^{(alpha - delta_1,0)} without the i; the sum otherwise follows from Eq 114 terms")
defn("ch16", 138, "Eq 116 definition of C")
ref("ch16", 139, "alpha = 2 pi nu: e^{i nu alpha} = 1")
d10, d01, C_ = symbols("delta10 delta01 C")
put("ch16", 140, "symbolic (sympy) + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-32): factoring r01 e^{i delta01} out of the previous line leaves C/r01, not C, inside the bracket "
    "(expanding the printed form gives r01 C e^{-i delta10} sum A^nu). The conclusion Eq 118 is unaffected")
defn("ch16", 141, "phase condition for dark reflected fringes")
defn("ch16", [142, 143, 144, 145, 146, 147, 148], "multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions")
ref("ch16", 149, "sum of the transmitted waves")
defn("ch16", [150, 151], "small-angle approximations")
kk, n, x, z, ph, Rr = symbols("k n x z phi Rr", positive=True)
nu_ = symbols("nu", integer=True, nonnegative=True)


def k_n_x(ang):
    return kk * n * x * ang

sym("ch16", 152, lambda: zero((nu_ * ph + k_n_x(2 * nu_ * symbols("alpha"))) - nu_ * (ph + 2 * kk * n * x * symbols("alpha"))), "phase of the nu-th wave with sin 2 nu alpha -> 2 nu alpha")


ref("ch16", [153, 154, 155], "geometric sum and its modulus, as Eqs 104-106")
sym("ch16", 156, lambda: zero((2 * kk * n * x * symbols("alpha")).subs(kk, 2 * pi / lam) - 4 * pi * n * x * symbols("alpha") / lam), "2knx alpha = 4 pi n x alpha/lambda")
defn("ch16", 157, "wedge thickness")
dd = symbols("d", positive=True)
sym("ch16", 158, lambda: zero(solve(ph + 4 * pi * n * dd / lam - nu_ * 2 * pi, dd)[0] * 2 * n - (nu_ * lam - lam * ph / (2 * pi))), "Eq 127 from Eq 125")
sym("ch16", 159, lambda: zero(solve(4 * pi * n * x * symbols("alpha") / lam - 2 * pi, x)[0] - lam / (2 * n * symbols("alpha"))), "fringe spacing")
h, Dx, alp = symbols("h Dx alpha", positive=True)
sym("ch16", [160, 161], lambda: zero((Dx * lam / (2 * n * h)).subs(h, lam / (2 * n * alp)) - alp * Dx), "step height from fringe shift; with h = lambda/(2 n alpha): t = alpha dx")
ref("ch16", 162, "Eq 127 with n = 1, f = -phi/(2 pi)")
b, f0, l0, s0, lv, lp, p, d_ = symbols("b f0 lambda0 s0 lambda_nu lambda_p p d")
defn("ch16", 163, "phase-change dispersion expansion")
lamv = symbols("lamv")
sym("ch16", [164, 165], lambda: zero(series((2 * d_ + lamv * (f0 + b * (lamv - l0))).subs(lamv, l0 + symbols("e")), symbols("e"), 0, 2).removeO()
                                     - series((2 * d_ - b * l0 ** 2 + (f0 + b * l0) * lamv).subs(lamv, l0 + symbols("e")), symbols("e"), 0, 2).removeO()),
    "Eq 133 agrees with Eq 131 + Eq 132 to first order about lambda0, with s0 = f0 + b lambda0")
sym("ch16", [166, 167], lambda: zero(solve(lv * (nu_ - s0) - lp * (nu_ + p - s0), nu_)[0] - s0 - p * lp / (lv - lp)), "Eq 136 from Eq 135")
ref("ch16", [168, 169, 170], "Eq 137 from Eq 133; difference of two thicknesses (same order: t = (nu - s0)(lambda_nu - lambda_mu)/2)")
ref("ch16", 171, "error propagation of Eq 139 with independent errors <= |dlambda| in each wavelength")
n0, n1, t0, c = symbols("n0 n1 t0 c", positive=True)
AB = symbols("AB", positive=True)
defn("ch16", [172, 173, 174], "Huygens construction for refraction")
sym("ch16", 175, lambda: zero((c * t0 / n0 / AB) / (c * t0 / n1 / AB) - n1 / n0), "Snell's law from wavelet speeds")
