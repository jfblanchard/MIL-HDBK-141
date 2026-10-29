import math
import numpy as np
from ledger import *
from thinfilm import layer, stack, RT, book_RT
from sympy import pi as pi_s, symbols, sqrt, Rational, simplify, solve, cos, sin, Matrix, I as J

rng = np.random.default_rng(7)


def hr_width():
    na, nb = 1.38, 2.3
    dg = 2 / math.pi * math.asin(abs((1 - na / nb) / (1 + na / nb)))
    for g, inside in ((1 + 0.97 * dg, True), (1 + 1.03 * dg, False)):
        d = math.pi / 2 * g
        tr = (layer(na, d) @ layer(nb, d)).trace().real
        if (abs(tr) > 2) != inside:
            return False
    return True


defn("ch20", 1, "phase thickness delta = 2 pi sigma n t (sigma = 1/lambda)")
num("ch20", 2, lambda: close(1e4 / 1.0, 10000), "1 um = 1000 m-mu = 10,000 A <-> 10,000 cm^-1 (sigma = 1/lambda)")
defn("ch20", 3, "quarter-wave optical thickness QWOT = 4 n t")
ref("ch20", [4, 5, 6], "wave in a medium: lambda' = lambda/n")
defn("ch20", 7, "unpolarised averages")
ref("ch20", [8, 9], "stack matrix = ordered product of layer matrices")


def eq9_11():
    for _ in range(20):
        lay = [(rng.uniform(1.3, 2.4), rng.uniform(0.2, 3)) for _ in range(rng.integers(1, 6))]
        n0, ns = 1.0, rng.uniform(1.4, 1.9)
        M = stack(lay, rng.uniform(0.5, 2))
        a, b = RT(M, n0, ns), book_RT(M, n0, ns)
        if not (abs(a[0] - b[0]) < 1e-12 and abs(a[1] - b[1]) < 1e-12 and abs(b[0] + b[1] - 1) < 1e-12):
            return False
    return True


num("ch20", [10, 11, 12, 13], eq9_11,
    "Eqs 9-11 (k_s = 0) equal an independent admittance calculation on 20 random lossless stacks, and R + T = 1 "
    "(Eq 11's '2' is 2 det M = 2(AD + BC))")
num("ch20", 14, lambda: np.allclose(stack([(1.5, 2.0)]), -np.eye(2)) or np.allclose(stack([(1.5, 4.0)]), np.eye(2)),
    "unit matrix: a full-wave layer (or absentee half-wave, up to sign) leaves R unchanged")
ref("ch20", [15, 16], "tilted phase thickness n t cos(theta); s-polarisation effective index n cos(theta)")
ref("ch20", 17, "p-polarisation effective index n/cos(theta)")
ref("ch20", 18, "n_i cos(theta_i) = sqrt(n_i^2 - n_0^2 sin^2 theta_0) at grazing incidence (theta_0 = 90 deg)")
num("ch20", [19, 20], lambda: close(1.56 / 0.977, 1.60, 0.003) and close(2.14 / 0.977, 2.19, 0.001), "0.977 : 1.56 : 2.14 = 1 : 1.597 : 2.190")
defn("ch20", 21, "ratio set as printed")
num("ch20", 22, lambda: close(RT(np.eye(2), 1.0, 1.52)[0], (0.52 / 2.52) ** 2), "bare substrate Fresnel reflectance")


def single():
    for _ in range(10):
        n0, n1, ns, g = 1.0, rng.uniform(1.3, 2.3), rng.uniform(1.4, 1.9), rng.uniform(.3, 2)
        d = math.pi / 2 * g
        a1, a2, a3, a4 = (n0 - ns) ** 2, (n1 - n0 * ns / n1) ** 2, (n0 + ns) ** 2, (n1 + n0 * ns / n1) ** 2
        Rb = (a1 * math.cos(d) ** 2 + a2 * math.sin(d) ** 2) / (a3 * math.cos(d) ** 2 + a4 * math.sin(d) ** 2)
        if abs(Rb - RT(stack([(n1, 1)], g), n0, ns)[0]) > 1e-12:
            return False
    return True


num("ch20", [23, 24, 25], single, "single-layer Eq 23 with a1..a4 equals the matrix result for 10 random layers and wavelengths")
num("ch20", 26, lambda: close(RT(stack([(1.38, 1)]), 1.0, 1.52)[0], ((1.38 ** 2 - 1.52) / (1.38 ** 2 + 1.52)) ** 2, 1e-9),
    "Eq 24 quarter-wave minimum")
defn("ch20", 27, "g = lambda0/lambda")
defn("ch20", 28, "Eq 25: minimum is below the bare value when n1 lies between n0 and ns")
num("ch20", 29, lambda: RT(stack([(math.sqrt(1.52), 1)]), 1.0, 1.52)[0] < 1e-20, "Eq 26: n1 = sqrt(n0 ns) gives R = 0")
Rg = RT(stack([(1.38, 1)], 0.737), 1.0, 1.51)[0]
num("ch20", 30, lambda: abs(Rg - 0.017) < 0.0015,
    f"example (a): MgF2 (1.38) quarter wave at 700 m-mu on n = 1.51, g = 0.737: R = {Rg:.4f} (book reads 0.017 from Fig 20.16)")
defn("ch20", 31, "g = lambda0/lambda")
n1, n2, n0s, nss = symbols("n_1 n_2 n_0 n_s", positive=True)
Q1 = Matrix([[0, J / n1], [J * n1, 0]]); Q2 = Matrix([[0, J / n2], [J * n2, 0]])
sym("ch20", 32, lambda: zero((Q1 * Q2)[0, 0] + n2 / n1) and zero((Q1 * Q2)[1, 1] + n1 / n2), "product of two quarter-wave matrices: -diag(n2/n1, n1/n2)")
num("ch20", 33, lambda: all(abs(RT(stack([(a, 1), (b, 1)]), 1.0, s)[0] - ((1.0 * b * b - s * a * a) / (1.0 * b * b + s * a * a)) ** 2) < 1e-12
                            for a, b, s in rng.uniform([1.3, 1.6, 1.4], [1.7, 2.4, 1.9], (10, 3))),
    "Eq 30 double quarter-wave R equals the matrix result (10 random cases)")
sym("ch20", 34, lambda: zero(((n0s * n2 ** 2 - nss * n1 ** 2)).subs(n2, n1 * sqrt(nss / n0s))), "Eq 31 zeroes Eq 30")
num("ch20", [35, 36], lambda: close(1.38 * math.sqrt(1.51), 1.69, 0.004) and close(1.65 * math.sqrt(1.51), 2.03, 0.002),
    "on n_s = 1.51: 1.38 x sqrt(1.51) = 1.696, 1.65 x sqrt(1.51) = 2.028 (book 1.69, 2.03)")
ref("ch20", 37, "Berning's quarter-half design conditions (geometric progression of indices)")
sym("ch20", 38, lambda: zero(n0s ** Rational(2, 3) * nss ** Rational(1, 3) * n0s ** Rational(1, 3) * nss ** Rational(2, 3) - n0s * nss),
    "Eq 34 follows from Eq 33")
defn("ch20", [39, 40, 41, 42], "index-order and three-layer design conditions")
num("ch20", 43, lambda: hr_width(), "Eq 39: edges of the (LH)^N high-reflectance zone from the matrix trace |A + D| = 2 match the formula")


P_ = symbols("P", positive=True)
sym("ch20", [44, 45], lambda: zero((1 - 4 / (P_ + 1 / P_ + 2)) - (P_ + 1 / P_ - 2) / (P_ + 1 / P_ + 2)), "Eq 40 = 1 - Eq 41")


def peak_P():
    """layers numbered from the incident medium n0 (layer 1 next to n0), as Eqs 42/43 require."""
    na, nb, n0, ns = 1.38, 2.3, 1.0, 1.52
    Te = RT(stack([(na, 1), (nb, 1)] * 4), n0, ns)[1]        # 8 layers, even: Eq 42/45
    Pe = (nb / na) ** 8 * n0 / ns
    To = RT(stack([(nb, 1), (na, 1)] * 3 + [(nb, 1)]), n0, ns)[1]   # 7 layers, odd: Eq 43
    Po = ((nb / na) ** 3 * nb) ** 2 / (n0 * ns)
    return abs(Te - 4 / (Pe + 1 / Pe + 2)) < 1e-12 and abs(To - 4 / (Po + 1 / Po + 2)) < 1e-12 and close(Te, 4 / Pe, 0.1)


num("ch20", [46, 47, 48, 49], peak_P, "Eqs 41-45: peak T of 8-layer (even, Eq 42/45) and 7-layer (odd, Eq 43) quarter-wave stacks from the matrix equals 4/(P + 1/P + 2) exactly, layers numbered from the incident medium; Eq 44 ~4/P within 10% at P = 39")
defn("ch20", 50, "Eq 46 resonance condition")
defn("ch20", [51, 52], "stack notation; 600/4 = 150 m-mu")
num("ch20", 53, lambda: close(2 * (0.92 + 0.879) * 150, 540, 0.001), "(0.92 + 0.879) x 150 = 269.9 = lambda0/2 (q = 1): lambda0 = 540 m-mu (book 540)")
defn("ch20", 54, "stack notation")
R_ = symbols("R", positive=True)
sym("ch20", 55, lambda: zero((1 - R_) ** 2 / (1 - R_ ** 2) - (1 - R_) / (1 + R_)), "incoherent double-plate sum with T = 1 - R")
defn("ch20", [56, 57], "stack notation; example value")
sym("ch20", 58, lambda: zero(((1 - R_) / (1 + R_)) / (1 - R_) - 1 / (1 + R_)) and close(1 / (1 + 0.9999), 0.5, 1e-3),
    "T/(1+R) -> T/2 as R -> 1")
ref("ch20", [59, 60, 61, 62, 63], "Airy transmission of a Fabry-Perot etalon, F = 4R/(1-R)^2, R = sqrt(R1 R2)")
m_, sg, nt, l0 = symbols("m sigma nt lambda_0", positive=True)
sym("ch20", [64, 65], lambda: zero(solve(m_ * pi_s - 2 * pi_s * sg * nt, nt)[0].subs(sg, 1 / l0) - m_ * l0 / 2),
    "peak condition m pi = 2 pi sigma n t with sigma = 1/lambda0 gives m lambda0/2 = n t")
ref("ch20", 66, "free spectral range 1/(2t) in wave numbers (n = 1 gap)")
defn("ch20", 67, "Q definition")
put("ch20", 68, "numeric + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.20-74): printed as the product (lambda0/dlambda)(sigma0/dsigma); the footnote shows the two ratios are "
    "equal, so the product is Q^2. Read as Q = lambda0/dlambda = sigma0/dsigma = m pi sqrt(R)/(1-R): with R = 0.95, t = 1 cm, "
    f"lambda = 0.55 um this gives Q = {2 / 0.55e-4 * math.pi * math.sqrt(.95) / .05:.2e}, the text's 'over two million'")
ref("ch20", [69, 70, 71], "plane waves, reflected wave with phase epsilon; d(lambda)/lambda = d(sigma)/sigma")
put("ch20", 72, "reference (standard form)", "VERIFIED",
    "Lorentzian approximation of Eq 49 near a peak (G = F pi^2 t^2 ...); note the equation number 59 is used twice in the chapter")
defn("ch20", 73, "bandwidth from Q")

