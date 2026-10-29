# Validation Response — Chapter 20: Applications of Thin Film Coatings

**Date:** 2026-09-12
**Validator:** Claude (Sonnet 5), self-validated per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`

---

### 20.1 — Reflectance table
**STATUS: FLAG (one row), PASS (rest)**
Recomputed all six rows from R=((n-1)/(n+1))²: n=1.51→4.13% (stated 4.12% ✓ rounding); n=1.58→5.05% (✓ exact); **n=1.70→6.72%, but the table stated 6.44%** — does not reproduce from the given n; n=2.40→16.96%≈17% ✓; n=3.50→30.86%≈30.9% (stated 30.7%, close, rounding); n=4.05→36.44% ✓ exact. The 5-element/10-surface transmission estimate T≈(0.9588)^10=0.656≈0.65 checks out using the stated 4.12% figure. **Corrected the n=1.70 row to 6.72% in the catalog.**

### 20.2 — Ideal AR index / MgF₂ residual
**STATUS: PASS**
√1.51=1.229≈1.23 ✓. Recomputed R_min for MgF₂ (n=1.38) on n=1.51 glass using R=[(n₀n_s-n_f²)/(n₀n_s+n_f²)]²: n_f²=1.9044, (1.51-1.9044)/(1.51+1.9044)=-0.1155, squared=1.33% — close to the stated ~1.2% (small difference consistent with using n_s≈1.52 or a slightly different MgF₂ index; order of magnitude and conclusion unaffected).

### 20.3 — Beam splitter rules
**STATUS: PASS**
Standard, well-documented rule of thumb for uncoated metal (silver) 50/50 beam splitters vs. lossless dielectric multilayer beam splitters. Polarization-splitting caveat (R_s≠R_p at 45°) is correct and important, standard Fresnel behavior away from normal incidence.

### 20.4 — Material reference table
**STATUS: PASS**
Index values and transparency ranges for MgF₂, ZnS, TiO₂, ZrO₂, CeO₂, Ge, Si, PbTe, cryolite/chiolite, ThF₄, NaCl, SiO are all consistent with standard thin-film material references. The SiO index-vs-O₂-pressure sensitivity note is a well-known real practical issue in evaporated SiO films.

### 20.5 — Film cracking thickness limit
**STATUS: PASS**
Tensile-stress cracking in evaporated MgF₂/CeO₂ films above ~1µm and compressive-stress ZnS being more tolerant is standard thin-film deposition knowledge. QWOT-at-10µm arithmetic for MgF₂ checked: 10/(4×1.38)=1.812µm ✓ matches stated 1.81µm, correctly exceeding the 1µm cracking limit.

### 20.6 — Absentee layer
**STATUS: PASS**
Standard result (characteristic matrix of a half-wave layer = identity). Checked the g-value claim: a QWOT layer (optical thickness λ₀/4) is absentee when λ₀/4 = mλ/2, i.e. g=λ₀/λ=2m → g=2,4,6,... ✓ correctly derived.

### 20.7 — QHQ broadband AR
**STATUS: PASS**
Standard, well-documented classical broadband AR structure (quarter-half-quarter); the qualitative behavior (better broadband performance than single-layer MgF₂, at the cost of overshoot outside the design band) matches established thin-film coating theory (Hass-era broadband AR designs).

### 20.8 — Quarter-wave stack HR zone width
**STATUS: FLAG (IR rows), PASS (visible rows)**
Recomputed Δg=(2/π)arcsin|(n_H-n_L)/(n_H+n_L)| for all four pairs:
- ZnS/MgF₂ (2.30/1.38): 0.161 ✓ exact match
- TiO₂/MgF₂ (2.40/1.38): 0.174 (stated 0.170, close, rounding)
- **Ge/ZnS (4.05/2.30): 0.178, not 0.273 as stated** (full zone 36%, not 55%)
- **Ge/cryolite (4.05/1.35): 0.333, not 0.434 as stated** (full zone 67%, not 87%)

The two high-index-ratio (IR) rows are both off by roughly the same proportion, suggesting a systematic transcription/calculation slip rather than two independent errors. **Corrected both rows in the catalog.** The formula itself, and the design conclusions drawn from it (width depends on ratio not absolute index; more periods increase peak R but not width), are all correct.

### 20.9 — Overcoated Al mirror reflectivity
**STATUS: PASS**
Figures consistent with well-known dielectric-overcoat mirror performance (Jenkins 1958 data on ZnS/MgF₂-overcoated Al is a real historical reference). Multi-bounce arithmetic checked: 0.90⁴=0.656≈66% ✓, 0.90⁸=0.430≈43% ✓, 0.995⁴=0.980≈98% ✓, 0.995⁸=0.961≈96% ✓ — all exact.

### 20.10 — Fabry-Perot tilt/convergent beam behavior
**STATUS: PASS**
Blue-shift with tilt (shorter effective optical path at oblique incidence) and asymmetric pass-band broadening in a convergent beam are both standard, well-documented FP interference-filter behavior; the cited Lissberger & Wilcock (1959) reference is a real, appropriate citation for convergent-beam filter design.

---

## Overall Assessment

This is the most quantitative chapter validated so far, and two genuine, independently-verifiable numeric errors were found and corrected (one reflectance-table entry in 20.1, two HR-stack bandwidth entries in 20.8) — both are internal arithmetic slips, not physics errors; the underlying formulas, all confirmed standard and correct, were applied inconsistently to those specific rows. Everything else — AR coating theory, beam-splitter rules, material reference data, absentee-layer principle, mirror overcoat performance, FP filter behavior — checks out cleanly against standard thin-film optics.
