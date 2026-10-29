# Independent Scientific Validation — ch11 (Telescope Objectives, deep pass)

**Validator:** second-opinion review per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`
**Date:** 2026-09-18
**Method:** Independent re-derivation of all equations; numerical recomputation of all
worked examples and tables; direct comparison with scan pages 1, 7, 8, 12, 19, 20,
24, 25 of `docs/scans/ch11.pdf` for contested items. Primary agent's notes and
briefs were not consulted.

---

## Equations

ITEM: Eq (1), (2) — Petzval angular aberrations α_y, α_x
STATUS: PASS
FINDING: Scan-verified verbatim. Physically sound: L, K, M are ray direction
cosines, so α_y = L/M − L̄/M̄ is the meridional angular aberration. ΣP Φ²/(2n·y)
is dimensionless once Φ carries the (length) invariant, and the aberration
scales as (Ȳ_o/ȳ_o)², i.e., as field² — correct for Petzval.

ITEM: Unnumbered eq in §11.1.3.4 and Eq (3) — telescope Petzval angular aberration
STATUS: PASS
FINDING: Numerically verified against Table 11.1. With (Ȳ_o/t_o)·MP = −0.6,
y_{k−1} = −0.35 cm, φ_e = 0.5, γ_o = γ_e = 1.5, Eq (3) gives
α_y = 0.021·(1 − 1/MP) rad → 108.3′ / 86.6′ / 79.4′ at MP = −2/−5/−10
(Table: 107′ / 87′ / 79′), and d = 100α/y_{k−1} gives −9.0 / −7.2 / −6.6 D
exactly. Sign convention confirmed by the text (positive = oblique bundles
focused behind the eye).

ITEM: Eqs (4)–(7) — achromatic doublet power split
STATUS: PASS
FINDING: Standard result, signs verified: for ν_a = 63.5 (crown), ν_b = 30.6
(flint), φ_a = +1.93φ, φ_b = −0.93φ.

ITEM: Eq (8) — doublet Petzval sum ΣP = −φ(ν_a/n_a − ν_b/n_b)/(ν_a − ν_b)
STATUS: PASS
FINDING: Re-derived from ΣP = −φ_a/n_a − φ_b/n_b with Eqs (6)–(7). For crown/
flint pairs evaluates to ≈ −φ/1.4, consistent with the stated γ_o ≈ 1.5 and the
text's claim that the ratio is nearly glass-independent.

ITEM: Eqs (9)–(12) — thin-lens B (quadratic) and F (linear) bending polynomials
STATUS: PASS
FINDING: Correct functional form for third-order thin-lens aberration vs.
element curvature; consistent with §8.10 methodology.

ITEM: §11.3.2.3 derivative system (ΔΣB, ΔΣF, ΔΣa vs. c_1, c_2, c_3)
STATUS: PASS

ITEM: §11.3.3.1 zonal tolerance (Y_k)_zone = 4.6λ/L_{k−1}
STATUS: PASS
FINDING: Scan-verified verbatim, including "L_{k−1} = optical direction cosine
of the emerging ray." Longitudinal equivalent ≈ 4.6λ/sin²U′ — consistent with
the classic ~4–6λ/sin²U zonal-aberration tolerances (Conrady era). Arithmetic
verified: 4.6 × 0.5893 µm / 0.14 = 19.4 µm; scaling 10 × 0.0194/0.000526 =
369 mm; residual −0.000526 matches Table 11.6 Y_D at Y_1 = 1.0 (the 0.71 zone).

ITEM: §11.3.4.4 aspheric deflection ΔY_k = λ[6fS⁵ + 8gS⁷ + 10hS⁹ + …]
STATUS: PASS
FINDING: Consistent as the aperture derivatives of S⁶, S⁸, S¹⁰ deformation
terms (the S⁴ term was already consumed correcting third order). Note: the λ
here is the deformation-to-deflection constant from Eq 8-(4a), not wavelength —
harmless symbol collision worth an editorial footnote in the modern edition.

ITEM: §11.3.4.5 triplet B/F coefficient equations
STATUS: PASS
FINDING: Same quadratic/linear structure as the doublet case; correct DOF count
(cemented b–c pair → c_1 and c_3 as variables).

ITEM: Eq (13) — index accuracy dn_λ = [d(TAch)/TAch]·(n_D − 1)/2200
STATUS: PASS
FINDING: With n_D − 1 ≈ 0.5, (n_D − 1)/2200 ≈ 2.3 × 10⁻⁴; demanding secondary
spectrum ≤ 1/10 normal requires dn ≈ 2 × 10⁻⁵ — exactly the text's "2 in the
fifth decimal place," and the ×2 error-combination argument then gives 1 × 10⁻⁵.
Self-consistent and physically standard.

ITEM: Eqs (14)–(16) — three-glass apochromat conditions
STATUS: PASS
FINDING: Total power, F/C achromatism (Σφ/ν = 0), and D-light secondary-spectrum
correction (ΣφP̃*/ν = 0) all correct.

ITEM: Eqs (17)–(20) — Cramer's-rule solution with Δ = det[P̃*, ν, 1]
STATUS: PASS
FINDING: Independently re-solved the 3×3 system; φ_a = φν_a(P̃*_c − P̃*_b)/Δ etc.
verified algebraically (the denominator reduces to exactly the printed
determinant). Note: Δ is strictly twice the signed triangle area — the text's
"the value of which is the area" is loose but is the source's own phrasing.

ITEM: φ_a/φ_c ratio and following inequality (§11.4.3.4)
STATUS: QUERY
FINDING: The ratio φ_a/φ_c = (ν_a/ν_c)(P̃*_c − P̃*_b)/(P̃*_b − P̃*_a) is correct.
The next sentence — "(P̃*_c − P̃*_a) should be less than (P̃*_b − P̃*_a)" —
is transcribed verbatim from the scan (confirmed at 600 dpi), but is physically
inconsistent with the ratio above: for φ_a/φ_c ≈ 1 with ν_a/ν_c > 1 the needed
condition is (P̃*_c − P̃*_b) < (P̃*_b − P̃*_a). The printed P̃*_c − P̃*_a
(equivalent to P̃*_c < P̃*_b) appears to be a source typo, not a transcription
error. Recommend an editorial footnote; do not silently "fix."

ITEM: Eqs (21), (22) — residual tertiary transverse aberration
STATUS: PASS
FINDING: Substitution of (17)–(19) into (21) reproduces (22) exactly; the
numerator expands to det[P̃*, P̃**, 1] as stated, hence the collinearity
argument. Dimensionally consistent.

ITEM: §11.4.6 OPD = Y_k·Y_1/(2f′)
STATUS: PASS
FINDING: Derived independently: defocus OPD = Δf·Y_1²/(2f′²) with Δf = Y_k·f′/Y_1
gives the printed form. All downstream arithmetic verified: 0.00015 cm ×
0.3/(2×10) → 0.038λ; 0.25/0.038 × 10 cm = 65.8 cm; ×2 = 131.6 cm;
131.6/16.7 = 7.9 cm diameter.

ITEM: §11.3.2.5 coefficients b_3 = −0.0014, b_5 = 0.000619
STATUS: QUERY
FINDING: Could not reproduce the Table 11.6 D-light curve from these under
obvious normalizations (raw Y_1 powers, Y_1/1.4-normalized, or tan U′ basis).
The fit basis/normalization in Eq 8-(1) is not given in this chapter. Not
necessarily wrong — flagging for someone with ch08 access to re-check the
basis of the fit.

---

## Gem claims

ITEM: Gem 11.1 — Fraunhofer orientation (crown in front)
STATUS: PASS (rule) / QUERY (mechanism & quantification)
FINDING: The orientation rule is correct and chapter-supported (§11.2.2.3:
"most favorable shape for the passage of the axial rays … Fraunhofer
objectives"). Two embellishments are NOT in the chapter: (a) the stated
off-axis/chief-ray-AOI mechanism — the book's stated reason is axial-ray
passage; (b) the "1.5–2× field" figure, which I cannot confirm from the chapter
or a standard reference. Suggest rewording the mechanism to match the source
and dropping or hedging the numeric claim.

ITEM: Gem 11.2 — Petzval scaling, objective contribution ∝ 1/MP²
STATUS: FLAG
FINDING: The conclusion (objective Petzval negligible at high MP → use a
doublet) is chapter-supported, but the scaling exponent is wrong. Eq (3)
suppresses the objective term by 1/MP relative to the eyepiece term:
the bracket is (−1/(γ_o·MP) + 1/γ_e), i.e., objective:eyepiece = γ_e/(γ_o·MP).
For γ_o = γ_e at MP = 10 the objective adds ~10% of the eyepiece contribution,
not 1%. Correct the gem to P_eff ≈ P_eye + P_obj/MP (or equivalently note the
suppression is already inside P_obj = φ_o/γ_o since φ_o = φ_e/MP); "100× smaller
at MP = 10" should read ~10×. The "P_obj ≤ 0.5·P_eye acceptable at MP ≥ 3"
quick-check is also unsupported by the chapter.

ITEM: Gem 11.3 — zonal tolerance |Y_zone| ≤ 4.6λ/|L_marginal|
STATUS: PASS (formula) / FLAG (symbol gloss & example)
FINDING: Formula matches the source exactly. But the gem misdefines
L_marginal as "focus shift of marginal ray relative to paraxial" — the book
defines L_{k−1} as the optical direction cosine of the emerging ray
(≈ sin U′ ≈ 1/(2·f/#)). The worked example is also wrong: at f/10,
L ≈ 0.05, giving 4.6·0.55 µm/0.05 ≈ 50 µm ≈ 0.05 mm, not 0.01 mm.

ITEM: Gem 11.4 — air-spacing to reduce zonal aberration
STATUS: PASS (mechanism) / QUERY (quantification)
FINDING: The mechanism matches §11.3.4.3 verbatim (marginal ray drops, strikes
the overcorrecting surface at lower aperture → reduced positive 5th order →
reduced zone). The quantitative claims are not in the chapter: no "3–5×"
figure appears, and Table 11.9's airspaces span 0.04–0.74 on f′ = 10
(i.e., 0.4–7.4% of focal length), so "typically 1–3% of focal length" is
narrower than the chapter's own data. The coma caveat matches §11.3.6.

ITEM: Gem 11.5 — secondary-spectrum threshold (65.8 cm at f/16.7)
STATUS: PASS (result & OPD equation) / FLAG (intermediate derivation)
FINDING: Headline numbers are all correct and scan-verified (0.038λ, 65.8 cm,
131.6 cm, 7.9 cm; f/#² scaling is also correct). But the intermediate step is
internally inconsistent: "OPD ≈ (f′/2200)·(1/(2×16.7)) ≈ f′/73,480" actually
computes the transverse aberration Y_k = f′/(2200·2·f/#) — not the OPD.
Setting f′/73,480 = λ/4 gives ~1 cm, not 65.8 cm. The correct chain is
Y_k = f′/(4400·f/#) → OPD = Y_k·Y_1/(2f′) = f′/(17,600·f/#²) ≈ f′/4.9×10⁶ at
f/16.7, which does yield ~67 cm ≈ the book's 65.8 cm. The gem reaches the right
answer via a wrong intermediate; fix the derivation.

ITEM: Gem 11.6 — Herzberger P*/P** collinearity rule
STATUS: PASS (substance) / FLAG (wording of the conditions)
FINDING: Core content confirmed by the deep pass and my re-derivation:
zero-residual TAch for the chosen wavelength pair requires the numerator
determinant det[P̃*, P̃**, 1] = 0, i.e., collinearity in the P*–P** plane —
the gem's equation is right. Three wording problems: (a) "area of the triangle
… is proportional to 1/Δ" is garbled — element powers ∝ 1/Δ, triangle area ∝ Δ;
(b) the gem reuses "Δ" for the numerator determinant, while the book's Δ
(Eq 20) is det[P̃*, ν, 1] — a different determinant controlling the secondary
correction; the gem should distinguish them; (c) "any three normal glasses can
be combined as an apochromat in principle" is misleading: glasses collinear on
the P*–ν glass line give Δ → 0, making Eqs 17–19 singular and element powers
infinite — secondary correction requires finite triangle area in the P*–ν
plane, while P*–P** collinearity zeroes the tertiary residual. The f/11–f/16.7
aperture caveat is chapter-verified.

---

## Chapter summary (§11.5)

STATUS: PASS
FINDING: Accurately represents the chapter — Petzval/field-curvature budgeting,
thin- and thick-lens doublet design, four zonal-reduction methods, secondary
spectrum and the three-glass apochromat with Herzberger geometry, and the
physical-optics reality check. The summary's "two glasses with the same P̃* and
P̃**" is verbatim from the scan.

---

## Tables

ITEM: Table 11.1 — angular aberration vs. MP
STATUS: PASS — all six values recomputed from Eq (3).

ITEM: Table 11.2 — thin-lens computing table
STATUS: PASS — structure consistent with a thin doublet in contact;
ΣP row leads correctly to Eq (8).

ITEM: Table 11.3 — Fraunhofer thin-lens doublets
STATUS: FLAG (one corrupted row)
FINDING: Spot-checked C_a, C_b for cases 1, 11, 31 via φ = φ·ν/(Δν),
C = φ/(n−1) — all match to the 4th decimal (e.g. case 31: 1.6831/−1.437 vs.
computed 1.6831/−1.4366). Row 25 is corrupted: it duplicates case 29's glass
pair (1.638/55.5, 1.689/30.9) and C_a (0.3536), has a blank C_b, and carries 11
fields. Scan-verified correct row 25:
`| 1.620 / 60.3 | 1.8052 / 25.5 | 0.2731 | -0.0861 | 0.1498 | -0.1232 | -0.1362 | -0.0502 | 25 |`

ITEM: Table 11.4 — flint-first doublets
STATUS: PASS
FINDING: Scan-verified rows 1, 12, 15, 25, 32–34, 37. Element powers swap
correctly vs. Table 11.3 (C_a/C_b magnitudes exchange with order). The 5-digit
values in row 34 (0.54795, −0.00047) are in the source itself.

ITEM: Tables 11.5–11.7 — thick doublet designs
STATUS: PASS
FINDING: For each: element powers from (n−1)(c_front − c_back) sum to ≈ 0.1
(f′ = 10 confirmed), achromat balance Σφ/ν ≈ 0 confirmed (11.5: 0.002628 −
0.002608; 11.6: 0.003323 − 0.003263; 11.7: 0.003697 − 0.003531). Marginal-ray
D focus ≈ 0 and F/C union at Y_1 = 1.0 hold per conditions (c),(d). Trend with
ν_b (25.4 → 33.8 → 38.0) matches the text's claim on marginal-ray crossing.

ITEM: Table 11.8 — per-surface B contributions
STATUS: PASS — ΣB recomputes to −0.00024 ≈ printed −0.00023; |ΣY_k| =
|ΣB/(2nu)| = 0.00115 verified.

ITEM: Table 11.9 — least-squares solutions
STATUS: FLAG (one corrupted row)
FINDING: The 611588/649338 row ends "-0. | -0.1523 | -0.0444 | +0.0064 |
+0.0039" — a truncated "-0." plus four extra values appended past the
OSC'-marginal column. Needs a scan re-check of that row.

ITEM: Table 11.10 — type 1 vs. type 2 triplet ray data
STATUS: PASS — zonal ratio ≈ 10× claim consistent with the data; minor: the
−0.0004681 entry carries an extra digit (source quirk or OCR, cosmetic).

ITEM: Table 11.11 — triplet lens data
STATUS: PASS — fully recomputed. Type 1: Σφ = 0.0646 + 0.1211 − 0.0857 =
0.1000; φ_a = 0.0646 ≈ the stated 0.066. Type 2: Σφ = 0.0999, φ_a = 0.0660.
Cemented-pair bookkeeping (shared c_4) verified.

ITEM: Table 11.12 — triplet vs. doublet powers
STATUS: PASS — both sums = 0.100; triplet achromat verified exactly
(0.2812/64.5 − 0.4747/44.2 + 0.2935/46.0 = 0.000); doublet 0.2138/63.5 −
0.1138/33.8 = 0. Strong element powers (|φ| sum ~1.05) consistent with the
"small apertures required" argument.

ITEM: Table 11.13 — F-1/KzFS-4/PKS-1 triplet (F-1 front)
STATUS: PASS — Σφ ≈ 0.108 and Σφ/ν ≈ −0.0005 with standard indices
(F-1 = 1.6259/35.7, KzFS-4 = 1.6134/44.3, PKS-1 = 1.5286/77); consistent with
f′ ≈ 10 and back focus 9.27.

ITEM: Table 11.14 — reversed triplet (PKS-1 front)
STATUS: QUERY
FINDING: Transcription is verbatim-correct against the scan, but the printed
curvatures do not recombine to an f′ = 10 achromat: element powers
(0.458/−0.606/+0.450 with standard indices) give Σφ ≈ 0.30, and Σφ/ν ≈
+0.005 ≠ 0. No plausible index assignment or spacing correction fixes this —
likely a misprinted curvature in the source document itself. Recommend an
editorial note; do not alter the transcription.

ITEM: Table 11.13 vs. 11.5.1 thin powers (0.338/−0.721/0.483, Σ = 0.100)
STATUS: PASS — thin-lens starting powers need not equal thick-element powers;
no inconsistency.

---

## Residual OCR / markup artifacts

- §11.4.3.3 (page 19): stray `</file` injected mid-sentence — the text reads
  "…and $\Delta$ </file is positive. In order to minimize $\phi_b$…" Remove the
  tag; words themselves are complete (scan-verified). FLAG (trivial fix).
- §11.4.2 heading/body uses P̃ (no star) while Eqs 16–22 use P̃*/P̃**. Probably
  the book distinguishing F–D vs. λ–D partial dispersions — worth a notation
  note rather than a fix. QUERY (light).
- Table 11.3 row 25 and Table 11.9 last row: corruption detailed above. FLAG.
- The unnumbered equation in §11.1.3.4's denominator (2n_{k−1}y_{k−1}) may
  carry a faint bar over y in the scan; unbarred y is the physically consistent
  reading and matches Eq (1), so no change needed.

---

## Overall assessment

Confidence in the deep pass is **high**. Every numbered equation was either
algebraically re-derived or numerically verified against worked data; Eqs (3),
(4)–(8), (13), (14)–(22), and the OPD relation all check out, and Tables 11.1,
11.5–11.8, 11.11–11.13 recompute correctly to the printed values — an unusually
clean result for OCR-sourced numeric material. The only transcription defects
found are localized: Table 11.3 row 25 (garbled — correct values supplied
above), Table 11.9's final row, and one stray `</file` tag on page 19. Two
genuine *source*-side oddities were uncovered and should be noted editorially
rather than "corrected": the inconsistent inequality in §11.4.3.4 and Table
11.14's curvatures (not an f′ = 10 achromat under standard indices). The b_3/b_5
fit coefficients remain unverifiable without ch08's Eq 8-(1) basis.

On the gem side, the physics judgments are mostly sound but several stated
quantifications outrun the chapter: gem 11.2's 1/MP² suppression should be
1/MP; gem 11.3's L_{k−1} gloss and 0.01 mm example are wrong; gem 11.5's
derivation reaches the right answer through a mislabeled intermediate step;
gem 11.6 conflates the two determinants and garbles the area/power relation;
gems 11.1 and 11.4 carry quantified claims (1.5–2× field, 3–5× zonal, 1–3%
airspace) not supported by the chapter text. Recommend targeted edits to the
gem catalog entries per the findings above.
