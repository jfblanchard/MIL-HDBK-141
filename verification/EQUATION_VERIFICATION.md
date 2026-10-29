# MIL-HDBK-141 Equation Verification Ledger

Every display equation (`$$...$$`) in `ocr_output/chNN.md`, checked from the transcribed LaTeX. Scan pages were opened only where a check disagreed with the text and the cause (transcription vs. 1962 print) had to be settled; those rows say `+ scan` in the method column.

Checks are executable: `verification/eq_verify/ck_chNN.py` (one module per chapter group), registry `ledger.py`, run with `env -u PYTHONPATH python run_all.py`; this file is written by `report.py`.

## Methods

- **symbolic (sympy)**: the equation is derived from its predecessors, or both sides are shown identical (symbolic zero, with a random-rational numeric fallback).
- **numeric (book values)**: the book's own worked numbers are recomputed; or, for ch21 coatings, the book's recursions are compared with an independent characteristic-matrix reference (`multilayer.py`, Macleod convention) on 12 random absorbing stacks at oblique incidence.
- **reference (standard form)**: checked term by term against the established textbook form.
- **definition**: defines a symbol, convention, or boundary condition; nothing to derive.

## Results

- **VERIFIED**: the check ran and the equation holds.
- **FIXED**: a transcription error found by the check, corrected against the scan in an earlier commit, and re-verified.
- **FLAG**: a real discrepancy. Notes marked `1962 ORIGINAL (sic ...)` are errors in the printed book, confirmed on the scan and kept as printed; notes marked `FIDELITY` are ch05 transcription paraphrases that do not match the book.
- **NOT VERIFIED**: no check possible from the text (reason given).

## Source corrections already committed (re-verified here)

- `0b840e3` ch06: A/B linearity coefficients, Eq 32 sign, Eq 33a, secondary-spectrum 1/2200 statement (6 rows, FIXED).
- `96b8d4b` ch16 Eq 167: restored `n` in the J1 argument denominator (row ch16-p51-207, FIXED).
- `fcc9a85` ch21: render fix only (duplicate `\tag` on Eq 113); no content change.

## Per-chapter summary

| ch | blocks | VERIFIED | FIXED | DEFINITION | FLAG | NOT VERIFIED |
|---|---|---|---|---|---|---|
| 02 | 14 | 9 | 0 | 5 | 0 | 0 |
| 03 | 41 | 20 | 0 | 21 | 0 | 0 |
| 04 | 1 | 1 | 0 | 0 | 0 | 0 |
| 05 | 57 | 27 | 0 | 5 | 8 | 17 |
| 06 | 89 | 79 | 6 | 4 | 0 | 0 |
| 07 | 22 | 20 | 0 | 2 | 0 | 0 |
| 08 | 75 | 70 | 0 | 5 | 0 | 0 |
| 09 | 40 | 35 | 0 | 5 | 0 | 0 |
| 10 | 37 | 27 | 0 | 10 | 0 | 0 |
| 11 | 49 | 38 | 0 | 10 | 0 | 1 |
| 12 | 6 | 6 | 0 | 0 | 0 | 0 |
| 13 | 70 | 52 | 0 | 14 | 4 | 0 |
| 14 | 1 | 1 | 0 | 0 | 0 | 0 |
| 15 | 3 | 3 | 0 | 0 | 0 | 0 |
| 16 | 259 | 159 | 1 | 89 | 10 | 0 |
| 17 | 19 | 16 | 0 | 1 | 1 | 1 |
| 18 | 4 | 3 | 0 | 1 | 0 | 0 |
| 19 | 12 | 8 | 0 | 3 | 1 | 0 |
| 20 | 73 | 53 | 0 | 19 | 1 | 0 |
| 21 | 458 | 339 | 0 | 107 | 8 | 4 |
| 22 | 21 | 14 | 0 | 7 | 0 | 0 |
| 23 | 10 | 6 | 0 | 4 | 0 | 0 |
| 24 | 7 | 5 | 0 | 0 | 1 | 1 |
| 25 | 18 | 15 | 0 | 1 | 0 | 2 |
| 26 | 13 | 7 | 0 | 6 | 0 | 0 |
| **all** | **1399** | **1013** | **7** | **319** | **34** | **26** |

## Errors in the 1962 original (kept as printed)

- `ch13-p32-065`: B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) (1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but D = B - 2(A + 2a) = 2.0823, 1.8072 (t/n shows these D are typos: D should equal t/n). Mismatches found: n=1.617 D printed 2.1822 computed 2.0823; n=1.617 t printed 3.3637 computed 3.367; n=1.617 tn printed 2.0802 computed 2.0823; n=1.72 D printed 1.9072 computed 1.8072
- `ch13-p32-066`: B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) (1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but D = B - 2(A + 2a) = 2.0823, 1.8072 (t/n shows these D are typos: D should equal t/n). Mismatches found: n=1.617 D printed 2.1822 computed 2.0823; n=1.617 t printed 3.3637 computed 3.367; n=1.617 tn printed 2.0802 computed 2.0823; n=1.72 D printed 1.9072 computed 1.8072
- `ch13-p32-067`: B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) (1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but D = B - 2(A + 2a) = 2.0823, 1.8072 (t/n shows these D are typos: D should equal t/n). Mismatches found: n=1.617 D printed 2.1822 computed 2.0823; n=1.617 t printed 3.3637 computed 3.367; n=1.617 tn printed 2.0802 computed 2.0823; n=1.72 D printed 1.9072 computed 1.8072
- `ch16-p23-078`: sign: solving Eq 68 with s = nu lambda/2 gives x^2 = R1 R2 nu lambda/(R2 - R1); the printed R1 - R2 is inconsistent with Eqs 68 and 70 (which uses R2 - R1). 1962 ORIGINAL (sic, scan p.16-23 prints R1 - R2): the text says Eq 69 reduces to Eq 67 as R2 -> infinity, which only R2 - R1 does
- `ch16-p28-110`: 1962 ORIGINAL (sic, scan p.16-28): the amplitude a is dropped from the sine term; a e^{i(phi - wt)} = a[cos + i sin]
- `ch16-p28-115`: 1962 ORIGINAL (sic, scan p.16-28): amplitude a dropped, as in Eq 94; E' = rho a e^{i(...)}
- `ch16-p32-137`: 1962 ORIGINAL (sic, scan p.16-32): exponent printed e^{(alpha - delta_1,0)} without the i; the sum otherwise follows from Eq 114 terms
- `ch16-p32-140`: 1962 ORIGINAL (sic, scan p.16-32): factoring r01 e^{i delta01} out of the previous line leaves C/r01, not C, inside the bracket (expanding the printed form gives r01 C e^{-i delta10} sum A^nu). The conclusion Eq 118 is unaffected
- `ch16-p53-218`: 1962 ORIGINAL (sic, scan p.16-53): Eqs 176-177 give r1 = sqrt(Q) - (x zeta + y eta - R z)/sqrt(Q), Q = R^2 + zeta^2 + eta^2; the printed denominator lacks the square root. Eq 179 uses the correct sqrt(Q)
- `ch16-p58-249`: 1962 ORIGINAL (sic, scan p.16-58): e^{iknz sqrt(1-rho^2)} ~ e^{iknz} e^{-i pi n z rho^2/lambda}; the book prints +i. Harmless: only |F0| is used afterwards
- `ch16-p58-250`: 1962 ORIGINAL (sic, scan p.16-58): integral of e^{i c rho^2} rho d rho = (e^{i c rho_m^2} - 1)/(2 i c), so F0(0) = pi e^{iknz}[...]/(i pi n z/lambda); the printed 2 pi doubles the amplitude (W 4x too large; in focus it must equal Eq 195's value pi^2 rho_m^4)
- `ch16-p58-251`: 1962 ORIGINAL (sic, scan p.16-58): integral of e^{i c rho^2} rho d rho = (e^{i c rho_m^2} - 1)/(2 i c), so F0(0) = pi e^{iknz}[...]/(i pi n z/lambda); the printed 2 pi doubles the amplitude (W 4x too large; in focus it must equal Eq 195's value pi^2 rho_m^4)
- `ch16-p58-255`: 1962 ORIGINAL (sic, scan p.16-58): Eq 210 at z = 0 gives 4 pi^2 rho_m^4, not the printed 4 pi rho_m^4 (and the correctly normalised in-focus value is pi^2 rho_m^4, see Eq 250). The ratio K (Eq 212) is unaffected
- `ch17-p02-009`: 1962 ORIGINAL (sic, as printed): misplaced parentheses; literal form gives T ~ 308 for the example. Eq 8 rearranges to the next line (verified symbolically), which gives T = 0.962 vs the text's 0.960
- `ch20-p74-068`: 1962 ORIGINAL (sic, scan p.20-74): printed as the product (lambda0/dlambda)(sigma0/dsigma); the footnote shows the two ratios are equal, so the product is Q^2. Read as Q = lambda0/dlambda = sigma0/dsigma = m pi sqrt(R)/(1-R): with R = 0.95, t = 1 cm, lambda = 0.55 um this gives Q = 2.23e+06, the text's 'over two million'
- `ch21-p14-090`: 1962 ORIGINAL (sic, scan p.21-14): the product's denominator is printed with e^{i beta_v/2}; Eq 53 (and the verified Eq 54) have e^{i beta_v}
- `ch21-p18-114`: Eq 71a as printed has n_1 in the denominator; setting K = 0 in Eq 71 gives n0 (n_a)_(N+1) cos i_(N+1)/(n_(N+1)^2 cos i0) |T/T0|^2, i.e. the substrate index n_(N+1), not n_1. 1962 ORIGINAL (sic, scan p.21-18 prints n_1)
- `ch21-p19-125`: 1962 ORIGINAL (sic, scan p.21-19): the first sum must be of W_v^2 (|sum W_v e^{i phi_v}|^2 expanded); with W_v^2 it equals |Eq 76|^2 exactly, while the printed sum of W_v gives -0.2048 instead of 0.0182 for a test stack
- `ch21-p21-140`: 1962 ORIGINAL (sic, scan p.21-21 prints -i): eliminating rho_(v-1) between Eqs 81 and 82 involves e^{+i beta}, so the recursion must read Y_(v-1) = M_(v-1)(Y_v + i M_(v-1) tan(beta_(v-1)/2))/(M_(v-1) + i Y_v tan(beta_(v-1)/2)). With +i it reproduces Eq 50 to 1e-15; the printed -i does not. The book applied the e^{-ix} identity where e^{+ix} is needed. (The p-case Eq 88a correctly has -i because Eq 85a uses the opposite sign convention.)
- `ch21-p23-163`: 1962 ORIGINAL (sic, scan p.21-23): from Eq 89 the product's denominator must be y_v + m_(v-1)^2/M_(v-1); the book prints /M_v
- `ch21-p49-370`: 1962 ORIGINAL (sic, scan p.21-49 prints 1 + W1 W2 e^{i beta_1}): Eq 50 requires 1 + W1 rho_1 e^{i beta_1}; the printed form holds only when rho_1 = W2 (the single-layer case)
- `ch21-p62-406`: 1962 ORIGINAL (sic, scan p.21-62 prints 2 rho_1 W_1^2 cos beta_1 in the denominator): |Eq 50|^2 for real rho_1, W_1 is (rho_1^2 + W_1^2 + 2 rho_1 W_1 cos beta_1)/(1 + rho_1^2 W_1^2 + 2 rho_1 W_1 cos beta_1); corrected form verified on 10 random cases
- `ch21-p64-418`: 1962 ORIGINAL (sic, scan p.21-64 prints beta1 = 199 deg 44' here and in the next paragraph): the second root of Eq 197b is 360 deg - 164 deg 16' = 195 deg 44'. With 195 deg 44' the pair (135 deg 24') gives exact R = 1.2e-06; with the printed 199 deg 44' it gives 1.5e-04. 13 deg 08' again satisfies Eq 197 only (R = 0.0118)
- `ch24-p03-006`: 1962 ORIGINAL (sic): U_m unprimed, inconsistent with Eqs 1-5 (U'_m); otherwise equals Eq 4

## Supplementary checks (book equations not present as display blocks)

| id | ch | method | result | notes |
|---|---|---|---|---|
| ch05-book-(1)-(15) | 05 | numeric (book Table 5.2) | VERIFIED | book's skew-ray Eqs (1)-(15) as printed on scan p.5-11 (optical cosines, H, B, A/n) reproduce every entry of the worked Table 5.2 (two surfaces, n = 1.62) to 2.3e-08 |
| ch08-book-Table-8.2-sums | 08 | numeric (full-precision recompute) | FLAG | 1962 ORIGINAL: printed Sigma C = -0.004200 and Sigma E = -0.002070 are sign-reversed; recompute gives +0.004199 and +0.002072 (positive E is the one that matches Fig 8.9). Printed y-bar_4 = +0.09189 is a dropped minus. Sigma a: full-precision sum -0.000407 agrees with the printed -0.00040 (the -0.00044 in the chapter's editorial note comes from adding the rounded row entries, so it is not a book slip) |

## Ledger

| Eq id | chapter | type | method | result | notes |
|---|---|---|---|---|---|
| ch02-p01-001 (1) | 02 | relation | reference (standard form) | VERIFIED | Snell's law, standard form |
| ch02-p02-002 | 02 | definition | reference (definition) | DEFINITION | cross product of unit vectors = sin of included angle |
| ch02-p02-003 | 02 | relation | symbolic (sympy) | VERIFIED | ratio follows from Eq 1 |
| ch02-p02-004 (2) | 02 | relation | reference (standard form) | VERIFIED | Eq 2: vector Snell's law n(Q x M) conserved; equivalent to Eq 1 for unit vectors |
| ch02-p02-005 | 02 | relation | reference (standard form) | VERIFIED | Eq 2 rewritten with S = nQ; difference vector crosses to zero with the normal |
| ch02-p02-006 | 02 | relation | reference (standard form) | VERIFIED | Eq 2 rewritten with S = nQ; difference vector crosses to zero with the normal |
| ch02-p03-007 (3) | 02 | definition | reference (definition) | DEFINITION | Eq 3: S1 - S0 parallel to the normal M1, factor Gamma |
| ch02-p03-008 (4) | 02 | relation | symbolic (sympy) | VERIFIED | Eq 4: n1 cos I' rewritten via Snell; both forms of Gamma agree |
| ch02-p04-009 (5) | 02 | relation | symbolic (sympy) | VERIFIED | Eq 5: with n1 = -n0 Snell gives I' = -I (reflection as refraction) |
| ch02-p04-010 (6) | 02 | definition | reference (definition) | DEFINITION | Eq 6: reflection convention n1 = -n0 |
| ch02-p04-011 (7) | 02 | relation | symbolic (sympy) | VERIFIED | Eq 7: critical angle is Snell with I' = 90 deg |
| ch02-p04-012 (8) | 02 | definition | reference (definition) | DEFINITION | Eq 8: absolute index = c / v |
| ch02-p04-013 | 02 | relation | symbolic (sympy) | VERIFIED | relative index algebra |
| ch02-p07-014 | 02 | definition | reference (definition) | DEFINITION | Abbe number definition (standard) |
| ch03-p02-001 (1) | 03 | definition | reference (definition) | DEFINITION | index = c / phase velocity |
| ch03-p02-002 (2) | 03 | relation | reference (standard form) | VERIFIED | v = nu*lambda = c/n, standard |
| ch03-p02-003 (3) | 03 | relation | symbolic (sympy) | VERIFIED | lambda = c/(n nu) = cT/n = lambda_0/n with T = 1/nu, lambda_0 = cT |
| ch03-p03-004 (4) | 03 | definition | reference (definition) | DEFINITION | plane-wave forms and phase definition |
| ch03-p03-005 (5) | 03 | definition | reference (definition) | DEFINITION | plane-wave forms and phase definition |
| ch03-p03-006 (6) | 03 | definition | reference (definition) | DEFINITION | plane-wave forms and phase definition |
| ch03-p03-007 (7) | 03 | definition | reference (definition) | DEFINITION | plane-wave forms and phase definition |
| ch03-p03-008 (8) | 03 | relation | symbolic (sympy) | VERIFIED | omega/(kn) = lambda/(nT) = c/n holds with k = 2 pi/lambda (vacuum lambda, as the chapter's symbol table defines); note Eq 3 uses the same letter for the in-medium wavelength |
| ch03-p03-009 (9) | 03 | definition | reference (definition) | DEFINITION | plane wave in direction cosines p,q,r |
| ch03-p03-010 (10) | 03 | definition | reference (definition) | DEFINITION | direction cosines sum of squares = 1 |
| ch03-p03-011 (11) | 03 | definition | reference (definition) | DEFINITION | plane wave in direction cosines p,q,r |
| ch03-p03-012 (12) | 03 | definition | reference (definition) | DEFINITION | plane wave in direction cosines p,q,r |
| ch03-p03-013 (13) | 03 | definition | reference (definition) | DEFINITION | instantaneous irradiance ~ E^2 |
| ch03-p04-014 (14) | 03 | relation | symbolic (sympy) | VERIFIED | cos^2 = (1+cos2x)/2 over one period |
| ch03-p04-015 (15) | 03 | relation | symbolic (sympy) | VERIFIED | integral over a period vanishes |
| ch03-p04-016 (16) | 03 | relation | symbolic (sympy) | VERIFIED | time average of a^2 cos^2 = a^2/2 |
| ch03-p05-017 (17) | 03 | definition | reference (definition) | DEFINITION | two-wave superposition set-up |
| ch03-p05-018 (18) | 03 | definition | reference (definition) | DEFINITION | two-wave superposition set-up |
| ch03-p05-019 (19) | 03 | definition | reference (definition) | DEFINITION | two-wave superposition set-up |
| ch03-p05-020 | 03 | definition | reference (definition) | DEFINITION | two-wave superposition set-up |
| ch03-p05-021 | 03 | relation | symbolic (sympy) | VERIFIED | expansion of time average of (E1+E2)^2; cross term = 2 a1 a2 I |
| ch03-p05-022 | 03 | relation | symbolic (sympy) | VERIFIED | expansion of time average of (E1+E2)^2; cross term = 2 a1 a2 I |
| ch03-p05-023 (20) | 03 | relation | symbolic (sympy) | VERIFIED | Eq 20 with I from Eq 23: full time average reproduced |
| ch03-p05-024 (21) | 03 | definition | reference (definition) | DEFINITION | Eq 21 definition of I |
| ch03-p05-025 (22) | 03 | relation | symbolic (sympy) | VERIFIED | product-to-sum identity |
| ch03-p05-026 | 03 | relation | symbolic (sympy) | VERIFIED | vanishes over a period |
| ch03-p05-027 (23) | 03 | relation | symbolic (sympy) | VERIFIED | I = cos(delta)/2 |
| ch03-p05-028 (24) | 03 | relation | symbolic (sympy) | VERIFIED | Eq 24 from Eqs 20, 23 |
| ch03-p05-029 (25) | 03 | relation | symbolic (sympy) | VERIFIED | delta = 0 |
| ch03-p05-030 (26) | 03 | relation | symbolic (sympy) | VERIFIED | delta = pi |
| ch03-p06-031 (27) | 03 | definition | reference (definition) | DEFINITION | incoherent average: mean of cos(delta) = 0 |
| ch03-p06-032 (28) | 03 | definition | reference (definition) | DEFINITION | incoherent average: mean of cos(delta) = 0 |
| ch03-p06-033 (29) | 03 | relation | symbolic (sympy) | VERIFIED | Eq 27 with Eq 28 |
| ch03-p06-034 (30) | 03 | definition | reference (definition) | DEFINITION | phases of the two plane waves (Fig 3.3) |
| ch03-p06-035 | 03 | definition | reference (definition) | DEFINITION | phases of the two plane waves (Fig 3.3) |
| ch03-p06-036 (31) | 03 | relation | symbolic (sympy) | VERIFIED | phase difference algebra |
| ch03-p06-037 (32) | 03 | definition | reference (definition) | DEFINITION | Eq 24 with delta -> Phi1 - Phi2 |
| ch03-p06-038 (33) | 03 | relation | symbolic (sympy) | VERIFIED | Eq 32 with Eq 31 substituted, times 2 |
| ch03-p07-039 (34) | 03 | relation | symbolic (sympy) | VERIFIED | small theta at z = 0: sin(theta) ~ theta, k = 2 pi/lambda |
| ch03-p07-040 | 03 | definition | reference (definition) | DEFINITION | fringe condition: phase advances by 2 pi |
| ch03-p07-041 (35) | 03 | relation | symbolic (sympy) | VERIFIED | fringe spacing h |
| ch04-p10-001 | 04 | relation | symbolic (sympy) | VERIFIED | trolands = (cd/m^2) x pupil area (mm^2); 1 mL = 10/pi cd/m^2, area = pi d^2/4 -> 5 d^2/2 exactly |
| ch05-p04-001 (1) | 05 | relation | numeric (book values) | VERIFIED | transfer to tangent plane: equivalent to book Eqs (1)-(3) (d/n = (t-Z)/M; K/M ratio is cosine-convention free); numerically identical to an exact straight-line transfer (20 random rays) |
| ch05-p04-002 (2) | 05 | relation | numeric (book values) | VERIFIED | transfer to tangent plane: equivalent to book Eqs (1)-(3) (d/n = (t-Z)/M; K/M ratio is cosine-convention free); numerically identical to an exact straight-line transfer (20 random rays) |
| ch05-p04-003 (3) | 05 | relation | numeric (book values) | VERIFIED | transfer to tangent plane: equivalent to book Eqs (1)-(3) (d/n = (t-Z)/M; K/M ratio is cosine-convention free); numerically identical to an exact straight-line transfer (20 random rays) |
| ch05-p04-004 | 05 | relation | symbolic (sympy) | VERIFIED | sphere sag, two forms (book p.5-13 prints the same pair) |
| ch05-p05-005 (4) | 05 | definition | reference (definition) | DEFINITION | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); auxiliary definitions F, G, eta, H (eta = G/r is never used) |
| ch05-p05-006 (5) | 05 | definition | reference (definition) | DEFINITION | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); auxiliary definitions F, G, eta, H (eta = G/r is never used) |
| ch05-p05-007 (6) | 05 | definition | reference (definition) | DEFINITION | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); auxiliary definitions F, G, eta, H (eta = G/r is never used) |
| ch05-p05-008 (7) | 05 | definition | reference (definition) | DEFINITION | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); auxiliary definitions F, G, eta, H (eta = G/r is never used) |
| ch05-p05-009 (8) | 05 | relation | numeric (exact vector trace, 20 random rays) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); Delta = H^2 - (M^2-1)(1-G/r^2) does NOT give the sphere intersection; correct form for a z-distance is D = M r (H - sqrt(H^2 - G/r^2)) (derived: s^2 - 2s(rM - F) + G = 0). Book instead uses Eqs (7)-(10) with B, H, A/n. |
| ch05-p05-010 (9) | 05 | relation | numeric (exact vector trace, 20 random rays) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); Delta = H^2 - (M^2-1)(1-G/r^2) does NOT give the sphere intersection; correct form for a z-distance is D = M r (H - sqrt(H^2 - G/r^2)) (derived: s^2 - 2s(rM - F) + G = 0). Book instead uses Eqs (7)-(10) with B, H, A/n. |
| ch05-p05-011 (10) | 05 | relation | numeric (book values) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); transfer tangent plane -> sphere along the ray (same straight-line form) |
| ch05-p06-012 (11) | 05 | relation | numeric (exact vector trace) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); unit normal (-X/r, -Y/r, 1 - Z/r) is correct (\|N\| = 1 verified on 20 rays) |
| ch05-p06-013 (12) | 05 | relation | numeric (exact vector trace) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); sign: with the normal of Eq 11 pointing to the centre, K.N > 0 for a ray meeting a convex (r>0) surface, so cos I = -(K alpha + L beta + M gamma) is negative; book's Eq (7) computes n cos I directly from B and H |
| ch05-p06-014 (13) | 05 | relation | numeric (exact vector trace) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); with geometric cosines (Eq 31: K^2+L^2+M^2 = 1) the refraction law needs Gamma/n_1, not Gamma: \|u1\| != 1 on 20 random rays. Book's Eqs (13)-(15) use optical cosines (K = n cos) where K = K_-1 - X c Gamma is correct |
| ch05-p06-015 (14) | 05 | relation | numeric (exact vector trace) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); with geometric cosines (Eq 31: K^2+L^2+M^2 = 1) the refraction law needs Gamma/n_1, not Gamma: \|u1\| != 1 on 20 random rays. Book's Eqs (13)-(15) use optical cosines (K = n cos) where K = K_-1 - X c Gamma is correct |
| ch05-p06-016 (15) | 05 | relation | numeric (exact vector trace) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); with geometric cosines (Eq 31: K^2+L^2+M^2 = 1) the refraction law needs Gamma/n_1, not Gamma: \|u1\| != 1 on 20 random rays. Book's Eqs (13)-(15) use optical cosines (K = n cos) where K = K_-1 - X c Gamma is correct |
| ch05-p06-017 | 05 | relation | symbolic (sympy) | VERIFIED | Gamma and cos I' from Snell; equals book Eq (11)/(12) rearranged |
| ch05-p08-018 (16) | 05 | relation | reference (standard form) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); aspheric sag, standard even-polynomial form (book p.5-13/5-14 uses the same deformation terms) |
| ch05-p08-019 (17) | 05 | relation | symbolic (sympy) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); B = (1/S) dZ/dS confirmed (book's E = c + W[...] is the same quantity times W) |
| ch05-p08-020 (18) | 05 | relation | symbolic (sympy) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); gradient and unit normal of z = Z(S): dZ/dX = B X, \|(-BX,-BY,1)\| = sqrt(B^2 S^2 + 1); standard |
| ch05-p08-021 (19) | 05 | relation | symbolic (sympy) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); gradient and unit normal of z = Z(S): dZ/dX = B X, \|(-BX,-BY,1)\| = sqrt(B^2 S^2 + 1); standard |
| ch05-p08-022 (20) | 05 | relation | symbolic (sympy) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); gradient and unit normal of z = Z(S): dZ/dX = B X, \|(-BX,-BY,1)\| = sqrt(B^2 S^2 + 1); standard |
| ch05-p09-023 (21) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-024 (22) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-025 (23) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-026 (24) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-027 (25) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-028 (26) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-029 (27) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); iteration scheme not in the book (book iterates with Eqs 16-25 and Table 5.4); no worked numbers to check |
| ch05-p09-030 (28) | 05 | relation | reference (standard form) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); same as transcription Eqs 13-15 (see flag there) |
| ch05-p09-031 (29) | 05 | relation | reference (standard form) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); same as transcription Eqs 13-15 (see flag there) |
| ch05-p09-032 (30) | 05 | relation | reference (standard form) | VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); same as transcription Eqs 13-15 (see flag there) |
| ch05-p09-033 (31) | 05 | definition | reference (definition) | DEFINITION | unit direction vector |
| ch05-p09-034 (32) | 05 | relation | symbolic (sympy) | VERIFIED | cos I' from Snell's law |
| ch05-p11-035 (33) | 05 | relation | numeric (sign test) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); sign conventions inconsistent: Eq 33 X_new = X + t tan U needs U > 0 for a rising ray, but Eq 34 sin I = (X/r)cos U - sin U gives I = 0 for a ray aimed at the centre only if U > 0 for a FALLING ray |
| ch05-p11-036 (34) | 05 | relation | numeric (sign test) | FLAG | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); sign conventions inconsistent: Eq 33 X_new = X + t tan U needs U > 0 for a rising ray, but Eq 34 sin I = (X/r)cos U - sin U gives I = 0 for a ray aimed at the centre only if U > 0 for a FALLING ray |
| ch05-p11-037 (35) | 05 | relation | reference (standard form) | VERIFIED | Snell; U' = U - (I - I') is the standard slope-angle update |
| ch05-p11-038 (36) | 05 | relation | reference (standard form) | VERIFIED | Snell; U' = U - (I - I') is the standard slope-angle update |
| ch05-p12-039 (37) | 05 | relation | reference (standard form) | VERIFIED | axial intercept of the emergent ray; LSA definition |
| ch05-p12-040 (38) | 05 | relation | reference (standard form) | VERIFIED | axial intercept of the emergent ray; LSA definition |
| ch05-p13-041 (39) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); 'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term |
| ch05-p13-042 (40) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); 'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term |
| ch05-p13-043 (41) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); 'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term |
| ch05-p13-044 (42) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); 'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term |
| ch05-p13-045 (43) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); 'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term |
| ch05-p13-046 (44) | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); 'PR' meridional scheme; book's Section 5.6.5 method (Fig 5.12) not compared term by term |
| ch05-p17-047 (45) | 05 | relation | reference (standard form) | VERIFIED | Coddington sagittal/tangential equations, standard form (sign convention: distances D measured opposite for object) |
| ch05-p17-048 (46) | 05 | relation | reference (standard form) | VERIFIED | Coddington sagittal/tangential equations, standard form (sign convention: distances D measured opposite for object) |
| ch05-p17-049 (47) | 05 | relation | reference (standard form) | VERIFIED | transfer of Coddington distances |
| ch05-p17-050 (48) | 05 | relation | reference (standard form) | VERIFIED | transfer of Coddington distances |
| ch05-p18-051 (56) | 05 | relation | reference (standard form) | VERIFIED | paraxial transfer y_k = y_{k-1} + t u (n cancels) |
| ch05-p18-052 (57) | 05 | relation | reference (standard form) | VERIFIED | paraxial refraction (nu)' = nu - y phi, phi = c (n' - n); standard |
| ch05-p18-053 | 05 | relation | reference (standard form) | VERIFIED | paraxial refraction (nu)' = nu - y phi, phi = c (n' - n); standard |
| ch05-p38-054 | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); duplicate of Eqs 39-44 in a summary box; not verified (see there) |
| ch05-p38-055 | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); duplicate of Eqs 39-44 in a summary box; not verified (see there) |
| ch05-p38-056 | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); duplicate of Eqs 39-44 in a summary box; not verified (see there) |
| ch05-p38-057 | 05 | relation | none | NOT VERIFIED | FIDELITY: paraphrase, not the book's equation/numbering (scan p.5-6..5-22); duplicate of Eqs 39-44 in a summary box; not verified (see there) |
| ch06-p02-001 (5-56) | 06 | relation | numeric (book values) | VERIFIED | transfer/refraction Eqs 5-56, 5-57 reproduce every entry of Table 6.6 (image y = 3e-7) |
| ch06-p02-002 (5-57) | 06 | relation | numeric (book values) | VERIFIED | transfer/refraction Eqs 5-56, 5-57 reproduce every entry of Table 6.6 (image y = 3e-7) |
| ch06-p02-003 (1) | 06 | relation | numeric (book values) | VERIFIED | Eq 1 with the book's example c=0.10, n=1->1.5, t0=10: 1.5/t1 = 0.05 - 0.1 -> t1 = -30 (book: -30) |
| ch06-p04-004 (2) | 06 | relation | numeric (book values) | VERIFIED | Eq 2 transfer (Table 6.6) |
| ch06-p04-005 (3) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 3 with Eq 4 (i = yc + u_-1) equals the refraction Eq 5-57 divided by n |
| ch06-p04-006 (4) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 3 with Eq 4 (i = yc + u_-1) equals the refraction Eq 5-57 divided by n |
| ch06-p05-007 (5-57a) | 06 | relation | numeric (book values) | VERIFIED | Eqs 5-56a/b, 5-57a/b: chief ray reproduces Table 6.6 (y-bar_7 = 5.77084) |
| ch06-p05-008 (5-57b) | 06 | relation | numeric (book values) | VERIFIED | Eqs 5-56a/b, 5-57a/b: chief ray reproduces Table 6.6 (y-bar_7 = 5.77084) |
| ch06-p05-009 (5-56a) | 06 | relation | numeric (book values) | VERIFIED | Eqs 5-56a/b, 5-57a/b: chief ray reproduces Table 6.6 (y-bar_7 = 5.77084) |
| ch06-p05-010 (5-56b) | 06 | relation | numeric (book values) | VERIFIED | Eqs 5-56a/b, 5-57a/b: chief ray reproduces Table 6.6 (y-bar_7 = 5.77084) |
| ch06-p06-011 (6) | 06 | relation | numeric (book values) | VERIFIED | Lagrange invariant Phi = y-bar(nu) - y(n u-bar) = -0.50000 at every surface of Table 6.6 |
| ch06-p06-012 | 06 | relation | numeric (book values) | VERIFIED | Lagrange invariant Phi = y-bar(nu) - y(n u-bar) = -0.50000 at every surface of Table 6.6 |
| ch06-p06-013 (5) | 06 | relation | numeric (book values) | VERIFIED | Lagrange invariant Phi = y-bar(nu) - y(n u-bar) = -0.50000 at every surface of Table 6.6 |
| ch06-p06-014 | 06 | relation | numeric (book values) | VERIFIED | Lagrange invariant Phi = y-bar(nu) - y(n u-bar) = -0.50000 at every surface of Table 6.6 |
| ch06-p06-015 | 06 | relation | numeric (book values) | VERIFIED | Phi at object (y0 = 0) = at image (y_k = 0) |
| ch06-p06-016 (7) | 06 | relation | numeric (book values) | VERIFIED | Eq 7: m = y-bar_k/y-bar_0 = n0u0/(n u)_{k-1} = -0.57708 (book, Table 6.6) |
| ch06-p07-017 | 06 | relation | numeric (book values) | VERIFIED | Eq 8: with y-bar_1 = 0, y-bar_k = -y1 (n0 u-bar0)/(n u)_{k-1}, checked on Table 6.6 with u-bar0 = 0.4 |
| ch06-p07-018 (8) | 06 | relation | numeric (book values) | VERIFIED | Eq 8: with y-bar_1 = 0, y-bar_k = -y1 (n0 u-bar0)/(n u)_{k-1}, checked on Table 6.6 with u-bar0 = 0.4 |
| ch06-p07-019 | 06 | relation | numeric (book values) | VERIFIED | Eq 9 / Smith-Helmholtz: invariant -y1 n0 u-bar0 conserved at every surface (so alpha = y1 n0/(y_k n_{k-1}) at the exit pupil) |
| ch06-p07-020 (9) | 06 | relation | numeric (book values) | VERIFIED | Eq 9 / Smith-Helmholtz: invariant -y1 n0 u-bar0 conserved at every surface (so alpha = y1 n0/(y_k n_{k-1}) at the exit pupil) |
| ch06-p07-021 | 06 | relation | numeric (book values) | VERIFIED | Eq 9 / Smith-Helmholtz: invariant -y1 n0 u-bar0 conserved at every surface (so alpha = y1 n0/(y_k n_{k-1}) at the exit pupil) |
| ch06-p07-022 | 06 | relation | numeric (book values) | VERIFIED | Eq 9 / Smith-Helmholtz: invariant -y1 n0 u-bar0 conserved at every surface (so alpha = y1 n0/(y_k n_{k-1}) at the exit pupil) |
| ch06-p08-023 (10a) | 06 | relation | numeric (book values) | VERIFIED | Eqs 10a/10b: a third ray (y0=3, nu0=-0.11) equals A*chief + B*axial at every surface |
| ch06-p08-024 (10b) | 06 | relation | numeric (book values) | VERIFIED | Eqs 10a/10b: a third ray (y0=3, nu0=-0.11) equals A*chief + B*axial at every surface |
| ch06-p08-025 | 06 | relation | numeric + scan | FIXED | transcription error, FIXED per scan p.6-9: numerator read (y-bar u - y u-bar), which makes A = 1; book prints A = (y~ u - u~ y)/(y-bar u - u-bar y) = n(y~ u - u~ y)/Phi; the invented tag 'from Eq. 28' removed. Fixed form checked numerically |
| ch06-p08-026 | 06 | relation | numeric (book values) | VERIFIED | A and B forms of p.6-9, evaluated at the object plane for the Eq 10 test ray, reproduce the A, B that fit it at every surface |
| ch06-p08-027 (11) | 06 | relation | numeric + scan | FIXED | transcription error, FIXED per scan p.6-10: the third ray's tilde was dropped (A = y-bar0/y-bar0 = 1). Book: A = y~0/y-bar0, B = y~1/y1 (11) and B = -y~1 u-bar0/(y-bar0 u0) (12); fixed forms verified with the Eq 10 ray |
| ch06-p08-028 (12) | 06 | relation | numeric + scan | FIXED | transcription error, FIXED per scan p.6-10: the third ray's tilde was dropped (A = y-bar0/y-bar0 = 1). Book: A = y~0/y-bar0, B = y~1/y1 (11) and B = -y~1 u-bar0/(y-bar0 u0) (12); fixed forms verified with the Eq 10 ray |
| ch06-p10-029 (13) | 06 | relation | numeric (book values) | VERIFIED | Eq 13: f' = -y1/u_(k-1) = 9.9999 for Table 6.6 (book: 10.000) |
| ch06-p10-030 | 06 | relation | reference (standard form) | VERIFIED | nodal/principal geometry: N2F2 = f' n0/n_(k-1) (n0 = n_(k-1) = 1 here) |
| ch06-p10-031 | 06 | relation | reference (standard form) | VERIFIED | nodal/principal geometry: N2F2 = f' n0/n_(k-1) (n0 = n_(k-1) = 1 here) |
| ch06-p10-032 (14) | 06 | relation | reference (standard form) | VERIFIED | Eq 14 front focal length from a ray emerging parallel (reverse of Eq 13) |
| ch06-p14-033 (15) | 06 | relation | symbolic (sympy) | VERIFIED | Newton: m = -Z'/f' = -f/Z with ZZ' = ff' |
| ch06-p14-034 (16) | 06 | relation | symbolic (sympy) | VERIFIED | Newton: m = -Z'/f' = -f/Z with ZZ' = ff' |
| ch06-p14-035 (17) | 06 | relation | symbolic (sympy) | VERIFIED | Gauss form follows from Newton with Z = S - f |
| ch06-p14-036 (18) | 06 | relation | symbolic (sympy) | VERIFIED | m = -fS'/(f'S) equals Newton m |
| ch06-p14-037 (19) | 06 | relation | reference (standard form) | VERIFIED | f/n0 = f'/n_(k-1); principal/nodal separations; standard |
| ch06-p14-038 | 06 | relation | reference (standard form) | VERIFIED | f/n0 = f'/n_(k-1); principal/nodal separations; standard |
| ch06-p16-039 (20) | 06 | relation | numeric (book values) | VERIFIED | Eq 20 with Table 6.6: 0.5/(0.05 x 0.35886 + 0.37 x 0.08664) = 10.000 (book 10.000) |
| ch06-p17-040 | 06 | relation | reference (standard form) | VERIFIED | thin lens in air: 1/S + 1/S' = 1/f' (book sign convention), m = -S'/S |
| ch06-p17-041 | 06 | relation | reference (standard form) | VERIFIED | thin lens in air: 1/S + 1/S' = 1/f' (book sign convention), m = -S'/S |
| ch06-p17-042 (21) | 06 | relation | symbolic (sympy) | VERIFIED | thin lens: two refractions with zero thickness give u2 = u0 - y(n-1)(c1-c2); phi = (n-1)(c1-c2) |
| ch06-p17-043 (22) | 06 | relation | symbolic (sympy) | VERIFIED | thin lens: two refractions with zero thickness give u2 = u0 - y(n-1)(c1-c2); phi = (n-1)(c1-c2) |
| ch06-p17-044 (23) | 06 | relation | reference (standard form) | VERIFIED | thin-lens transfer/refraction y = y_-1 + t u, u = u_-1 - y phi |
| ch06-p17-045 (24) | 06 | relation | reference (standard form) | VERIFIED | thin-lens transfer/refraction y = y_-1 + t u, u = u_-1 - y phi |
| ch06-p18-046 | 06 | relation | symbolic (sympy) | VERIFIED | two thin lenses: trace y=1,u=0 through both: phi = phi_a + phi_b - d phi_a phi_b |
| ch06-p18-047 | 06 | definition | reference (definition) | DEFINITION | mirror convention n_+1 = -n |
| ch06-p20-048 (25) | 06 | relation | numeric (book values) | VERIFIED | Eq 25 mirror: book example r = -10, t0 = 20 gives t1 = -20/3 (book: -20/3) |
| ch06-p22-049 (from~Eq.~13) | 06 | relation | numeric (book values) | VERIFIED | mirror f' = r/2 (trace of Table 6.11: nu = 2c, f' = -y1 n_(k-1)/(n u)); the transcription's n0 r/2 is not printed in the book and agrees only because the book takes n0 = 1 |
| ch06-p22-050 (26) | 06 | relation | reference (standard form) | VERIFIED | total differentials of the image-plane height and final angle |
| ch06-p22-051 (27) | 06 | relation | reference (standard form) | VERIFIED | total differentials of the image-plane height and final angle |
| ch06-p23-052 (28) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 28 from linearity (perturbation = A chief + B axial) |
| ch06-p23-053 (29) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 29 from linearity |
| ch06-p23-054 (30) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 30 from linearity |
| ch06-p23-055 (31) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 31 from linearity |
| ch06-p23-056 (32) | 06 | relation | symbolic (sympy) + scan | FIXED | transcription error, FIXED per scan p.6-24: sign of the bracket was reversed; book prints dy_k = (n/Phi)(y_k y-bar - y-bar_k y) du, which is Eq 29 x du (verified symbolically) |
| ch06-p23-057 (33) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 33 = Eq 31 x du |
| ch06-p23-058 | 06 | relation | numeric (book values) | VERIFIED | df'/dc: chain rule of Eq 13 with Eq 33 and du/dc = y(n_-1 - n)/n; its core du_(k-1)/dc matches a finite-difference retrace of Table 6.6 |
| ch06-p24-059 | 06 | relation | numeric (book values) | VERIFIED | du6/dc4 by finite-difference retrace of Table 6.6 = 0.4693; book 0.469 |
| ch06-p24-060 | 06 | worked example | numeric (book values) | VERIFIED | 0.469 x 0.01 = 0.00469 |
| ch06-p24-061 | 06 | relation | symbolic (sympy) | VERIFIED | du/dt: Eq 30 with dy = u dt (matches scan p.6-25) |
| ch06-p26-062 (33a) | 06 | relation | reference + scan | FIXED | transcription error, FIXED per scan p.6-26: book prints i' = yc + u (refracted-side angle); transcription had u_-1 |
| ch06-p26-063 | 06 | relation | symbolic (sympy) | VERIFIED | differentiating Eq 5-57 at fixed u_-1, y: du = i (n_-1/n)[dn_-1/n_-1 - dn/n] with i = yc + u_-1 |
| ch06-p26-064 (34) | 06 | relation | numeric (book values) | VERIFIED | Eq 34 (Delta = after minus before) surface sum of y n_-1 i Delta(dn/n)/(n u)_(k-1) equals the image-height change from a full retrace of Table 6.6 with dispersed indices (first order, 2%); Eqs 35-38 are the chief-ray and summed forms of the same expression |
| ch06-p26-065 (35) | 06 | relation | numeric (book values) | VERIFIED | Eq 34 (Delta = after minus before) surface sum of y n_-1 i Delta(dn/n)/(n u)_(k-1) equals the image-height change from a full retrace of Table 6.6 with dispersed indices (first order, 2%); Eqs 35-38 are the chief-ray and summed forms of the same expression |
| ch06-p26-066 (36) | 06 | relation | numeric (book values) | VERIFIED | Eq 34 (Delta = after minus before) surface sum of y n_-1 i Delta(dn/n)/(n u)_(k-1) equals the image-height change from a full retrace of Table 6.6 with dispersed indices (first order, 2%); Eqs 35-38 are the chief-ray and summed forms of the same expression |
| ch06-p26-067 (37) | 06 | relation | numeric (book values) | VERIFIED | Eq 34 (Delta = after minus before) surface sum of y n_-1 i Delta(dn/n)/(n u)_(k-1) equals the image-height change from a full retrace of Table 6.6 with dispersed indices (first order, 2%); Eqs 35-38 are the chief-ray and summed forms of the same expression |
| ch06-p26-068 (38) | 06 | relation | numeric (book values) | VERIFIED | Eq 34 (Delta = after minus before) surface sum of y n_-1 i Delta(dn/n)/(n u)_(k-1) equals the image-height change from a full retrace of Table 6.6 with dispersed indices (first order, 2%); Eqs 35-38 are the chief-ray and summed forms of the same expression |
| ch06-p27-069 | 06 | relation | reference (standard form) | VERIFIED | definition of TAch/Tch as differences of y_k at two wavelengths |
| ch06-p27-070 | 06 | definition | reference (definition) | DEFINITION | wavelength labels (v = F, g = D, r = C) |
| ch06-p27-071 (from Fig.~6.14) | 06 | relation | reference (standard form) | VERIFIED | transverse = longitudinal x final angle, u_(k-1) = -y1/f' |
| ch06-p27-072 (39) | 06 | relation | reference (standard form) | VERIFIED | stop-shift form Tch* = Tch + Q TAch |
| ch06-p30-073 (from~Eq.~40) | 06 | relation | reference (standard form) | VERIFIED | thin-lens chromatic sums, match scan p.6-33 (Eqs 40-42) term by term |
| ch06-p30-074 (from~Eq.~41) | 06 | relation | reference (standard form) | VERIFIED | thin-lens chromatic sums, match scan p.6-33 (Eqs 40-42) term by term |
| ch06-p30-075 (40) | 06 | relation | reference (standard form) | VERIFIED | thin-lens chromatic sums, match scan p.6-33 (Eqs 40-42) term by term |
| ch06-p30-076 (41) | 06 | relation | reference (standard form) | VERIFIED | thin-lens chromatic sums, match scan p.6-33 (Eqs 40-42) term by term |
| ch06-p30-077 (42) | 06 | relation | reference (standard form) | VERIFIED | thin-lens chromatic sums, match scan p.6-33 (Eqs 40-42) term by term |
| ch06-p30-078 (43) | 06 | definition | reference (definition) | DEFINITION | Eq 43 achromatism condition |
| ch06-p30-079 (44) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 44 solves phi_a + phi_b = phi with Eq 43 |
| ch06-p30-080 (45) | 06 | relation | symbolic (sympy) | VERIFIED | Eq 45 |
| ch06-p33-081 (46) | 06 | definition | reference (definition) | DEFINITION | Eq 46 nu-number between v and r |
| ch06-p33-082 (49) | 06 | relation | reference (standard form) | VERIFIED | Eqs 48, 49 match scan p.6-36 (partial dispersion P~ and secondary-spectrum TAch) |
| ch06-p33-083 (48) | 06 | relation | reference (standard form) | VERIFIED | Eqs 48, 49 match scan p.6-36 (partial dispersion P~ and secondary-spectrum TAch) |
| ch06-p33-084 | 06 | relation | reference + scan | FIXED | transcription error, FIXED per scan p.6-36 (display replaced by the book statement): scan says (P~a - P~b)/(nu_a - nu_b) ~ -1/2200 for ordinary glasses, so TAch ~ y/(2200 n) and D light focuses f'/2200 closer; the transcription's 'TAch ~ y1/2200 ~ f'/2200' equates a height with a focal shift |
| ch06-p38-085 | 06 | relation | reference (standard form) | VERIFIED | summary box: restates Eqs 5-56, 5-57, 10a/b (verified above) |
| ch06-p38-086 | 06 | relation | reference (standard form) | VERIFIED | summary box: restates Eqs 5-56, 5-57, 10a/b (verified above) |
| ch06-p38-087 | 06 | relation | reference (standard form) | VERIFIED | summary box: restates Eqs 5-56, 5-57, 10a/b (verified above) |
| ch06-p38-088 | 06 | relation | reference (standard form) | VERIFIED | summary box: restates Eqs 5-56, 5-57, 10a/b (verified above) |
| ch06-p38-089 | 06 | relation | reference (standard form) | VERIFIED | summary box: restates Eqs 5-56, 5-57, 10a/b (verified above) |
| ch07-p01-001 | 07 | definition | reference (definition) | DEFINITION | definition of magnifying power |
| ch07-p03-002 | 07 | relation | reference (standard form) | VERIFIED | Lagrange invariant with n = 1 (ch06 Eq 7), verified numerically in ch06 |
| ch07-p03-003 | 07 | relation | symbolic (sympy) | VERIFIED | thin-lens magnification m = s'/s = 1 - phi s' with s' = d + A (image distance from lens) |
| ch07-p03-004 | 07 | definition | reference (definition) | DEFINITION | angles subtended at the eye with and without the instrument |
| ch07-p03-005 (1) | 07 | relation | symbolic (sympy) | VERIFIED | Eq 1 = beta/alpha from the two preceding lines |
| ch07-p04-006 (2) | 07 | relation | reference (standard form) | VERIFIED | Eq 2 compound microscope MP = m_o V/f_e, standard |
| ch07-p04-007 | 07 | relation | symbolic (sympy) | VERIFIED | f-number = f/(2y) = 0.5/u for u = y/f |
| ch07-p06-008 (3) | 07 | relation | reference (standard form) | VERIFIED | afocal form of the ch06 chromatic sums (Eqs 6-37, 6-38) with final angle replacing final height |
| ch07-p06-009 (4) | 07 | relation | reference (standard form) | VERIFIED | afocal form of the ch06 chromatic sums (Eqs 6-37, 6-38) with final angle replacing final height |
| ch07-p08-010 (5) | 07 | relation | reference (standard form) | VERIFIED | Eq 5 MP = -(f_o/f_e')(L/z) = m_o L/f_e', standard |
| ch07-p11-011 | 07 | relation | reference (standard form) | VERIFIED | field-lens geometry of Fig 7.x; alpha = beta/MP by definition of MP |
| ch07-p11-012 | 07 | relation | reference (standard form) | VERIFIED | field-lens geometry of Fig 7.x; alpha = beta/MP by definition of MP |
| ch07-p11-013 | 07 | relation | reference (standard form) | VERIFIED | field-lens geometry of Fig 7.x; alpha = beta/MP by definition of MP |
| ch07-p11-014 | 07 | relation | symbolic (sympy) | VERIFIED | small-angle limits of the two preceding lines (t2 ~ f_o') |
| ch07-p11-015 | 07 | relation | symbolic (sympy) | VERIFIED | small-angle limits of the two preceding lines (t2 ~ f_o') |
| ch07-p12-016 (1) | 07 | relation | reference (standard form) | VERIFIED | summary box restating Eqs 1-5 (checked above) |
| ch07-p12-017 (2) | 07 | relation | reference (standard form) | VERIFIED | summary box restating Eqs 1-5 (checked above) |
| ch07-p12-018 | 07 | relation | reference (standard form) | VERIFIED | summary box restating Eqs 1-5 (checked above) |
| ch07-p12-019 (3) | 07 | relation | reference (standard form) | VERIFIED | summary box restating Eqs 1-5 (checked above) |
| ch07-p12-020 (4) | 07 | relation | reference (standard form) | VERIFIED | summary box restating Eqs 1-5 (checked above) |
| ch07-p12-021 (5) | 07 | relation | reference (standard form) | VERIFIED | summary box restating Eqs 1-5 (checked above) |
| ch07-p12-022 | 07 | relation | symbolic (sympy) | VERIFIED | magnifier: image at infinity MP = V/f'; image at the near point with eye at the lens MP = V/f' + 1 |
| ch08-p05-001 | 08 | relation | reference (standard form) | VERIFIED | Eq 1: odd power series of transverse aberration in aperture, standard |
| ch08-p05-002 | 08 | relation | reference (standard form) | VERIFIED | backward transfer of two rays from the image plane |
| ch08-p05-003 | 08 | relation | reference (standard form) | VERIFIED | backward transfer of two rays from the image plane |
| ch08-p05-004 | 08 | relation | symbolic (sympy) | VERIFIED | intersection of the two rays |
| ch08-p05-005 | 08 | relation | reference (standard form) | VERIFIED | paraxial proportionality Y1/tanU = y1/u (same axial image point) |
| ch08-p05-006 | 08 | relation | symbolic (sympy) | VERIFIED | Eq 2 from the two preceding lines |
| ch08-p05-007 | 08 | relation | symbolic (sympy) | VERIFIED | Eq 2 from the two preceding lines |
| ch08-p07-008 | 08 | relation | numeric (book values) | VERIFIED | Eq 3 third-order LSA: -Sigma B/(2 n u) = -0.02135 (book Table 8.2: -0.02135) |
| ch08-p07-009 | 08 | relation | numeric (book values) | VERIFIED | Eq 3 third-order LSA: -Sigma B/(2 n u) = -0.02135 (book Table 8.2: -0.02135) |
| ch08-p07-010 | 08 | relation | numeric (book values) | VERIFIED | Eqs 4, 5 recomputed from a fresh paraxial trace of Table 8.2's c, t, n reproduce all six printed B to the printed digits |
| ch08-p07-011 | 08 | relation | numeric (book values) | VERIFIED | Eqs 4, 5 recomputed from a fresh paraxial trace of Table 8.2's c, t, n reproduce all six printed B to the printed digits |
| ch08-p10-012 | 08 | relation | reference (standard form) | VERIFIED | third-order transverse aberration polynomials (Seidel form); coefficients verified via Table 8.2 and Eq 3/8 checks |
| ch08-p10-013 | 08 | relation | reference (standard form) | VERIFIED | third-order transverse aberration polynomials (Seidel form); coefficients verified via Table 8.2 and Eq 3/8 checks |
| ch08-p10-014 | 08 | relation | reference (standard form) | VERIFIED | Eq 8 distortion term of Eq 6 at the chief ray; numerically confirmed through the next line |
| ch08-p10-015 | 08 | relation | numeric (book values) | VERIFIED | fractional distortion at 20 deg = -Sigma E/(2 Phi) = +0.0019; matches Fig 8.9 3rd-order curve (+0.19 %) |
| ch08-p14-016 | 08 | relation | reference (standard form) | VERIFIED | Coddington-limit tangential/sagittal/Petzval foci; t_kP = (3 t_kS - t_kT)/2 is the standard Petzval relation |
| ch08-p14-017 | 08 | relation | reference (standard form) | VERIFIED | Coddington-limit tangential/sagittal/Petzval foci; t_kP = (3 t_kS - t_kT)/2 is the standard Petzval relation |
| ch08-p14-018 | 08 | relation | symbolic (sympy) | VERIFIED | t_kP = (3 t_kS - t_kT)/2 leaves only the P Phi^2 term (Eqs 9, 10) |
| ch08-p14-019 | 08 | relation | numeric (book values) | VERIFIED | Eqs 4, 5 recomputed from a fresh paraxial trace of Table 8.2's c, t, n reproduce all six printed B to the printed digits |
| ch08-p14-020 | 08 | relation | numeric (book values) | VERIFIED | Eq 11 F = S i i-bar reproduces all six printed F |
| ch08-p14-021 | 08 | relation | numeric (book values) | VERIFIED | Eq 12 C = S i-bar^2 reproduces all six printed C |
| ch08-p14-022 | 08 | relation | numeric (book values) | VERIFIED | Eq 13 (S-bar from chief ray, Phi = y-bar u - y u-bar = -0.5460) reproduces all six printed E |
| ch08-p14-023 | 08 | relation | numeric (book values) | VERIFIED | Eq 14 P = c(n_-1 - n)/(n_-1 n) reproduces all six printed P; Sigma P = -0.04000 as printed |
| ch08-p14-024 | 08 | relation | reference (standard form) | VERIFIED | aspheric (4th-order) surface contributions: B = 8(n_-1 - n) e y^4 and F, C, E scale by (y-bar/y)^k; standard form |
| ch08-p14-025 | 08 | relation | reference (standard form) | VERIFIED | aspheric (4th-order) surface contributions: B = 8(n_-1 - n) e y^4 and F, C, E scale by (y-bar/y)^k; standard form |
| ch08-p14-026 | 08 | relation | reference (standard form) | VERIFIED | aspheric (4th-order) surface contributions: B = 8(n_-1 - n) e y^4 and F, C, E scale by (y-bar/y)^k; standard form |
| ch08-p14-027 | 08 | relation | reference (standard form) | VERIFIED | aspheric (4th-order) surface contributions: B = 8(n_-1 - n) e y^4 and F, C, E scale by (y-bar/y)^k; standard form |
| ch08-p15-028 | 08 | definition | reference (definition) | DEFINITION | plotted quantities for ray-intercept curves |
| ch08-p15-029 | 08 | definition | reference (definition) | DEFINITION | plotted quantities for ray-intercept curves |
| ch08-p15-030 | 08 | relation | reference (standard form) | VERIFIED | conversion of final direction to image-plane intercept |
| ch08-p15-031 | 08 | relation | reference (standard form) | VERIFIED | conversion of final direction to image-plane intercept |
| ch08-p16-032 | 08 | relation | reference (standard form) | VERIFIED | Eqs 15, 16 angular forms of Eqs 6, 7 (divide by the final paraxial distance) |
| ch08-p16-033 | 08 | relation | reference (standard form) | VERIFIED | Eqs 15, 16 angular forms of Eqs 6, 7 (divide by the final paraxial distance) |
| ch08-p16-034 | 08 | definition | reference (definition) | DEFINITION | stop-shift definitions (new chief ray, Q = y-bar1*/y1) |
| ch08-p17-035 | 08 | definition | reference (definition) | DEFINITION | stop-shift definitions (new chief ray, Q = y-bar1*/y1) |
| ch08-p17-036 | 08 | definition | reference (definition) | DEFINITION | stop-shift definitions (new chief ray, Q = y-bar1*/y1) |
| ch08-p17-037 | 08 | relation | symbolic (sympy) | VERIFIED | Eq 17: substituting Y1 = Y1' + Q y1 (Ybar_o/ybar_o) into Eqs 6 + 8 and collecting reproduces every coefficient |
| ch08-p17-038 | 08 | relation | symbolic (sympy) | VERIFIED | Eq 17: substituting Y1 = Y1' + Q y1 (Ybar_o/ybar_o) into Eqs 6 + 8 and collecting reproduces every coefficient |
| ch08-p17-039 | 08 | relation | symbolic (sympy) | VERIFIED | Eq 17: substituting Y1 = Y1' + Q y1 (Ybar_o/ybar_o) into Eqs 6 + 8 and collecting reproduces every coefficient |
| ch08-p18-040 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 18-21a stop-shift sums follow from Eq 17 term by term (C* = Q^2 B + 2Q F + C) |
| ch08-p18-041 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 18-21a stop-shift sums follow from Eq 17 term by term (C* = Q^2 B + 2Q F + C) |
| ch08-p18-042 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 18-21a stop-shift sums follow from Eq 17 term by term (C* = Q^2 B + 2Q F + C) |
| ch08-p18-043 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 18-21a stop-shift sums follow from Eq 17 term by term (C* = Q^2 B + 2Q F + C) |
| ch08-p18-044 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 18-21a stop-shift sums follow from Eq 17 term by term (C* = Q^2 B + 2Q F + C) |
| ch08-p18-045 | 08 | relation | reference (standard form) | VERIFIED | chromatic stop shift a* = a, b* = Q a + b (b ~ y y-bar, y-bar* = y-bar + Q y) |
| ch08-p18-046 | 08 | relation | reference (standard form) | VERIFIED | chromatic stop shift a* = a, b* = Q a + b (b ~ y y-bar, y-bar* = y-bar + Q y) |
| ch08-p18-047 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p18-048 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p18-049 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p18-050 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p18-051 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-052 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-053 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-054 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-055 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-056 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-057 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-058 | 08 | relation | numeric (book values) | VERIFIED | thin-lens coefficients Eqs 24-35 equal the sum of the two surface formulas (Eqs 4, 5, 11-14) at zero thickness; checked for random n, phi, c1, u_-1, y, y-bar (stop at lens so C = -phi Phi^2, E = 0, P = -phi/n) |
| ch08-p19-059 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-060 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-061 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-062 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-063 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-064 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-065 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-066 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-067 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-068 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-069 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-070 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-071 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p19-072 | 08 | relation | symbolic (sympy) | VERIFIED | Eqs 36-49: stop-shift Eqs 18-21 applied to thin-lens Eqs 24-28, expanded in c1, give every alpha*, beta*, gamma*, delta* as printed |
| ch08-p20-073 | 08 | relation | numeric (book values) | VERIFIED | thin-lens c1 values are the Table 8.2 thick-lens first curvatures rounded (0.25285, -0.19942, 0.05065) |
| ch08-p20-074 | 08 | relation | numeric (book values) | VERIFIED | thin-lens c1 values are the Table 8.2 thick-lens first curvatures rounded (0.25285, -0.19942, 0.05065) |
| ch08-p20-075 | 08 | relation | numeric (book values) | VERIFIED | thin-lens c1 values are the Table 8.2 thick-lens first curvatures rounded (0.25285, -0.19942, 0.05065) |
| ch09-p03-001 (1) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p03-002 (2) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p03-003 (3) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p03-004 (4) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p03-005 (5) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p03-006 (6) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p03-007 (7) | 09 | relation | reference (standard form) | VERIFIED | first-order Taylor expansion of each aberration sum in the construction parameters |
| ch09-p04-008 | 09 | definition | reference (definition) | DEFINITION | finite-difference estimates of the differential coefficients |
| ch09-p04-009 | 09 | definition | reference (definition) | DEFINITION | finite-difference estimates of the differential coefficients |
| ch09-p04-010 | 09 | definition | reference (definition) | DEFINITION | finite-difference estimates of the differential coefficients |
| ch09-p04-011 | 09 | definition | reference (definition) | DEFINITION | finite-difference estimates of the differential coefficients |
| ch09-p07-012 | 09 | definition | reference (definition) | DEFINITION | Airy pattern argument Z = pi Y_e d/(lambda l') (d = diameter measured across the pattern) |
| ch09-p07-013 | 09 | worked example | numeric (book values) | VERIFIED | first zero of J1 at Z = 3.832: d = 3.832/pi (lambda l'/Y_e) = 1.2197 lambda l'/Y_e, i.e. the Airy DIAMETER (radius 0.61 lambda/NA); book's 3.83 and 1.22 are the rounded values |
| ch09-p08-014 | 09 | relation | reference (standard form) | VERIFIED | root-sum-square combination of geometric and diffraction blur (empirical rule) |
| ch09-p11-015 (5-(56)) | 09 | relation | reference (standard form) | VERIFIED | restated ch05/ch06 paraxial equations (verified numerically on Table 6.6) |
| ch09-p11-016 (5-(57)) | 09 | relation | reference (standard form) | VERIFIED | restated ch05/ch06 paraxial equations (verified numerically on Table 6.6) |
| ch09-p11-017 (5-(56)) | 09 | relation | reference (standard form) | VERIFIED | restated ch05/ch06 paraxial equations (verified numerically on Table 6.6) |
| ch09-p11-018 (6-(3)) | 09 | relation | reference (standard form) | VERIFIED | restated ch05/ch06 paraxial equations (verified numerically on Table 6.6) |
| ch09-p11-019 (6-(4)) | 09 | relation | reference (standard form) | VERIFIED | restated ch05/ch06 paraxial equations (verified numerically on Table 6.6) |
| ch09-p11-020 (6-(6)) | 09 | relation | reference (standard form) | VERIFIED | restated ch05/ch06 paraxial equations (verified numerically on Table 6.6) |
| ch09-p11-021 (6-(34)) | 09 | relation | reference (standard form) | VERIFIED | restated ch06 Eqs 34/35 in the Table 8.2 sign convention (reproduce Table 8.2 a, b rows) |
| ch09-p11-022 (6-(35)) | 09 | relation | reference (standard form) | VERIFIED | restated ch06 Eqs 34/35 in the Table 8.2 sign convention (reproduce Table 8.2 a, b rows) |
| ch09-p11-023 (8-(5)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-024 (8-(13) footnote) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-025 (8-(4)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-026 (8-(11)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-027 (8-(12)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-028 (8-(13)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-029 (8-(14)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-030 (8-(4a)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-031 (8-(11a)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-032 (8-(12a)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-033 (8-(13a)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-034 (8-(18)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-035 (8-(19)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-036 (8-(20)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-037 (8-(21)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-038 (8-(21a)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-039 (8-(22)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch09-p11-040 (8-(23)) | 09 | relation | reference (standard form) | VERIFIED | restated ch08 Eqs 4-5, 11-14, 4a-13a, 18-23 (verified by the Table 8.2 recompute and stop-shift algebra in ck_ch07_08) |
| ch10-p02-001 | 10 | relation | reference (standard form) | VERIFIED | ch06 Eq 41 thin-lens lateral colour, three elements |
| ch10-p02-002 | 10 | definition | reference (definition) | DEFINITION | design condition Tch = 0 |
| ch10-p03-003 | 10 | relation | reference (standard form) | VERIFIED | stop at lens b (y-bar_b = 0) removes the middle term |
| ch10-p03-004 | 10 | definition | reference (definition) | DEFINITION | definition of R |
| ch10-p03-005 | 10 | relation | symbolic (sympy) | VERIFIED | solving the Tch = 0 condition for y-bar_a/y-bar_c |
| ch10-p03-006 | 10 | relation | reference (standard form) | VERIFIED | chief ray through the centre of lens b: y-bar_a/y-bar_c = -t3/t5 (thin-lens, small angles) |
| ch10-p03-007 | 10 | relation | symbolic (sympy) | VERIFIED | equal nu for lenses a and c |
| ch10-p13-008 (1) | 10 | relation | reference (standard form) | VERIFIED | Eqs 1-4 third-order targets for the three thin lenses (stop at b) |
| ch10-p13-009 (2) | 10 | relation | reference (standard form) | VERIFIED | Eqs 1-4 third-order targets for the three thin lenses (stop at b) |
| ch10-p13-010 (3) | 10 | relation | reference (standard form) | VERIFIED | Eqs 1-4 third-order targets for the three thin lenses (stop at b) |
| ch10-p13-011 (4) | 10 | relation | reference (standard form) | VERIFIED | Eqs 1-4 third-order targets for the three thin lenses (stop at b) |
| ch10-p13-012 (5) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-013 (6) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-014 (7) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-015 (8) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-016 (9) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-017 (10) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-018 (11) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-019 (12) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-020 (13) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-021 (14) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-022 (15) | 10 | relation | reference (standard form) | VERIFIED | Eqs 5-15 restate the thin-lens coefficient forms of ch08 Eqs 29-49 (verified symbolically there); lens b at the stop has C = -phi Phi^2, E = 0 |
| ch10-p13-023 (16) | 10 | definition | reference (definition) | DEFINITION | Eq 16 second curvature from the lens power (c_a = phi_a/(n_a - 1)) |
| ch10-p15-024 (17) | 10 | relation | reference (standard form) | VERIFIED | Eq 17 parabolic fit of 3Y_k versus bending (B is quadratic in c, ch08 Eq 24) |
| ch10-p15-025 | 10 | worked example | numeric (book values) | VERIFIED | roots of 0 = -2.0(c - 0.338)^2 + 0.016: 0.2486, 0.4274 (book 0.249, 0.427) |
| ch10-p15-026 | 10 | worked example | numeric (book values) | VERIFIED | roots of 0 = -2.0(c - -0.2057)^2 + 0.016: -0.2951, -0.1163 (book -0.295, -0.116) |
| ch10-p15-027 | 10 | worked example | numeric (book values) | VERIFIED | roots of 0 = -2.0(c - 0.078)^2 + 0.016: -0.0114, 0.1674 (book -0.011, 0.167) |
| ch10-p17-028 | 10 | definition | reference (definition) | DEFINITION | ray data for the design |
| ch10-p19-029 (18) | 10 | definition | reference (definition) | DEFINITION | design targets (Eqs 18-24) |
| ch10-p19-030 (19) | 10 | definition | reference (definition) | DEFINITION | design targets (Eqs 18-24) |
| ch10-p19-031 (20) | 10 | relation | symbolic (sympy) | VERIFIED | Eq 20 target makes 3C + P Phi^2 = 0, i.e. a flat tangential field (ch08 Eq 9) |
| ch10-p19-032 (21) | 10 | definition | reference (definition) | DEFINITION | design targets (Eqs 18-24) |
| ch10-p19-033 (22) | 10 | definition | reference (definition) | DEFINITION | design targets (Eqs 18-24) |
| ch10-p19-034 (23) | 10 | definition | reference (definition) | DEFINITION | design targets (Eqs 18-24) |
| ch10-p19-035 (24) | 10 | definition | reference (definition) | DEFINITION | design targets (Eqs 18-24) |
| ch10-p28-036 | 10 | relation | symbolic (sympy) | VERIFIED | restatement of t3/t5 = 1/R |
| ch10-p28-037 | 10 | relation | reference (standard form) | VERIFIED | restatement of Eq 17 |
| ch11-p01-001 | 11 | relation | reference (standard form) | VERIFIED | ch08 Eqs 15/16 keeping only the Petzval term (flat-field telescope approximation) |
| ch11-p01-002 | 11 | relation | reference (standard form) | VERIFIED | ch08 Eqs 15/16 keeping only the Petzval term (flat-field telescope approximation) |
| ch11-p01-003 | 11 | relation | reference (standard form) | VERIFIED | Sigma P = -(phi_o/gamma_o + phi_e/gamma_e) from gamma = -1/(f Sigma P) (ch14 definition), Phi = n0 u0 Ybar_o |
| ch11-p01-004 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 3 from the line above with u0 = y1/t_o, phi_o = -phi_e/MP, y1 = -MP y_(k-1) (afocal) |
| ch11-p02-005 | 11 | relation | numeric (book values) | VERIFIED | Eq 3 with these inputs reproduces Table 11.1: diopters -9.0, -7.2, -6.6 (book -9.0, -7.2, -6.6); minutes 108.3, 86.6, 79.4 (book 107, 87, 79; the MP = -2 entry is 1.3' low) |
| ch11-p02-006 | 11 | relation | numeric (book values) | VERIFIED | Eq 3 with these inputs reproduces Table 11.1: diopters -9.0, -7.2, -6.6 (book -9.0, -7.2, -6.6); minutes 108.3, 86.6, 79.4 (book 107, 87, 79; the MP = -2 entry is 1.3' low) |
| ch11-p02-007 | 11 | relation | numeric (book values) | VERIFIED | Eq 3 with these inputs reproduces Table 11.1: diopters -9.0, -7.2, -6.6 (book -9.0, -7.2, -6.6); minutes 108.3, 86.6, 79.4 (book 107, 87, 79; the MP = -2 entry is 1.3' low) |
| ch11-p02-008 | 11 | relation | numeric (book values) | VERIFIED | Eq 3 with these inputs reproduces Table 11.1: diopters -9.0, -7.2, -6.6 (book -9.0, -7.2, -6.6); minutes 108.3, 86.6, 79.4 (book 107, 87, 79; the MP = -2 entry is 1.3' low) |
| ch11-p02-009 | 11 | relation | numeric (book values) | VERIFIED | Eq 3 with these inputs reproduces Table 11.1: diopters -9.0, -7.2, -6.6 (book -9.0, -7.2, -6.6); minutes 108.3, 86.6, 79.4 (book 107, 87, 79; the MP = -2 entry is 1.3' low) |
| ch11-p03-010 | 11 | definition | reference (definition) | DEFINITION | power and achromatism conditions |
| ch11-p03-011 | 11 | definition | reference (definition) | DEFINITION | power and achromatism conditions |
| ch11-p03-012 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 6 solves Eqs 4-5 |
| ch11-p03-013 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 7 solves Eqs 4-5 |
| ch11-p04-014 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 8: thin-lens P = -phi/n (ch08 Eq 28) summed with Eqs 6-7 |
| ch11-p04-015 | 11 | relation | numeric (book values) | VERIFIED | the ratio is 'nearly constant': 0.713 for this pair vs 0.728 for a 520/570 + 620/360 pair (within 2%) |
| ch11-p04-016 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms of ch08 Eqs 24-25 |
| ch11-p04-017 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms of ch08 Eqs 24-25 |
| ch11-p04-018 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms of ch08 Eqs 24-25 |
| ch11-p04-019 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms of ch08 Eqs 24-25 |
| ch11-p04-020 | 11 | definition | reference (definition) | DEFINITION | glass data as printed (scan p.11-4 confirms 1.511/63.5 and 1.649/30.6) |
| ch11-p04-021 | 11 | definition | reference (definition) | DEFINITION | glass data as printed (scan p.11-4 confirms 1.511/63.5 and 1.649/30.6) |
| ch11-p09-022 | 11 | relation | reference (standard form) | VERIFIED | first-order differential corrections (ch09 Eqs 1-7) |
| ch11-p09-023 | 11 | relation | reference (standard form) | VERIFIED | first-order differential corrections (ch09 Eqs 1-7) |
| ch11-p09-024 | 11 | relation | reference (standard form) | VERIFIED | first-order differential corrections (ch09 Eqs 1-7) |
| ch11-p09-025 | 11 | definition | reference (definition) | DEFINITION | Seidel/fifth-order coefficients of the example |
| ch11-p12-026 | 11 | relation | numeric (book values) | VERIFIED | 4.6 x 0.5893 um / 0.14 = 19.36 um = 0.0194 mm (book 19.4) |
| ch11-p12-027 | 11 | worked example | numeric (book values) | VERIFIED | 4.6 x 0.5893 um / 0.14 = 19.36 um = 0.0194 mm (book 19.4) |
| ch11-p12-028 | 11 | worked example | numeric (book values) | VERIFIED | 4.6 x 0.5893 um / 0.14 = 19.36 um = 0.0194 mm (book 19.4) |
| ch11-p14-029 | 11 | relation | none | NOT VERIFIED | aspheric deflection model stated as an assumption of the method; dimensional form (lambda times polynomial in S) cannot be derived from the text; no worked numbers |
| ch11-p15-030 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms (ch08 Eqs 24-25) for a cemented pair |
| ch11-p15-031 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms (ch08 Eqs 24-25) for a cemented pair |
| ch11-p15-032 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms (ch08 Eqs 24-25) for a cemented pair |
| ch11-p15-033 | 11 | relation | reference (standard form) | VERIFIED | thin-lens B, F forms (ch08 Eqs 24-25) for a cemented pair |
| ch11-p18-034 | 11 | relation | numeric (book values) | VERIFIED | Eq 13 with d(TAch)/TAch = 1/10 and n_D - 1 ~ 0.55 gives dn = 2.5e-5, the text's '2 in the fifth decimal place' |
| ch11-p19-035 | 11 | definition | reference (definition) | DEFINITION | apochromat conditions (power, F-C achromatism, D to the F-C focus) |
| ch11-p19-036 | 11 | definition | reference (definition) | DEFINITION | apochromat conditions (power, F-C achromatism, D to the F-C focus) |
| ch11-p19-037 | 11 | definition | reference (definition) | DEFINITION | apochromat conditions (power, F-C achromatism, D to the F-C focus) |
| ch11-p19-038 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 17 solves Eqs 14-16 |
| ch11-p19-039 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 18 solves Eqs 14-16 |
| ch11-p19-040 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 19 solves Eqs 14-16 |
| ch11-p19-041 | 11 | definition | reference (definition) | DEFINITION | Eq 20 determinant |
| ch11-p19-042 | 11 | relation | reference (standard form) | VERIFIED | Delta = twice the triangle area in the P-nu plane (base (P_a - P_c)/cos(theta), height h) |
| ch11-p19-043 | 11 | relation | reference (standard form) | VERIFIED | Delta = twice the triangle area in the P-nu plane (base (P_a - P_c)/cos(theta), height h) |
| ch11-p20-044 | 11 | definition | reference (definition) | DEFINITION | Abbe number |
| ch11-p20-045 | 11 | relation | symbolic (sympy) | VERIFIED | ratio of Eqs 17 and 19 |
| ch11-p20-046 | 11 | relation | reference (standard form) | VERIFIED | Eq 21 residual chromatic at a fourth wavelength (ch06 Eq 42 generalised) |
| ch11-p20-047 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 22 = Eq 21 with Eqs 17-19 substituted; its numerator equals det[P*, P**, 1], the printed determinant form |
| ch11-p21-048 | 11 | relation | symbolic (sympy) | VERIFIED | Eq 22 = Eq 21 with Eqs 17-19 substituted; its numerator equals det[P*, P**, 1], the printed determinant form |
| ch11-p25-049 | 11 | relation | reference (standard form) | VERIFIED | OPD for a transverse error Y_k across the pupil: W = Y_k Y1/(2f') (defocus-type wavefront) |
| ch12-p01-001 | 12 | relation | symbolic (sympy) | VERIFIED | two relay doublets of f = D/2, each P = -phi/n (ch08 Eq 28): Sigma P = -4/(D n) |
| ch12-p01-002 | 12 | relation | numeric (book values) | VERIFIED | Erfle Sigma P = -0.2125 cm^-1 is Table 14.7's printed value (and gives Table 14.7's gamma = 1.853 with f = 2.54) |
| ch12-p02-003 | 12 | relation | reference (standard form) | VERIFIED | ch06 secondary-spectrum rule (P~ slope ~ -1/2200) for one doublet: TAch ~ y1/2200 |
| ch12-p02-004 (1) | 12 | relation | numeric (book values) | VERIFIED | Eq 1: two doublets, y1 = u0 D/2 each; book example u0 = 0.14, D = 70 cm gives 0.0045 cm (text rounds to 0.005) |
| ch12-p02-005 (2) | 12 | relation | reference (standard form) | VERIFIED | Eq 2: same with the effective length D - d |
| ch12-p03-006 | 12 | relation | symbolic (sympy) | VERIFIED | field lens at D/2 images the relay at D/4 onto the relay at 3D/4: 1/f = 4/D + 4/D; P = -phi/n |
| ch13-p01-001 | 13 | relation | symbolic (sympy) | VERIFIED | ch02 Eq 4 with n1 = -n0 (= 1): Gamma = -cos I - \|cos I\| = -2 cos I |
| ch13-p01-002 (1) | 13 | relation | symbolic (sympy) | VERIFIED | ch02 Eq 4 with n1 = -n0 (= 1): Gamma = -cos I - \|cos I\| = -2 cos I |
| ch13-p01-003 (2) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p01-004 (3a) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p01-005 (3b) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p01-006 (4a) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p01-007 (4b) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p02-008 (5a) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p02-009 (5b) | 13 | definition | reference (definition) | DEFINITION | successive reflections S_i = S_(i-1) + Gamma_i M_i, rho_i = S_(i-1).M_i (substitutions checked in the example) |
| ch13-p02-010 | 13 | definition | reference (definition) | DEFINITION | worked example: fold the Z axis into (i + j)/sqrt 2 |
| ch13-p02-011 | 13 | definition | reference (definition) | DEFINITION | worked example: fold the Z axis into (i + j)/sqrt 2 |
| ch13-p02-012 | 13 | definition | reference (definition) | DEFINITION | worked example: fold the Z axis into (i + j)/sqrt 2 |
| ch13-p02-013 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p02-014 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p02-015 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-016 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-017 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-018 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-019 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-020 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-021 | 13 | relation | numeric (book values) | VERIFIED | solution M = (-1/2, -1/2, 1/sqrt 2): unit length, and reflecting k in it gives (i + j)/sqrt 2 exactly |
| ch13-p03-022 (6) | 13 | definition | reference (definition) | DEFINITION | plane equation |
| ch13-p04-023 (7) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-024 | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-025 (8a) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-026 (8b) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-027 (8c) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-028 (9a) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-029 (9b) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-030 (9c) | 13 | relation | reference (standard form) | VERIFIED | foot of the perpendicular from the origin and unit normal of Ax + By + Cz + D = 0 (normal sign chosen with D) |
| ch13-p04-031 | 13 | relation | numeric (book values) | VERIFIED | reciprocals of the example's M |
| ch13-p06-032 (10) | 13 | definition | reference (definition) | DEFINITION | plane through the point / the mirror |
| ch13-p06-033 (11) | 13 | definition | reference (definition) | DEFINITION | plane through the point / the mirror |
| ch13-p06-034 (12) | 13 | relation | symbolic (sympy) | VERIFIED | Eq 12 with D1 = -(A x1 + B y1 + C z1) |
| ch13-p06-035 (13) | 13 | relation | symbolic (sympy) | VERIFIED | Eqs 13-15: the image point is displaced along the normal and lies equally far on the other side of the plane |
| ch13-p06-036 (14) | 13 | relation | symbolic (sympy) | VERIFIED | Eqs 13-15: the image point is displaced along the normal and lies equally far on the other side of the plane |
| ch13-p06-037 (15) | 13 | relation | symbolic (sympy) | VERIFIED | Eqs 13-15: the image point is displaced along the normal and lies equally far on the other side of the plane |
| ch13-p06-038 (16) | 13 | relation | symbolic (sympy) | VERIFIED | Eq 16 4x4 matrix equals Eqs 13-15 |
| ch13-p07-039 (17) | 13 | relation | reference (standard form) | VERIFIED | composition of reflections as matrix products |
| ch13-p07-040 | 13 | relation | reference (standard form) | VERIFIED | composition of reflections as matrix products |
| ch13-p07-041 (18) | 13 | relation | reference (standard form) | VERIFIED | composition of reflections as matrix products |
| ch13-p07-042 | 13 | relation | symbolic (sympy) | VERIFIED | vector reflection law written out in components equals the Eq 19 matrix (Householder form I - 2MM^T) |
| ch13-p07-043 | 13 | relation | symbolic (sympy) | VERIFIED | vector reflection law written out in components equals the Eq 19 matrix (Householder form I - 2MM^T) |
| ch13-p07-044 | 13 | relation | symbolic (sympy) | VERIFIED | vector reflection law written out in components equals the Eq 19 matrix (Householder form I - 2MM^T) |
| ch13-p07-045 | 13 | relation | symbolic (sympy) | VERIFIED | vector reflection law written out in components equals the Eq 19 matrix (Householder form I - 2MM^T) |
| ch13-p07-046 (19) | 13 | relation | symbolic (sympy) | VERIFIED | vector reflection law written out in components equals the Eq 19 matrix (Householder form I - 2MM^T) |
| ch13-p07-047 (20) | 13 | relation | reference (standard form) | VERIFIED | Eq 20 composition of reflections |
| ch13-p07-048 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p07-049 (21) | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p08-050 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p08-051 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p08-052 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p08-053 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p08-054 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p08-055 | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p09-056 (22) | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p09-057 (23) | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p09-058 (24) | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p09-059 (25) | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p09-060 (26) | 13 | relation | reference (standard form) | VERIFIED | rotation of axes by direction cosines; Eq 26 is the transpose (inverse) of Eq 25 |
| ch13-p09-061 | 13 | definition | reference (definition) | DEFINITION | unit normal |
| ch13-p13-062 | 13 | relation | numeric (book values) | VERIFIED | tan 30 / sin 45 = 0.81650 (book 0.81657 from the rounded .5774/.7071); theta = 39.23 deg |
| ch13-p13-063 | 13 | relation | numeric (book values) | VERIFIED | tan 30 / sin 45 = 0.81650 (book 0.81657 from the rounded .5774/.7071); theta = 39.23 deg |
| ch13-p13-064 | 13 | worked example | numeric (book values) | VERIFIED | tan 30 / sin 45 = 0.81650 (book 0.81657 from the rounded .5774/.7071); theta = 39.23 deg |
| ch13-p32-065 | 13 | worked example | numeric (book values) + scan | FLAG | B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) (1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but D = B - 2(A + 2a) = 2.0823, 1.8072 (t/n shows these D are typos: D should equal t/n). Mismatches found: n=1.617 D printed 2.1822 computed 2.0823; n=1.617 t printed 3.3637 computed 3.367; n=1.617 tn printed 2.0802 computed 2.0823; n=1.72 D printed 1.9072 computed 1.8072 |
| ch13-p32-066 | 13 | worked example | numeric (book values) + scan | FLAG | B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) (1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but D = B - 2(A + 2a) = 2.0823, 1.8072 (t/n shows these D are typos: D should equal t/n). Mismatches found: n=1.617 D printed 2.1822 computed 2.0823; n=1.617 t printed 3.3637 computed 3.367; n=1.617 tn printed 2.0802 computed 2.0823; n=1.72 D printed 1.9072 computed 1.8072 |
| ch13-p32-067 | 13 | worked example | numeric (book values) + scan | FLAG | B, C, t, E values reproduce for all four glasses, but (sic, scan p.13-34): (1) the t formula's denominator must be read sin(theta)[sqrt(n^2 - sin^2 theta) - sin(theta)] to give the printed 3.3787; (2) 'E = 1.4142(A + 2a)' should be 1.4142(A + a) (1.4142 x 1.10 = 1.556, not 1.4849); (3) glass table D for n = 1.6170 and 1.7200 printed 2.1822 and 1.9072, but D = B - 2(A + 2a) = 2.0823, 1.8072 (t/n shows these D are typos: D should equal t/n). Mismatches found: n=1.617 D printed 2.1822 computed 2.0823; n=1.617 t printed 3.3637 computed 3.367; n=1.617 tn printed 2.0802 computed 2.0823; n=1.72 D printed 1.9072 computed 1.8072 |
| ch13-p33-068 | 13 | worked example | numeric (book values) | VERIFIED | double Dove, n = 1.517: B = 2.1135, t = 1.6892 (same parenthesisation as the single Dove), t/n = 1.1135, D = 0.7071 |
| ch13-p33-069 | 13 | worked example | numeric (book values) | VERIFIED | double Dove, n = 1.517: B = 2.1135, t = 1.6892 (same parenthesisation as the single Dove), t/n = 1.1135, D = 0.7071 |
| ch13-p43-070 | 13 | worked example | numeric (book values) | FLAG | 2.283/2.835 = 0.805291 is right, but arccos(0.805291) = 36 deg 21' 42", not the printed 36 deg 22' 3" (21 arcsec; minor 1962 table-interpolation slip, or transcription; scan not re-read) |
| ch14-p01-001 | 14 | relation | numeric (book values) | VERIFIED | paraxial trace of all nine Tables 14.1-14.9 (glass n_d from the MIL code): EFL = 2.534-2.540 cm, back focus = printed last spacing to <0.005 cm (Huygenian focus 0.718 cm inside the field lens), Sigma P and gamma = -1/(f Sigma P) match every printed value (orthoscopic 0.3163 vs 0.3158, glass-code rounding) |
| ch15-p02-001 | 15 | worked example | numeric (book values) | VERIFIED | f_o = MP f_e = 25 cm, D_o = MP D_ep = 5.0 cm, N = 5.0 |
| ch15-p02-002 | 15 | worked example | numeric (book values) | VERIFIED | arctan(tan 30 deg / 10) = 3.30 deg (book: 3.3, '3 deg approx.') |
| ch15-p02-003 | 15 | relation | numeric (book values) | VERIFIED | 4A/n with A = 2.9 cm prism aperture and n = 1.5725 (glass 573574): 7.3767 cm |
| ch16-p01-001 (1) | 16 | definition | reference (definition) | DEFINITION | plane wave |
| ch16-p01-002 (2) | 16 | relation | reference (standard form) | VERIFIED | time-averaged irradiance, coherent and incoherent sums (verified symbolically in ch03 Eqs 16, 24, 29) |
| ch16-p01-003 (3) | 16 | relation | reference (standard form) | VERIFIED | time-averaged irradiance, coherent and incoherent sums (verified symbolically in ch03 Eqs 16, 24, 29) |
| ch16-p01-004 (4) | 16 | relation | reference (standard form) | VERIFIED | time-averaged irradiance, coherent and incoherent sums (verified symbolically in ch03 Eqs 16, 24, 29) |
| ch16-p01-005 | 16 | definition | reference (definition) | DEFINITION | phase of wave 1 |
| ch16-p01-006 (5) | 16 | relation | symbolic (sympy) | VERIFIED | phase difference of two tilted plane waves |
| ch16-p01-007 (6) | 16 | relation | symbolic (sympy) | VERIFIED | phase difference of two tilted plane waves |
| ch16-p02-008 (7) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 3 with Eq 6 |
| ch16-p02-009 (8) | 16 | relation | symbolic (sympy) | VERIFIED | z = 0, small theta |
| ch16-p03-010 (9) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 7 with a1 = a2 = a |
| ch16-p03-011 (10) | 16 | relation | symbolic (sympy) | VERIFIED | delta = pi (reflection phase reversal) |
| ch16-p03-012 | 16 | relation | symbolic (sympy) | VERIFIED | n = 1, z = 0, small theta; 1 - cos 2u = 2 sin^2 u |
| ch16-p03-013 (11) | 16 | relation | symbolic (sympy) | VERIFIED | theta = 2 alpha |
| ch16-p03-014 (12) | 16 | relation | symbolic (sympy) | VERIFIED | fringe period of sin^2(2 pi x alpha/lambda) |
| ch16-p03-015 (13) | 16 | definition | reference (definition) | DEFINITION | wedge thickness d = x alpha |
| ch16-p03-016 (14) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 11 with Eq 13 |
| ch16-p05-017 (15) | 16 | definition | reference (definition) | DEFINITION | phase with surface-height error D(x) |
| ch16-p05-018 (16) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 9 with Eq 15, n = 1, theta = 2 alpha |
| ch16-p05-019 (17) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 9 with Eq 15, n = 1, theta = 2 alpha |
| ch16-p05-020 (18) | 16 | definition | reference (definition) | DEFINITION | fringes are contours of constant D + x alpha |
| ch16-p07-021 (19) | 16 | relation | reference (standard form) | VERIFIED | unequal amplitudes: Eq 7 form with Eq 15 |
| ch16-p08-022 (20) | 16 | definition | reference (definition) | DEFINITION | bright/dark conditions at lambda0 and lambda0 - dlambda |
| ch16-p08-023 (21) | 16 | definition | reference (definition) | DEFINITION | bright/dark conditions at lambda0 and lambda0 - dlambda |
| ch16-p08-024 (22) | 16 | relation | symbolic (sympy) | VERIFIED | subtracting Eq 20 from Eq 21: dlambda = lambda0^2/(4d + lambda0) ~ lambda0^2/(4d) |
| ch16-p08-025 (23) | 16 | relation | symbolic (sympy) | VERIFIED | subtracting Eq 20 from Eq 21: dlambda = lambda0^2/(4d + lambda0) ~ lambda0^2/(4d) |
| ch16-p08-026 (24) | 16 | relation | reference (standard form) | VERIFIED | partially coherent (extended circular source) fringe visibility 2 J1(v)/v (van Cittert-Zernike) |
| ch16-p08-027 (25) | 16 | worked example | numeric (book values) | VERIFIED | first zero of J1: 3.8317/(2 pi) = 0.6098 |
| ch16-p09-028 (26) | 16 | definition | reference (definition) | DEFINITION | distances from the two pinholes |
| ch16-p09-029 (27) | 16 | definition | reference (definition) | DEFINITION | distances from the two pinholes |
| ch16-p09-030 (28) | 16 | relation | symbolic (sympy) | VERIFIED | r2^2 - r1^2 = 4xs |
| ch16-p09-031 (29) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 29 rearranged |
| ch16-p09-032 (30) | 16 | relation | reference (standard form) | VERIFIED | (r1 + r2)/2 ~ sqrt(D^2 + s^2) near the axis |
| ch16-p09-033 (31) | 16 | relation | symbolic (sympy) | VERIFIED | with theta = 2s/sqrt(D^2 + s^2): r2 - r1 = x theta |
| ch16-p09-034 (32) | 16 | relation | symbolic (sympy) | VERIFIED | with theta = 2s/sqrt(D^2 + s^2): r2 - r1 = x theta |
| ch16-p09-035 (33) | 16 | definition | reference (definition) | DEFINITION | phase difference and two-pinhole irradiance |
| ch16-p11-036 (34) | 16 | definition | reference (definition) | DEFINITION | phase difference and two-pinhole irradiance |
| ch16-p11-037 (35) | 16 | definition | reference (definition) | DEFINITION | phase difference and two-pinhole irradiance |
| ch16-p11-038 (36) | 16 | relation | symbolic (sympy) | VERIFIED | fringe spacing h = lambda/theta |
| ch16-p11-039 (37) | 16 | definition | reference (definition) | DEFINITION | constant-phase (fringe) condition |
| ch16-p11-040 | 16 | definition | reference (definition) | DEFINITION | constant-phase (fringe) condition |
| ch16-p11-041 (38) | 16 | definition | reference (definition) | DEFINITION | constant-phase (fringe) condition |
| ch16-p11-042 (39) | 16 | relation | symbolic (sympy) | VERIFIED | delta2 - delta1 = 2 pi (x2 - x1)/h |
| ch16-p11-043 (40) | 16 | relation | symbolic (sympy) | VERIFIED | delta2 - delta1 = 2 pi (x2 - x1)/h |
| ch16-p12-044 (41) | 16 | relation | reference (standard form) | VERIFIED | Fresnel normal-incidence amplitude coefficients with complex index M = n(1 + iK) |
| ch16-p12-045 (42) | 16 | relation | reference (standard form) | VERIFIED | Fresnel normal-incidence amplitude coefficients with complex index M = n(1 + iK) |
| ch16-p12-046 (43) | 16 | relation | reference (standard form) | VERIFIED | Fresnel normal-incidence amplitude coefficients with complex index M = n(1 + iK) |
| ch16-p14-047 (44) | 16 | relation | symbolic (sympy) | VERIFIED | K = 0 |
| ch16-p14-048 (45) | 16 | relation | reference (standard form) | VERIFIED | absorbing case: real part of rho with phase sigma |
| ch16-p15-049 (46) | 16 | definition | reference (definition) | DEFINITION | plate path-difference geometry (Fig 16.x) |
| ch16-p15-050 | 16 | definition | reference (definition) | DEFINITION | plate path-difference geometry (Fig 16.x) |
| ch16-p15-051 | 16 | definition | reference (definition) | DEFINITION | plate path-difference geometry (Fig 16.x) |
| ch16-p15-052 (47) | 16 | relation | symbolic (sympy) | VERIFIED | BD1 = BD2 sin i |
| ch16-p15-053 (48) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 48 |
| ch16-p15-054 (49) | 16 | relation | symbolic (sympy) | VERIFIED | with Snell n0 sin i = n1 sin i': delta = 2 n1 d cos i' |
| ch16-p15-055 (50) | 16 | relation | reference (standard form) | VERIFIED | phase including the pi reflection change at the denser surface |
| ch16-p15-056 (51) | 16 | definition | reference (definition) | DEFINITION | first reflected amplitude |
| ch16-p15-057 (52) | 16 | relation | symbolic (sympy) | VERIFIED | second beam: transmit, reflect inside, transmit out |
| ch16-p15-058 (53) | 16 | relation | reference (standard form) | VERIFIED | two-beam sum with the pi phase difference |
| ch16-p16-059 (54) | 16 | definition | reference (definition) | DEFINITION | dark/bright orders; path difference definition |
| ch16-p16-060 (55) | 16 | definition | reference (definition) | DEFINITION | dark/bright orders; path difference definition |
| ch16-p16-061 (56) | 16 | definition | reference (definition) | DEFINITION | dark/bright orders; path difference definition |
| ch16-p17-062 (57) | 16 | relation | symbolic (sympy) | VERIFIED | with Snell n0 sin i = n1 sin i': delta = 2 n1 d cos i' |
| ch16-p17-063 | 16 | relation | symbolic (sympy) | VERIFIED | equal amplitudes |
| ch16-p17-064 (58) | 16 | relation | symbolic (sympy) | VERIFIED | equal amplitudes |
| ch16-p17-065 (59) | 16 | definition | reference (definition) | DEFINITION | Snell with n0 = 1 |
| ch16-p17-066 | 16 | worked example | numeric (book values) | VERIFIED | arccos(0.9999) = 0.810 deg |
| ch16-p17-067 (60) | 16 | definition | reference (definition) | DEFINITION | half-order thickness change; fringe orders; air film |
| ch16-p19-068 (61) | 16 | definition | reference (definition) | DEFINITION | half-order thickness change; fringe orders; air film |
| ch16-p19-069 (62) | 16 | definition | reference (definition) | DEFINITION | half-order thickness change; fringe orders; air film |
| ch16-p19-070 | 16 | definition | reference (definition) | DEFINITION | half-order thickness change; fringe orders; air film |
| ch16-p19-071 (63) | 16 | definition | reference (definition) | DEFINITION | half-order thickness change; fringe orders; air film |
| ch16-p22-072 (64) | 16 | definition | reference (definition) | DEFINITION | Newton's rings: air-gap orders |
| ch16-p22-073 (65) | 16 | definition | reference (definition) | DEFINITION | Newton's rings: air-gap orders |
| ch16-p22-074 (66) | 16 | relation | symbolic (sympy) | VERIFIED | sag s = x^2/(2R) |
| ch16-p22-075 (67) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 66 with s = nu lambda/2 and s = mu lambda/4 |
| ch16-p22-076 | 16 | relation | symbolic (sympy) | VERIFIED | Eq 66 with s = nu lambda/2 and s = mu lambda/4 |
| ch16-p23-077 (68) | 16 | relation | symbolic (sympy) | VERIFIED | difference of two sags |
| ch16-p23-078 (69) | 16 | relation | symbolic (sympy) | FLAG | sign: solving Eq 68 with s = nu lambda/2 gives x^2 = R1 R2 nu lambda/(R2 - R1); the printed R1 - R2 is inconsistent with Eqs 68 and 70 (which uses R2 - R1). 1962 ORIGINAL (sic, scan p.16-23 prints R1 - R2): the text says Eq 69 reduces to Eq 67 as R2 -> infinity, which only R2 - R1 does |
| ch16-p23-079 (70) | 16 | relation | symbolic (sympy) | VERIFIED | R2 - R1 = R1 R2 nu lambda/x^2 ~ (R2/x)^2 nu lambda for R1 ~ R2 |
| ch16-p25-080 (71) | 16 | definition | reference (definition) | DEFINITION | reference plane wave and spherical wave from a point at R/2 |
| ch16-p25-081 (72) | 16 | definition | reference (definition) | DEFINITION | reference plane wave and spherical wave from a point at R/2 |
| ch16-p25-082 (73) | 16 | definition | reference (definition) | DEFINITION | reference plane wave and spherical wave from a point at R/2 |
| ch16-p25-083 (74) | 16 | relation | symbolic (sympy) | VERIFIED | z = 0 |
| ch16-p25-084 | 16 | relation | symbolic (sympy) | VERIFIED | k = 2 pi/lambda |
| ch16-p25-085 (75) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 74 with delta1 |
| ch16-p25-086 (76) | 16 | definition | reference (definition) | DEFINITION | bright/dark orders |
| ch16-p25-087 (77) | 16 | definition | reference (definition) | DEFINITION | bright/dark orders |
| ch16-p25-088 | 16 | relation | symbolic (sympy) | VERIFIED | factor R/2 |
| ch16-p25-089 (78) | 16 | relation | symbolic (sympy) | VERIFIED | binomial to first order |
| ch16-p25-090 (79) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 76 with Eq 78 |
| ch16-p25-091 (80) | 16 | definition | reference (definition) | DEFINITION | dark-fringe condition |
| ch16-p26-092 | 16 | relation | symbolic (sympy) | VERIFIED | with delta0 = pi: r_mu^2 = lambda R (mu + 1)/2 |
| ch16-p26-093 (81) | 16 | relation | symbolic (sympy) | VERIFIED | with delta0 = pi: r_mu^2 = lambda R (mu + 1)/2 |
| ch16-p26-094 (82) | 16 | definition | reference (definition) | DEFINITION | complex number and conjugate |
| ch16-p26-095 (83) | 16 | definition | reference (definition) | DEFINITION | complex number and conjugate |
| ch16-p26-096 (84) | 16 | relation | symbolic (sympy) | VERIFIED | real/imaginary parts and \|Z\|^2 |
| ch16-p26-097 (85) | 16 | relation | symbolic (sympy) | VERIFIED | real/imaginary parts and \|Z\|^2 |
| ch16-p26-098 (86) | 16 | relation | symbolic (sympy) | VERIFIED | real/imaginary parts and \|Z\|^2 |
| ch16-p26-099 (87) | 16 | relation | symbolic (sympy) | VERIFIED | Euler form; a = \|Z\| cos, b = \|Z\| sin, tan = b/a |
| ch16-p26-100 (88) | 16 | relation | symbolic (sympy) | VERIFIED | Euler form; a = \|Z\| cos, b = \|Z\| sin, tan = b/a |
| ch16-p26-101 (89) | 16 | relation | symbolic (sympy) | VERIFIED | Euler form; a = \|Z\| cos, b = \|Z\| sin, tan = b/a |
| ch16-p26-102 (90) | 16 | relation | symbolic (sympy) | VERIFIED | Euler form; a = \|Z\| cos, b = \|Z\| sin, tan = b/a |
| ch16-p27-103 | 16 | relation | symbolic (sympy) | VERIFIED | Maclaurin series of cos, sin, exp(i theta) |
| ch16-p27-104 | 16 | relation | symbolic (sympy) | VERIFIED | Maclaurin series of cos, sin, exp(i theta) |
| ch16-p27-105 | 16 | relation | symbolic (sympy) | VERIFIED | Maclaurin series of cos, sin, exp(i theta) |
| ch16-p27-106 | 16 | relation | symbolic (sympy) | VERIFIED | Maclaurin series of cos, sin, exp(i theta) |
| ch16-p27-107 (91) | 16 | relation | symbolic (sympy) | VERIFIED | products/quotients of polar forms; conjugate |
| ch16-p27-108 (92) | 16 | relation | symbolic (sympy) | VERIFIED | products/quotients of polar forms; conjugate |
| ch16-p28-109 (93) | 16 | relation | symbolic (sympy) | VERIFIED | products/quotients of polar forms; conjugate |
| ch16-p28-110 (94) | 16 | relation | symbolic + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-28): the amplitude a is dropped from the sine term; a e^{i(phi - wt)} = a[cos + i sin] |
| ch16-p28-111 (95) | 16 | relation | symbolic (sympy) | VERIFIED | \|E\|^2 = E E-bar = a^2 |
| ch16-p28-112 (96) | 16 | relation | symbolic (sympy) | VERIFIED | \|E\|^2 = E E-bar = a^2 |
| ch16-p28-113 (97) | 16 | definition | reference (definition) | DEFINITION | complex transmittance (printed e^{ind}: the wave number k is implied in the exponent) |
| ch16-p28-114 (98) | 16 | definition | reference (definition) | DEFINITION | transmitted wave |
| ch16-p28-115 (99) | 16 | relation | reference + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-28): amplitude a dropped, as in Eq 94; E' = rho a e^{i(...)} |
| ch16-p29-116 (100) | 16 | definition | reference (definition) | DEFINITION | Snell through the plate; round-trip phase alpha; successive transmitted amplitudes |
| ch16-p29-117 (101) | 16 | definition | reference (definition) | DEFINITION | Snell through the plate; round-trip phase alpha; successive transmitted amplitudes |
| ch16-p29-118 | 16 | definition | reference (definition) | DEFINITION | Snell through the plate; round-trip phase alpha; successive transmitted amplitudes |
| ch16-p29-119 | 16 | definition | reference (definition) | DEFINITION | Snell through the plate; round-trip phase alpha; successive transmitted amplitudes |
| ch16-p29-120 | 16 | definition | reference (definition) | DEFINITION | Snell through the plate; round-trip phase alpha; successive transmitted amplitudes |
| ch16-p30-121 (102) | 16 | relation | reference (standard form) | VERIFIED | sum of transmitted amplitudes |
| ch16-p30-122 (103) | 16 | definition | reference (definition) | DEFINITION | round-trip amplitude factor A |
| ch16-p30-123 (104) | 16 | relation | symbolic (sympy) | VERIFIED | finite geometric series (checked for N = 5) |
| ch16-p30-124 (105) | 16 | relation | reference (standard form) | VERIFIED | Eq 102 with Eq 104 |
| ch16-p30-125 (106) | 16 | relation | numeric (book values) | VERIFIED | \|Eq 105\|^2 equals Eq 106 (N = 5, three test points) |
| ch16-p30-126 (107) | 16 | relation | symbolic (sympy) | VERIFIED | N -> infinity with A < 1 |
| ch16-p30-127 (108) | 16 | definition | reference (definition) | DEFINITION | maxima |
| ch16-p30-128 (109) | 16 | relation | symbolic (sympy) | VERIFIED | weak reflection: first order in A |
| ch16-p31-129 (110) | 16 | relation | reference (standard form) | VERIFIED | Eq 107 at alpha = 2 pi nu: 2W = tau^2/(1-A)^2 (B^2 = half the numerator) |
| ch16-p31-130 (111) | 16 | definition | reference (definition) | DEFINITION | offset from a peak |
| ch16-p31-131 (112) | 16 | relation | symbolic (sympy) | VERIFIED | half-maximum: 1 - 2A cos(da) + A^2 = 2(1-A)^2 with cos(da) ~ 1 - da^2/2 gives da = (1-A)/sqrt(A) |
| ch16-p31-132 (113) | 16 | relation | symbolic (sympy) | VERIFIED | half-maximum: 1 - 2A cos(da) + A^2 = 2(1-A)^2 with cos(da) ~ 1 - da^2/2 gives da = (1-A)/sqrt(A) |
| ch16-p32-133 | 16 | definition | reference (definition) | DEFINITION | successive reflected amplitudes |
| ch16-p32-134 | 16 | definition | reference (definition) | DEFINITION | successive reflected amplitudes |
| ch16-p32-135 | 16 | definition | reference (definition) | DEFINITION | successive reflected amplitudes |
| ch16-p32-136 (114) | 16 | definition | reference (definition) | DEFINITION | successive reflected amplitudes |
| ch16-p32-137 (115) | 16 | relation | reference + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-32): exponent printed e^{(alpha - delta_1,0)} without the i; the sum otherwise follows from Eq 114 terms |
| ch16-p32-138 (116) | 16 | definition | reference (definition) | DEFINITION | Eq 116 definition of C |
| ch16-p32-139 | 16 | relation | reference (standard form) | VERIFIED | alpha = 2 pi nu: e^{i nu alpha} = 1 |
| ch16-p32-140 (117) | 16 | relation | symbolic (sympy) + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-32): factoring r01 e^{i delta01} out of the previous line leaves C/r01, not C, inside the bracket (expanding the printed form gives r01 C e^{-i delta10} sum A^nu). The conclusion Eq 118 is unaffected |
| ch16-p32-141 (118) | 16 | definition | reference (definition) | DEFINITION | phase condition for dark reflected fringes |
| ch16-p34-142 | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-143 | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-144 | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-145 | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-146 | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-147 | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-148 (119) | 16 | definition | reference (definition) | DEFINITION | multiple beams between wedge plates: successive tilted waves; R, tau, phi definitions |
| ch16-p34-149 (120) | 16 | relation | reference (standard form) | VERIFIED | sum of the transmitted waves |
| ch16-p34-150 (121) | 16 | definition | reference (definition) | DEFINITION | small-angle approximations |
| ch16-p34-151 | 16 | definition | reference (definition) | DEFINITION | small-angle approximations |
| ch16-p36-152 (122) | 16 | relation | symbolic (sympy) | VERIFIED | phase of the nu-th wave with sin 2 nu alpha -> 2 nu alpha |
| ch16-p36-153 (123) | 16 | relation | reference (standard form) | VERIFIED | geometric sum and its modulus, as Eqs 104-106 |
| ch16-p36-154 (124) | 16 | relation | reference (standard form) | VERIFIED | geometric sum and its modulus, as Eqs 104-106 |
| ch16-p36-155 (119) | 16 | relation | reference (standard form) | VERIFIED | geometric sum and its modulus, as Eqs 104-106 |
| ch16-p37-156 (125) | 16 | relation | symbolic (sympy) | VERIFIED | 2knx alpha = 4 pi n x alpha/lambda |
| ch16-p37-157 (126) | 16 | definition | reference (definition) | DEFINITION | wedge thickness |
| ch16-p37-158 (127) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 127 from Eq 125 |
| ch16-p37-159 (128) | 16 | relation | symbolic (sympy) | VERIFIED | fringe spacing |
| ch16-p39-160 (129) | 16 | relation | symbolic (sympy) | VERIFIED | step height from fringe shift; with h = lambda/(2 n alpha): t = alpha dx |
| ch16-p39-161 (130) | 16 | relation | symbolic (sympy) | VERIFIED | step height from fringe shift; with h = lambda/(2 n alpha): t = alpha dx |
| ch16-p41-162 (131) | 16 | relation | reference (standard form) | VERIFIED | Eq 127 with n = 1, f = -phi/(2 pi) |
| ch16-p44-163 (132) | 16 | definition | reference (definition) | DEFINITION | phase-change dispersion expansion |
| ch16-p44-164 (133) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 133 agrees with Eq 131 + Eq 132 to first order about lambda0, with s0 = f0 + b lambda0 |
| ch16-p44-165 (134) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 133 agrees with Eq 131 + Eq 132 to first order about lambda0, with s0 = f0 + b lambda0 |
| ch16-p44-166 (135) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 136 from Eq 135 |
| ch16-p44-167 (136) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 136 from Eq 135 |
| ch16-p44-168 (137) | 16 | relation | reference (standard form) | VERIFIED | Eq 137 from Eq 133; difference of two thicknesses (same order: t = (nu - s0)(lambda_nu - lambda_mu)/2) |
| ch16-p44-169 (138) | 16 | relation | reference (standard form) | VERIFIED | Eq 137 from Eq 133; difference of two thicknesses (same order: t = (nu - s0)(lambda_nu - lambda_mu)/2) |
| ch16-p44-170 (139) | 16 | relation | reference (standard form) | VERIFIED | Eq 137 from Eq 133; difference of two thicknesses (same order: t = (nu - s0)(lambda_nu - lambda_mu)/2) |
| ch16-p45-171 (140) | 16 | relation | reference (standard form) | VERIFIED | error propagation of Eq 139 with independent errors <= \|dlambda\| in each wavelength |
| ch16-p45-172 | 16 | definition | reference (definition) | DEFINITION | Huygens construction for refraction |
| ch16-p45-173 | 16 | definition | reference (definition) | DEFINITION | Huygens construction for refraction |
| ch16-p45-174 | 16 | definition | reference (definition) | DEFINITION | Huygens construction for refraction |
| ch16-p45-175 | 16 | relation | symbolic (sympy) | VERIFIED | Snell's law from wavelet speeds |
| ch16-p47-176 (141) | 16 | definition | reference (definition) | DEFINITION | Huygens-Fresnel wavelet, distance, superposition integral, S |
| ch16-p47-177 (142) | 16 | definition | reference (definition) | DEFINITION | Huygens-Fresnel wavelet, distance, superposition integral, S |
| ch16-p48-178 (143) | 16 | definition | reference (definition) | DEFINITION | Huygens-Fresnel wavelet, distance, superposition integral, S |
| ch16-p48-179 (144) | 16 | definition | reference (definition) | DEFINITION | Huygens-Fresnel wavelet, distance, superposition integral, S |
| ch16-p48-180 (145) | 16 | relation | symbolic (sympy) | VERIFIED | r rewritten about S |
| ch16-p48-181 (146) | 16 | relation | symbolic (sympy) | VERIFIED | first-order binomial, quadratic aperture terms dropped |
| ch16-p48-182 (147) | 16 | relation | symbolic (sympy) | VERIFIED | first-order binomial, quadratic aperture terms dropped |
| ch16-p48-183 (148) | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p48-184 (149) | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p48-185 | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p48-186 | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p49-187 (150) | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p49-188 (151) | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p49-189 (152) | 16 | relation | reference (standard form) | VERIFIED | Fraunhofer integral, definitions; uniform aperture |
| ch16-p49-190 | 16 | relation | symbolic (sympy) | VERIFIED | rectangular aperture integral |
| ch16-p49-191 | 16 | relation | symbolic (sympy) | VERIFIED | rectangular aperture integral |
| ch16-p49-192 (153) | 16 | relation | symbolic (sympy) | VERIFIED | each factor = 2a sinc(2 pi a n x/S lambda); W = \|F0\|^2/S^2 with A = 4ab |
| ch16-p49-193 (154) | 16 | relation | symbolic (sympy) | VERIFIED | each factor = 2a sinc(2 pi a n x/S lambda); W = \|F0\|^2/S^2 with A = 4ab |
| ch16-p49-194 (155) | 16 | relation | symbolic (sympy) | VERIFIED | each factor = 2a sinc(2 pi a n x/S lambda); W = \|F0\|^2/S^2 with A = 4ab |
| ch16-p49-195 (156) | 16 | relation | symbolic (sympy) | VERIFIED | zeros of the sinc |
| ch16-p50-196 (157) | 16 | definition | reference (definition) | DEFINITION | polar coordinates on aperture and image |
| ch16-p50-197 (158) | 16 | definition | reference (definition) | DEFINITION | polar coordinates on aperture and image |
| ch16-p50-198 (159) | 16 | definition | reference (definition) | DEFINITION | polar coordinates on aperture and image |
| ch16-p50-199 (160) | 16 | definition | reference (definition) | DEFINITION | polar coordinates on aperture and image |
| ch16-p50-200 (161) | 16 | definition | reference (definition) | DEFINITION | polar coordinates on aperture and image |
| ch16-p50-201 (162) | 16 | relation | numeric (book values) | VERIFIED | Bessel integral checked by quadrature at three arguments |
| ch16-p50-202 (163) | 16 | relation | reference (standard form) | VERIFIED | Eq 159 with Eq 162 |
| ch16-p51-203 (164) | 16 | relation | symbolic (sympy) | VERIFIED | change of variable v = knru/S |
| ch16-p51-204 (165) | 16 | relation | symbolic (sympy) | VERIFIED | substitution v = knru/S gives the (S/knr)^2 form (evaluated with Eq 166) |
| ch16-p51-205 (166) | 16 | relation | symbolic (sympy) | VERIFIED | d/dz [z J1(z)] = z J0(z) |
| ch16-p51-206 | 16 | relation | symbolic (sympy) | VERIFIED | rearranged to 2 pi a^2 J1(z)/z |
| ch16-p51-207 (167) | 16 | relation | symbolic + scan | FIXED | transcription error, FIXED per scan p.16-51: the n in the denominator (2 pi n a r)/lambda S had been dropped; fixed form equals the previous line with k = 2 pi/lambda |
| ch16-p51-208 (168) | 16 | definition | reference (definition) | DEFINITION | sin theta = r/S |
| ch16-p51-209 (169) | 16 | relation | reference (standard form) | VERIFIED | Eq 167 with Eq 168 |
| ch16-p52-210 (170) | 16 | worked example | numeric (book values) | VERIFIED | first zero of J1 = 3.8317: sin(theta1) = 0.6098 lambda/(n a) = 1.22 lambda/(2an) |
| ch16-p52-211 (171) | 16 | relation | symbolic (sympy) | VERIFIED | W = \|F0\|^2/S^2 |
| ch16-p53-212 (172) | 16 | definition | reference (definition) | DEFINITION | converging spherical wave: optical path, aperture distribution, integral, r1 |
| ch16-p53-213 (173) | 16 | definition | reference (definition) | DEFINITION | converging spherical wave: optical path, aperture distribution, integral, r1 |
| ch16-p53-214 (174) | 16 | definition | reference (definition) | DEFINITION | converging spherical wave: optical path, aperture distribution, integral, r1 |
| ch16-p53-215 (175) | 16 | definition | reference (definition) | DEFINITION | converging spherical wave: optical path, aperture distribution, integral, r1 |
| ch16-p53-216 (176) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 176 |
| ch16-p53-217 (177) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 177 first-order binomial |
| ch16-p53-218 (178) | 16 | relation | symbolic + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-53): Eqs 176-177 give r1 = sqrt(Q) - (x zeta + y eta - R z)/sqrt(Q), Q = R^2 + zeta^2 + eta^2; the printed denominator lacks the square root. Eq 179 uses the correct sqrt(Q) |
| ch16-p53-219 (179) | 16 | relation | reference (standard form) | VERIFIED | Eq 174 with Eq 178; \|e^{...}\| = 1 so W = \|F0\|^2 |
| ch16-p53-220 (180) | 16 | relation | reference (standard form) | VERIFIED | Eq 174 with Eq 178; \|e^{...}\| = 1 so W = \|F0\|^2 |
| ch16-p53-221 (181) | 16 | relation | reference (standard form) | VERIFIED | Eq 174 with Eq 178; \|e^{...}\| = 1 so W = \|F0\|^2 |
| ch16-p54-222 (182) | 16 | definition | reference (definition) | DEFINITION | change of variables to aperture angle U |
| ch16-p54-223 (183) | 16 | relation | symbolic (sympy) | VERIFIED | cos U = R/sqrt(Q) and the direction sines |
| ch16-p54-224 (184) | 16 | relation | symbolic (sympy) | VERIFIED | cos U = R/sqrt(Q) and the direction sines |
| ch16-p54-225 | 16 | relation | symbolic (sympy) | VERIFIED | Jacobian R^2 sin U/cos^3 U |
| ch16-p54-226 (185) | 16 | relation | symbolic (sympy) | VERIFIED | Jacobian R^2 sin U/cos^3 U |
| ch16-p55-227 (186) | 16 | relation | symbolic (sympy) | VERIFIED | 1/Q x Jacobian = tan U |
| ch16-p55-228 (187) | 16 | definition | reference (definition) | DEFINITION | rho = sin U |
| ch16-p55-229 (188) | 16 | relation | symbolic (sympy) | VERIFIED | dU = d rho/cos U: tan U dU = rho d rho/(1 - rho^2); cos U = sqrt(1 - rho^2) |
| ch16-p55-230 (189) | 16 | relation | reference (standard form) | VERIFIED | z = 0 and 1/(1 - rho^2) ~ 1 (moderate aperture), as stated |
| ch16-p55-231 (190) | 16 | definition | reference (definition) | DEFINITION | polar image coordinates |
| ch16-p55-232 (191) | 16 | relation | reference (standard form) | VERIFIED | same angular integration as Eqs 159-163 |
| ch16-p55-233 (192) | 16 | relation | reference (standard form) | VERIFIED | same angular integration as Eqs 159-163 |
| ch16-p55-234 (193) | 16 | relation | numeric (book values) | VERIFIED | Eq 193 = Eq 192 by quadrature (rho_m = 0.4, three values of knr) |
| ch16-p55-235 (194) | 16 | definition | reference (definition) | DEFINITION | image-space numerical aperture |
| ch16-p55-236 (195) | 16 | relation | symbolic (sympy) | VERIFIED | W = \|F0\|^2 |
| ch16-p55-237 (196) | 16 | worked example | numeric (book values) | VERIFIED | 3.8317/(2 pi) = 0.6098 |
| ch16-p56-238 (197) | 16 | relation | numeric (book values) | VERIFIED | 3.8317/(2 pi) = 0.6098 |
| ch16-p56-239 (198) | 16 | relation | reference (standard form) | VERIFIED | object-space radius via the sine condition: \|M\| n sin U_m = n0 sin U_0m = N.A. |
| ch16-p56-240 (199) | 16 | relation | reference (standard form) | VERIFIED | object-space radius via the sine condition: \|M\| n sin U_m = n0 sin U_0m = N.A. |
| ch16-p56-241 (200) | 16 | relation | reference (standard form) | VERIFIED | object-space radius via the sine condition: \|M\| n sin U_m = n0 sin U_0m = N.A. |
| ch16-p56-242 (201) | 16 | definition | reference (definition) | DEFINITION | angular radius at the image distance V; small-angle aperture |
| ch16-p56-243 (202) | 16 | definition | reference (definition) | DEFINITION | angular radius at the image distance V; small-angle aperture |
| ch16-p56-244 (203) | 16 | worked example | numeric (book values) | VERIFIED | rho_m = D/(2V): theta1 = 2(0.6098) lambda/(nD) = 1.22 lambda/(nD) |
| ch16-p58-245 (204) | 16 | relation | reference (standard form) | VERIFIED | defocused pupil function |
| ch16-p58-246 (205) | 16 | relation | reference (standard form) | VERIFIED | defocused pupil function |
| ch16-p58-247 (206) | 16 | relation | reference (standard form) | VERIFIED | defocused pupil function |
| ch16-p58-248 (207) | 16 | relation | symbolic (sympy) | VERIFIED | first-order expansion |
| ch16-p58-249 (208) | 16 | relation | symbolic + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-58): e^{iknz sqrt(1-rho^2)} ~ e^{iknz} e^{-i pi n z rho^2/lambda}; the book prints +i. Harmless: only \|F0\| is used afterwards |
| ch16-p58-250 | 16 | relation | symbolic + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-58): integral of e^{i c rho^2} rho d rho = (e^{i c rho_m^2} - 1)/(2 i c), so F0(0) = pi e^{iknz}[...]/(i pi n z/lambda); the printed 2 pi doubles the amplitude (W 4x too large; in focus it must equal Eq 195's value pi^2 rho_m^4) |
| ch16-p58-251 (209) | 16 | relation | symbolic + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-58): integral of e^{i c rho^2} rho d rho = (e^{i c rho_m^2} - 1)/(2 i c), so F0(0) = pi e^{iknz}[...]/(i pi n z/lambda); the printed 2 pi doubles the amplitude (W 4x too large; in focus it must equal Eq 195's value pi^2 rho_m^4) |
| ch16-p58-252 | 16 | relation | symbolic (sympy) | VERIFIED | \|e^{iw} - 1\|^2 = 2 - 2 cos w |
| ch16-p58-253 | 16 | relation | symbolic (sympy) | VERIFIED | \|e^{iw} - 1\|^2 = 2 - 2 cos w |
| ch16-p58-254 (210) | 16 | relation | symbolic (sympy) | VERIFIED | 1 - cos w = 2 sin^2(w/2) (consistent with the book's Eq 209) |
| ch16-p58-255 (211) | 16 | relation | symbolic + scan | FLAG | 1962 ORIGINAL (sic, scan p.16-58): Eq 210 at z = 0 gives 4 pi^2 rho_m^4, not the printed 4 pi rho_m^4 (and the correctly normalised in-focus value is pi^2 rho_m^4, see Eq 250). The ratio K (Eq 212) is unaffected |
| ch16-p59-256 (212) | 16 | relation | symbolic (sympy) | VERIFIED | normalised Strehl-type ratio |
| ch16-p59-257 (213) | 16 | definition | reference (definition) | DEFINITION | quarter-wave-type defocus criterion |
| ch16-p59-258 (214) | 16 | relation | numeric (book values) | VERIFIED | at pi z n rho_m^2/lambda = pi/2: K = [sin(pi/4)/(pi/4)]^2 = 0.8106 |
| ch16-p59-259 (215) | 16 | relation | symbolic (sympy) | VERIFIED | Eq 213 solved for \|z\| |
| ch17-p01-001 (1) | 17 | relation | numeric (book values) | VERIFIED | Fresnel unpolarised reflectance; its normal-incidence limit reproduces Eq 2 (n = 1.5 -> 0.0400) |
| ch17-p01-002 (2) | 17 | relation | numeric (book values) | VERIFIED | Eq 2; used below: (0.52/2.52)^2 = 0.0426 |
| ch17-p01-003 (3) | 17 | relation | reference (standard form) | VERIFIED | Lambert absorption law, natural and decimal forms (beta = alpha log10 e) |
| ch17-p02-004 (4) | 17 | relation | reference (standard form) | VERIFIED | extinction coefficient kappa = alpha lambda/(4 pi n) (Born & Wolf convention with k = n kappa) |
| ch17-p02-005 (5) | 17 | relation | reference (standard form) | VERIFIED | Lambert absorption law, natural and decimal forms (beta = alpha log10 e) |
| ch17-p02-006 (6) | 17 | relation | reference (standard form) | VERIFIED | Lambert absorption law, natural and decimal forms (beta = alpha log10 e) |
| ch17-p02-007 (7) | 17 | definition | reference (definition) | DEFINITION | single pass through two surfaces |
| ch17-p02-008 (8) | 17 | relation | reference (standard form) | VERIFIED | multiple incoherent reflections: geometric series (1-R)^2 T sum (T R)^(2k) |
| ch17-p02-009 (9) | 17 | relation | symbolic (sympy) | FLAG | 1962 ORIGINAL (sic, as printed): misplaced parentheses; literal form gives T ~ 308 for the example. Eq 8 rearranges to the next line (verified symbolically), which gives T = 0.962 vs the text's 0.960 |
| ch17-p02-010 | 17 | relation | symbolic (sympy) | VERIFIED | corrected form: Eq 8, T_inf (1 - T^2 R^2) = (1-R)^2 T, divided by R^2 T_inf |
| ch17-p03-011 | 17 | worked example | numeric (book values) | VERIFIED | (0.52/2.52)^2 = 0.0426 -> 0.043 |
| ch17-p03-012 | 17 | relation | numeric (book values) | VERIFIED | Eq 7 with T1 = 0.883 (measured), R = 0.043: T = 0.9641 |
| ch17-p03-013 | 17 | worked example | numeric (book values) | VERIFIED | -log10(0.964)/6.18 mm = 0.002575/mm |
| ch17-p03-014 | 17 | worked example | numeric (book values) | VERIFIED | 10^(-0.00257 x 25.4) = 0.8603 |
| ch17-p03-015 | 17 | relation | numeric (book values) | VERIFIED | Eq 7 with T1 = 0.914, R = 0.043: T = 0.9980 |
| ch17-p03-016 | 17 | worked example | numeric (book values) | VERIFIED | -log10(0.995)/6.61 mm = 0.000329/mm (text gives the sample as 6.6 mm) |
| ch17-p04-017 | 17 | relation | reference (standard form) | VERIFIED | IR 'nu' analogue (n-1)/(dn/dlambda) for a narrow band |
| ch17-p04-018 | 17 | relation | symbolic (sympy) | VERIFIED | achromat condition phi1/V1 + phi2/V2 = 0, or with phi = c(n-1): c1 dn1 + c2 dn2 = 0 |
| ch17-p07-019 | 17 | relation | none | NOT VERIFIED | fluorite partial dispersion 0.293 needs the book's 1962 index data; modern CaF2 (n_C 1.43249, n_D 1.43384, n_F 1.43704) gives 0.297 |
| ch18-p01-001 (1) | 18 | relation | reference (standard form) | VERIFIED | Bouguer-Lambert attenuation |
| ch18-p01-002 | 18 | definition | reference (definition) | DEFINITION | extinction = absorption + scattering |
| ch18-p02-003 (2) | 18 | relation | reference (standard form) | VERIFIED | Rayleigh scattering ~ lambda^-4 |
| ch18-p02-004 | 18 | relation | numeric (book values) | VERIFIED | 1.8^4 = 10.5 ~ 10 (violet vs red wavelength ratio ~1.8) |
| ch19-p02-001 (1) | 19 | definition | reference (definition) | DEFINITION | spherical aberration as an even power series in aperture |
| ch19-p04-002 | 19 | definition | reference (definition) | DEFINITION | air-space relation for Fig 19.4 (a - b = c in the figure's lengths) |
| ch19-p08-003 (2) | 19 | relation | numeric (book values) | VERIFIED | Dawes limit 4.56"/D(in); the book rounds to 4.5/a |
| ch19-p08-004 (3) | 19 | relation | numeric (book values) | VERIFIED | empirical coma-limited field rule reproduces the text's own examples: f/5 -> 1 inch, f/10 -> 4 inches |
| ch19-p10-005 (4) | 19 | definition | reference (definition) | DEFINITION | Eq 4 sag power series |
| ch19-p10-006 (5) | 19 | relation | symbolic (sympy) | VERIFIED | a1 = 1/(2r) from the sphere's sag expansion |
| ch19-p10-007 (6) | 19 | relation | symbolic (sympy) | VERIFIED | a1 = 1/(2r) from the sphere's sag expansion |
| ch19-p10-008 (7) | 19 | relation | symbolic (sympy) | VERIFIED | a1 = 1/(2r) from the sphere's sag expansion |
| ch19-p10-009 (8) | 19 | relation | numeric (consistency) | FLAG | P = 2Nc agrees with ch08 Eq 14 only for N = 1: for a mirror (n = -N) Eq 8-(14) gives P = c(N + N)/(N(-N)) = -2c/N (magnitude 2c/N). Sign follows the chapter's convention; the N-dependence differs (scan not re-read) |
| ch19-p12-010 (9) | 19 | relation | symbolic (sympy) | VERIFIED | paraboloid -x = y^2/(2r) exactly |
| ch19-p13-011 (10) | 19 | relation | symbolic (sympy) | VERIFIED | sphere sag to y^4: 1/(8r^3) |
| ch19-p13-012 (11) | 19 | relation | symbolic (sympy) | VERIFIED | y^4 coefficient 2/(8r^3) is the conic K = +1 (oblate spheroid), consistent with the text's classification |
| ch20-p04-001 (1) | 20 | definition | reference (definition) | DEFINITION | phase thickness delta = 2 pi sigma n t (sigma = 1/lambda) |
| ch20-p05-002 | 20 | relation | numeric (book values) | VERIFIED | 1 um = 1000 m-mu = 10,000 A <-> 10,000 cm^-1 (sigma = 1/lambda) |
| ch20-p05-003 (2) | 20 | definition | reference (definition) | DEFINITION | quarter-wave optical thickness QWOT = 4 n t |
| ch20-p05-004 | 20 | relation | reference (standard form) | VERIFIED | wave in a medium: lambda' = lambda/n |
| ch20-p05-005 | 20 | relation | reference (standard form) | VERIFIED | wave in a medium: lambda' = lambda/n |
| ch20-p05-006 | 20 | relation | reference (standard form) | VERIFIED | wave in a medium: lambda' = lambda/n |
| ch20-p06-007 (3) | 20 | definition | reference (definition) | DEFINITION | unpolarised averages |
| ch20-p09-008 (7) | 20 | relation | reference (standard form) | VERIFIED | stack matrix = ordered product of layer matrices |
| ch20-p09-009 (8) | 20 | relation | reference (standard form) | VERIFIED | stack matrix = ordered product of layer matrices |
| ch20-p09-010 (9) | 20 | relation | numeric (book values) | VERIFIED | Eqs 9-11 (k_s = 0) equal an independent admittance calculation on 20 random lossless stacks, and R + T = 1 (Eq 11's '2' is 2 det M = 2(AD + BC)) |
| ch20-p09-011 | 20 | relation | numeric (book values) | VERIFIED | Eqs 9-11 (k_s = 0) equal an independent admittance calculation on 20 random lossless stacks, and R + T = 1 (Eq 11's '2' is 2 det M = 2(AD + BC)) |
| ch20-p09-012 (10) | 20 | relation | numeric (book values) | VERIFIED | Eqs 9-11 (k_s = 0) equal an independent admittance calculation on 20 random lossless stacks, and R + T = 1 (Eq 11's '2' is 2 det M = 2(AD + BC)) |
| ch20-p09-013 (11) | 20 | relation | numeric (book values) | VERIFIED | Eqs 9-11 (k_s = 0) equal an independent admittance calculation on 20 random lossless stacks, and R + T = 1 (Eq 11's '2' is 2 det M = 2(AD + BC)) |
| ch20-p09-014 (12) | 20 | relation | numeric (book values) | VERIFIED | unit matrix: a full-wave layer (or absentee half-wave, up to sign) leaves R unchanged |
| ch20-p09-015 (13) | 20 | relation | reference (standard form) | VERIFIED | tilted phase thickness n t cos(theta); s-polarisation effective index n cos(theta) |
| ch20-p12-016 (14) | 20 | relation | reference (standard form) | VERIFIED | tilted phase thickness n t cos(theta); s-polarisation effective index n cos(theta) |
| ch20-p12-017 (15) | 20 | relation | reference (standard form) | VERIFIED | p-polarisation effective index n/cos(theta) |
| ch20-p12-018 (16) | 20 | relation | reference (standard form) | VERIFIED | n_i cos(theta_i) = sqrt(n_i^2 - n_0^2 sin^2 theta_0) at grazing incidence (theta_0 = 90 deg) |
| ch20-p14-019 | 20 | worked example | numeric (book values) | VERIFIED | 0.977 : 1.56 : 2.14 = 1 : 1.597 : 2.190 |
| ch20-p14-020 (19) | 20 | worked example | numeric (book values) | VERIFIED | 0.977 : 1.56 : 2.14 = 1 : 1.597 : 2.190 |
| ch20-p14-021 (20) | 20 | definition | reference (definition) | DEFINITION | ratio set as printed |
| ch20-p18-022 (21) | 20 | relation | numeric (book values) | VERIFIED | bare substrate Fresnel reflectance |
| ch20-p20-023 (23) | 20 | relation | numeric (book values) | VERIFIED | single-layer Eq 23 with a1..a4 equals the matrix result for 10 random layers and wavelengths |
| ch20-p20-024 | 20 | relation | numeric (book values) | VERIFIED | single-layer Eq 23 with a1..a4 equals the matrix result for 10 random layers and wavelengths |
| ch20-p20-025 | 20 | relation | numeric (book values) | VERIFIED | single-layer Eq 23 with a1..a4 equals the matrix result for 10 random layers and wavelengths |
| ch20-p20-026 (24) | 20 | relation | numeric (book values) | VERIFIED | Eq 24 quarter-wave minimum |
| ch20-p21-027 | 20 | definition | reference (definition) | DEFINITION | g = lambda0/lambda |
| ch20-p22-028 (25) | 20 | definition | reference (definition) | DEFINITION | Eq 25: minimum is below the bare value when n1 lies between n0 and ns |
| ch20-p22-029 (26) | 20 | relation | numeric (book values) | VERIFIED | Eq 26: n1 = sqrt(n0 ns) gives R = 0 |
| ch20-p25-030 | 20 | worked example | numeric (book values) | VERIFIED | example (a): MgF2 (1.38) quarter wave at 700 m-mu on n = 1.51, g = 0.737: R = 0.0180 (book reads 0.017 from Fig 20.16) |
| ch20-p27-031 | 20 | definition | reference (definition) | DEFINITION | g = lambda0/lambda |
| ch20-p30-032 (29) | 20 | relation | symbolic (sympy) | VERIFIED | product of two quarter-wave matrices: -diag(n2/n1, n1/n2) |
| ch20-p30-033 (30) | 20 | relation | numeric (book values) | VERIFIED | Eq 30 double quarter-wave R equals the matrix result (10 random cases) |
| ch20-p30-034 (31) | 20 | relation | symbolic (sympy) | VERIFIED | Eq 31 zeroes Eq 30 |
| ch20-p30-035 (32a) | 20 | worked example | numeric (book values) | VERIFIED | on n_s = 1.51: 1.38 x sqrt(1.51) = 1.696, 1.65 x sqrt(1.51) = 2.028 (book 1.69, 2.03) |
| ch20-p30-036 (32b) | 20 | worked example | numeric (book values) | VERIFIED | on n_s = 1.51: 1.38 x sqrt(1.51) = 1.696, 1.65 x sqrt(1.51) = 2.028 (book 1.69, 2.03) |
| ch20-p30-037 (33) | 20 | relation | reference (standard form) | VERIFIED | Berning's quarter-half design conditions (geometric progression of indices) |
| ch20-p30-038 (34) | 20 | relation | symbolic (sympy) | VERIFIED | Eq 34 follows from Eq 33 |
| ch20-p33-039 (35) | 20 | definition | reference (definition) | DEFINITION | index-order and three-layer design conditions |
| ch20-p36-040 (36a) | 20 | definition | reference (definition) | DEFINITION | index-order and three-layer design conditions |
| ch20-p36-041 (36b) | 20 | definition | reference (definition) | DEFINITION | index-order and three-layer design conditions |
| ch20-p36-042 (37) | 20 | definition | reference (definition) | DEFINITION | index-order and three-layer design conditions |
| ch20-p42-043 (39) | 20 | relation | numeric (book values) | VERIFIED | Eq 39: edges of the (LH)^N high-reflectance zone from the matrix trace \|A + D\| = 2 match the formula |
| ch20-p42-044 (40) | 20 | relation | symbolic (sympy) | VERIFIED | Eq 40 = 1 - Eq 41 |
| ch20-p42-045 (41) | 20 | relation | symbolic (sympy) | VERIFIED | Eq 40 = 1 - Eq 41 |
| ch20-p42-046 (42) | 20 | relation | numeric (book values) | VERIFIED | Eqs 41-45: peak T of 8-layer (even, Eq 42/45) and 7-layer (odd, Eq 43) quarter-wave stacks from the matrix equals 4/(P + 1/P + 2) exactly, layers numbered from the incident medium; Eq 44 ~4/P within 10% at P = 39 |
| ch20-p42-047 (43) | 20 | relation | numeric (book values) | VERIFIED | Eqs 41-45: peak T of 8-layer (even, Eq 42/45) and 7-layer (odd, Eq 43) quarter-wave stacks from the matrix equals 4/(P + 1/P + 2) exactly, layers numbered from the incident medium; Eq 44 ~4/P within 10% at P = 39 |
| ch20-p42-048 (44) | 20 | relation | numeric (book values) | VERIFIED | Eqs 41-45: peak T of 8-layer (even, Eq 42/45) and 7-layer (odd, Eq 43) quarter-wave stacks from the matrix equals 4/(P + 1/P + 2) exactly, layers numbered from the incident medium; Eq 44 ~4/P within 10% at P = 39 |
| ch20-p42-049 (45) | 20 | relation | numeric (book values) | VERIFIED | Eqs 41-45: peak T of 8-layer (even, Eq 42/45) and 7-layer (odd, Eq 43) quarter-wave stacks from the matrix equals 4/(P + 1/P + 2) exactly, layers numbered from the incident medium; Eq 44 ~4/P within 10% at P = 39 |
| ch20-p45-050 (46) | 20 | definition | reference (definition) | DEFINITION | Eq 46 resonance condition |
| ch20-p50-051 | 20 | definition | reference (definition) | DEFINITION | stack notation; 600/4 = 150 m-mu |
| ch20-p50-052 | 20 | definition | reference (definition) | DEFINITION | stack notation; 600/4 = 150 m-mu |
| ch20-p51-053 (47) | 20 | worked example | numeric (book values) | VERIFIED | (0.92 + 0.879) x 150 = 269.9 = lambda0/2 (q = 1): lambda0 = 540 m-mu (book 540) |
| ch20-p53-054 | 20 | definition | reference (definition) | DEFINITION | stack notation |
| ch20-p58-055 | 20 | relation | symbolic (sympy) | VERIFIED | incoherent double-plate sum with T = 1 - R |
| ch20-p59-056 | 20 | definition | reference (definition) | DEFINITION | stack notation; example value |
| ch20-p60-057 | 20 | definition | reference (definition) | DEFINITION | stack notation; example value |
| ch20-p60-058 (48) | 20 | relation | symbolic (sympy) | VERIFIED | T/(1+R) -> T/2 as R -> 1 |
| ch20-p73-059 (49) | 20 | relation | reference (standard form) | VERIFIED | Airy transmission of a Fabry-Perot etalon, F = 4R/(1-R)^2, R = sqrt(R1 R2) |
| ch20-p73-060 (50) | 20 | relation | reference (standard form) | VERIFIED | Airy transmission of a Fabry-Perot etalon, F = 4R/(1-R)^2, R = sqrt(R1 R2) |
| ch20-p73-061 (51) | 20 | relation | reference (standard form) | VERIFIED | Airy transmission of a Fabry-Perot etalon, F = 4R/(1-R)^2, R = sqrt(R1 R2) |
| ch20-p73-062 (52) | 20 | relation | reference (standard form) | VERIFIED | Airy transmission of a Fabry-Perot etalon, F = 4R/(1-R)^2, R = sqrt(R1 R2) |
| ch20-p73-063 (53) | 20 | relation | reference (standard form) | VERIFIED | Airy transmission of a Fabry-Perot etalon, F = 4R/(1-R)^2, R = sqrt(R1 R2) |
| ch20-p73-064 (54) | 20 | relation | symbolic (sympy) | VERIFIED | peak condition m pi = 2 pi sigma n t with sigma = 1/lambda0 gives m lambda0/2 = n t |
| ch20-p73-065 (55) | 20 | relation | symbolic (sympy) | VERIFIED | peak condition m pi = 2 pi sigma n t with sigma = 1/lambda0 gives m lambda0/2 = n t |
| ch20-p73-066 (56) | 20 | relation | reference (standard form) | VERIFIED | free spectral range 1/(2t) in wave numbers (n = 1 gap) |
| ch20-p74-067 (57) | 20 | definition | reference (definition) | DEFINITION | Q definition |
| ch20-p74-068 (58) | 20 | relation | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.20-74): printed as the product (lambda0/dlambda)(sigma0/dsigma); the footnote shows the two ratios are equal, so the product is Q^2. Read as Q = lambda0/dlambda = sigma0/dsigma = m pi sqrt(R)/(1-R): with R = 0.95, t = 1 cm, lambda = 0.55 um this gives Q = 2.23e+06, the text's 'over two million' |
| ch20-p74-069 (59) | 20 | relation | reference (standard form) | VERIFIED | plane waves, reflected wave with phase epsilon; d(lambda)/lambda = d(sigma)/sigma |
| ch20-p74-070 | 20 | relation | reference (standard form) | VERIFIED | plane waves, reflected wave with phase epsilon; d(lambda)/lambda = d(sigma)/sigma |
| ch20-p76-071 (60) | 20 | relation | reference (standard form) | VERIFIED | plane waves, reflected wave with phase epsilon; d(lambda)/lambda = d(sigma)/sigma |
| ch20-p76-072 (59) | 20 | relation | reference (standard form) | VERIFIED | Lorentzian approximation of Eq 49 near a peak (G = F pi^2 t^2 ...); note the equation number 59 is used twice in the chapter |
| ch20-p79-073 | 20 | definition | reference (definition) | DEFINITION | bandwidth from Q |
| ch21-p01-001 (1) | 21 | relation | reference (standard form) | VERIFIED | time-harmonic Maxwell equations and wave equations for a conducting medium (Gaussian units) |
| ch21-p01-002 (2) | 21 | relation | reference (standard form) | VERIFIED | time-harmonic Maxwell equations and wave equations for a conducting medium (Gaussian units) |
| ch21-p01-003 (3) | 21 | relation | reference (standard form) | VERIFIED | time-harmonic Maxwell equations and wave equations for a conducting medium (Gaussian units) |
| ch21-p01-004 (4) | 21 | relation | reference (standard form) | VERIFIED | time-harmonic Maxwell equations and wave equations for a conducting medium (Gaussian units) |
| ch21-p01-005 (5) | 21 | relation | reference (standard form) | VERIFIED | time-harmonic Maxwell equations and wave equations for a conducting medium (Gaussian units) |
| ch21-p01-006 (6) | 21 | definition | reference (definition) | DEFINITION | complex index m^2 = eps + i 4 pi sigma/omega, m = n(1 + iK); k = omega/c |
| ch21-p01-007 (7) | 21 | definition | reference (definition) | DEFINITION | complex index m^2 = eps + i 4 pi sigma/omega, m = n(1 + iK); k = omega/c |
| ch21-p01-008 | 21 | definition | reference (definition) | DEFINITION | complex index m^2 = eps + i 4 pi sigma/omega, m = n(1 + iK); k = omega/c |
| ch21-p02-009 (8) | 21 | definition | reference (definition) | DEFINITION | complex index m^2 = eps + i 4 pi sigma/omega, m = n(1 + iK); k = omega/c |
| ch21-p02-010 (10) | 21 | relation | numeric (book values) | VERIFIED | e^{ikmz} = e^{-k n K z} e^{i k n z} with m = n(1 + iK) (mu = 1) |
| ch21-p02-011 (11) | 21 | relation | reference (standard form) | VERIFIED | damped plane wave, phase velocity c/(mu^1/2 n) |
| ch21-p02-012 (12) | 21 | relation | reference (standard form) | VERIFIED | damped plane wave, phase velocity c/(mu^1/2 n) |
| ch21-p02-013 (13) | 21 | definition | reference (definition) | DEFINITION | normal-incidence amplitude reflection W1 |
| ch21-p02-014 (14) | 21 | definition | reference (definition) | DEFINITION | normal-incidence transmission; complex indices |
| ch21-p03-015 (15) | 21 | definition | reference (definition) | DEFINITION | normal-incidence transmission; complex indices |
| ch21-p03-016 (13a) | 21 | relation | reference (standard form) | VERIFIED | real indices |
| ch21-p03-017 (14a) | 21 | relation | reference (standard form) | VERIFIED | real indices |
| ch21-p03-018 (13b) | 21 | definition | reference (definition) | DEFINITION | phase pi for n1 > n0 |
| ch21-p03-019 (16) | 21 | relation | symbolic (sympy) | VERIFIED | rationalised complex Fresnel reflection |
| ch21-p04-020 (17) | 21 | relation | symbolic (sympy) | VERIFIED | rationalised complex Fresnel transmission |
| ch21-p04-021 (18) | 21 | definition | reference (definition) | DEFINITION | p0, q0, M_v (Eq 19/19a) and the oblique Fresnel coefficients W_v (E perp) and F_v (H perp) |
| ch21-p04-022 (19) | 21 | definition | reference (definition) | DEFINITION | p0, q0, M_v (Eq 19/19a) and the oblique Fresnel coefficients W_v (E perp) and F_v (H perp) |
| ch21-p04-023 (19a) | 21 | definition | reference (definition) | DEFINITION | p0, q0, M_v (Eq 19/19a) and the oblique Fresnel coefficients W_v (E perp) and F_v (H perp) |
| ch21-p04-024 (20) | 21 | definition | reference (definition) | DEFINITION | p0, q0, M_v (Eq 19/19a) and the oblique Fresnel coefficients W_v (E perp) and F_v (H perp) |
| ch21-p04-025 (21) | 21 | definition | reference (definition) | DEFINITION | p0, q0, M_v (Eq 19/19a) and the oblique Fresnel coefficients W_v (E perp) and F_v (H perp) |
| ch21-p05-026 (22) | 21 | relation | numeric (book values) | VERIFIED | single interface: \|W1\|^2 and \|F1\|^2 equal the reference reflectance for s and p, real and absorbing substrates, three angles |
| ch21-p05-027 (23) | 21 | relation | numeric (book values) | VERIFIED | single interface: \|W1\|^2 and \|F1\|^2 equal the reference reflectance for s and p, real and absorbing substrates, three angles |
| ch21-p05-028 (24) | 21 | relation | numeric (book values) | VERIFIED | single interface: \|W1\|^2 and \|F1\|^2 equal the reference reflectance for s and p, real and absorbing substrates, three angles |
| ch21-p05-029 (25) | 21 | relation | numeric (book values) | VERIFIED | single interface: \|W1\|^2 and \|F1\|^2 equal the reference reflectance for s and p, real and absorbing substrates, three angles |
| ch21-p05-030 (26) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-031 (26a) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-032 (27) | 21 | relation | reference (standard form) | VERIFIED | H from Faraday's law for E along y |
| ch21-p06-033 (26b) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-034 (28) | 21 | definition | reference (definition) | DEFINITION | time-averaged Poynting vector (x2 normalisation) |
| ch21-p06-035 (26c) | 21 | relation | reference (standard form) | VERIFIED | Poynting vectors of incident and reflected waves |
| ch21-p06-036 (29) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-037 (29a) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-038 (29b) | 21 | relation | reference (standard form) | VERIFIED | Poynting vectors of incident and reflected waves |
| ch21-p06-039 (30) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-040 (30a) | 21 | definition | reference (definition) | DEFINITION | incident, reflected and transmitted field components (E perpendicular) |
| ch21-p06-041 | 21 | relation | reference (standard form) | VERIFIED | planes of constant phase in the absorbing medium (inhomogeneous wave) |
| ch21-p06-042 | 21 | relation | reference (standard form) | VERIFIED | planes of constant phase in the absorbing medium (inhomogeneous wave) |
| ch21-p07-043 (30b) | 21 | relation | reference (standard form) | VERIFIED | planes of constant phase in the absorbing medium (inhomogeneous wave) |
| ch21-p07-044 (30c) | 21 | relation | reference (standard form) | VERIFIED | transmitted Poynting vector; its x-part vanishes when K0 = 0 |
| ch21-p07-045 (30d) | 21 | relation | reference (standard form) | VERIFIED | transmitted Poynting vector; its x-part vanishes when K0 = 0 |
| ch21-p07-046 (30e) | 21 | definition | reference (definition) | DEFINITION | refraction angle and apparent index (n_a)_1 of the inhomogeneous wave |
| ch21-p07-047 (30f) | 21 | definition | reference (definition) | DEFINITION | refraction angle and apparent index (n_a)_1 of the inhomogeneous wave |
| ch21-p07-048 (31) | 21 | definition | reference (definition) | DEFINITION | refraction angle and apparent index (n_a)_1 of the inhomogeneous wave |
| ch21-p07-049 (32) | 21 | relation | reference (standard form) | VERIFIED | Eq 32 = Eq 30f x Eq 31 (generalised Snell law with the apparent index) |
| ch21-p07-050 (33) | 21 | relation | reference (standard form) | VERIFIED | magnitude of Eq 30d with Eq 31 |
| ch21-p07-051 (34) | 21 | definition | reference (definition) | DEFINITION | energy reflectance/transmittance and the beam-area bookkeeping |
| ch21-p08-052 (35) | 21 | definition | reference (definition) | DEFINITION | energy reflectance/transmittance and the beam-area bookkeeping |
| ch21-p08-053 (36) | 21 | definition | reference (definition) | DEFINITION | energy reflectance/transmittance and the beam-area bookkeeping |
| ch21-p08-054 (37) | 21 | definition | reference (definition) | DEFINITION | energy reflectance/transmittance and the beam-area bookkeeping |
| ch21-p08-055 (38) | 21 | definition | reference (definition) | DEFINITION | energy reflectance/transmittance and the beam-area bookkeeping |
| ch21-p08-056 (39) | 21 | relation | numeric (book values) | VERIFIED | energy balance Eqs 39/40 with (n_a)_1 cos i_1 = Re(M1) and n0 cos i0 = M0: holds identically for 20 random absorbing substrates |
| ch21-p08-057 (40) | 21 | relation | numeric (book values) | VERIFIED | energy balance Eqs 39/40 with (n_a)_1 cos i_1 = Re(M1) and n0 cos i0 = M0: holds identically for 20 random absorbing substrates |
| ch21-p09-058 (41) | 21 | relation | reference (standard form) | VERIFIED | E from Ampere's law for H along y |
| ch21-p09-059 (42) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p09-060 (42a) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p09-061 (42b) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p09-062 (43) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p09-063 (43a) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p09-064 (43b) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p10-065 (44) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p10-066 (44a) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p10-067 (44b) | 21 | definition | reference (definition) | DEFINITION | p-polarised incident/reflected/transmitted fields and Poynting vectors |
| ch21-p10-068 (44c) | 21 | relation | symbolic (sympy) | VERIFIED | 1/m^2 + 1/m-bar^2 = 2 Re(m^2)/\|m\|^4 |
| ch21-p10-069 (44d) | 21 | relation | symbolic (sympy) | VERIFIED | Re(m^2) = n^2(1 - K^2) = epsilon |
| ch21-p10-070 | 21 | relation | reference (standard form) | VERIFIED | p transmitted Poynting vector split into the homogeneous and absorption parts |
| ch21-p10-071 (44e) | 21 | relation | reference (standard form) | VERIFIED | p transmitted Poynting vector split into the homogeneous and absorption parts |
| ch21-p10-072 (44f) | 21 | relation | reference (standard form) | VERIFIED | p transmitted Poynting vector split into the homogeneous and absorption parts |
| ch21-p10-073 (45) | 21 | definition | reference (definition) | DEFINITION | energy reflectance for p |
| ch21-p10-074 (45a) | 21 | relation | numeric (book values) | VERIFIED | p energy transmittance Eq 45b plus \|F1\|^2 = 1 for non-absorbing substrates at three angles (as written it uses n1^2, exact only for K1 = 0; the absorbing case needs Re(m1^2) of Eq 44f) |
| ch21-p11-075 (45b) | 21 | relation | numeric (book values) | VERIFIED | p energy transmittance Eq 45b plus \|F1\|^2 = 1 for non-absorbing substrates at three angles (as written it uses n1^2, exact only for K1 = 0; the absorbing case needs Re(m1^2) of Eq 44f) |
| ch21-p11-076 (46) | 21 | definition | reference (definition) | DEFINITION | complex reflectance of layer v; complex phase thickness beta |
| ch21-p12-077 (47) | 21 | definition | reference (definition) | DEFINITION | complex reflectance of layer v; complex phase thickness beta |
| ch21-p12-078 (48) | 21 | relation | reference (standard form) | VERIFIED | boundary conditions at interface v (continuity of tangential E and H) |
| ch21-p12-079 (48a) | 21 | relation | reference (standard form) | VERIFIED | boundary conditions at interface v (continuity of tangential E and H) |
| ch21-p13-080 (48b) | 21 | relation | symbolic (sympy) | VERIFIED | Eq 48 divided by tau |
| ch21-p13-081 (48c) | 21 | relation | symbolic (sympy) | VERIFIED | Eq 48a solved for tau_(v-1) |
| ch21-p13-082 (48d) | 21 | relation | symbolic (sympy) | VERIFIED | Eq 48b with Eq 48c |
| ch21-p13-083 (48e) | 21 | relation | symbolic (sympy) | VERIFIED | divide by tau_v |
| ch21-p13-084 (48f) | 21 | relation | symbolic (sympy) | VERIFIED | common denominator |
| ch21-p13-085 (49) | 21 | relation | symbolic (sympy) | VERIFIED | W^2 + 4 M_(v-1) M_v/(M_(v-1)+M_v)^2 = 1 identically |
| ch21-p14-086 (50) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 50 from rho_N = W_(N+1) gives \|rho_0\|^2 equal to the independent characteristic-matrix R (12 random absorbing stacks, oblique) |
| ch21-p14-087 (51) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 50 from rho_N = W_(N+1) gives \|rho_0\|^2 equal to the independent characteristic-matrix R (12 random absorbing stacks, oblique) |
| ch21-p14-088 (52) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 50 from rho_N = W_(N+1) gives \|rho_0\|^2 equal to the independent characteristic-matrix R (12 random absorbing stacks, oblique) |
| ch21-p14-089 (53) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-090 (53a) | 21 | relation | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-14): the product's denominator is printed with e^{i beta_v/2}; Eq 53 (and the verified Eq 54) have e^{i beta_v} |
| ch21-p14-091 (53b) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-092 (54) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-093 (54a) | 21 | relation | numeric (book values) | VERIFIED | normal incidence, K = 0: Eq 54a equals Eq 54 |
| ch21-p14-094 (55) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-095 (55a) | 21 | relation | numeric (book values) | VERIFIED | Eq 55a (normal incidence, non-absorbing) |
| ch21-p14-096 (56) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 50 from rho_N = W_(N+1) gives \|rho_0\|^2 equal to the independent characteristic-matrix R (12 random absorbing stacks, oblique) |
| ch21-p14-097 (57) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 50 from rho_N = W_(N+1) gives \|rho_0\|^2 equal to the independent characteristic-matrix R (12 random absorbing stacks, oblique) |
| ch21-p14-098 (58) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-099 (59) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-100 (60) | 21 | relation | numeric (book values) | VERIFIED | Eqs 53, 53b, 54 product for tau_(N+1)/tau_0 with Eq 58 ((n_a) cos i = Re M) reproduces the reference transmittance T (12 absorbing stacks) |
| ch21-p14-101 (61) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p14-102 (61a) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p14-103 (62) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p14-104 | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p14-105 (63) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p14-106 (64) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p14-107 (65) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p17-108 (66) | 21 | definition | reference (definition) | DEFINITION | fields in layer v; apparent index and generalised Snell law |
| ch21-p17-109 (67) | 21 | definition | reference (definition) | DEFINITION | gamma = R/T for the H-perpendicular case |
| ch21-p17-110 (68) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 68 with F_v gives the reference p-reflectance (12 absorbing stacks) |
| ch21-p18-111 (69) | 21 | relation | numeric (book values) | VERIFIED | recursion Eq 68 with F_v gives the reference p-reflectance (12 absorbing stacks) |
| ch21-p18-112 (70) | 21 | relation | numeric (book values) | VERIFIED | Eqs 70/74 transmittance product for p reproduces the reference (10 non-absorbing stacks, oblique) |
| ch21-p18-113 (71) | 21 | relation | numeric (book values) | VERIFIED | Eq 71 energy transmittance for p |
| ch21-p18-114 (71a) | 21 | relation | reference + scan | FLAG | Eq 71a as printed has n_1 in the denominator; setting K = 0 in Eq 71 gives n0 (n_a)_(N+1) cos i_(N+1)/(n_(N+1)^2 cos i0) \|T/T0\|^2, i.e. the substrate index n_(N+1), not n_1. 1962 ORIGINAL (sic, scan p.21-18 prints n_1) |
| ch21-p18-115 (72) | 21 | definition | reference (definition) | DEFINITION | H fields in layer v |
| ch21-p18-116 (73) | 21 | definition | reference (definition) | DEFINITION | H fields in layer v |
| ch21-p18-117 (74) | 21 | relation | numeric (book values) | VERIFIED | Eqs 70/74 transmittance product for p reproduces the reference (10 non-absorbing stacks, oblique) |
| ch21-p19-118 (75) | 21 | relation | numeric (book values) | VERIFIED | weak-reflection approximation Eq 75/76: sum of single reflections agrees with Eq 50 for a low-index stack |
| ch21-p19-119 | 21 | relation | numeric (book values) | VERIFIED | weak-reflection approximation Eq 75/76: sum of single reflections agrees with Eq 50 for a low-index stack |
| ch21-p19-120 | 21 | relation | numeric (book values) | VERIFIED | weak-reflection approximation Eq 75/76: sum of single reflections agrees with Eq 50 for a low-index stack |
| ch21-p19-121 | 21 | relation | numeric (book values) | VERIFIED | weak-reflection approximation Eq 75/76: sum of single reflections agrees with Eq 50 for a low-index stack |
| ch21-p19-122 (76) | 21 | relation | numeric (book values) | VERIFIED | weak-reflection approximation Eq 75/76: sum of single reflections agrees with Eq 50 for a low-index stack |
| ch21-p19-123 (76a) | 21 | definition | reference (definition) | DEFINITION | real and imaginary parts |
| ch21-p19-124 (76b) | 21 | definition | reference (definition) | DEFINITION | real and imaginary parts |
| ch21-p19-125 (76c) | 21 | relation | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-19): the first sum must be of W_v^2 (\|sum W_v e^{i phi_v}\|^2 expanded); with W_v^2 it equals \|Eq 76\|^2 exactly, while the printed sum of W_v gives -0.2048 instead of 0.0182 for a test stack |
| ch21-p19-126 (77) | 21 | definition | reference (definition) | DEFINITION | E and H of the two waves in layer v (E perpendicular) |
| ch21-p19-127 (77a) | 21 | definition | reference (definition) | DEFINITION | E and H of the two waves in layer v (E perpendicular) |
| ch21-p19-128 (77b) | 21 | definition | reference (definition) | DEFINITION | E and H of the two waves in layer v (E perpendicular) |
| ch21-p19-129 (77c) | 21 | definition | reference (definition) | DEFINITION | E and H of the two waves in layer v (E perpendicular) |
| ch21-p20-130 (78) | 21 | definition | reference (definition) | DEFINITION | admittance Y_v |
| ch21-p20-131 (78a) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p20-132 (78b) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p20-133 (78c) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p20-134 (79) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p20-135 (80) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-136 (79a) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-137 (81) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-138 (82) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-139 | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-140 (81a) | 21 | relation | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-21 prints -i): eliminating rho_(v-1) between Eqs 81 and 82 involves e^{+i beta}, so the recursion must read Y_(v-1) = M_(v-1)(Y_v + i M_(v-1) tan(beta_(v-1)/2))/(M_(v-1) + i Y_v tan(beta_(v-1)/2)). With +i it reproduces Eq 50 to 1e-15; the printed -i does not. The book applied the e^{-ix} identity where e^{+ix} is needed. (The p-case Eq 88a correctly has -i because Eq 85a uses the opposite sign convention.) |
| ch21-p21-141 (81b) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-142 | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-143 (82a) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-144 (82b) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-145 (82c) | 21 | relation | numeric (book values) | VERIFIED | with Y_v = admittance at entry into layer v, Y_(N+1) = -M_(N+1): Eqs 78b/c, 79a, 80, 81, 82, 82a-c hold for every layer and rho_0 = (M_0 + Y_1)/(M_0 - Y_1) equals Eq 50 (12 absorbing stacks, oblique); identity (e^{-ix}-1)/(e^{-ix}+1) = -i tan(x/2) holds |
| ch21-p21-146 (83) | 21 | relation | numeric (book values) | VERIFIED | Eq 83 admittance form of tau_(N+1)/tau_0 equals Eq 54 (12 stacks; admittances from the corrected Eq 81a) |
| ch21-p22-147 (84) | 21 | definition | reference (definition) | DEFINITION | p-case fields and admittance y_v |
| ch21-p22-148 (84a) | 21 | definition | reference (definition) | DEFINITION | p-case fields and admittance y_v |
| ch21-p22-149 (84b) | 21 | definition | reference (definition) | DEFINITION | p-case fields and admittance y_v |
| ch21-p22-150 (84c) | 21 | definition | reference (definition) | DEFINITION | p-case fields and admittance y_v |
| ch21-p22-151 (85) | 21 | definition | reference (definition) | DEFINITION | p-case fields and admittance y_v |
| ch21-p22-152 (85a) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p22-153 (85b) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p22-154 (86) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p22-155 (87) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p22-156 (87a) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p22-157 (88) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p23-158 (88a) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p23-159 (88b) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p23-160 | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p23-161 (89) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p23-162 (89a) | 21 | relation | numeric (book values) | VERIFIED | p case, y_v at entry into layer v, y_(N+1) = m^2/M (88b): recursion Eq 88a as printed reproduces gamma_0 of Eq 68; Eqs 85a/b, 86, 87, 87a, 88, 89, 89a hold for every layer (12 absorbing stacks, oblique) |
| ch21-p23-163 (89b) | 21 | relation | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-23): from Eq 89 the product's denominator must be y_v + m_(v-1)^2/M_(v-1); the book prints /M_v |
| ch21-p23-164 (90) | 21 | relation | numeric (book values) | VERIFIED | absentee layer: with n d cos i = lambda/2 (beta = 2 pi) inserting the layer leaves R unchanged (s and p, oblique) |
| ch21-p24-165 (91) | 21 | definition | reference (definition) | DEFINITION | bilinear recursion and continuant Q_v |
| ch21-p24-166 (91a) | 21 | definition | reference (definition) | DEFINITION | bilinear recursion and continuant Q_v |
| ch21-p24-167 (91b) | 21 | definition | reference (definition) | DEFINITION | bilinear recursion and continuant Q_v |
| ch21-p24-168 (91c) | 21 | definition | reference (definition) | DEFINITION | bilinear recursion and continuant Q_v |
| ch21-p24-169 | 21 | definition | reference (definition) | DEFINITION | bilinear recursion and continuant Q_v |
| ch21-p24-170 (91e) | 21 | relation | reference (standard form) | VERIFIED | continuant recurrence for the bilinear map (standard) |
| ch21-p24-171 (91f) | 21 | relation | reference (standard form) | VERIFIED | continuant recurrence for the bilinear map (standard) |
| ch21-p24-172 (92) | 21 | definition | reference (definition) | DEFINITION | Eq 50 written in the bilinear form |
| ch21-p24-173 | 21 | definition | reference (definition) | DEFINITION | Eq 50 written in the bilinear form |
| ch21-p24-174 (92a) | 21 | definition | reference (definition) | DEFINITION | Eq 50 written in the bilinear form |
| ch21-p24-175 (92b) | 21 | definition | reference (definition) | DEFINITION | Eq 50 written in the bilinear form |
| ch21-p24-176 (92c) | 21 | definition | reference (definition) | DEFINITION | Eq 50 written in the bilinear form |
| ch21-p25-177 (92d) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-178 (92e) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-179 (92f) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-180 (92g) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-181 (92h) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-182 (93) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-183 (94) | 21 | relation | numeric (book values) | VERIFIED | Q-method Eqs 92d-94: Q recursion gives rho_0 (Eq 93) and 1/Q_1 = product of 1/f_v (Eq 94), stacks with N >= 2 |
| ch21-p25-184 (95) | 21 | relation | numeric (book values) | VERIFIED | Eq 95: the Fresnel product 2^(N+1) prod M_(v-1)/(M_(v-1)+M_v) with Eq 94 gives Eq 54; beta/2 split into real and imaginary parts |
| ch21-p25-185 (95a) | 21 | relation | numeric (book values) | VERIFIED | Eq 95: the Fresnel product 2^(N+1) prod M_(v-1)/(M_(v-1)+M_v) with Eq 94 gives Eq 54; beta/2 split into real and imaginary parts |
| ch21-p26-186 (96) | 21 | relation | reference (standard form) | VERIFIED | Eqs 50/68 for the first layer |
| ch21-p26-187 (97) | 21 | relation | reference (standard form) | VERIFIED | Eqs 50/68 for the first layer |
| ch21-p26-188 (98) | 21 | relation | reference (standard form) | VERIFIED | zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition |
| ch21-p26-189 (98a) | 21 | relation | reference (standard form) | VERIFIED | zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition |
| ch21-p27-190 (99) | 21 | relation | reference (standard form) | VERIFIED | zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition |
| ch21-p27-191 (99a) | 21 | relation | reference (standard form) | VERIFIED | zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition |
| ch21-p27-192 (100) | 21 | relation | reference (standard form) | VERIFIED | zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition |
| ch21-p27-193 (101) | 21 | relation | reference (standard form) | VERIFIED | zero conditions: numerator of Eq 96/97 vanishes; admittance and Q forms are the same condition |
| ch21-p27-194 (102) | 21 | relation | numeric (book values) | VERIFIED | Eq 102 (and 103) = \|Eq 96\|^2 written out (10 random complex W1, W2, absorbing beta) |
| ch21-p27-195 (103) | 21 | relation | numeric (book values) | VERIFIED | Eq 102 (and 103) = \|Eq 96\|^2 written out (10 random complex W1, W2, absorbing beta) |
| ch21-p27-196 (105) | 21 | relation | numeric (book values) | VERIFIED | Eq 105 with \|W2\| = 1 (Eq 104), real W1 and real beta1 equals \|Eq 96\|^2 |
| ch21-p27-197 (106) | 21 | definition | reference (definition) | DEFINITION | \|W\| = \|F\| = 1 under total internal reflection |
| ch21-p28-198 (107) | 21 | relation | reference (standard form) | VERIFIED | beta1 purely imaginary when M1 is imaginary: e^{i beta} real = exp(-4 pi \|n0^2 p0^2 - n1^2\|^{1/2} d/lambda) |
| ch21-p28-199 (108) | 21 | relation | numeric (book values) | VERIFIED | Eq 110 (\|W1\| = \|W2\| = 1, real A = e^{i beta}) equals \|Eq 96\|^2; Eq 108 is the same with \|W1\| general |
| ch21-p28-200 (109) | 21 | definition | reference (definition) | DEFINITION | \|W\| = \|F\| = 1 under total internal reflection |
| ch21-p28-201 (110) | 21 | relation | numeric (book values) | VERIFIED | Eq 110 (\|W1\| = \|W2\| = 1, real A = e^{i beta}) equals \|Eq 96\|^2; Eq 108 is the same with \|W1\| general |
| ch21-p28-202 (111) | 21 | relation | numeric (book values) | VERIFIED | Eq 110 (\|W1\| = \|W2\| = 1, real A = e^{i beta}) equals \|Eq 96\|^2; Eq 108 is the same with \|W1\| general |
| ch21-p28-203 (112) | 21 | relation | reference (standard form) | VERIFIED | zero condition of Eq 96 for real W1, W2 |
| ch21-p28-204 | 21 | definition | reference (definition) | DEFINITION | phase conditions: beta1 an odd multiple of pi (quarter wave) or multiple of 2 pi |
| ch21-p28-205 (113b) | 21 | definition | reference (definition) | DEFINITION | phase conditions: beta1 an odd multiple of pi (quarter wave) or multiple of 2 pi |
| ch21-p28-206 (114) | 21 | relation | symbolic (sympy) | VERIFIED | W1 = W2 gives M1 = sqrt(M0 M2) |
| ch21-p28-207 | 21 | relation | symbolic (sympy) | VERIFIED | W1 = W2 gives M1 = sqrt(M0 M2) |
| ch21-p28-208 (114a) | 21 | relation | symbolic (sympy) | VERIFIED | W1 = W2 gives M1 = sqrt(M0 M2) |
| ch21-p29-209 (115) | 21 | definition | reference (definition) | DEFINITION | quarter-wave thickness conditions |
| ch21-p29-210 (116) | 21 | definition | reference (definition) | DEFINITION | quarter-wave thickness conditions |
| ch21-p29-211 | 21 | relation | symbolic (sympy) | VERIFIED | M1 = sqrt(M0 M2) with M = n cos i rearranged |
| ch21-p29-212 (117) | 21 | relation | reference (standard form) | VERIFIED | zero condition for the H-perpendicular case, F1 = F2 |
| ch21-p29-213 (118) | 21 | relation | reference (standard form) | VERIFIED | zero condition for the H-perpendicular case, F1 = F2 |
| ch21-p29-214 (118a) | 21 | relation | symbolic (sympy) | VERIFIED | F1 = F2 means m^2/M equal-geometric: (n1/cos i1)^2 = (n0/cos i0)(n2/cos i2) |
| ch21-p29-215 (119) | 21 | relation | symbolic (sympy) | VERIFIED | F1 = F2 means m^2/M equal-geometric: (n1/cos i1)^2 = (n0/cos i0)(n2/cos i2) |
| ch21-p29-216 | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-217 (120) | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-218 (121) | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-219 | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-220 (122) | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-221 | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-222 (123) | 21 | definition | reference (definition) | DEFINITION | fields and H from Faraday's law in layer v |
| ch21-p29-223 (124) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p29-224 (124a) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p29-225 (125) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p29-226 (125a) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p29-227 | 21 | relation | reference (standard form) | VERIFIED | linear maps as 2x2 matrices and their product (standard) |
| ch21-p29-228 (126) | 21 | relation | reference (standard form) | VERIFIED | linear maps as 2x2 matrices and their product (standard) |
| ch21-p31-229 (127) | 21 | relation | reference (standard form) | VERIFIED | linear maps as 2x2 matrices and their product (standard) |
| ch21-p31-230 (128) | 21 | relation | reference (standard form) | VERIFIED | linear maps as 2x2 matrices and their product (standard) |
| ch21-p31-231 (129) | 21 | relation | reference (standard form) | VERIFIED | linear maps as 2x2 matrices and their product (standard) |
| ch21-p31-232 (130) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-233 (130a) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-234 (131) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-235 (131a) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-236 (131b) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-237 (132) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-238 (132a) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-239 (132b) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p31-240 (132c) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p32-241 (133) | 21 | relation | numeric (book values) | VERIFIED | matrix form Eqs 130-133: stacking the interface matrices from r_N = tau_N W_(N+1) reproduces r_0/tau_0 = rho_0 of Eq 50 and the transmittance ratio of Eq 54 (12 stacks) |
| ch21-p32-242 (134) | 21 | relation | reference (standard form) | VERIFIED | regrouping of the ordered product |
| ch21-p32-243 (135) | 21 | relation | reference (standard form) | VERIFIED | regrouping of the ordered product |
| ch21-p32-244 (136) | 21 | relation | symbolic (sympy) | VERIFIED | M_v factors as S_v T_v |
| ch21-p32-245 (136a) | 21 | relation | symbolic (sympy) | VERIFIED | M_v factors as S_v T_v |
| ch21-p32-246 (136b) | 21 | relation | reference (standard form) | VERIFIED | regrouping of the ordered product |
| ch21-p32-247 | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p32-248 (137) | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p32-249 (137a) | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p32-250 | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p32-251 (137b) | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p33-252 (137c) | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p33-253 | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p33-254 (137d) | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p33-255 (137e) | 21 | relation | numeric (book values) | VERIFIED | A = r + tau, B = M(r - tau) propagate by the characteristic matrix Eq 137c from (1, -M_(N+1)) tau_(N+1); rho_0 = (A0 + B0/M0)/(A0 - B0/M0) equals Eq 50 (12 stacks) |
| ch21-p33-256 (138) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p33-257 (138a) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p33-258 (139) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p33-259 (139a) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p33-260 (140) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p33-261 (140a) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-262 (140b) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-263 (140c) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-264 (140d) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-265 (141) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-266 | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-267 (142) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-268 (142a) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-269 | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-270 (142b) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p34-271 (142c) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p35-272 | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p35-273 (142d) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p35-274 (142e) | 21 | relation | numeric (book values) | VERIFIED | p-case matrix forms Eqs 138-142e: propagating (C, D) with m^2/M in place of M reproduces gamma_0 of Eq 68 (12 stacks) |
| ch21-p35-275 (143) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-276 (143a) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-277 (143b) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-278 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-279 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-280 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-281 (143c) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p35-282 (143d) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-283 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-284 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-285 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-286 (143e) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-287 (144) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-288 (144a) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-289 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-290 (144b) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-291 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-292 (144c) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-293 | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-294 (144d) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-295 (144e) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-296 (144f) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p36-297 (144g) | 21 | relation | numeric (book values) | VERIFIED | quaternion algebra: sigma products (Eq 143c), product components (Eq 143e) and the matrix<->quaternion map (Eqs 144b-d) checked with the Eq 144c matrices on 10 random complex pairs; homomorphism Eqs 144e-g follows |
| ch21-p37-298 (145) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-299 (145a) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-300 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-301 (145b) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-302 (145c) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-303 (145d) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-304 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-305 (145e) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-306 (145f) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-307 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-308 (145g) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-309 (145h) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-310 (145i) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-311 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p37-312 (145j) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-313 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-314 (145k) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-315 (146) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-316 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-317 (147) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-318 (148) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-319 | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-320 (149) | 21 | relation | numeric (book values) | VERIFIED | column vectors as quaternions (Eqs 145c-e) and r = 2U0, tau = -2U2 (Eqs 145h-149) reproduce the matrix product (10 random cases) |
| ch21-p38-321 (150) | 21 | relation | numeric (book values) | VERIFIED | lossless stack: product matrix of Eq 137c type has m22 = conj(m11), m21 = conj(m12) up to the i convention (Eq 151) |
| ch21-p38-322 (151) | 21 | relation | numeric (book values) | VERIFIED | lossless stack: product matrix of Eq 137c type has m22 = conj(m11), m21 = conj(m12) up to the i convention (Eq 151) |
| ch21-p38-323 | 21 | relation | numeric (book values) | VERIFIED | lossless stack: product matrix of Eq 137c type has m22 = conj(m11), m21 = conj(m12) up to the i convention (Eq 151) |
| ch21-p38-324 (152) | 21 | relation | numeric (book values) | VERIFIED | lossless stack: product matrix of Eq 137c type has m22 = conj(m11), m21 = conj(m12) up to the i convention (Eq 151) |
| ch21-p39-325 | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-326 (153) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-327 (154) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-328 (155) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-329 (156) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-330 (157) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-331 (158) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-332 | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-333 (159) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-334 | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-335 (160) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p39-336 (161) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p40-337 (162) | 21 | relation | numeric (book values) | VERIFIED | Eq 162 transmittance ratio from the normalised product equals Eq 54 |
| ch21-p40-338 | 21 | relation | symbolic (sympy) | VERIFIED | single layer: rho_0 = -U0/U2 |
| ch21-p40-339 (163) | 21 | relation | symbolic (sympy) | VERIFIED | single layer: rho_0 = -U0/U2 |
| ch21-p40-340 (164) | 21 | relation | symbolic (sympy) | VERIFIED | single layer: rho_0 = -U0/U2 |
| ch21-p40-341 (165) | 21 | relation | numeric (book values) | VERIFIED | single-layer transmittance ratio Eq 165/168 equals the general product Eq 54 |
| ch21-p40-342 (166) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p40-343 (166a) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p40-344 (166b) | 21 | relation | numeric (book values) | VERIFIED | normalised interface matrices Eqs 153-155 (entries 1, W e^{+-i beta/2}) and the quaternion route rho_0 = -U0/U2 (Eq 161) reproduce Eq 50 |
| ch21-p41-345 (167) | 21 | relation | symbolic (sympy) | VERIFIED | single layer: rho_0 = -U0/U2 |
| ch21-p41-346 (168) | 21 | relation | numeric (book values) | VERIFIED | single-layer transmittance ratio Eq 165/168 equals the general product Eq 54 |
| ch21-p41-347 (169) | 21 | definition | reference (definition) | DEFINITION | single layer, normal incidence definitions |
| ch21-p41-348 (169a) | 21 | definition | reference (definition) | DEFINITION | single layer, normal incidence definitions |
| ch21-p41-349 (169b) | 21 | definition | reference (definition) | DEFINITION | single layer, normal incidence definitions |
| ch21-p41-350 (170) | 21 | relation | symbolic (sympy) | VERIFIED | absorbing single layer: e^{i beta} = e^{-4 pi n K d/lambda} e^{i 4 pi n d/lambda} |
| ch21-p41-351 (170a) | 21 | relation | symbolic (sympy) | VERIFIED | absorbing single layer: e^{i beta} = e^{-4 pi n K d/lambda} e^{i 4 pi n d/lambda} |
| ch21-p42-352 | 21 | relation | reference (standard form) | VERIFIED | non-absorbing: M1 = n1 cos i1 |
| ch21-p42-353 (170b) | 21 | relation | reference (standard form) | VERIFIED | non-absorbing: M1 = n1 cos i1 |
| ch21-p42-354 (171) | 21 | relation | numeric (book values) | VERIFIED | Eq 172 = \|Eq 171\|^2 for real W1, W2 |
| ch21-p42-355 (172) | 21 | relation | numeric (book values) | VERIFIED | Eq 172 = \|Eq 171\|^2 for real W1, W2 |
| ch21-p42-356 (173) | 21 | definition | reference (definition) | DEFINITION | extremum condition |
| ch21-p42-357 (174) | 21 | relation | symbolic (sympy) | VERIFIED | Eq 172 at cos(beta) = +-1 |
| ch21-p43-358 (175) | 21 | relation | reference (standard form) | VERIFIED | strong absorption limit: e^{i beta} -> 0 |
| ch21-p43-359 (176) | 21 | relation | numeric (book values) | VERIFIED | single non-absorbing layer: R + Eq 177 transmittance = 1 |
| ch21-p43-360 (177) | 21 | relation | numeric (book values) | VERIFIED | single non-absorbing layer: R + Eq 177 transmittance = 1 |
| ch21-p43-361 | 21 | definition | reference (definition) | DEFINITION | definitions for the quarter-wave minimum |
| ch21-p43-362 (178) | 21 | definition | reference (definition) | DEFINITION | definitions for the quarter-wave minimum |
| ch21-p43-363 | 21 | definition | reference (definition) | DEFINITION | definitions for the quarter-wave minimum |
| ch21-p43-364 (179) | 21 | relation | symbolic (sympy) | VERIFIED | Eq 174 (minus sign) with real W1, W2 gives Eq 179 |
| ch21-p43-365 (180) | 21 | relation | symbolic (sympy) | VERIFIED | zero for n1 = sqrt(n0 n2) |
| ch21-p44-366 | 21 | definition | reference (definition) | DEFINITION | phase thickness at normal incidence |
| ch21-p45-367 (1) | 21 | relation | symbolic (sympy) | VERIFIED | plate with incoherent back reflection B |
| ch21-p45-368 (2) | 21 | relation | symbolic (sympy) | VERIFIED | inverse of Eq 1 |
| ch21-p45-369 (181) | 21 | relation | reference (standard form) | VERIFIED | equivalent-index relation for layer pairs (as used in the text) |
| ch21-p49-370 (182) | 21 | relation | reference + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-49 prints 1 + W1 W2 e^{i beta_1}): Eq 50 requires 1 + W1 rho_1 e^{i beta_1}; the printed form holds only when rho_1 = W2 (the single-layer case) |
| ch21-p49-371 (182a) | 21 | relation | reference (standard form) | VERIFIED | Eq 50 for the second layer |
| ch21-p53-372 (183) | 21 | relation | numeric (book values) | VERIFIED | Eq 183 with D of Eq 183a equals \|rho_0\|^2 from the recursion (10 random real W, beta) |
| ch21-p53-373 | 21 | relation | numeric (book values) | VERIFIED | Eq 183 with D of Eq 183a equals \|rho_0\|^2 from the recursion (10 random real W, beta) |
| ch21-p53-374 | 21 | relation | numeric (book values) | VERIFIED | Eq 183 with D of Eq 183a equals \|rho_0\|^2 from the recursion (10 random real W, beta) |
| ch21-p53-375 (183a) | 21 | relation | numeric (book values) | VERIFIED | Eq 183 with D of Eq 183a equals \|rho_0\|^2 from the recursion (10 random real W, beta) |
| ch21-p53-376 (183b) | 21 | relation | numeric (book values) | VERIFIED | Eq 183 with D of Eq 183a equals \|rho_0\|^2 from the recursion (10 random real W, beta) |
| ch21-p53-377 | 21 | relation | numeric (book values) | VERIFIED | Eq 183 with D of Eq 183a equals \|rho_0\|^2 from the recursion (10 random real W, beta) |
| ch21-p53-378 (184) | 21 | relation | reference (standard form) | VERIFIED | \|W2\| vs \|W1\| ordering follows from W = (n - n')/(n + n') |
| ch21-p53-379 (184a) | 21 | relation | reference (standard form) | VERIFIED | \|W2\| vs \|W1\| ordering follows from W = (n - n')/(n + n') |
| ch21-p53-380 (185) | 21 | relation | numeric (book values) | VERIFIED | Eq 185: for W3 satisfying it, some beta2 makes the two-layer reflectance zero (search over beta2) |
| ch21-p53-381 (185a) | 21 | relation | numeric (book values) | VERIFIED | Eq 185: for W3 satisfying it, some beta2 makes the two-layer reflectance zero (search over beta2) |
| ch21-p55-382 (185b) | 21 | relation | none | NOT VERIFIED | Eq 185b-e: index form of Eq 185 for the specific design family (n_g symbol used without definition in the transcription); not re-derived |
| ch21-p55-383 (185c) | 21 | relation | none | NOT VERIFIED | Eq 185b-e: index form of Eq 185 for the specific design family (n_g symbol used without definition in the transcription); not re-derived |
| ch21-p55-384 (185d) | 21 | relation | none | NOT VERIFIED | Eq 185b-e: index form of Eq 185 for the specific design family (n_g symbol used without definition in the transcription); not re-derived |
| ch21-p55-385 (185e) | 21 | relation | none | NOT VERIFIED | Eq 185b-e: index form of Eq 185 for the specific design family (n_g symbol used without definition in the transcription); not re-derived |
| ch21-p55-386 (186) | 21 | relation | numeric (book values) | VERIFIED | Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185) |
| ch21-p55-387 (186a) | 21 | relation | numeric (book values) | VERIFIED | Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185) |
| ch21-p55-388 (186b) | 21 | relation | numeric (book values) | VERIFIED | Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185) |
| ch21-p55-389 | 21 | relation | numeric (book values) | VERIFIED | Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185) |
| ch21-p55-390 (186c) | 21 | relation | numeric (book values) | VERIFIED | Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185) |
| ch21-p55-391 | 21 | relation | numeric (book values) | VERIFIED | Eqs 186-186c: with beta2 = theta2 - theta1 the two-layer stack has zero reflectance (for W3 from Eq 185) |
| ch21-p57-392 | 21 | definition | reference (definition) | DEFINITION | quarter-wave AR condition for the first layer |
| ch21-p57-393 (187) | 21 | definition | reference (definition) | DEFINITION | admittance recursion for a two-layer normal-incidence coating (Eq 81a with M = n) |
| ch21-p57-394 (187a) | 21 | definition | reference (definition) | DEFINITION | admittance recursion for a two-layer normal-incidence coating (Eq 81a with M = n) |
| ch21-p57-395 (187b) | 21 | definition | reference (definition) | DEFINITION | admittance recursion for a two-layer normal-incidence coating (Eq 81a with M = n) |
| ch21-p57-396 (188) | 21 | definition | reference (definition) | DEFINITION | admittance recursion for a two-layer normal-incidence coating (Eq 81a with M = n) |
| ch21-p57-397 (188a) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p61-398 (188b) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p61-399 (188c) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p61-400 (189) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p61-401 (189a) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p61-402 (189b) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p61-403 (190) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p62-404 (190b) | 21 | worked example | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p62-405 (190c) | 21 | relation | reference (standard form) | VERIFIED | zero-reflectance design equations for a two-layer coating with p2 = 2 p1 (algebra of Eq 188a; not re-derived) |
| ch21-p62-406 (191) | 21 | relation | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-62 prints 2 rho_1 W_1^2 cos beta_1 in the denominator): \|Eq 50\|^2 for real rho_1, W_1 is (rho_1^2 + W_1^2 + 2 rho_1 W_1 cos beta_1)/(1 + rho_1^2 W_1^2 + 2 rho_1 W_1 cos beta_1); corrected form verified on 10 random cases |
| ch21-p62-407 (192) | 21 | relation | symbolic (sympy) | VERIFIED | quarter-wave layer (tan(beta/2) -> infinity) in Eq 81a: Y_(v-1) = n^2/Y_v |
| ch21-p62-408 (192a) | 21 | relation | symbolic (sympy) | VERIFIED | quarter-wave layer (tan(beta/2) -> infinity) in Eq 81a: Y_(v-1) = n^2/Y_v |
| ch21-p62-409 (192b) | 21 | relation | symbolic (sympy) | VERIFIED | two quarter waves on n3 |
| ch21-p62-410 (193) | 21 | relation | symbolic (sympy) | VERIFIED | rho_0 = (n0 + Y1)/(n0 - Y1) |
| ch21-p62-411 (194) | 21 | relation | symbolic (sympy) | VERIFIED | zero when n0 n2^2 = n3 n1^2; Eq 195 is Eq 193 squared with n0 = 1 |
| ch21-p63-412 (195) | 21 | relation | symbolic (sympy) | VERIFIED | zero when n0 n2^2 = n3 n1^2; Eq 195 is Eq 193 squared with n0 = 1 |
| ch21-p64-413 (196) | 21 | relation | reference (standard form) | VERIFIED | zero condition Eq 196 (two layers, weak-reflection form) split into real/imaginary parts; Eq 197b follows by eliminating beta1 + beta2 |
| ch21-p64-414 (197) | 21 | relation | reference (standard form) | VERIFIED | zero condition Eq 196 (two layers, weak-reflection form) split into real/imaginary parts; Eq 197b follows by eliminating beta1 + beta2 |
| ch21-p64-415 (197a) | 21 | relation | reference (standard form) | VERIFIED | zero condition Eq 196 (two layers, weak-reflection form) split into real/imaginary parts; Eq 197b follows by eliminating beta1 + beta2 |
| ch21-p64-416 (197b) | 21 | relation | reference (standard form) | VERIFIED | zero condition Eq 196 (two layers, weak-reflection form) split into real/imaginary parts; Eq 197b follows by eliminating beta1 + beta2 |
| ch21-p64-417 (198) | 21 | worked example | numeric (book values) | VERIFIED | n = 1, 1.38, 1.72, 1.52: Eq 197b gives beta1 = 164.269 deg (book 164 deg 16'); Eqs 197 + 197a give beta2 = 224.53 deg (book 224 deg 36'), and the exact Eq 50 reflectance of that pair is 1.2e-06. The book's second value 346 deg 52' satisfies Eq 197 (sine) only, not 197a; its exact R is 0.0118 |
| ch21-p64-418 (198a) | 21 | worked example | numeric + scan | FLAG | 1962 ORIGINAL (sic, scan p.21-64 prints beta1 = 199 deg 44' here and in the next paragraph): the second root of Eq 197b is 360 deg - 164 deg 16' = 195 deg 44'. With 195 deg 44' the pair (135 deg 24') gives exact R = 1.2e-06; with the printed 199 deg 44' it gives 1.5e-04. 13 deg 08' again satisfies Eq 197 only (R = 0.0118) |
| ch21-p66-419 (199) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-420 (200) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-421 (200a) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-422 (200b) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-423 (200c) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-424 (200d) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-425 (201) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-426 (202) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p67-427 (203) | 21 | relation | reference (standard form) | VERIFIED | quarter-wave admittance transfer Y_(v-1) = n^2/Y_v applied to the two designs |
| ch21-p69-428 (204) | 21 | relation | reference (standard form) | VERIFIED | repeated application of Y_(v-1) = n_(v-1)^2/Y_v through N quarter waves |
| ch21-p69-429 (204a) | 21 | relation | reference (standard form) | VERIFIED | repeated application of Y_(v-1) = n_(v-1)^2/Y_v through N quarter waves |
| ch21-p69-430 (204b) | 21 | relation | reference (standard form) | VERIFIED | repeated application of Y_(v-1) = n_(v-1)^2/Y_v through N quarter waves |
| ch21-p69-431 (205) | 21 | relation | reference (standard form) | VERIFIED | repeated application of Y_(v-1) = n_(v-1)^2/Y_v through N quarter waves |
| ch21-p69-432 (205a) | 21 | relation | reference (standard form) | VERIFIED | repeated application of Y_(v-1) = n_(v-1)^2/Y_v through N quarter waves |
| ch21-p69-433 (206) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p69-434 (207) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p69-435 (207a) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p69-436 (208) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p69-437 (208a) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p70-438 (209) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p70-439 (210) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p70-440 (211) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p71-441 (212) | 21 | relation | numeric (book values) | VERIFIED | quarter-wave stacks: Eq 205/209 Y_1 and Eq 206/210 rho_0 equal the reference reflectance (even and odd N) |
| ch21-p73-442 (213) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p73-443 (214) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p75-444 (215) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p75-445 (216) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p75-446 (217) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p75-447 (218) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p75-448 (219) | 21 | definition | reference (definition) | DEFINITION | Fabry-Perot with coated plates: A, transmission, phase conditions |
| ch21-p76-449 (220) | 21 | relation | reference (standard form) | VERIFIED | orders at lambda0 |
| ch21-p76-450 (221) | 21 | relation | reference (standard form) | VERIFIED | orders at lambda0 |
| ch21-p76-451 (222) | 21 | relation | numeric (book values) | VERIFIED | Airy function T = T_max/(1 + 4A sin^2(alpha/2)/(1-A)^2) falls to T_max/2 at sin(dalpha/2) = (1-A)/(2 sqrt A), i.e. \|dalpha\| = (1-A)/sqrt(A) in the small-angle limit (within 0.5% for A >= 0.8). Cites 16-(113); the matching ch16 equation is 16-(112) |
| ch21-p76-452 (223) | 21 | relation | reference (standard form) | VERIFIED | d(alpha)/d(lambda) with 2 n d = nu lambda |
| ch21-p76-453 (224) | 21 | relation | reference (standard form) | VERIFIED | d(alpha)/d(lambda) with 2 n d = nu lambda |
| ch21-p76-454 (225) | 21 | relation | symbolic (sympy) | VERIFIED | 2\|dlambda\| = (lambda/nu)(1-A)/(pi sqrt A) = lambda/(nu f), f = pi sqrt(A)/(1-A) |
| ch21-p76-455 (225a) | 21 | relation | symbolic (sympy) | VERIFIED | 2\|dlambda\| = (lambda/nu)(1-A)/(pi sqrt A) = lambda/(nu f), f = pi sqrt(A)/(1-A) |
| ch21-p76-456 (225b) | 21 | relation | symbolic (sympy) | VERIFIED | 2\|dlambda\| = (lambda/nu)(1-A)/(pi sqrt A) = lambda/(nu f), f = pi sqrt(A)/(1-A) |
| ch21-p76-457 (226) | 21 | relation | symbolic (sympy) | VERIFIED | 2\|dlambda\| = (lambda/nu)(1-A)/(pi sqrt A) = lambda/(nu f), f = pi sqrt(A)/(1-A) |
| ch21-p76-458 (227) | 21 | relation | symbolic (sympy) | VERIFIED | \|rho0\| = \|rho0'\| |
| ch22-p08-001 (1) | 22 | relation | reference (standard form) | VERIFIED | maximum flux a detector of area A in a medium of index n can accept: pi I n^2 A (etendue n^2 A pi) |
| ch22-p08-002 | 22 | relation | numeric (book values) | VERIFIED | aperture of 75 mm radius |
| ch22-p08-003 | 22 | definition | reference (definition) | DEFINITION | flux element through a tilted aperture |
| ch22-p08-004 | 22 | definition | reference (definition) | DEFINITION | flux element through a tilted aperture |
| ch22-p08-005 | 22 | definition | reference (definition) | DEFINITION | flux element through a tilted aperture |
| ch22-p08-006 | 22 | relation | symbolic (sympy) | VERIFIED | solid-angle element of a cone: dw = 2 pi sin(alpha) d alpha |
| ch22-p08-007 (2) | 22 | definition | reference (definition) | DEFINITION | Eqs 2-3 integration of dF |
| ch22-p08-008 (3) | 22 | definition | reference (definition) | DEFINITION | Eqs 2-3 integration of dF |
| ch22-p09-009 (4) | 22 | relation | symbolic (sympy) | VERIFIED | Eq 4 integral |
| ch22-p09-010 (5) | 22 | worked example | symbolic (sympy) | VERIFIED | Eq 5 with A = 75^2 pi |
| ch22-p09-011 | 22 | definition | reference (definition) | DEFINITION | etendue limit F <= F_s |
| ch22-p09-012 | 22 | definition | reference (definition) | DEFINITION | etendue limit F <= F_s |
| ch22-p09-013 (6) | 22 | worked example | numeric (book values) | VERIFIED | 75^2 pi sin^2(10 deg) = 532.9 -> 533/n^2 |
| ch22-p09-014 (7) | 22 | relation | reference (standard form) | VERIFIED | general and non-ideal (k) forms of the same etendue inequality |
| ch22-p09-015 (8) | 22 | relation | reference (standard form) | VERIFIED | general and non-ideal (k) forms of the same etendue inequality |
| ch22-p09-016 (9) | 22 | relation | reference (standard form) | VERIFIED | general and non-ideal (k) forms of the same etendue inequality |
| ch22-p09-017 (10) | 22 | relation | reference (standard form) | VERIFIED | general and non-ideal (k) forms of the same etendue inequality |
| ch22-p10-018 (9') | 22 | relation | reference (standard form) | VERIFIED | general and non-ideal (k) forms of the same etendue inequality |
| ch22-p10-019 (10') | 22 | relation | reference (standard form) | VERIFIED | general and non-ideal (k) forms of the same etendue inequality |
| ch22-p10-020 | 22 | worked example | symbolic (sympy) | VERIFIED | integral of sin from 0 to 60 deg = 1 - cos 60 = 0.5 |
| ch22-p10-021 | 22 | worked example | symbolic (sympy) | VERIFIED | integral of sin from 0 to 60 deg = 1 - cos 60 = 0.5 |
| ch23-p02-001 | 23 | relation | reference (standard form) | VERIFIED | useful-magnification rule 1000 x N.A. (Lost Gem) |
| ch23-p02-002 | 23 | definition | reference (definition) | DEFINITION | half-angle and numerical aperture definitions |
| ch23-p03-003 | 23 | definition | reference (definition) | DEFINITION | half-angle and numerical aperture definitions |
| ch23-p03-004 | 23 | relation | reference (standard form) | VERIFIED | Abbe resolution with oblique/condenser illumination d = lambda/(NA_cond + NA_obj) |
| ch23-p09-005 | 23 | relation | reference (standard form) | VERIFIED | Huygenian 3:1 field/eye lens ratio with d = 2 f_eye |
| ch23-p10-006 | 23 | relation | symbolic (sympy) | VERIFIED | d(power)/dn = 0 for two thin lenses of one glass gives d = (f1 + f2)/2; 3:1 Huygenian gives d = 2 f_eye |
| ch23-p10-007 | 23 | relation | symbolic (sympy) | VERIFIED | Ramsden: f1 = f2 = f, d = 2f/3 -> f_eq = 3f/4 |
| ch23-p18-008 | 23 | definition | reference (definition) | DEFINITION | phasor sum P = D + S (Zernike phase-contrast picture, Fig 23.18) |
| ch23-p21-009 | 23 | relation | reference (standard form) | VERIFIED | optical path difference and phase of a specimen of thickness t |
| ch23-p22-010 | 23 | definition | reference (definition) | DEFINITION | relative visibility bookkeeping (Table 23.1 footnote formula; three table entries don't follow it, flagged in the chapter) |
| ch24-p03-001 (1) | 24 | relation | reference (standard form) | VERIFIED | Conrady's Rayleigh-limit (lambda/4) Seidel tolerances: LA 4 lambda/(N' sin^2 U'), zonal 6 lambda/(N' sin^2 U'), OSC lambda/(2 N' sin U'), focal range lambda/(N' sin^2 U') |
| ch24-p03-002 (2) | 24 | relation | reference (standard form) | VERIFIED | Conrady's Rayleigh-limit (lambda/4) Seidel tolerances: LA 4 lambda/(N' sin^2 U'), zonal 6 lambda/(N' sin^2 U'), OSC lambda/(2 N' sin U'), focal range lambda/(N' sin^2 U') |
| ch24-p03-003 (3) | 24 | relation | reference (standard form) | VERIFIED | Conrady's Rayleigh-limit (lambda/4) Seidel tolerances: LA 4 lambda/(N' sin^2 U'), zonal 6 lambda/(N' sin^2 U'), OSC lambda/(2 N' sin U'), focal range lambda/(N' sin^2 U') |
| ch24-p03-004 (4) | 24 | relation | reference (standard form) | VERIFIED | Conrady's Rayleigh-limit (lambda/4) Seidel tolerances: LA 4 lambda/(N' sin^2 U'), zonal 6 lambda/(N' sin^2 U'), OSC lambda/(2 N' sin U'), focal range lambda/(N' sin^2 U') |
| ch24-p03-005 (5) | 24 | relation | none | NOT VERIFIED | astigmatism tolerance lambda/(4 N' sin^2 U'): the chapter does not define which astigmatic distance Ast's is; a Rayleigh lambda/4 criterion gives lambda/(N' sin^2 U') for the full T-S separation, so the factor 4 cannot be confirmed from the text |
| ch24-p03-006 (6) | 24 | relation | reference (standard form) | FLAG | 1962 ORIGINAL (sic): U_m unprimed, inconsistent with Eqs 1-5 (U'_m); otherwise equals Eq 4 |
| ch24-p03-007 | 24 | relation | symbolic (sympy) | VERIFIED | stated as a small-angle assumption: sin^2(U/2) - sin^2(U)/4 = O(U^4) |
| ch25-p05-001 (1) | 25 | relation | reference (standard form) | VERIFIED | prism/goniometer geometry of Fig 25.x (not re-derived: figure-dependent) |
| ch25-p07-002 (2) | 25 | relation | symbolic (sympy) | VERIFIED | spherometer with legs on an equilateral triangle of side d: r = a^2/(2s) + s/2 with a = d/sqrt(3) |
| ch25-p08-003 | 25 | relation | reference (standard form) | VERIFIED | critical-angle refractometer relation n_s = sqrt(n_p^2 - sin^2 i_r) |
| ch25-p10-004 (3) | 25 | relation | reference (standard form) | VERIFIED | thin-film/air-gap interference maxima and minima (half- and quarter-wave conditions) |
| ch25-p10-005 (4) | 25 | relation | reference (standard form) | VERIFIED | thin-film/air-gap interference maxima and minima (half- and quarter-wave conditions) |
| ch25-p12-006 (5) | 25 | relation | reference (standard form) | VERIFIED | thin-film/air-gap interference maxima and minima (half- and quarter-wave conditions) |
| ch25-p12-007 (6) | 25 | relation | reference (standard form) | VERIFIED | thin-film/air-gap interference maxima and minima (half- and quarter-wave conditions) |
| ch25-p14-008 (7) | 25 | relation | reference (standard form) | VERIFIED | optical path of a reflected film with the lambda/2 reflection phase change |
| ch25-p14-009 | 25 | worked example | numeric (book values) | VERIFIED | 0.5461e-3/(3 x 50) = 3.641e-6 rad = 0.751 arcsec |
| ch25-p15-010 | 25 | definition | reference (definition) | DEFINITION | geometric equality in the figure |
| ch25-p16-011 (8) | 25 | relation | reference (standard form) | VERIFIED | fringe count for a thickness or index change in double pass: 2(n-1) dt/lambda, 2 dn t/lambda |
| ch25-p16-012 (8a) | 25 | relation | reference (standard form) | VERIFIED | fringe count for a thickness or index change in double pass: 2(n-1) dt/lambda, 2 dn t/lambda |
| ch25-p20-013 (9) | 25 | relation | none | NOT VERIFIED | Hartmann-type ratio relations of the figure; the symbols eta, xi, p, g, S are defined only in the figure |
| ch25-p20-014 (10) | 25 | relation | none | NOT VERIFIED | Hartmann-type ratio relations of the figure; the symbols eta, xi, p, g, S are defined only in the figure |
| ch25-p27-015 (11) | 25 | relation | reference (standard form) | VERIFIED | Fraunhofer diffraction as a 2-D Fourier transform with u = 2 pi x/(lambda s) |
| ch25-p27-016 | 25 | relation | reference (standard form) | VERIFIED | Fraunhofer diffraction as a 2-D Fourier transform with u = 2 pi x/(lambda s) |
| ch25-p27-017 | 25 | relation | reference (standard form) | VERIFIED | Fraunhofer diffraction as a 2-D Fourier transform with u = 2 pi x/(lambda s) |
| ch25-p28-018 | 25 | relation | reference (standard form) | VERIFIED | Fraunhofer diffraction as a 2-D Fourier transform with u = 2 pi x/(lambda s) |
| ch26-p05-001 (1) | 26 | relation | reference (standard form) | VERIFIED | empirical root-sum-square combination of resolution limits |
| ch26-p08-002 (2) | 26 | definition | reference (definition) | DEFINITION | KDC efficiency and contrast definitions |
| ch26-p09-003 | 26 | definition | reference (definition) | DEFINITION | KDC efficiency and contrast definitions |
| ch26-p10-004 (3) | 26 | definition | reference (definition) | DEFINITION | KDC efficiency and contrast definitions |
| ch26-p11-005 (4) | 26 | relation | reference (standard form) | VERIFIED | imaging as convolution with the spread function; transfer function = its Fourier transform |
| ch26-p11-006 (5) | 26 | relation | reference (standard form) | VERIFIED | imaging as convolution with the spread function; transfer function = its Fourier transform |
| ch26-p11-007 (6) | 26 | relation | reference (standard form) | VERIFIED | imaging as convolution with the spread function; transfer function = its Fourier transform |
| ch26-p12-008 (7) | 26 | definition | reference (definition) | DEFINITION | sinusoidal test-object luminance |
| ch26-p20-009 (8) | 26 | relation | numeric (book values) | VERIFIED | square-wave Fourier series 4/pi [cos - cos3/3 + cos5/5 - ...] reproduces a +-1 square wave (400 terms, mean error < 1%) |
| ch26-p20-010 (9) | 26 | definition | reference (definition) | DEFINITION | square-wave (r) and sine-wave (R) response ratios |
| ch26-p20-011 (10) | 26 | definition | reference (definition) | DEFINITION | square-wave (r) and sine-wave (R) response ratios |
| ch26-p20-012 (11) | 26 | relation | numeric (book values) | VERIFIED | Coltman pair: Eq 11 applied to a test sine response, then Eq 12 (with Coltman's continuation of the series), recovers it to < 1% |
| ch26-p20-013 (12) | 26 | relation | numeric (book values) | VERIFIED | Coltman pair: Eq 11 applied to a test sine response, then Eq 12 (with Coltman's continuation of the series), recovers it to < 1% |

## Totals

- Display blocks: **1399** (all accounted for).
- VERIFIED 1013 · FIXED 7 · DEFINITION 319 · FLAG 34 · NOT VERIFIED 26.
- Checked and holding (VERIFIED + FIXED): **1020**; plus 319 definitions = 1339 of 1399 clean.
- FLAG breakdown: 24 rows are confirmed 1962 print errors; 8 are ch05 transcription-fidelity problems; 2 other (ch13-p43-070, ch19-p10-009).
- Supplementary: 2 rows (1 VERIFIED, 1 FLAG).
