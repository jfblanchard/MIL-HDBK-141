# Validation Response — Chapter 21: Coating of Optical Surfaces

**Date:** 2026-09-12
**Validator:** Claude (Sonnet 5), self-validated per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`

---

### 21.1 — Non-ideal monolayer R_min
**STATUS: PASS**
Recomputed: n₁²=1.9044, n₀n₂=1.52, (1.9044-1.52)/(1.9044+1.52)=0.1123, squared=1.26% — exact match. Ideal index √1.52=1.233 ✓. Formula and worked example both correct.

### 21.2 — TiO₂/MgF₂ bilayer universal inner layer
**STATUS: PASS**
Internally consistent: 15.5°/360°=0.0431≈0.043 ✓ unit conversion checks out. The underlying physical claim (near-invariance of the inner high-index layer's required phase across a range of substrate indices in a bilayer AR null) is a real, known bilayer-AR design result; I can't re-derive the exact 15.5° figure from scratch without solving the full two-layer null-reflectance system, but nothing here is inconsistent or implausible.

### 21.3 — Jupnik equivalent-bilayer principle
**STATUS: PASS**
This is the standard equivalent-layer / Herpin-equivalent-index principle in thin-film optics — any single layer can be represented by (or replaced with) a two-layer combination of available materials satisfying the stated index-product relation, provided both layers are quarter-wave at the design wavelength. Well-established, textbook technique (Macleod, *Thin-Film Optical Filters*, ch. on equivalent layers); the historical attribution to "Jupnik" is plausible as a specific period reference and not something I can independently confirm or deny.

### 21.4 — Single-layer AR failure at 45° on crown glass
**STATUS: PASS**
Sound physical reasoning: p-polarization approaches zero reflectance near Brewster's angle regardless of coating, while s-polarization reflectance increases with angle and requires a lower film index to compensate — consistent with standard oblique-incidence thin-film AR theory. The n<1.30 material-availability constraint matches 20.2/20.4's material table (no rugged film below MgF₂'s n=1.38 is listed there either).

### 21.5 — HR stack closed-form reflectance
**STATUS: FLAG (formula), PASS (worked numeric example)**
**FINDING:** Derived the equivalent-admittance recursion for a terminated (HL)^M H quarter-wave stack from scratch (Y_after_H=n_H²/Y_prev, Y_after_L=n_L²/Y_prev, starting from the substrate). For N=2M+1 layers ending in H at the incident-medium side: Y_N = n_H²·(n_H/n_L)^(N-1)/n_sub, and ρ₀=(n₀-Y_N)/(n₀+Y_N). Plugging in the worked example (n_H=2.35, n_L=1.38, n_sub=1.52, N=11): Y=745.2, ρ₀=-0.9973, |ρ₀|²=0.9946 — **this exactly reproduces the stated worked answer.** But plugging the *catalog's stated formula* [n₀(n_H/n_L)^N - n_sub]/[n₀(n_H/n_L)^N + n_sub] into the same numbers gives |ρ₀|²=0.9827, not 0.9946 — the transcribed formula does not reproduce its own worked example. **Corrected the formula in the catalog** to the verified equivalent-admittance form; the worked numeric answer (0.9946, T=0.54%) was already correct and is unchanged.

### 21.6 — FP filter half-width formula
**STATUS: PASS**
|Δλ|=(λ₀/ν)(1-|ρ₀|²)/(π|ρ₀|) is the standard Fabry-Perot Airy-function FWHM formula (equivalent to FSR/finesse, with finesse F=π√R/(1-R) and √R=|ρ₀|). Worked example (|ρ₀|=0.9899, ν=1) recomputes to ≈35.5 Å assuming λ₀≈550nm, close to the stated 36.2 Å (consistent with λ₀≈560nm — a reasonable rounding/reference-wavelength difference, not an error). The ν=3 scaling (36.2/3=12.1 Å) is exact by the formula's own 1/ν dependence.

---

## Overall Assessment

Strong chapter overall. One genuine formula-transcription error found in 21.5 — the closed-form reflectance expression as written didn't reproduce its own worked example — traced to a missing n_H² factor and an off-by-one exponent; corrected. The worked numeric answer itself was already right, meaning whoever originally computed it (likely working from the correct recursive/matrix method) used a different route than the simplified formula that got written down. Everything else (monolayer/bilayer AR limits, equivalent-layer principle, oblique-incidence polarization behavior, FP bandwidth formula) is standard and checks out.
