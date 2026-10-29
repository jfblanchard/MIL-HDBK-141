# Chapter 11 — Telescope Objectives: Scientific Validation Report

**Validator:** Devin (independent second opinion)
**Date:** 2026-09-06
**Inputs:** `exchanges/20260830_ch11_validate_prompt.md`, `ocr_output/ch11.md`
**Method:** First-principles checks against optical engineering (Kingslake, Born & Wolf, Smith),
plus internal-consistency arithmetic verification of the worked examples.

---

## EQUATIONS

```
ITEM: EQ-A — Achromatic doublet power split (φa = φ·νa/(νa−νb), φb = −φ·νb/(νa−νb))
STATUS: PASS
FINDING: Verified against the two simultaneous conditions Σφ = φ and Σ(φ/ν) = 0; solving gives
exactly these expressions (numerator check: φa(1 − νb/νa) = φ → φa = φ·νa/(νa−νb)). Sign and
magnitudes correct for crown/flint (νa > νb).
```

```
ITEM: EQ-B — Petzval sum ΣP = −φ·(νa/na − νb/nb)/(νa − νb)
STATUS: PASS
FINDING: The minus sign is a convention difference, not an error. For a thin lens the Petzval
term is +φ/n; summing φa/na + φb/nb yields +φ·(νa/na − νb/nb)/(νa − νb). The handbook defines
P = −φ/n (Eq 8-28, quoted in §11.1.3.2), so under that sign convention the overall minus is
internally consistent and correct. Note the numerator is positive here (crown has higher ν/n),
so the physical field curvature magnitude is |ΣP| = φ·(νa/na − νb/nb)/(νa − νb).
```

```
ITEM: EQ-C — Zonal tolerance (Yk)_zone = 4.6λ / Lk−1
STATUS: QUERY
FINDING: The internal arithmetic is self-consistent (4.6×0.5893/0.14 = 19.4 µm; scaling
10×0.0194/0.000526 ≈ 369 mm, both reproduced), but I could not reproduce the constant 4.6 from
the stated Rayleigh λ/4 criterion. Applying the book's own EQ-D relation at the 0.707 zone
(Y1 ≈ 1.0, f' = 10) gives OPD = 0.0194×1.0/(2×10) ≈ 0.00097 mm ≈ 1.65λ at the quoted tolerance,
i.e. well above λ/4. My first-principles derivations of a diffraction-limited zonal tolerance
return constants in the range ~0.4 (λ/4 at the edge for primary spherical aberration balanced at
the margin) to ~5 (defocus-based, at the zone) depending on the balance criterion, none cleanly
equal to 4.6. Also note the formula is only dimensionally coherent if Lk−1 is treated as a
dimensionless direction cosine/NA (= Y1/f' ≈ 0.14), which should be stated explicitly. Recommend
a third-opinion check of the 4.6 derivation against the original scan; it may correspond to a
more lenient (non-strict λ/4) practical tolerance rather than the Rayleigh criterion.
```

```
ITEM: EQ-D — OPD = Yk · Y1 / (2f')  (focus-shift / transverse aberration)
STATUS: PASS
FINDING: Correct for a longitudinal (defocus) error. A defocus wavefront is parabolic in the
pupil, so OPD = ½·(Yk/f')·Y1 (the ½ arises from the quadratic pupil dependence), not Yk·Y1/f'.
Verified numerically: at f/16.7 with f'=10 cm, Y1=0.3, Yk=0.00015 cm gives OPD = 0.0382λ,
matching the text (§11.4.6). The factor 1/2 is justified and correct for this application.
```

```
ITEM: EQ-E — Secondary-spectrum threshold at f/16.7 (65.8 cm)
STATUS: PASS
FINDING: Arithmetic verified. OPD at f'=10 cm, f/16.7 is 0.038λ; scaling to λ/4 gives factor
0.25/0.038 = 6.58, hence 65.8 cm. The transverse value 0.00015 cm is reconciled with the
f'/2200 rule if f'/2200 is read as the *longitudinal* secondary spectrum: transverse at zone
Y1 is (f'/2200)·(Y1/f') = Y1/2200 = 0.30/2200 ≈ 0.000136 cm, consistent with the book's
0.00015 cm (rounding). The whole chain (§11.4.6, GEM-11.5) is internally consistent.
```

```
ITEM: EQ-F — Triplet collinearity determinant Δ = |P* P** 1| = 0 for primary+secondary color
STATUS: FLAG
FINDING: The determinant condition is conflated with the wrong aberration. Per the chapter
itself, collinearity in P* vs P** space (§11.4.3.5, Fig 11.11) is the condition for suppressing
the *tertiary* spectrum (residual color at other wavelengths), whereas simultaneous F/C/D
(primary+secondary) correction requires a *finite, non-zero* triangle area in the P* vs ν space
(§11.4.3.3, Fig 11.10); that determinant (Eq 20) appears in the *denominator* of the power
solutions, so a zero determinant would give impractically large/infinite element powers. The
statement "Δ = 0 enables simultaneous correction of primary and secondary color" is therefore
reversed. Modern analog: an apochromat needs the three glasses to be non-collinear in the
partial-dispersion vs Abbe plot (distinct anomalous partial dispersions, e.g. ΔP_{g,F} off the
normal line); collinearity in the higher-order P*/P** plane is the tertiary-color criterion.
```

---

## GEMS

```
ITEM: GEM-11.1 — Fraunhofer (crown-first) gives 1.5–2× the useful field of Steinheil
STATUS: QUERY
FINDING: The qualitative claim is sound and standard — crown-first telescope objectives have
better off-axis correction (smaller coma at the stop) and are the preferred orientation — but
the specific "1.5–2×" factor does not appear anywhere in this chapter's OCR, which only states
that flint-in-front "offer no advantages" (§11.2.3.1) and that crown-first has "the most
favorable shape for the passage of the axial rays." The number likely comes from gem
enrichment/general literature; document its source before publishing.
```

```
ITEM: GEM-11.2 — Petzval curvature scales as 1/MP² (objective negligible vs eyepiece)
STATUS: PASS
FINDING: The scaling law and its conclusion (objective field-curvature contribution ~γo/(νo·MP²)
vs eyepiece ~γe/νe, i.e. ~1/100 at MP=10) are consistent with the afocal angular-magnification
argument and the book's own assertion that the angular aberration varies as the square of MP
(§11.1.3.4) and that the objective is negligible at high power (§11.1.3.8). Caveat: the
supporting OCR sentence in §11.1.3.8 ("objective contribution is multiplied by the magnifying
power ... yet negligible at high power") is internally contradictory as transcribed and should
be re-checked against the scan; the scientific conclusion itself is correct.
```

```
ITEM: GEM-11.3 — Zonal tolerance (Yk)_zone = 4.6λ/Lk−1; diffraction-limited when satisfied
STATUS: QUERY
FINDING: Consistent with EQ-C. The book's wording specifies the marginal ray (Y_max) is set to
Yk = 0 and the tolerance is on the residual; the "0.707-zone" attribution is the conventional
zone but is not explicit in the OCR. The constant 4.6 (and whether it truly enforces a λ/4 OPD)
remains unverified — see EQ-C.
```

```
ITEM: GEM-11.4 — Air-spaced doublet achieves 3–5× less zonal aberration than best cemented
STATUS: QUERY
FINDING: The qualitative mechanism (§11.3.4.3 — air space drops the marginal rays lower before
the negative element, reducing the positive fifth-order term, so third order can be made less
negative) is physically sound and the reduced zone is clearly shown in Figs 11.4–11.6/Table 11.9.
However, the specific 3–5× figure is not extractable from the OCR'd tables (Table 11.9's last
columns are OSC' coma values, not zonal), so the quantitative claim could not be verified
against the source data.
```

```
ITEM: GEM-11.5 — Secondary spectrum threshold: no apochromat below f' = 65.8 cm at f/16.7
STATUS: PASS
FINDING: Arithmetic verified (see EQ-E). This is a legitimate consequence of the f'/2200
secondary-spectrum rule combined with the Rayleigh λ/4 criterion at f/16.7; the 65.8 cm and
131.6 cm (2×) scalings are internally consistent and physically reasonable.
```

```
ITEM: GEM-11.6 — Herzberger P*/P** rule: large triangle area in P* vs P** space → usable apochromat
STATUS: FLAG
FINDING: The two coordinate spaces are conflated. Large triangle area (→ moderate element
powers) is required in the P* vs ν space (§11.4.3.3), which governs the F/C/D correction;
in the P* vs P** space one instead wants the three glasses *near-collinear* (small area) to
suppress tertiary spectrum (§11.4.3.5). As stated, "large area in P* vs P** space" would
maximize, not minimize, tertiary color. Correct guidance: large area in P* vs ν for element
powers + near-collinearity in P* vs P** for tertiary. Maps to modern terms as non-collinearity
in P_{g,F} vs ν (distinct ΔP_{g,F}) for the F/C/D correction.
```

---

## SUMMARY

```
ITEM: Chapter summary (intro Petzval, thin-lens tables, thick-lens/zonal, secondary spectrum,
Herzberger, two triplets, conclusions)
STATUS: QUERY
FINDING: The summary accurately reflects the chapter's arc and content (§11.1 Petzval/Table 11.1;
§11.2 thin-lens doublets; §11.3 thick-lens four-degrees-of-freedom and zonal correction;
§11.4 secondary spectrum, Herzberger P*/P**, and the two ray-traced triplets; §11.5 conclusions
on anomalous-dispersion glasses and higher-order spherical risk). Two items need checking:
(1) "16 Steinheil-form designs" — the OCR'd Table 11.4 contains ~38 flint-in-front rows
(matching Table 11.3's 38 cases), so the "16" count appears wrong or unverified and should be
recounted against the scan; (2) the "(MP ≥ 4×)" threshold is an editorial framing not stated in
the source (the book only says "high power telescopes"). Additionally, the §11.4.2.4 claim that
index accuracy of ~1–2×10⁻⁵ is needed to hold secondary spectrum to 1/10 is qualitatively
correct (secondary spectrum is famously sensitive to index error) but the exact 1/2200
amplification factor could not be independently re-derived from the OCR'd Eq 13.
```

---

## TABLES

```
ITEM: Table 11.12 — Doublet vs triplet element powers
STATUS: PASS
FINDING: Both rows sum correctly to 0.100 (doublet 0.21380 − 0.1138 = 0.1000; triplet
0.2812 − 0.4747 + 0.2935 = 0.1000), and the thin-lens solution (§11.4.5.1: 0.338 − 0.721 +
0.483 = 0.100) is consistent. Magnitudes are physically reasonable for an apochromat: the
triplet's much larger element powers (up to ~5× the net 0.1, with KzFS-4 the strong negative)
are the expected signature explaining the small relative aperture, and are consistent with the
glass roles (F-1 positive, KzFS-4 strong negative with anomalous partial dispersion, PKS-1
positive). Note: OCR read the doublet crown power as 0.21880; the scan value 0.21380 (which
makes the sum exactly 0.1) is correct.
```

```
ITEM: Table 11.13 — Triplet lens spec (F-1 / KzFS-4 / PKS-1) and ray-trace data
STATUS: PASS
FINDING: Internally consistent and physically correct. At the small aperture (Y1=0.25) the D, F,
C transverse values (3.7e-6, 9.2e-5, 2.3e-5) cluster near zero, confirming the F/C/D common-focus
(secondary-color) correction; the growing divergence at Y1=0.5 (D=−1.06e-3, F=−5.7e-4,
C=−1.14e-3) reflects the large higher-order/chromatic-variation-of-spherical expected for such a
triplet, exactly matching the book's description that the triplet only beats a doublet within
Y1≲0.4 and must be stopped to f/16.7. Thicknesses and BFD (9.2728 for f=10) are plausible.
Minor: the last curvature reads "+0.1272" in OCR vs "−0.1272" in the prompt; OCR routinely drops
signs, so confirm the sign against the scan (does not affect the scientific assessment).
```

---

## OVERALL ASSESSMENT

Confidence in the chapter's scientific content is **high** for the first-order and thin-lens
core (EQ-A, EQ-B, EQ-D, EQ-E all verified from first principles; both table power sums and the
triplet ray-trace data check out), and the overall arc and worked arithmetic are internally
consistent. Two genuine issues surfaced, both confined to the Herzberger secondary-color
section: the determinant/collinearity condition (EQ-F) and the corresponding gem (GEM-11.6)
conflate the P* vs ν space (where a non-zero triangle is needed for F/C/D correction) with the
P* vs P** space (where near-collinearity suppresses tertiary color); these should be corrected,
as they would mislead a reader about how to select glasses. The zonal-tolerance constant 4.6
(EQ-C/GEM-11.3) is asserted without derivation and could not be reconciled with a strict λ/4
criterion (it corresponds to ~1.6λ under the chapter's own OPD relation); flag for a human
check against the scan. Lesser items: the "16 Steinheil designs" count in the summary, the
unattributed "1.5–2×" and "3–5×" factors in GEM-11.1/GEM-11.4, and the OCR sign on Table 11.13's
last curvature all warrant a quick confirmation. No errors were found in the verified thin-lens
equations, the secondary-spectrum threshold arithmetic, or the table power/ray-trace consistency.
