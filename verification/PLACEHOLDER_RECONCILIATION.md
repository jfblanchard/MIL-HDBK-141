# Figure/Table Placeholder Reconciliation — ch16, 20, 21 (2026-10-03)

Method: cross-referenced every bare `[FIGURE … needs manual extraction]` / `[TABLE …
needs manual extraction]` placeholder page in `ocr_output/ch16/20/21.md` against the
figure regeneration specs in `verification/gap_pages_figure_specs.md` (commit `a86d81e`).

## Figures — essentially done (97%)

| Chapter | Figure placeholder pages | Covered by specs | Uncovered |
|---|---|---|---|
| ch16 | 21 | **20** (2,4,6,10,11,13,20,21,22,23,24,38,40,47,50,51,54,57,59,60) | **1** (p31) |
| ch20 | 15 | **14** (2,11,15,23,24,38,47,66,72,75,90,91,93,94) | **1** (p26) |
| ch21 | 4 | **4** (4,13,77,78) | **0** |

**Only 2 figure pages remain uncovered:**
- **ch16 p31** — Fig 16.19: plot of transmitted beam / multiple-beam interference
  fringe sharpness (W…)
- **ch20 p26** — Figs 20.23 + 20.24: computed spectral reflectivity vs wavelength (microns);
  20.24 is same as 20.23 but with n₁ = 2.40

These two are small and can be folded into the ch22-25 batch's follow-up or a tiny next pass.

## Tables — large separate gap (~95 pages), with false positives

| Chapter | Table placeholder pages | Covered | Uncovered |
|---|---|---|---|
| ch16 | 35 | 4 (11,23,47,57) | ~31 |
| ch20 | 62 | 7 (11,15,23,24,47,75,91) | ~55 |
| ch21 | 10 | 1 (77) | ~9 |

**Important:** several of these are **false positives** — OCR misread figure gridlines /
axes / alignment as data tables. Known example (EDITORIAL_NOTES): "Pages 23–25 have
multiple TABLE placeholders from figure gridlines. The actual figure is a meridional ray
plot (Figure 11.13) not a data table." A table pass must **filter false positives first**,
then transcribe real tables (with column-header OCR fix noted in EDITORIAL_NOTES).

## Column-header OCR issue (tables)
EDITORIAL_NOTES: "column headers garbled (systematic OCR issue with table headers)" — a
table-transcription pass must reconstruct headers from the scan, not trust OCR text.

## Recommendation
1. ✅ Figures: collect ch22/23/24/25 pass (running), then fold in ch16 p31 + ch20 p26.
2. ⏳ Tables: separate filtered pass — detect+drop gridline false positives, then verify
   real table headers against scans. Candidate for the next Devin batch.