import math
from ledger import *
from sympy import symbols, solve, Matrix, simplify

ref("ch11", [1, 2], "ch08 Eqs 15/16 keeping only the Petzval term (flat-field telescope approximation)")
u0, Yo, n1, y, Y1, y1, po, pe, go, ge, MP, to = symbols("u_0 Ybar_o n_1 y_k Y_1 y_1 phi_o phi_e gamma_o gamma_e MP t_o")
ref("ch11", 3, "Sigma P = -(phi_o/gamma_o + phi_e/gamma_e) from gamma = -1/(f Sigma P) (ch14 definition), Phi = n0 u0 Ybar_o")
a3 = -(u0 ** 2 / (2 * y)) * Yo ** 2 * (Y1 / y1) * (po / go + pe / ge)
sub = {u0: y1 / to, po: -pe / MP, y1: -MP * y}
a3s = a3.subs(u0, y1 / to).subs(po, -pe / MP).subs(y1, -MP * y)
eq3 = -(Yo / to) ** 2 / 2 * (Y1 / (-MP * y)) * MP ** 2 * y * pe * (-1 / (go * MP) + 1 / ge)
sym("ch11", 4, lambda: zero(a3s - eq3), "Eq 3 from the line above with u0 = y1/t_o, phi_o = -phi_e/MP, y1 = -MP y_(k-1) (afocal)")


def alpha(mp):
    return -0.5 * 0.36 * 1.0 * (-0.35) * 0.5 * (-1 / (1.5 * mp) + 1 / 1.5)


tab = {-2: (-9.0, 107), -5: (-7.2, 87), -10: (-6.6, 79)}
res = {m: (100 * alpha(m) / -0.35, math.degrees(alpha(m)) * 60) for m in tab}
num("ch11", [5, 6, 7, 8, 9], lambda: all(close(res[m][0], tab[m][0], 0.01) for m in tab) and all(abs(res[m][1] - tab[m][1]) <= 1.5 for m in tab),
    "Eq 3 with these inputs reproduces Table 11.1: diopters " + ", ".join(f"{res[m][0]:.1f}" for m in tab) +
    " (book -9.0, -7.2, -6.6); minutes " + ", ".join(f"{res[m][1]:.1f}" for m in tab) +
    " (book 107, 87, 79; the MP = -2 entry is 1.3' low)")
pa, pb, na, nb, va, vb, ph = symbols("phi_a phi_b n_a n_b nu_a nu_b phi")
s2 = solve([pa + pb - ph, pa / va + pb / vb], [pa, pb])
defn("ch11", [10, 11], "power and achromatism conditions")
sym("ch11", 12, lambda: zero(s2[pa] - ph * va / (va - vb)), "Eq 6 solves Eqs 4-5")
sym("ch11", 13, lambda: zero(s2[pb] - ph * vb / (vb - va)), "Eq 7 solves Eqs 4-5")
sym("ch11", 14, lambda: zero((-s2[pa] / na - s2[pb] / nb) - (-ph * (va / na - vb / nb) / (va - vb))),
    "Eq 8: thin-lens P = -phi/n (ch08 Eq 28) summed with Eqs 6-7")
num("ch11", 15, lambda: close((63.5 / 1.511 - 30.6 / 1.649) / (63.5 - 30.6), (57.0 / 1.52 - 36.0 / 1.62) / (57 - 36), 0.05),
    "the ratio is 'nearly constant': 0.713 for this pair vs 0.728 for a 520/570 + 620/360 pair (within 2%)")
ref("ch11", [16, 17, 18, 19], "thin-lens B, F forms of ch08 Eqs 24-25")
defn("ch11", [20, 21], "glass data as printed (scan p.11-4 confirms 1.511/63.5 and 1.649/30.6)")
ref("ch11", [22, 23, 24], "first-order differential corrections (ch09 Eqs 1-7)")
defn("ch11", 25, "Seidel/fifth-order coefficients of the example")
num("ch11", [26, 27, 28], lambda: close(4.6 * 0.5893 / 0.14, 19.4), "4.6 x 0.5893 um / 0.14 = 19.36 um = 0.0194 mm (book 19.4)")
nv("ch11", 29, "aspheric deflection model stated as an assumption of the method; dimensional form (lambda times polynomial in S) "
   "cannot be derived from the text; no worked numbers")
ref("ch11", [30, 31, 32, 33], "thin-lens B, F forms (ch08 Eqs 24-25) for a cemented pair")
num("ch11", 34, lambda: 2e-5 <= 0.1 * 0.55 / 2200 * 1.0 <= 3e-5,
    "Eq 13 with d(TAch)/TAch = 1/10 and n_D - 1 ~ 0.55 gives dn = 2.5e-5, the text's '2 in the fifth decimal place'")
pc, vc, Pa, Pb, Pc, Qa, Qb, Qc = symbols("phi_c nu_c Pa Pb Pc Qa Qb Qc")
s3 = solve([pa + pb + pc - ph, pa / va + pb / vb + pc / vc, pa * Pa / va + pb * Pb / vb + pc * Pc / vc], [pa, pb, pc])
D = Matrix([[Pa, va, 1], [Pb, vb, 1], [Pc, vc, 1]]).det()
defn("ch11", [35, 36, 37], "apochromat conditions (power, F-C achromatism, D to the F-C focus)")
sym("ch11", 38, lambda: zero(s3[pa] - ph * va * (Pc - Pb) / D), "Eq 17 solves Eqs 14-16")
sym("ch11", 39, lambda: zero(s3[pb] - ph * vb * (Pa - Pc) / D), "Eq 18 solves Eqs 14-16")
sym("ch11", 40, lambda: zero(s3[pc] - ph * vc * (Pb - Pa) / D), "Eq 19 solves Eqs 14-16")
defn("ch11", 41, "Eq 20 determinant")
ref("ch11", [42, 43], "Delta = twice the triangle area in the P-nu plane (base (P_a - P_c)/cos(theta), height h)")
defn("ch11", 44, "Abbe number")
sym("ch11", 45, lambda: zero(s3[pa] / s3[pc] - (va / vc) * (Pc - Pb) / (Pb - Pa)), "ratio of Eqs 17 and 19")
ref("ch11", 46, "Eq 21 residual chromatic at a fourth wavelength (ch06 Eq 42 generalised)")
sym("ch11", [47, 48], lambda: zero((s3[pa] * Qa / va + s3[pb] * Qb / vb + s3[pc] * Qc / vc) / ph
                                   - (Qa * (Pc - Pb) + Qb * (Pa - Pc) + Qc * (Pb - Pa)) / D)
    and zero((Qa * (Pc - Pb) + Qb * (Pa - Pc) + Qc * (Pb - Pa)) - Matrix([[Pa, Qa, 1], [Pb, Qb, 1], [Pc, Qc, 1]]).det()),
    "Eq 22 = Eq 21 with Eqs 17-19 substituted; its numerator equals det[P*, P**, 1], the printed determinant form")
ref("ch11", 49, "OPD for a transverse error Y_k across the pupil: W = Y_k Y1/(2f') (defocus-type wavefront)")
