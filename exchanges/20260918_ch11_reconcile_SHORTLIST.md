# ch11 Reconciliation — Bucket B Shortlist (human decision needed)

Reconciling Devin's independent validation (`exchanges/20260918_ch11_validate_response.md`)
against the primary deep pass. **Bucket A note:** the three items Devin flagged as
mechanical transcription corruption — Table 11.3 row 25 (glass-pair duplication),
Table 11.9's truncated last-column row, and a stray `</file` tag on page 19 — are
already correct/absent in the current `ocr_output/ch11.md` (verified against git
history: fixed in commits `0fd9d81`/`78272a8` before the deep pass ran). Devin
appears to have validated an earlier snapshot. No Bucket A edits were needed.

Everything below was a judgment call. **Batch closed out 2026-09-18** on human approval:
each item carries a **Disposition** line. Tier 2 catalog edits were applied only after an
independent second re-derivation (Claude, agreeing with Devin).

---

Bucket B: §11.4.3.4 inequality "(P̃*_c − P̃*_a) should be less than (P̃*_b − P̃*_a)" | Devin says: scan-verified verbatim but physically inconsistent with the φ_a/φ_c ratio derived one line earlier; the needed condition is (P̃*_c − P̃*_b) < (P̃*_b − P̃*_a) — looks like a 1962 source typo, not a transcription error | scan/context: confirmed at 600 dpi, transcription is faithful to the printed page | Options: [preserve-as-printed+sic-note / apply-corrected / unresolved]

**Disposition: sic-preserved.** Printed text unchanged in `ocr_output/ch11.md`; inline editorial note added after §11.4.3.4 giving the derived condition (P̃*_c − P̃*_b) < (P̃*_b − P̃*_a) and noting the printed form also fails for the Fig. 11.10 glasses. No catalog reference existed (gem 11.6 does not use the inequality).

Bucket B: Table 11.14 (reversed PKS-1-front triplet) curvatures don't recombine to an f′=10 achromat | Devin says: element powers under standard indices give Σφ≈0.30 and Σφ/ν≈+0.005≠0; no plausible index/spacing fix works — likely a misprinted curvature in the source itself | scan/context: transcription is verbatim-correct; this is a Table 11.13-vs-11.14 pair (front-reversed triplet), so the mismatch may also hint at an index mislabel rather than a curvature typo — undetermined which | Options: [preserve-as-printed+sic-note / apply-corrected / unresolved]

**Disposition: sic-preserved.** Table unchanged; editorial note added below Table 11.14. Independent paraxial trace: Table 11.13 gives system power ≈0.100, Σφ/ν≈0 (consistent), Table 11.14 gives ≈0.29 and Σφ/ν≈+0.005 (inconsistent). Curvature misprint vs. index mislabel remains undetermined.

Bucket B: §11.3.2.5 coefficients b_3=−0.0014, b_5=0.000619 unreproducible | Devin says: could not reproduce the Table 11.6 D-light curve under raw-Y1, Y1/1.4-normalized, or tan U′ bases; the fit basis is defined in ch08's Eq 8-(1), not in ch11 | scan/context: not resolvable without cross-checking ch08 — outside ch11 scope | Options: [preserve-as-printed+sic-note / apply-corrected / unresolved — recommend deferring until ch08 is deep-passed]

**Disposition: deferred to ch08 deep pass.** b₃/b₅ left as printed; the fit basis is defined in ch08 Eq 8-(1).

**Update 2026-09-20 (ch08 validation):** resolved. Eq 8-(1) in raw $Y_1$ reproduces b₀=0 and b₅ (0.000622 vs 0.000619) but not b₃ (fit −0.001144, Table 11.8 route −0.00115). Verdict: source erratum, probable dropped digit for −0.00114. Printed value preserved; sic note added in `ocr_output/ch11.md`. See `exchanges/20260920_ch08_reconcile_SHORTLIST.md`.

Bucket B: §11.4.2 heading/body uses P̃ (no star) while Eqs 16–22 use P̃*/P̃** | Devin says: light QUERY — probably the book's own way of distinguishing F−D vs. λ−D partial dispersions, not an OCR error | scan/context: not independently checked beyond Devin's note | Options: [preserve-as-printed+sic-note / apply-corrected / unresolved]

**Disposition: resolved (annotate-only).** One-line editorial note added at §11.4.2: unstarred P̃ vs starred P̃*/P̃** is the book's own notation distinction, not an OCR error. Printed text unchanged.

Bucket B: Gem 11.1 (Fraunhofer orientation, crown in front) | Devin says: the orientation rule itself is chapter-supported (§11.2.2.3), but the stated off-axis/chief-ray-AOI mechanism is not the book's own reasoning (book cites axial-ray passage), and the "1.5–2× field" figure is not confirmable from the chapter or a standard reference | scan/context: no independent check performed beyond Devin's | Options: [apply-corrected (reword mechanism to match source, drop/hedge the 1.5–2× figure) / preserve-as-printed+sic-note / unresolved]

**Disposition: applied (Tier 2, independently confirmed).** §11.2.2.3/§11.2.3.1 cite axial-ray passage only; mechanism reworded, "1.5–2× field" and chief-ray/AOI claims removed. Title changed from "preferred for off-axis" accordingly.

Bucket B: Gem 11.2 (Petzval scaling, objective contribution ∝ 1/MP²) | Devin says: scaling exponent is wrong — Eq (3)'s bracket gives objective:eyepiece = γ_e/(γ_o·MP), i.e. 1/MP suppression, not 1/MP²; at MP=10 objective contributes ~10% not ~1%; "100× smaller at MP=10" should read ~10×; the "P_obj ≤ 0.5·P_eye acceptable at MP≥3" quick-check is also unsupported by the chapter | scan/context: Devin's re-derivation from Eq (3) is shown in the validation file and looks consistent with Table 11.1 numbers already confirmed elsewhere in the same report | Options: [apply-corrected (this looks like a genuine exponent error, not a style choice) / unresolved]

**Disposition: applied (Tier 2, independently confirmed).** Exponent corrected to 1/MP (objective:eyepiece = γ_e/(γ_o·|MP|)); confirmed by reproducing Table 11.1 (108′/87′/79′). "100×" → ~10×, ~10% at MP=10; unsupported "P_obj ≤ 0.5·P_eye at MP≥3" quick-check dropped; sign note added.

Bucket B: Gem 11.3 (zonal tolerance, L_marginal symbol gloss + worked example) | Devin says: formula matches the source exactly, but the gem misdefines L_marginal as "focus shift of marginal ray relative to paraxial" when the book defines L_{k−1} as the optical direction cosine of the emerging ray (≈sin U′≈1/(2·f/#)); the worked example is wrong — at f/10, L≈0.05 gives 4.6·0.55µm/0.05≈50µm≈0.05mm, not the gem's 0.01mm | scan/context: ch11.md main text already carries the correct L_{k-1} definition (line 493/507) so this is purely a catalog-wording/arithmetic issue | Options: [apply-corrected (fix definition + recompute example) / unresolved]

**Disposition: applied (Tier 2, independently confirmed).** L_{k-1} redefined as the emerging ray's direction cosine (≈1/(2·f/#)); f/10 example recomputed to ≈0.05 mm; the book's own 19.4 µm example added.

Bucket B: Gem 11.4 (air-spacing to reduce zonal aberration, quantified claims) | Devin says: mechanism matches §11.3.4.3 verbatim, but no "3–5×" reduction figure appears in the chapter, and Table 11.9's airspaces span 0.4–7.4% of focal length — wider than the gem's stated "typically 1–3%" | scan/context: no independent check beyond Devin's Table 11.9 read | Options: [apply-corrected (widen/drop the % range, hedge or drop the 3–5× figure) / preserve-as-printed+sic-note / unresolved]

**Disposition: applied (Tier 2, independently confirmed).** "3–5×" removed (book says only "remarkable degree"); air-space range replaced by Table 11.9's actual span (≈0 to 7.4% of f′, scan re-checked; note a few rows print ≈0 or slightly negative t₂, and t₂ tracks Δν).

Bucket B: Gem 11.5 (secondary-spectrum threshold, intermediate derivation) | Devin says: headline numbers (0.038λ, 65.8cm, 131.6cm, 7.9cm) are correct and scan-verified, but the gem's intermediate step "OPD ≈ (f′/2200)·(1/(2×16.7)) ≈ f′/73,480" actually computes transverse aberration Y_k, not OPD; correct chain is Y_k=f′/(4400·f/#) → OPD=Y_k·Y_1/(2f′)=f′/(17,600·f/#²)≈f′/4.9×10⁶ | scan/context: Devin shows the corrected chain reproduces the same final ~65.8cm answer, so this is a derivation-clarity fix, not a result change | Options: [apply-corrected (fix intermediate step only, final numbers unchanged) / unresolved]

**Disposition: applied (Tier 1).** Intermediate step rewritten (Y_k = f′/(4400·F), OPD = f′/(17,600·F²) ≈ f′/4.9×10⁶). Final numbers unchanged. Note: the earlier chain did not actually reproduce 65.8 cm; the closed form gives ≈67 cm at λ=0.55 µm, consistent with the book's 65.8 (which uses its ray-traced Y_k=0.00015 cm, λ=0.5893 µm).

Bucket B: Gem 11.6 (Herzberger P*/P** collinearity, wording of conditions) | Devin says: core substance confirmed, but three wording problems: (a) "area of the triangle ∝ 1/Δ" is garbled — element powers ∝1/Δ, triangle area ∝Δ; (b) gem reuses "Δ" for the Eq(21)/(22) numerator determinant when the book's Δ (Eq 20) is a different determinant det[P̃*,ν,1] controlling secondary correction — should be distinguished; (c) "any three normal glasses can be combined as an apochromat in principle" is misleading since collinear glasses on the P*–ν line make Δ→0 (singular, infinite element powers) | scan/context: no independent check beyond Devin's re-derivation, which matches the PASS items elsewhere in the same report (Eqs 17–22) | Options: [apply-corrected (three wording fixes, no formula/number change) / unresolved]

**Disposition: applied (Tier 1).** (a) powers ∝1/Δ, area ∝Δ; (b) Eq 20 Δ = det[P̃*,ν,1] distinguished from the Eq 21/22 numerator determinant (renamed D_λ); (c) "any three normal glasses" restricted to non-collinear triples (Δ→0 on the normal line). Beyond the brief's letter: the gem's headline ("primary and secondary corrected iff collinear on P̃*–P̃**") was also reworded, since per Eqs 15–16 and 22 that collinearity governs the residual at a further wavelength, not F/D/C correction. No formulas changed.

---

**Not shortlisted (resolved, no action):** the unbarred-y question in §11.1.3.4's denominator — Devin confirmed unbarred y is correct and matches Eq (1); no change needed.
