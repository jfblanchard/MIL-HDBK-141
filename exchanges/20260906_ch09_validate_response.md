# Chapter 9 — Scientific Validation Response

**Validator:** Devin (second opinion, independent of primary VLM pass)
**Date:** 2026-09-06
**Chapter:** 9 — Method of Lens Design (12 pages; page 12 blank)
**Inputs:** `exchanges/20260828_ch09_validate_prompt.md`; `ocr_output/ch09.md`; standing role prompt

Method: cross-checked each equation and claim against first principles and standard
references (Hecht, Smith, Kingslake, Born & Wolf, Conrady). Chapter 9 is a procedural
summary chapter; most equations are restatements of chs. 5/6/8, which I re-derived or
verified algebraically rather than taking on faith.

---

## EQUATIONS

```
ITEM: A1 — Differential aberration equations (1)–(7)
STATUS: PASS
FINDING: Structure correct. Monochromatic Seidel coefficients (B, F, C, E, P) depend on
c, t, n but NOT on dispersion, so the absence of a ∂/∂ν term in (1)–(5) is physically
correct; ν (Abbe number) enters only the chromatic coefficients a, b through the δn/n
terms (dispersion ~ 1/ν). The sums are analytic (polynomial/rational) functions of c, t,
n away from ray-trace singularities, so local linearization is valid; the book itself
notes nonlinearity and the need for iteration (9.2.4.8), which is the correct caveat.
Two minor caveats: (i) n and ν are not truly independent for real glasses (glass
manufacture couples them), so the ∂/∂ν term models selecting a different glass, not an
independent perturbation — the book is aware of this (9.2.4.9); (ii) the j=1..k-1 index
matches the k-1 thicknesses; curvature/media indexing is a book convention, not an error.
```

```
ITEM: A2 — 0.01% perturbation for differential coefficients
STATUS: PASS
FINDING: A 0.01% relative perturbation is a reasonable forward-difference step for
analytic Seidel sums: small enough to stay in the (locally linear) regime, large enough
to avoid subtractive-cancellation roundoff. Tradeoffs are as expected: too small →
roundoff dominates the difference f(c+h)−f(c); too large → O(h) truncation error and
nonlinearity. Edge case not stated in the chapter: if a parameter is exactly zero (e.g. a
plane surface with c = 0), "0.01% of its initial value" is zero → Δc = 0 → division by
zero in ∂ΣB/∂c. Practically one perturbs by 0.01% of a characteristic scale or skips
zero surfaces; worth an editorial note but not a physics error.
```

```
ITEM: A3 — Diffraction parameter Z; first dark ring at Z = 3.83
STATUS: PASS
FINDING: With a = Y_e (pupil radius) and sinθ = d/(2ℓ'), the definition gives
Z = πY_e d/(λℓ') = 2πa sinθ/λ, which is exactly the argument of J₁(z) in the circular
aperture diffraction amplitude I ∝ [2J₁(z)/z]². The first dark ring is the first zero of
J₁ at z = 3.8317 ≈ 3.83, consistent. Z is the standard dimensionless diffraction
parameter.
```

```
ITEM: A4 — Airy disk diameter d = 1.22λℓ'/Y_e
STATUS: PASS
FINDING: At the first dark ring (Z = 3.8317), d = 2ℓ'sinθ = 3.8317λℓ'/(πY_e) =
1.2197λℓ'/Y_e ≈ 1.22λℓ'/Y_e. 3.83/π = 1.219... ≈ 1.22 confirmed. With ℓ'/Y_e = 2(f/#)
(see C4), d = 2.44λ(f/#). Correct standard Airy disk formula.
```

```
ITEM: A5 — Combined spot Z_{G+D} = √(Z_G² + Z_D²)
STATUS: PASS
FINDING: Valid as an engineering approximation, not an exact result. Quadrature (RMS)
combination of independent geometrical and diffraction blur is a commonly used estimate
(essentially identical to the "combined spot size" used in detector sizing / MTF
budgets). It is meaningful in the aberration-dominated (Z_G ≫ Z_D) and diffraction-limited
(Z_D ≫ Z_G) limits and a reasonable interpolation between them; it is not a rigorous
convolution of the two distributions. The chapter correctly frames it as an estimate
("One can then estimate..."), so this is a sound heuristic, not an overreach.
```

```
ITEM: B1 — Paraxial ray trace: 5-(56), 5-(57), 6-(3), 6-(4), 6-(6)
STATUS: PASS
FINDING: 5-(56) is the transfer equation in reduced coordinates ((t₋₁/n₋₁)(n₋₁u₋₁) = t₋₁u₋₁,
correct); the "alternate" 5-(56) is the same equation written plainly (benign duplicate
numbering). 5-(57): n u = n₋₁u₋₁ + y(n₋₁−n)c matches the standard refraction
n'u' = nu − y(n'−n)c with n'=n, n=n₋₁. 6-(3)/6-(4): u = u₋₁ + i(n₋₁/n − 1) with i = yc + u₋₁;
substituting i and multiplying by n reproduces 5-(57) exactly (verified algebraically), so
the two forms are equivalent refraction formulas. 6-(6): Φ = ȳ(nu) − y(nū) = n(ȳu − yū) is
the Lagrange (optical) invariant, and the pre/post-surface equality holds because the
quantity is invariant across refraction (nu and nū transform together). All correct.
```

```
ITEM: B2 — Chromatic contributions a (6-(34)) and b (6-(35))
STATUS: PASS
FINDING: a = −yn₋₁i(δn'/n' − δn/n) is the standard axial-chromatic surface contribution
using axial-ray height y and axial incidence i. b = −yn₋₁ī(δn'/n' − δn/n) is the lateral
(transverse) color contribution and correctly uses axial-ray height y with CHIEF-ray
incidence ī. This is the right pairing, not ȳ. Verification: for a thin lens with the
stop at the lens, the formula gives b = 0 (the two surface contributions cancel because
n·ī₂ = ī₁), matching the known result that a thin lens at the stop has zero lateral
color; using ȳ (chief height) instead would force zero for ALL thin lenses regardless of
stop position, which is wrong. So the use of y (not ȳ) is correct.
```

```
ITEM: B3 — Distortion E = S̄iī + Φ(ū₋₁² − ū²)
STATUS: PASS
FINDING: Correct standard (Conrady-style) distortion surface contribution, with
S̄ = ȳn₋₁(n₋₁/n − 1)(ū + ī). Two independent confirmations: (a) thin lens with the stop at
the lens gives S̄ = 0 at both surfaces and the Φ pupil terms cancel, yielding total
E = 0 — physically correct (thin lens at the stop has zero distortion); (b) Φ here is the
system Lagrange invariant (matching 6-(6)), and the identification Φ²ΣP = Petzval sum
SIV is verified (see B4), so the pupil term has the right invariant and magnitude. Φ is
the correct quantity; no separate Φ̄ is needed. The absolute sign of the (ū₋₁² − ū²)
pupil term follows the book's sign convention; structure, invariant, and magnitude are
all consistent with the verified stop-shift equation. (B, F, C, P = S i², S iī, S ī²,
c(n₋₁−n)/(n₋₁n) in the same convention are all verified standard forms.)
```

```
ITEM: B4 — Stop shift ΣE* = Q³ΣB + 3Q²ΣF + QΣ(3C + PΦ²) + ΣE
STATUS: PASS
FINDING: Matches the standard stop-shift SV* = Q³SI + 3Q²SII + Q(3SIII + SIV) + SV exactly
(and the companion B, F, C, P equations match SI*, SII*, SIII*, SIV*). The identification
is confirmed: book P = c(n₋₁−n)/(n₋₁n) = c·δ(1/n), and SIV = H²Σc·δ(1/n) = Φ²ΣP with
H = Φ the invariant. Since Φ is a system constant, QΣ(3C + PΦ²) = Q(3ΣC + Φ²ΣP) — the two
written forms are equivalent. Correct.
```

```
ITEM: Aspheric contributions 8-(4a)–(13a)
STATUS: PASS
FINDING: B = 8(n₋₁−n)e·y⁴ is the standard 4th-order aspheric spherical contribution (the
factor 8 and the (n'−n) index-difference dependence are the well-known result; the sign
reflects this book's convention, consistent with the other formulas). F = B·(ȳ/y),
C = B·(ȳ/y)², E = B·(ȳ/y)³ are the standard field-ratio relations for a pure 4th-order
aspheric profile (an asphere perturbs the aperture-like coefficient B and projects it to
the field orders via ȳ/y). Correct.
```

---

## GEMS

```
ITEM: Gem 9.1 — 9-step iterative design procedure
STATUS: PASS
FINDING: The 9-step sequence and the pre-computer two-part decomposition (correct a, b,
P, E by adjusting focal lengths/spacings; correct B, F, C by bending) are faithful to the
chapter and scientifically sound. The claim that step 1 (lens type selection) is the
"most creative" and experience-heavy part is consistent with the text. Caveat folded in
from C1: the associated phrase "bending affects B, F, C only" is precise for thick lenses
only (see C1).
```

```
ITEM: C1 — Bending affects B, F, C; not a, b, P (thin lens)
STATUS: FLAG
FINDING: For a STRICT thin lens, bending changes only B (SI, spherical) and F (SII, coma);
C (SIII, astigmatism, = −φΦ² in this convention) and P (SIV) are shape-INVARIANT (they
depend only on power and conjugates/stop, not on the shape factor). So the book's
"bending affects primarily B, F, and C" is only an approximation, appropriate for THICK
lenses (where changing c₁, c₂ at fixed φ moves principal planes and internal conjugates,
so C does shift a bit). As written — and as repeated in the chapter summary and Gem 9.1
("affects B, F, C only") — it overstates the thin-lens case. Suggest qualifying: "for a
thin lens bending affects B and F; for a thick lens it affects B, F, and (to a lesser
extent) C, a, b, P." Not a hard physics error for real (thick) designs, but worth a
clarity note so it isn't applied to thin-lens theory.
```

```
ITEM: Gem 9.2 — Standard ray tracing plan; 0.7 ≈ 1/√2
STATUS: PASS
FINDING: Ray-count arithmetic correct: 3 axial + (3 fields × 5 meridional) + (3 fields ×
4 skew) = 3 + 15 + 12 = 30 rays in D light; ×3 for D/F/C ≈ 90. The justification that
0.7 ≈ 1/√2 samples the half-area (≈ half-energy) radius of a uniform circular pupil is
physically sound (encircled area fraction = (r/R)², = ½ at r/R = 1/√2 ≈ 0.707).
```

```
ITEM: C2 — All aberrations zero → stop position irrelevant
STATUS: PASS
FINDING: Correct. With B = F = C = E = P = 0, the stop-shift equations give
B* = F* = C* = E* = P* = 0 for any Q. Physical meaning as stated is correct: a lens
corrected for all third-order (and chromatic) aberrations shows no third-order
degradation from moving the stop. Note this holds at third order only; higher-order
terms (and vignetting/pupil aberrations) still depend on stop position, which the chapter
does not overclaim.
```

```
ITEM: Gem 9.3 — Standard plot scale 0.01 cm = 100 microns
STATUS: FLAG
FINDING: The core unit conversions are trivially correct: 0.01 cm = 100 μm, and for
inches 0.004 in × 25400 μm/in = 101.6 μm ≈ 100 μm. HOWEVER, the transcription/Gem phrasing
"1 cm on the graph = 100 microns" is arithmetically wrong (1 cm = 10,000 μm = 10 mm). The
intended standard is one 0.01 cm division = 100 μm (i.e. the whole ±0.01 strip ≈ ±100 μm,
or 100 μm per division). Flag for correction: it should read "one 0.01 cm division = 100
microns" (and, for inches, "0.004 in ≈ 100 microns"), not "1 cm = 100 microns."
```

```
ITEM: Gem 9.4 — Diffraction limit, Airy disk, combined spot
STATUS: PASS
FINDING: Z normalization and d_Airy = 1.22λℓ'/Y_e = 2.44λ(f/#) verified (see A3, A4, C4).
Worked example correct: λ = 0.5 μm, f/4 → d = 2.44 × 0.5 × 4 = 4.88 ≈ 4.9 μm. Quadrature
combination valid as an estimate (see A5). Figure 9.2 figure-spec claim that the first
dark ring (Z = 3.83) encloses ≈ 84% energy is correct (standard circular-aperture value
is 0.838). The "universal reference overlay" guidance is sound.
```

```
ITEM: C4 — Airy disk = 2.44λ(f/#)
STATUS: PASS
FINDING: For an object at infinity, ℓ' ≈ f' and the exit pupil radius Y_e ≈ aperture
radius, so f/# = f'/(2Y_e) and ℓ'/Y_e = f'/Y_e = 2(f/#). Then d = 1.22λ · 2(f/#) = 2.44λ(f/#).
Standard result; the ℓ' ≈ f' (exit pupil ≈ aperture for a focused-at-infinity system)
approximation is the intended one.
```

---

## SUMMARY

```
ITEM: Chapter summary (OCR §9.1–9.3)
STATUS: PASS
FINDING: Accurately represents a procedural chapter: the 9-step iterative workflow, the
differential aberration equations (1)–(7), bending, the standard ray-trace plan, plot
scale, diffraction/Airy/combined-spot material, OTF/MTF introduction, and the §9.3
cross-chapter equation summary. Correctly identifies it as a synthesis chapter with few
new equations. Two minor issues: (i) it repeats the "bending affects B, F, C" phrasing
(see C1), and (ii) it states "Tables: None," whereas §9.2.5.2 contains a small skew-ray
coordinate table (see Tables). Figure inventory (9.1–9.5) is correct.
```

---

## TABLES

```
ITEM: Skew-ray coordinate table (§9.2.5.2)
STATUS: PASS
FINDING: The four skew-ray coordinates per field — (X₁max, 0), (0.7X₁max, 0), (0.5X₁max, 0),
(X₁max, Y₁max) — are a sensible sampling of the assumed-circular entrance pupil (three
points along the X-diameter plus one at the upper corner/aperture edge), consistent with
the text's "3–4 skew rays per field." No suspicious values. (The chapter summary's
"Tables: None" undercounts this small table, which belongs in the inventory as a minor
corrective note.)
```

---

## Overall Assessment

High confidence in the chapter's scientific accuracy. Chapter 9 is a procedural summary
chapter with little new physics, and every equation I could check against first
principles or standard references — the differential aberration equations, the paraxial
transfer/refraction and Lagrange-invariant forms, the chromatic and Seidel surface
contributions, the aspheric relations, and the stop-shift equations — is correct,
including the subtle choices (ν appears only in chromatic terms; b uses axial height y
with chief incidence ī rather than ȳ; Φ in the distortion pupil term is the system
invariant, equivalent to the standard Φ²ΣP Petzval form). I found no hard physics errors.
Two wording/precision issues are worth correcting for the pocket edition: (1) the
"bending affects B, F, and C" claim is only valid for thick lenses — for a strict thin
lens C (astigmatism) is shape-invariant, so it should be "B and F" in the thin-lens
context; and (2) the plot-scale phrasing "1 cm = 100 microns" is arithmetically wrong and
should be "one 0.01 cm division = 100 microns" (0.004 in ≈ 100 μm for inch units). Minor
editorial caveats: n and ν are not independent variables for real glasses (the ∂/∂ν
terms represent glass selection), and the 0.01% perturbation rule degenerates for a
parameter that is exactly zero (division by zero). None of these undermine the chapter's
physics. Recommended disposition: ACCEPT with the two wording corrections flagged above.
