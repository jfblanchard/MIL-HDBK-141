from ledger import *
from sympy import symbols, sin, cos, sqrt, pi, asin, integrate, Rational, simplify, trigsimp, expand

# ---------------- ch02 Fundamentals of geometrical optics ----------------
n0, n1, I, Ip = symbols("n_0 n_1 I I'", positive=True)
ref("ch02", 1, "Snell's law, standard form")
defn("ch02", 2, "cross product of unit vectors = sin of included angle")
sym("ch02", 3, lambda: zero(sin(I) / sin(asin(n0 * sin(I) / n1)) - n1 / n0),
    "ratio follows from Eq 1")
ref("ch02", 4, "Eq 2: vector Snell's law n(Q x M) conserved; equivalent to Eq 1 for unit vectors")
ref("ch02", [5, 6], "Eq 2 rewritten with S = nQ; difference vector crosses to zero with the normal")
defn("ch02", 7, "Eq 3: S1 - S0 parallel to the normal M1, factor Gamma")
sym("ch02", 8, lambda: zero((n1 * sqrt(1 - (n0 / n1) ** 2 * sin(I) ** 2) - n0 * cos(I))
                            - (-n0 * cos(I) + n1 * sqrt((n0 / n1 * cos(I)) ** 2 - (n0 / n1) ** 2 + 1))),
    "Eq 4: n1 cos I' rewritten via Snell; both forms of Gamma agree")
sym("ch02", 9, lambda: zero(n0 * sin(I) - (-n0) * sin(-I)),
    "Eq 5: with n1 = -n0 Snell gives I' = -I (reflection as refraction)")
defn("ch02", 10, "Eq 6: reflection convention n1 = -n0")
sym("ch02", 11, lambda: zero(n0 * sin(asin(n1 / n0)) - n1 * sin(pi / 2)),
    "Eq 7: critical angle is Snell with I' = 90 deg")
defn("ch02", 12, "Eq 8: absolute index = c / v")
v, va, vo = symbols("v_vac v_air v_o", positive=True)
sym("ch02", 13, lambda: zero((v / vo) / (v / va) - va / vo), "relative index algebra")
defn("ch02", 14, "Abbe number definition (standard)")

# ---------------- ch03 Physical optics ----------------
c, nu, T, n, lam0, a, a1, a2, w, t, d, phi, x, th, k = symbols("c nu T n lambda_0 a a_1 a_2 omega t delta phi x theta k", positive=True)
defn("ch03", 1, "index = c / phase velocity")
ref("ch03", 2, "v = nu*lambda = c/n, standard")
sym("ch03", 3, lambda: zero(c / (n * nu) - c * (1 / nu) / n) and zero(c * T / n - (c * T) / n),
    "lambda = c/(n nu) = cT/n = lambda_0/n with T = 1/nu, lambda_0 = cT")
defn("ch03", [4, 5, 6, 7], "plane-wave forms and phase definition")
sym("ch03", 8, lambda: zero((2 * pi / T) / ((2 * pi / lam0) * n) - lam0 / (n * T)) and zero((lam0 / (n * T)).subs(lam0, c * T) - c / n),
    "omega/(kn) = lambda/(nT) = c/n holds with k = 2 pi/lambda (vacuum lambda, as the chapter's symbol table defines); "
    "note Eq 3 uses the same letter for the in-medium wavelength")
defn("ch03", [9, 11, 12], "plane wave in direction cosines p,q,r")
defn("ch03", 10, "direction cosines sum of squares = 1")
defn("ch03", 13, "instantaneous irradiance ~ E^2")
Phi = symbols("Phi")
sym("ch03", 14, lambda: zero(integrate(a ** 2 * cos(Phi - w * t) ** 2, (t, 0, 2 * pi / w)) / (2 * pi / w)
                             - a ** 2 / (2 * (2 * pi / w)) * integrate(1 + cos(2 * (Phi - w * t)), (t, 0, 2 * pi / w))),
    "cos^2 = (1+cos2x)/2 over one period")
sym("ch03", 15, lambda: zero(integrate(cos(2 * (Phi - w * t)), (t, 0, 2 * pi / w))), "integral over a period vanishes")
sym("ch03", 16, lambda: zero(integrate(a ** 2 * cos(Phi - w * t) ** 2, (t, 0, 2 * pi / w)) / (2 * pi / w) - a ** 2 / 2),
    "time average of a^2 cos^2 = a^2/2")
defn("ch03", [17, 18, 19, 20], "two-wave superposition set-up")
P1, P2 = symbols("Phi_1 Phi_2")
Tp = 2 * pi / w
sym("ch03", [21, 22], lambda: zero(integrate(a1 ** 2 * cos(P1 - w * t) ** 2 + a2 ** 2 * cos(P2 - w * t) ** 2, (t, 0, Tp)) / Tp
                                   - a1 ** 2 / 2 - a2 ** 2 / 2),
    "expansion of time average of (E1+E2)^2; cross term = 2 a1 a2 I")
sym("ch03", 23, lambda: zero(a1 ** 2 / 2 + a2 ** 2 / 2 + 2 * a1 * a2 * cos(P1 - P2) / 2
                             - integrate((a1 * cos(P1 - w * t) + a2 * cos(P2 - w * t)) ** 2, (t, 0, Tp)) / Tp),
    "Eq 20 with I from Eq 23: full time average reproduced")
defn("ch03", 24, "Eq 21 definition of I")
sym("ch03", 25, lambda: zero(cos(P1 - w * t) * cos(P2 - w * t) - (cos(P1 + P2 - 2 * w * t) + cos(P1 - P2)) / 2),
    "product-to-sum identity")
sym("ch03", 26, lambda: zero(integrate(cos(P1 + P2 - 2 * w * t), (t, 0, Tp))), "vanishes over a period")
sym("ch03", 27, lambda: zero(integrate(cos(P1 - w * t) * cos(P2 - w * t), (t, 0, Tp)) / Tp - cos(P1 - P2) / 2),
    "I = cos(delta)/2")
sym("ch03", 28, lambda: zero(a1 ** 2 / 2 + a2 ** 2 / 2 + 2 * a1 * a2 * cos(d) / 2 - (a1 ** 2 + 2 * a1 * a2 * cos(d) + a2 ** 2) / 2),
    "Eq 24 from Eqs 20, 23")
sym("ch03", 29, lambda: zero(((a1 ** 2 + 2 * a1 * a2 * cos(d) + a2 ** 2) / 2).subs(d, 0) - (a1 + a2) ** 2 / 2), "delta = 0")
sym("ch03", 30, lambda: zero(((a1 ** 2 + 2 * a1 * a2 * cos(d) + a2 ** 2) / 2).subs(d, pi) - (a1 - a2) ** 2 / 2), "delta = pi")
defn("ch03", [31, 32], "incoherent average: mean of cos(delta) = 0")
sym("ch03", 33, lambda: zero(((a1 ** 2 + 2 * a1 * a2 * 0 + a2 ** 2) / 2) - (a1 ** 2 + a2 ** 2) / 2), "Eq 27 with Eq 28")
z, ph1, ph2 = symbols("z phi_1 phi_2")
defn("ch03", [34, 35], "phases of the two plane waves (Fig 3.3)")
sym("ch03", 36, lambda: zero((k * n * z + ph1) - (k * n * (x * sin(th) + z * cos(th)) + ph2)
                             - (ph1 - ph2 - k * n * x * sin(th) + k * n * z * (1 - cos(th)))),
    "phase difference algebra")
defn("ch03", 37, "Eq 24 with delta -> Phi1 - Phi2")
sym("ch03", 38, lambda: zero(2 * (a1 ** 2 + 2 * a1 * a2 * cos(d - k * n * x * sin(th) + k * n * z * (1 - cos(th))) + a2 ** 2) / 2
                             - (a1 ** 2 + a2 ** 2 + 2 * a1 * a2 * cos(d - k * n * x * sin(th) + k * n * z * (1 - cos(th))))),
    "Eq 32 with Eq 31 substituted, times 2")
lam = symbols("lambda", positive=True)
sym("ch03", 39, lambda: zero((d - k * n * x * th).subs(k, 2 * pi / lam) - (d - 2 * pi * n * x * th / lam)),
    "small theta at z = 0: sin(theta) ~ theta, k = 2 pi/lambda")
defn("ch03", 40, "fringe condition: phase advances by 2 pi")
sym("ch03", 41, lambda: zero((2 * pi / ((2 * pi / lam) * n * sin(th))) - lam / (n * sin(th))), "fringe spacing h")

# ---------------- ch04 Visual optics ----------------
L, dd = symbols("L d", positive=True)
sym("ch04", 1, lambda: zero(L * (10 / pi) * pi * dd ** 2 / 4 - L * 5 * dd ** 2 / 2),
    "trolands = (cd/m^2) x pupil area (mm^2); 1 mL = 10/pi cd/m^2, area = pi d^2/4 -> 5 d^2/2 exactly")
