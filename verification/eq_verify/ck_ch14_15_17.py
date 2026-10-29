import math
from ledger import *
from eyepieces import parse_ch14, paraxial
from sympy import symbols, sin, tan, simplify, solve, sqrt, Rational

# ---------------- ch14 eyepieces ----------------
EP = parse_ch14()


def ch14_ok():
    msgs = []
    for tid, d in EP.items():
        efl, bfd, p = paraxial(d["rows"])
        g = -1 / (efl * -p)
        last = d["rows"][-1][1]
        ok = close(efl, 2.54, 0.003) and close(-p, d["sigmaP"], 0.002) and close(g, d["gamma"], 0.003) and (last is None or abs(bfd - last) < 0.006)
        msgs.append(ok)
    return len(EP) == 9 and all(msgs)


num("ch14", 1, ch14_ok,
    "paraxial trace of all nine Tables 14.1-14.9 (glass n_d from the MIL code): EFL = 2.534-2.540 cm, back focus = printed last "
    "spacing to <0.005 cm (Huygenian focus 0.718 cm inside the field lens), Sigma P and gamma = -1/(f Sigma P) match every "
    "printed value (orthoscopic 0.3163 vs 0.3158, glass-code rounding)")

# ---------------- ch15 complete telescope ----------------
num("ch15", 1, lambda: close(10 * 2.5, 25) and close(10 * 0.5, 5.0) and close(25 / 5.0, 5.0),
    "f_o = MP f_e = 25 cm, D_o = MP D_ep = 5.0 cm, N = 5.0")
num("ch15", 2, lambda: close(math.degrees(math.atan(math.tan(math.radians(30)) / 10)), 3.30, 0.005),
    "arctan(tan 30 deg / 10) = 3.30 deg (book: 3.3, '3 deg approx.')")
num("ch15", 3, lambda: close(4 * 2.9 / 1.5725, 7.3767, 1e-4),
    "4A/n with A = 2.9 cm prism aperture and n = 1.5725 (glass 573574): 7.3767 cm")

# ---------------- ch17 optical materials ----------------
I, Ip, n = symbols("I I' n", positive=True)
num("ch17", 1, lambda: close(0.5 * (math.sin(math.radians(1e-3) - math.radians(1e-3) / 1.5) ** 2 / math.sin(math.radians(1e-3) + math.radians(1e-3) / 1.5) ** 2
                                    + math.tan(math.radians(1e-3) - math.radians(1e-3) / 1.5) ** 2 / math.tan(math.radians(1e-3) + math.radians(1e-3) / 1.5) ** 2), 0.04, 1e-3),
    "Fresnel unpolarised reflectance; its normal-incidence limit reproduces Eq 2 (n = 1.5 -> 0.0400)")
num("ch17", 2, lambda: close(((1.52 - 1) / (1.52 + 1)) ** 2, 0.043, 0.01), "Eq 2; used below: (0.52/2.52)^2 = 0.0426")
ref("ch17", [3, 5, 6], "Lambert absorption law, natural and decimal forms (beta = alpha log10 e)")
ref("ch17", 4, "extinction coefficient kappa = alpha lambda/(4 pi n) (Born & Wolf convention with k = n kappa)")
R, T, Ti = symbols("R T T_inf", positive=True)
defn("ch17", 7, "single pass through two surfaces")
ref("ch17", 8, "multiple incoherent reflections: geometric series (1-R)^2 T sum (T R)^(2k)")
put("ch17", 9, "symbolic (sympy)", "FLAG",
    "1962 ORIGINAL (sic, as printed): misplaced parentheses; literal form gives T ~ 308 for the example. Eq 8 rearranges to the "
    "next line (verified symbolically), which gives T = 0.962 vs the text's 0.960")
sym("ch17", 10, lambda: zero(((T ** 2 + (1 / R - 1) ** 2 * T / Ti - 1 / R ** 2) * R ** 2 * Ti).expand()
                             - (Ti * (T ** 2 * R ** 2) + (1 - R) ** 2 * T - Ti).expand()),
    "corrected form: Eq 8, T_inf (1 - T^2 R^2) = (1-R)^2 T, divided by R^2 T_inf")
num("ch17", 11, lambda: close((0.52 / 2.52) ** 2, 0.043, 0.01), "(0.52/2.52)^2 = 0.0426 -> 0.043")
num("ch17", 12, lambda: close(0.883 / (1 - 0.043) ** 2, 0.964, 0.001), "Eq 7 with T1 = 0.883 (measured), R = 0.043: T = 0.9641")
num("ch17", 13, lambda: close(-math.log10(0.964) / 6.18, 0.00257, 0.005), "-log10(0.964)/6.18 mm = 0.002575/mm")
num("ch17", 14, lambda: close(10 ** (-0.00257 * 25.4), 0.860, 0.001), "10^(-0.00257 x 25.4) = 0.8603")
num("ch17", 15, lambda: close(0.914 / (1 - 0.043) ** 2, 0.998, 0.001), "Eq 7 with T1 = 0.914, R = 0.043: T = 0.9980")
num("ch17", 16, lambda: close(-math.log10(0.995) / 6.61, 0.00033, 0.01),
    "-log10(0.995)/6.61 mm = 0.000329/mm (text gives the sample as 6.6 mm)")
ref("ch17", 17, "IR 'nu' analogue (n-1)/(dn/dlambda) for a narrow band")
p1, p2, V1, V2, c1, c2, d1, d2 = symbols("phi_1 phi_2 V_1 V_2 c_1 c_2 d_1 d_2")
sym("ch17", 18, lambda: zero(solve(p1 / V1 + p2 / V2, p1)[0] / p2 + V1 / V2) and zero(solve(c1 * d1 + c2 * d2, c1)[0] / c2 + d2 / d1),
    "achromat condition phi1/V1 + phi2/V2 = 0, or with phi = c(n-1): c1 dn1 + c2 dn2 = 0")
nv("ch17", 19, "fluorite partial dispersion 0.293 needs the book's 1962 index data; modern CaF2 (n_C 1.43249, n_D 1.43384, "
   "n_F 1.43704) gives 0.297")
