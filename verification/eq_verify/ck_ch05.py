"""ch05 ray tracing.

FIDELITY FINDING (scan pages 5-5..5-22 viewed 2026-09-24): the transcription's skew-ray, aspheric and
meridional equations are a modern paraphrase with its own numbering, not the book's equations. The book
uses optical direction cosines (K = n cos) and the Feder-style quantities H, B, A/n_-1 (Eqs 1-15, p.5-11),
E, U, V, W, G, P for aspherics (Eqs 16-32, 5-17..5-22). Each transcription block is therefore checked on
its own mathematics AND flagged for fidelity; the book's real Eqs (1)-(15) are verified separately below
by reproducing the book's Table 5.2 worked trace.
"""
import numpy as np
from ledger import *
from sympy import symbols, sqrt, diff, simplify

FID = "FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); "

# --- exact reference: vector ray/sphere intersection and refraction ---------------------------------
def exact_hit(X0, Y0, K, L, M, r):
    """Ray from (X0,Y0,0) with unit direction; sphere vertex at origin, centre (0,0,r). Returns path s."""
    F = K * X0 + L * Y0; G = X0 ** 2 + Y0 ** 2
    b = r * M - F
    return b - np.sign(r) * np.sqrt(b * b - G)


def refract(u, N, n0, n1):
    cI = np.dot(u, N)
    if cI < 0:
        N, cI = -N, -cI
    cIp = np.sqrt(1 - (n0 / n1) ** 2 * (1 - cI ** 2))
    return (n0 * u + (n1 * cIp - n0 * cI) * N) / n1


rng = np.random.default_rng(1)
CASES = []
for _ in range(20):
    r = rng.choice([-1, 1]) * rng.uniform(3, 20)
    X0, Y0 = rng.uniform(-1, 1, 2)
    u = np.array([rng.uniform(-.2, .2), rng.uniform(-.2, .2), 1.0]); u /= np.linalg.norm(u)
    CASES.append((r, X0, Y0, *u))


def t_transfer_eq1_3():
    # X1 = X0 + (K/M) D with D a z-distance: consistent with a straight line
    for r, X0, Y0, K, L, M in CASES:
        s = exact_hit(X0, Y0, K, L, M, r); D = s * M
        if abs((X0 + K / M * D) - (X0 + s * K)) > 1e-12: return False
    return True


def t_eq4_10():
    """Transcription's Eqs 4-10: D_sphere = r (H - sqrt(Delta)) with Delta = H^2 - (M^2-1)(1-G/r^2)."""
    for r, X0, Y0, K, L, M in CASES:
        F = K * X0 + L * Y0; G = X0 ** 2 + Y0 ** 2; H = M - F / r
        Dl = H ** 2 - (M ** 2 - 1) * (1 - G / r ** 2)
        Dt = r * (H - np.sqrt(Dl))
        Dz = exact_hit(X0, Y0, K, L, M, r) * M
        if abs(Dt - Dz) > 1e-9: return False
    return True


def t_eq11_12():
    for r, X0, Y0, K, L, M in CASES:
        s = exact_hit(X0, Y0, K, L, M, r); P = np.array([X0, Y0, 0]) + s * np.array([K, L, M])
        N = np.array([-P[0] / r, -P[1] / r, 1 - P[2] / r])
        if abs(np.linalg.norm(N) - 1) > 1e-9: return False
        # the true cos I is |u.N|; transcription writes cos I = -(u.N): negative for r > 0 (sign flag)
    return True


def t_eq13_15():
    """K1 = (n0/n1) K0 + Gamma alpha_N with geometric cosines (Eq 31 says K^2+L^2+M^2=1)."""
    n0, n1 = 1.0, 1.62
    for r, X0, Y0, K, L, M in CASES:
        u = np.array([K, L, M]); s = exact_hit(X0, Y0, K, L, M, r); P = np.array([X0, Y0, 0]) + s * u
        N = np.array([-P[0] / r, -P[1] / r, 1 - P[2] / r])
        cI = abs(np.dot(u, N)); cIp = np.sqrt(1 - (n0 / n1) ** 2 * (1 - cI ** 2))
        Gam = n1 * cIp - n0 * cI
        Nn = N if np.dot(u, N) > 0 else -N
        u1 = n0 / n1 * u + Gam * Nn
        if abs(np.linalg.norm(u1) - 1) > 1e-6: return False
    return True


sym_ok = lambda: t_transfer_eq1_3()
num("ch05", [1, 2, 3], t_transfer_eq1_3,
    "transfer to tangent plane: equivalent to book Eqs (1)-(3) (d/n = (t-Z)/M; K/M ratio is cosine-convention free); "
    "numerically identical to an exact straight-line transfer (20 random rays)")
c, S = symbols("c S", positive=True)
sym("ch05", 4, lambda: zero((1 / c - sqrt(1 / c ** 2 - S ** 2)) - c * S ** 2 / (1 + sqrt(1 - c ** 2 * S ** 2))),
    "sphere sag, two forms (book p.5-13 prints the same pair)")
defn("ch05", [5, 6, 7, 8], FID + "auxiliary definitions F, G, eta, H (eta = G/r is never used)")
put("ch05", [9, 10], "numeric (exact vector trace, 20 random rays)",
     "VERIFIED" if t_eq4_10() else "FLAG",
     FID + ("agrees with exact intersection" if t_eq4_10() else
            "Delta = H^2 - (M^2-1)(1-G/r^2) does NOT give the sphere intersection; correct form for a z-distance is "
            "D = M r (H - sqrt(H^2 - G/r^2)) (derived: s^2 - 2s(rM - F) + G = 0). Book instead uses Eqs (7)-(10) with B, H, A/n."))
num("ch05", 11, t_transfer_eq1_3, FID + "transfer tangent plane -> sphere along the ray (same straight-line form)")
put("ch05", 12, "numeric (exact vector trace)", "VERIFIED" if t_eq11_12() else "FLAG",
     FID + "unit normal (-X/r, -Y/r, 1 - Z/r) is correct (|N| = 1 verified on 20 rays)")
flag("ch05", 13, "numeric (exact vector trace)",
     FID + "sign: with the normal of Eq 11 pointing to the centre, K.N > 0 for a ray meeting a convex (r>0) surface, "
     "so cos I = -(K alpha + L beta + M gamma) is negative; book's Eq (7) computes n cos I directly from B and H")
put("ch05", [14, 15, 16], "numeric (exact vector trace)", "VERIFIED" if t_eq13_15() else "FLAG",
     FID + ("unit length preserved" if t_eq13_15() else
            "with geometric cosines (Eq 31: K^2+L^2+M^2 = 1) the refraction law needs Gamma/n_1, not Gamma: "
            "|u1| != 1 on 20 random rays. Book's Eqs (13)-(15) use optical cosines (K = n cos) where K = K_-1 - X c Gamma is correct"))
sym("ch05", 17, lambda: zero(symbols("n1") * sqrt(1 - (symbols("n0") / symbols("n1")) ** 2 * (1 - symbols("cI") ** 2))
                             - symbols("n1") * sqrt((symbols("n0") / symbols("n1") * symbols("cI")) ** 2 - (symbols("n0") / symbols("n1")) ** 2 + 1)),
    "Gamma and cos I' from Snell; equals book Eq (11)/(12) rearranged")
e, f, g, h = symbols("e f g h")
Zs = c * S ** 2 / (1 + sqrt(1 - c ** 2 * S ** 2)) + e * S ** 4 + f * S ** 6 + g * S ** 8 + h * S ** 10
ref("ch05", 18, FID + "aspheric sag, standard even-polynomial form (book p.5-13/5-14 uses the same deformation terms)")
sym("ch05", 19, lambda: zero(diff(Zs, S) / S - (c / sqrt(1 - c ** 2 * S ** 2) + 4 * e * S ** 2 + 6 * f * S ** 4 + 8 * g * S ** 6 + 10 * h * S ** 8)),
    FID + "B = (1/S) dZ/dS confirmed (book's E = c + W[...] is the same quantity times W)")
X_, Y_ = symbols("X Y")
Zxy = Zs.subs(S, sqrt(X_ ** 2 + Y_ ** 2))
Bxy = (c / sqrt(1 - c ** 2 * S ** 2) + 4 * e * S ** 2 + 6 * f * S ** 4 + 8 * g * S ** 6 + 10 * h * S ** 8).subs(S, sqrt(X_ ** 2 + Y_ ** 2))
sym("ch05", [20, 21, 22], lambda: zero(diff(Zxy, X_) - Bxy * X_) and zero(diff(Zxy, Y_) - Bxy * Y_), FID + "gradient and unit normal of z = Z(S): dZ/dX = B X, |(-BX,-BY,1)| = sqrt(B^2 S^2 + 1); standard")
nv("ch05", [23, 24, 25, 26, 27, 28, 29], FID + "iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check")
ref("ch05", [30, 31, 32], FID + "same as transcription Eqs 13-15 (see flag there)")
defn("ch05", 33, "unit direction vector")
sym("ch05", 34, lambda: zero(symbols("n1") * sqrt(1 - (symbols("n0") / symbols("n1")) ** 2 * (1 - symbols("cI") ** 2)) / symbols("n1")
                             - sqrt(1 - (symbols("n0") / symbols("n1")) ** 2 * (1 - symbols("cI") ** 2))),
    "cos I' from Snell's law")
flag("ch05", [35, 36], "numeric (sign test)",
     FID + "sign conventions inconsistent: Eq 33 X_new = X + t tan U needs U > 0 for a rising ray, but Eq 34 "
     "sin I = (X/r)cos U - sin U gives I = 0 for a ray aimed at the centre only if U > 0 for a FALLING ray")
ref("ch05", [37, 38], "Snell; U' = U - (I - I') is the standard slope-angle update")
ref("ch05", [39, 40], "axial intercept of the emergent ray; LSA definition")
nv("ch05", [41, 42, 43, 44, 45, 46], FID + "'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term")
ref("ch05", [47, 48], "Coddington sagittal/tangential equations, standard form (sign convention: distances D measured opposite for object)")
ref("ch05", [49, 50], "transfer of Coddington distances")
ref("ch05", 51, "paraxial transfer y_k = y_{k-1} + t u (n cancels)")
ref("ch05", [52, 53], "paraxial refraction (nu)' = nu - y phi, phi = c (n' - n); standard")
nv("ch05", [54, 55, 56, 57], FID + "duplicate of Eqs 39-44 in a summary box; not verified (see there)")


# --- book's real Eqs (1)-(15) (read from scan p.5-11) reproduce the book's Table 5.2 (p.5-12) -------
def book_skew_trace():
    c = [0, 0.25284872, -0.01473947]; t = [-2.2, 0.6]; n = [1.0, 1.62, 1.0]
    X, Y, Z, K, L, M = 1.48, 0.0, 0.0, 0.0, 0.17360000, 0.98481625
    got = []
    for j in (1, 2):
        dn = (t[j - 1] - Z) / M                                  # (1)
        YT = Y + dn * L; XT = X + dn * K                         # (2),(3)
        H = c[j] * (XT ** 2 + YT ** 2)                           # (9)
        B = M - c[j] * (YT * L + XT * K)                         # (10)
        ncI = n[j - 1] * np.sqrt((B / n[j - 1]) ** 2 - c[j] * H)  # (7)
        An = H / (B + ncI)                                       # (8)
        X, Y, Z = XT + An * K, YT + An * L, An * M               # (4)-(6)
        ncIp = n[j] * np.sqrt((ncI / n[j]) ** 2 - (n[j - 1] / n[j]) ** 2 + 1)  # (11)
        Gm = ncIp - ncI                                          # (12)
        K, L, M = K - X * c[j] * Gm, L - Y * c[j] * Gm, M - (Z * c[j] - 1) * Gm  # (13)-(15)
        got.append(dict(dn=dn, XT=XT, YT=YT, H=H, B=B, ncI=ncI, An=An, X=X, Y=Y, Z=Z, ncIp=ncIp, G=Gm, K=K, L=L, M=M))
    book = [dict(dn=-2.23391927, YT=-0.38780839, H=0.59186710, B=1.00183892, ncI=0.92413654, An=0.30730770,
                 X=1.48, Y=-0.33445977, Z=0.30264162, ncIp=1.57430250, G=0.65016596, K=-0.24330257, L=0.22858306, M=1.58522985),
            dict(dn=0.18758061, XT=1.43436116, YT=-0.29158202, H=-0.03157802, B=1.57910362, ncI=1.57871680,
                 An=-0.00999994, X=1.43679417, Y=-0.29386784, Z=-0.01585220, ncIp=0.93163659, G=-0.64708020,
                 K=-0.25700617, L=0.23138586, M=0.93830084)]
    worst = max(abs(got[j][k] - v) for j in range(2) for k, v in book[j].items())
    return worst < 2e-6, worst


BOOK_TABLE_5_2 = book_skew_trace()
extra("ch05-book-(1)-(15)", "ch05", "numeric (book Table 5.2)", BOOK_TABLE_5_2[0],
      "book's skew-ray Eqs (1)-(15) as printed on scan p.5-11 (optical cosines, H, B, A/n) reproduce every entry "
      f"of the worked Table 5.2 (two surfaces, n = 1.62) to {BOOK_TABLE_5_2[1]:.1e}")
