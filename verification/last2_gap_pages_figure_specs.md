# Figure & Table Regeneration Specs (Final Gap Pages: ch16 p31 & ch20 p26)

> Produced 2026-10-03 by Devin + `gemini-3-7-flash-medium` (vision pass).
> Closes the last 2 uncovered figure pages in the MIL-HDBK-141 audit. Cross-checked
> against OCR captions — verbatim transcriptions.

## Figure 16.19

**Type:** Line plot / schematic diagram (Fabry-Pérot multiple beam interference fringe intensity distribution / Airy formula profile)

**Caption (verbatim):** `FIGURE 16. 19- The Sharpness Quality of Multiple Beam Interference Fringes.`

**Orientation/size:** Landscape orientation, aspect ratio ~2.2:1 (wide horizontal layout spanning the lower half of page 16-31).

**Components (X-axis → Y-axis / layers / series):**
- **Y-axis (vertical):** Labeled $W$ (energy density) with an upward-pointing arrowhead at the top.
  - Upper horizontal reference guide: Straight horizontal line across both peak tops labeled $W_{\text{max}}$.
  - Half-power horizontal reference guide: Straight horizontal line at half height labeled $\frac{W_{\text{max}}}{2}$.
- **X-axis (horizontal):** Labeled $\alpha$ (phase angle parameter) with a rightward-pointing arrowhead at the far right.
  - Major position ticks on axis: $\nu 2\pi$ and $(\nu + 1) 2\pi$.
  - Horizontal dimension line spanning the two peaks: Labeled $2\pi$ with arrows pointing to the peak centerlines (fringe spacing / free spectral range in phase angle $\alpha$).
- **Plotted Series / Intensity Curve:**
  - Single continuous curve showing two sharp, symmetric resonance transmission peaks centered at $\alpha = \nu 2\pi$ and $\alpha = (\nu + 1) 2\pi$, falling rapidly to a near-zero flat baseline between peaks.
  - Annotation over left peak: Pointer arrow labeled $\nu^{\text{th}}\text{ SPECTRAL ORDER}$.
  - Half-maximum geometry:
    - Four solid circular dots mark where the intensity curve intersects the $\frac{W_{\text{max}}}{2}$ line (two points per peak).
    - Vertical dashed drop lines extend downward from the half-maximum points on the first peak through the horizontal axis.
    - Horizontal dimension arrow from peak center ($\nu 2\pi$) to right half-power drop line labeled $\Delta\alpha$ (half-width at half-maximum).
    - Dimension bracket below axis spanning both drop lines labeled $2w = \frac{\Delta\alpha}{\pi}$ (full width at half-maximum in normalized optical units).

**Color scheme:** 1960s B/W handbook — black-on-white line art. Solid black lines for axes, guidelines, and intensity curve; dashed vertical lines for half-power drop lines; solid circular dots at half-power intersections.

**Notes / physical details:**
- Illustrates Fabry-Pérot transmission function $W(\alpha) = \frac{B^2}{(1 - A)^2 + 4A\sin^2(\alpha/2)}$ where amplitude parameter $A \rightarrow 1$ (handbook text discusses $A = 0.9$, yielding sharp fringe optical half-width $2w \approx 0.032 \times 2\pi$).
- Peak maximum values touch the $W_{\text{max}}$ line; valleys touch near zero.

---

## Table 20.3

**Type:** Table

**Caption (verbatim):** `Table 20. 3 - The effective indices at \phi = 65^\circ incidence of a single-layer antireflection coating.`

**Orientation/size:** Landscape / horizontal boxed table, aspect ratio ~2.5:1 (top of page 20-26).

**Components (X-axis → Y-axis / layers / series):**
- **Grid Layout:** 4 columns × 4 rows (1 header block + 3 data rows).
- **Header Structure:**
  - Column 1: `LAYER`
  - Column 2: `INDEX AT NORMAL INCIDENCE`
  - Columns 3 & 4 (Super-header spanning both columns): `EFFECTIVE INDEX AT \phi = 65^\circ`
    - Sub-header Column 3: `POLARIZATION P`
    - Sub-header Column 4: `POLARIZATION S`
- **Data Rows:**
  - Row 1: `Incident medium (Air)` | `1.00` | `2.366` | `0.423`
  - Row 2: `Magnesium fluoride` | `1.38` | `1.83` | `1.041`
  - Row 3: `Glass substrate` | `1.51` | `1.89` | `1.208`

**Color scheme:** 1960s B/W handbook — black text within solid black bordered grid lines.

**Notes / physical details:**
- Numerical values illustrate effective index splitting for P- and S-polarizations ($n_p = n/\cos\theta$, $n_s = n\cos\theta$) at high incidence angle ($\phi = 65^\circ$) compared to normal incidence.

---

## Figure 20.23

**Type:** Line plot with integrated layer schematic / ray diagram

**Caption (verbatim):** `Figure 20. 23 - Computed spectral reflectivity of a single-layer antireflection coating at \phi = 0^\circ and \phi = 45^\circ .`

**Orientation/size:** Portrait orientation (single column width, aspect ratio ~1:1.6 overall including upper schematic and lower grid plot).

**Components (X-axis → Y-axis / layers / series):**
- **Upper Schematic / Ray Diagram:**
  - Ray path: Incident ray arriving at angle $\phi$ to surface normal (dashed vertical centerline), reflected ray exiting symmetrically at angle $\phi$. Double-headed angle arc labeled $\phi$. Ambient medium labeled `Air`.
  - Coating layer: Stippled / dotted rectangular layer labeled on right `n_1 = 1.55`. Design parameters on upper left: $n_1 t_1 = \lambda_0 / 4$, $\lambda_0 = 3.00\,\mu$.
  - Substrate block: Diagonally hatched rectangular substrate with ragged bottom/side borders labeled `As_2 S_3 glass substrate` and `n_s = 2.40` on right.
- **Lower Coordinate Plot:**
  - Background: Full rectangular Cartesian grid / graph paper grid.
  - **Y-axis (vertical):** Labeled `Reflectivity` (rotated 90° CCW).
    - Grid tick values: `.05`, `.10`, `.15`, `.20` (spanning 0.00 to 0.20).
  - **X-axis (horizontal):** Labeled `Wavelength in microns`.
    - Grid tick values: `1.5`, `2.0`, `3.0`, `4.0`, `5.0`.
  - **Curves / Series:**
    - Curve 1 ($\phi = 0^\circ$ / normal incidence): Smooth U-shaped curve starting at $R \approx 0.17$ at $\lambda = 1.5\,\mu\text{m}$, reaching zero minimum ($R = 0$) at $\lambda_0 = 3.0\,\mu\text{m}$, and rising to $R \approx 0.07$ at $\lambda = 5.0\,\mu\text{m}$. Labeled `\phi = 0` with an arrow pointing to the curve near $\lambda = 2.3\,\mu\text{m}$.
    - Curve 2 ($\phi = 45^\circ$ / oblique incidence): Shifted U-shaped curve starting at $R \approx 0.16$ at $\lambda = 1.5\,\mu\text{m}$, reaching a non-zero minimum ($R \approx 0.04$) near $\lambda \approx 2.6\,\mu\text{m}$, crossing the normal-incidence curve near $\lambda \approx 2.9\,\mu\text{m}$, and rising to $R \approx 0.09$ at $\lambda = 5.0\,\mu\text{m}$. Labeled `\phi = 45^\circ` with an arrow pointing to the curve near $\lambda = 3.5\,\mu\text{m}$.

**Color scheme:** 1960s B/W handbook — black line art on white background with dense black grid lines.

**Notes / physical details:**
- Arsenic Trisulfide substrate ($As_2S_3$, $n_s = 2.40$) coated with a single quarter-wave film ($n_1 = 1.55 \approx \sqrt{2.40}$) centered at $\lambda_0 = 3.00\,\mu\text{m}$. Demonstrates zero reflectance at design center for normal incidence and spectral shift / degradation under 45° angle of incidence.

---

## Figure 20.24

**Type:** Line plot with integrated layer schematic / ray diagram

**Caption (verbatim):** `Figure 20. 24 - Computed spectral reflectivity of a single-layer antireflection coating at \phi = 0 and \phi = 45^\circ .`

**Orientation/size:** Portrait orientation (single column width, aspect ratio ~1:1.6 overall including upper schematic and lower grid plot).

**Components (X-axis → Y-axis / layers / series):**
- **Upper Schematic / Ray Diagram:**
  - Ray path: Incident ray arriving at angle $\phi$ to surface normal (dashed vertical centerline), reflected ray exiting symmetrically at angle $\phi$. Double-headed angle arc labeled $\phi$. Ambient medium labeled `Air`.
  - Coating layer: Stippled / dotted rectangular layer labeled on right `n_1 = 1.90`. Design parameters on upper left: $n_1 t_1 = \lambda_0 / 4$, $\lambda_0 = 3.00\,\mu$.
  - Substrate block: Diagonally hatched rectangular substrate labeled inside/below `Germanium` and `n_s = 4.05` on right.
- **Lower Coordinate Plot:**
  - Background: Full rectangular Cartesian grid / graph paper grid.
  - **Y-axis (vertical):** Labeled `Reflectivity` (rotated 90° CCW).
    - Grid tick values: `0`, `.05`, `.10`, `.15`, `.20`, `.25`, `.30`, `.35`, `.40` (spanning 0.00 to 0.40).
  - **X-axis (horizontal):** Labeled `Wavelength in microns`.
    - Grid tick values: `1.5`, `2.0`, `3.0`, `4.0`, `5.0`.
  - **Curves / Series:**
    - Curve 1 ($\phi = 0$ / normal incidence): Deep U-shaped curve starting at $R \approx 0.35$ at $\lambda = 1.5\,\mu\text{m}$, dropping to a near-zero minimum ($R \approx 0.003$) at $\lambda_0 = 3.0\,\mu\text{m}$, and rising to $R \approx 0.15$ at $\lambda = 5.0\,\mu\text{m}$. Labeled `\phi = 0` with an arrow pointing to the curve near $\lambda = 4.3\,\mu\text{m}$.
    - Curve 2 ($\phi = 45^\circ$ / oblique incidence): Shifted U-shaped curve starting at $R \approx 0.36$ at $\lambda = 1.5\,\mu\text{m}$, reaching a minimum of $R \approx 0.04$ near $\lambda \approx 2.8\,\mu\text{m}$, crossing the normal curve near $\lambda \approx 3.0\,\mu\text{m}$, and rising to $R \approx 0.20$ at $\lambda = 5.0\,\mu\text{m}$. Labeled `\phi = 45^\circ` with an arrow pointing to the curve near $\lambda = 3.5\,\mu\text{m}$.

**Color scheme:** 1960s B/W handbook — black line art on white background with dense black grid lines.

**Notes / physical details:**
- High-index Germanium substrate ($n_s = 4.05$) coated with single film ($n_1 = 1.90$, e.g. silicon monoxide) quarter-wave centered at $\lambda_0 = 3.00\,\mu\text{m}$. Demonstrates the broader reflectivity swing and angle-shift effects for high-index IR optics compared to Figure 20.23.