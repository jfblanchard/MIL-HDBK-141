import math
import numpy as np
from ledger import *
from sympy import symbols, sqrt, Matrix, eye, Rational, simplify

# ---------------- ch12 lens relays ----------------
D, n, f = symbols("D n f", positive=True)
sym("ch12", 1, lambda: zero(2 * (-(2 / D) / n) - (-4 / (D * n))),
    "two relay doublets of f = D/2, each P = -phi/n (ch08 Eq 28): Sigma P = -4/(D n)")
num("ch12", 2, lambda: close(-1 / (2.54 * -0.2125), 1.853, 0.001),
    "Erfle Sigma P = -0.2125 cm^-1 is Table 14.7's printed value (and gives Table 14.7's gamma = 1.853 with f = 2.54)")
ref("ch12", 3, "ch06 secondary-spectrum rule (P~ slope ~ -1/2200) for one doublet: TAch ~ y1/2200")
num("ch12", 4, lambda: close(0.14 * 70 / 2200, 0.00445) and abs(0.14 * 70 / 2200 - 0.005) < 0.0006,
    "Eq 1: two doublets, y1 = u0 D/2 each; book example u0 = 0.14, D = 70 cm gives 0.0045 cm (text rounds to 0.005)")
ref("ch12", 5, "Eq 2: same with the effective length D - d")
sym("ch12", 6, lambda: zero(1 / (4 / D + 4 / D) - D / 8) and zero(-(8 / D) / n - (-8 / (D * n))),
    "field lens at D/2 images the relay at D/4 onto the relay at 3D/4: 1/f = 4/D + 4/D; P = -phi/n")

# ---------------- ch13 mirror and prism systems ----------------
cI = symbols("cosI", positive=True)
sym("ch13", [1, 2], lambda: zero((-cI - sqrt(cI ** 2)) + 2 * cI), "ch02 Eq 4 with n1 = -n0 (= 1): Gamma = -cos I - |cos I| = -2 cos I")
defn("ch13", [3, 4, 5, 6, 7, 8, 9], "successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example)")
s0 = np.array([0, 0, 1.0]); M = np.array([-0.5, -0.5, 1 / math.sqrt(2)])
s1 = s0 - 2 * np.dot(s0, M) * M
defn("ch13", [10, 11, 12], "worked example: fold the Z axis into (i + j)/sqrt 2")
num("ch13", [13, 14, 15, 16, 17, 18, 19, 20, 21], lambda: np.allclose(s1, [1 / math.sqrt(2), 1 / math.sqrt(2), 0]) and close(np.linalg.norm(M), 1),
    "solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly")
defn("ch13", 22, "plane equation")
ref("ch13", [23, 24, 25, 26, 27, 28, 29, 30], "foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D)")
num("ch13", 31, lambda: close(1 / M[0], -2) and close(1 / M[1], -2) and close(1 / M[2], math.sqrt(2)), "reciprocals of the example's M")
A_, B_, C_, D_, x, y, z = symbols("A B C D x y z")
F = sqrt(A_ ** 2 + B_ ** 2 + C_ ** 2)
d = (A_ * x + B_ * y + C_ * z + D_) / F
refl = Matrix([x, y, z]) - 2 * d * Matrix([A_, B_, C_]) / F
defn("ch13", [32, 33], "plane through the point / the mirror")
sym("ch13", 34, lambda: zero(((D_ - (-(A_ * x + B_ * y + C_ * z))) / F) - d), "Eq 12 with D1 = -(A x1 + B y1 + C z1)")
sym("ch13", [35, 36, 37], lambda: zero((refl - Matrix([x, y, z])).dot(Matrix([B_, -A_, 0]))) and zero((A_ * refl[0] + B_ * refl[1] + C_ * refl[2] + D_) + (A_ * x + B_ * y + C_ * z + D_)),
    "Eqs 13-15: the image point is displaced along the normal and lies equally far on the other side of the plane")
Mh = Matrix([[1, 0, 0, 0],
             [-2 * A_ * D_ / F ** 2, 1 - 2 * A_ ** 2 / F ** 2, -2 * B_ * A_ / F ** 2, -2 * A_ * C_ / F ** 2],
             [-2 * B_ * D_ / F ** 2, -2 * A_ * B_ / F ** 2, 1 - 2 * B_ ** 2 / F ** 2, -2 * B_ * C_ / F ** 2],
             [-2 * C_ * D_ / F ** 2, -2 * A_ * C_ / F ** 2, -2 * B_ * C_ / F ** 2, 1 - 2 * C_ ** 2 / F ** 2]])
sym("ch13", 38, lambda: all(zero(e) for e in (Mh * Matrix([1, x, y, z]))[1:, 0] - refl), "Eq 16 4x4 matrix equals Eqs 13-15")
ref("ch13", [39, 40, 41], "composition of reflections as matrix products")
Mx, My, Mz = symbols("M_x M_y M_z")
Mv = Matrix([Mx, My, Mz]); S0 = Matrix(symbols("S_x S_y S_z"))
R = eye(3) - 2 * Mv * Mv.T
sym("ch13", [42, 43, 44, 45, 46], lambda: all(zero(e) for e in (S0 - 2 * (S0.dot(Mv)) * Mv) - R * S0),
    "vector reflection law written out in components equals the Eq 19 matrix (Householder form I - 2MM^T)")
ref("ch13", 47, "Eq 20 composition of reflections")
ref("ch13", [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], "rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25")
defn("ch13", 61, "unit normal")
num("ch13", [62, 63, 64], lambda: close(math.tan(math.radians(30)) / math.sin(math.radians(45)), 0.81657, 1e-4) and
    close(math.degrees(math.atan(0.81657)), 39.2, 0.002),
    "tan 30 / sin 45 = 0.81650 (book 0.81657 from the rounded .5774/.7071); theta = 39.23 deg")


def dove(n_, A=1.0, a=0.05, th=math.radians(45)):
    s = math.sin(th); r = math.sqrt(n_ ** 2 - s ** 2)
    B = (A + 2 * a) * ((r + s) / (r - s) + 1)
    t = n_ * (A + 2 * a) / (s * (r - s))
    return dict(B=B, C=B - 2 * a, D=B - 2 * (A + 2 * a), E=(a + A) / math.cos(th), t=t, tn=t / n_)


TAB = {1.5170: (4.6498, 4.5498, 2.4498, 1.4849, 3.7165, 2.4499), 1.5725: (4.4303, 4.3303, 2.2303, 1.4849, 3.5071, 2.2303),
       1.6170: (4.2822, 4.1822, 2.1822, 1.4849, 3.3637, 2.0802), 1.7200: (4.0072, 3.9072, 1.9072, 1.4849, 3.1084, 1.8072)}
bad = [(n_, k, v, round(dove(n_)[k], 4)) for n_, row in TAB.items() for k, v in zip(("B", "C", "D", "E", "t", "tn"), row)
       if abs(dove(n_)[k] - v) > 1e-3]
flag("ch13", [65, 66, 67], "numeric (book values) + scan",
     "B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read "
     "sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) "
     "(1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but "
     "D = B - 2(A + 2a) = " + ", ".join(f"{b[3]:.4f}" for b in bad if b[1] == "D") + " (t/n shows these D are typos: D should equal t/n). "
     "Mismatches found: " + "; ".join(f"n={b[0]} {b[1]} printed {b[2]} computed {b[3]}" for b in bad))
num("ch13", [68, 69], lambda: close((1.0 / 2) * ((math.sqrt(1.517 ** 2 - .5) + math.sqrt(.5)) / (math.sqrt(1.517 ** 2 - .5) - math.sqrt(.5)) + 1), 2.1136, 1e-4)
    and close(1.517 / (2 * math.sqrt(.5) * (math.sqrt(1.517 ** 2 - .5) - math.sqrt(.5))), 1.6893, 2e-4) and close(1 / (2 * math.cos(math.radians(45))), 0.7071, 1e-4),
    "double Dove, n = 1.517: B = 2.1135, t = 1.6892 (same parenthesisation as the single Dove), t/n = 1.1135, D = 0.7071")
flag("ch13", 70, "numeric (book values)",
     "2.283/2.835 = 0.805291 is right, but arccos(0.805291) = 36 deg 21' 42\", not the printed 36 deg 22' 3\" (21 arcsec; "
     "minor 1962 table-interpolation slip, or transcription; scan not re-read)")
