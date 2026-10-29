# MIL-HDBK-141 Figure Audit (gemini-3.1-flash-lite-image)
- Total blocks: 529. KEPT 349 · REWRITTEN 127 · UNVERIFIED 53
- Note: UNVERIFIED = render/API failure or 'no figure on page' — needs Claude/manual check.

## Claude sanity pass (2026-09-24, `pipeline/figure_audit_sanity.py`)

Every REWRITTEN row and every 'no figure on page' row was checked against the scan (or, where
marked 'caption text', against the validated caption line in `ocr_output/`). Titles are now the
book's printed captions.

- **REWRITTEN 127** → CONFIRMED 32 (Gemini right) · RESTORED 81 (Gemini wrong, original stands) ·
  CORRECTED 14 (neither right; fixed from the scan).
- **UNVERIFIED 53** → 42 bare `needs manual extraction` placeholders, left as extraction gaps;
  the 11 'no figure on page' rows are not benign: 9 are fabricated ch05 blocks (CORRECTED) and
  2 are ch13 page-offset cases (RESTORED, figure on p.13-27).

Why Gemini went wrong (81 RESTORED):
- **ch13 page offset (60 rows):** from Fig 13.21 on, the transcription's page labels run 1-2 pages
  behind the scan, so Gemini was shown the wrong page and "corrected" titles to the figure
  printed there. Gemini's own readings of the right pages confirm the originals.
- **Display truncation:** the table cuts titles at 80 characters; several "cut off" complaints
  were about that, not the spec.

Real defects found in `ocr_output/` figure blocks (ch05/ch20/ch13 **fixed 2026-09-24**, checked
against the scan):
- **ch05:** the 21 figure blocks were fabricated past the first few numbers. The book has 13
  figures (5.1-5.13, pp. 5-1 to 5-24); 5.14-5.20 do not exist. **Fixed:** all 21 replaced by the
  13 printed figures, each placed under its scan page marker.
- **ch20:** blocks 20.54-20.56 were shifted one figure (the "20.54" block was 20.55's caption).
  **Fixed:** 20.54 added on p.20-43; p.20-44 now holds 20.55-20.58; 20.52/20.53 specs corrected
  (layer counts, H = 2.30).
- **ch13:** the first "13.52" block was the lower half of 13.51. **Fixed:** folded into 13.51;
  13.49 retitled Harting-Dove; 13.58 marked (printed "13.56", sic); blocks 13.21-13.84 now carry
  their scan page ("scan p.13-NN"). The transcript's `PAGE` markers themselves still run 1-2
  behind the scan from p.13-18 on (not changed; body structure).
- **Spec content errors (CONFIRMED rows):** 4.2, 6.2, 6.6, 6.12, 6.18, 10.10/10.11, 14.19, 20.23,
  20.24, 20.52, 20.100, 20.114, 21.18, 26.14, 26.15; see each row's note.
- **1962 original:** the Penta prism tunnel diagram (p.13-38) is printed "Figure 13.56" (sic);
  should be 13.58.

| fig | ch | page | status | title/correction | reason |
|---|---|---|---|---|---|
| None | 16 | 2 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 4 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 6 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 10 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 11 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 13 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 13 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 20 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 21 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 21 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 22 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 23 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 24 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 38 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 38 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 40 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 47 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 50 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 51 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 51 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 54 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 57 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 59 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 16 | 60 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 2 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 11 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 15 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 23 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 38 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 47 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 66 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 72 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 75 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 90 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 91 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 93 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 20 | 94 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 21 | 4 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 21 | 13 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 21 | 13 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 21 | 77 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| None | 21 | 78 | UNVERIFIED | — needs manual extraction | bare placeholder (needs manual extraction) |
| 2.1 | 02 | 2 | REWRITTEN→RESTORED | Illustration of refraction. | p.2-2; original adds 'at a plane interface' (descriptive, correct) |
| 2.2 | 02 | 2 | REWRITTEN→RESTORED | Unit vectors for ray directions. | p.2-2; original adds 'at a curved interface' (descriptive, correct) |
| 2.3 | 02 | 3 | KEPT | Figure 2.3 — Vector diagram showing relation between $\vec{S}_o$, $\vec{S}_1$, a |   |
| 2.4 | 02 | 3 | KEPT | Figure 2.4 — Illustration of reflection. Vertical surface (right side shaded, in |   |
| 2.5 | 02 | 5 | KEPT | Figure 2.5 — Schematic of a beam of white light passing through a dispersing pri |   |
| 3.1 | 03 | 2 | KEPT | Figure 3.1 — Three-dimensional diagram of a plane-polarized electromagnetic wave |   |
| 3.2 | 03 | 4 | KEPT | Figure 3.2 — Three-dimensional perspective diagram showing the propagation of a  |   |
| 3.3 | 03 | 7 | KEPT | Figure 3.3 — Two-dimensional diagram of interference between two plane wavefront |   |
| 4.1 | 04 | 2 | KEPT | Figure 4.1 — Horizontal section of the right eye. Fully labeled anatomical diagr |   |
| 4.2 | 04 | 4 | REWRITTEN→CONFIRMED | Optical constants for a "standard eye." | p.4-4; a full schematic eye (lens outer/inner n, nodal points); the spec's '(Gullstrand reduced eye)' is wrong |
| 4.3 | 04 | 6 | REWRITTEN→RESTORED | Variation of some attributes of vision with luminance. | p.4-6; spec correct, only display-truncated |
| 4.4 | 04 | 8 | KEPT | Figure 4.4 — Distribution of cones and rods across the retina (horizontal meridi |   |
| 4.5 | 04 | 8 | KEPT | Figure 4.5 — Sensitivity to just perceptable luminance across the retina. x-axis |   |
| 4.6 | 04 | 9 | KEPT | Figure 4.6 — Distribution of visual acuity across the retina expressed in degree |   |
| 4.7 | 04 | 10 | KEPT | Figure 4.7 — Threshold decrease with distance (in degrees, 0°–15°) from the fove |   |
| 4.8 | 04 | 11 | KEPT | Figure 4.8 — Photopic and Scotopic standard observer curves and chromatic aberra |   |
| 4.9 | 04 | 12 | KEPT | Figure 4.9 — A typical curve of dark adaptation. x-axis: minutes in the dark, 0– |   |
| 4.10 | 04 | 15 | KEPT | Figure 4.10 — Planes of rotation of the external eye muscles. 3D perspective dia |   |
| 4.11 | 04 | 15 | KEPT | Figure 4.11 — Monocular and binocular visual fields. Elliptical contour map show |   |
| 4.12 | 04 | 17 | KEPT | Figure 4.12 — Stereoscopic vision with disparate images. Schematic showing left  |   |
| 4.13 | 04 | 19 | KEPT | Figure 4.13 — Some age changes in vision (x-axis: age 10–80). Five stacked panel |   |
| 5.1 | 05 | 3 | UNVERIFIED→CORRECTED | A cross-section view of a photographic lens. | ch05 figure block is fabricated (not in the book); real Fig 5.1 is on p.5-1 |
| 5.2 | 05 | 4 | REWRITTEN→CORRECTED | An optical system containing a mirror. | ch05 figure block is fabricated (not in the book); real Fig 5.2 is on p.5-1; no 'ray transfer diagram' exists |
| 5.3 | 05 | 5 | UNVERIFIED→CORRECTED | Diagram showing "folding out" of an optical system containing a mirror. | ch05 figure block is fabricated (not in the book); real Fig 5.3 is on p.5-2 |
| 5.4 | 05 | 6 | REWRITTEN→CORRECTED | Cross-sectional view of a centered optical system. | ch05 figure block is fabricated (not in the book); real Fig 5.4 is on p.5-4; Gemini's 5.6 is the next figure (p.5-6) |
| 5.5 | 05 | 7 | REWRITTEN→CORRECTED | Right-handed coordinate axes. | ch05 figure block is fabricated (not in the book); real Fig 5.5 is on p.5-4 |
| 5.6 | 05 | 8 | UNVERIFIED→CORRECTED | Diagram of a skew ray in space between the j₋₁ surface and the jth surface. | ch05 figure block is fabricated (not in the book); real Fig 5.6 is on p.5-6 |
| 5.7 | 05 | 9 | UNVERIFIED→CORRECTED | Some properties of a spherical surface. | ch05 figure block is fabricated (not in the book); real Fig 5.7 is on p.5-7 |
| 5.8 | 05 | 10 | REWRITTEN→CORRECTED | Determination of n₋₁ cos I. | ch05 figure block is fabricated (not in the book); real Fig 5.8 is on p.5-7 |
| 5.9 | 05 | 10 | REWRITTEN→CONFIRMED | Triangle for the law of refraction. | ch05 figure block is fabricated (not in the book); real Fig 5.9 is on p.5-10, as Gemini read |
| 5.10 | 05 | 11 | UNVERIFIED→CORRECTED | Diagram of a skew ray in space between the j₋₁ surface and the jth aspheric surface. | ch05 figure block is fabricated (not in the book); real Fig 5.10 is on p.5-14 |
| 5.11 | 05 | 12 | REWRITTEN→CORRECTED | Step-wise approximations from tangent sphere intersection, point 0, to final intersection point. | ch05 figure block is fabricated (not in the book); real Fig 5.11 is on p.5-15 |
| 5.12 | 05 | 12 | REWRITTEN→CORRECTED | Ray tracing by the PR method. | ch05 figure block is fabricated (not in the book); real Fig 5.12 is on p.5-23 |
| 5.13 | 05 | 13 | REWRITTEN→CORRECTED | Transfer procedure for the PR method. | ch05 figure block is fabricated (not in the book); real Fig 5.13 is on p.5-24 (the last ch05 figure) |
| 5.14 | 05 | 14 | REWRITTEN→CORRECTED | (no Figure 5.14 in the book) | ch05 figure block is fabricated (not in the book); ch05 figures end at 5.13; the p.5-14 figure is 5.10 |
| 5.15 | 05 | 15 | REWRITTEN→CORRECTED | (no Figure 5.15 in the book) | ch05 figure block is fabricated (not in the book); the p.5-15 figure is 5.11 |
| 5.16 | 05 | 16 | UNVERIFIED→CORRECTED | (no Figure 5.16 in the book) | ch05 figure block is fabricated (not in the book); ch05 figures end at 5.13 |
| 5.17 | 05 | 16 | UNVERIFIED→CORRECTED | (no Figure 5.17 in the book) | ch05 figure block is fabricated (not in the book); ch05 figures end at 5.13 |
| 5.18 | 05 | 17 | UNVERIFIED→CORRECTED | (no Figure 5.18 in the book) | ch05 figure block is fabricated (not in the book); ch05 figures end at 5.13 |
| 5.19 | 05 | 18 | UNVERIFIED→CORRECTED | (no Figure 5.19 in the book) | ch05 figure block is fabricated (not in the book); ch05 figures end at 5.13 |
| 5.19 | 05 | 19 | REWRITTEN→CORRECTED | (no Figure 5.19 in the book) | ch05 figure block is fabricated (not in the book); p.5-19 holds Table 5.3 |
| 5.20 | 05 | 20 | REWRITTEN→CORRECTED | (no Figure 5.20 in the book) | ch05 figure block is fabricated (not in the book); p.5-20 holds Table 5.4 |
| 6.2 | 06 | 6 | REWRITTEN→CONFIRMED | Diagram illustrating the data used to compute the optical invariant. | p.6-6; only the axial ray from the object base is drawn; the spec's chief ray and Φ annotation are not in the figure |
| 6.3 | 06 | 7 | KEPT | Figure 6.3 — Three diagrams illustrating Smith-Helmholtz equations. (a) Lateral  |   |
| 6.4 | 06 | 9 | KEPT | Figure 6.4 — Rays used to find simple expressions for A and B. Shows two surface |   |
| 6.5 | 06 | 11 | KEPT | Figure 6.5 — Location of second focal point F₂, second principal plane, and seco |   |
| 6.6 | 06 | 12 | REWRITTEN→CONFIRMED | Location of first focal point, first principal point, and first focal length. | p.6-12; spec's 'principal plane' and 'second focal length' are wrong |
| 6.7 | 06 | 13 | KEPT | Figure 6.7 — Diagram showing object and image relations. Shows a general optical |   |
| 6.8 | 06 | 15 | KEPT | Figure 6.8 — Graphical construction to locate positions of nodal points. Shows a |   |
| 6.9 | 06 | 16 | KEPT | Figure 6.9 — Numerical example showing location of the cardinal points for a len |   |
| 6.10 | 06 | 20 | KEPT | Figure 6.10 — The path of rays through a mirror system. Shows a concave mirror ( |   |
| 6.11 | 06 | 21 | KEPT | Figure 6.11 — Imaging an object in a concave mirror. Shows a concave mirror at r |   |
| 6.12 | 06 | 22 | REWRITTEN→CONFIRMED | The location of the principal points, focal points, and nodal points for a single mirror system. | p.6-22; N₁N₂ at the centre of curvature, F₁F₂ at r/2, P₁P₂ at the vertex; the spec puts all six at one point |
| 6.13 | 06 | 28 | KEPT | Figure 6.13 — Under-corrected chromatic aberration of axial and oblique rays in  |   |
| 6.14 | 06 | 29 | KEPT | Figure 6.14 — Plot of y_k for F and D light versus the height y₁ of the axial pa |   |
| 6.15 | 06 | 29 | KEPT | Figure 6.15 — Plot of ȳ_k for F and D light versus the height ȳ₁ of the oblique  |   |
| 6.16 | 06 | 31 | KEPT | Figure 6.16 — Illustration of axial and lateral color correction for paraxial ra |   |
| 6.18 | 06 | 34 | REWRITTEN→CONFIRMED | P̃ versus ν_F-C for several glasses. | p.6-34 (page rotated); ν = (n_D−1)/(n_F−n_C) is the horizontal axis, P̃ the vertical; the spec swaps them |
| 6.19 | 06 | 35 | KEPT | Figure 6.19 — Transverse axial chromatic aberration for an achromatic objective  |   |
| 6.20 | 06 | 35 | KEPT | Figure 6.20 — Plot of y_k versus wavelength λ (Angstroms, 4500 to 7700) for an a |   |
| 6.21 | 06 | 37 | KEPT | Figure 6.21 — Plot shows the qualitative connection between Petzval curvature an |   |
| 6.22 | 06 | 38 | KEPT | Figure 6.22 — Location of entrance pupil and numbering of surfaces. Shows a two- |   |
| 7.1 | 07 | 2 | KEPT | Figure 7.1 — Diagrammatic illustration of a single lens magnifier. Two-panel dia |   |
| 7.2 | 07 | 5 | KEPT | Figure 7.2 — The simple microscope. Lens (a) is the relay lens. Schematic showin |   |
| 7.3 | 07 | 6 | KEPT | Figure 7.3 — Two lens cross-section sketches. (a) $f/1$ single biconvex lens: $R |   |
| 7.4 | 07 | 9 | KEPT | Figure 7.4 — The optics of a simple telescope. Two-panel diagram. Top: unaided e |   |
| 7.5 | 07 | 10 | KEPT | Figure 7.5 — An optical relay system or periscope. Schematic with Objective at l |   |
| 7.6 | 07 | 10 | KEPT | Figure 7.6 — A periscope with field lenses. Same system as Fig. 7.5 but with Fie |   |
| 7.7 | 07 | 12 | KEPT | Figure 7.7 — The Galilean telescope. Schematic with positive objective lens at l |   |
| 8.1 | 08 | 2 | KEPT | Figure 8.1 — Spot diagram of rays in the entrance pupil plane. Axes $X_1$ (horiz |   |
| 8.1 | 08 | 2 | KEPT | Figure 8.1 — Spot diagram of rays in the paraxial image plane, axes $X_k$ (horiz |   |
| 8.2 | 08 | 2 | KEPT | Figure 8.2 — Energy distribution for the image of Figure 8.1(b). Vertical axis P |   |
| 8.3 | 08 | 4 | KEPT | Figure 8.3 — Positions in the entrance pupil of selected meridional rays and ske |   |
| 8.4 | 08 | 4 | REWRITTEN→RESTORED | Sample lens used for numerical analysis. | caption text; ch08 text says the figure is 'drawn to scale from Table 6.7' (Table 8.1 gives its numbers), so Gemini's 'Table 8.1' fix is wrong |
| 8.5 | 08 | 6 | KEPT | Figure 8.5 — Meridional ray plot at $0°$. Horizontal axis $Y_1$ from $-1.5$ to $ |   |
| 8.6 | 08 | 6 | KEPT | Figure 8.6 — Diagram illustrating shift of focus relationships. Two vertical lin |   |
| 8.7 | 08 | 11 | KEPT | Figure 8.7 — Meridional ray plots, three stacked panels on fine graph paper, eac |   |
| 8.8 | 08 | 12 | KEPT | Figure 8.8 — Skew ray image coordinates ($X_k$). Printed rotated 90° on the page |   |
| 8.8 | 08 | 12 | KEPT | Figure 8.8 — Skew ray image coordinates ($Y_k - \bar{Y}_k$). Printed rotated 90° |   |
| 8.9 | 08 | 13 | KEPT | Figure 8.9 — Fractional distortion as a function of field angle. Horizontal axis |   |
| 8.10 | 08 | 13 | KEPT | Figure 8.10 — Field curves for a triplet. Vertical axis: field angle, $0°$ at bo |   |
| 8.11 | 08 | 17 | KEPT | Figure 8.11 — Application of stop shift equations. Two vertical lines near the t |   |
| 9.1 | 09 | 6 | REWRITTEN→RESTORED | Sample plot of selected ray trace data. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 9.2 | 09 | 8 | KEPT | Figure 9.2 — Energy distribution for a perfect lens. Line plot on fine graph pap |   |
| 9.3 | 09 | 9 | KEPT | Figure 9.3 — Energy distribution curves. Line plot on fine graph paper, horizont |   |
| 9.4 | 09 | 10 | KEPT | Figure 9.4 — A series of energy distribution curves. Line plot on fine graph pap |   |
| 9.5 | 09 | 10 | KEPT | Figure 9.5 — Modulation transfer curves (the caption is printed as "Figure 9.5 - |   |
| 10.1 | 10 | 1 | KEPT | Figure 10.1 — Triplet objective used to illustrate design procedure. Three separ |   |
| 10.2 | 10 | 6 | KEPT | Figure 10.2 — Diagram used to find a thin lens first order solution. Horizontal  |   |
| 10.3 | 10 | 12 | KEPT | Figure 10.3 — Glass map (nd vs. ν) for all glasses used in the 29-system triplet |   |
| 10.4 | 10 | 14 | REWRITTEN→CONFIRMED | Variation of distortion and spherical aberration with curvature c₂. | p.10-14; original title 'Third order solution curves for System 10A' is not the caption |
| 10.5 | 10 | 16 | KEPT | Figure 10.5 — 3Yk and F.D. vs c2 curves for same glass system at R=0.5, 1, 2 ove |   |
| 10.6 | 10 | 21 | KEPT | Figure 10.6 — Aberration plots for left hand solution of lenses in Table 10.8. T |   |
| 10.7 | 10 | 22 | KEPT | Figure 10.7 — Aberration plots for right hand solution of lenses in Table 10.8.  |   |
| 10.8 | 10 | 23 | KEPT | Figure 10.8 — Aberration plots for left hand solution of lenses in Table 10.9 (Σ |   |
| 10.9 | 10 | 24 | KEPT | Figure 10.9 — Aberration plots for right hand solution of lenses in Table 10.9 ( |   |
| 10.10 | 10 | 26 | REWRITTEN→CONFIRMED | Spot diagrams for left hand solution in Table 10.10. | p.10-26; two rows only (t_k = −0.02, 0); the spec's third row (t = +0.02) is not in the figure |
| 10.11 | 10 | 26 | REWRITTEN→CONFIRMED | Spot diagrams for right hand solution in Table 10.10. | p.10-26; two rows (t_k = −0.02, 0), same as 10.10 |
| 11.1 | 11 | 5 | KEPT | Figure 11.1 — Two types of doublets, both with the positive (low-dispersion) len |   |
| 11.2 | 11 | 5 | KEPT | Figure 11.2 — Doublet with the negative lens in front (same two glasses as the F |   |
| 11.3 | 11 | 11 | KEPT | Figure 11.3 — Meridional ray plot at $0°$ for a doublet lens. X-axis: $Y_1$ (ape |   |
| 11.4 | 11 | 13 | KEPT | Figure 11.4 — 11.5, 11.6 — a 3x3 grid of nine small aberration-curve plots, each |   |
| 11.7 | 11 | 14 | KEPT | Figure 11.7 — Two types of triplet solution, each a three-element lens (elements |   |
| 11.8 | 11 | 16 | REWRITTEN→RESTORED | A plot of B_c the total spherical aberration of the negative lens as a function of φ_a. | p.11-16; spec matches |
| 11.9 | 11 | 17 | REWRITTEN→RESTORED | A plot of B_c as a function of φ_a for a triplet. | p.11-17; spec matches |
| 11.10 | 11 | 20 | KEPT | Figure 11.10 — A plot of $\tilde{P}^* = \dfrac{n_F - n_D}{n_F - n_C}$ (vertical  |   |
| 11.11 | 11 | 21 | KEPT | Figure 11.11 — A plot showing tertiary spectrum: three side-by-side sub-plots sh |   |
| 11.12 | 11 | 22 | KEPT | Figure 11.12 — Plot of $\bar{Y}_k$ (vertical axis, -0.0005 to 0.0025) versus wav |   |
| 11.13 | 11 | 23 | KEPT | Figure 11.13 — Meridional ray plot at $0°$ for a triplet, two stacked panels sha |   |
| 12.1 | 12 | 1 | KEPT | Figure 12.1 — A single-relay system: ray diagram with the object plane on the le |   |
| 12.2 | 12 | 3 | KEPT | Figure 12.2 — A double-relay system: ray diagram from point A to point B spannin |   |
| 13.1 | 13 | 2 | KEPT | Figure 13.1 — Reflection from a single surface mirror: a rectangular mirror bloc |   |
| 13.3 | 13 | 3 | REWRITTEN→RESTORED | A single reflection problem. | p.13-3; S₀ does travel along +Z: M = (−½, −½, 1/√2) reflects +k into S₁ at 45° in the XY plane, as drawn. Gemini's −Z is wrong |
| 13.4 | 13 | 5 | KEPT | Figure 13.4 — Solution to the problem of Figure 13.3: a parallelogram-shaped mir |   |
| 13.7 | 13 | 8 | REWRITTEN→RESTORED | Rotation of the coordinate axes. | p.13-8; spec matches |
| 13.9 | 13 | 10 | KEPT | Figure 13.9 — The right and left-hand image: three rotated copies of the letter  |   |
| 13.10 | 13 | 10 | KEPT | Figure 13.10 — Image position and orientation in the Y-plane: a wireframe sphere |   |
| 13.12 | 13 | 11 | REWRITTEN→RESTORED | Image position and orientation in the Z-plane. | p.13-11; 'Z-plane' is printed; Gemini's 'Y-plane' is wrong |
| 13.14 | 13 | 12 | KEPT | Figure 13.14 — Image position and orientation for compound angles: four wirefram |   |
| 13.15 | 13 | 14 | REWRITTEN→RESTORED | The solid-angle image. | p.13-14; four panels (a)-(d), as the spec says |
| 13.16 | 13 | 15 | KEPT | Figure 13.16 — Reflection from two perpendicular mirrors, two views. (a) Three-d |   |
| 13.17 | 13 | 16 | KEPT | Figure 13.17 — used as a right-angle prism: a single 45°-90°-45° prism cross-sec |   |
| 13.20 | 13 | 17 | KEPT | Figure 13.20 — The Amici prism in a telescope: objective lens, followed by a 45° |   |
| 13.21 | 13 | 17 | REWRITTEN→RESTORED | The Amici prism as a double reflector. | Gemini was shown the transcription's page label; the figure is on scan p.13-18 (read there) |
| 13.23 | 13 | 18 | REWRITTEN→RESTORED | The Amici prism in telescope systems. | Gemini was shown the transcription's page label; the figure is on scan p.13-19, where Gemini itself read this caption |
| 13.25 | 13 | 18 | REWRITTEN→RESTORED | Reflections through the Porro prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-20 (read there) |
| 13.27 | 13 | 19 | REWRITTEN→RESTORED | Right-angle prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-21, where Gemini itself read this caption |
| 13.28 | 13 | 20 | REWRITTEN→RESTORED | Porro prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-22 (read there) |
| 13.30 | 13 | 21 | REWRITTEN→RESTORED | The apparent thickness of a glass block. | Gemini was shown the transcription's page label; the figure is on scan p.13-23 (read there) |
| 13.32 | 13 | 22 | REWRITTEN→RESTORED | The glass block and the convergent beam of light. | Gemini was shown the transcription's page label; the figure is on scan p.13-24, where Gemini itself read this caption |
| 13.33 | 13 | 24 | REWRITTEN→RESTORED | Porro prism system. | Gemini was shown the transcription's page label; the figure is on scan p.13-26, where Gemini itself read this caption |
| 13.34 | 13 | 24 | REWRITTEN→RESTORED | Porro prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-26, where Gemini itself read this caption |
| 13.35 | 13 | 25 | UNVERIFIED→RESTORED | Abbe prism system. | Gemini was shown the transcription's page label; the figure is on scan p.13-27, where Gemini read this caption |
| 13.36 | 13 | 25 | UNVERIFIED→RESTORED | Abbe prism system tunnel diagram. | figure is on scan p.13-27, where Gemini read this caption |
| 13.37 | 13 | 26 | REWRITTEN→RESTORED | Abbe prism, type A. | Gemini was shown the transcription's page label; the figure is on scan p.13-28, where Gemini itself read this caption |
| 13.38 | 13 | 26 | REWRITTEN→RESTORED | Abbe prism, type A, tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-28, where Gemini itself read this caption |
| 13.39 | 13 | 27 | REWRITTEN→RESTORED | Abbe prism, type B. | Gemini was shown the transcription's page label; the figure is on scan p.13-29, where Gemini itself read this caption |
| 13.40 | 13 | 27 | REWRITTEN→RESTORED | Abbe prism, type B, tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-29, where Gemini itself read this caption |
| 13.41 | 13 | 28 | REWRITTEN→RESTORED | Leman prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-30, where Gemini itself read this caption |
| 13.42 | 13 | 28 | REWRITTEN→RESTORED | Leman prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-30, where Gemini itself read this caption |
| 13.43 | 13 | 29 | REWRITTEN→RESTORED | Amici prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-31, where Gemini itself read this caption |
| 13.44 | 13 | 29 | REWRITTEN→RESTORED | Amici prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-31, where Gemini itself read this caption |
| 13.45 | 13 | 30 | REWRITTEN→RESTORED | Schmidt prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-32, where Gemini itself read this caption |
| 13.46 | 13 | 30 | REWRITTEN→RESTORED | Schmidt prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-32, where Gemini itself read this caption |
| 13.47 | 13 | 31 | REWRITTEN→RESTORED | Right-angle prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-33 (read there) |
| 13.48 | 13 | 31 | REWRITTEN→RESTORED | Right-angle prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-33 (read there) |
| 13.49 | 13 | 32 | REWRITTEN→RESTORED | Harting-Dove prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-34, where Gemini itself read this caption; printed name is 'Harting-Dove' |
| 13.50 | 13 | 32 | REWRITTEN→RESTORED | Dove prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-34, where Gemini itself read this caption |
| 13.51 | 13 | 33 | REWRITTEN→RESTORED | Double Dove prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-35 (read there) |
| 13.52 | 13 | 33 | REWRITTEN→CORRECTED | (lower half of Figure 13.51, mislabeled 13.52) | p.13-35; the orthographic hexagonal section and dimension data belong to Fig 13.51; the next block is the real 13.52 |
| 13.52 | 13 | 33 | REWRITTEN→RESTORED | Double Dove prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-35 (read there) |
| 13.53 | 13 | 34 | REWRITTEN→RESTORED | Pechan prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-36, where Gemini itself read this caption |
| 13.54 | 13 | 34 | REWRITTEN→RESTORED | Pechan prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-36, where Gemini itself read this caption |
| 13.55 | 13 | 35 | REWRITTEN→RESTORED | Reversion prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-37, where Gemini itself read this caption |
| 13.56 | 13 | 35 | KEPT | Figure 13.56 — Reversion prism tunnel diagram: the two cemented elements shown u |   |
| 13.57 | 13 | 36 | REWRITTEN→RESTORED | Penta prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-38 (read there) |
| 13.58 | 13 | 36 | REWRITTEN→RESTORED | Penta prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-38 (read there); 1962 ORIGINAL (sic): printed as 'Figure 13.56' (duplicate of the reversion-prism number), should be 13.58 |
| 13.59 | 13 | 37 | REWRITTEN→RESTORED | The Wollaston prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-39, where Gemini itself read this caption |
| 13.60 | 13 | 37 | REWRITTEN→RESTORED | The Wollaston prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-39, where Gemini itself read this caption |
| 13.61 | 13 | 38 | REWRITTEN→RESTORED | A Carl Zeiss prism system. | Gemini was shown the transcription's page label; the figure is on scan p.13-40 (read there) |
| 13.62 | 13 | 38 | REWRITTEN→RESTORED | Carl Zeiss prism system tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-40 (read there) |
| 13.63 | 13 | 39 | REWRITTEN→RESTORED | A Goerz prism system. | Gemini was shown the transcription's page label; the figure is on scan p.13-41, where Gemini itself read this caption |
| 13.64 | 13 | 39 | REWRITTEN→RESTORED | A Goerz prism system tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-41, where Gemini itself read this caption |
| 13.65 | 13 | 40 | REWRITTEN→RESTORED | An ocular prism by Zeiss. | Gemini was shown the transcription's page label; the figure is on scan p.13-42, where Gemini itself read this caption |
| 13.66 | 13 | 41 | REWRITTEN→RESTORED | A Barr and Stroud ocular prism. | Gemini was shown the transcription's page label; the figure is on scan p.13-43 (read there) |
| 13.67 | 13 | 42 | REWRITTEN→RESTORED | A Zeiss coincidence prism system. | Gemini was shown the transcription's page label; the figure is on scan p.13-44, where Gemini itself read this caption |
| 13.69 | 13 | 43 | REWRITTEN→RESTORED | A Carl Zeiss binocular-ocular prism system. | Gemini was shown the transcription's page label; the figure is on scan p.13-45, where Gemini itself read this caption |
| 13.70 | 13 | 43 | REWRITTEN→RESTORED | A Zeiss binocular-ocular prism tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-45, where Gemini itself read this caption |
| 13.71 | 13 | 44 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 1. | Gemini was shown the transcription's page label; the figure is on scan p.13-46, where Gemini itself read this caption |
| 13.72 | 13 | 44 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 1 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-46, where Gemini itself read this caption |
| 13.73 | 13 | 45 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 2. | Gemini was shown the transcription's page label; the figure is on scan p.13-47, where Gemini itself read this caption |
| 13.74 | 13 | 45 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 2 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-47, where Gemini itself read this caption |
| 13.75 | 13 | 46 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 3. | Gemini was shown the transcription's page label; the figure is on scan p.13-48, where Gemini itself read this caption |
| 13.76 | 13 | 46 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 3 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-48, where Gemini itself read this caption |
| 13.77 | 13 | 47 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 4. | Gemini was shown the transcription's page label; the figure is on scan p.13-49, where Gemini itself read this caption |
| 13.78 | 13 | 47 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 4 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-49, where Gemini itself read this caption |
| 13.79 | 13 | 48 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 5. | Gemini was shown the transcription's page label; the figure is on scan p.13-50, where Gemini itself read this caption |
| 13.80 | 13 | 48 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 5 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-50, where Gemini itself read this caption |
| 13.81 | 13 | 49 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 6. | Gemini was shown the transcription's page label; the figure is on scan p.13-51 (read there) |
| 13.82 | 13 | 49 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 6 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-51 (read there) |
| 13.83 | 13 | 50 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 7. | Gemini was shown the transcription's page label; the figure is on scan p.13-52 (read there) |
| 13.84 | 13 | 50 | REWRITTEN→RESTORED | Frankford Arsenal prism No. 7 tunnel diagram. | Gemini was shown the transcription's page label; the figure is on scan p.13-52 (read there) |
| 14.1 | 14 | 2 | REWRITTEN→RESTORED | Huygenian eyepiece. Distances in cm. | p.14-2; spec's lens order is right (eye lens by the exit pupil, both plano-convex, plane sides to the eye), matching Table 14.1 |
| 14.2 | 14 | 3 | KEPT | Figure 14.2 — Meridional and skew fans for the Huygenian eyepiece. Three stacked |   |
| 14.3 | 14 | 3 | KEPT | Figure 14.3 — Field, distortion, and lateral color curves for the Huygenian eyep |   |
| 14.4 | 14 | 4 | KEPT | Figure 14.4 — Ramsden eyepiece, cross-section. Exit pupil at far left, 1.187 cm  |   |
| 14.5 | 14 | 5 | KEPT | Figure 14.5 — Meridional and skew fans for the Ramsden eyepiece. Same layout as  |   |
| 14.6 | 14 | 5 | KEPT | Figure 14.6 — Field, distortion, and lateral color curves for the Ramsden eyepie |   |
| 14.7 | 14 | 6 | REWRITTEN→RESTORED | Kellner eyepiece. Distances in cm. | p.14-6; Gemini's 'field then eye' order is wrong. Spec nits: the eye-side doublet is a 617366 flint meniscus then a 541599 biconvex crown; '0.705 cm wide' is the exit-pupil distance |
| 14.8 | 14 | 7 | KEPT | Figure 14.8 — Meridional and skew fans for the Kellner eyepiece. Same layout as  |   |
| 14.9 | 14 | 7 | KEPT | Figure 14.9 — Field, distortion, and lateral color curves for the Kellner eyepie |   |
| 14.10 | 14 | 8 | KEPT | Figure 14.10 — Orthoscopic eyepiece, cross-section. Exit pupil at far left, 2.06 |   |
| 14.11 | 14 | 9 | KEPT | Figure 14.11 — Meridional and skew fans for the orthoscopic eyepiece. Same layou |   |
| 14.12 | 14 | 9 | KEPT | Figure 14.12 — Field, distortion, and lateral color curves for the orthoscopic e |   |
| 14.13 | 14 | 10 | KEPT | Figure 14.13 — Symmetrical (Plössl) eyepiece, cross-section. Exit pupil at far l |   |
| 14.14 | 14 | 11 | KEPT | Figure 14.14 — Meridional and skew fans for the symmetrical eyepiece. Same layou |   |
| 14.15 | 14 | 11 | KEPT | Figure 14.15 — Field, distortion, and lateral color curves for the symmetrical e |   |
| 14.16 | 14 | 12 | KEPT | Figure 14.16 — Berthele eyepiece, cross-section. Exit pupil at far left, 1.743 c |   |
| 14.17 | 14 | 13 | KEPT | Figure 14.17 — Meridional and skew fans for the Berthele eyepiece. Same layout a |   |
| 14.18 | 14 | 13 | KEPT | Figure 14.18 — Field, distortion, and lateral color curves for the Berthele eyep |   |
| 14.19 | 14 | 14 | REWRITTEN→CONFIRMED | Erfle eyepiece. Distances in cm. | p.14-14; Table 14.7 is 3 groups / 5 elements (doublet, singlet, doublet); the spec's 'five lens groups, six elements' is wrong |
| 14.20 | 14 | 15 | KEPT | Figure 14.20 — Meridional and skew fans for the Erfle eyepiece. Same layout as F |   |
| 14.21 | 14 | 15 | KEPT | Figure 14.21 — Field, distortion, and lateral color curves for the Erfle eyepiec |   |
| 14.22 | 14 | 16 | KEPT | Figure 14.22 — Modified Erfle eyepiece, cross-section. Exit pupil at far left, 1 |   |
| 14.23 | 14 | 17 | KEPT | Figure 14.23 — Meridional and skew fans for the modified Erfle eyepiece. Same la |   |
| 14.24 | 14 | 17 | KEPT | Figure 14.24 — Field, distortion, and lateral color curves for the modified Erfl |   |
| 14.25 | 14 | 18 | KEPT | Figure 14.25 — Wild eyepiece, cross-section. Exit pupil at far left, 1.895 cm to |   |
| 14.26 | 14 | 19 | KEPT | Figure 14.26 — Meridional and skew fans for the Wild eyepiece. Same layout as Fi |   |
| 14.27 | 14 | 19 | KEPT | Figure 14.27 — Field, distortion, and lateral color curves for the Wild eyepiece |   |
| 15.1 | 15 | 2 | KEPT | Figure 15.1 — Diagram illustrating positioning of Porro prism system in telescop |   |
| 15.2 | 15 | 3 | KEPT | Figure 15.2 — Scale drawing of the objective. Cross-sectional profile view of a  |   |
| 15.3 | 15 | 4 | KEPT | Figure 15.3 — Two-panel diagram of an eye viewing through an exit pupil. Panel ( |   |
| 15.4 | 15 | 5 | KEPT | Figure 15.4 — Skew ray aberration plot. Three stacked strip-chart panels, one pe |   |
| 15.5 | 15 | 6 | REWRITTEN→RESTORED | Tangential rays. | p.15-6; spec is accurate (one D curve plus F and C points per oblique panel) |
| 15.6 | 15 | 7 | KEPT | Figure 15.6 — Three-panel field-performance chart, all sharing a common vertical |   |
| 16.3 | 16 | 6 | KEPT | Figure 16.3 — notation for the Twyman-Green interferometer: pinhole H
(half-angl |   |
| 16.4 | 16 | 10 | KEPT | Figure 16.4 — Young's pinhole interferometer coordinate diagram: pinhole H on
th |   |
| 16.5 | 16 | 12 | KEPT | Figure 16.5 — Lloyd's interferometer: actual pinhole/slit H1 sits a distance s
a |   |
| 16.8 | 16 | 14 | KEPT | Figure 16.8 — the dielectric plate as an interferometer: incident ray AB
(angle  |   |
| 16.9 | 16 | 16 | REWRITTEN→RESTORED | The parallel plate interferometer with nearby light source S. | Gemini itself says the caption matches |
| 16.10 | 16 | 18 | KEPT | Figure 16.10 — arrangement for observing Haidinger's fringes: extended
monochrom |   |
| 16.17 | 16 | 27 | KEPT | Figure 16.17 — representation of complex numbers in the complex Z-plane
(Z = X + |   |
| 16.18 | 16 | 29 | KEPT | Figure 16.18 — convention for the transmitted beam in a plate or Fabry-Perot
int |   |
| 16.19 | 16 | 31 | KEPT | Figure 16.19 — plot of transmitted
energy density W vs. phase α, showing sharp A |   |
| 16.19 | 16 | 31 | KEPT | Figure 16.19 — the sharpness quality of multiple beam interference fringes: W
vs |   |
| 16.20 | 16 | 33 | KEPT | Figure 16.20 — simple parallel plate interferometer: extended monochromatic
sour |   |
| 16.21 | 16 | 33 | KEPT | Figure 16.21 — the Fabry-Perot interferometer: extended monochromatic source,
co |   |
| 16.22 | 16 | 35 | KEPT | Figure 16.22 — multiple reflections in two reflecting surfaces S1 and S2
forming |   |
| 16.23 | 16 | 36 | KEPT | Figure 16.23 — method of producing and viewing transmitted multiple beam
fringes |   |
| 16.25 | 16 | 39 | KEPT | Figure 16.25 — the usual method of preparing the sample film for thickness
measu |   |
| 16.27 | 16 | 40 | KEPT | Figure 16.27 — movement of an interference fringe, x, to the position x+Δx by
in |   |
| 16.28 | 16 | 42 | KEPT | Figure 16.28 — conventional method for obtaining channeled spectra from a
source |   |
| 16.29 | 16 | 43 | REWRITTEN→CONFIRMED | A second method for producing channeled spectra. | p.16-43; the Osterberg-LaMarre attribution in the spec is supported by the text on p.16-42 |
| 16.30 | 16 | 46 | KEPT | Figure 16.30 — propagation of a plane wave in accordance with Huygens'
Principle |   |
| 16.31 | 16 | 46 | KEPT | Figure 16.31 — construction for obtaining Snell's law from Huygens' principle:
i |   |
| 17.1 | 17 | 6 | REWRITTEN→RESTORED | The range of commercially available glass, with respect to index and ν values. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
u$ values | Description is incomplete. Missing points (25, 1.74) and (30, 1.80). |
| 17.2 | 17 | 9 | KEPT | Figure 17.2 — Reflectance of freshly deposited Ag, Al, Au, Cu, Rh films vs wavel |   |
| 18.1 | 18 | 3 | KEPT | Figure 18.1 — Relative intensity vs wavelength. Line plot of the Rayleigh law $I |   |
| 19.1 | 19 | 1 | KEPT | - Tracking telescopes used with ROTI. (Courtesy of Perkin-Elmer Corp.) Photograp |   |
| 19.2 | 19 | 3 | REWRITTEN→CONFIRMED | A plot of spherical aberration of a single refracting surface. | p.19-3; original was a caption tail split off by the parser |
| 19.3 | 19 | 3 | REWRITTEN→CONFIRMED | Corrected doublet-surfaces 1 and 3 undercorrecting, surface 2 overcorrecting. | p.19-3 |
| 19.4 | 19 | 4 | KEPT | Figure 19.4 — with marginal aberration equal to zero. Three-part plot: (a) under |   |
| 19.5 | 19 | 5 | REWRITTEN→CONFIRMED | Single positive lens used in doublet of Figure 19.3. | p.19-5 |
| 19.6 | 19 | 5 | REWRITTEN→CONFIRMED | Clark lens, illustrating air spacing to increase over-correction of zonal ray. | p.19-5 |
| 19.7 | 19 | 5 | REWRITTEN→CONFIRMED | The doublet used in Figure 19.2 corrected for spherical aberration and color. | p.19-5 |
| 19.8 | 19 | 5 | REWRITTEN→CONFIRMED | Refraction of monochromatic light by the positive element of the doublet shown in Figure 19.3. | p.19-5 |
| 19.9 | 19 | 5 | REWRITTEN→CONFIRMED | Refraction and correction of monochromatic light by the Clark lens shown in Figure 19.6. | p.19-5 |
| 19.10 | 19 | 6 | KEPT | Figure 19.10 — an air space, and a rear cemented doublet consisting of a positiv |   |
| 19.11 | 19 | 6 | KEPT | Figure 19.11 — 24" high resolution lens. (JOSA Vol. 42, 7 pg. 451, S. Rosin). Op |   |
| 19.12 | 19 | 7 | KEPT | Figure 19.12 — showing vertical straight lines free from zonal bulge and sphero- |   |
| 19.13 | 19 | 7 | KEPT | Figure 19.13 — center of curvature C, and focal point F midway between V and C. |   |
| 19.14 | 19 | 8 | KEPT | Figure 19.14 — 45-degree flat diagonal mirror M, and external focal point F. |   |
| 19.15 | 19 | 9 | KEPT | Figure 19.15 — convex secondary mirror $M_2$, primary focus $F_1$, and final foc |   |
| 19.16 | 19 | 11 | REWRITTEN→CONFIRMED | Curved focal surface, concave mirror. | p.19-11 |
| 19.17 | 19 | 12 | KEPT | Figure 19.17 — correction plate not shown. Optical diagram showing spherical mir |   |
| 19.18 | 19 | 13 | REWRITTEN→CONFIRMED | Schmidt plate with parallel central section, (a); and parallel zonal section, (b). | p.19-13 |
| 19.19 | 19 | 14 | KEPT | - Ross arrangement. Diagram (not to scale; size ratio of R to M is approximately |   |
| 19.20 | 19 | 14 | KEPT | Figure 19.20 — full-aperture Schmidt corrector plate S at the entrance aperture, |   |
| 19.21 | 19 | 15 | REWRITTEN→CONFIRMED | Section view of a satellite-tracking camera. (Courtesy of Perkin Elmer Corp.) | p.19-15 |
| 19.22 | 19 | 16 | KEPT | Figure 19.22 — 24-inch aperture window/stop, 24-inch f/4.17 (100" focal length)  |   |
| 19.23 | 19 | 18 | KEPT | Figure 19.23 — 18-inch clear aperture Schmidt corrector plate S, 118-inch focal  |   |
| 19.24 | 19 | 19 | REWRITTEN→CONFIRMED | A Barlow lens. | p.19-19 |
| 19.25 | 19 | 19 | REWRITTEN→CONFIRMED | S. M. T. Optical arrangement. (Courtesy of Perkin Elmer Corp.) | p.19-19 |
| 20.3 | 20 | 3 | KEPT | Figure 20.3 — nomenclature for a multilayer stack: incident ray at angle φ in
me |   |
| 20.4 | 20 | 3 | KEPT | Figure 20.4 — a sine wave of wavelength λ (in vacuo) compared against a
layer of |   |
| 20.5 | 20 | 7 | KEPT | Figure 20.5 — vector-addition-of-amplitude reflectivity diagrams for a single
qu |   |
| 20.6 | 20 | 7 | KEPT | Figure 20.6 — stack "B" (layers 2,3,5) is equivalent to stack "A" (layers
1-5, w |   |
| 20.9 | 20 | 13 | KEPT | Figure 20.9 — a three-layer stack drawn proportional to optical thickness:
n1=4. |   |
| 20.10 | 20 | 13 | KEPT | Figure 20.10 — essential parts of a thin-film evaporator: glass bell jar over
a  |   |
| 20.11 | 20 | 13 | KEPT | Figure 20.11 — optical transmission (0-1.0) vs. wavelength (1-10 µm) for five
IR |   |
| 20.12 | 20 | 13 | KEPT | Figure 20.12 — light incident at angle φ=60° upon the front surface of a
wide-an |   |
| 20.13 | 20 | 19 | KEPT | Figure 20.13 — computed spectral reflectivity (0-0.03) vs. wavelength
(400-700 m |   |
| 20.14 | 20 | 19 | KEPT | Figure 20.14 — same as Figure 20.13 but on glass ns=1.58 — needs manual
extracti |   |
| 20.15 | 20 | 19 | KEPT | Figure 20.15 — same as Figure 20.13 but on glass ns=1.68 — needs manual
extracti |   |
| 20.18 | 20 | 23 | KEPT | Figure 20.18 — computed spectral reflectivity (0-x%) vs. g=λ0/λ (0-2.0) at
vario |   |
| 20.19 | 20 | 24 | KEPT | Figure 20.19 — computed spectral reflectivity (0-.03) vs wavelength
(400-700mµ)  |   |
| 20.20 | 20 | 24 | KEPT | Figure 20.20 — same as 20.19 but ns=1.68 — needs manual extraction |   |
| 20.21 | 20 | 24 | KEPT | Figure 20.21 — computed Rs, Rp, and Rav=1/2(Rp+Rs) vs wavelength (400-700mµ)
at  |   |
| 20.22 | 20 | 24 | KEPT | Figure 20.22 — average reflectivity (0-.30) vs angle of incidence φ (0-90°)
in a |   |
| 20.23 | 20 | 26 | REWRITTEN→CONFIRMED | Computed spectral reflectivity of a single-layer antireflection coating at φ = 0 and φ = 45°. | p.20-26; n₁ = 1.55 on As₂S₃ glass (n_s = 2.40); the spec's n₁ = 1.90 is wrong |
| 20.24 | 20 | 26 | REWRITTEN→CONFIRMED | Computed spectral reflectivity of a single-layer antireflection coating at φ = 0 and φ = 45°. | p.20-26; n₁ = 1.90 on germanium (n_s = 4.05); the spec's 'n₁ = 2.40' is wrong |
| 20.27 | 20 | 29 | KEPT | Figure 20.27 — computed Rs, Rp, Ravg vs g=λ0/λ (0-2.0) at φ=65° for a
quarter-wa |   |
| 20.28 | 20 | 29 | KEPT | Figure 20.28 — computed spectral reflectivity (0-.05) vs wavelength
(400-700mµ)  |   |
| 20.29 | 20 | 29 | KEPT | Figure 20.29 — computed spectral reflectivity (0-.05) vs wavelength
(400-700mµ,  |   |
| 20.30 | 20 | 31 | KEPT | Figure 20.30 — computed spectral reflectivity (0-.08) vs g=λ0/λ (0-2.0) on
glass |   |
| 20.31 | 20 | 31 | KEPT | Figure 20.31 — computed average spectral reflectivity (.04-.12) vs wavelength
(3 |   |
| 20.32 | 20 | 32 | KEPT | Figure 20.32 — computed spectral reflectivity (0-.16) vs wavelength
(1.5-5.0µ) o |   |
| 20.33 | 20 | 32 | KEPT | Figure 20.33 — designs of the single (n1=1.55), double (n1=1.38/n2=2.10),
and tr |   |
| 20.34 | 20 | 32 | KEPT | Figure 20.34 — computed spectral reflectivity (0-.18) vs g=λ0/λ (0-2.0) at
norma |   |
| 20.35 | 20 | 34 | KEPT | Figure 20.35 — computed spectral reflectivity (0-.18) vs g=λ0/λ (0-2.0) of
singl |   |
| 20.36 | 20 | 34 | KEPT | Figure 20.36 — computed spectral reflectivity (0-.30) vs wavelength (1.5-5.0µ)
o |   |
| 20.37 | 20 | 34 | KEPT | Figure 20.37 — designs of single (n1=1.87), double (n1=1.38,n2=2.40), triple
(n1 |   |
| 20.38 | 20 | 35 | KEPT | Figure 20.38 — computed spectral reflectivity (0-.36) vs g=λ0/λ (0-2.0),
single  |   |
| 20.39 | 20 | 35 | KEPT | Figure 20.39 — computed spectral reflectivity (0-.4) vs wavelength (1.5-5.0µ),
s |   |
| 20.40 | 20 | 35 | KEPT | Figure 20.40 — computed spectral reflectivity (0-.40) vs wavelength (1.5-5.0µ)
c |   |
| 20.41 | 20 | 37 | KEPT | Figure 20.41 — measured transmittance (0-1.0) vs wavelength (2-6µ) of a Ge
plate |   |
| 20.42 | 20 | 37 | KEPT | Figure 20.42 — measured transmittance (0-1.0) vs wavelength (1-6µ) of a Si
plate |   |
| 20.43 | 20 | 37 | KEPT | Figure 20.43 — computed spectral reflectivity (0-.18) vs g=λ0/λ (0-2.0) on
glass |   |
| 20.48 | 20 | 40 | KEPT | Figure 20.48 — diagram of an 8-layer quarter-wave HL stack (H=n=2.30,
L=n=1.38,  |   |
| 20.49 | 20 | 41 | KEPT | Figure 20.49 — computed spectral reflectivity (0-1.0, right axis transmission
1. |   |
| 20.50 | 20 | 41 | KEPT | Figure 20.50 — same as 20.49 but 8-layer (LH)⁴ and 10-layer (LH)⁵ stack —
needs  |   |
| 20.51 | 20 | 41 | KEPT | Figure 20.51 — same style but 8-layer (LH)⁴ and 12-layer (LH)⁶ stack with
L=1.38 |   |
| 20.52 | 20 | 43 | REWRITTEN→CONFIRMED | Computed spectral reflectivity of an eight-layer and a twelve-layer quarter-wave stack, and the envelope of maximum reflectivity. | p.20-43; Glass (LH)⁴ / (LH)⁶ Air, L = 1.90, H = 2.30; the spec's 4/6 layers and H = 4.30 are wrong |
| 20.53 | 20 | 43 | REWRITTEN→CONFIRMED | Computed spectral reflectivity of a four-layer and a ten-layer quarter-wave stack, and envelope of maximum reflectivity. | p.20-43; Glass (LH)² / (LH)⁵ Air, L = 1.35, H = 4.00 |
| 20.54 | 20 | 44 | KEPT→CORRECTED | Showing the high-reflectance zone, and the minimum and maximum of the reflectivity envelope of the quarter-wave stacks shown in Fig. 20.53. | Figure 20.54 is on p.20-43; this block's text was the caption of 20.55 (numbering shifted by one); fixed 2026-09-24 |
| 20.55 | 20 | 44 | REWRITTEN→CORRECTED | A comparison of the wavelength (in vacuo) with the optical thickness of a basic period of a multilayer with a periodic structure, for various orders of interference. | p.20-44; the block's text describes Fig 20.56, not 20.55 (numbering shifted by one) |
| 20.56 | 20 | 44 | REWRITTEN→CORRECTED | Computed spectral reflectivity of an eight-layer quarter-wave stack and its envelope of maximum reflectivity. | p.20-44; the block's text describes Figs 20.57 (2:1 stack) and 20.58 (3:1 stack), which have no blocks of their own |
| 20.59 | 20 | 47 | KEPT | Figure 20.59 — computed spectral transmission (0-1.0) vs wavelength
(0.4-4.0µ) o |   |
| 20.60 | 20 | 47 | KEPT | Figure 20.60 — computed Rp, Rs, Rav=1/2(Rp+Rs) vs g=λc/λ (0-2.0) of an
8-layer q |   |
| 20.61 | 20 | 49 | KEPT | Figure 20.61 — computed Rp, Rs, Rav vs g=λ0/λ (0.2-1.8) at φ=φ0 of a
fictitious  |   |
| 20.62 | 20 | 49 | KEPT | Figure 20.62 — computed Tav at φ=0° and φ=65° of sixteen-layer quarter-wave
stac |   |
| 20.63 | 20 | 49 | KEPT | Figure 20.63 — computed Tav at φ=0° and φ=65° of a sixteen-layer 2:1 stack
Glass |   |
| 20.64 | 20 | 54 | KEPT | Figure 20.64 — Tav of a sixteen-layer 2:1 stack, Glass(HLL)⁸ Air and
Glass(LHH)⁸ |   |
| 20.65 | 20 | 54 | KEPT | Figure 20.65 — computed spectral reflectivity (left axis) / transmission
(right  |   |
| 20.66 | 20 | 54 | KEPT | Figure 20.66 — computed spectral transmission/reflection vs wavelength
(0.4-1.5µ |   |
| 20.67 | 20 | 57 | KEPT | Figure 20.67 — computed spectral transmission (0-1.0, right axis reflectivity
0- |   |
| 20.69 | 20 | 57 | KEPT | Figure 20.69 — computed spectral transmission (0-1.0) vs g=λ0/λ (0.45-0.8)
of mu |   |
| 20.68 | 20 | 57 | KEPT | Figure 20.68 — computed spectral reflectivity (left axis 0-1.0) / transmission
( |   |
| 20.70 | 20 | 58 | REWRITTEN→RESTORED | Computed spectral reflectivity of a multilayer consisting of an ensemble to two stacks. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect ('to', sic, as printed) |
| 20.71 | 20 | 58 | KEPT | Figure 20.71 — reflectivity (0-1.0) vs λ (350-700mµ) showing overlapping
high-re |   |
| 20.72 | 20 | 58 | REWRITTEN→RESTORED | An illustration of the method of computing the total transmission T₂ of a composite … | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 20.73 | 20 | 62 | KEPT | Figure 20.73 — measured spectral transmittance (0-100%) vs wavelength
(0.4-2.0µ) |   |
| 20.74 | 20 | 62 | KEPT | Figure 20.74 — measured reflectance R (dashed) and transmittance T (solid)
(0-1. |   |
| 20.75 | 20 | 62 | KEPT | Figure 20.75 — measured spectral transmittance (0-1.0) vs wavelength
(400-1100mµ |   |
| 20.76 | 20 | 62 | KEPT | Figure 20.76 — measured spectral transmittance (0-.9) vs wavelength
(1.00-2.00µ) |   |
| 20.77 | 20 | 63 | KEPT | Figure 20.77 — measured spectral transmittance (0-.9) vs wavelength
(2.50-5.00µ) |   |
| 20.78 | 20 | 63 | KEPT | Figure 20.78 — measured spectrophotometric transmittance (0-100) vs
wavelength ( |   |
| 20.79 | 20 | 63 | KEPT | Figure 20.79 — measured transmittance (0-.9) vs wavelength (3.0-4.5µ) of
a long- |   |
| 20.80 | 20 | 63 | KEPT | Figure 20.80 — measured spectral transmittance (0-100) vs wavelength
(2-14µ) of  |   |
| 20.81 | 20 | 65 | KEPT | Figure 20.81 — measured spectral transmittance (0-100) vs wavelength
(5-13µ) of  |   |
| 20.82 | 20 | 65 | KEPT | Figure 20.82 — measured spectral transmittance (0-1.00) vs wavelength
(.4-.8µ) o |   |
| 20.83 | 20 | 65 | KEPT | Figure 20.83 — measured spectral transmittance (0-100) vs wavelength
(.4-2.0µ) o |   |
| 20.84 | 20 | 65 | KEPT | Figure 20.84 — measured transmission (0-.9) vs wavelength (.4-1.8µ) of a
short-w |   |
| 20.85 | 20 | 66 | KEPT | Figure 20.85 — measured spectral transmittance (0-.9) vs wavelength
(.4-1.1µ) of |   |
| 20.86 | 20 | 66 | KEPT | Figure 20.86 — measured spectral transmittance (left axis 0-1.0) /
reflectance ( |   |
| 20.87 | 20 | 66 | KEPT | Figure 20.87 — measured spectral transmittance (0-1.0) vs wavelength
(400-1100µ) |   |
| 20.88 | 20 | 66 | KEPT | Figure 20.88 — schematic of a camera beam splitter: light through the
objective  |   |
| 20.89 | 20 | 68 | KEPT | Figure 20.89 — computed Rp, Rs, Rav=1/2(Rp+Rs) (left axis) and
transmission (rig |   |
| 20.90 | 20 | 68 | KEPT | Figure 20.90 — measured transmittance (0-1.00) vs wavelength
(400-700mµ) of a 60 |   |
| 20.91 | 20 | 68 | KEPT | Figure 20.91 — measured transmittance (left axis 0-1.0) / reflectance
(right axi |   |
| 20.92 | 20 | 70 | KEPT | Figure 20.92 — measured spectral transmittance (0-1.0) vs wavelength
(400-750mµ) |   |
| 20.93 | 20 | 70 | KEPT | Figure 20.93 — computed Tp, Ts, Tav=1/2(Tp+Ts) (left axis transmission,
right ax |   |
| 20.94 | 20 | 70 | KEPT | Figure 20.94 — computed spectral reflectivity (0.60-1.00, scale change at
0.90)  |   |
| 20.100 | 20 | 75 | REWRITTEN→CONFIRMED | The transmission as a function of wave number of a Fabry-Perot interferometer with t_g = 0.0025 cm. | p.20-75; the spec's 780-820 mμ wavelength axis belongs to Fig 20.101 |
| 20.102 | 20 | 77 | KEPT | Figure 20.102 — three standing-wave diagrams at a reflecting surface,
showing no |   |
| 20.103 | 20 | 77 | KEPT | Figure 20.103 — enlarged cross-section of a silver-dielectric-silver
Fabry-Perot |   |
| 20.104 | 20 | 78 | KEPT | Figure 20.104 — scatter plot of Δλ1/2 (mµ, .05-.25) vs wavelength
(200-1100mµ) f |   |
| 20.108 | 20 | 82 | KEPT | Figure 20.108 — cross-section of a conventional all-dielectric Fabry-Perot
type  |   |
| 20.109 | 20 | 82 | KEPT | Figure 20.109 — computed spectral transmission (0-1.0) vs g=λ0/λ (0-2.0)
of an a |   |
| 20.110 | 20 | 82 | KEPT | Figure 20.110 — computed transmission (0-1.0) vs g=λ0/λ (0.99-1.02) of
the pass  |   |
| 20.111 | 20 | 84 | KEPT | Figure 20.111 — computed spectral transmission (0-1.0) vs g=λ0/λ
(0.92-1.08) of  |   |
| 20.112 | 20 | 84 | KEPT | Figure 20.112 — phase shift upon reflection ε (degrees, 352-8 wrapped) vs
g=λ0/λ |   |
| 20.113 | 20 | 85 | KEPT | Figure 20.113 — measured transmittance vs wavelength (480-500mµ) of an
all-diele |   |
| 20.114 | 20 | 85 | REWRITTEN→CONFIRMED | Measured spectral transmittance of a Fabry-Perot type filter and auxiliary blocking filter composed of ZnS and PbTe. | p.20-85; Δλ½ = .330 μ as printed (and .051 × 6.45 μ = .329); the spec's .302 μ is wrong |
| 20.115 | 20 | 87 | REWRITTEN→RESTORED | Measured spectral transmittance of a Fabry-Perot type filter at various values of φ. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 20.116 | 20 | 87 | REWRITTEN→RESTORED | Measured spectral transmittance of a Fabry-Perot type filter on a BaF2 substrate. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 20.117 | 20 | 88 | KEPT | Figure 20.117 — computed spectral transmission (0-1.0) vs g=λ0/λ (0-2.0)
of a Fa |   |
| 20.113 | 20 | 88 | KEPT | Figure 20.113 — likely a duplicate figure number in the original for what
contex |   |
| 20.119 | 20 | 88 | KEPT | Figure 20.119 — measured spectral transmittance (0-.7) vs wavelength
(2.50-2.90µ |   |
| 20.120 | 20 | 90 | KEPT | Figure 20.120 — measured spectral transmittance (0-.6) vs wavelength
(4.20-4.70µ |   |
| 20.121 | 20 | 90 | KEPT | Figure 20.121 — measured transmittance (0-1.00) vs wavelength (5-14µ) of a
nine- |   |
| 21.1 | 21 | 3 | REWRITTEN→RESTORED | Notation with respect to Fresnel's coefficients for normal incidence. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 21.2 | 21 | 4 | KEPT | Figure 21.2 — schematic of Fresnel oblique-incidence notation: X-Z plane
of inci |   |
| 21.3 | 21 | 9 | KEPT | Figure 21.3 — schematic showing incident, reflected, and transmitted
Poynting-ve |   |
| 21.4 | 21 | 12 | KEPT | Figure 21.4 — schematic of N layers 0,1,...,ν-1,ν,...,N,N+1 at normal
incidence  |   |
| 21.5 | 21 | 13 | KEPT | Figure 21.5 — schematic of flow conditions at the (ν-1)th and νth layers:
incide |   |
| 21.6 | 21 | 16 | KEPT | Figure 21.6 — schematic of N-film multilayer at oblique incidence, E-vector
perp |   |
| 21.7 | 21 | 17 | KEPT | Figure 21.7 — schematic of N-film multilayer at oblique incidence, H-vector
perp |   |
| 21.8 | 21 | 20 | KEPT | Figure 21.8 — computed energy reflectances /ρ0/² (accurate, 0-1.4%) and
/ρ0a/² ( |   |
| 21.9 | 21 | 26 | KEPT | Figure 21.9 — monolayer of refractive index n1, thickness d1, between medium
0 ( |   |
| 21.10 | 21 | 42 | KEPT | Figure 21.10 — schematic of a monolayer (case N=1): medium 0 (n0,K0) /
layer 1 ( |   |
| 21.11 | 21 | 44 | KEPT | Figure 21.11 — energy reflectance /ρ0/² (0-.34) vs β1 (0-12.5 radians) for
non-a |   |
| 21.12 | 21 | 46 | KEPT | Figure 21.12 — energy reflectance vs wavelength (0.4-0.8µ) for various low
refle |   |
| 21.13 | 21 | 47 | KEPT | Figure 21.13 — energy reflectance /ρ0/² vs wavelength (1.15-3.45µ) for low
refle |   |
| 21.14 | 21 | 48 | KEPT | Figure 21.14 — (top) energy reflectance (0.70-1.00) vs optical path n1d1
(0-λ/2) |   |
| 21.15 | 21 | 49 | KEPT | Figure 21.15 — reflectance (0-100%) vs 2p1=Re(β1) in degrees (0-360°) for
variou |   |
| 21.16 | 21 | 50 | KEPT | Figure 21.16 — (a) reflectance/transmittance (0-1.00) vs thickness of film
in wa |   |
| 21.17 | 21 | 51 | KEPT | Figure 21.17 — reflectances /ρ0/² and /γ0/² (E perpendicular / parallel to
plane |   |
| 21.18 | 21 | 51 | REWRITTEN→CONFIRMED | Plot of the minimum reflectances /ρ₀/²min and /γ₀/²min against the refractive indices n₁ of the monolayers on spectacle crown glass at 45° angle of incidence. | p.21-51; the n₁ axis runs 1.0-1.4; the spec's 1.0-1.3 is wrong |
| 21.19 | 21 | 52 | KEPT | Figure 21.19 — minimum reflectances /ρ0/²min and /γ0/²min (0-0.06) vs
refractive |   |
| 21.20 | 21 | 52 | KEPT | Figure 21.20 — schematic of bilayer (case N=2) at oblique incidence: media
0(n0, |   |
| 21.21 | 21 | 54 | KEPT | Figure 21.21 — two schematics illustrating augmenting an interfacial
reflectance |   |
| 21.22 | 21 | 54 | KEPT | Figure 21.22 — schematic of the simplest low-reflecting bilayer: medium
0=glass( |   |
| 21.23 | 21 | 56 | KEPT | Figure 21.23 — (a) required optical path p1 (degrees) of the inner TiO2 layer
(n |   |
| 21.24 | 21 | 58 | KEPT | Figure 21.24 — % reflectance per surface (0-8) vs wavelength (0.40-0.7µ):
○ Calc |   |
| 21.25 | 21 | 59 | KEPT | Figure 21.25 — % reflectance (0-3.0) vs wavelength (0.4-0.7µ) for a family
of is |   |
| 21.26 | 21 | 59 | KEPT | Figure 21.26 — % reflectance (0-2.0) vs wavelength (0.4-0.7µ) for two
achromatic |   |
| 21.27 | 21 | 60 | KEPT | Figure 21.27 — reflectance % (0-3.0) vs β1=360n1d1/λ in degrees
(130-250°) illus |   |
| 21.28 | 21 | 61 | KEPT | Figure 21.28 — reflectance % (0-8) vs β1=360n1d1/λ in degrees (90-250°)
showing  |   |
| 21.29 | 21 | 63 | KEPT | Figure 21.29 — reflectance at quarter-wave condition (λ=λ0) (0-0.4) vs
outer-lay |   |
| 21.30 | 21 | 65 | KEPT | Figure 21.30 — reflectance % (0-8) vs wavelength (0.4-0.75µ) for
quarter-half-qu |   |
| 21.31 | 21 | 66 | KEPT | Figure 21.31 — notation comparing the λ/4-λ/2-λ/4 trilayer (media
0..4: n0,n1,n2 |   |
| 21.32 | 21 | 68 | KEPT | Figure 21.32 — reflectance % (0-5) vs wavelength (0.4-0.75µ) for Jupnik's
quadri |   |
| 21.33 | 21 | 68 | KEPT | Figure 21.33 — reflectance % (0-5) vs wavelength (0.4-0.75µ) for the same
quadri |   |
| 21.34 | 21 | 70 | KEPT | Figure 21.34 — schematic of a periodic multilayer of repeated bilayers,
media 0. |   |
| 21.35 | 21 | 71 | KEPT | Figure 21.35 — schematic of a multilayer with an odd number N of alternating
qua |   |
| 21.36 | 21 | 72 | KEPT | Figure 21.36 — transmittance % (0-100) vs wavelength (0.40-0.75µ) for
alternatin |   |
| 21.37 | 21 | 73 | KEPT | Figure 21.37 — schematic of multilayer Air/(.5L)H(.5L)/(.5L)H(.5L)/...
/Substrat |   |
| 21.38 | 21 | 74 | KEPT | Figure 21.38 — transmittance % (0-100, scattered data points) vs wavelength
(0.4 |   |
| 21.39 | 21 | 75 | KEPT | Figure 21.39 — schematic of a narrow pass band interference filter: Air /
B1 = s |   |
| 22.1 | 22 | 3 | KEPT | Figure 22.1 — optical schematic of an image converter system: objective assembly |   |
| 22.2 | 22 | 4 | KEPT | Figure 22.2 — schematic of an aspheric magnifier: field lens (adjacent to the
ph |   |
| 22.3 | 22 | 11 | REWRITTEN→RESTORED | Examples of basic scanning systems. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 22.4 | 22 | 11 | KEPT | Figure 22.4 — two schematics illustrating the advantage of an immersed detector: |   |
| 23.1 | 23 | 3 | KEPT | Figure 23.1 — Determination of numerical aperture. Line diagram: two rays crossi |   |
| 23.2 | 23 | 4 | KEPT | Figure 23.2 — optical schematic of a compound microscope: light source →
lamphou |   |
| 23.3 | 23 | 4 | KEPT | Figure 23.3 — cutaway of a compound microscope body showing the ray path
from mi |   |
| 23.4 | 23 | 5 | KEPT | Figure 23.4 — Kohler illumination schematic: light source + spherical reflector
 |   |
| 23.5 | 23 | 6 | KEPT | Figure 23.5 — vertical illuminator type A schematic: light source → two
condense |   |
| 23.6 | 23 | 7 | KEPT | Figure 23.6 — Optical layout of a 1.25 N.A. Abbe condenser. Scale lens drawing,  |   |
| 23.7 | 23 | 9 | KEPT | Figure 23.7 — Optical layout of a 1.8 mm fluorite (semi-apochromatic) objective. |   |
| 23.8 | 23 | 10 | KEPT | Figure 23.8 — Optical layout of a 10X Huygenian eyepiece, with aberration plot.  |   |
| 23.9 | 23 | 11 | KEPT | Figure 23.9 — optical schematic of a Ramsden eyepiece: eye lens (E.L.) and
field |   |
| 23.10 | 23 | 12 | KEPT | Figure 23.10 — optical schematic of a high-eyepoint compensating eyepiece:
eye l |   |
| 23.11 | 23 | 13 | KEPT | Figure 23.11 — Typical compensating eyepieces. Four lens cross-sections on a com |   |
| 23.12 | 23 | 14 | KEPT | Figure 23.12 — refracting darkfield condenser with a central stop: object on a
g |   |
| 23.13 | 23 | 14 | KEPT | Figure 23.13 — two aspheric darkfield condensers in cross-section, both showing
 |   |
| 23.14 | 23 | 15 | KEPT | Figure 23.14 — Bispheric (bicentric) darkfield condenser. Cross-section of a gla |   |
| 23.15 | 23 | 16 | KEPT | Figure 23.15 — elements of a slit ultramicroscope, ray-traced left to right:
A ( |   |
| 23.16 | 23 | 17 | KEPT | Figure 23.16 — elements of a phase microscope: annular diaphragm (K) uniformly
i |   |
| 23.17 | 23 | 17 | KEPT | Figure 23.17 — passage of light waves through mediums: wave A (undisturbed)
vs.  |   |
| 23.18 | 23 | 18 | KEPT | Figure 23.18 — Superimposed light waves. Four numbered panels of sinusoids on a  |   |
| 23.19 | 23 | 20 | KEPT | Figure 23.19 — optical schematic of the AO Baker interference microscope,
top to |   |
| 23.20 | 23 | 21 | KEPT | Figure 23.20 — path of light rays through a shearing and a double-focus system,
 |   |
| 23.21 | 23 | 24 | KEPT | Figure 23.21 — optical schematic (cross-section) of a Greenough-type
stereoscopi |   |
| 23.22 | 23 | 25 | KEPT | Figure 23.22 — optical system of a petrographic microscope, top to bottom:
focus |   |
| 24.1 | 24 | 6 | KEPT | Figure 24.1 — comparison of computed spot diagram (bottom) and actual photograph |   |
| 24.2 | 24 | 6 | KEPT | Figure 24.2 — determination of constant phase front from ray tracing data: rays
 |   |
| 25.1 | 25 | 2 | KEPT | Figure 25.1 — halftone photograph of a nodal slide instrument developed at the
U |   |
| 25.2 | 25 | 2 | KEPT | Figure 25.2 — schematic of focal-length measurement by visual nodal slide: point |   |
| 25.3 | 25 | 3 | KEPT | Figure 25.3 — measurement of spherical aberration by the Hartmann test:
(left) H |   |
| 25.4 | 25 | 4 | KEPT | Figure 25.4 — measurement of astigmatism with a grid reticle: grid reticle R,
co |   |
| 25.5 | 25 | 6 | KEPT | Figure 25.5 — basic diagram for measurement of distortion by nodal slide: system |   |
| 25.6 | 25 | 6 | KEPT | Figure 25.6 — halftone photograph of an elementary spherometer (CENCO-branded):
 |   |
| 25.7 | 25 | 7 | KEPT | Figure 25.7 — halftone photograph of the Guild-Watts precision spectrometer: a
d |   |
| 25.8 | 25 | 8 | REWRITTEN→RESTORED | Schematic of the Pulfrich refractometer. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 25.9 | 25 | 9 | KEPT | Figure 25.9 — simple interferometer for viewing Fizeau/Newton's fringes at
norma |   |
| 25.10 | 25 | 9 | KEPT | Figure 25.10 — most commonly used method for illuminating the interferometer:
li |   |
| 25.11 | 25 | 11 | KEPT | Figure 25.11 — arrangement of the interferometer surfaces S1 and S2 for obtainin |   |
| 25.12 | 25 | 13 | KEPT | Figure 25.12 — a Fizeau interferoscope: illuminated pinhole H sends light down
t |   |
| 25.13 | 25 | 15 | KEPT | Figure 25.13 — a modified Michelson interferometer: light source through filter  |   |
| 25.14 | 25 | 15 | KEPT | Figure 25.14 — Michelson's interferometer as a method of forming Fizeau fringes
 |   |
| 25.15 | 25 | 17 | KEPT | Figure 25.15 — Twyman-Green interferometer as used for inspecting a glass
plate  |   |
| 25.16 | 25 | 18 | KEPT | Figure 25.16 — modification of the location of end mirror M1 for testing prisms  |   |
| 25.17 | 25 | 18 | KEPT | Figure 25.17 — method for obviating surface flatness errors of test plate P:
bea |   |
| 25.18 | 25 | 19 | KEPT | Figure 25.18 — adaptation of the Twyman-Green interferometer to observation of
s |   |
| 25.19 | 25 | 20 | KEPT | Figure 25.19 — geometrical theory of the Ronchi Test: lens L forms a converging
 |   |
| 25.20 | 25 | 21 | KEPT | Figure 25.20 — the Ann Arbor Tester setup: plane mirror and lens under test on
t |   |
| 25.21 | 25 | 22 | KEPT | Figure 25.21 — two rows of halftone Ann Arbor tester photographs: "Figure 4"
row |   |
| 25.22 | 25 | 23 | KEPT | Figure 25.22 — 3D perspective diagram for determining the optical axis of an
off |   |
| 25.23 | 25 | 24 | KEPT | Figure 25.23 — Jentsch's grid method: four halftone shadow-fringe patterns
label |   |
| 25.24 | 25 | 25 | KEPT | Figure 25.24 — experimental arrangement for a Foucault Test of a mirror: a
conca |   |
| 25.25 | 25 | 25 | KEPT | Figure 25.25 — schematic demonstration of the sensitivity of Foucault testing: a |   |
| 25.26 | 25 | 26 | REWRITTEN→RESTORED | Foucault test appearances. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 25.27 | 25 | 27 | KEPT | Figure 25.27 — isophotal lines (dashed concentric ellipses, axis labels B/B'
and |   |
| 25.28 | 25 | 28 | KEPT | Figure 25.28 — Foucault Test set-up for paraboloidal mirrors: the paraboloidal
m |   |
| 25.29 | 25 | 29 | REWRITTEN→RESTORED | The Gaviola technique of Foucault Testing. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 25.30 | 25 | 30 | KEPT | Figure 25.30 — experimental arrangement for a star test: lamp illuminating a
"st |   |
| 25.31 | 25 | 32 | KEPT | Figure 25.31 — a grid of 24 small halftone star-test photographs (Taylor's
figur |   |
| 25.32 | 25 | 33 | KEPT | Figure 25.32 — four halftone star-test photographs showing astigmatism of
increa |   |
| 25.33 | 25 | 34 | KEPT | Figure 25.33 — three ray-fan diagrams of a lens showing types of spherical
aberr |   |
| 25.34 | 25 | 35 | REWRITTEN→RESTORED | Star images showing various amounts of primary spherical aberration. | caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect |
| 25.35 | 25 | 36 | KEPT | Figure 25.35 — six star-image photographs exhibiting coma, labeled p=0,
p=10, p= |   |
| 26.1 | 26 | 2 | KEPT | Figure 26.1 — the USAF resolving power target: six groups of tribar
patterns (th |   |
| 26.2 | 26 | 2 | KEPT | Figure 26.2 — the Nutting and Annuli resolving power targets: (left) a
radial se |   |
| 26.3 | 26 | 3 | KEPT | Figure 26.3 — the old NBS resolving-power test chart: a cross-shaped
arrangement |   |
| 26.4 | 26 | 3 | KEPT | Figure 26.4 — the new NBS resolving-power targets: two nested-square bar
charts  |   |
| 26.5 | 26 | 5 | KEPT | Figure 26.5 — image contrast (0 to 1.5) vs. line frequency (0-80 lines/mm)
for h |   |
| 26.6 | 26 | 7 | KEPT | Figure 26.6 — six halftone reproductions of the USAF-type resolution
target (eac |   |
| 26.7 | 26 | 9 | KEPT | Figure 26.7 — halftone schematic of the KDC apparatus: plan view
(top) showing t |   |
| 26.7 | 26 | 9 | KEPT | Figure 26.7 — halftone modified Foucault resolution targets: an upper
row of fiv |   |
| 26.8 | 26 | 13 | KEPT | Figure 26.8 — block diagram of the basic Schade system: motor-driven film
loop ( |   |
| 26.9 | 26 | 13 | KEPT | Figure 26.9 — halftone reproduction of a strip of sine-wave test target
film: a  |   |
| 26.10 | 26 | 14 | KEPT | Figure 26.10 — sine wave response (-0.2 to 1.0) vs. spatial frequency
(0-100 cyc |   |
| 26.11 | 26 | 14 | KEPT | Figure 26.11 — response (0 to 1.0) vs. focal position (-1.0 to 1.0 mm)
for lens  |   |
| 26.12 | 26 | 15 | KEPT | Figure 26.12 — through-focus response curves (response 0 to 1.0, some
dipping to |   |
| 26.13 | 26 | 15 | KEPT | Figure 26.13 — frequency response (0 to 1.0, one curve dipping to -0.2) vs.
spat |   |
| 26.14 | 26 | 16 | REWRITTEN→CONFIRMED | Frequency response of lens A .4 mm outside focus for various colors. | p.26-16; curve 5 bottoms out near −0.08 at about 20 cycles/mm; the spec's '−0.8 near 15' is wrong |
| 26.15 | 26 | 16 | REWRITTEN→CONFIRMED | The Lambert's test object for measuring sine wave response. | p.26-16; a variable-area object with a sinusoidal (scalloped) edge; the spec's 'square-wave profile' is wrong |
| 26.16 | 26 | 18 | KEPT | Figure 26.16 — halftone photo of Lambert's lens bench: light source, collimating |   |
| 26.17 | 26 | 18 | KEPT | Figure 26.17 — (a) sine-wave response /A#/ and its Fourier transforms A#c,
A#s v |   |
| 26.18 | 26 | 19 | KEPT | Figure 26.18 — enlarged halftone photographs at seven intervals along a
continuo |   |
| 26.19 | 26 | 19 | KEPT | Figure 26.19 — block diagram of the Herriott recording electronic lens bench:
le |   |
| 26.20 | 26 | 21 | KEPT | Figure 26.20 — halftone reproduction of an actual "Photoelectric Lens
Bench Reco |   |
| 26.21 | 26 | 21 | KEPT | Figure 26.21 — three line diagrams illustrating the Coltman definition of
respon |   |
| 26.22 | 26 | 23 | KEPT | Figure 26.22 — basic square wave system for studying ophthalmic lens power:
sour |   |
| 26.23 | 26 | 23 | KEPT | Figure 26.23 — the Hayes target for the American Optical automatic lens
power me |   |
