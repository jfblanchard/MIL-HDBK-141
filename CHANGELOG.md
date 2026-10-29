# Changelog

## 2026-10-29

### Public release
- Repository history reset to a single commit for public release; earlier history is kept privately.
- Scripts no longer hardcode local tool or repo paths: `ocr_pipeline.py` finds tesseract/pdftoppm on PATH
  (override with `TESSERACT_CMD` / `PDFTOPPM`), `cleanup_ocr.py` and `cross_diff.py` resolve paths from the repo,
  and `build/lens_designs/run.py` falls back to `OPTILAND_SRC`.

## 2026-10-27

### Last two OptiLand schematics + both ch20 tables done; side-by-side figure review PDF
- **16.13** (`ch16_fringe_localization`): Fizeau-fringe localisation construction — wedge S1/S2 (angle theta, medium n1),
  source S, reflections at D and Q crossing at P beside the surfaces, eye lens imaging to P' on the retina, dashed
  continuations to virtual source images s1/s2, 'd = QD, approximately'. Pure `schem.py` construction; P is placed where
  the book draws it (an exact wedge reflection at the exaggerated angle would not cross there).
- **16.24** (`ch16_reflect_microscope`): microscope for reflected fringes under vertical illumination — lateral
  source + lens + monochromatic filter + pin-hole H, 45 deg beamsplitter, objective, specimen plates P1/P2 with test
  faces S1/S2, pin-hole images H0/H1/H2, reticle at the image plane, micrometer eyepiece. Ideal elements only.
- **Table 20.1** (13 substrate materials) and **Table 20.3** (effective indices at phi = 65 deg) transcribed from the
  scans to markdown tables in `ocr_output/ch20.md`, replacing the garbled OCR bodies (house format, as Table 20.4).
  A false-positive `[FIGURE:]` placeholder on p15 removed (the page holds only the table).
- `verification/figure_review_pdf.py` -> `build/figure_review.pdf`: one landscape page per figure, scan crop
  (auto-detected region, caption-anchored via tesseract TSV) vs the rebuilt PNG, for human sign-off. Sections:
  73 rebuilt figures + 7 layout rebuilds, 13 flagged, 11 halftone (scan only), 5 3D-coordinate (scan only), 2 tables.
- Schematic bucket is now 44 DONE / 13 FLAGGED / 0 TODO; tables 2/2. Remaining: 11 halftone scan crops, 5 3D figures.

## 2026-10-25

### Matplotlib batch complete: 16.2, 16.26, 25.27 (066f1f0)
- These three had been counted as done but never built. **16.2** (`ch16_fizeau_notation`): the scan's Figure 16.2 is the Fizeau
  interferoscope notation diagram (H, L1, L2, beam splitter, S1, S2, C, A, B, d, theta, alpha, X/Z/P at O), not the sine-wave plot
  the spec describes; drawn as a construction schematic with `schem.py`. **16.26** (`ch16_narrow_fringes`): narrow fringes of
  order nu to nu+2 shifted by Delta x across the film edge AB, spacings h. **25.27** (`ch25_foucault_isophotes`): isophotes and
  intensity along the diameter for a perfect mirror, knife edge central, from Linfoot's eq. (11) in closed form; one scale factor
  fitted to the printed centre value, then agrees with the printed curve to about 5 percent. Isophote levels are the formula's values
  at the scan's crossings of the diameter (the book gives no levels).

### Matplotlib batch: the 13 measured-curve figures, traced from the scans
- 20.44-20.47 (`34e3c9b`), 20.85-20.87 (`2aa957d`), 20.95 (`6acffab`), 20.96 (`fe65077`), 20.97 (`b6e356a`),
  20.101 with its circuit inset (`893e8ad`), 20.120 (`2c684be`), 20.121 (`9e116c3`). One `build/lens_designs/<name>/` folder
  each: `<name>_trace.py`, `trace.csv`, `<name>_plot.py`, vector `.pdf`, 600 dpi `.png`, `README.md`.
- `digitize.py` extended: `AffineAxes`, `calibrate` (grid intersections) and `tick_axes` (tick-only plots) fit pixel to data
  and absorb the scan tilt; `rule_mask` blanks grid rules; `snap` moves a hand-read guide onto the ink along its normal;
  `trace_figure` runs a figure end to end and writes a debug overlay. `plotkit.py` gained `load_trace`.
- Every trace was checked by drawing it back on the scan. Accuracy about 0.5 percent of axis span; 20.87 about 1 percent
  (hand-ruled grid); 20.96 hand-read (seven interleaved curves) at about 1.5 percent.
- The ch20 specs in `gap_pages_figure_specs.md` had wrong axes for most of these figures; the scans were followed and each
  README states the correction. Discrepancies in the 1962 figures kept as printed: 20.46 x labels; 20.120 widths vs labels;
  20.121 '.12 mu' half width.
- Manifest: Matplotlib section is now a per-figure table, 26 DONE, 3 TODO. 16.2, 16.26 and 25.27 had been counted as done
  in STATUS but were never built.

## 2026-10-24

### OptiLand schematic batch: manifest + 42 book-quality schematics
- **Step A:** `verification/OPTiLAND_BATCH_MANIFEST.md` (`78ddb0f`) classifies all 104 specs in the three
  figure-spec files: 57 OptiLand-schematic, 29 Matplotlib-plot, 11 Halftone-photo, 5 3D-coordinate, 2 Table.
- **Step B:** 42 schematics built to `BOOK_QUALITY_RECIPE.md` (frameless, true scale, black line art, Latin Modern, vector
  `.pdf` + 600 dpi `.png`, named parts, ray styles): ch16 x13 (`80323f5`, `6700189`), ch20 x5 and ch21 x2 (`6861f5d`),
  ch25 x15 (`4699d2f`), ch22 x1, ch23 x5, ch24 x1 (`1d108f0`). One `build/lens_designs/<name>/` folder each.
- The specs give no prescriptions, so the figures are constructions of ideal thin lenses, plane/spherical mirrors, plates and
  splitters at the geometry each figure defines. New `build/lens_designs/schem.py` (on top of `common.py`): `canvas`, `ray`
  with direction arrowheads, `mirror`, `spherical_mirror`, `plate`, `splitter`, `tlens`, `biconvex`, `eye`, `dim`, `arc`,
  `lamp_housing`, `tg_common` (Twyman-Green frame), `hatch_block`, `reflect`/`hit`. `common.py` is unchanged.
- 13 figures flagged `FLAG-UNABLE` (missing prescriptions/dimensions or ambiguous spec); 2 not started (16.13, 16.24).
  The five existing systems (ch12, ch14, ch15, ch23) are untouched.

## 2026-10-10 (later)

### ch12 relay, ch14 Huygenian + Ramsden, ch15 telescope converted to book quality
- Same recipe as ch23 (`BOOK_QUALITY_RECIPE.md`): true scale, no axes/grid/title/color, Latin Modern,
  vector `.pdf` + 600 dpi `.png`, OptiLand surface numbers, named parts, ray key, scale bar. Optics
  and the printed book-vs-OptiLand README lines are untouched; only the drawing layer changed.
- **ch12:** `ch12_single_relay_layout` (Fig 12.1) and `ch12_double_relay_layout` (Fig 12.2), 6.5 in.
  Ideal lenses as plane symbols, axial pair at u_o and the chief ray from the 6.6 mm field edge,
  object/image arrows, D, A/B, f = D/8. Replaces the two-panel `ch12_relay_layout.png`.
- **ch14:** `ch14_huygenian_layout` (Fig 14.1) and `ch14_ramsden_layout` (Fig 14.4), 4.8 in, book
  orientation (exit pupil left, light toward the eye), axial pair + 15 deg chief ray, exit pupil and
  field stop with the book's 0.292/0.268 and 1.187/0.673 cm. The Huygenian's virtual-focus stop no
  longer draws rays running backward from the last surface.
- **ch15:** `ch15_telescope_10x_layout`, 6.5 in, objective / Porro block (2.9 cm aperture, 11.6 cm) /
  Erfle eyepiece at one true scale with the 15 cm tube cut out, chief ray of the full field to the eyepoint.
- `common.py`: `stop_bars`, `dimension`, `thin_lens`, `draw_ch14_eyepiece`, `draw_rays(reverse=)`.

## 2026-10-10

### ch23 microscope book-quality prove-out + render recipe (commit `1d6f525`)
- **Quality bar for figure generation set** on the hardest case. `ch23_objective_layout` (Fig 23.7
  redrawn: axial bundle at N.A. 1.25, cover glass + oil, surfaces 1-11, "174.90 to image plane",
  2 mm bar, 4.8 in wide) and `ch23_microscope_layout` (6.5 in full width; objective and eyepiece at
  one true scale with the tube cut out; axial pair + chief ray to the eyepoint; Fig 23.8's 11.08 mm
  diaphragm at the traced focal plane; surfaces 12-15; ray key; 5 mm bar). Both are B/W line art
  in Latin Modern, vector `.pdf` + 600 dpi `.png`.
- **Before:** `optic.draw()` defaults: 14x4 / 8x4 in panoramic plots, grid, in-figure title, gray
  translucent lenses, default color cycle without a key, no numbers or labels; the full scope at
  20:1 with the objective a smudge.
- `build/lens_designs/common.py`: new book-drawing layer (`BOOK_RC`, ray/lens styles, `book_axes`,
  `broken_axes`, `trace`, `draw_rays`, `sag`, `clear_apertures`, `elements`, `draw_lenses`,
  `draw_slab`, `number_surfaces`, `label`, `scale_bar`, `save_book`). `save_layout()` kept as-is.
- `build/lens_designs/run.py`: launcher; the optiland env's editable install can point at a
  stale path, so it falls back to a local optiland checkout (`OPTILAND_SRC`).
- `build/lens_designs/BOOK_QUALITY_RECIPE.md`: conventions, before/after, 5-item checklist for the
  Devin batch.
- Optics untouched: the script's book-vs-OptiLand lines reproduce the README exactly.

## 2026-10-04

### ch06 tables rendered + authoritative handoff docs; 521-pp placeholder PDF (commits `797d19d` + doc updates)
- **ch06 tables rendered** (`797d19d`): all 13 ch06 markdown tables (6.1–6.12 + 6.14) built from
  their numeric `[TABLE]` placeholders and verified (Table 6.6 c/t/n rows intact, U+2212 minus
  signs present, zero unmapped glyphs after ellipsis fix). ch08 cross-ref to the non-existent
  "Table 6.13" flagged `(sic — no Table 6.13 in ch06; sequence runs 6.1–6.12 then 6.14)`. Closes
  the last table gap.
- **Full 27-chapter PDF built** with figure placeholders: `build/MIL-HDBK-141.pdf`, 521 pp,
  letter, 2,736,936 bytes. All 1543 display equations rendered; 893 `[FIGURE/…]` placeholder
  boxes shown as small sans-serif blockquotes. 4 pre-existing ch13 unmapped glyphs remain
  (U+042F, U+10B6/U+10B9, U+1D1A) — non-blocking OCR artifacts.
- **Authoritative handoff docs refreshed** so any LLM can resume without repeating work:
  - `CLAUDE.md` — added a mandatory **"START HERE"** block (read STATUS.md first; check
    CHANGELOG.md + FIGURE_AUDIT.md + `git log`), a **STATUS-UPDATE RULE** (update STATUS.md +
    CHANGELOG.md in the same commit as any completed work — never leave stale), a current-state
    summary, refreshed next steps (figure generation), a corrected repo path, and the
    vision-routing update (Devin+Gemini for scan-page vision).
  - `STATUS.md` — marked ch06 tables DONE, added the LLM-pickup note + status-update rule at the
    top, and reframed the remaining work as **figure generation** (480 figures from specs;
    tooling split Matplotlib/OptiLand/scan-crop) + figures-embedded PDF.

## 2026-09-26

### Full PDF re-rendered incl. corrected ch05 (commit `d109acc`)
- `build/MIL-HDBK-141.pdf` regenerated from ch01–ch27 so the re-transcribed ch05 (commit
  `303434e`, full re-transcription from scan) is included: 495 → 519 pp, 1399 → 1543 display
  equations (+144, all from ch05: 57 → 201 `$$` blocks), 1543/1543 rendered
- Build clean: pandoc exit 0, pdflatex 3 passes exit 0, zero LaTeX errors; unmapped-glyph
  placeholders identical to the prior build (U+042F ×2, U+10B6 ×10, U+10B9 ×1, U+1D1A ×7),
  no new ones; worst overfull hbox 72.9pt in ch08 (pre-existing, chapter unchanged)
- `STATUS.md` pipeline row → ✅ DONE, `build/README.md` build date/commit updated

## 2026-09-20

### ch08 blind validation and reconcile
- Validator: DeepSeek v4 Pro (OpenRouter, text-only). Reply saved verbatim, with a provenance header, in `exchanges/20260918_ch08_validate_response.md`. The first attempt spent its whole token budget on reasoning and returned nothing; the rerun used low reasoning effort.
- The validator's numeric claims were shown without arithmetic, so each was re-derived independently (retrace of Table 8.2, data fits, scan re-reads). Details: `exchanges/20260920_ch08_reconcile_SHORTLIST.md`.
- **Eq 8-(13) is correct as printed.** It reproduces the whole Table 8.2 E row once $\Phi=\bar y u-y\bar u=-0.5460$ (Eq 35). The deep pass's "does not reproduce" note used the wrong $\Phi$; corrected in ch08, and the same false claim in ch09.
- **b₃ (ch11 §11.3.2.5): source erratum.** Printed −0.0014 (scan re-read); fit −0.001144, Table 11.8 route −0.00115; b₅ and b₀ reproduce. Printed value preserved, sic note added to ch11.
- New Table 8.2 finding: $\bar y_4$ printed +0.09189 but the retrace gives −0.09189 (dropped minus in the source). ΣC and ΣE are printed with the sign opposite to the arithmetic sums; the positive ΣE is confirmed by Fig 8.9, whose axis is in percent (+0.19% at 20°). All preserved as printed with sic notes.
- Validator wrong on one point: it read Fig 8.9 as 20% and called the third-order term negligible; the axis is percent and the curves match.
- Gem 8.4 (invariant written as $y(nu)-\bar y(n\bar u)$) confirmed wrong by validator, primary and a proof; gems 8.1 and 8.4 edits are shortlisted for the human, not applied.

## 2026-09-18

### ch11 reconciliation close-out (Tier 1/2/3)
- Catalog gems 11.1-11.6 corrected after independent re-derivation (Devin first, Claude second, agreeing):
  - 11.2 Petzval scaling is 1/MP, not 1/MP² (Eq. 3 bracket; reproduces Table 11.1 exactly); "100×" → ~10×; unsupported quick-check dropped
  - 11.3 L_{k-1} is the emerging ray's direction cosine, not a focus shift; f/10 example is ≈0.05 mm, not 0.01 mm
  - 11.4 "3-5×" removed; air-space range now Table 11.9's actual span (≈0 to 7.4% of f′)
  - 11.1 mechanism reworded to the book's axial-ray reasoning; "1.5-2× field" removed
  - 11.5 intermediate OPD step fixed (Y_k = f′/(4400·F), OPD = f′/(17,600·F²)); final numbers unchanged
  - 11.6 wording fixes: powers ∝1/Δ, two determinants distinguished, collinear-glass caveat, headline reworded
- `ocr_output/ch11.md`: inline editorial notes (sic-preserve, transcribed text unchanged) for the §11.4.3.4 inequality and Table 11.14 curvatures (Table 11.14 system power ≈0.29 vs 0.10 required; Table 11.13 checks out); notation note on P̃ vs P̃*/P̃** at §11.4.2
- b₃/b₅ (§11.3.2.5) deferred to the ch08 deep pass
- `exchanges/20260918_ch11_reconcile_SHORTLIST.md`: every item now carries a Disposition line

## 2026-09-13

### Reconcile independent validation (Devin/DeepSeek) findings for ch25 and ch26
- Cleaned up a section of ch25.md (§25.8.1.3, §25.8.1.11, §25.8.2.2, §25.10.1.1-25.10.2.1)
  that had been left as raw uncleaned Tesseract OCR despite the chapter's deep-pass commit;
  fixed OCR-garbled λ (misread as π/"r"/"2") in two phase-change passages, section numbers,
  and general noise — no physics content changed, both "π/2" FLAGs were λ misreads, not
  source errors
- ch25 Eq. (1) (nodal-slide distortion): confirmed genuine dimensional ambiguity in the
  1962 source (linear displacement vs. fractional distortion, undefined in the text) —
  added an editorial note rather than rewriting the printed equation; gem 25.8 updated
  to match
- ch25 Eqs. (9)-(10) (Ronchi shadow magnification): scan confirms the radicands are
  printed without exponents (√(η+ξ) not √(η²+ξ²)) — preserved as-printed (sic) with an
  editorial note on the physically consistent form; not a transcription error
- ch25 §25.10.1.4 (Foucault worked example): scan confirms "10⁻⁴ inches or .025 mm" is
  printed as-is despite being internally inconsistent by ~10× — preserved as printed with
  an editorial note (did NOT adopt Devin's speculative ".0025 mm" rewrite, since the scan
  does not support it); separately, scan confirms "10⁻⁶ radians" where a prior transcription
  pass had corrupted this to unreadable OCR noise — fixed, and gem 25.4 corrected
  (was mistitled with 10⁻⁷)
- ch26 Eq. (12) (Coltman inverse series): independent re-derivation confirms the printed
  leading coefficients are exact and that r(9n) = 0 exactly — added as a caution to gem
  26.4 so the "..." is never filled in with a naive alternating continuation
- ch26 gem 26.5 (KDC): fixed acronym expansion to "Kinetic Definition Chart" (§26.1.4.1,
  confirmed via scan) and corrected the source citation from "§26.2.x" to §26.1.4
- ch26 Figure 26.4 table (NBS chart pattern-56 line width): scan confirms ".233" is printed
  as-is; added an editorial note that this is very likely a source typo for .223 mm (the
  25/(2N) rule and the table's own 3-line-width entry both point to .223) — preserved
  as-printed rather than silently corrected
- ch26 §26.1.2.1 ("contrast of black on white is 1.4"): scan confirms as-printed; added an
  editorial note that this cannot be a bounded reflectance contrast and is almost certainly
  a density/log-contrast figure — gem 26.3 updated to flag the convention ambiguity
- ch26 Table 26.1 row F: scan confirms values (5.6, 4.8) and blank EFL/F-number as printed;
  added an editorial note that the row's identity cannot be determined from the source
- Rejected: Devin's ch26 Eq. (8) δ-normalization query (scan matches the transcription
  exactly, no error) and the Eq. (4)/"equation (3)" cross-reference (confirmed as a genuine
  typo in the 1962 source, already faithfully transcribed, cosmetic only)
- Full findings and disposition: see `exchanges/20260913_ch25_deep_validate_response.md`
  and `exchanges/20260913_ch26_deep_validate_response.md`

### Catalog enrichment: fold ch22-26 deep-pass cross-checks into LOST_GEMS_CATALOG.md
- Deep LaTeX pass completed for ch25 (12 eqs, 36 figure-label fixes) and ch26 (12 eqs,
  21 figure/table-label fixes), closing out the full ch20-ch26 deep transcription pass
- Gem 22.5 (n² detector immersion gain): confirmed via ch22 Eq. (1), F_s = πIn²A
- Gem 24.1 (Seidel tolerances): re-confirmed via ch24 deep pass; Eq.(4)/Eq.(6) sin vs.
  sin² discrepancy preserved as-printed, consistent with the 2026-09-12 editorial note
- Gem 25.2 (Newton's fringe rules): confirmed via ch25 Eqs. (3)-(6), including the
  plate-immersion (index n) form
- Gem 25.4 (Foucault test sensitivity): confirmed via ch25 Fig. 25.24 caption (2θ
  deflection) and Eq. (11) (Linfoot's diffraction-limited treatment)
- Gem 26.1 (cascaded resolution): confirmed via ch26 Eq. (1)
- Gem 26.4 (Coltman square/sine-wave MTF conversion): confirmed via ch26 Eqs. (8)-(12)
- Added gem 25.7 (spherometer sagitta-to-radius formula, Eq. 2) and 25.8 (nodal-slide
  distortion measurement without a reference lens, Eq. 1)
- Added gem 26.5 (KDC visual-instrument efficiency metric, Eqs. 2-3)
- Catalog now spans 25.1-25.8 (ch25) and 26.1-26.5 (ch26); 151 gems total

## 2026-08-26 (session 15)

### ch05 validation response incorporated (exchanges/20260825_ch05_validate_response.md)
- All 7 questions PASS, all equations PASS — no corrections needed to ch05.md
- Response committed; confirmed: (K,L,M) direction cosines, (e,f,g,h) aspheric coefficients,
  Frankford Arsenal sign convention, Coddington RHS = Γ/r, Table 5.5 arithmetic, P invariant

### ch06 full VLM pass (ocr_output/ch06.md)
- Complete rewrite from 38 scan pages (ch06 = First Order Optics, not Aberrations — memory corrected)
- All 49 equations as LaTeX: paraxial trace (5-56, 5-57), optical invariant (Eq. 6), linearity (10a-10b),
  cardinal points (13-19), Newton/Gauss image equations (15-18), thin lens power (22), dialyte formula,
  mirror via negative index, differential coefficients (28-31), chromatic (37-38, 40-41), achromatic
  doublet conditions (43-45), Abbe number (46), secondary spectrum (48-49)
- Table 6.6 (three-element lens): full numerical data, 8 surfaces, m=−0.57708, Φ=−0.50000, f'=10.000
- Table 6.12 (differential example): Δu₆=0.00469 for Δc₄=0.01 — exact agreement with Eqs. 28-31
- 23 figure specs (Figs 6.1–6.22), 14 table specs (Tables 6.1–6.14)
- Gems 6.1–6.3 verified against scan

### ch06 validation prompt written (exchanges/20260826_ch06_validate_prompt.md)
- 7 specific questions covering ray trace format constants, optical invariant naming, focal length
  sign convention, Newton vs Gauss image equations, nodal point relation, mirror negative-index
  convention, and secondary spectrum f'/2200 constant source
- All 49 equations, Table 6.6 full data, Table 6.12 differential example included

## 2026-08-25 (session 14, continued)

### ch05 full VLM pass (ocr_output/ch05.md)
- Complete rewrite from 38 scan pages (Tesseract original was unusable: 166+ false EQUATION placeholders)
- All 15 skew-spherical equations (Eqs 1–15), aspheric sagitta + iteration (Eqs 16–32), meridional (Eqs 33–44), Coddington (Eqs 45–48), paraxial (Eqs 56–57)
- Table 5.5 (PR method 3-surface example) fully transcribed with numerical values
- 20 figure specs (Figs 5.1–5.20), 4 table specs (Tables 5.1–5.4)
- Gems 5.1 (PR method) and 5.2 (graphical Snell's law) verified against scan

### ch05 validation prompt written (exchanges/20260825_ch05_validate_prompt.md)
- 7 specific questions covering direction cosine notation, aspheric coefficient symbols, paraxial sign convention, Coddington RHS, Table 5.5 arithmetic, PR conservation property, orders-of-optics terminology

## 2026-08-25 (session 12, continued)

### Catalog restructure + renumber (analysis/LOST_GEMS_CATALOG.md)
- Reordered all chapter sections to match original document order (ch02 -> ch26)
- Renumbered all 132 gems from GEM-NNN to X.Y (chapter-scoped: 17.3 = Chapter 17, Gem 3)
- Standardized all 4 inconsistent chapter header styles to single <!-- CHAPTER NN --> format
- Updated 7 inline cross-references (GEM-021 -> 4.5, GEM-011 -> 6.3, etc.)
- Rewrote chapters table at top of catalog
- ch08 gems (8.1-8.5) confirmed in own section, not folded into ch06

### Plan update
- VLM enrichment pass decided as next step (replaces text-replacement LaTeX script)
- Per gem: validate text + write LaTeX from scan pages + figure specs + recreated tables
- Book format confirmed: A5 / 5.5x8.5" pocket reference, chapter-scoped gem IDs

### VLM enrichment pass started
- ch02 (gems 2.1–2.3): DONE
  - 2.1: inline LaTeX, noted relative-to-air convention, pointer to Table 2.4
  - 2.2: exact formula sin(Ic)=1/n added; Table 2.1 expanded to 21 rows (rad+deg); TIR figure spec
  - 2.3: Abbe constant formula added; Abbe diagram figure spec added
- ch03 (gem 3.1): DONE
  - Fixed formula from approximation to exact h=lambda/(n*sin(theta)); Figure 3.3 spec; Nyquist note
- ch04–ch26: pending

## 2026-08-24 (session 10, ch01 + ch02)

### Lost Gems — ch01 Introduction (analysis/LOST_GEMS_CATALOG.md)
No gems extracted. Pure administrative chapter: notation/symbol tables, scope history,
reference bibliography. Catalog table row marked DONE.

### Lost Gems — ch02 Fundamentals of Geometrical Optics (analysis/LOST_GEMS_CATALOG.md)
3 new gems extracted (GEM-130 to GEM-132):
- GEM-130: Quick-reference refractive indices for 10 common optical materials (Table 2.2)
- GEM-131: TIR critical angle rule: sin(Ic) = 1/n; crown glass Ic ≈ 41° — the prism design check
- GEM-132: Glass type number 6-digit encoding (nD refractivity + v-number); decode any glass spec
Catalog now covers all 29 chapters (27 content chapters mined); 132 gems total (GEM-001 to GEM-132).
Note: Page 8 (Table 2.4, full glass data table) was completely unreadable OCR — 65 equation
placeholders. The VLM figure pass will be needed to recover that table.

## 2026-08-24 (session 10, ch27_apdx)

### Lost Gems — ch27 Appendix: Trig Tables (analysis/LOST_GEMS_CATALOG.md)
No gems extracted. Appendix is 10 pages of Sine-Angle and Angle-Sine conversion tables —
standard trig lookup tables from the pre-calculator era, completely superseded by sin()/asin().
OCR captured no usable numerical data (all noise). Table row marked DONE with explanation.

## 2026-08-24 (session 10, ch26)

### Lost Gems — ch26 Evaluation Phase Optical Tests (analysis/LOST_GEMS_CATALOG.md)
4 new gems extracted (GEM-126 to GEM-129):
- GEM-126: Cascaded system resolution: 1/Re² = 1/R₁² + 1/R₂² + ... (§26.1.2.6)
- GEM-127: Visual test rule: chart lines must subtend >60 arc-sec at eye; NBS standard = 26 focal lengths (§26.1.2.5)
- GEM-128: High-contrast target = accurate measurement; low-contrast = realistic field performance; match to use case (§26.1.2.3)
- GEM-129: Square wave targets → MTF via Coltman formula R(n) = (π/4)[r(n) + r(3n)/3 - r(5n)/5 + ...] (§26.4.1.1)
Catalog now covers 25 chapters; 129 gems total.
Note: ch26 memory label was "Infrared Systems" — actual chapter is "Evaluation Phase Optical Tests" (corrected).

## 2026-08-24 (session 10, ch25)

### Lost Gems — ch25 Production Phase Optical Tests (analysis/LOST_GEMS_CATALOG.md)
6 new gems extracted (GEM-120 to GEM-125):
- GEM-120: Always specify exact focal length reference point — two documented real failures from ambiguity
- GEM-121: Newton's fringes 7-rule interpretation guide (contour map, pressure test, λ/2 per fringe, λ/4 bright-to-dark)
- GEM-122: Interferometric flatness spec: Newton fringes/inch; h/5 practical sensitivity limit; "uniform color" for highest grade
- GEM-123: Foucault test sensitivity — 10⁻⁵ rad slope errors visible; 10⁻⁷ rad detectable on long focal-length mirrors
- GEM-124: Star test zonal rule — bright ring inside focus = positive zonal; outside = negative; inspect out-of-focus with several rings
- GEM-125: Coma causes asymmetric boresight error; astigmatism does not — critical distinction for targeting/tracking systems
Catalog now covers 24 chapters; 125 gems total.
Note: ch25 memory label was "Photographic Systems" — actual chapter is "Production Phase Optical Tests" (corrected).

## 2026-08-24 (session 10, continued again)

### Lost Gems — ch24 Design Phase Optical Tests (analysis/LOST_GEMS_CATALOG.md)
3 new gems extracted (GEM-117 to GEM-119):
- GEM-117: Seidel aberration tolerances from Rayleigh λ/4 criterion (spherical, coma, astigmatism, focal range)
- GEM-118: Tolerance calibration caveats — spherical too loose for fast systems (4× factor); coma must → 0; astigmatism 2× too tight
- GEM-119: Spot diagram only valid for aberration-limited systems; compare to Airy disk to decide regime
Catalog now covers 23 chapters; 119 gems total.
Note: ch24 memory label was "Eye and Vision" — actual chapter is "Design Phase Optical Tests" (corrected).

## 2026-08-24 (session 10, continued)

### Lost Gems — ch23 Microscope Optics (analysis/LOST_GEMS_CATALOG.md)
8 new gems extracted (GEM-109 to GEM-116):
- GEM-109: Max useful magnification = 1000 × NA (rule of thumb)
- GEM-110: Resolution limit d = λ / (NA_obj + NA_cond); matched condenser doubles resolution vs coherent
- GEM-111: Kohler illumination required for photomicrography; critical illumination for low-power visual only
- GEM-112: Achromat objective construction recipe by NA (1 doublet to NA 0.25; 4-group needed at NA 1.25)
- GEM-113: Huygenian vs Ramsden eyepiece selection — Ramsden when reticle needed; compensating for apochromats
- GEM-114: Darkfield NA constraint — obj NA must be < inner cone NA (0.7); funnel stop required above NA 0.7
- GEM-115: Phase (qualitative, haloes) vs interference (quantitative, no haloes) microscopy decision guide
- GEM-116: Fluorescence: use achromatic objectives + Abbe condensers — apochromats often contain fluorescent glass
Catalog now covers 22 chapters; 116 gems total.
Note: ch23 catalog label was "Optical Instruments" — actual chapter is "Microscope Optics" (corrected).

## 2026-08-24 (session 10)

### Lost Gems — ch22 Infrared Optical Design (analysis/LOST_GEMS_CATALOG.md)
6 new gems extracted (GEM-103 to GEM-108):
- GEM-103: IR resolution degradation rule — 5× coarser at 3 µm, 18× coarser at 10 µm (vs 0.56 µm visible)
- GEM-104: Ordinary glass cutoff at 2.7 µm; flints transmit slightly better than crowns near the edge
- GEM-105: Near-IR achromatization (0.8–1.2 µm) requires ~2× stronger element powers than visible (V-values converge)
- GEM-106: Mid-IR Abbe number ratio up to 46:1 (Si+negative in 3.5–5.5 µm) vs 2.4:1 max in visible
- GEM-107: Optical immersion multiplies detector light-receiving ability by n²; hemisphere geometry realizes it fully
- GEM-108: Place IR photoconductive detector at aperture image, not focal plane, to average out non-uniform responsivity
Catalog now covers 21 chapters; 108 gems total.
Note: ch22 OCR/memory label was "Optical Cements" — actual chapter is "Infrared Optical Design" (corrected in catalog and memory).

## 2026-08-23 (session 9)

### Lost Gems — ch03 Considerations of Physical Optics (analysis/LOST_GEMS_CATALOG.md)
1 new gem extracted (GEM-102):
- GEM-102: Interferometer fringe width h = λ/(nθ); HeNe at 1 mrad → 0.633 mm/fringe
Ch03 is ~95% wave theory derivation; only §3.3.3.2 yields an actionable gem.
Catalog now covers 20 chapters; 102 gems total.

## 2026-08-23 (session 8)

### Lost Gems — ch21 Coating of Optical Surfaces (analysis/LOST_GEMS_CATALOG.md)
6 new gems extracted (GEM-096 to GEM-101):
- GEM-096: R_min formula for non-ideal monolayer AR — [(n₁²-n₀n₂)/(n₁²+n₀n₂)]²; MgF₂ on glass → 1.26% min
- GEM-097: TiO₂ inner layer thickness ≈ 0.043λ (15.5°) is universal across all ordinary glasses in TiO₂/MgF₂ bilayer AR
- GEM-098: Jupnik's equivalent bilayer — replace unavailable index n₃ with bilayer satisfying n'₁·n'₂ = n₃²
- GEM-099: Single-layer AR at 45° fails on crown glass — rugged films below n=1.30 unavailable; need n≈1.2
- GEM-100: HR stack rule — maximize n_H/n_L; (HL)⁵H with ZnS/MgF₂ exceeds silver (T=0.54%)
- GEM-101: Thin-film FP filter half-width formula |Δλ|=(λ₀/ν)·(1-|ρ₀|²)/(π|ρ₀|); ZnS/MgF₂ example: 36.2 Å at ν=1
Catalog now covers 19 chapters; 101 gems total.
Note: ch21 is ~80% theoretical EM derivation (Maxwell, Fresnel, matrix, quaternion methods); practical gems concentrate in §21.6–21.10.

## 2026-08-23 (session 7)

### Lost Gems — ch20 Applications of Thin Film Coatings (analysis/LOST_GEMS_CATALOG.md)
10 new gems extracted (GEM-086 to GEM-095):
- GEM-086: Fresnel surface reflectivity formula + values for common glasses (crown 4.1%, Ge 36.4%)
- GEM-087: Ideal single-layer AR: n_film = √(n₀·ns); MgF₂ (n=1.38) as practical compromise
- GEM-088: Silver BS absorbs 1/3; dielectric BS absorbs <1%
- GEM-089: Thin film coating materials reference table (n, transparency range for 14 materials)
- GEM-090: Film cracking limit: MgF₂ and CeO₂ crack above ~1 µm physical thickness
- GEM-091: Half-wave absentee layer — λ/2 film contributes nothing to reflectivity at that λ
- GEM-092: Quarter-half-quarter (QHQ) triple AR: R < 0.5% across full visible
- GEM-093: Quarter-wave stack high-reflectance zone width: Δg = (2/π)arcsin|(nH-nL)/(nH+nL)|
- GEM-094: Overcoated Al mirrors: bare Al ~90%, 6-layer dielectric overcoat ~99.4%
- GEM-095: FP filter angle-tuning and collimation rules (blue shift, f/2 offset = 2 nm)
Catalog now covers 18 chapters; 95 gems total.

## 2026-08-23 (session 6)

### Lost Gems — ch19 Optics for Missile Tracking (analysis/LOST_GEMS_CATALOG.md)
7 new gems extracted (GEM-079 to GEM-085):
- GEM-079: Paraboloid coma-limited field formula: v (in) = (f/#)^2 / 25 (verified by 3 data points)
- GEM-080: Reflective vs. refractive crossover at ~12-inch (300 mm) aperture
- GEM-081: Clark lens / air-spaced doublet corrects zonal spherical AND sphero-chromatism
- GEM-082: Aspheric at stop corrects spherical only — off-axis Seidel coefficients unchanged
- GEM-083: Concave mirror Petzval is opposite sign to lens (P = 2Nc) — enables flat-field catadioptrics
- GEM-084: Schmidt tube = 2x focal length; oblate spheroid variant halves tube to 1x focal length
- GEM-085: Cassegrain secondary magnification typically 4x; paraboloid-hyperboloid is standard coma-free form
Catalog now covers 17 chapters; 85 gems total.
Note: ch19 OCR label was "Optical Coatings (intro)" — actual chapter is "Optics for Missile Tracking" (corrected).

## 2026-08-23 (session 5)

### Lost Gems — ch18 Atmospheric Optics (analysis/LOST_GEMS_CATALOG.md)
9 new gems extracted (GEM-070 to GEM-078):
- GEM-070: Visual filter decision table — 3-case rule for sky backgrounds (white/dark target, blue/white sky)
- GEM-071: Large particle (10–40 µm) extinction is filter-independent ±10% from 0.4–5.5 µm
- GEM-072: Wratten filter numbers for upward-looking photography (W25/29 red, W47 blue)
- GEM-073: Yellow/orange filter is standard compromise for aerial haze (red too dark on vegetation)
- GEM-074: 2-inch / 10× / 15° immunity rule — small instruments not affected by turbulence
- GEM-075: Smaller aperture can outresolve larger in poor seeing (Hale 200" actual 2.5" vs 0.04" theory)
- GEM-076: Use ND filters not aperture stops for brightness reduction in scatter conditions
- GEM-077: 1 PSIA vacuum (not hard vacuum) restores image quality degraded by tube currents
- GEM-078: >80% of solar energy is below 1 µm — white paint needs VIS reflectivity, not just IR
Catalog now covers 16 chapters; 78 gems total.
Note: ch18 OCR title was "Optical Fabrication" — actual chapter is "Atmospheric Optics" (corrected in catalog table).

## 2026-08-23 (session 4)

### Lost Gems continued — ch16 Applications of Physical Optics (analysis/LOST_GEMS_CATALOG.md)
7 new gems extracted (GEM-063 to GEM-069):
- GEM-063: λ/2 per fringe — fundamental interferometric rule; includes Newton's rings r_v=√(vλR)
- GEM-064: OPD formula δ = 2n·d·cos(i') — cornerstone of all thin-film optics
- GEM-065: Phase change on reflection — π at denser medium, 0 at rarer; common sign-error source
- GEM-066: Haidinger fringe blink counting — eye-only parallelism test; count blinks as plate moves
- GEM-067: Fringe shift = film thickness t = (Δx/h)·(λ/2) — thin film measurement without profilometer
- GEM-068: Rayleigh resolution 0.61λ/NA and Sparrow physical limit 0.47λ/NA
- GEM-069: Depth of focus ∝ λ/NA² (not NA⁻¹) — diffraction-derived; NA² scaling is commonly forgotten
Catalog now covers 15 chapters; 69 gems total.

## 2026-08-23 (session 3)

### Lost Gems continued — ch15 Complete Telescope (analysis/LOST_GEMS_CATALOG.md)
6 new gems extracted (GEM-057 to GEM-062):
- GEM-057: Erfle eye relief ≈ 0.8 × focal length (derive f_min directly from eye relief spec)
- GEM-058: Porro prism reduced path length L' = 4A/n (key formula for first-order telescope layout)
- GEM-059: 50% vignetting at field edge acceptable for prism sizing
- GEM-060: Telescope design sequence — correct eyepiece (astigmatism + lateral color) first, then objective
- GEM-061: Wide-angle exit pupil — large exit pupil prevents iris rollout when eye rotates to field edge
- GEM-062: Edge-of-field philosophy — ±12° acute vision zone; wide-but-blurry beats narrow-but-sharp
Catalog now covers 14 chapters; 62 gems total.

## 2026-08-23 (session 2)

### Lost Gems continued — ch14 Eyepieces (analysis/LOST_GEMS_CATALOG.md)
7 new gems extracted (GEM-050 to GEM-056):
- GEM-050: Eye relief ≥10–12 mm minimum (hard mechanical constraint for all visual instruments)
- GEM-051: Apparent field 30°–60° anti-tunnel-vision rule
- GEM-052: Don't redesign eyepieces from scratch — modify a classic form
- GEM-053: Eyepiece type selection table (Huygenian → Wild; eye relief, field, Petzval y, lateral color)
- GEM-054: Huygenian eyepiece incompatible with reticles (field stop behind eye lens → colored fringes)
- GEM-055: Prism system compensates eyepiece lateral color — design them together, don't over-correct eyepiece alone
- GEM-056: Erfle first-surface proximity trap — moving focal plane close to first surface puts dust in focus
Catalog now covers 13 chapters; 56 gems total.

## 2026-08-23

### Layer 1 cleanup (pipeline/cleanup_ocr.py)
Removed 11,750 lines of noise from all 29 chapters: MIL-HDBK header variants (235),
page footers (277), decorative rule artifacts (7,299), gutter prefixes i /| (3,333),
42 equation placeholders flagged as noise. Backups in ocr_output/backup/ (gitignored).

### Quality spot-check (verification/SPOT_CHECK_REPORT.md)
VLM vs Tesseract blind comparison on ch17 (text-heavy), ch08 (math-moderate),
ch21 (math-intensive). Prose quality 82-90% across all types. All equations flagged,
none passed silently. Fixed confirmed OCR error: ch21 "10.5.2" -> "21.5.2 Quaternions".
Systematic issues documented: TABLE false positives from horizontal rules, header
variant stripping misses, Greek symbols mangled (Sigma->Z, sigma->o, nu-bar->p).

### Lost Gems continued — ch04, ch05, ch07, ch09 (analysis/LOST_GEMS_CATALOG.md)
17 new gems extracted (GEM-017 to GEM-033):
- ch04 Visual Optics (GEM-017–024): diopter range rule, exit pupil sizing, Stiles-Crawford
  effect, visual acuity numbers+vernier, night myopia, binocular tolerances, dark adaptation
  red-light trick, age illumination doubling rule
- ch05 Ray Tracing (GEM-025–026): PR method (fastest hand meridional trace, 40-60 s/surface),
  graphical Snell's law two-circle construction
- ch07 Thin Lens Systems (GEM-027–029): magnifier relaxed-eye rule, f-number from paraxial
  angle change, symmetric field-lens lateral color cancellation condition
- ch09 Lens Design (GEM-030–033): lens bending decoupling, 2-5 wave diffraction check,
  geometric+diffraction quadrature spot estimate, pre-computer two-step design heuristic
Catalog now covers 8 chapters; 33 gems total.

### Lost Gems catalog started (analysis/LOST_GEMS_CATALOG.md)
16 gems extracted from ch17, ch06, ch08:
- GEM-001: Normal-incidence reflection formula R=((n-1)/(n+1))^2
- GEM-002: Separating reflection loss from bulk absorption (spectrophotometer data)
- GEM-003: Metal mirror selection by wavelength region (Al/Ag/Au/Cu/Rh)
- GEM-004: When wavelength variation of R can be ignored
- GEM-005: CTE matching rule for cemented/mounted optics
- GEM-006: Hardness vs environment tradeoff for material selection
- GEM-007: Plastics vs glass weight savings — when the tradeoff is real
- GEM-008: UV material quick-reference table (NaCl, KBr, LiF, CaF2, fused quartz, BaF2)
- GEM-009: Paraxial ray trace format (two-constant table method)
- GEM-010: Two-ray rule — any paraxial ray as linear combination of two traced rays
- GEM-011: Graphical ray tracing accuracy limit (~1%)
- GEM-012: Spot diagram as primary ray-trace quality metric
- GEM-013: Third-order spherical aberration sign convention
- GEM-014: Stop shift equations — changing stop without re-optimizing
- GEM-015: Optical invariant (Smith-Helmholtz/Lagrange) — conservation law of paraxial optics
- GEM-016: "Easiest operation first" rule for reverse ray tracing

### Lost Gems continued — ch10, ch11, ch12, ch13 (analysis/LOST_GEMS_CATALOG.md)
16 new gems extracted (GEM-034 to GEM-049):
- ch10 Triplet Design (GEM-034–038): negative lens 1/10-diameter rule, identical-crown-glass
  rule, deliberate 3rd/5th-order balance, "boxing in" graphical solve, L/R solutions + R≈1
- ch11 Telescope Objectives (GEM-039–042): Fraunhofer vs Steinheil orientation, Petzval 1/MP²
  scaling, zonal aberration diffraction-limit formula, air-spacing for zonal correction
- ch12 Relay Systems (GEM-043–046): secondary-color/field-curvature tradeoff, double-relay
  6× Petzval penalty, don't stop down free field, 50% Petzval negligibility threshold
- ch13 Mirror/Prism Systems (GEM-047–049): even/odd parity rule, 2θ mirror rotation rule,
  unfolding principle (any mirror system = equivalent refracting system)
Catalog now covers 12 chapters; 49 gems total.

### Next session priorities
1. Continue Lost Gems mining: ch14 (eyepieces), ch15, ch16, ch18+
2. VLM figure/table description pass (on-demand as gems reference figures)
3. LaTeX equation pass (deferred — high effort, needs expert review)


## 2026-09-06 (session — parallel burst via Bridge)

### Parallel full-VLM pass ch12-15 (4 Claude Sonnet 5 sessions)
- ch12 Lens Relay Systems: OCR refreshed, +3 gems (12.5-12.7, now 12.1-12.7), validate prompt written
- ch13 Mirror and Prism Systems: OCR refreshed (52 pages), +6 gems (13.4-13.9, now 13.1-13.9), validate prompt written
- ch14 Eyepieces: OCR refreshed, +3 gems (14.8-14.10, now 14.1-14.10), validate prompt written
- ch15 Complete Telescope: OCR refreshed (no new gems), validate prompt written
- Committed a8fa248. Next pending: ch16.

## 2026-09-12 (session — validation backlog cleared, ch19 + ch16-26)

### Repo hygiene
- Restored `analysis/EDITORIAL_NOTES.md` (160 lines accidentally emptied, uncommitted)
- Dropped superseded ch12 validate-prompt draft (20260830 version; 20260906 already validated)
- Committed the ch19 full VLM pass that was sitting uncommitted (LaTeX equations, gems 19.8-19.9)
- Committed the ch19 validate-prompt file itself, which had been written but never added to git

### Scientific validation, ch19 + ch16-26 (self-validated: Claude acted as both primary
VLM pass author and independent validator, since no external-LLM round-trip was available
this session — see exchanges/VALIDATOR_SYSTEM_PROMPT.md for the role definition used)
- ch19: 2 QUERY (paraboloid coma-field exponent EQ-A/gem 19.1, Schmidt neutral-zone EQ-E/19.8), rest PASS
- ch16-18: gem 17.2's waterwhite worked example corrected (wrong thickness + T value; final β/conclusion were already right); rest PASS with minor QUERYs (Sparrow coefficient, Hale/solar-spectrum historical figures)
- ch20-22: **3 confirmed arithmetic errors fixed** — gem 20.1 reflectance table (n=1.70 row), gem 20.8 HR-stack bandwidth (2 IR material-pair rows), gem 21.5's transcribed closed-form formula (worked answer was already correct; formula as written wasn't)
- ch23-25: all PASS, one QUERY noted (24.1 focal-range formula: factor-of-2 ambiguity between one-sided tolerance and full ± span, not resolved without the scan)
- ch26: all PASS, including verification of Coltman's square-wave/sine-wave MTF formula
- ch16-18 and ch20-26 still have 0 LaTeX equations (deferred per plan, not done this session)
- All 10 previously-pending chapters (16,17,18,20-26) plus ch19 now have validate prompt +
  response pairs in `exchanges/`, committed in 5 batches

