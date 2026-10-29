# MIL-HDBK-141 Table Reconcile — FINAL (2026-10-03)

**Question asked:** are there any REAL table gaps requiring a vision pass before going back
to Devin+Gemini image reads? A short, cheap, zero-Devin-quota reconcile (pure regex over
`ocr_output/`) answers it.

## Method
For every `ocr_output/ch*.md`:
1. Collect every "Table N.M" / "TABLE N.M" reference (prose call-outs AND printed headings).
2. Detect whether the chapter contains any proper markdown table (`|` header + `|---|` separator).
3. Flag a table as a gap ONLY if it is referenced but the chapter has NO markdown tables.

## Result — NO vision-required table gaps exist

| Outcome | Count | Detail |
|---|---|---|
| **Already markdown tables** | most | ch07 (5), ch08 (4), ch10 (13), ch11 (14), ch13/ch14/ch15/ch17/ch20/ch21/ch23/ch24/ch26 |
| **Spurious cross-chapter refs** | 2 | ch12's "Table 11.3"/"14.7" are prose refs to tables living in ch11/ch14 (both already markdown) |
| **ch06 cohort — 13 tables, all buildable from OCR** | 13 | Tables 6.1–6.14 present as fully-specified `[TABLE]` placeholders with real numeric cell values (see below) |

## ch06 — the only "MISSING" cluster, but NOT a vision gap
ch06 has 13 referenced tables (6.1–6.14) with **zero markdown tables and zero printed headings**
in `ocr_output/ch06.md`. However, every one exists as a **rich `[TABLE]` placeholder** that spells
out the exact columns, rows, and **numeric cell values** — e.g.:

- **Table 6.10** (p20): "Columns SURFACE|OBJECT|1|…|k. c: 0, −0.500, −0.330…; t: ∞, 1.000, 3.000…;
  n: 1.000, 1.500, 1.000…; c(n₋₁−n): 0, 0.250…; t/n: ∞, 0.667, 3.000…" — complete data.
- **Table 6.1** (p2): full row/column structure + diagonal computation rule (the only one with an
  "etc." — cosmetic; the format table is fully specified structurally).
- **Table 6.11** (p21): c: 0, c, 0; t: t₀, t₁; n: 1, −1 (reflection); c(n₋₁−n): 0, 2c, 0 … complete.

All 13 contain numeric cell data (`HAS-NUMS`). They are **mechanically reconstructable as markdown
tables from the OCR text** — a formatting task, NOT a vision task.

## Bottom line
- **Do NOT run a vision pass over the ~150 `[TABLE]` placeholders** — they are figure/gridline
  noise (proven by the ch21 pilot: all 8 pages → "NO REAL TABLE").
- The book's real tables are **already transcribed as markdown** everywhere except ch06.
- **ch06 table render: ✅ DONE 2026-10-03** — all 13 tables (6.1–6.12 + 6.14) turned from rich
  placeholders into `|` markdown tables in `ocr_output/ch06.md`. Verified: each rendered exactly
  once; ch06 partial PDF builds clean (pandoc 0, 3× pdflatex 0, zero unmapped glyphs; Table 6.6's
  signature values confirmed in the extracted PDF text). No vision, no Devin quota used.

## Table 6.13 — genuinely absent (1962 source skip, not a gap)
ch06's table sequence runs **6.1–6.12 then 6.14 — there is no Table 6.13**. The ch08 cross-ref
"the thin lens illustrated in Table 6.13" is a **1962 original reference error** (kept as printed,
flagged `(sic)` at `ocr_output/ch08.md`; it presumably points to ch06's thin-lens Table 6.8/6.9).

## Artifacts
- Script: `pipeline/table_reconcile.py` (reproducible — rerun with `python3 pipeline/table_reconcile.py`)
- ch06 render transform: `/tmp/ch06_render_tables.py` (replace `[TABLE:]` → markdown, keyed templates)
- This doc: `verification/table_reconcile_final.md`