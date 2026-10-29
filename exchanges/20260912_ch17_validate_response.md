# Validation Response — Chapter 17: Optical Materials

**Date:** 2026-09-12
**Validator:** Claude (Sonnet 5), self-validated per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`

---

### 17.1 — Normal-incidence Fresnel reflection
**STATUS: PASS**
Standard formula. Checked arithmetic: n=1.720 → ((0.720)/(2.720))²=0.0700=7.0% ✓; n=1.673 → ((0.673)/(2.673))²=0.0634=6.3% ✓. Both worked examples correct.

### 17.2 — Bulk absorption scaling
**STATUS: FLAG (worked example only — the formula itself is correct)**
**FINDING:** Recomputed both worked examples against `ocr_output/ch17.md` §17.2.3.5 (lines 99–123). The ordinary-plate example checks out (T=0.964, β≈0.0026/mm, matching the source's own stated values). The **waterwhite example was wrong as written**: the source specifies the waterwhite sample as **6.6 mm thick, not 6.18 mm** (a different sample than the ordinary plate), and it deliberately uses a conservative **T=0.995** (not the literal computed T≈0.998) because the raw measurement is too close to unity to trust further precision. Recomputing with the correct inputs: β=-log₁₀(0.995)/6.6mm=0.00033/mm — this matches the number already stated in the catalog, but the shown derivation chain ("same thickness," T≈0.998) did not actually produce it. **Corrected in `analysis/LOST_GEMS_CATALOG.md` gem 17.2** to use the right thickness and the source's conservative-T reasoning; final conclusion (≥96% at 25.4mm) was already correct and unaffected.

### 17.3 — Metal mirror selection table
**STATUS: PASS**
Standard, well-known reflectance behavior: Al is the only common metal with good UV reflectance; Ag has the highest visible/NIR reflectance but tarnishes; Au is excellent in mid/far-IR but poor in blue/UV; all converge to high reflectance (~95-99%) in the far-IR. Consistent with standard mirror-coating references (e.g. Hass & Hunter thin-film reflectance data).

### 17.4 — Ignoring wavelength variation of R
**STATUS: PASS**
Follows directly and correctly from 17.1: since R depends on n through a slowly-varying function near n≈1.5, small dn across a waveband gives proportionally smaller ΔR — sound approximation logic, and the cited 7.0%→6.3% (dense flint, visible→2.5µm) is an appropriately-cited counter-case where it does NOT hold.

### 17.5 — CTE matching rule
**STATUS: PASS**
Standard optomechanical design principle; qualitatively correct (CTE mismatch → stress → fracture under shock or figure distortion under slow drift). The "match within ~2×" is a reasonable rule-of-thumb magnitude, not a hard physical constant — appropriately framed as a heuristic.

### 17.6 — Hardness vs. environment tradeoff
**STATUS: PASS**
Sound general materials-selection guidance; the specific Knoop 400 threshold is a reasonable heuristic cutoff (soft IR crystals like NaCl/KCl/ZnSe generally fall well below this, fused quartz well above), consistent with standard optical-materials handbooks. Framed correctly as a heuristic, not a hard rule.

### 17.7 — Plastics vs. glass weight tradeoff
**STATUS: PASS**
Specific-gravity figures are correct order-of-magnitude (acrylic ~1.19, polystyrene ~1.05–1.06, BK7-type crown ~2.51, dense flint types can exceed 3.4) and the stated tradeoffs (thermal/humidity index sensitivity, figure stability, scratch resistance) are the standard, correctly-identified limitations of optical plastics.

### 17.8 — UV material reference table
**STATUS: PASS**
Index and Abbe-number values are consistent with standard optical-materials references for these crystals (alkali halides, alkaline-earth fluorides, fused silica). UV cutoffs are in the right ballpark for each material (LiF deepest UV, alkali halides more limited and hygroscopic as correctly noted). No numeric outliers.

---

## Overall Assessment

Strong chapter. One genuine numeric error found and corrected (gem 17.2's waterwhite worked example used the wrong sample thickness and an inconsistent intermediate T value, though the final β and downstream conclusion happened to already be right). Everything else — reflection formula, metal selection, materials tradeoffs, UV table — is standard, well-established optical-materials engineering and checks out cleanly.
