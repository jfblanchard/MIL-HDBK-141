# Validation Response — Chapter 24: Design Phase Optical Tests

**Date:** 2026-09-12
**Validator:** Claude (Sonnet 5), self-validated per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`

---

### 24.1 — Seidel tolerance table and focal-range derivation
**STATUS: QUERY**
**FINDING:** The overall structure of the tolerance table (different powers of sinU'_m for different aberration orders — coma scaling as 1/sinU vs. spherical/astigmatism/field-curvature scaling as 1/sin²U) is dimensionally and physically consistent with standard OPD-to-transverse-aberration conversion theory; I can't independently re-derive each specific numeric coefficient (4, 6, ½, 1, ¼) from scratch with full confidence, so I'm not flagging them as wrong, but I can't fully confirm them either — treat these as a faithful transcription of the book's own Table pending an independent cross-check against Conrady or Kingslake's published tolerance tables.

On the "Focal range ≈ 8λ(f/#)²" derivation specifically: substituting sinU'_m=1/(2·f/#) into the stated Δf=λ/(N'sin²U'_m) (N'=1) gives Δf=4λ(f/#)², not 8λ(f/#)². This resolves cleanly, though, if "Δf" in the table is a **one-sided** tolerance and "focal range" means the full **±Δf span** (2×Δf=8λ(f/#)²) — a plausible and common convention distinction (tolerance vs. total usable range). I can't be certain which convention the source intends without checking the original page, so this is QUERY rather than FLAG; no edit made to the catalog since either interpretation is self-consistent and I'd risk introducing my own error by guessing which one the source means.

### 24.2 — Practical tolerance calibration
**STATUS: PASS**
This is empirical/historical engineering guidance from the source (not a first-principles derivation), and all three calibration notes are physically sensible: spherical aberration's higher-order OPD dependence does make the simple λ/4 tolerance progressively less protective for fast systems; driving coma to zero rather than accepting the full nominal tolerance is standard conservative visual-system practice; and astigmatism's comparatively gentle degradation of the PSF (spreading energy between two line foci rather than concentrating it into a comatic flare) makes a more generous practical tolerance plausible. No computation to independently verify; nothing implausible.

### 24.3 — Spot diagram vs. Airy disk check
**STATUS: PASS (mechanism), QUERY (worked-example wavelength)**
The decision rule (compare spot diagram RMS/diameter to the Airy disk before trusting geometric ray-trace analysis) is standard, correct optical-testing practice, and the formula cited (Airy disk diameter = 2.44λ(f/#)) is the standard circular-aperture diffraction result. In the NBS worked example, 2.44×0.55µm×3.5=4.70µm, not the headline 4.0µm figure — the catalog entry already flags this itself and attributes it to a different operating wavelength for the actual test. That's a reasonable explanation (e.g. λ≈0.47µm would reproduce 4.0µm almost exactly), but since the exact test wavelength isn't stated, I can't independently confirm it — this is already appropriately self-caveated in the existing entry, so no further correction made.

---

## Overall Assessment

Good chapter overall — all three gems represent sound, standard optical-testing practice. Two genuine QUERY items (the Δf vs. full-focal-range factor-of-2 ambiguity in 24.1, and the un-stated test wavelength behind 24.3's Airy-disk worked example) are flagged for a human/primary-source check rather than corrected, since in both cases a self-consistent non-error explanation exists and I don't want to guess wrong.
