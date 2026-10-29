# Scientific Validation Report — MIL-HDBK-141 Chapter 8
**Chapter:** 8 — Aberration Analysis and Third Order Theory (22 pages)
**Validator response date:** 2026-09-06
**Prompt source:** exchanges/20260827_ch08_validate_prompt.md
**Validated source:** ocr_output/ch08.md

> Method note: The validator's model in this session cannot render images, so the scan
> pages could not be read independently. All items were checked from the corrected OCR
> text against optical engineering first principles and standard references (Born & Wolf
> *Principles of Optics*, Kingslake *Lens Design Fundamentals*, Smith *Modern Optical
> Engineering*, Welford *Aberrations of Optical Systems*). Algebra and arithmetic were
> verified numerically. Confidence is high for derivable items; items requiring the scan
> image (Table 8.2/8.4 values) are marked QUERY.

---

## EQUATIONS

```
ITEM: A1 — Meridional ray polynomial Eq.(1)
STATUS: PASS
FINDING: Correct odd-power polynomial for meridional transverse aberration (symmetry forces
odd powers of Y1). The claim b1=0 at the paraxial image plane is correct: the linear term is
pure defocus, and vanishes only when the ray-height plane coincides with paraxial focus.

ITEM: A2 — Focus shift from fan slope Eq.(2)
STATUS: PASS
FINDING: Final relation t_k ≈ −(y/u_{k−1})·Δ(Y_k−Ȳ_k)/ΔY_1 is correct. Verified by paraxial
scaling: slope of the axial fan ∝ ΔY/ΔY_1 = Y_k/y_1 and t_k = −Y_k/u_{k−1}, giving
t_k = −(y_1/u_{k−1})(ΔY/ΔY_1). For object at infinity −y/u_{k−1} = f' is correct (a parallel
axial ray at height y emerges at angle u_{k−1} = −y/f'). Note: the intermediate OCR steps
"tan U ≈ y/u_{k−1}" are dimensionally garbled (length vs. dimensionless) but the final result
is right, so this is an OCR-presentation issue, not an error in the result.

ITEM: A3 — Third-order spherical aberration Eq.(3)
STATUS: PASS
FINDING: Correct Seidel transverse spherical aberration. Denominator 2(n_{k−1}u_{k−1})y_1^2
is the correct form; b_3 = −ΣB/(2 n_{k−1}u_{k−1} y_1^2) reproduces the worked example
(−0.006341 → −0.0214 at Y1=1.5) and matches Fig. 8.5. The book's own §8.5.3.2 relation
"Seidel longitudinal = 3Y_{3k}/u_{k−1}" is also correct: it uses the differential slope
(d/dY_1 of the cubic gives 3b_3Y_1^2), i.e. the infinitely-close-zone focus shift, per §8.5.1.4,
not the marginal-ray chord slope (which would give Y_{3k}/u_{k−1}). Both are legitimate, distinct
definitions; the factor 3 is consistent with differentiating the cubic. The literal dimensions of
Eq.(3) are a legacy notational quirk (paraxial "u" treated as dimensionless slope), not an error.

ITEM: A4 — Seidel S and B, Eqs.(4)(5)
STATUS: PASS
FINDING: B=Si^2 with S = y n_{−1}(n_{−1}/n − 1)(u+i) is the classic legacy Seidel surface-sum form
and is internally consistent (produces b_3 matching the figure and Table 8.2). It is a different
algebraic normalization from the modern y(n'−n)(u'/n' − u/n) form; the two are related through the
paraxial refraction equation (n'i' = ni, u' = u − yc(n'−n)/n'), but I could not establish exact
term-by-term equality, so the equivalence proposed in the prompt is convention-dependent rather than
an identity. Not an error; treat as verified-through-internal-consistency.

ITEM: A5 — Oblique aberration polynomials Eqs.(6)(7)
STATUS: PASS
FINDING: Confirmed correct against derivatives of the standard Seidel wavefront. (a) Spherical
aperture dependence Y(3Y²+X²) [meridional] and X(Y²+X²) [sagittal] are the classic forms.
(b) Coma: meridional ∂/∂Y[(Y²+X²)Y]·Ȳ_o gives 3Y²·Ȳ_o, sagittal ∂/∂X gives 2XY·Ȳ_o — the factors
3 (Eq.6) and 2 (Eq.7) are correct. (c) Astigmatism+Petzval: taking S_III=2C, S_IV=2(C+PΦ²) in the
standard (S_III+½S_IV) / (½S_IV) transverse coefficients yields exactly meridional (3C+PΦ²) and
sagittal (C+PΦ²) — so the combined form (3ΣC+ΣPΦ²) is correct, not (ΣC+ΣPΦ²).

ITEM: A6 — Distortion Eqs.(8)(9)
STATUS: PASS
FINDING: Transverse distortion ∝ (field ratio)³ (Eq.8) and fractional distortion ∝ (field ratio)²
(Eq.9) are correct standard results. Fractional distortion varies as the square of the field ratio,
as required. The apparent dimensional looseness of Eq.(9) as written is a legacy-units quirk.

ITEM: A7 — Field curves Eqs.(10)–(12)
STATUS: FLAG
FINDING: Eqs.(10) and (11) (tangential ∝ 3C+PΦ², sagittal ∝ C+PΦ²) and the individual
t_P = −ΣPΦ²/(2 n u²)(...) form are correct. The Petzval relation stated as t_{kP} = 2 t_{kS} − t_{kT}
is WRONG. Substituting (10),(11) gives 2t_S − t_T ∝ 2(C+P) − (3C+P) = (P − C), which is not the
Petzval-only term; the correct identity is t_P = (3 t_S − t_T)/2, which yields exactly
(3(C+P) − (3C+P))/2 = P. This matches the standard Coddington/Petzval rule T = 3S − 2P (i.e.
2t_P = 3t_S − t_T). Likely an OCR error (dropped "/2" and misread 3 as 2), or a source error.
The concluding claim "for ΣC=0: t_{kP}=t_{kS}=t_{kT}" is correct.

ITEM: A8 — Surface contributions F, C, E, P Eqs.(11)–(14)
STATUS: PASS (F, C, E) / QUERY (P sign convention)
FINDING: (a) F=Siī and C=Sī² are correct standard forms (coma ∝ axial×chief incidence, astig ∝ ī²).
(b) E = S̄īi + Φ̄(ū_{−1}²−ū²) is a recognizable legacy distortion surface-sum form and plausible.
(c) P = c(n_{−1}−n)/(n_{−1}n): summed over a thin lens it gives ΣP = −φ/n, which is exactly
consistent with the book's own thin-lens Eq.(28). This is internally consistent BUT the sign is
opposite the common Petzval convention (ΣP = +Σφ/n), and combined with Eq.(12) it yields
t_P > 0 (away from lens) for a positive lens, whereas the standard physical result is t_P < 0
(Petzval surface bulges toward the lens, undercorrected). This may be a pure book sign-convention,
but it should be confirmed against Fig. 8.10 (does the plotted Petzval surface curve inward?).

ITEM: A9 — Aspheric contributions Eqs.(4a),(11a)–(13a)
STATUS: PASS
FINDING: B = 8(n_{−1}−n)e y^4 is the standard 4th-order-aspheric spherical-aberration surface
contribution (coefficient 8 is correct; depends on e and y^4, independent of curvature c). The ratios
F/B = ȳ/y, C/B = (ȳ/y)², E/B = (ȳ/y)³ are correct. No Petzval (no added first-order power to O(1))
and no chromatic (surface shape, no dispersion) contributions: correct.

ITEM: A10 — Stop shift equations Eqs.(18)–(23)
STATUS: PASS
FINDING: All correct. ΣB* = ΣB and ΣP* = ΣP (stop-invariance) are standard. F*, C* are standard.
The distortion term Q(3ΣC + ΣPΦ²) is the correct translation of the standard Q(3S_III + S_IV)
(with S_III=2C, S_IV=2(C+PΦ²) the combination reduces to 3C+PΦ²) — the proposed alternative
Q(ΣC+ΣPΦ²) would be wrong. Chromatic a*=a, b*=Qa+b are the correct chromatic stop-shift equations.

ITEM: A11 — Thin lens coefficients Eqs.(24)–(28)
STATUS: PASS
FINDING: (a) B quadratic in c_1 (bending): correct. (b) F linear in c_1: correct. (c)
C = −φΦ² for a thin lens at the stop: correct (astigmatism of a thin lens at the stop is independent
of bending, depends only on power and conjugate). (d) E=0 for stop at lens: correct. (e)
P = −φ/n: correct (matches the Eq.(14) surface-sum result).

ITEM: A12 — Thin lens coefficient constants Eqs.(29)–(35) [FLAGGED]
STATUS: FLAG
FINDING: The general structure (quadratic in c_1 for B with α_i ∝ φ³, φ², φ; linear in c_1 for F;
bending-independent C) is correct and consistent with standard thin-lens Seidel theory. The numerical
factors (n+2)/(n−1), 4(n+1)/(n−1), 4(2n+1)/(n−1), (3n+2)/(n−1), (2n+1)/(n−1) are the recognizable
standard thin-lens coefficient factors, so the reconstruction is likely close. Eq.(35)
Φ = yū − ȳu is the correct Lagrange–Helmholtz invariant. However, Eq.(34) "φ = yu_{−1} − yu = yu − ȳu"
is dimensionally inconsistent as transcribed (φ has units 1/length; the right-hand side is length)
and is clearly OCR-garbled (it duplicates Φ). These coefficients must be re-verified against a
standard source (Born & Wolf §9.3 / Welford) before use, as the prompt already flagged.
```

---

## NUMERICAL CHECKS

```
ITEM: B1 — b3 arithmetic and 5th-order residual
STATUS: PASS (with minor note)
FINDING: b5 = 0.002818 (from −b3·(1.5)³/(1.5)⁵ = 0.006341/2.25) and the Y1=1.0 prediction
Y = b3+b5 = −0.006341+0.002818 = −0.003523 are both correct; the residual vs. the traced −0.0041 is
0.0006, a plausible 5th-order (and O(7)) residual for a lens with a large-incidence-angle surface, as
the book argues. Minor note: exact division gives b3 = −0.02135/3.375 = −0.006326, not −0.006341;
−0.006341 corresponds to Y_{3k} = −0.02140. The two quoted values are inconsistent at the ~0.2% level
(a rounding/reading slip in the source or the figure); insignificant to the physics.

ITEM: B2 — Table 8.3 sign discrepancies
STATUS: FLAG
FINDING: All three are almost certainly OCR errors, not genuine thick-lens effects.
(a) Petzval P, lens (b): −0.1770 (thin) → +0.1759 (thick) is impossible — Petzval does not change
sign with small thickness; the thick value should be −0.1759 (dropped minus). The near-identical
magnitude supports this. (b) Coma F, lens (c): 0.0136 → 0.1029 (7.5×) is implausible for a small
thickness correction, especially since lenses (a) and (b) show F changing only ~10%; the thick value
is misread (expect ~0.012–0.014). (c) Distortion E, lens (b): −0.0182 → +0.0195 sign flip; E can in
principle change sign near a node, but a full flip at near-equal magnitude for small thickness,
combined with the dropped-minus pattern on the same row (P), makes a dropped minus on the thick value
(−0.0195) most likely. Human check against the scan is warranted.

ITEM: B3 — Aspheric at pupil vs. image
STATUS: QUERY
FINDING: Aspheric at pupil (ȳ=0): only B nonzero — correct. Aspheric at image (y=0): the claim that it
"corrects distortion" is PHYSICALLY correct (a 4th-order aspheric near an image adds an OPD ∝ Ȳ⁴ for
oblique beams, whose derivative ∝ Ȳ³ is a cubic distortion), but it does NOT follow from Eqs.(4a,11a–13a)
at y=0: those give B=0 and E = B(ȳ/y)³ → 0·∞ (indeterminate; the regulated limit is 8(n_{−1}−n)e·y·ȳ³ → 0
as y→0). The book's formulas are valid for a regular refracting surface with finite axial-ray height;
at a focal surface the operative coordinate is field height ȳ (chief ray), a distinct mechanism the
formulas do not capture. The book's treatment is incomplete/ambiguous here and should be clarified —
do not present "aspheric at image" as following from Eqs.(4a,11a–13a).
```

---

## CONCEPTUAL / PHYSICAL CLAIMS

```
ITEM: C1 — ΣB and ΣP stop-shift invariance
STATUS: PASS
FINDING: Correct. Spherical aberration depends only on the axial paraxial ray, which is unchanged by
moving the stop; Petzval depends only on surface curvatures/indices (the invariant term), also
unchanged. Hence stop position cannot correct spherical aberration or Petzval curvature.

ITEM: C2 — Three higher-order design rules (§8.7.4.2)
STATUS: PASS
FINDING: All three are physically justified. (1) Balanced, alternating-sign third-order contributions
keep the fifth-order (quadratic-in-surface-terms) residuals small. (2) Higher-order terms scale steeply
with incidence angle. (3) Local correction lets the correlated higher-order terms of adjacent,
geometrically similar (similar ȳ/y) surfaces cancel; remote correction leaves them uncancelled. All
correct and sound.

ITEM: C3 — Thin lens astigmatism C = −φΦ² (Eq.26)
STATUS: PASS
FINDING: With ȳ=0 at the lens, Φ = yū, giving C = −φ(yū)² = −φΦ². Consistent with the bending-
independent astigmatism of a thin lens at the stop and with the sum of C = Sī² over the two surfaces
in the book's convention. Sign consistent within the chapter.

ITEM: C4 — Thin lens distortion E = 0 (Eq.27)
STATUS: PASS
FINDING: Correct. With the stop at the thin lens, the chief ray passes undeviated through the center:
ī ≈ 0 and ū_{−1} = ū, so both terms of E = S̄īi + Φ̄(ū_{−1}²−ū²) vanish. This is the standard result
that a thin lens used as the stop produces no distortion.
```

---

## GEMS

```
ITEM: Gem 8.1 — Meridional fan slope = longitudinal focus shift
STATUS: PASS
FINDING: Correct and accurately sourced to §8.5.1. The slope-to-t_k relation, the f' identification
for object at infinity, and the "slope at chief ray gives field curvature" remark are all sound.

ITEM: Gem 8.2 — Third-order spherical aberration from paraxial data alone
STATUS: PASS
FINDING: Correct. b3 from paraxial data only is the chapter's central result and is validated by the
worked example. The one caveat (inherited from B1) is the ~0.2% rounding inconsistency between
Y_{3k}=−0.02135 and b3=−0.006341; immaterial to the gem's usefulness.

ITEM: Gem 8.3 — Three rules for controlling higher-order aberrations
STATUS: PASS
FINDING: Correct restatement of §8.7.4.2; rules are sound (see C2). "Correct locally, similar ȳ/y"
is an accurate capture of the book's argument.

ITEM: Gem 8.4 — Stop shift equations (18)–(23)
STATUS: PASS
FINDING: All seven equations transcribed correctly, including the distortion term Q(3ΣC+ΣPΦ²) and the
two chromatic relations. The practical-value claims (single paraxial trace, ΣB/ΣP invariance) are
correct.

ITEM: Gem 8.5 — Aspheric surface aberration ratio rule
STATUS: QUERY
FINDING: The ratio formulas B, F=B(ȳ/y), C=B(ȳ/y)², E=B(ȳ/y)³ are correct (see A9). The "aspheric at
an image (y=0) corrects only distortion" claim carries the B3 caveat: it is physically true via a
field-coordinate mechanism, but it does not follow from these formulas at y=0 (which give E=0 or 0/0).
Recommend softening/qualifying that specific sentence in the gem.
```

---

## SUMMARY

```
ITEM: Chapter summary
STATUS: PASS
FINDING: Accurately represents the chapter content and covers all major topics: spot diagrams,
meridional/skew fans, spherical aberration, oblique Seidel polynomials, distortion, field curves,
surface contributions, afocal systems, stop-shift equations, thin-lens theory, aspherics, and the
three design rules. No major topic is missing. The stated numerical sums from Table 8.2
(ΣF=−0.000170, ΣC=−0.004200, ΣE=−0.002070) are plausible orders for a balanced triplet but are not
independently verifiable from text alone (marked QUERY-adjacent); they should be confirmed when
Table 8.2 is extracted. The summary correctly flags the Table 8.3 discrepancies.
```

---

## TABLES

```
ITEM: Table 8.1 — sample triplet data
STATUS: PASS
FINDING: Reasonable and consistent with the surrounding text (BFL=82.794 mm, entrance pupil 2.2 cm
right of first surface, vignetted 10°/20° fans). Placeholder needs scan extraction for exact radii;
curvatures stated in §8.10.2.2 (c1(a)=0.253, c1(b)=−0.200, c1(c)=0.050) are cross-referenced consistently.

ITEM: Table 8.2 — full surface third-order calculation
STATUS: QUERY
FINDING: Individual surface values are not readable in the OCR and could not be independently checked
(no scan read in this session). The reported totals are plausible and the b3/−0.02135 cross-check with
Fig. 8.5 is internally consistent. Full verification requires scan extraction.

ITEM: Table 8.3 — thin vs. thick lens comparison
STATUS: FLAG
FINDING: See B2. Three entries are almost certainly OCR errors (P sign flip lens (b); F 7.5× lens (c);
likely E sign flip lens (b)); the "−0.1770/−0.1759" P and the near-equal thin/thick magnitudes on all
other rows confirm thickness corrections are small, so the three flagged rows should read
(−0.1759, likely −0.0195, and an F near 0.012–0.014).

ITEM: Table 8.4 — thin lens coefficient calculation
STATUS: QUERY
FINDING: Placeholder only; partial OCR (y², y⁴, n+1, n+2, u_{−1}/y) is internally plausible but the
derived α/β values require scan extraction. Cross-check the thin-lens coefficients here against a
standard source given the A12 flags.
```

---

## OVERALL ASSESSMENT

The scientific quality of the Chapter 8 transcription is high. The core Seidel framework — the
meridional polynomial (A1), the fan-slope to focus-shift relation (A2), the third-order spherical
aberration formula and its paraxial-data derivation (A3, A4), the full oblique Seidel polynomials with
the correct coma (3/2) and astigmatism+Petzval ((3C+P)/(C+P)) factors (A5), distortion (A6), the
aspheric ratio rule (A9), the stop-shift equations including the correct Q(3C+ΣPΦ²) distortion term
(A10), and the thin-lens coefficients (A11) — all check out against first principles and standard
references, and the worked numerical example is internally consistent. Gems 8.1–8.4 and the three
design rules (C2) are accurate. The chapter summary is faithful and complete. The systemic issues are
concentrated in a few specific spots, in decreasing confidence: (1) the field-curve Petzval relation
Eq.(12) is written as t_P = 2t_S − t_T but the only internally and physically consistent form is
t_P = (3t_S − t_T)/2 — a definite FLAG (very likely OCR, possibly source); (2) the Table 8.3
thin/thick sign and magnitude discrepancies are OCR errors, not physics (Petzval and coma cannot move
by those amounts for a small thickness); (3) the "aspheric at an image corrects distortion" claim is
physically true but does not follow from the book's own aspheric formulas at y=0 and needs a caveat;
(4) the reconstructed thin-lens constant coefficients (A12) and Table 8.4 require source verification,
with Eq.(34) clearly OCR-garbled. A residual ~0.2% rounding inconsistency between Y_{3k} and b3 is
immaterial. Confidence in the chapter's scientific accuracy is HIGH, pending (a) a human/scan check of
the Eq.(12) Petzval relation and the three Table 8.3 entries, (b) extraction of Tables 8.2 and 8.4,
and (c) verification of the thin-lens constants against a standard source.
