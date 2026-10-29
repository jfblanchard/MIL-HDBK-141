# ch08 Reconciliation (2026-09-20)

Validator: DeepSeek v4 Pro via OpenRouter, text-only (`exchanges/20260918_ch08_validate_response.md`).

**Independence caveat.** The validator's reply asserts recomputations without showing arithmetic, and it
read the primary agent's `[NOTE]` blocks (they are inline in `ch08.md`), so parts of its reply echo those notes.
Every claim below was therefore re-derived by the coordinator (a Python retrace of Table 8.2 from c, t, n;
fits of the Table 11.5/11.6/11.7 data; Eq 36-39/48 arithmetic; scan re-read of ch08 p.8 and ch11 p.9).

## Verdicts

| Item | Validator | Coordinator re-check | Result |
|---|---|---|---|
| Eq 8-(13) reproduces Table 8.2 E row (Q1) | Yes | **Yes**, with $\Phi=\bar y u-y\bar u=-0.5460$ (Eq 35). All six E values match to the printed digits. With $+0.5460$ it does not. | Primary's earlier note was WRONG (used wrong $\Phi$). Fixed (Bucket A). |
| b₃ = −0.0014 (Q7) | Not reproducible; likely misprint | LSQ fit −0.001144, b₅ 0.000622; Table 11.8 route −0.00115. Printed constants fit none of Tables 11.5/11.6/11.7. Scan re-read: −0.0014 is printed. | **Source erratum** (probable dropped digit, −0.00114), not a transcription error. |
| ΣC, ΣE printed with wrong sign (Q2) | Yes | Yes: arithmetic sums +0.00419 / +0.00207. Fig 8.9 confirms ΣE is positive (below). | Source slip, preserved (sic). |
| $\bar y_4$ printed +0.09189 | Should be −0.09189 | Yes: $-0.61944+1.06541\times0.49516=-0.09189$; printed $\bar y_5$ and the surface-4 F, C, E follow from the negative value. Scan shows "0.09189". | NEW finding; source dropped minus. Noted, preserved (sic). |
| Table 8.3 lens (c) thick F = 0.1029 (Q4) | Misprint for 0.0129 | −0.00542+0.01827 = 0.01285; thin 0.0136 | Confirmed; preserved (sic). |
| Table 8.4 lens (b) δ₂* (Q3) | Eq 48 gives +0.00379 | $Q^3\alpha_2+3Q^2\beta_2=+0.00379$; the printed thin-lens E −0.0182 uses −0.00379 (with +: −0.0198, thick −0.0195) | Confirmed; preserved (sic). |
| Fig 8.9 magnitude (Q5) | Third-order term negligible (0.19%) vs plotted 20% | **Validator wrong.** Eq 8 gives +0.0019 at 20° and +0.00045 at 10°; the plot's 3rd Order curve reads 0.19 and ~0.05. The axis is percent and it matches. | Note added after Fig 8.9. |
| Σa −0.00040 vs −0.00044 (Q6) | Rounding | Sum is −0.00044; a 4-unit gap in the 5th decimal, outside pure rounding | Noted (sic). |
| §8.5.2.3 arithmetic | PASS | b₃ −0.006341, b₅ 0.002818, Y_k(1.0) −0.003523 all reproduce | PASS |
| Table 8.3 thick sums, thin E for (a),(b),(c) | PASS | Confirmed by hand | PASS |
| Gem 8.1 (r/r_max)² rule | FLAG | Not in ch08 §8.2.3.1 (agrees with the catalog's own supplement) | See Bucket B-2 |
| Gem 8.4 invariant | FLAG | $y(nu)-\bar y(n\bar u)$ changes by $t(u^2-\bar u^2)$ under translation, so it is not invariant. Eq 35: $\Phi=\bar y u-y\bar u$; general $\Phi=n(\bar y u-y\bar u)$. | See Bucket B-1 |
| Gems 8.2, 8.3 | PASS | Text supports both | PASS |

## Bucket A (applied)
- `ocr_output/ch08.md`: Table 8.2 editorial note rewritten (E row now confirmed by Eq 13; ΣE sign tied to Fig 8.9; $\bar y_4$ sign slip recorded).
- `ocr_output/ch08.md`: Eq 13 note corrected; Table 8.3 note (iii) corrected; Fig 8.9 units note added; b₃ note updated.
- `ocr_output/ch09.md`: note repeating the false "Eq 8-(13) does not reproduce the E row" claim corrected.
- `ocr_output/ch11.md`: editorial sic note added after the b₃/b₅ line (printed text unchanged).

## Bucket B (human decision; NOT applied)
1. **Gem 8.4 formula** | catalog prints $\Phi=y(nu)-\bar y(n\bar u)$ | validator, primary, and a translation-invariance proof all agree it is not invariant | correct form $\Phi=\bar y(nu)-y(n\bar u)$ (Eq 35 sign, $=-0.5460$ for the Table 8.2 triplet) | Options: [apply-corrected (recommended) / leave for the ch06 deep pass]. Source is ch06, so the edit also needs a check against the ch06 scan.
2. **Gem 8.1 "quick energy estimate" (r/r_max)²** | not in ch08; valid only for a perfect pupil-to-image mapping | the catalog already carries a supplement saying so, but the gem body still states the rule | Options: [delete the rule from the body / keep with the supplement / unresolved].
3. **Table 8.2 as-printed slips** ($\bar y_4$ sign, ΣC, ΣE, Σa) and **Table 8.3 (c) F = 0.1029**, **Table 8.4 (b) δ₂***: all currently preserved as printed with sic notes | Options per item: [preserve+sic (current) / apply-corrected values in the edition text].
4. **ch11 b₃ = −0.0014**: preserved with sic note; the corrected value would be −0.00114 | Options: [preserve+sic (current, recommended) / apply-corrected].
