import math
from ledger import *
from sympy import symbols, integrate, sin, cos, pi, sqrt, series, Rational, simplify, solve

# ---------------- ch18 atmospheric optics ----------------
ref("ch18", 1, "Bouguer-Lambert attenuation")
defn("ch18", 2, "extinction = absorption + scattering")
ref("ch18", 3, "Rayleigh scattering ~ lambda^-4")
num("ch18", 4, lambda: close(1.8 ** 4, 10.5, 0.01) and abs(1.8 ** 4 - 10) < 0.6,
    "1.8^4 = 10.5 ~ 10 (violet vs red wavelength ratio ~1.8)")

# ---------------- ch19 missile tracking optics ----------------
defn("ch19", 1, "spherical aberration as an even power series in aperture")
defn("ch19", 2, "air-space relation for Fig 19.4 (a - b = c in the figure's lengths)")
num("ch19", 3, lambda: close(4.56 / 1.0, 4.5, 0.02), "Dawes limit 4.56\"/D(in); the book rounds to 4.5/a")
num("ch19", 4, lambda: close(5 ** 2 / 25, 1.0) and close(10 ** 2 / 25, 4.0),
    "empirical coma-limited field rule reproduces the text's own examples: f/5 -> 1 inch, f/10 -> 4 inches")
defn("ch19", 5, "Eq 4 sag power series")
r, y, K = symbols("r y K", positive=True)
sph = r - sqrt(r ** 2 - y ** 2)
sym("ch19", [6, 7, 8], lambda: zero(series(sph, y, 0, 4).removeO() - y ** 2 / (2 * r)), "a1 = 1/(2r) from the sphere's sag expansion")
put("ch19", 9, "numeric (consistency)", "FLAG",
    "P = 2Nc agrees with ch08 Eq 14 only for N = 1: for a mirror (n = -N) Eq 8-(14) gives P = c(N + N)/(N(-N)) = -2c/N "
    "(magnitude 2c/N). Sign follows the chapter's convention; the N-dependence differs (scan not re-read)")
sym("ch19", 10, lambda: zero(((y ** 2 / r) / (1 + sqrt(1 - (1 + K) * y ** 2 / r ** 2))).subs(K, -1) - y ** 2 / (2 * r)),
    "paraboloid -x = y^2/(2r) exactly")
sym("ch19", 11, lambda: zero(series(sph, y, 0, 6).removeO() - (y ** 2 / (2 * r) + y ** 4 / (8 * r ** 3))), "sphere sag to y^4: 1/(8r^3)")
conic = (y ** 2 / r) / (1 + sqrt(1 - (1 + K) * y ** 2 / r ** 2))
sym("ch19", 12, lambda: zero(series(conic.subs(K, 1), y, 0, 6).removeO() - (y ** 2 / (2 * r) + 2 * y ** 4 / (8 * r ** 3))),
    "y^4 coefficient 2/(8r^3) is the conic K = +1 (oblate spheroid), consistent with the text's classification")

# ---------------- ch22 infrared design ----------------
I, A, n, a, ap = symbols("I A n alpha alpha_p", positive=True)
ref("ch22", 1, "maximum flux a detector of area A in a medium of index n can accept: pi I n^2 A (etendue n^2 A pi)")
num("ch22", 2, lambda: close(75 ** 2 * math.pi, 17671.5), "aperture of 75 mm radius")
defn("ch22", [3, 4, 5], "flux element through a tilted aperture")
sym("ch22", 6, lambda: zero(integrate(2 * pi * sin(a), (a, 0, ap)) - 2 * pi * (1 - cos(ap))), "solid-angle element of a cone: dw = 2 pi sin(alpha) d alpha")
defn("ch22", [7, 8], "Eqs 2-3 integration of dF")
Ab = symbols("Abar", positive=True)
sym("ch22", 9, lambda: zero(2 * pi * I * Ab * integrate(cos(a) * sin(a), (a, 0, ap)) - pi * I * Ab * sin(ap) ** 2), "Eq 4 integral")
sym("ch22", 10, lambda: zero((pi * I * Ab * sin(ap) ** 2).subs(Ab, 75 ** 2 * pi) - pi ** 2 * I * 75 ** 2 * sin(ap) ** 2), "Eq 5 with A = 75^2 pi")
defn("ch22", [11, 12], "etendue limit F <= F_s")
num("ch22", 13, lambda: close(75 ** 2 * math.pi * math.sin(math.radians(10)) ** 2, 533, 0.002),
    "75^2 pi sin^2(10 deg) = 532.9 -> 533/n^2")
ref("ch22", [14, 15, 16, 17, 18, 19], "general and non-ideal (k) forms of the same etendue inequality")
sym("ch22", [20, 21], lambda: zero(integrate(sin(a), (a, 0, pi / 3)) - (1 - cos(pi / 3))), "integral of sin from 0 to 60 deg = 1 - cos 60 = 0.5")

# ---------------- ch23 microscope ----------------
ref("ch23", 1, "useful-magnification rule 1000 x N.A. (Lost Gem)")
defn("ch23", [2, 3], "half-angle and numerical aperture definitions")
ref("ch23", 4, "Abbe resolution with oblique/condenser illumination d = lambda/(NA_cond + NA_obj)")
ref("ch23", 5, "Huygenian 3:1 field/eye lens ratio with d = 2 f_eye")
f1, f2, d, f = symbols("f_1 f_2 d f", positive=True)
feq = f1 * f2 / (f1 + f2 - d)
nn_ = symbols("n", positive=True); c1_, c2_ = symbols("c_1 c_2")
P_eq = (nn_ - 1) * c1_ + (nn_ - 1) * c2_ - d * (nn_ - 1) ** 2 * c1_ * c2_
sym("ch23", 6, lambda: zero(solve(P_eq.diff(nn_).subs(nn_, 1 + 1 / (c1_ * f1)).subs(c2_, c1_ * f1 / f2), d)[0] - (f1 + f2) / 2),
    "d(power)/dn = 0 for two thin lenses of one glass gives d = (f1 + f2)/2; 3:1 Huygenian gives d = 2 f_eye")
sym("ch23", 7, lambda: zero(feq.subs({f1: f, f2: f, d: 2 * f / 3}) - 3 * f / 4), "Ramsden: f1 = f2 = f, d = 2f/3 -> f_eq = 3f/4")
defn("ch23", 8, "phasor sum P = D + S (Zernike phase-contrast picture, Fig 23.18)")
ref("ch23", 9, "optical path difference and phase of a specimen of thickness t")
defn("ch23", 10, "relative visibility bookkeeping (Table 23.1 footnote formula; three table entries don't follow it, flagged in the chapter)")

# ---------------- ch24 design-phase tests ----------------
ref("ch24", [1, 2, 3, 4], "Conrady's Rayleigh-limit (lambda/4) Seidel tolerances: LA 4 lambda/(N' sin^2 U'), zonal 6 lambda/(N' sin^2 U'), "
    "OSC lambda/(2 N' sin U'), focal range lambda/(N' sin^2 U')")
nv("ch24", 5, "astigmatism tolerance lambda/(4 N' sin^2 U'): the chapter does not define which astigmatic distance Ast's is; a Rayleigh "
   "lambda/4 criterion gives lambda/(N' sin^2 U') for the full T-S separation, so the factor 4 cannot be confirmed from the text")
put("ch24", 6, "reference (standard form)", "FLAG", "1962 ORIGINAL (sic): U_m unprimed, inconsistent with Eqs 1-5 (U'_m); otherwise equals Eq 4")
Um = symbols("U", positive=True)
sym("ch24", 7, lambda: zero(series(sin(Um / 2) ** 2 - sin(Um) ** 2 / 4, Um, 0, 4).removeO()),
    "stated as a small-angle assumption: sin^2(U/2) - sin^2(U)/4 = O(U^4)")
