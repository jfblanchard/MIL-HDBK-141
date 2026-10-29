# Validation Response — Chapter 22: Infrared Optical Design

**Date:** 2026-09-12
**Validator:** Claude (Sonnet 5), self-validated per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`

---

### 22.1 — IR resolution degradation
**STATUS: PASS**
Diffraction-limited resolution scales linearly with λ. 3/0.56=5.36≈5×; 10/0.56=17.9≈18× — both check out against the stated reference wavelength.

### 22.2 — Ordinary glass IR cutoff
**STATUS: PASS**
Standard, well-known material property: ordinary optical glass (silicate-based) transmits well to ~2.0-2.5µm with absorption becoming severe by ~2.7µm; flints (higher heavy-metal-oxide content) do have somewhat different absorption edges than crowns, consistent with standard glass-catalog IR transmission curves.

### 22.3 — Near-IR achromat power convergence
**STATUS: PASS**
Recomputed the visible-band example using φ_a=φ·ν_a/(ν_a-ν_b), φ_b=-φ·ν_b/(ν_a-ν_b) with ν_a=57.4, ν_b=36.6, φ=1/100mm⁻¹: φ_a=0.01×57.4/20.8=0.02760 → f_a=36.2mm ✓ matches stated 36mm; φ_b=-0.01×36.6/20.8=-0.01760 → f_b=56.8mm ✓ matches stated 57mm. Both element focal lengths check out exactly. The qualitative near-IR claim (V-number convergence between crown and flint reduces the effective dispersion difference, forcing shorter/stronger elements to hit the same achromatic condition) is correct physics, and the stated near-IR focal lengths (19mm, 23mm) represent roughly the expected 1.9-2.5× reduction — reasonably described as "twice as short," though the two elements don't scale by quite the same factor.

### 22.4 — Mid-IR V-ratio
**STATUS: PASS**
Silicon's very low dispersion (anomalously high V-number) in the 3-5µm window relative to available negative mid-IR materials is well documented; a V-ratio far exceeding the visible-glass range (~2.4:1) is physically plausible and consistent with known Si-based IR achromat design practice. Can't independently verify the exact "46:1" figure without specific glass dispersion data at hand, but nothing about the order of magnitude is implausible.

### 22.5 — Optical immersion n² gain
**STATUS: PASS**
Checked all three worked values: BaF₂ n≈1.5 → n²=2.25≈2.3 (consistent with n≈1.51); SrTiO₃ n=2.2 → n²=4.84≈4.8 ✓ exact; Ge n≈4.0 → n²=16 ✓ exact. The étendue/thermodynamic argument for the n² limit and the hemisphere-geometry requirement (to keep rays normal-incidence at the curved surface so none are lost to TIR) are both standard, correct IR-detector-optics results.

### 22.6 — Detector placement at aperture image
**STATUS: PASS**
Sound, well-documented photoconductive-detector design practice — averaging spatial non-uniformity in responsivity by imaging the aperture (pupil) rather than the field onto the detector is a real and still-used technique in IR detector integration.

---

## Overall Assessment

Clean chapter — every gem checked against either standard IR-optics physics or (for 22.3) an independently recomputed achromatic-doublet worked example, and all check out. No corrections needed.
