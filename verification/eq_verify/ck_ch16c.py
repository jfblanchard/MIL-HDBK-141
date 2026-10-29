import math
import cmath
import numpy as np
from scipy import special, integrate as sint
from ledger import *
from sympy import (symbols, sin, cos, tan, sqrt, pi, series, solve, simplify, exp, I, integrate, Matrix, besselj, diff, conjugate, expand)

x, y, D, zt, et, S, k, n, a, b, lam, R, z, U, ph, rho, rm = symbols("x y D zeta eta S k n a b lambda R z U phi rho rho_m", positive=True)
defn("ch16", [176, 177, 178, 179], "Huygens-Fresnel wavelet, distance, superposition integral, S")
r = sqrt((x - zt) ** 2 + (y - et) ** 2 + D ** 2)
Sx = sqrt(D ** 2 + x ** 2 + y ** 2)
sym("ch16", 180, lambda: zero(r - Sx * sqrt(1 + (zt ** 2 + et ** 2) / Sx ** 2 - 2 * (x * zt + y * et) / Sx ** 2)), "r rewritten about S")
w = symbols("w")
sym("ch16", [181, 182], lambda: zero(series(sqrt(1 - 2 * w), w, 0, 2).removeO() - (1 - w)), "first-order binomial, quadratic aperture terms dropped")
ref("ch16", [183, 184, 185, 186, 187, 188, 189], "Fraunhofer integral, definitions; uniform aperture")
sym("ch16", [190, 191], lambda: zero(integrate(exp(-I * k * n * x * zt / S), (zt, -a, a)) - (exp(I * k * n * x * a / S) - exp(-I * k * n * x * a / S)) / (I * k * n * x / S)),
    "rectangular aperture integral")
sym("ch16", [192, 193, 194], lambda: zero(((exp(I * k * n * x * a / S) - exp(-I * k * n * x * a / S)) / (I * k * n * x / S)).rewrite(sin).subs(k, 2 * pi / lam)
                                          - 2 * a * sin(2 * pi * a * n * x / (S * lam)) / (2 * pi * a * n * x / (S * lam))),
    "each factor = 2a sinc(2 pi a n x/S lambda); W = |F0|^2/S^2 with A = 4ab")
nu = symbols("nu", positive=True)
sym("ch16", 195, lambda: zero(solve(2 * pi * a * n * x / (S * lam) - nu * pi, x)[0] / S - nu * lam / (2 * a * n)), "zeros of the sinc")
defn("ch16", [196, 197, 198, 199, 200], "polar coordinates on aperture and image")
num("ch16", 201, lambda: all(abs(sint.quad(lambda p: math.cos(zv * math.cos(p)), 0, 2 * math.pi)[0] - 2 * math.pi * special.j0(zv)) < 1e-9 for zv in (0.3, 2.0, 7.5)),
    "Bessel integral checked by quadrature at three arguments")
ref("ch16", 202, "Eq 159 with Eq 162")
uu, rr = symbols("u rr", positive=True)
sym("ch16", 203, lambda: zero((S / (k * n * rr)) * (k * n * rr * uu / S) - uu), "change of variable v = knru/S")
v = symbols("v", positive=True)
sym("ch16", 204, lambda: zero((2 * pi * integrate(symbols("u") * besselj(0, k * n * symbols("rr") * symbols("u") / S), (symbols("u"), 0, a))).rewrite(besselj).simplify()
                              - 2 * pi * (S / (k * n * symbols("rr"))) ** 2 * (k * n * symbols("rr") * a / S) * besselj(1, k * n * symbols("rr") * a / S)),
    "substitution v = knru/S gives the (S/knr)^2 form (evaluated with Eq 166)")
sym("ch16", 205, lambda: zero(diff(v * besselj(1, v), v) - v * besselj(0, v)), "d/dz [z J1(z)] = z J0(z)")
sym("ch16", 206, lambda: zero(2 * pi * (S / (k * n * x)) ** 2 * (k * n * x * a / S) * besselj(1, k * n * x * a / S)
                              - 2 * pi * a ** 2 * besselj(1, k * n * x * a / S) / (k * n * x * a / S)), "rearranged to 2 pi a^2 J1(z)/z")
put("ch16", 207, "symbolic + scan", "FIXED",
    "transcription error, FIXED per scan p.16-51: the n in the denominator (2 pi n a r)/lambda S had been dropped; fixed form equals "
    "the previous line with k = 2 pi/lambda")
defn("ch16", 208, "sin theta = r/S")
ref("ch16", 209, "Eq 167 with Eq 168")
num("ch16", 210, lambda: close(special.jn_zeros(1, 1)[0] / (2 * math.pi), 0.61, 0.001), "first zero of J1 = 3.8317: sin(theta1) = 0.6098 lambda/(n a) = 1.22 lambda/(2an)")
sym("ch16", 211, lambda: zero((2 * pi * a ** 2) ** 2 / S ** 2 - 4 * pi ** 2 * a ** 4 / S ** 2), "W = |F0|^2/S^2")
defn("ch16", [212, 213, 214, 215], "converging spherical wave: optical path, aperture distribution, integral, r1")
Q = R ** 2 + zt ** 2 + et ** 2
r1 = sqrt((x - zt) ** 2 + (y - et) ** 2 + (R + z) ** 2)
sym("ch16", 216, lambda: zero(r1 ** 2 - Q * (1 + (x ** 2 + y ** 2 + z ** 2 - 2 * (x * zt + y * et - R * z)) / Q)), "Eq 176")
sym("ch16", 217, lambda: zero(series(sqrt(1 - 2 * w), w, 0, 2).removeO() - (1 - w)), "Eq 177 first-order binomial")
put("ch16", 218, "symbolic + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-53): Eqs 176-177 give r1 = sqrt(Q) - (x zeta + y eta - R z)/sqrt(Q), Q = R^2 + zeta^2 + eta^2; "
    "the printed denominator lacks the square root. Eq 179 uses the correct sqrt(Q)")
ref("ch16", [219, 220, 221], "Eq 174 with Eq 178; |e^{...}| = 1 so W = |F0|^2")
Uz, phz = symbols("U phi", positive=True)
zeta = R * tan(Uz) * cos(phz); eta = R * tan(Uz) * sin(phz)
defn("ch16", 222, "change of variables to aperture angle U")
sym("ch16", [223, 224], lambda: all(abs(float((sqrt(zeta ** 2 + eta ** 2 + R ** 2) * cos(Uz) - R).subs({R: 3.1, Uz: u_, phz: p_}))) < 1e-12
                 and abs(float((zeta / sqrt(zeta ** 2 + eta ** 2 + R ** 2) - sin(Uz) * cos(phz)).subs({R: 3.1, Uz: u_, phz: p_}))) < 1e-12
                 for u_, p_ in ((0.2, 0.3), (0.7, 2.5), (1.2, 4.0))),
    "cos U = R/sqrt(Q) and the direction sines")
Jm = Matrix([[diff(zeta, Uz), diff(eta, Uz)], [diff(zeta, phz), diff(eta, phz)]])
sym("ch16", [225, 226], lambda: zero(simplify(Jm.det()) - R ** 2 * sin(Uz) / cos(Uz) ** 3), "Jacobian R^2 sin U/cos^3 U")
sym("ch16", 227, lambda: zero((cos(Uz) ** 2 / R ** 2) * R ** 2 * sin(Uz) / cos(Uz) ** 3 - sin(Uz) / cos(Uz)), "1/Q x Jacobian = tan U")
defn("ch16", 228, "rho = sin U")
sym("ch16", 229, lambda: zero((sin(Uz) / cos(Uz)) / cos(Uz) - (rho / (1 - rho ** 2)).subs(rho, sin(Uz)).subs(1 - sin(Uz) ** 2, cos(Uz) ** 2).simplify()),
    "dU = d rho/cos U: tan U dU = rho d rho/(1 - rho^2); cos U = sqrt(1 - rho^2)")
ref("ch16", 230, "z = 0 and 1/(1 - rho^2) ~ 1 (moderate aperture), as stated")
defn("ch16", 231, "polar image coordinates")
ref("ch16", [232, 233], "same angular integration as Eqs 159-163")
num("ch16", 234, lambda: all(abs(2 * math.pi * sint.quad(lambda p: special.j0(kr * p) * p, 0, 0.4)[0]
                                 - 2 * math.pi * 0.4 ** 2 * special.j1(kr * 0.4) / (kr * 0.4)) < 1e-10 for kr in (1.0, 9.0, 25.0)),
    "Eq 193 = Eq 192 by quadrature (rho_m = 0.4, three values of knr)")
defn("ch16", 235, "image-space numerical aperture")
sym("ch16", 236, lambda: zero((2 * pi * rm ** 2) ** 2 - 4 * pi ** 2 * rm ** 4), "W = |F0|^2")
num("ch16", [237, 238], lambda: close(special.jn_zeros(1, 1)[0] / (2 * math.pi), 0.6098, 1e-4), "3.8317/(2 pi) = 0.6098")
ref("ch16", [239, 240, 241], "object-space radius via the sine condition: |M| n sin U_m = n0 sin U_0m = N.A.")
defn("ch16", [242, 243], "angular radius at the image distance V; small-angle aperture")
num("ch16", 244, lambda: close(2 * 0.6098, 1.22, 0.001), "rho_m = D/(2V): theta1 = 2(0.6098) lambda/(nD) = 1.22 lambda/(nD)")
ref("ch16", [245, 246, 247], "defocused pupil function")
sym("ch16", 248, lambda: zero(series(sqrt(1 - rho ** 2), rho, 0, 3).removeO() - (1 - rho ** 2 / 2)), "first-order expansion")
put("ch16", 249, "symbolic + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-58): e^{iknz sqrt(1-rho^2)} ~ e^{iknz} e^{-i pi n z rho^2/lambda}; the book prints +i. "
    "Harmless: only |F0| is used afterwards")
cc = symbols("c", positive=True)
put("ch16", [250, 251], "symbolic + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-58): integral of e^{i c rho^2} rho d rho = (e^{i c rho_m^2} - 1)/(2 i c), so F0(0) = pi e^{iknz}[...]/(i pi n z/lambda); "
    "the printed 2 pi doubles the amplitude (W 4x too large; in focus it must equal Eq 195's value pi^2 rho_m^4)")
sym("ch16", [252, 253], lambda: zero(expand((exp(I * w) - 1) * (exp(-I * w) - 1)) - (2 - 2 * cos(w)).rewrite(exp)), "|e^{iw} - 1|^2 = 2 - 2 cos w")
sym("ch16", 254, lambda: zero(8 * pi ** 2 * (1 - cos(cc * rm ** 2)) / cc ** 2 - 4 * pi ** 2 * rm ** 4 * (sin(cc * rm ** 2 / 2) / (cc * rm ** 2 / 2)) ** 2),
    "1 - cos w = 2 sin^2(w/2) (consistent with the book's Eq 209)")
put("ch16", 255, "symbolic + scan", "FLAG",
    "1962 ORIGINAL (sic, scan p.16-58): Eq 210 at z = 0 gives 4 pi^2 rho_m^4, not the printed 4 pi rho_m^4 (and the correctly normalised "
    "in-focus value is pi^2 rho_m^4, see Eq 250). The ratio K (Eq 212) is unaffected")
sym("ch16", 256, lambda: zero((4 * pi ** 2 * rm ** 4 * (sin(w) / w) ** 2) / (4 * pi ** 2 * rm ** 4) - (sin(w) / w) ** 2), "normalised Strehl-type ratio")
defn("ch16", 257, "quarter-wave-type defocus criterion")
num("ch16", 258, lambda: close((math.sin(math.pi / 4) / (math.pi / 4)) ** 2, 0.8106, 1e-4), "at pi z n rho_m^2/lambda = pi/2: K = [sin(pi/4)/(pi/4)]^2 = 0.8106")
sym("ch16", 259, lambda: zero(solve(pi * z * n * rm ** 2 / lam - pi / 2, z)[0] - n * lam / (2 * (n * rm) ** 2)), "Eq 213 solved for |z|")
