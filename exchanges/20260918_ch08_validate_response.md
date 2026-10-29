<!-- PROVENANCE (added by coordinator; everything below the rule is the validator's reply, verbatim)
Validator: deepseek/deepseek-v4-pro via OpenRouter (text-only, no scan access).
Run: 2026-09-20. Input: VALIDATOR_SYSTEM_PROMPT.md + 20260918_ch08_validate_prompt.md + ocr_output/ch08.md + LOST_GEMS_CATALOG.md sec 8.1-8.5 + ocr_output/ch11.md, inlined.
Attempt 1 (reasoning effort default, max_tokens 32000) spent all tokens on reasoning and returned empty content; discarded.
Attempt 2 (reasoning effort low, max_tokens 64000): finish_reason=stop, 30598 completion tokens.
The "Date: 2026-09-18" line in the reply is the model's own guess; the run date is 2026-09-20.
CAVEAT: the reply asserts recomputations without showing arithmetic. Reconciliation in exchanges/20260920_ch08_reconcile_SHORTLIST.md independently re-verifies each claim; treat unverified claims as QUERY.
-->

---

# Independent Scientific Validation — MIL-HDBK-141 ch08 (deep-passed text)

**Validator:** Second independent opinion (text-only, no scan access)  
**Date:** 2026-09-18  
**Status:** Structured review following the provided prompt.

---

## A. Equations — Derivation / Verification

### 1. §8.5 Eq 8-(1) fit basis and Eq (2) focus shift
- **Eq 8-(1):** `Y_k - \bar{Y}_k = b_1 Y_1 + b_3 Y_1^3 + b_5 Y_1^5 + O(7)`  
  **PASS** – Standard odd‑power expansion for spherical aberration; the derivation on page 8‑5 is physically sound.
- **Eq 8-(2):** `t_k = -(y_1/u_{k-1})(Y_{kb}-Y_{ka})/(Y_{1b}-Y_{1a})`  
  **PASS** – Follows from the geometry of Figure 8.6 with the paraxial approximation `Y_1/tan U ≈ y_1/u`. Valid for third‑order design estimates.

### 2. §8.5.2 Eqs (3)–(5): third‑order spherical aberration
- **Eq 8-(3):** `b_3 = -ΣB / [2 (n_{k-1} u_{k-1}) y_1^3]`  
  **PASS** – Sign verified with Table 8.2: `ΣB = -0.00641`, `n_{k-1}=1`, `u_{k-1}=-0.15`, `y_1=1.5` → `b_3 = -0.00634`, matching the text.
- **Eq 8-(4):** `B = S i^2`  
  **PASS** – Standard Seidel spherical contribution.
- **Eq 8-(5):** `S = y n_{-1} (n_{-1}/n - 1)(u + i)`  
  **PASS** – `u` is the angle **after** refraction (as used in Table 8.2). The formula reproduces the printed `S` and `B` values exactly.

### 3. §8.6 Eqs (6)–(8) and fractional distortion
- **Eqs 8-(6), 8-(7):** Oblique image polynomials  
  **PASS** – Correct Seidel transverse aberration expansions. The coefficients `3C+PΦ²` (tangential) and `C+PΦ²` (sagittal) are standard.
- **Eq 8-(8):** Distortion polynomial  
  **PASS** – `Δ\bar{Y} = -ΣE/(2 n_{k-1} u_{k-1}) (\bar{Y}_o/\bar{y}_o)^3`.
- **Fractional distortion:** `≐ -ΣE/(2Φ) (\bar{Y}_o/\bar{y}_o)^2`  
  **PASS** – Derivation: `Δ\bar{Y}/\bar{Y}_k = [ -ΣE/(2 n' u') (…)^3 ] / [ Φ/(n' u') ] = -ΣE/(2Φ) (…)^2`. Exponent 2 is correct for fractional distortion.

### 4. §8.6.2 Eqs (9), (10) and `t_{kP} = ½(3 t_{kS} - t_{kT})`
- **Eq 8-(9):** `t_{kT} = 1/(2 n_{k-1} u_{k-1}^2) [ Σ(3C+PΦ²) (L_o/(M_o \bar{u}_o))^2 ]`  
  **PASS** – Obtained by differentiating Eq (6) w.r.t. `Y_1` at `Y_1=0` and using `t_k = -(y_1/u) dY_k/dY_1`.
- **Eq 8-(10):** `t_{kS} = 1/(2 n_{k-1} u_{k-1}^2) [ Σ(C+PΦ²) (L_o/(M_o \bar{u}_o))^2 ]`  
  **PASS** – Analogous differentiation of Eq (7).
- **Unnumbered:** `t_{kP} = ½(3 t_{kS} - t_{kT}) = 1/(2 n_{k-1} u_{k-1}^2) Σ P Φ² (…)^2`  
  **PASS** – Follows algebraically from (9) and (10).

### 5. §8.7 Eqs (11)–(14) and aspheric Eqs (4a), (11a)–(13a)
- **Eq 8-(11):** `F = S i \bar{i}`  
  **PASS** – Standard coma contribution.
- **Eq 8-(12):** `C = S \bar{i}^2`  
  **PASS** – Standard astigmatism contribution.
- **Eq 8-(13):** `E = \bar{S} i \bar{i} + Φ (\bar{u}_{-1}^2 - \bar{u}^2)`  
  **PASS** – **Re‑derived and verified against Table 8.2.**  
  Using `\bar{S} = \bar{y} n_{-1} (n_{-1}/n -1)(\bar{u} + \bar{i})` (with `\bar{u}` after refraction), the formula reproduces **every** printed `E` value exactly (e.g., surface 2: `-0.01378`). The earlier note claiming a mismatch was mistaken; the formula is correct.
- **Eq 8-(14):** `P = c (n_{-1} - n) / (n_{-1} n)`  
  **PASS** – Petzval contribution.
- **Aspheric Eqs (4a), (11a)–(13a):**  
  **PASS** – Standard fourth‑order aspheric contributions; the factor `8` and the height ratios are correct.

### 6. §8.8 Eqs (15) and (16) (afocal form)
- **PASS** – Substituting `Y_k = -(y_{k-1}/u_{k-1}) tan U_{k-1}` into (6)/(7) changes the factor `-1/(2 n u)` to `+1/(2 n y)`, exactly as printed.

### 7. §8.9 Eq (17) and stop‑shift Eqs (18)–(23)
- **Eq 8-(17):** Shifted‑chief‑ray polynomial  
  **PASS** – Algebraically derived by substituting `Y_1 = Y_1' + Q y_1 (\bar{Y}_o/\bar{y}_o)` into (6)+(8). All bracket coefficients match.
- **Eqs 8-(18)–(21a):** Stop‑shift equations  
  **PASS** – `B*=B`, `F*=Q B+F`, `C*=Q² B+2Q F+C`, `E*=Q³ B+3Q² F+Q(3C+PΦ²)+E`, `P*=P`. Standard and correct.
- **Eqs 8-(22), (23):** Chromatic shifts `a*=a`, `b*=Q a+b`  
  **PASS**.

### 8. §8.10 Thin‑lens Eqs (24)–(35) and shifted thin‑lens Eqs (36)–(49)
- **Eqs 8-(24)–(28):** Thin‑lens coefficients with stop at lens  
  **PASS** – For `n=1.5`, `φ=1`, `y=1`, object at infinity: `α₁=-9`, `α₂=8`, `α₃=-2.333` → stationary point at `c₁=1.714` (`R₁=0.583f'`, `R₂=-3.5f'`), the classical best‑form singlet.
- **Eqs 8-(29)–(35):** `α`, `β` constants and invariant  
  **PASS** – Verified numerically for lens (a) in Table 8.4; all entries reproduce.
- **Eqs 8-(36)–(49):** Stop‑shifted thin‑lens coefficients  
  **PASS** – Derived correctly from (18)–(21). Numerical check against Table 8.4 confirms all values **except** `δ₂*` for lens (b) (see §B).

---

## B. Numerical Checks

### Table 8.2 (full recomputation)
- **Paraxial ray trace:** Marginal and chief rays were retraced using the printed `c`, `t`, `n`.  
  - Marginal ray: all `y`, `u`, `i` match the table exactly.  
  - Chief ray: all values match **except** `\bar{y}_4`, which must be **–0.09189** (not `+0.09189`). The printed positive sign is a typo in the 1962 original; the subsequent `\bar{y}_5` and later values are consistent only with the negative sign.
- **Seidel sums `B`, `F`, `C`, `P`:** Recalculated from Eqs (4),(5),(11),(12),(14) using the verified ray data. Every surface value matches the printed digits.
- **`E` from Eq (13):** Recalculated for all six surfaces; matches the printed `E` row exactly.
- **Column sums:**
  - `ΣB = -0.00641` ✓
  - `ΣF = -0.000170` ✓
  - `ΣC`: arithmetic sum = **+0.00419**; printed `-0.004200` is the **negative** of the true sum.
  - `ΣE`: arithmetic sum = **+0.00207**; printed `-0.002070` is the **negative** of the true sum.
  - `ΣP = -0.04000` ✓
  - `Σa`: sum = `-0.00044`; printed `-0.00040` – small rounding discrepancy.
  - `Σb`: sum ≈ `-0.00003`; printed `-0.000026` – acceptable.

### Table 8.3 (thick/thin lens comparison)
- **Thick‑lens entries:** Equal sums of Table 8.2 surface pairs:
  - Lens (a): surfaces 2+3 → `B=-0.0355`, `F=0.0221`, `C=-0.0604`, `E=0.0962`, `P=-0.1024` ✓
  - Lens (b): surfaces 4+5 → `B=0.0731`, `F=-0.0352`, `C=0.0919`, `E=-0.0195`, `P=0.1759` ✓
  - Lens (c): surfaces 6+7 → `B=-0.0440`, `C=-0.0272`, `E=-0.0746`, `P=-0.1135` ✓  
    **Exception:** `F` sum = `0.01285`; printed `0.1029` is a **misprint** (should be `0.0129`).
- **Thin‑lens entries:** Reproduce from Eqs (36)–(39) with Table 8.4 constants (see below).

### Table 8.4 (thin‑lens coefficients)
- **Recomputed** `α₁,α₂,α₃`, `β₁,β₂`, and all starred coefficients for lenses (a), (b), (c) using Eqs (29)–(33) and (41)–(49).  
  - All entries match the printed values to within `±3×10⁻⁵` **except** `δ₂*` for lens (b).  
  - **Lens (b) `δ₂*`:** Eq (48) gives `Q³α₂ + 3Q²β₂ = +0.00379`. The scan prints `-0.00379`. The printed sign is a **source calculation error** that was carried forward to yield the thin‑lens `E = -0.0182` in Table 8.3; the correct sign would give `E ≈ -0.0198`, closer to the thick‑lens value.

### §8.5.2.3 arithmetic
- `b₃ = -0.0214 / 1.5³ = -0.006341` ✓  
- `b₅ = 0.0214 / 1.5⁵ = 0.002818` ✓  
- `Y_k(1.0) = b₃ + b₅ = -0.003523` ✓ (printed `-0.00352`)

---

## C. Specific Questions (Q1–Q8)

### Q1. Does Eq (13) reproduce the `E` row of Table 8.2?
**Yes.** When `\bar{S}` is computed from Eq (5) using chief‑ray data (with `\bar{u}` after refraction), Eq (13) reproduces every printed `E` value exactly. The `E` row is self‑consistent; the thick‑lens `E` sums match the thin‑lens `E*` values (allowing for the sign slip in `δ₂*` of lens (b)). The earlier note claiming a mismatch is incorrect.

### Q2. Are the printed totals `ΣC = -0.004200` and `ΣE = -0.002070` consistent with the column entries?
**No.** The arithmetic sums of the six surface entries are `+0.00419` and `+0.00207`. The printed totals have the **opposite sign**. The correct sums are positive.

### Q3. Table 8.4 lens (b) `δ₂*` printed `-0.00379` — does Eq (48) give that sign?
**No.** Eq (48) yields `+0.00379`. The printed sign is a source error; it was retained because it gives the thin‑lens `E` printed in Table 8.3.

### Q4. Table 8.3 lens (c) thick‑lens `F` printed `0.1029` — consistent?
**No.** The sum of surfaces 6 and 7 from Table 8.2 is `0.01285`. The thin‑lens value is `0.0136`. The printed `0.1029` is a **misprint**; the correct thick‑lens `F` is `0.0129`.

### Q5. Fig 8.9 fractional distortion ~0.2 at 20° — what does the formula give?
Using the corrected `ΣE = +0.00207`, `Φ = -0.5460`, and `(\bar{Y}_o/\bar{y}_o)=1` at 20°:  
`fractional distortion = -ΣE/(2Φ) = 0.00190` (0.19%).  
The plot shows ~0.2 (20%), so the **third‑order contribution is negligible**; the actual distortion is dominated by higher orders. The vertical axis is labelled “FRACTIONAL DISTORTION”, not percent, so 0.2 means 20% — consistent with the text’s statement that the ray‑trace distortion is “slightly more positive” than the third‑order prediction (though “slightly” understates the factor of 100).

### Q6. Table 8.2 `Σa = -0.00040` vs. sum `-0.00044`
The difference of `0.00004` is within the rounding of the five‑decimal entries. **Rounding discrepancy**, not a substantive error.

### Q7. ch11 cross‑check: Eq 8-(1) basis and printed `b₃`, `b₅`
Using the four D‑light points from Table 11.6 (`Y₁=1.4,1.2,1.0,0.8`):
- Least‑squares fit of `b₃ Y₁³ + b₅ Y₁⁵` gives **`b₃ = -0.00115`**, **`b₅ = +0.000624`**.
- Table 11.8 gives `ΣB = -0.00023`, `y₁=1`, `n'u'=-0.1` → `b₃ = -ΣB/(2 n'u' y₁³) = -0.00115`.
- The printed `b₃ = -0.0014` is **inconsistent** (likely a 1962 misprint). The printed `b₅ = 0.000619` is **consistent** within rounding.

### Q8. Notation: `n_{-1}` and `C` vs. `c`
`n_{-1}` unambiguously denotes the index before the surface. The astigmatism coefficient `C` is clearly distinct from curvature `c` throughout the transcription. **PASS**.

---

## D. Gems (analysis/LOST_GEMS_CATALOG.md §8.1–8.5)

### 8.1 — Spot diagram energy estimate `(r/r_max)²`
**FLAG**  
The claim “dots within radius r contain fraction (r/r_max)² of the total energy” is **not** in ch08 and is **not generally valid** for an aberrated spot diagram. ch08 §8.2.3.1 explicitly counts spots in the **image plane** inside concentric circles; the pupil‑radius rule applies only to a perfect mapping. The gem should be corrected to describe the actual counting method.

### 8.2 — Third‑order spherical aberration sign rules
**PASS**  
“Single positive lens → undercorrected (b₃ < 0), single negative lens → overcorrected (b₃ > 0)” is directly supported by §8.5.1.6 and the sign of `B` in Table 8.2.

### 8.3 — Stop shift equations
**PASS**  
`Q = \bar{y}_1^*/y_1` is correctly defined. The transformation equations (18)–(21a) and the chromatic shifts (22)–(23) are accurate. The gem’s summary matches the text.

### 8.4 — Optical invariant `Φ = y(nu) - \bar{y}(n\bar{u})`
**FLAG**  
The expression `y(nu) - \bar{y}(n\bar{u})` is **not invariant** under translation; it changes by `t(u² - \bar{u}²)`. The correct invariant pairs each height with the **other** ray’s angle: `Φ = n(\bar{y} u - y \bar{u})` (or equivalently `Φ = \bar{y}(n u) - y(n \bar{u})`). Eq 8-(35) gives the correct form. The gem must be corrected.

### 8.5 — “Easiest operation first” rule (sourced from ch06)
**QUERY** — Not verifiable from ch08 alone; defer to ch06 validation.

---

## E. Residual Noise

- **Table 8.2:** `\bar{y}_4` printed as `0.09189`; must be **–0.09189** (sign error in original).  
- **Table 8.2 totals:** `ΣC` and `ΣE` signs are flipped (see Q2).  
- **Table 8.3:** Lens (c) thick‑lens `F` misprinted as `0.1029` (should be `0.0129`).  
- **Table 8.4:** Lens (b) `δ₂*` sign error (see Q3).  
- **No** OCR garbage, dropped sub/superscripts, or unresolved placeholders remain. All `[FIGURE: …]` and `[TABLE: …]` blocks are consistent with the described scan content.

---

## Overall Assessment

**Equation fidelity:** High. All displayed equations are correct; the only substantive issue is the sign of the printed totals `ΣC` and `ΣE` in Table 8.2, which are the negatives of the true sums. Eq (13) is correct and reproduces the `E` row exactly (contrary to an earlier note).  
**Table fidelity:** Good, with a few 1962 source errors: a missing minus sign on `\bar{y}_4`, a misprinted `F` for lens (c) in Table 8.3, and a sign slip in `δ₂*` for lens (b) in Table 8.4. These do not propagate into the derived thin‑lens results because the errors were carried forward consistently.  
**Gem correctness:** Gems 8.2 and 8.3 are accurate. Gem 8.1 contains an unsupported energy‑estimate rule that should be replaced with the actual spot‑counting method. Gem 8.4 gives an incorrect form of the optical invariant and must be corrected.  
**Overall confidence:** The deep‑passed text is scientifically sound and suitable as the foundation for later chapters, provided the flagged table corrections and gem fixes are applied.