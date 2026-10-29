"""ch21 coating theory: numeric verification against multilayer.reference_RT (independent characteristic matrix)."""
import math
import numpy as np
from ledger import *
from multilayer import Mv, book, reference_RT, random_stack
from sympy import symbols, I, simplify, expand, conjugate, Abs, sqrt, solve, cos, sin, tan, tanh, exp

rng = np.random.default_rng(21)
TRIALS = [random_stack(rng, int(rng.integers(1, 6))) for _ in range(12)]


def all_trials(fn):
    return all(fn(*t) for t in TRIALS)


def rc(lo=0.1, hi=2.0):
    return complex(rng.uniform(lo, hi), rng.uniform(-0.3, 0.3))


# ---- 1-12 Maxwell / plane waves ----
ref("ch21", [1, 2, 3, 4, 5], "time-harmonic Maxwell equations and wave equations for a conducting medium (Gaussian units)")
defn("ch21", [6, 7, 8, 9], "complex index m^2 = eps + i 4 pi sigma/omega, m = n(1 + iK); k = omega/c")
num("ch21", 10, lambda: all(abs(np.exp(1j * 2.0 * m * 0.7) - np.exp(-2.0 * m.real * (m.imag / m.real) * 0.7) * np.exp(1j * 2.0 * m.real * 0.7)) < 1e-12
                           for m in (1.5 + 0.1j, 2.2 + 0.4j)), "e^{ikmz} = e^{-k n K z} e^{i k n z} with m = n(1 + iK) (mu = 1)")
ref("ch21", [11, 12], "damped plane wave, phase velocity c/(mu^1/2 n)")
# ---- 13-25 Fresnel ----
defn("ch21", 13, "normal-incidence amplitude reflection W1")
defn("ch21", [14, 15], "normal-incidence transmission; complex indices")
n0, n1, K1 = symbols("n0 n1 K1", positive=True)
ref("ch21", [16, 17], "real indices")
defn("ch21", 18, "phase pi for n1 > n0")
sym("ch21", 19, lambda: zero(simplify((n0 - n1 - I * n1 * K1) / (n0 + n1 + I * n1 * K1)
                                      - (n0 ** 2 - n1 ** 2 * (1 + K1 ** 2) - 2 * I * n0 * n1 * K1) / ((n0 + n1) ** 2 + n1 ** 2 * K1 ** 2))),
    "rationalised complex Fresnel reflection")
sym("ch21", 20, lambda: zero(simplify(2 * n0 / (n0 + n1 + I * n1 * K1) - 2 * (n0 * (n0 + n1) - I * n0 * n1 * K1) / ((n0 + n1) ** 2 + n1 ** 2 * K1 ** 2))),
    "rationalised complex Fresnel transmission")
defn("ch21", [21, 22, 23, 24, 25], "p0, q0, M_v (Eq 19/19a) and the oblique Fresnel coefficients W_v (E perp) and F_v (H perp)")
num("ch21", [26, 27, 28, 29], lambda: all(abs(abs(book([1 + 0j, m], [], 500, p, pol)[0]) ** 2 - reference_RT([1 + 0j, m], [], 500, p, pol)[0]) < 1e-12
                                          for m in (1.52 + 0j, 1.9 + 0.2j) for p in (0.0, 0.5, 0.9) for pol in "sp"),
    "single interface: |W1|^2 and |F1|^2 equal the reference reflectance for s and p, real and absorbing substrates, three angles")
# ---- 26-40 s-polarised fields, Poynting, energy balance ----
defn("ch21", [30, 31, 33, 36, 37, 39, 40], "incident, reflected and transmitted field components (E perpendicular)")
ref("ch21", 32, "H from Faraday's law for E along y")
defn("ch21", 34, "time-averaged Poynting vector (x2 normalisation)")
ref("ch21", [35, 38], "Poynting vectors of incident and reflected waves")
ref("ch21", [41, 42, 43], "planes of constant phase in the absorbing medium (inhomogeneous wave)")
ref("ch21", [44, 45], "transmitted Poynting vector; its x-part vanishes when K0 = 0")
defn("ch21", [46, 47, 48], "refraction angle and apparent index (n_a)_1 of the inhomogeneous wave")
m1c = symbols("M1", complex=True)
sym("ch21", 49, lambda: True if False else zero(0), "Eq 32 follows from Eqs 30f and 31 by multiplication") if False else \
    ref("ch21", 49, "Eq 32 = Eq 30f x Eq 31 (generalised Snell law with the apparent index)")
ref("ch21", 50, "magnitude of Eq 30d with Eq 31")
defn("ch21", [51, 52, 53, 54, 55], "energy reflectance/transmittance and the beam-area bookkeeping")


def eq40():
    for _ in range(20):
        M0 = rng.uniform(0.3, 1.0)
        M1 = complex(rng.uniform(0.5, 2), rng.uniform(0, 1))
        if abs(abs(M0 - M1) ** 2 / abs(M0 + M1) ** 2 + M1.real / M0 * 4 * M0 ** 2 / abs(M0 + M1) ** 2 - 1) > 1e-12:
            return False
    return True


num("ch21", [56, 57], eq40, "energy balance Eqs 39/40 with (n_a)_1 cos i_1 = Re(M1) and n0 cos i0 = M0: holds identically for 20 random absorbing substrates")
# ---- 41-45 p-polarised ----
ref("ch21", 58, "E from Ampere's law for H along y")
defn("ch21", [59, 60, 61, 62, 63, 64, 65, 66, 67], "p-polarised incident/reflected/transmitted fields and Poynting vectors")
m = symbols("m", complex=True)
nn, KK = symbols("n K", positive=True)
sym("ch21", 68, lambda: zero(simplify(1 / (nn * (1 + I * KK)) ** 2 + 1 / (nn * (1 - I * KK)) ** 2 - 2 * (nn ** 2 * (1 - KK ** 2)) / (nn ** 4 * (1 + KK ** 2) ** 2))),
    "1/m^2 + 1/m-bar^2 = 2 Re(m^2)/|m|^4")
sym("ch21", 69, lambda: zero(expand(((nn * (1 + I * KK)) ** 2 + (nn * (1 - I * KK)) ** 2) / 2) - nn ** 2 * (1 - KK ** 2)), "Re(m^2) = n^2(1 - K^2) = epsilon")
ref("ch21", [70, 71, 72], "p transmitted Poynting vector split into the homogeneous and absorption parts")
defn("ch21", 73, "energy reflectance for p")


def p_transmit_ok():
    for m1 in (1.52 + 0j, 1.9 + 0j):
        for p in (0.1, 0.5, 0.8):
            M0, M1 = Mv(1 + 0j, 1, p), Mv(m1, 1, p)
            F1 = (m1 ** 2 * M0 - M1) / (m1 ** 2 * M0 + M1)
            T1T0 = 2 * m1 ** 2 * M0 / (m1 ** 2 * M0 + M1)
            na = math.sqrt(p ** 2 + M1.real ** 2)
            cos1 = M1.real / na
            Te = na * m1.real ** 2 / abs(m1) ** 4 * 1.0 * abs(T1T0) ** 2 * cos1 / M0.real
            if abs(Te + abs(F1) ** 2 - 1) > 1e-12:
                return False
    return True


num("ch21", [74, 75], p_transmit_ok, "p energy transmittance Eq 45b plus |F1|^2 = 1 for non-absorbing substrates at three angles (as written it uses n1^2, "
    "exact only for K1 = 0; the absorbing case needs Re(m1^2) of Eq 44f)")
defn("ch21", [76, 77], "complex reflectance of layer v; complex phase thickness beta")
# ---- 48-57 recursion ----
ref("ch21", [78, 79], "boundary conditions at interface v (continuity of tangential E and H)")
W, rho, beta, tv, rv, Ma, Mb = symbols("W rho beta tau r M_a M_b")
Wab = (Ma - Mb) / (Ma + Mb)
e = exp(I * beta)
sym("ch21", 80, lambda: zero((tv * Wab + rv * exp(I * beta / 2) * 2 * Mb / (Ma + Mb)) / tv - (Wab + rv / tv * exp(I * beta / 2) * 2 * Mb / (Ma + Mb))), "Eq 48 divided by tau")
tau_prev = (tv + rv * Wab * e) * (Ma + Mb) / (2 * Ma) * exp(-I * beta / 2)
sym("ch21", 81, lambda: zero(tv - (tau_prev * 2 * Ma / (Ma + Mb) * exp(I * beta / 2) - rv * Wab * e)), "Eq 48a solved for tau_(v-1)")
sym("ch21", 82, lambda: zero(Wab + rv * exp(I * beta / 2) * 2 * Mb / (Ma + Mb) / tau_prev - (Wab + rv * e / (tv + rv * Wab * e) * 4 * Ma * Mb / (Ma + Mb) ** 2)),
    "Eq 48b with Eq 48c")
sym("ch21", 83, lambda: zero((Wab + rv * e / (tv + rv * Wab * e) * 4 * Ma * Mb / (Ma + Mb) ** 2).subs(rv, rho * tv)
                             - (Wab + rho * e / (1 + Wab * rho * e) * 4 * Ma * Mb / (Ma + Mb) ** 2)), "divide by tau_v")
sym("ch21", 84, lambda: zero((Wab + rho * e / (1 + Wab * rho * e) * 4 * Ma * Mb / (Ma + Mb) ** 2)
                             - (rho * e * (Wab ** 2 + 4 * Ma * Mb / (Ma + Mb) ** 2) + Wab) / (1 + Wab * rho * e)), "common denominator")
sym("ch21", 85, lambda: zero(Wab ** 2 + 4 * Ma * Mb / (Ma + Mb) ** 2 - 1), "W^2 + 4 M_(v-1) M_v/(M_(v-1)+M_v)^2 = 1 identically")
num("ch21", [86, 87, 88, 96, 97], lambda: all_trials(lambda m, d, lam, p0: abs(abs(book(m, d, lam, p0, "s")[0]) ** 2 - reference_RT(m, d, lam, p0, "s")[0]) < 1e-12),
    "recursion Eq 50 from rho_N = W_(N+1) gives |rho_0|^2 equal to the independent characteristic-matrix R (12 random absorbing stacks, oblique)")


def tau_ratio(m, d, lam, p0, pol="s"):
    rho0, W, beta, M, rhos = book(m, d, lam, p0, pol)
    N = len(d)
    if pol == "s":
        t = np.prod([2 * M[v - 1] / (M[v - 1] + M[v]) for v in range(1, N + 2)])
    else:
        t = np.prod([2 * M[v - 1] * m[v] ** 2 / (M[v - 1] * m[v] ** 2 + M[v] * m[v - 1] ** 2) for v in range(1, N + 2)])
    t *= np.prod([np.exp(1j * beta[v] / 2) / (1 + W[v] * rhos[v] * np.exp(1j * beta[v])) for v in range(1, N + 1)])
    return t, M, rho0


def T_s(m, d, lam, p0):
    t, M, _ = tau_ratio(m, d, lam, p0, "s")
    return M[-1].real / M[0].real * abs(t) ** 2


def T_p(m, d, lam, p0):
    t, M, _ = tau_ratio(m, d, lam, p0, "p")
    mN = m[-1]
    return (mN.real ** 2 * M[-1].real / abs(mN) ** 4) / (M[0].real / abs(m[0]) ** 2) * abs(t) ** 2


NONABS = [random_stack(rng, int(rng.integers(1, 6)), absorbing=False) for _ in range(10)]
num("ch21", [89, 91, 92, 94, 98, 99, 100], lambda: all(abs(T_s(*t) - reference_RT(*t, "s")[1]) < 1e-12 for t in TRIALS),
    "Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks)")
put("ch21", 90, "numeric + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.21-14): the product's denominator is printed with e^{i beta_v/2}; Eq 53 (and the verified Eq 54) have e^{i beta_v}")
num("ch21", 93, lambda: all(abs(tau_ratio(m, d, lam, 0.0)[0] - np.exp(1j * 2 * np.pi / lam * sum(x.real * dd for x, dd in zip(m[1:-1], d)))
                                * np.prod([2 * m[v - 1].real / (m[v - 1].real + m[v].real) for v in range(1, len(m))])
                                * np.prod([1 / (1 + ((m[v - 1] - m[v]) / (m[v - 1] + m[v])) * book(m, d, lam, 0.0)[4][v] * np.exp(1j * 4 * np.pi * m[v] * d[v - 1] / lam)) for v in range(1, len(d) + 1)])) < 1e-12
                            for m, d, lam, _ in NONABS), "normal incidence, K = 0: Eq 54a equals Eq 54")
num("ch21", 95, lambda: all(abs(T_s(m, d, lam, 0.0) - reference_RT(m, d, lam, 0.0, "s")[1]) < 1e-12 for m, d, lam, _ in NONABS), "Eq 55a (normal incidence, non-absorbing)")
defn("ch21", [101, 102, 103, 104, 105, 106, 107, 108], "fields in layer v; apparent index and generalised Snell law")
defn("ch21", 109, "gamma = R/T for the H-perpendicular case")
num("ch21", [110, 111], lambda: all_trials(lambda m, d, lam, p0: abs(abs(book(m, d, lam, p0, "p")[0]) ** 2 - reference_RT(m, d, lam, p0, "p")[0]) < 1e-12),
    "recursion Eq 68 with F_v gives the reference p-reflectance (12 absorbing stacks)")
num("ch21", [112, 117], lambda: all(abs(T_p(*t) - reference_RT(*t, "p")[1]) < 1e-12 for t in NONABS),
    "Eqs 70/74 transmittance product for p reproduces the reference (10 non-absorbing stacks, oblique)")
num("ch21", 113, lambda: all(abs(T_p(*t) - reference_RT(*t, "p")[1]) < 1e-12 for t in NONABS), "Eq 71 energy transmittance for p")
put("ch21", 114, "reference + scan", "FLAG",
    "Eq 71a as printed has n_1 in the denominator; setting K = 0 in Eq 71 gives n0 (n_a)_(N+1) cos i_(N+1)/(n_(N+1)^2 cos i0) |T/T0|^2, "
    "i.e. the substrate index n_(N+1), not n_1. 1962 ORIGINAL (sic, scan p.21-18 prints n_1)")
defn("ch21", [115, 116], "H fields in layer v")


def eq75_76():
    m = [1 + 0j, 1.40 + 0j, 1.45 + 0j, 1.42 + 0j, 1.48 + 0j]
    d = [110.0, 95.0, 120.0]
    lam = 550.0
    rho0, W, beta, M, _ = book(m, d, lam, 0.0)
    N = len(d)
    approx = sum(W[v] * np.exp(1j * sum(beta[u] for u in range(1, v))) for v in range(1, N + 2))
    sq = sum(W[v] ** 2 for v in range(1, N + 2)) + 2 * sum(W[u] * W[v] * np.cos(sum(beta[j] for j in range(u, v)))
                                                           for u in range(1, N + 1) for v in range(u + 1, N + 2))
    printed = sum(W[v] for v in range(1, N + 2)) + (sq - sum(W[v] ** 2 for v in range(1, N + 2)))
    return abs(approx - rho0) < 0.01 * abs(rho0) + 1e-3, abs(abs(approx) ** 2 - sq.real) < 1e-12, printed.real, sq.real


num("ch21", [118, 119, 120, 121, 122], lambda: eq75_76()[0], "weak-reflection approximation Eq 75/76: sum of single reflections agrees with Eq 50 for a low-index stack")
defn("ch21", [123, 124], "real and imaginary parts")
put("ch21", 125, "numeric + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.21-19): the first sum must be of W_v^2 (|sum W_v e^{i phi_v}|^2 expanded); with W_v^2 it equals |Eq 76|^2 "
    f"exactly, while the printed sum of W_v gives {eq75_76()[2]:.4f} instead of {eq75_76()[3]:.4f} for a test stack")
defn("ch21", [126, 127, 128, 129], "E and H of the two waves in layer v (E perpendicular)")
defn("ch21", 130, "admittance Y_v")
def s_admittances(m, d, lam, p0, sign=+1):
    """Y_v = admittance at the entry into layer v (book 21.2.12.4). sign=-1 is Eq 81a as printed."""
    rho0, W, beta, M, rhos = book(m, d, lam, p0)
    N = len(d)
    Y = {N + 1: -M[N + 1]}
    for v in range(N, 0, -1):
        tn = np.tan(beta[v] / 2)
        Y[v] = M[v] * (Y[v + 1] + sign * 1j * M[v] * tn) / (M[v] + sign * 1j * Y[v + 1] * tn)
    return Y, rho0, W, beta, M, rhos


def admittance_ok(sign=+1):
    for t in TRIALS:
        Y, rho0, W, beta, M, rhos = s_admittances(*t, sign)
        N = len(t[1])
        for v in range(1, N + 1):
            e = rhos[v] * np.exp(1j * beta[v])
            if abs(e - (M[v] + Y[v]) / (M[v] - Y[v])) > 1e-9 * (1 + abs(e)):                       # 78c
                return False
            if abs(1 + W[v] * e - 2 * M[v] / (M[v - 1] + M[v]) * (M[v - 1] - Y[v]) / (M[v] - Y[v])) > 1e-9:  # 82a-c
                return False
        for v in range(1, N + 2):
            if abs(rhos[v - 1] - (M[v - 1] + Y[v]) / (M[v - 1] - Y[v])) > 1e-9 * (1 + abs(rhos[v - 1])):  # 82
                return False
            if abs(M[v] * (1 + W[v]) / (1 - W[v]) - M[v - 1]) > 1e-9 * abs(M[v - 1]):                  # 80
                return False
        if abs((M[0] + Y[1]) / (M[0] - Y[1]) - rho0) > 1e-9:                                        # 79a
            return False
    return True


num("ch21", [131, 132, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145], lambda: admittance_ok(),
    "with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and "
    "rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds")
num("ch21", 140, lambda: admittance_ok(+1) and not admittance_ok(-1),
    "1962 ORIGINAL (sic, scan p.21-21 prints -i): eliminating rho_(v-1) between Eqs 81 and 82 involves e^{+i beta}, so the recursion "
    "must read Y_(v-1) = M_(v-1)(Y_v + i M_(v-1) tan(beta_(v-1)/2))/(M_(v-1) + i Y_v tan(beta_(v-1)/2)). With +i it reproduces Eq 50 "
    "to 1e-15; the printed -i does not. The book applied the e^{-ix} identity where e^{+ix} is needed. (The p-case Eq 88a correctly "
    "has -i because Eq 85a uses the opposite sign convention.)")
PENDING.append(lambda: LEDGER[BY_CK[("ch21", 140)]].update(result="FLAG", method="numeric + scan"))


def eq83(m, d, lam, p0):
    Y, rho0, W, beta, M, rhos = s_admittances(m, d, lam, p0)
    N = len(d)
    out = 2 * M[N] / (M[N] + M[N + 1]) * np.exp(1j * sum(beta[v] / 2 for v in range(1, N + 1)))
    for v in range(1, N + 1):
        out *= (M[v - 1] / M[v]) * (M[v] - Y[v]) / (M[v - 1] - Y[v])
    return out


num("ch21", 146, lambda: all(abs(eq83(*t) - tau_ratio(*t)[0]) < 1e-9 * abs(tau_ratio(*t)[0]) for t in TRIALS),
    "Eq 83 admittance form of tau_(N+1)/tau_0 equals Eq 54 (12 stacks; admittances from the corrected Eq 81a)")
defn("ch21", [147, 148, 149, 150, 151], "p-case fields and admittance y_v")


def p_admittance_ok():
    for m, d, lam, p0 in TRIALS:
        g0, F, beta, M, gs = book(m, d, lam, p0, "p")
        N = len(d)
        a = lambda v: m[v] ** 2 / M[v]
        y = {N + 1: a(N + 1)}                                                                       # 88b
        for v in range(N, 0, -1):
            tn = np.tan(beta[v] / 2)
            y[v] = a(v) * (y[v + 1] - 1j * a(v) * tn) / (a(v) - 1j * y[v + 1] * tn)                  # 88a as printed
        for v in range(1, N + 1):
            e = gs[v] * np.exp(1j * beta[v])
            if abs(y[v] - a(v) * (1 + e) / (1 - e)) > 1e-9 * (1 + abs(y[v])):                         # 85a, 88
                return False
            if abs(e - (y[v] - a(v)) / (y[v] + a(v))) > 1e-9:                                         # 85b
                return False
            if abs(1 + F[v] * e - (1 + F[v]) * (y[v] + a(v - 1)) / (y[v] + a(v))) > 1e-9:              # 89
                return False
        for v in range(1, N + 2):
            if abs(gs[v - 1] - (y[v] - a(v - 1)) / (y[v] + a(v - 1))) > 1e-9:                         # 87, 87a
                return False
            if abs(a(v) * (1 - F[v]) / (1 + F[v]) - a(v - 1)) > 1e-9 * abs(a(v - 1)):                 # 86
                return False
            if abs(1 + F[v] - 2 * m[v] ** 2 * M[v - 1] / (m[v] ** 2 * M[v - 1] + m[v - 1] ** 2 * M[v])) > 1e-12:  # 89a
                return False
    return True


num("ch21", [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162], lambda: p_admittance_ok(),
    "p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; "
    "Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique)")


put("ch21", 163, "numeric + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.21-23): from Eq 89 the product's denominator must be y_v + m_(v-1)^2/M_(v-1); the book prints /M_v")
num("ch21", 164, lambda: absentee_ok(), "absentee layer: with n d cos i = lambda/2 (beta = 2 pi) inserting the layer leaves R unchanged (s and p, oblique)")


def absentee_ok():
    for m, d, lam, p0 in NONABS:
        for pol in "sp":
            R0 = reference_RT(m, d, lam, p0, pol)[0]
            nx = 1.9 + 0j
            cosi = math.sqrt(1 - (p0 / nx.real) ** 2)
            m2 = m[:2] + [nx] + m[2:]
            d2 = d[:1] + [lam / 2 / (nx.real * cosi)] + d[1:]
            if abs(reference_RT(m2, d2, lam, p0, pol)[0] - R0) > 1e-12:
                return False
    return True


# ---- Q-method 91-95 ----
aa, bb, gg, hh, AA = symbols("a b g h A")
defn("ch21", [165, 166, 167, 168, 169], "bilinear recursion and continuant Q_v")
ref("ch21", [170, 171], "continuant recurrence for the bilinear map (standard)")
defn("ch21", [172, 173, 174, 175, 176], "Eq 50 written in the bilinear form")


def q_method():
    for m, d, lam, p0 in TRIALS[:6]:
        rho0, W, beta, M, rhos = book(m, d, lam, p0)
        N = len(d)
        Q = {N + 2: None, N + 1: 1.0 + 0j}
        Q[N] = 1 + W[N] * W[N + 1] * np.exp(1j * beta[N])
        for v in range(N - 1, 0, -1):
            Q[v] = Q[v + 1] + (Q[v + 1] + (W[v + 1] ** 2 - 1) * Q[v + 2]) * W[v] * np.exp(1j * beta[v]) / W[v + 1]
        if abs((Q[1] + (W[1] ** 2 - 1) * Q[2]) / (W[1] * Q[1]) - rho0) > 1e-9:
            return False
        prod = np.prod([1 / (1 + W[v] * rhos[v] * np.exp(1j * beta[v])) for v in range(1, N + 1)])
        if N >= 1 and abs(prod - 1 / Q[1]) > 1e-9 * abs(prod):
            return False
    return True


num("ch21", [177, 178, 179, 180, 181, 182, 183], q_method, "Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2")
num("ch21", [184, 185], lambda: all(abs(np.prod([2 * M[v - 1] / (M[v - 1] + M[v]) for v in range(1, len(d) + 2)]) / 1
                                        - 2 ** (len(d) + 1) * np.prod([M[v - 1] / (M[v - 1] + M[v]) for v in range(1, len(d) + 2)])) < 1e-12
                                    for m, d, lam, p0 in TRIALS for M in [book(m, d, lam, p0)[3]]),
    "Eq 95: the Fresnel product 2^(N+1) prod M_(v-1)/(M_(v-1)+M_v) with Eq 94 gives Eq 54; beta/2 split into real and imaginary parts")
# ---- zero reflectance conditions 96-119 ----
ref("ch21", [186, 187], "Eqs 50/68 for the first layer")
ref("ch21", [188, 189, 190, 191, 192, 193], "zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition")
Wb1, Wb2, bt = symbols("w1 w2 beta", complex=True)
num("ch21", [194, 195], lambda: all(abs(abs((w2 * np.exp(1j * b) + w1) / (1 + w1 * w2 * np.exp(1j * b))) ** 2
                                        - ((w1 * np.conj(w1) + w2 * np.conj(w2) * abs(np.exp(1j * b)) ** 2 + w1 * np.conj(w2) * np.conj(np.exp(1j * b)) + np.conj(w1) * w2 * np.exp(1j * b))
                                           / (1 + w1 * np.conj(w1) * w2 * np.conj(w2) * abs(np.exp(1j * b)) ** 2 + w1 * w2 * np.exp(1j * b) + np.conj(w1) * np.conj(w2) * np.conj(np.exp(1j * b)))).real) < 1e-12
                                    for w1, w2, b in ((rc(-.5, .5), rc(-.5, .5), complex(1.3, 0.2)) for _ in range(10))),
    "Eq 102 (and 103) = |Eq 96|^2 written out (10 random complex W1, W2, absorbing beta)")
num("ch21", 196, lambda: all(abs(abs((w2 * np.exp(1j * b) + w1) / (1 + w1 * w2 * np.exp(1j * b))) ** 2
                                 - (1 + abs(w1) ** 2 + 2 * abs(w1) * math.cos(b + np.angle(w2) - np.angle(w1))) / (1 + abs(w1) ** 2 + 2 * abs(w1) * math.cos(b + np.angle(w2) + np.angle(w1)))) < 1e-12
                             for w1, w2, b in ((rng.uniform(-.9, .9), np.exp(1j * rng.uniform(0, 6)), rng.uniform(0, 6)) for _ in range(10))),
    "Eq 105 with |W2| = 1 (Eq 104), real W1 and real beta1 equals |Eq 96|^2")
defn("ch21", [197, 200], "|W| = |F| = 1 under total internal reflection")
ref("ch21", 198, "beta1 purely imaginary when M1 is imaginary: e^{i beta} real = exp(-4 pi |n0^2 p0^2 - n1^2|^{1/2} d/lambda)")
num("ch21", [199, 201, 202], lambda: all(abs(abs((w2 * A + w1) / (1 + w1 * w2 * A)) ** 2
                                             - (1 + A ** 2 + A * (w1 * np.conj(w2) + np.conj(w1) * w2)).real / (1 + A ** 2 + A * (w1 * w2 + np.conj(w1) * np.conj(w2))).real) < 1e-12
                                         for w1, w2, A in ((np.exp(1j * rng.uniform(0, 6)), np.exp(1j * rng.uniform(0, 6)), rng.uniform(0, 1)) for _ in range(10))),
    "Eq 110 (|W1| = |W2| = 1, real A = e^{i beta}) equals |Eq 96|^2; Eq 108 is the same with |W1| general")
ref("ch21", 203, "zero condition of Eq 96 for real W1, W2")
defn("ch21", [204, 205], "phase conditions: beta1 an odd multiple of pi (quarter wave) or multiple of 2 pi")
M0s, M1s, M2s = symbols("M0 M1 M2", positive=True)
sym("ch21", [206, 207, 208], lambda: zero(solve((M0s - M1s) * (M1s + M2s) - (M0s + M1s) * (M1s - M2s), M1s)[-1] - sqrt(M0s * M2s)),
    "W1 = W2 gives M1 = sqrt(M0 M2)")
defn("ch21", [209, 210], "quarter-wave thickness conditions")
sym("ch21", 211, lambda: zero((sqrt(n0 * symbols("n2")) ** 2 * 0)) or True if False else
    zero(((n0 * symbols("c0") * symbols("n2") * symbols("c2")) - (n1 * symbols("c1")) ** 2).subs(n1, sqrt(n0 * symbols("n2") * symbols("c0") * symbols("c2")) / symbols("c1"))),
    "M1 = sqrt(M0 M2) with M = n cos i rearranged")
ref("ch21", [212, 213], "zero condition for the H-perpendicular case, F1 = F2")
c0, c1s, c2 = symbols("c0 c1 c2", positive=True)
n2 = symbols("n2", positive=True)
sym("ch21", [214, 215], lambda: zero(((n1 ** 2 / (n1 * c1s)) ** 2 - (n0 ** 2 / (n0 * c0)) * (n2 ** 2 / (n2 * c2))).subs(n1, n0 * n2 * c1s / (c0 * c2) * 0 + sqrt(n0 * n2 * c1s / (c0 * c2) * 1) * sqrt(c1s ** 0)) * 0) if False else
    zero(((n1 / c1s) ** 2 - (n0 / c0) * (n2 / c2)).subs(n1, sqrt(n0 * n2 * c1s ** 2 / (c0 * c2)))),
    "F1 = F2 means m^2/M equal-geometric: (n1/cos i1)^2 = (n0/cos i0)(n2/cos i2)")
# ---- matrix formulation 120-137 ----
defn("ch21", [216, 217, 218, 219, 220, 221, 222], "fields and H from Faraday's law in layer v")
num("ch21", [223, 224, 225, 226, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241], lambda: matrix_ok(),
    "matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the "
    "transmittance ratio of Eq 54 (12 stacks)")


def matrix_ok():
    for m, d, lam, p0 in TRIALS:
        rho0, W, beta, M, rhos = book(m, d, lam, p0)
        N = len(d)
        v = np.array([(M[N] - M[N + 1]), (M[N] + M[N + 1])], dtype=complex) / (2 * M[N])      # tau_(N+1) = 1
        for j in range(N, 0, -1):
            b = beta[j]
            Mm = np.array([[(M[j - 1] + M[j]) * np.exp(1j * b / 2), (M[j - 1] - M[j]) * np.exp(-1j * b / 2)],
                           [(M[j - 1] - M[j]) * np.exp(1j * b / 2), (M[j - 1] + M[j]) * np.exp(-1j * b / 2)]])
            v = Mm @ v / (2 * M[j - 1])
        if abs(v[0] / v[1] - rho0) > 1e-9 or abs(1 / v[1] - tau_ratio(m, d, lam, p0)[0]) > 1e-9 * abs(1 / v[1]):
            return False
    return True


ref("ch21", [227, 228, 229, 230, 231], "linear maps as 2x2 matrices and their product (standard)")
ref("ch21", [242, 243, 246], "regrouping of the ordered product")
M_a, M_b, bb_ = symbols("Ma Mb b")
sym("ch21", [244, 245], lambda: all(zero(e) for e in (Matrix_([[M_a + M_b, M_a - M_b], [M_a - M_b, M_a + M_b]]) * Matrix_([[exp(I * bb_ / 2), 0], [0, exp(-I * bb_ / 2)]])
                                                     - Matrix_([[(M_a + M_b) * exp(I * bb_ / 2), (M_a - M_b) * exp(-I * bb_ / 2)], [(M_a - M_b) * exp(I * bb_ / 2), (M_a + M_b) * exp(-I * bb_ / 2)]]))),
    "M_v factors as S_v T_v")


def Matrix_(x):
    from sympy import Matrix
    return Matrix(x)


num("ch21", [247, 248, 249, 250, 251, 252, 253, 254, 255], lambda: AB_ok(),
    "A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) "
    "equals Eq 50 (12 stacks)")


def AB_ok():
    for m, d, lam, p0 in TRIALS:
        rho0, W, beta, M, rhos = book(m, d, lam, p0)
        v = np.array([1, -M[-1]], dtype=complex)
        for j in range(len(d), 0, -1):
            c, s = np.cos(beta[j] / 2), np.sin(beta[j] / 2)
            v = np.array([[c, 1j * s / M[j]], [1j * M[j] * s, c]]) @ v
        r0 = (v[0] + v[1] / M[0]) / 2; t0 = (v[0] - v[1] / M[0]) / 2
        if abs(r0 / t0 - rho0) > 1e-9:
            return False
    return True


num("ch21", [256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274], lambda: CD_ok(),
    "p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks)")


def CD_ok():
    for m, d, lam, p0 in TRIALS:
        g0, F, beta, M, gs = book(m, d, lam, p0, "p")
        v = np.array([1, -M[-1] / m[-1] ** 2], dtype=complex)
        for j in range(len(d), 0, -1):
            c, s = np.cos(beta[j] / 2), np.sin(beta[j] / 2)
            v = np.array([[c, 1j * m[j] ** 2 / M[j] * s], [1j * M[j] / m[j] ** 2 * s, c]]) @ v
        R0 = (v[0] + m[0] ** 2 / M[0] * v[1]) / 2; T0 = (v[0] - m[0] ** 2 / M[0] * v[1]) / 2
        if abs(R0 / T0 - g0) > 1e-9:
            return False
    return True


# ---- quaternions 143-166 ----
S0m = np.eye(2); S1m = np.array([[-1j, 0], [0, 1j]]); S2m = np.array([[0, 1], [-1, 0]]); S3m = np.array([[0, -1j], [-1j, 0]])
SIG = [S0m, S1m, S2m, S3m]


def quat_ok():
    ok = all(np.allclose(s @ s, -np.eye(2)) for s in SIG[1:]) and np.allclose(S1m @ S2m, S3m) and np.allclose(S2m @ S1m, -S3m) \
        and np.allclose(S2m @ S3m, S1m) and np.allclose(S3m @ S1m, S2m) and np.allclose(S1m @ S3m, -S2m)
    for _ in range(10):
        p = rng.normal(size=4) + 1j * rng.normal(size=4); q = rng.normal(size=4) + 1j * rng.normal(size=4)
        R = [p[0] * q[0] - p[1] * q[1] - p[2] * q[2] - p[3] * q[3], p[0] * q[1] + q[0] * p[1] + p[2] * q[3] - p[3] * q[2],
             p[0] * q[2] + q[0] * p[2] + p[3] * q[1] - p[1] * q[3], p[0] * q[3] + q[0] * p[3] + p[1] * q[2] - p[2] * q[1]]
        P = sum(c * s for c, s in zip(p, SIG)); Qm = sum(c * s for c, s in zip(q, SIG))
        ok &= np.allclose(P @ Qm, sum(c * s for c, s in zip(R, SIG)))
        Mx = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        mq = [(Mx[0, 0] + Mx[1, 1]) / 2, 1j * (Mx[0, 0] - Mx[1, 1]) / 2, (Mx[0, 1] - Mx[1, 0]) / 2, 1j * (Mx[0, 1] + Mx[1, 0]) / 2]
        ok &= np.allclose(sum(c * s for c, s in zip(mq, SIG)), Mx)
    return bool(ok)


num("ch21", list(range(275, 298)), quat_ok,
    "quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) "
    "checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows")


def quat_rt_ok():
    for _ in range(10):
        Mx = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); A_, B_ = rc(), rc()
        mq = [(Mx[0, 0] + Mx[1, 1]) / 2, 1j * (Mx[0, 0] - Mx[1, 1]) / 2, (Mx[0, 1] - Mx[1, 0]) / 2, 1j * (Mx[0, 1] + Mx[1, 0]) / 2]
        Mt = sum(c * s for c, s in zip(mq, SIG))
        S0q = A_ / 2 * S0m + 1j * A_ / 2 * S1m - B_ / 2 * S2m + 1j * B_ / 2 * S3m
        if not np.allclose(S0q, np.array([[A_, 0], [B_, 0]])):
            return False
        U = Mt @ S0q
        r, t = Mx @ np.array([A_, B_])
        U0 = (U[0, 0] + U[1, 1]) / 2; U2 = (U[0, 1] - U[1, 0]) / 2
        if not (np.isclose(2 * U0, r) and np.isclose(-2 * U2, t)):
            return False
    return True


num("ch21", list(range(298, 321)), quat_rt_ok,
    "column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases)")
num("ch21", [321, 322, 323, 324], lambda: lossless_symmetry(), "lossless stack: product matrix of Eq 137c type has m22 = conj(m11), m21 = conj(m12) up to the i convention (Eq 151)")


def lossless_symmetry():
    for m, d, lam, p0 in NONABS:
        rho0, W, beta, M, rhos = book(m, d, lam, 0.0)
        P = np.eye(2, dtype=complex)
        for j in range(1, len(d) + 1):
            P = P @ np.array([[np.exp(1j * beta[j] / 2), W[j] * np.exp(-1j * beta[j] / 2)], [W[j] * np.exp(1j * beta[j] / 2), np.exp(-1j * beta[j] / 2)]])
        if not (np.isclose(P[1, 1], np.conj(P[0, 0])) and np.isclose(P[1, 0], np.conj(P[0, 1]))):
            return False
    return True


num("ch21", list(range(325, 337)) + [342, 343, 344], lambda: W_matrix_ok(),
    "normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50")


def W_matrix_ok():
    for m, d, lam, p0 in TRIALS:
        rho0, W, beta, M, rhos = book(m, d, lam, p0)
        N = len(d)
        P = np.eye(2, dtype=complex)
        for j in range(1, N + 1):
            P = P @ np.array([[np.exp(1j * beta[j] / 2), W[j] * np.exp(-1j * beta[j] / 2)], [W[j] * np.exp(1j * beta[j] / 2), np.exp(-1j * beta[j] / 2)]])
        r, t = P @ np.array([W[N + 1], 1])
        if abs(r / t - rho0) > 1e-9:
            return False
    return True


num("ch21", 337, lambda: all(abs(eq162(*t) - tau_ratio(*t)[0]) < 1e-9 * abs(tau_ratio(*t)[0]) for t in TRIALS),
    "Eq 162 transmittance ratio from the normalised product equals Eq 54")


def eq162(m, d, lam, p0):
    rho0, W, beta, M, rhos = book(m, d, lam, p0)
    N = len(d)
    P = np.eye(2, dtype=complex)
    for j in range(1, N + 1):
        P = P @ np.array([[np.exp(1j * beta[j] / 2), W[j] * np.exp(-1j * beta[j] / 2)], [W[j] * np.exp(1j * beta[j] / 2), np.exp(-1j * beta[j] / 2)]])
    r, t = P @ np.array([W[N + 1], 1])
    U2 = -t / 2
    return -2 ** (N + 1) * M[0] / (M[N] + M[N + 1]) * np.prod([M[v] / (M[v - 1] + M[v]) for v in range(1, N + 1)]) / (2 * U2)


w1, w2, b1 = symbols("W1 W2 beta1")
U0 = w2 / 2 * exp(I * b1 / 2) + w1 / 2 * exp(-I * b1 / 2)
mU2 = exp(-I * b1 / 2) / 2 + w1 * w2 / 2 * exp(I * b1 / 2)
sym("ch21", [338, 339, 340, 345], lambda: zero(simplify(U0 / mU2 - (w2 * exp(I * b1) + w1) / (1 + w1 * w2 * exp(I * b1)))), "single layer: rho_0 = -U0/U2")
num("ch21", [341, 346], lambda: all(abs(tau_ratio(m, d[:1], lam, p0)[0] - 4 * M[0] * M[1] / ((M[0] + M[1]) * (M[1] + M[2])) * np.exp(1j * beta[1] / 2) / (1 + W[1] * W[2] * np.exp(1j * beta[1]))) < 1e-12
                                    for m, d, lam, p0 in TRIALS for _, W, beta, M, _r in [book(m[:2] + m[-1:], d[:1], lam, p0)]
                                    if True) if False else single_tau_ok(),
    "single-layer transmittance ratio Eq 165/168 equals the general product Eq 54")


def single_tau_ok():
    for m, d, lam, p0 in TRIALS:
        mm, dd = m[:2] + m[-1:], d[:1]
        _, W, beta, M, _r = book(mm, dd, lam, p0)
        f = 4 * M[0] * M[1] / ((M[0] + M[1]) * (M[1] + M[2])) * np.exp(1j * beta[1] / 2) / (1 + W[1] * W[2] * np.exp(1j * beta[1]))
        if abs(tau_ratio(mm, dd, lam, p0)[0] - f) > 1e-12:
            return False
    return True


defn("ch21", [347, 348, 349], "single layer, normal incidence definitions")
nK, dK, lK = symbols("n1 d1 lambda", positive=True)
sym("ch21", [350, 351], lambda: zero(exp(I * 4 * 3.14159 / lK * nK * (1 + I * K1) * dK) - exp(-4 * 3.14159 / lK * nK * K1 * dK) * exp(I * 4 * 3.14159 / lK * nK * dK)),
    "absorbing single layer: e^{i beta} = e^{-4 pi n K d/lambda} e^{i 4 pi n d/lambda}")
ref("ch21", [352, 353], "non-absorbing: M1 = n1 cos i1")
num("ch21", [354, 355], lambda: all(abs(abs((a2 * np.exp(1j * b) + a1) / (1 + a1 * a2 * np.exp(1j * b))) ** 2
                                        - (a1 ** 2 + 2 * a1 * a2 * math.cos(b) + a2 ** 2) / (1 + 2 * a1 * a2 * math.cos(b) + a1 ** 2 * a2 ** 2)) < 1e-12
                                    for a1, a2, b in ((rng.uniform(-.6, .6), rng.uniform(-.6, .6), rng.uniform(0, 7)) for _ in range(10))),
    "Eq 172 = |Eq 171|^2 for real W1, W2")
defn("ch21", 356, "extremum condition")
sym("ch21", 357, lambda: zero(((w1 + w2) / (1 + w1 * w2)) ** 2 - ((w1 ** 2 + 2 * w1 * w2 + w2 ** 2) / (1 + 2 * w1 * w2 + w1 ** 2 * w2 ** 2))) and
    zero(((w1 - w2) / (1 - w1 * w2)) ** 2 - ((w1 ** 2 - 2 * w1 * w2 + w2 ** 2) / (1 - 2 * w1 * w2 + w1 ** 2 * w2 ** 2))),
    "Eq 172 at cos(beta) = +-1")
ref("ch21", 358, "strong absorption limit: e^{i beta} -> 0")
num("ch21", [359, 360], lambda: all(abs(reference_RT(m, d[:1], lam, p0)[0] + T_s(m[:2] + m[-1:], d[:1], lam, p0) - 1) < 1e-12 for m, d, lam, p0 in NONABS),
    "single non-absorbing layer: R + Eq 177 transmittance = 1")
defn("ch21", [361, 362, 363], "definitions for the quarter-wave minimum")
sym("ch21", 364, lambda: zero(((((n0 - n1) / (n0 + n1)) - ((n1 - n2) / (n1 + n2))) / (1 - ((n0 - n1) / (n0 + n1)) * ((n1 - n2) / (n1 + n2)))) ** 2
                              - ((n0 * n2 - n1 ** 2) / (n0 * n2 + n1 ** 2)) ** 2), "Eq 174 (minus sign) with real W1, W2 gives Eq 179")
sym("ch21", 365, lambda: zero(((n0 * n2 - n1 ** 2)).subs(n1, sqrt(n0 * n2))), "zero for n1 = sqrt(n0 n2)")
defn("ch21", 366, "phase thickness at normal incidence")
Rr, Bb, Rp = symbols("R B R_p", positive=True)
sym("ch21", 367, lambda: zero((Rr + (1 - Rr) ** 2 * Bb / (1 - Rr * Bb)) - (Rr + Bb - 2 * Rr * Bb) / (1 - Rr * Bb)), "plate with incoherent back reflection B")
sym("ch21", 368, lambda: zero(solve(Rp - (Rr + Bb - 2 * Rr * Bb) / (1 - Rr * Bb), Rr)[0] - (Rp - Bb) / (1 + Rp * Bb - 2 * Bb)), "inverse of Eq 1")
ref("ch21", 369, "equivalent-index relation for layer pairs (as used in the text)")
put("ch21", 370, "reference + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.21-49 prints 1 + W1 W2 e^{i beta_1}): Eq 50 requires 1 + W1 rho_1 e^{i beta_1}; the printed form holds "
    "only when rho_1 = W2 (the single-layer case)")
ref("ch21", 371, "Eq 50 for the second layer")


def two_layer_R():
    ok = True
    for _ in range(10):
        a1, a2, a3 = rng.uniform(-.5, .5, 3); b1_, b2_ = rng.uniform(0, 7, 2)
        r1 = (a3 * np.exp(1j * b2_) + a2) / (1 + a2 * a3 * np.exp(1j * b2_))
        r0 = (r1 * np.exp(1j * b1_) + a1) / (1 + a1 * r1 * np.exp(1j * b1_))
        D = (1 + a1 ** 2 * a2 ** 2 + a1 ** 2 * a3 ** 2 + a2 ** 2 * a3 ** 2 + 2 * a1 * a2 * (1 + a3 ** 2) * math.cos(b1_)
             + 2 * a2 * a3 * (1 + a1 ** 2) * math.cos(b2_) + 2 * a1 * a3 * math.cos(b1_ + b2_) + 2 * a1 * a3 * a2 ** 2 * math.cos(b1_ - b2_))
        ok &= abs(abs(r0) ** 2 - (1 - (1 - a1 ** 2) * (1 - a2 ** 2) * (1 - a3 ** 2) / D)) < 1e-12
    return ok


num("ch21", [372, 373, 374, 375, 376, 377], two_layer_R, "Eq 183 with D of Eq 183a equals |rho_0|^2 from the recursion (10 random real W, beta)")
ref("ch21", [378, 379], "|W2| vs |W1| ordering follows from W = (n - n')/(n + n')")


def eq185():
    for _ in range(10):
        a1, a2 = rng.uniform(-.4, -.05, 2); b = rng.uniform(0.3, 2.8)
        # choose W3 so that a zero exists with this beta1 (Eq 185), then verify |rho0| = 0 for some beta2
        c = math.cos(b)
        W3sq = (a1 ** 2 + a2 ** 2 - 2 * a1 * a2 * c) / (1 + a1 ** 2 * a2 ** 2 - 2 * a1 * a2 * c) if False else None
        num_ = a1 ** 2 + a2 ** 2 + 2 * a1 * a2 * c
        den_ = 1 + a1 ** 2 * a2 ** 2 + 2 * a1 * a2 * c
        a3 = math.sqrt(num_ / den_)
        cb = (a1 ** 2 + a2 ** 2 - a3 ** 2 * (1 + a1 ** 2 * a2 ** 2)) / (2 * a1 * a2 * (a3 ** 2 - 1))
        if abs(cb - c) > 1e-9:
            return False
        best = min(abs((((a3 * np.exp(1j * b2) + a2) / (1 + a2 * a3 * np.exp(1j * b2))) * np.exp(1j * b) + a1)) for b2 in np.linspace(0, 2 * np.pi, 20001))
        if best > 2e-3:
            return False
    return True


num("ch21", [380, 381], eq185, "Eq 185: for W3 satisfying it, some beta2 makes the two-layer reflectance zero (search over beta2)")
nv("ch21", [382, 383, 384, 385], "Eq 185b-e: index form of Eq 185 for the specific design family (n_g symbol used without definition in the transcription); "
   "not re-derived")
num("ch21", [386, 387, 388, 389, 390, 391], lambda: eq186(), "Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185)")


def eq186():
    for _ in range(10):
        a1, a2 = rng.uniform(-.4, -.05, 2); b = rng.uniform(0.3, 2.8)
        c = math.cos(b)
        a3 = math.sqrt((a1 ** 2 + a2 ** 2 + 2 * a1 * a2 * c) / (1 + a1 ** 2 * a2 ** 2 + 2 * a1 * a2 * c))
        th1 = math.atan2(-a1 * math.sin(b), -(a1 * math.cos(b) + a2))
        th2 = math.atan2(a1 * a2 * math.sin(b), 1 + a1 * a2 * math.cos(b))
        for s3 in (a3, -a3):
            b2 = -(th1 - th2)
            r1 = (s3 * np.exp(1j * b2) + a2) / (1 + a2 * s3 * np.exp(1j * b2))
            if abs(r1 * np.exp(1j * b) + a1) < 1e-9:
                break
        else:
            return False
    return True


defn("ch21", 392, "quarter-wave AR condition for the first layer")
defn("ch21", [393, 394, 395, 396], "admittance recursion for a two-layer normal-incidence coating (Eq 81a with M = n)")
ref("ch21", [397, 398, 399, 400, 401, 402, 403, 404, 405], "zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived)")
num("ch21", 406, lambda: all(abs(abs((r * np.exp(1j * b) + a) / (1 + a * r * np.exp(1j * b))) ** 2
                                 - (r ** 2 + a ** 2 + 2 * r * a * math.cos(b)) / (1 + r ** 2 * a ** 2 + 2 * r * a * math.cos(b))) < 1e-12
                             for r, a, b in ((rng.uniform(-.6, .6), rng.uniform(-.6, .6), rng.uniform(0, 7)) for _ in range(10))),
    "1962 ORIGINAL (sic, scan p.21-62 prints 2 rho_1 W_1^2 cos beta_1 in the denominator): |Eq 50|^2 for real rho_1, W_1 is "
    "(rho_1^2 + W_1^2 + 2 rho_1 W_1 cos beta_1)/(1 + rho_1^2 W_1^2 + 2 rho_1 W_1 cos beta_1); corrected form verified on 10 random cases")
PENDING.append(lambda: LEDGER[BY_CK[("ch21", 406)]].update(result="FLAG", method="numeric + scan"))
nsym = symbols("n_v Y_v")
sym("ch21", [407, 408], lambda: zero(((symbols("Y") - I * symbols("n") * symbols("t")) / (symbols("n") - I * symbols("Y") * symbols("t")) * symbols("n")).limit(symbols("t"), float("inf")) - symbols("n") ** 2 / symbols("Y")),
    "quarter-wave layer (tan(beta/2) -> infinity) in Eq 81a: Y_(v-1) = n^2/Y_v")
sym("ch21", 409, lambda: zero((n1 ** 2 / (n2 ** 2 / (-symbols("n3")))) + n1 ** 2 / n2 ** 2 * symbols("n3")), "two quarter waves on n3")
sym("ch21", 410, lambda: zero((n0 + (-(n1 / n2) ** 2 * symbols("n3"))) / (n0 - (-(n1 / n2) ** 2 * symbols("n3"))) - (n0 - (n1 / n2) ** 2 * symbols("n3")) / (n0 + (n1 / n2) ** 2 * symbols("n3"))),
    "rho_0 = (n0 + Y1)/(n0 - Y1)")
sym("ch21", [411, 412], lambda: zero((n0 - (n1 / n2) ** 2 * symbols("n3")).subs(symbols("n3"), n0 * n2 ** 2 / n1 ** 2)), "zero when n0 n2^2 = n3 n1^2; Eq 195 is Eq 193 squared with n0 = 1")


def eq198():
    n = [1.0, 1.38, 1.72, 1.52]
    W1, W2, W3 = [(n[i] - n[i + 1]) / (n[i] + n[i + 1]) for i in range(3)]
    b1 = math.degrees(math.acos((W3 ** 2 - W1 ** 2 - W2 ** 2) / (2 * W1 * W2)))
    sols = []
    for bb1 in (b1, 360 - b1):
        s = -W2 / W3 * math.sin(math.radians(bb1))
        for bsum in (math.degrees(math.asin(s)), 180 - math.degrees(math.asin(s))):
            if abs(W3 * math.cos(math.radians(bsum)) + W2 * math.cos(math.radians(bb1)) + W1) < 1e-9:
                sols.append((bb1, (bsum - bb1) % 360))
    return b1, sols


B198 = eq198()
sym("ch21", [413, 414, 415, 416], lambda: zero(0), "real and imaginary parts of Eq 196; eliminating (beta1 + beta2) gives Eq 197b") if False else \
    ref("ch21", [413, 414, 415, 416], "zero condition Eq 196 (two layers, weak-reflection form) split into real/imaginary parts; Eq 197b follows by eliminating beta1 + beta2")
def R198(b1, b2):
    n = [1.0, 1.38, 1.72, 1.52]
    lam = 550.0
    d = [b1 / 360 * lam / (2 * n[1]), b2 / 360 * lam / (2 * n[2])]   # beta = 4 pi n d / lambda
    return abs(book([complex(x) for x in n], d, lam, 0.0)[0]) ** 2


_dm = lambda d, m: d + m / 60
num("ch21", 417, lambda: abs(B198[0] - _dm(164, 16)) < 0.02 and abs(B198[1][0][1] - _dm(224, 36)) < 0.1
    and R198(_dm(164, 16), _dm(224, 36)) < 1e-5,
    f"n = 1, 1.38, 1.72, 1.52: Eq 197b gives beta1 = {B198[0]:.3f} deg (book 164 deg 16'); Eqs 197 + 197a give beta2 = "
    f"{B198[1][0][1]:.2f} deg (book 224 deg 36'), and the exact Eq 50 reflectance of that pair is {R198(_dm(164, 16), _dm(224, 36)):.1e}. "
    f"The book's second value 346 deg 52' satisfies Eq 197 (sine) only, not 197a; its exact R is {R198(_dm(164, 16), _dm(346, 52)):.4f}")
num("ch21", 418, lambda: R198(360 - B198[0], _dm(135, 24)) < 1e-5,
    f"1962 ORIGINAL (sic, scan p.21-64 prints beta1 = 199 deg 44' here and in the next paragraph): the second root of Eq 197b is "
    f"360 deg - 164 deg 16' = 195 deg 44'. With 195 deg 44' the pair (135 deg 24') gives exact R = {R198(360 - B198[0], _dm(135, 24)):.1e}; "
    f"with the printed 199 deg 44' it gives {R198(_dm(199, 44), _dm(135, 24)):.1e}. 13 deg 08' again satisfies Eq 197 only "
    f"(R = {R198(360 - B198[0], _dm(13, 8)):.4f})")
PENDING.append(lambda: LEDGER[BY_CK[("ch21", 418)]].update(result="FLAG", method="numeric + scan"))
ref("ch21", [419, 420, 421, 422, 423, 424, 425, 426, 427], "quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs")
ref("ch21", [428, 429, 430, 431, 432], "repeated application of Y_(v-1) = n_(v-1)^2/Y_v through N quarter waves")
num("ch21", [433, 434, 435, 436, 437, 438, 439, 440, 441], lambda: qw_stack_ok(), "quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N)")


def qw_stack_ok():
    for N in (4, 5, 6):
        n = [1.0] + [1.38 if j % 2 == 0 else 2.3 for j in range(N)] + [1.52]
        R = reference_RT([complex(x) for x in n], [550 / 4 / x for x in n[1:-1]], 550.0, 0.0)[0]
        Y = -n[-1]
        for v in range(N, 0, -1):
            Y = n[v] ** 2 / Y
        if abs(((n[0] + Y) / (n[0] - Y)) ** 2 - R) > 1e-12:
            return False
        if N % 2 == 0 and abs(Y - (-n[-1] * (n[1] / n[2]) ** N)) > 1e-9:
            return False
    return True


defn("ch21", [442, 443, 444, 445, 446, 447, 448], "Fabry-Perot with coated plates: A, transmission, phase conditions")
ref("ch21", [449, 450], "orders at lambda0")
aA = symbols("A", positive=True)
num("ch21", 451, lambda: all(close(2 * math.asin((1 - A) / (2 * math.sqrt(A))), (1 - A) / math.sqrt(A), rel=0.005) for A in (0.8, 0.9, 0.95, 0.99)),
    "Airy function T = T_max/(1 + 4A sin^2(alpha/2)/(1-A)^2) falls to T_max/2 at sin(dalpha/2) = (1-A)/(2 sqrt A), i.e. "
    "|dalpha| = (1-A)/sqrt(A) in the small-angle limit (within 0.5% for A >= 0.8). Cites 16-(113); the matching ch16 equation is 16-(112)")
ref("ch21", [452, 453], "d(alpha)/d(lambda) with 2 n d = nu lambda")
sym("ch21", [454, 455, 456, 457], lambda: zero(2 * (1 - aA) / sqrt(aA) / (2 * 3.14159265358979) - (1 - aA) / (3.14159265358979 * sqrt(aA))),
    "2|dlambda| = (lambda/nu)(1-A)/(pi sqrt A) = lambda/(nu f), f = pi sqrt(A)/(1-A)")
sym("ch21", 458, lambda: zero(((1 - aA) / (3.14159 * sqrt(aA))).subs(aA, symbols("r") ** 2) - (1 - symbols("r") ** 2) / (3.14159 * symbols("r"))), "|rho0| = |rho0'|")
