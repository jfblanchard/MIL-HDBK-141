# Spot-Check Verification Report — ch17, ch08, ch21
_Date: 2026-08-23. Method: Claude VLM (vision) on raw PNGs vs Tesseract OCR output, blind comparison._

## Chapters sampled

| Chapter | Title | Pages | Eq density | Pages sampled |
|---------|-------|-------|------------|---------------|
| ch17 | Optical Material | 10 | 1.5/pg | 1, 5, 9 |
| ch08 | Aberration Analysis & Third Order Theory | 22 | 4.2/pg | 2, 10, 18 |
| ch21 | Coating of Optical Surfaces | 78 | 6.6/pg | 5, 35, 65 |

---

## ch17 — Optical Material (text-heavy)

### Page 01 (section 17.1–17.2.3, prose + 3 equations)
- **Prose**: HIGH agreement. Body text matches well across both methods.
- **Header not stripped**: "MIL-HOBK-14[" passed through (bracket/digit confusion; stripped pattern only catches "MIL-HDBK").
- **TABLE false positive**: Tesseract placed a TABLE placeholder at the top of a page with no table — a horizontal rule triggered the blob detector.
- **Equation fragments leaking**: Raw partial equation text appears ABOVE and BELOW the `[EQUATION]` placeholder lines (e.g. loose `sin? (I +1')` and `n- 1]?` lines). The placeholder fires but doesn't fully suppress the surrounding OCR noise.
- **Symbol error**: "p-value" instead of "v̄-value" (ν-bar / nu-bar). OCR cannot render the overbar symbol; renders it as "p". Systematic across the chapter.

### Page 05 (section 17.4–17.6.1, numbered list prose)
- **Prose**: HIGH agreement. The 7 environmental characteristics (softening, thermal shock, thermal expansion, specific gravity, hardness, surface deterioration, devitrification) all transcribed accurately.
- **TABLE false positive**: Another horizontal rule at top of page triggered a TABLE placeholder.
- **Gutter artifacts**: Many lines prefixed with `i ` or `| ` (page-binding shadow artifacts) — these persist in the output.

### Page 09 (section 17.7.2–17.7.3 + Figure 17.2 reflectance chart)
- **Prose**: HIGH agreement. Metal coating text (Al, Ag, Au, Cu, Rh reflectance discussion) accurate.
- **FIGURE placeholder**: Correctly detected Figure 17.2 (reflectance graph).
- **EQUATION false positive**: EQUATION 15 fired on graph noise — the graph data area bled into OCR and was misclassified as a math line. Not an equation.
- **Small OCR error**: "ona vacuum" → should be "or a vacuum".
- **Header not stripped**: "OPTICAL MATERIAL MIL- HOBK-{4{" — the running chapter title combined with the garbled header passed through the header filter (which only strips lines containing "MIL-HDBK" joined).

### ch17 verdict
- Prose quality: **~88–90%**
- Systematic issues: TABLE false positives (horizontal rules), EQUATION false positives on graph noise, incomplete header stripping, ν-bar symbol rendered as "p".

---

## ch08 — Aberration Analysis (math-moderate)

### Page 02 (almost entirely figures: Fig 8.1a, 8.1b spot diagrams + Fig 8.2 energy curve)
- **FIGURE placeholder**: Correctly fired — page is flagged as a figure.
- **Caption leakage**: "Figure 8.1 (a)- Spot diagram..." and "Figure 8.1 (b) ~..." partially readable in Tesseract output. Caption text present but mixed with garbage.
- **Graph data garbling**: Dot patterns from spot diagrams and curve axis labels come through as garbage characters ("ms 60", "py 90", "0 Jo 06200 380s 40").
- This page is handled correctly at the intent level — human will need to manually describe the figures.

### Page 10 (equations 6–8, sections 8.6.1.2–8.6.2)
- **Prose**: HIGH agreement. Sections 8.6.1.2 (definitions of ΣB, ΣF, ΣC, ΣP) and 8.6.1.3 (using equations to predict ray positions) match well.
- **TABLE false positive**: Full-page table placeholder despite no table.
- **Header partial miss**: "MIL HDBK-141" (space instead of hyphen) not caught by header strip.
- **Equations (6) and (7)**: Complex multi-line equations split across EQUATIONS 14–19. All flagged correctly; none silently passed. However raw fragments leak between placeholders (e.g. standalone lines "3Y₁² + X₁..." appear outside any placeholder).
- **Symbol**: Σ rendered as "Z" throughout (ΣB → ZB, ΣF → ZF). Consistent and predictable.
- **"fractional distortion"**: Correctly identified and flagged as EQUATION 20, though formula content garbled.

### Page 18 (stop shift equations 18–23, thin lens section 8.10, equations 24–28)
- **Prose**: HIGH agreement. Sections 8.9.4, 8.9.5.1, 8.9.5.2, 8.10, 8.10.1 all well transcribed.
- **TABLE false positive**: Again.
- **Equations (18)–(21a)**: Captured as EQUATIONS 53–57. All flagged. Content garbled but flagged correctly.
- **Word corruption**: "chromatic coefficients" → "chromatic poeexenss" (severe OCR error on one word).
- **Equations (24)–(28)**: Captured as EQUATIONS 60–64. All flagged.
- **Symbol**: φ (phi) rendered as "9" or "?" in equation content (garbled, but inside placeholder).

### ch08 verdict
- Prose quality: **~88–90%**
- Equation handling: **Solid** — every equation is flagged; none passed silently. Fragment leakage around placeholders is the main nuisance.
- One prose word corruption: "poeexenss" (page 18).

---

## ch21 — Coating of Optical Surfaces (math-intensive)

### Page 05 (sections 21.2.4.3–21.2.4.5, Fresnel coefficients, EM theory)
- **Prose**: GOOD agreement. Fresnel coefficient derivations and total internal reflection discussion mostly accurate.
- **TABLE false positive**: Horizontal rule at top triggered it again.
- **EQUATION 30 false positive / garbage**: The placeholder content is pure noise ("E———E—AE=S—EEeEeEe...") — a decorative rule or line art triggered the equation detector.
- **Equations (22)–(25)**: Partially captured. Some as placeholders (EQUATIONS 31–32), some as raw leakage lines. All flagged, none silently passed.
- **Symbol garbling**: Subscript notation mangled ("ig 2 sin7}" for "i_g ≥ sin⁻¹"), "n2 p2 2 nz" for "n₂ρ₂ ≥ n₁". Dense in this chapter.
- **Section number format**: "21, 2. 44 4" → should be "21.2.4.4" (spaces inserted into section numbers).

### Page 35 (matrix/quaternion equations 142d–142e, Section 21.5 quaternion methods)
- **Prose**: GOOD. Section 21.5.1 introduction and 21.5.2 definitions well transcribed.
- **CRITICAL ERROR — section number corruption**: Tesseract output shows **"10.5.2 Quaternions"** — the leading "2" was dropped, making it read as section 10.5.2 instead of 21.5.2. This would mislead a reader into thinking this is a cross-reference from Chapter 10. **Needs correction in ch21.md.**
- **Equations (142d)–(142e)**: Flagged as EQUATIONS 274–279. Matrix product notation completely garbled but flagged.
- **Greek/symbol**: σ (sigma unit vectors) rendered as "o" or "%" throughout. q₀, q₁ subscripts garbled.
- **FIGURE placeholder**: Matrix equation block partially flagged as a figure (large connected ink region).

### Page 65 (almost entirely Figure 21.30 — spectral reflectance graph)
- **FIGURE placeholder**: Correctly fired.
- **Header severely garbled**: "MiL-HD6K-I41t" (6 instead of B, lowercase i, trailing t). This chapter has more header garbling than ch17 or ch08.
- **EQUATION false positives**: Graph legend labels (n₀=1, n₁=1.51, etc.) captured as EQUATIONS 445–448. These are curve labels on the graph, not equations.
- **Axis labels**: Partial capture of "0.4 0.45 0.50..." x-axis values — readable.
- **Caption**: "Figure 21.30- Spectral reflectances..." partially captured and readable.

### ch21 verdict
- Prose quality: **~82–85%** (lower due to denser math context and more symbol garbling)
- **One confirmed content error requiring fix**: section "10.5.2" should be "21.5.2" in ch21.md.
- Equation handling: All real equations flagged. Higher false positive rate from graph legends.
- Header garbling: More severe than other chapters.

---

## Cross-chapter summary

### Systematic issues (affect every chapter)

| Issue | Severity | Chapters |
|-------|----------|---------|
| TABLE false positives from horizontal rules | Medium | ALL |
| Header stripping misses variations (spaces, garbled chars) | Low | ALL |
| Equation content leaking as raw text around placeholders | Low-Medium | ch08, ch21 |
| EQUATION false positives on graph noise / legend text | Low | ch17, ch21 |
| Greek/special symbols mangled (Σ→Z, σ→o, ν-bar→p, φ→9) | Medium | ALL |
| Gutter artifacts (`i `, `| ` line prefixes) not fully cleaned | Low | ALL |

### One confirmed content error

- **ch21.md, around page 35**: "10.5.2 Quaternions" should be "21.5.2 Quaternions". Section number digit dropped by OCR. **Action required: fix in ocr_output/ch21.md.**

### Prose quality across profiles

| Chapter | Profile | Prose quality estimate |
|---------|---------|----------------------|
| ch17 | Text-heavy | ~88–90% |
| ch08 | Math-moderate | ~88–90% |
| ch21 | Math-intensive | ~82–85% |

Quality degrades slightly with equation density — not because prose errors increase, but because the math context introduces more symbol noise and the proximity of equations creates more OCR interference. Still consistent with the ch06 pilot (80% agreement).

### Conclusion

The pipeline is **performing consistently** across all three chapter types. No equations passed silently through without being flagged. Prose is reliable. The issues are **systematic and fixable** in a cleanup pass rather than random chapter-by-chapter failures.

**Recommended next actions:**
1. Fix the confirmed section number error in ch21.md (21.5.2 vs 10.5.2).
2. Cleanup pass on all chapters: strip surviving header variants, remove `i ` / `| ` gutter artifacts.
3. For the "Lost Gems" analysis: prose quality is good enough to proceed on text-heavy chapters (ch17 and similar). Math-intensive chapters (ch21) need equation LaTeX pass first.
4. Consider tightening the TABLE placeholder detector to ignore thin horizontal rules (< 10px height blobs).
