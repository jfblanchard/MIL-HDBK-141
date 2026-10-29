# Scientific Validation Report — Chapter 7: Simple Thin Lens Optical Systems

**Validator:** Independent (secondary) scientific check, per VALIDATOR_SYSTEM_PROMPT.md
**Date:** 2026-09-06
**Chapter OCR file:** ocr_output/ch07.md
**Status of review:** 18/18 items independently verified; no flags.

Method note: each equation was re-derived from first principles (ray-trace algebra, Newton's
equation, thin-lens chromatic surface contributions) and every numerical claim was recomputed
independently, including a full two-wavelength (F/C) paraxial trace used to independently
confirm the afocal chromatic aberration values.

---

## EQUATIONS

```
ITEM: Eq. (1) — Simple magnifier MP = -(V/A)[1 - phi(d+A)]
STATUS: PASS
FINDING: Confirmed. Transverse magnification for the magnifier is m = v/u = 1 - phi(d+A)
(v = d+A, signed), giving MP = beta/alpha = (y_k/A)/(-y_o/V) = -(V/A)[1 - phi(d+A)].
Matches the ray-trace derivation y_k = y_o[1 - phi(d+A)] and MP = beta/alpha.
```

```
ITEM: Eq. (1) special cases a) A=-inf, b) d=f'=1/phi, c) A=-V, d=0
STATUS: PASS
FINDING: All three verified. (a) MP -> V*phi; (b) bracket becomes 1-phi(1/phi+A) = -phi*A,
giving V*phi; (c) MP = (V/V)[1+phi*V] = 1+V*phi. Computed 9.84 for the 25.4 mm example.
```

```
ITEM: Eq. (2) — Microscope MP = m_o * V/f_e
STATUS: PASS
FINDING: Standard afocal microscope form; eyepiece magnifying power V/f_e times objective
lateral magnification m_o (negative for a real intermediate image). No issue.
```

```
ITEM: f-number = 0.5/|Delta u|
STATUS: PASS
FINDING: From Delta u = -y*phi = -y/f' with y = D/2: |Delta u| = D/(2f'), so
0.5/|Delta u| = f'/D. Correct. The stated caveat that this gives the working f-number for
finite conjugates (not necessarily f'/D) is sound.
```

```
ITEM: Eqs. (3) and (4) — afocal chromatic aberrations
STATUS: PASS
FINDING: Verified via an independent two-wavelength trace. For the afocal microscope,
d(u_5) = du_3 - d(y_4*phi_e) = -0.00458 - (-0.03727) = +0.0327 rad, matching
alpha*TAch = sum(a)/(y_k*n) = -0.02043/(-0.625) = 0.0327. Likewise the emergent chief-ray
angular color computes to +0.0076 rad, matching alpha*Tch = 0.0076. The use of y_k (axial
ray at exit surface), not y_k-chief, is correct: the two-wavelength trace shows the dominant
term is d(y_4*phi_e) driven by the axial-ray height, so y_k is the right normalizing quantity.
```

```
ITEM: Eq. (5) — Telescope MP = -(f_o/f_e')*(L/z) = m_o*L/f_e'
STATUS: PASS
FINDING: Correct in magnitude and physically self-consistent. m_o = -f_o/z follows from
Newton's equation m = -f/x with x = z; the negative sign correctly encodes the inverted
(astronomical) image. The sign differs from a naive beta/alpha derivation only by field-angle
sign convention, not by physics; the book's convention is internally consistent. L/z -> 1 as
L -> infinity is verified (z = L - f_o).
```

```
ITEM: Image erection rule (odd/even number of real images)
STATUS: PASS
FINDING: Correct. Each real-image relay stage contributes a negative lateral magnification;
an odd number of negative factors gives MP < 0 (inverted), even gives MP > 0 (erect).
```

```
ITEM: Galilean telescope FOV equations, beta ~= 1/[2(f/#)_o], alpha ~= beta/MP
STATUS: PASS
FINDING: Verified. For MP=10, f/3: alpha = 1/(10*2*3) = 0.0167 rad = 0.955 deg (~0.95 deg),
beta = 10*alpha = 9.55 deg (~9.5 deg). Also consistent with the f/1 case in the text
(alpha = 0.05 rad).
```

---

## GEMS

```
ITEM: Gem 7.1 — Simple magnifier MP limits
STATUS: PASS
FINDING: MP_min = V/f' and MP_max = V/f' + 1 are the correct limiting cases of Eq. (1)
(A = -inf and A = -V with d = 0). V = 250 mm, 25 mm -> 10x, 5 mm -> 50x all recomputed
correct. Design-for-infinity guidance is sound and matches the chapter.
```

```
ITEM: Gem 7.2 — f-number from paraxial trace
STATUS: PASS
FINDING: Table values independently recomputed: objective axial 0.5/0.275 = 1.82; objective
oblique infinity (y_2-bar = 0, chief ray through center, no bending); eyelens axial
0.5/0.025 = 20; eyelens oblique 0.5/0.4568 = 1.09. The "working vs paraxial f-number" caveat
and the split-lens rule (each sub-element at N x the single-lens f-number, e.g. 0.1375 each
-> f/3.64) are both correct.
```

```
ITEM: Gem 7.3 — Symmetric field lens cancels lateral color
STATUS: PASS
FINDING: Mechanism verified numerically. With the table sign convention b_j = -y*y_bar*phi/nu
(equivalent to b proportional to y*y_bar*Delta(1/nu)): b_3 = -0.00238 and b_4 = +0.00238,
sum = 0 exactly, so alpha*Tch = 0. Trade-off claims (eye relief reduced by factor ~3,
TAch 0.0327 -> 0.0332, reticle plane not color-corrected) all match the chapter and are
correct. The Ramsden/Kellner attribution is accurate.
```

---

## SUMMARY

```
ITEM: Chapter 7 summary (scope, equations, tables, key results)
STATUS: PASS
FINDING: Accurately represents the chapter. All major topics are present: simple magnifier
(Eq. 1, MP limits, design rule), microscope (Eq. 2, f-number, afocal chromatic Eqs. 3-4,
field-lens lateral color cancellation), telescope (Eq. 5, erection rule), and Galilean
telescope (FOV dependence on objective f-number). 5 numbered equations, 7 figures, 5 tables
all correct. No major topic omitted.
```

---

## TABLES

```
ITEM: Table 7.1 — Simple magnifier computation sheet
STATUS: PASS
FINDING: Symbolic entries consistent with the ray-trace derivation leading to Eq. (1)
(y_2 = 1 normalization, u_2 = u_3 = -1/(d+A), u_1 = phi - 1/(d+A), y-bar_2 = -beta*d).
No scientific error detected.
```

```
ITEM: Table 7.2 — Simple afocal microscope trace
STATUS: PASS
FINDING: All spot-checks recomputed and correct: y_2 = 4.4, u_3 = -0.025, image distance
176.0 mm, m_o = -10, u_5 = 0 (afocal), exit pupil at 28.55 mm. a_j and b_j values follow the
chapter convention a_j = -y^2*phi/nu, b_j = -y*y_bar*phi/nu (both verified numerically).
Exit pupil radius 0.625 mm (1.25 mm dia) consistent.
```

```
ITEM: Table 7.3 — f-numbers
STATUS: PASS
FINDING: Objective 1.82 axial / infinity oblique; eyelens 20 axial / 1.09 oblique. All four
recomputed correctly. The restored Eyelens row (axial 20, oblique 1.09) is verified and
internally consistent.
```

```
ITEM: Table 7.4 — Afocal microscope with double-lens eyepiece
STATUS: PASS
FINDING: Entries verified. Note: the "-phi" column row means phi_3 = +0.02662 (a positive
field lens), and u_4 = -0.025 - 0.625*(+0.02662) = -0.04164, t_34 = 30.02, y-bar_4 = -3.428,
exit pupil t_45 = 8.571, sum(a) = -0.0208 -> alpha*TAch = 0.0332, and sum(b) = 0 -> alpha*Tch
= 0. All correct. Minor note on the validate prompt's B4 arithmetic: it read the "-phi" row
value (-0.02662) directly as the power and used b = y*y_bar*phi/nu; the table convention is
b = -y*y_bar*phi/nu with phi positive, but both sign treatments yield the same magnitudes
(|b_3| = |b_4| = 0.00238) and the same exact cancellation. This is a prompt-side sign
convention, not a chapter error.
```

```
ITEM: Table 7.5 — Galilean telescope computation sheet
STATUS: PASS
FINDING: Symbolic entries are consistent with the section-7.6 analysis (exit pupil = eye,
objective = field stop, t_2 = f_o' + f_e, y-bar_2 = beta[MP*d - t_2]). The table is
self-consistent with the FOV equations; no error found.
```

```
ITEM: Conceptual claims C1-C5 (10% MP gain; axial color 98.7% from objective; lateral color
entirely from eyelens; 0.0003 rad = 1'; eye relief factor ~3)
STATUS: PASS
FINDING: All confirmed. (C1) 10.84/9.84 = 1.102, ~10%. (C2) 0.02017/0.02043 = 98.7%; the
objective works at f/1.82 (large y^2*phi) so dominating axial color is physically expected.
(C3) b_obj = 0 because the entrance pupil is at the objective (y_2-bar = 0). (C4) 1 arcmin =
2.909e-4 rad ~ 0.0003 rad. (C5) 28.55/8.571 = 3.33, consistent with "factor of 3."
```

---

## Overall Assessment

High confidence in the scientific accuracy of Chapter 7. Every one of the 18 items — 9
formal equations, 3 gems, the chapter summary, 5 tables, and 5 conceptual claims — was
independently re-derived or recomputed and passed. The two most demanding checks both
succeeded: Eq. (1) reproduces the three standard magnifier limiting cases, and the afocal
chromatic formulas Eqs. (3)–(4) were confirmed by a full two-wavelength F/C paraxial trace
(emergent axial color +0.0327 rad, chief-ray color +0.0076 rad), which also validates the
use of the axial-ray height y_k (not the chief-ray height) in the denominator. All numerical
values in Tables 7.2–7.5 and the gems (f-numbers 1.82/20/1.09/infinity, exit pupils 28.55
and 8.571 mm, field-lens lateral color cancellation to zero, MP 9.84/10.84, Galilean angles
0.95 deg/9.5 deg) are correct to the reported precision. The only observations are not
content errors: (a) the "-phi" table rows denote the negative of the element power, so the
field lens is positive as expected; and (b) the validate prompt's B4 arithmetic used the
"-phi" value directly with b = y*y_bar*phi/nu, which happens to reproduce the table's values
because both sign conventions flip together. Neither affects the chapter's correctness.
No systemic issues, no fabricated values, and no misleading approximations were found.
The chapter can be accepted as scientifically verified.
