# Validation Response — Chapter 25: Production Phase Optical Tests (deep-pass re-validation)

**Date:** 2026-09-13
**Validator:** Independent scientific validator (per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`)
**Input:** `ocr_output/ch25.md` (fresh deep-passed text, 36 pages), re-verified against
prior gem claims 25.1–25.8 (prompt 20260912 listed 25.1–25.6; catalog also contains 25.7, 25.8).

---

## EQUATIONS

### Eq. (1) — Distortion from nodal slide: D_β = (R−L)/2 · sec β
**STATUS: QUERY**
**FINDING:** The geometry checks out structurally: with the lens rotated ±β about the
nodal point and translated f(sec β − 1), a distortion-free lens images exactly onto the
microscope axis (R = L = 0), and a fractional distortion D shifts the image by f·sin β·D
laterally and f·tan β·D along the tilted focal plane. The formula as printed is therefore
dimensionally a **linear focal-plane displacement** (image-height error), not a dimensionless
fractional distortion: it equals the lateral reading (R−L)/2 projected onto the tilted focal
plane by sec β. If the intended quantity is the conventional fractional distortion
(y' − f·tan β)/(f·tan β), the correct form is D = (R−L)/(2f·sin β) = (R−L)·sec β/(2f·tan β).
The book calls it "the distortion, D" without defining the normalization, and the scan's
intended definition cannot be resolved from the transcription alone. Recommend a scan check
of the surrounding wording (Washer, Tayman & Darling, J. Res. NBS 61, 509 (1958)) to
determine whether D is defined as a linear or fractional quantity.

### Eq. (2) — Spherometer: r = d²/(6s) + s/2
**STATUS: PASS**
**FINDING:** Correct. For an equilateral 3-leg spherometer the circumradius of the leg
circle is a = d/√3, and the exact sphere relation R = (a² + s²)/(2s) = a²/(2s) + s/2 gives
R = d²/(6s) + s/2. Verified algebraically; the formula is exact for a true sphere (no
small-sagitta approximation needed), with d = average leg distance as stated.

### Eqs. (3), (4) — Newton's fringes: dark at d = νλ/2, bright at d = μλ/4 (μ odd)
**STATUS: PASS**
**FINDING:** Derived from first principles: reflection at the upper (glass→air) surface has
phase change 0, at the lower (air→glass) surface π, so the phase difference is 4πd/λ + π;
dark when d = νλ/2 (ν = 0,1,2,…), bright when d = μλ/4 (μ = 1,3,5,…). Matches Eqs. (3)–(4)
exactly, and is consistent with rules (e) (λ/2 between like fringes) and (f) (λ/4 bright-to-
dark). Prior gem 25.2's algebraic derivation (dark νλ/2 → bright (2ν+1)λ/4) remains valid
against the new text.
**Minor note:** §25.8.1.3's "a fringe shift h/5 corresponds to a change of separation, da,
by the amount 10" — the "10" should read **λ/10** (1/5 fringe × λ/2 per fringe); the λ symbol
was lost. The h/10 detection limit statement (λ/20) is consistent.

### Eqs. (5), (6) — Fizeau interferoscope plate case: nd = νλ/2, nd = μλ/4
**STATUS: PASS**
**FINDING:** Correct. For two beams reflected from the two faces of a plate of index n,
path difference 2nd plus π phase change at the air→glass face gives dark at nd = νλ/2 and
bright at nd = μλ/4 (μ odd). Verified.

### Eq. (7) — Δ = 2nd − λ/2 (phase difference, plate case)
**STATUS: PASS** (equation itself) — but see prose FLAG below (§25.8.2.2's "π/2").
**FINDING:** With dark fringes at nd = νλ/2, Δ = (ν − 1/2)λ (destructive ✓); with bright at
nd = μλ/4 (μ odd), Δ = (μ−1)λ/2 with (μ−1)/2 integer (constructive ✓). The equation is
correct; the surrounding prose explanation of the phase changes is not (see FLAG item).

### §25.8.2.3 worked example: α = 3.64×10⁻⁶ rad = 0.75 arcsec
**STATUS: PASS**
**FINDING:** Recomputed: (λ/2n)/diameter = 0.5461×10⁻³/(3×50) mm = 3.641×10⁻⁶ rad =
0.751 arcsec ✓. Fringe bookkeeping also consistent: nd increased by λ/2 moves μ → μ+2
(odd→odd ✓), and the mid-plate position satisfies eq. (5) (dark), giving "one dark and two
bright fringes" ✓. The 0.1-fringe scaling to 0.075 arcsec is linear ✓.

### Eqs. (8), (8a) — Twyman-Green: Δd = 2(n−1)Δt/λ; Δd = 2Δn·t/λ (wavelength numbers)
**STATUS: PASS**
**FINDING:** Optical path through plate = (n−1)t relative to air; variations (n−1)Δt and
t·Δn, doubled for double pass, divided by λ ✓. Correct.

### Eqs. (9), (10) — Ronchi shadow magnification
**STATUS: FLAG**
**FINDING:** The transcribed radial ratio √(η+ξ)/√(y+x) is missing the squares. It is
mathematically false except at unit magnification (for an undistorted shadow ξ = Mx,
η = My, the expression gives √M, not M). The correct relation, consistent with the
surrounding prose ("without distortion and with a constant magnification over its area"),
is **√(η²+ξ²)/√(y²+x²) = p/g** (equivalently ξ/x = η/y = p/g), and for the aberrated case
√(η²+ξ²)/√(y²+x²) = (p−S)/(g−S), where S is the longitudinal spherical aberration of the
ray through the point (verified by similar triangles with the displaced center of
projection at B). The (p−S)/(g−S) structure of Eq. (10) is right; only the missing
superscripts need restoring. Most likely a dropped-superscript transcription error; please
verify against the scan (after Martin, Technical Optics).

### Eq. (11) + W(u,v) — Linfoot Foucault illumination integral
**STATUS: PASS**
**FINDING:** Structure is the standard result: the field in the knife-edge plane is the
Fourier transform of the pupil illumination E(x,y) (u = 2πx₁/λs, v = 2πy₁/λs ✓), and the
observed distribution is the inverse transform of the truncated (knife-edge) field. The
half-range u-integral (0 → ∞) is consistent with the knife edge occluding half the pupil.
Sign conventions are Fourier-convention dependent and not errors. i = √−1 ✓. (Exact printed
limits cannot be independently confirmed without the scan; no physical problem found.)

### C′ = 2πC/λs (normalized knife-edge displacement)
**STATUS: PASS**
**FINDING:** Consistent with the u, v scaling. Minor wording note: C′ is dimensionless
(a phase-like normalized displacement), so calling it "the distance moved in the plane of
the image of the knife edge" is loose — C′ is that distance in units of λs/2π.

### Pulfrich refractometer: n_s = √(n_p² − sin² i_r)
**STATUS: PASS**
**FINDING:** Derived: grazing incidence in the sample (n_s·sin 90° = n_p·sin θ_c), side-face
emergence (n_p·cos θ_c = sin i_r) → n_s² = n_p² − sin² i_r ✓. Correct.

### §25.10.1.4 Foucault sensitivity example numbers
**STATUS: FLAG**
**FINDING:** The transcribed pair "deflection is 10⁻⁴ inches or .025 mm" is internally
inconsistent: 10⁻⁴ in = 0.00254 mm, not 0.025 mm (factor of 10). Using the correct
Δx = 2θR (θ = 10⁻⁵): R = 10 in gives 2×10⁻⁴ in = 0.0051 mm; R = 10 cm gives 2×10⁻³ mm ≈
10⁻⁴ in; R = 5 in (i.e., a 10-inch-diameter surface) gives exactly 10⁻⁴ in = 0.00254 mm.
The most probable reconstruction of the original is "…deflection is 10⁻⁴ inches or .0025 mm"
(a dropped zero in the mm value; consistent with R = 5 in / 10-in diameter with the factor
2θ, or with R = 10 in if the source itself dropped the factor 2 — the prose explicitly
states the 2θ rule, so the first reading is preferred). The gem 25.4 formula Δx = R·2θ is
unaffected and correct; only this worked example needs a scan re-check and correction.
(Also note the "10⁻⁷ rad" benchmark = 0.0206 arcsec, correctly converted in the gem.)

### PROSE FLAG — phase change on reflection stated as π/2 (two places)
**STATUS: FLAG**
**FINDING:** §25.8.2.2 states "the phase change on reflection will be π/2 at surface S1,
and 0 at surface S11, so that the difference in the phase changes on reflection is π/2",
and §25.8.1.11 refers to phase changes "that differ from … 2/2 (as in the reflection from
an air-to-glass interface)" (garbled π). Both are wrong: for dielectrics the phase change
is **0** at glass→air and **π** at air→glass (Fresnel coefficient sign), a difference of
**π** = λ/2 — which is exactly what the book's own Eq. (7) (Δ = 2nd − λ/2) and Eqs. (5)–(6)
use. The two "π/2" occurrences (one cleanly transcribed, one OCR-garbled "2/2") should read
π. This may be a faithful transcription of a typo in the 1962 source; the equations are
correct either way, so only the prose needs the fix.

---

## GEMS

### 25.1 — Focal length reference-point ambiguity
**STATUS: PASS**
**FINDING:** Both failure anecdotes and the EFL/BFL/FFL/reference-surface prescription are
consistent with the new text (§25.2.1) and remain standard, correct optomechanical
practice. No conflicts introduced by the deep pass.

### 25.2 — Newton's fringes 7-rule guide
**STATUS: PASS**
**FINDING:** All seven rules now match transcribed Eqs. (3)–(4) exactly (dark νλ/2, bright
odd μλ/4), and rule (g) follows from (e)+(f) as previously derived: dark at νλ/2 plus λ/4
bright-to-dark spacing gives μ = 2ν+1 = 1, 3, 5, … ✓. Rule (d) (pressure moves fringes
outward on a convex area, maintaining constant d) is the standard interpretation ✓.

### 25.3 — Interferometric flatness specification levels
**STATUS: PASS**
**FINDING:** Fringes/inch, h/N straightness fractions (h/5 detectable, h/10 practical
limit), and "uniform color" all match §25.8.1.3–25.8.1.5 and remain standard shop language.
Consistent with the λ/2-per-fringe height rule of Eqs. (3)/(4).

### 25.4 — Foucault test sensitivity, Δx = R·2θ
**STATUS: PASS** (with the chapter-text example flagged above)
**FINDING:** Δx = R·2θ is correct (slope error θ doubles on reflection; displacement grows
linearly with R). The 10⁻⁵ rad ≈ 2 arcsec and 10⁻⁷ rad ≈ 0.02 arcsec conversions are
correct, and the sensitivity claims are consistent with the test's documented performance.
The gem does not carry the inconsistent worked-example numbers, so the gem itself stands;
the fix belongs in the chapter text (§25.10.1.4).

### 25.5 — Star test zonal interpretation
**STATUS: PASS**
**FINDING:** Bright ring inside focus = short-focusing (positive) zone; outside = long
(negative) — matches §25.11.6.4 and the ray fans of Figure 25.33. Standard, correct
(consistent with Suiter and Taylor). Out-of-focus multi-ring examination is correctly
recommended as the more sensitive technique.

### 25.6 — Coma vs. symmetric aberrations and boresight error
**STATUS: PASS**
**FINDING:** Correct: coma's asymmetric flare displaces the image centroid (systematic
boresight bias), while spherical and (principal-ray-centered) astigmatism blur symmetrically
and can be centered on. §25.4.1 supports the gem exactly. Also consistent with §25.11.5.3's
note that astigmatism can still enlarge the spot several hundred percent for pointing.

### 25.7 — Spherometer r = d²/(6s) + s/2
**STATUS: PASS**
**FINDING:** Equation matches transcribed Eq. (2) and is verified correct. Minor wording
nit: the caveat says "s ≪ d is assumed (small-sagitta approximation is exact for a true
sphere, not approximate)" — the formula is exact for a true sphere at any s; the
parenthetical is self-contradictory but harmless. No scientific error.

### 25.8 — Nodal-slide distortion D_β = (R−L)/2 · sec β
**STATUS: QUERY**
**FINDING:** The formula matches transcribed Eq. (1), and the procedure (symmetric ±β
rotation, self-referencing) is a real, sound technique — but the equation is dimensionally
a linear image-height error, not a fractional distortion, and the chapter does not define
the normalization. If the gem is to be used for quantitative distortion values, it should
state the quantity's units (linear mm in the focal plane) or supply the fractional form
D = (R−L)/(2f·sin β). See Eq. (1) entry above.

---

## SUMMARY

**STATUS: PASS**
**FINDING:** The chapter accurately represents its scope (focal length, Hartmann, coma,
astigmatism/field curvature, distortion, radii/index measurement, contact and Fizeau
interferometry, Twyman-Green, Ronchi, Foucault, star test). No major topic is missing.
The scientific content is overwhelmingly sound; the flagged items are localized (missing
superscripts in the two Ronchi equations, the inconsistent Foucault example, the π/2 phase-
change prose, the λ/10 dropped symbol).

---

## OVERALL ASSESSMENT

Confidence in ch25's scientific accuracy: **high**, with four localized corrections needed.
Independently verified 12 of 16 equation items as PASS (spherometer, Newton's-fringe
conditions in both air-gap and plate forms, the phase-difference equation, the wedge-angle
worked example, both Twyman-Green variations, the Linfoot integral, the normalized
knife-edge displacement, the Pulfrich relation, the λ/2 and λ/4 spacing rules), FLAGged 3
(the Ronchi magnification equations missing the squares; the internally inconsistent
Foucault worked-example numbers, most likely a dropped zero making ".0025 mm" → ".025 mm";
the two "π/2" phase-change prose statements that should be π), and QUERYed 1 (the
dimensionality/normalization of the nodal-slide distortion formula). All 8 gem claims
(25.1–25.8) survive contact with the new text: 7 PASS, 1 QUERY (25.8, inherited from
Eq. (1)). No gem now conflicts with a deep-passed equation. The most important corrections
for the record: Eq. (9)/(10) need η², ξ², y², x² restored; §25.10.1.4's ".025 mm" needs a
scan re-check (likely ".0025 mm"); §25.8.2.2 and §25.8.1.11 "π/2" → π.

---

## RECONCILIATION (2026-09-13, against docs/scans/ch25.pdf)

All four items were checked directly against the scan; the scan is the arbiter per house
convention, and it settled every one differently than the speculative fix above:

1. **Eq. (9)/(10), missing η²/ξ²/y²/x²:** REJECTED as a transcription fix. The scan itself
   prints the radicands with no exponents (verified at 250dpi crop of ch25 p.20) — this is
   the 1962 source, not an OCR loss. Preserved as-printed (sic) in `ocr_output/ch25.md` with
   an editorial note giving the physically consistent form. Devin's physics critique of the
   equation is correct; it just applies to the book, not the transcription.
2. **§25.10.1.4 ".025 mm":** the speculative ".0025 mm" rewrite was REJECTED — the scan
   prints "10⁻⁴ inches or .025 mm" exactly as transcribed, internally inconsistent by ~10×
   in the source itself. Preserved as-printed with an editorial note. Separately, while
   re-checking this passage we found the entire §25.10.1.1–25.10.2.1 span had been left as
   raw uncleaned Tesseract OCR (not deep-passed as the chapter commit claimed) — cleaned it
   up, which also surfaced that the "sensitivity" benchmark is **10⁻⁶ radians**, not the
   10⁻⁷ this response's summary and the (then-corrupted) transcription both had — scan
   confirms 10⁻⁶. Fixed in `ocr_output/ch25.md` and gem 25.4.
3. **§25.8.2.2 / §25.8.1.11 "π/2" → π:** REJECTED — the scan prints **λ/2**, not π/2, at
   both locations. It was never a phase-in-radians statement; the book states the phase
   change directly in path-length units (a π phase shift ≡ λ/2 optical path), which is
   correct as physics. The "π/2" this validation reasoned about was an OCR misread of λ
   (rendered as "r", "7", or "»" in the raw scan text) that had not yet been cleaned up.
   Fixed the λ misread in `ocr_output/ch25.md`; no equation or physics was ever wrong here.
4. **Eq. (1) nodal-slide distortion, dimensionality QUERY:** ACCEPTED as genuinely
   unresolvable from the scan — added an editorial note in `ocr_output/ch25.md` and to
   gem 25.8 documenting the ambiguity (linear vs. fractional distortion) rather than
   guessing a normalization.

Net: 0 of the 4 flagged items required an equation/value to be silently rewritten; 1 was a
confirmed source-level anomaly worth an editorial note (Foucault example), 1 was a confirmed
likely-source-typo needing only a note (none here — see ch26 for that pattern), 2 were OCR
misreadings (λ, and an uncleaned raw-OCR section) now fixed, and 1 remains a genuine
unresolved ambiguity in the 1962 text. Also corrected in passing: gem 25.4's 10⁻⁷ rad → 10⁻⁶
rad (confirmed against the scan).
