# Validation Response — Chapter 26: Evaluation Phase Optical Tests (deep-pass re-validation)

**Date:** 2026-09-13
**Validator:** Independent scientific validator (per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`)
**Input:** `ocr_output/ch26.md` (fresh deep-passed text, 24 pages), re-verified against
prior gem claims 26.1–26.5 (prompt 20260912 listed 26.1–26.4; catalog also contains 26.5;
no gems 26.6–26.9 exist in the catalog — the brief's "26.1–26.9" overcounts by four).

---

## EQUATIONS

### Eq. (1) — Cascaded resolution: 1/R_e = √(1/R₁² + 1/R₂² + …)
**STATUS: PASS**
**FINDING:** Standard quadrature-cascade approximation, correct as stated (analogous to
cascaded amplifier bandwidth). Worked example recomputed: 1/100² + 1/50² = 1×10⁻⁴ + 4×10⁻⁴
= 5×10⁻⁴; R_e = 1/√(5×10⁻⁴) = 44.7 ≈ 45 lp/mm ✓ (gem 26.1's example matches exactly).

### Eq. (2) — KDC efficiency = (α_e/(α_i·M_i)) × 100
**STATUS: PASS**
**FINDING:** Definitionally sound: for a perfect lossless instrument α_i = α_e/M_i →
100%; any real degradation lowers the score. Consistent with its stated purpose (benchmark
vs. the unaided eye).

### Eq. (3) — KDC efficiency = (X_i/(M_i·X_e)) × 100
**STATUS: PASS**
**FINDING:** Verified mutually consistent with Eq. (2): since the threshold angle
α ∝ 1/X (fixed target line width w at threshold distance X, α = w/X), substituting
α_e = w/X_e and α_i = w/X_i into Eq. (2) gives exactly Eq. (3). ✓

### Eq. (4) — Image = convolution: i(x,y) = ∬ S(x−ξ, y−η) O(ξ,η) dξ dη
**STATUS: PASS**
**FINDING:** Standard incoherent imaging convolution of object with spread function ✓.
Minor numbering nit: the prose references "equation (3)" for this display, which is tagged
(4); one stale cross-reference (likely OCR of "(4)"). Cosmetic only.

### Eq. (5) — i(ω_x, ω_y) = τ(ω_x, ω_y)·O(ω_x, ω_y)
**STATUS: PASS**
**FINDING:** Correct transfer-function multiplication in the spatial-frequency domain ✓.

### Eq. (6) — τ(ω_x, ω_y) = (1/2π) ∬ S(x,y) e^{i(ω_x x + ω_y y)} dx dy
**STATUS: PASS**
**FINDING:** Correct Fourier transform of the spread function (prefactor and exponent sign
are convention-dependent, not errors) ✓. Consistent Fourier pair with Eq. (4).

### Eq. (7) — Lamberts: F(x) = b₀ + b₁|A*|cos(2πγx − φ)
**STATUS: PASS**
**FINDING:** Correct form for the image irradiance of a sinusoidal target: mean b₀ plus
modulated cosine with amplitude b₁|A*| (|A*| = sine-wave response) and phase φ ✓.
The "b₁/b₀ normalized amplitude" gloss is the standard Lamberts normalization ✓.

### Eq. (8) — Square-wave Fourier series: F(x) = B₁ + ΔB₁(4/π)[cos(2πnx/δ) − ⅓cos3(2πnx/δ) + ⅕cos5(2πnx/δ) − …]
**STATUS: PASS** (structure) **/ QUERY** (frequency normalization)
**FINDING:** The Fourier series itself is correct: a square wave of amplitude ΔB₁ around
mean B₁ has fundamental (4/π)ΔB₁ and odd harmonics with alternating signs and 1/(2k+1)
weights — standard, verified. The one uncertain detail is the δ in the cosine argument:
it makes the spatial period δ/n (n = cycles per aperture-width δ), whereas the chapter's
own gloss says "n, the number of cycles in some unit distance," which would require the
argument 2πnx. The sentence defining δ (equivalent-rectangle width of the aperture flux
distribution, after Coltman Fig. 26.21) is tied to this equation in the text, so δ may be
faithful to the scan — but the normalization (n per unit length vs. per δ) needs a scan
check before this is quoted in the catalog. Harmless for the later results, which use r(n),
R(n) as functions of the same n.

### Eqs. (9), (10) — r(n) = R(n) = (ΔB₂/ΔB₁)/(B₂/B₁)
**STATUS: PASS**
**FINDING:** Both response factors are contrast ratios (output modulation normalized by
input modulation, (ΔB₂/ΔB₁)·(B₁/B₂) — algebraically identical to the transcribed form).
Having the square-wave and sine-wave response share one formal definition (differing only
in input waveform) is exactly Coltman's convention ✓.

### Eq. (11) — Coltman forward: r(n) = (4/π)[R(n) − R(3n)/3 + R(5n)/5 − R(7n)/7 + …]
**STATUS: PASS**
**FINDING:** Correct and exact; this is the standard published relation (J.W. Coltman,
JOSA 44, 468 (1954)): the square-wave response is the alternating odd-harmonic synthesis of
sine-wave responses, following from the Eq. (8) Fourier coefficients and linearity ✓.

### Eq. (12) — Coltman inverse: R(n) = (π/4)[r(n) + r(3n)/3 − r(5n)/5 + r(7n)/7 + …]
**STATUS: PASS** (as written) **— with a substantive caution**
**FINDING:** The four printed leading coefficients are correct: I re-derived the exact
inversion algebraically (successive cancellation of r(Kn)/K series) and obtained
R(n) = (π/4)[r(n) + r(3n)/3 − r(5n)/5 + r(7n)/7 + 0·r(9n)/9 + r(11n)/11 − r(13n)/13 −
r(15n)/15 − r(17n)/17 + …]. Note the deviation from any simple alternating continuation:
the r(9n) coefficient is exactly **zero** (the 9n contribution cancels via the 3n×3n
cross-term), and r(13n), r(15n), r(17n) are all negative. The book's "…" is safe as printed,
but the ellipsis must not be filled in with a naive alternating sign pattern. If the scan
prints an explicit continuation after r(7n), that continuation deserves a scan check against
the exact coefficients above. In practice the series is truncated after 2–3 terms (R falls
rapidly), so the impact is minor.

---

## GEMS

### 26.1 — Cascaded resolution 1/R_e² = 1/R₁² + 1/R₂² + …
**STATUS: PASS**
**FINDING:** Matches Eq. (1) (equivalent square-root form ✓); worked example recomputed
= 44.7 ≈ 45 lp/mm ✓. Caveats (Gaussian-spread approximation, incoherent imaging) are
correct and appropriately stated.

### 26.2 — Visual test: chart lines must subtend > 60 arcsec at the eye; 26-focal-length distance
**STATUS: PASS**
**FINDING:** ~60 arcsec (1 arcmin) per line pair is the standard eye-resolution figure, and
the requirement that the chart's lines, magnified by the instrument, exceed it is correct
testing methodology (matches §26.1.2.5). The 26f NBS standard distance matches §26.1.2.1
and the Fig. 26.3 caption; the spherical-aberration rationale is stated for the analogous
35f case in §26.1.3.2 and is a fair synthesis. Convention note: the gem's operational
formula 206265/(N·D) arcsec gives the line-**pair** (period) subtense, which is the correct
quantity to compare against the 60-arcsec line-pair eye limit; if one speaks of a single
line, halve it.

### 26.3 — High- vs. low-contrast targets
**STATUS: PASS** (with a QUERY carried on the "1.4" contrast value)
**FINDING:** The distinction, its rationale (steep high-contrast curve → more accurate
threshold; low-contrast target → realistic field prediction), and the "match target to use"
rule are all correct and match §26.1.2.3 and Figure 26.5. One number carries a definitional
QUERY into the gem's table: "black on white, ratio ~1.4" (see Table/Figure QUERY below) —
recommend stating the convention alongside the value.

### 26.4 — Coltman square-wave↔sine-wave conversion
**STATUS: PASS**
**FINDING:** Both series match Eqs. (11)–(12) and the published Coltman result. Caveats are
sound: phase information is lost (modulus only — correct for an odd-symmetric input
measured as contrast), convergence is fast, and nonlinear systems (film) need care —
all stated. The "only the first two or three terms matter" guidance is consistent with the
exact-coefficient analysis above. Note the same caution as Eq. (12): don't extrapolate the
sign pattern of the inverse series beyond r(7n) (r(9n) term is zero).

### 26.5 — KDC visual efficiency
**STATUS: PASS** (science) **/ FLAG** (acronym expansion and section citation)
**FINDING:** The formula and both equivalent forms are correct and mutually consistent
(verified above), and the "perfect instrument = 100%" interpretation is right. Two metadata
errors: (1) the gem expands "K.D.C." as "knowledge/detection/comparison," but the chapter
(§26.1.4.1) defines it as the **Kinetic Definition Chart** apparatus ("kinetic" from the
motorization, per the source); (2) the Source line cites "§26.2.x" — the section is
§26.1.4 (pp. 26-8 to 26-10 is correct).

---

## TABLES

### Table 26.1 — Resolving power of hand-held camera lenses
**STATUS: PASS** (spot-checked) **with one QUERY**
**FINDING:** Spot-checked values are internally consistent: all readings fall on the chart
pattern values (80, 68, 56, 48, 40, 34, 28, 24, 20, 17, 14, 12, 7, 5), the aperture trends
are physically sensible (e.g., lens A: 68 lp/mm at f/2, 80 at f/4–f/11, 56 at f/16–f/22 —
consistent with aberration-limited wide-open, diffraction-limited mid-aperture, and
diffraction falloff stopped down), and field falloff is plausible for the lesser lenses
(B, E). QUERY: row F (values 4.8–5.6 lp/mm, no EFL/F-number) does not fall on any chart
pattern value and is far below every other lens; its identity (reference/control instrument,
or a mis-transcription) cannot be determined from the transcription. Scan check recommended.

### Figure 26.4 table — NBS chart pattern dimensions
**STATUS: FLAG**
**FINDING:** One value is wrong: the "Width of single black or white line" for pattern 56
is transcribed as **0.233 mm; it should be 0.223 mm.** Verified two independent ways:
(i) at the standard 25× minification the chart line width is 25/(2N) mm, giving
25/112 = 0.2232 mm for N = 56 (every other entry in both columns matches this rule
exactly: 80→0.156, 40→0.312, 28→0.446, 20→0.625, 14→0.893; 68→0.184, 48→0.260,
34→0.368, 24→0.521, 17→0.735, 12→1.042 — all exact); (ii) the 3-line pattern width for
56 is transcribed as 1.116 mm = 5 × 0.2232 ✓, whereas 5 × 0.233 = 1.165 ✗. The 0.233 is
almost certainly a 2↔3 digit misread. All other table values (3-line widths, inter-pattern
spaces, line lengths) checked consistent, including the low-contrast column's uniform
0.633× space-to-pattern-width ratio.

---

## SUMMARY

**STATUS: PASS**
**FINDING:** The chapter accurately covers its scope (resolving-power targets and methods,
KDC apparatus, sine-wave testing — Schade/Lamberts/Herriott — square-wave testing with
Coltman conversion, automatic ophthalmic lensometry) with nothing major missing. The
Schade-era history (Schade 1948, Duffieux, Selwyn, O'Neill, Coltman 1954, Herriott 1947/1958)
is correctly attributed. All five gem claims (26.1–26.5) survive contact with the new text.

---

## OVERALL ASSESSMENT

Confidence in ch26's scientific accuracy: **high**. Independently verified all 12 equation
items as PASS (with two substantiative notes: the δ-normalization question in Eq. (8), and
the exact Coltman-inversion coefficients beyond r(7n), where the r(9n) term vanishes — the
transcription's ellipsis is safe but must not be continued with a naive alternating sign
pattern). One table FLAG: the NBS pattern-56 line width 0.233 → 0.223 mm (proved two ways).
Two QUERYs: the "contrast … 1.4" figure (§26.1.2.1) — as a reflectance-based contrast it
cannot exceed 1, so it must be a log-contrast/density value (1.4 ≈ D of printed black;
0.20 ≈ D of grey; consistent with the Figure 26.5 axis spanning 0–1.5) or a 1.0 typo —
the definition should be stated wherever it is quoted; and the identity of Table 26.1's
row F (4.8–5.6 lp/mm). One gem metadata FLAG: 26.5's acronym expansion should be "Kinetic
Definition Chart," not "knowledge/detection/comparison." Nothing in the chapter now
conflicts with any gem's stated formula; all four previously-PASSed gems (26.1–26.4) and
26.5 remain valid on the rewritten text. Spot-check requests from the brief: 10⁻⁵ rad
Foucault slope and λ/2 fringe spacing verified in ch25; the 1000×NA and 0.61λ/NA figures do
not appear anywhere in ch25/ch26 (they belong to the microscope chapters) — nothing to
verify here.

---

## RECONCILIATION (2026-09-13, against docs/scans/ch26.pdf)

1. **Eq. (12) Coltman inverse, r(9n)=0 caution:** ACCEPTED. The printed leading coefficients
   match the scan exactly and the ellipsis is safe as printed — no change to `ch26.md`.
   Added the r(9n)=0 caution (and negative r(13n)/r(15n)/r(17n) terms) to gem 26.4 so future
   use of the series doesn't extend it with a naive alternating pattern.
2. **Gem 26.5 KDC acronym/citation:** ACCEPTED. Scan confirms §26.1.4 "The Kinetic Definition
   Chart" and §26.1.4.2's "derives the word 'kinetic' from the motorization of some of its
   parts." Fixed the acronym expansion and the source citation (§26.2.x → §26.1.4) in
   `analysis/LOST_GEMS_CATALOG.md`.
3. **NBS chart pattern-56 width, 0.233 → 0.223:** the scan prints **.233**, matching the
   existing transcription exactly (verified at 300dpi crop of ch26 p.3) — not a
   transcription error. REJECTED as a silent correction; ACCEPTED the underlying arithmetic
   finding (25/(2·56) = 0.2232, and the table's own 3-line-width entry 1.116 = 5×0.2232, not
   5×0.233) as a genuine likely-typo *in the 1962 source*. Added an editorial note in
   `ocr_output/ch26.md` documenting the inconsistency and the probable correct value, without
   rewriting the printed .233.
4. **"Contrast of black on white is 1.4":** scan confirms as printed. ACCEPTED the physical
   reasoning (can't be a bounded reflectance ratio) as a genuine ambiguity in the source's
   own convention; added an editorial note in `ocr_output/ch26.md` and to gem 26.3 rather
   than guessing which of density/log-contrast/typo it is.
5. **Table 26.1 row F identity:** scan confirms the row exactly as transcribed (blank
   EFL/F-number, values 5.6/4.8, no chart-pattern-value match) — genuinely unresolvable from
   the source. Added an editorial note in `ocr_output/ch26.md` documenting the anomaly.
6. **Eq. (8) δ-normalization query:** REJECTED — scan confirms `cos(2πn·x/δ)` exactly as
   transcribed; no ambiguity in the transcription itself. No change needed; noted here only
   for the audit trail.
7. **Eq. (4) "equation (3)" stale cross-reference:** REJECTED as an error to fix — scan
   confirms the 1962 source itself prints "equation (3)" as the in-text reference to the
   display tagged (4). A genuine typo in the original, already faithfully transcribed;
   cosmetic, no action.

Net: 2 accepted as source-level corrections needing editorial notes (NBS .233, row F), 1
accepted as a gem metadata fix (KDC), 1 accepted as a verified caution added to a gem
(Coltman r(9n)=0), 1 accepted as a genuine convention ambiguity flagged (contrast 1.4), and
2 rejected as non-issues after scan comparison (Eq. 8 δ, Eq. 4 cross-reference — both already
correct/faithful as transcribed).
