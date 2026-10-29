# Ch10 Validation Report — An Application of the Method of Lens Design

**Validator:** independent scientific second opinion (against MIL-HDBK-141, 1962)
**Date:** 2026-09-06
**Inputs:** `ocr_output/ch10.md` (corrected chapter), `20260828_ch10_validate_prompt.md` (checklist)
**Method:** first-principles verification of all stated equations, re-derivation of the
ray traces in Tables 10.4 and 10.7, recomputation of the parabola roots and Petzval sum,
and cross-checks against standard Seidel / thin-lens theory.

All numerical checks below were recomputed independently (not read from the OCR).

---

## EQUATIONS

```
ITEM: E1 — Lateral color condition and t3/t5 = (1/R)(νa/νc)  [prompt A1]
STATUS: PASS
FINDING: The zero-lateral-color condition Σ(y ȳ φ/ν) = 0 with ȳ_b = 0 reduces correctly
to y_a ȳ_a φ_a/ν_a + y_c ȳ_c φ_c/ν_c = 0. With R = y_a φ_a/(y_c φ_c) this gives
ȳ_a/ȳ_c = −(1/R)(ν_a/νc), and since the undeviated chief ray through lens b is a straight
line, ȳ_a/ȳ_c = t3/t5 (paraxial), hence t3/t5 = (1/R)(ν_a/νc). The νa=νc simplification to
t3/t5 = 1/R is correct. The "stop conjugate to lens b" reading of the ȳ_b = 0 assumption is
the correct physical interpretation. The general (νa≠νc) form is stated correctly in the
OCR (line 57/61); the prompt's simplified form is valid only for equal outer glasses.
```

```
ITEM: E2 — Petzval sum  [prompt A2]
STATUS: PASS
FINDING: Pa+Pb+Pc = −0.12346 + 0.23191 − 0.13717 = −0.02872, verified. The negative lens
contributing +0.23191 (positive) is physically correct: P = −φ/n and φ_b < 0, so P_b > 0.
Backing out the element powers (φ = −P·n) gives φ_a = +0.2000, φ_b = −0.3750, φ_c = +0.2222,
consistent with Table 10.4. Iterating from the −0.0287 estimate toward the −0.03 target is
reasonable.
```

```
ITEM: E3 — Axial color residual TAch = 0.0026  [prompt A3]
STATUS: PASS
FINDING: The per-lens chromatic contributions Σ(−φ y²/ν) = −(0.2·1²)/60.3 − (−0.375·0.8²)/36.6
− (0.2222·0.9²)/60.3 = 0.000256. Dividing by |u_{k-1}| = 0.1 (the f'=10 normalization) gives
TAch = 0.00256 ≈ 0.0026. Internally consistent. The value is a small, plausible residual for
an uncorrected P-N-P triplet of f'=10 being steered toward TAch = 0. (b) still contributes to
axial color because axial color depends on y (axial ray height), not ȳ; the ȳ_b = 0 condition
kills only the lateral color term y_b ȳ_b φ_b/ν_b.
```

```
ITEM: E4 — Four third-order conditions ΣB, ΣF, ΣC, ΣE  [prompt B1]
STATUS: PASS
FINDING: The four simultaneous conditions and the assignment of the stop-shifted (asterisked)
coefficients to lenses a and c, with lens b unstarred, are consistent with the ȳ_b = 0 design.
E_b = 0 follows because distortion (third-order) is ∝ powers of ȳ_b, and ȳ_b = 0. ΣC =
−(1/3)ΣPΦ² is the book's astigmatism = 0 target from Eq 8-(9); it is a balanced field-curvature
condition in this convention and is used self-consistently throughout. CAVEAT for the prompt
only (not the chapter text): the prompt's B1(c) claim that "stop is at lens a so E_a = 0" is
inconsistent with the chapter — the design puts the chief ray through the CENTER OF LENS b
(ȳ_b = 0, so E_b = 0, while ȳ_a ≠ 0 and E_a ≠ 0). The chapter text (ocr_output/ch10.md) does
not make this error.
```

```
ITEM: E5 — C_b = −φ_b Φ² independent of bending  [prompt B2]
STATUS: PASS
FINDING: Correct. A thin lens located at (conjugate to) the aperture stop has its
astigmatism coefficient determined solely by its power and the configuration, independent of
shape (bending); the bending-dependent terms vanish with ȳ_b = 0. The chapter correctly uses
this to reduce Eq (3) to a two-variable problem in c2 and c6. (The exact meaning of the Φ²
normalization is book-conventional but the physical claim — constancy in bending — is sound.)
```

```
ITEM: E6 — Parabola method 3Y_k = −2.0(c_i − c_vertex)² + 3Y_k,vertex  [prompt B3]
STATUS: PASS
FINDING: All roots verified. For System 16A (c_vertex = 0.3380, 3Y_k,vertex = 0.016):
√(0.016/2.0) = 0.0894; c2 = 0.3380 ± 0.0894 = 0.249 / 0.427; c4 = −0.295 / −0.116;
c6 = −0.011 / 0.167. All match the chapter. The coefficient −2.0 is dimensionally consistent
when c_i is expressed in inverse units of the f'=10 normalization (curvatures here ~0.1–0.5
in units of 1/10), so −2.0 carries units of length². The claim that −2.0 is approximately
constant across glass combinations is an empirical result from the 29-system study and is
flagged in-text as "for practical purposes" — acceptable for a handbook heuristic.
```

```
ITEM: E7 — Axial ray traces, Tables 10.4 and 10.7  [new check]
STATUS: PASS
FINDING: Both traces reproduce exactly under the book's paraxial convention u' = u − φ·y.
Table 10.4 (y1=1): u3 = −0.20, y_b = 0.8, u5 = +0.10, y_c = 0.9, u_exit = −0.10 → f' = 1/0.10 = 10.
Table 10.7 (y1=1.5): u3 = −0.276, y_b = 1.158, u_after_b = +0.126, u_exit = −0.15 → f' = 1.5/0.15 = 10.
The chief-ray row (ȳ_b = 0, ȳ_c = 0.5, ū_after_c = 0.389, back-space 9.0 → ȳ_k = 4.0) is also
consistent. Minor sign-convention quirks in the OCR'd ū column are cosmetic, not errors.
```

---

## GEMS

```
ITEM: G1 — Gem 10.1 Triplet airspace ratio rule (t3/t5 = 1/R)
STATUS: PASS
FINDING: The formula 1/R = y_c φ_c/(y_a φ_a) is correct for the equal-glass (νa = νc) case it
states, and the R ≈ 1 guidance is supported by the chapter's thin-lens study. Caveat: the rule
is a THIN-LENS paraxial relation; in the thick-lens tables (10.8–10.10) the reported R does not
equal the airspace ratio t3/t5 (see T4). The gem should state this applicability boundary.
```

```
ITEM: G2 — Gem 10.2 Triplet glass selection rule
STATUS: PASS
FINDING: Correct and faithful to the chapter. Large Δν lowers the spherical-aberration parabola
(needed for the two solutions to converge) but lengthens the system; optimum balances the two at
R slightly above 1. The screening condition "parabola vertex 3Y_k,vertex > 0 for real solutions"
is mathematically correct for a downward-opening parabola (if the vertex is ≤ 0 it never crosses
zero). Sound pre-ray-trace screen.
```

```
ITEM: G3 — Gem 10.3 Parabola method for triplet bending
STATUS: PASS
FINDING: Formula and two-root prescription c_i = c_vertex ± √(3Y_k,vertex/2.0) verified
arithmetically (see E6). The 5-minute pre-design screen (vertex>0 check, two-root warm start for
an optimizer) is sound and genuinely useful.
```

```
ITEM: G4 — Gem 10.4 Left-hand solution preference
STATUS: PASS
FINDING: Supported by the chapter: the left-hand solution is shorter, lies closer to the
parabola vertex (lower sensitivity to curvature/manufacture error, per §10.3.3), and is
"definitely superior" at large field (>15°) in the spot-diagram study. The claim that every
viable triplet has two third-order solutions follows from the two roots of the parabola. Fine.
```

---

## SUMMARY

```
ITEM: S1 — Summary claim "φ_a + φ_b + φ_c = 0.1"
STATUS: FLAG
FINDING: Incorrect. From the chapter's own Petzval data the element powers are φ_a = +0.2000,
φ_b = −0.3750, φ_c = +0.2222, which sum to +0.0472, NOT 0.1. The total system power of 0.1
(f' = 10) is achieved through the finite airspaces; for separated lenses Σφ ≠ Φ_total. The
summary conflates total power with the sum of element powers. Suggested correction: state
Φ_total = 0.1 with element powers φ_a = 0.20, φ_b = −0.375, φ_c = 0.222 (Σ = 0.047).
```

```
ITEM: S2 — Summary labels the design "f/5"
STATUS: FLAG
FINDING: The actual design is f/3.33, not f/5. §10.4.1 sets entrance-pupil diameter 3 with
f' = 10 → semi-aperture y1 = 1.5 → f/ = 10/(2·1.5) = 3.33; Table 10.7 and all subsequent
ray traces use y1 = 1.5. "f/5" refers only to the third-order coefficient normalization
(y1 = 1, §10.3.1). The summary (and validate prompt) carries "f/5" as if it were the design
aperture. The two should be reconciled against the original scan; the ray-traced numbers are
internally consistent only at f/3.33.
```

```
ITEM: S3 — Remaining summary content (steps one through six, targets, table R/T values)
STATUS: PASS
FINDING: Accurately represents the chapter: glass selection, TAch = 0.0026, ΣP = −0.02872
(target −0.03), the 29-system study, the four third-order conditions, the parabola method,
the two-solution left/right structure, the IBM 650 7-variable design, and the iterative
revision ΣP → −0.035 → −0.040 with t4 → 0.15 all match the body text.
```

---

## TABLES

```
ITEM: T1 — Table 10.8 (ΣP = −0.035), T verification  [prompt C1]
STATUS: PASS
FINDING: T is the total barrel length front-of-(a) to back-of-(c): T = t2 + t3 + t4 + t5 + t6.
Left hand: 0.600 + 1.3949 + 0.2500 + 0.9631 + 0.600 = 3.808. Right hand: 0.600 + 0.8572 +
0.2500 + 1.628 + 0.600 = 3.935. Both match exactly. (The prompt's guesses T = t3+t5 or
t3+t4+t5 were wrong; the correct definition includes both positive-lens thicknesses.)
```

```
ITEM: T2 — Table 10.9 (ΣP = −0.040), t3 = 1.211 and T  [prompt C2]
STATUS: PASS
FINDING: The OCR correction from "4.211" to 1.211 is justified: T = 0.600 + 1.211 + 0.250 +
1.016 + 0.600 = 3.677 matches the stated T exactly (4.211 would give T = 6.677). Right hand
T = 0.600 + 0.8900 + 0.250 + 1.426 + 0.600 = 3.766 also matches. t3 = 1.211 is correct.
```

```
ITEM: T3 — Table 10.10 (t4 = 0.15), T and R  [prompt C3]
STATUS: PASS / FLAG
FINDING: T values verify: left 0.600 + 1.128 + 0.150 + 1.0738 + 0.600 = 3.552; right
0.600 + 0.9289 + 0.150 + 1.3209 + 0.600 = 3.600. FLAG: the right-hand R appears as 1.383 in
the table but the body text (§10.6.2) states "0.987 and 1.363." One of these is a
transcription/OCR discrepancy that should be checked against the original scan.
```

```
ITEM: T4 — R vs. airspace ratio t3/t5 in the thick-lens tables  [prompt C1/C2/C3]
STATUS: QUERY
FINDING: In all thick-lens tables the reported R does NOT equal the airspace ratio:
T10.8 L t3/t5 = 1.448 vs 1/R = 1.301; T10.8 R 0.527 vs 0.549; T10.9 L 1.192 vs 1.111;
T10.9 R 0.624 vs 0.670; T10.10 L 1.051 vs 1.013; T10.10 R 0.703 vs 0.723. The relation is
close but not exact (4–11% off). Because T sums reproduce exactly from the OCR'd airspaces,
the airspace values are reliable; therefore R in these tables is a separate design variable
(per §10.4.3, R was freed to correct distortion), only approximately tied to t3/t5 once
thickness is introduced. The thin-lens relation t3/t5 = 1/R remains correct for the first-order
stage. Recommend confirming the book's intended definition of R in Tables 10.8–10.10 against
the original scan.
```

```
ITEM: T5 — Glass/power and ray-trace tables 10.1–10.5, 10.7
STATUS: PASS
FINDING: Spot-checked Table 10.4 (axial + chief ray) and Table 10.7 (y1 = 1.5) reproduce
exactly under u' = u − φ·y; f' = 10 confirmed in both. Petzval and chromatic sums in Table 10.5
verified (see E2, E3). BFD values (8.453 / 7.599) are plausible for this barrel length and
curvature set; not independently re-derived but within a reasonable range.
```

---

## OVERALL ASSESSMENT

The scientific content of the corrected Chapter 10 is fundamentally sound and internally
consistent. Every equation I could verify against first principles checks out: the lateral-color
and Petzval conditions, the axial-color residual, the four third-order Seidel conditions, the
bending-parabola method (all three sets of roots reproduce exactly), and the full axial and
chief-ray traces in Tables 10.4 and 10.7 (f' = 10 confirmed in both). The design narrative and
the four "Lost Gems" faithfully represent the chapter, and the iterative rationale
(under-correct ΣB = −0.006, more-negative ΣP to lower the parabola, thinner negative lens to
converge the two solutions, left-hand solution superior at large field) is physically sensible
and standard. I found no errors in any stated equation. The issues are confined to (a) the
summary's claim φ_a + φ_b + φ_c = 0.1, which is wrong (the element powers sum to 0.047; 0.1 is
the total system power achieved via airspaces), (b) the "f/5" label, which conflicts with the
y1 = 1.5 / entrance-pupil-diameter-3 ray trace that makes the design f/3.33, and (c) the
right-hand R discrepancy (1.383 table vs 1.363 text) in Table 10.10. One systematic point:
the R = t3/t5 relation is a thin-lens paraxial result and does not hold exactly in the thick-lens
tables, where R is a freed design variable — the summary and Gem 10.1 should state this boundary,
and the book's thick-lens definition of R should be confirmed against the original scan. Overall
confidence in the chapter's scientific accuracy is HIGH for the equations and ray-trace data and
MODERATE-to-HIGH for the summary's parameter labels (φ-sum, f-number), which need the two
corrections above.
