# MIL-HDBK-141 — Editorial & Notation Notes

This document captures editorial findings, historical errata, notation discrepancies, and modern engineering mappings identified during OCR transcription and scientific validation across all chapters.

---

## Chapter 1: Introduction

### 1. Mathematical Notation & Errata
- **Table III — $\Pi\Pi$ Quaternion Operator**:
  - *Handbook Entry*: `ΠΠ | Quaternion summation operator.` (p. 1-4)
  - *Editorial Note*: In 3D spatial vector ray tracing and quaternion calculus, successive rotation operations are composed **multiplicatively** ($\prod$), not additively ($\sum$). The text in the 1962 handbook is a typographical/nomenclature misnomer for cumulative quaternion product / composition.

### 2. Sign Conventions & Modern Mappings
- **Angle of Incidence ($I, I'$)**:
  - *Handbook Convention*: Positive if rotating the ray clockwise by $< 90^\circ$ aligns it with the surface normal.
  - *Modern Alignment*: Follows Conrady / Frankford Arsenal convention; contrasts with modern ISO 10110 standards which measure counter-clockwise angles from normal to ray.
- **Abbe Number**:
  - *Handbook Convention*: Uses Greek letter $\nu$ for Abbe $V$-number ($V_d$).
  - *Modern Alignment*: Modern texts use $V$ or $V_d = \frac{n_d - 1}{n_F - n_C}$.
- **Optical Invariant**:
  - *Handbook Convention*: Uses $\Phi$ for the Lagrange-Helmholtz / Smith-Helmholtz optical invariant ($n u y = \text{const}$).
  - *Modern Alignment*: Modern literature often designates power by $\Phi$ and optical invariant by $H$ or $\mathcal{L}$.

### 3. Omissions from Master Symbol Table
- The introductory tables omit explicit definitions for $NA$ (Numerical Aperture) and OTF/MTF notation ($T(\nu)$), though $NA$ and $\nu$-equivalents are introduced in substantive chapters.

---

## Chapter 2: Fundamentals of Geometrical Optics

### 1. Mathematical Notation & Formulations
- **Astigmatic Constant / Refraction Invariant ($\Gamma$, Eq. 3–4)**:
  - *Formulation*: $\vec{S}_1 - \vec{S}_o = \Gamma\vec{M}_1$, where $\vec{S} = n\vec{Q}$.
  - *Editorial Note*: $\Gamma = n_1\cos I' - n_o\cos I = -n_o\cos I + n_1 [ ( \frac{n_o}{n_1}\cos I )^2 - ( \frac{n_o}{n_1} )^2 + 1 ]^{1/2}$ is exact and forms the basis for 3D skew ray tracing across arbitrary curved interfaces.

### 2. Sign Conventions & Modern Mappings
- **Abbe Number Reference Wavelength ($n_D$ vs $n_d$)**:
  - *Handbook Convention*: Uses sodium D line centroid ($n_D = 589.3\text{ nm}$) in $\nu = (n_D - 1)/(n_F - n_C)$ per US MIL-G-174.
  - *Modern Alignment*: Modern international standards (ISO/DIN, Schott) use the helium d-line ($n_d = 587.56\text{ nm}$) or mercury e-line ($n_e = 546.07\text{ nm}$).
- **Glass Designation Coding (6-digit MIL-G-174 / Schott)**:
  - Standard format `[first 3 digits of (n_D - 1)*1000][first 3 digits of nu*10]`. Example: $n_D = 1.51250$, $\nu = 60.5 \rightarrow 513605$.

---

## Chapter 3: Considerations of Physical Optics

### 1. Mathematical Formulations & Approximations
- **Energy Density Proportionality Factor (Eq. 13–16)**:
  - *Handbook Formulation*: $W_i = E^2$ and $\bar{W} = a^2/2$.
  - *Editorial Note*: Proportionality factor $\frac{1}{2}\epsilon_0 c n$ is set to unity by convention, standard in classical wave optics analysis.
- **Interferometric Small-Angle Approximation (Eqs. 34–35)**:
  - *Formula*: $h = \lambda / (n\sin\theta) \approx \lambda / (n\theta)$.
  - *Editorial Note*: Omitting the $knz(1-\cos\theta)$ axial term is valid strictly in transverse observation planes near the intersection region ($z \approx 0$).
  - *Sampling / Detector Rule*: Fringe detection without moiré/aliasing requires sensor pixel pitch $\le h/2$ (Nyquist-Shannon limit).

---

## Chapter 4: Visual Optics

### 1. Terminology & Units
- **Troland unit (§4.4.5.2)**:
  - *Handbook term*: "Troland (formerly called photon)" — 1 Troland = 1 cd/m² · 1 mm² of pupil area.
  - *Editorial Note*: The name "photon" for this unit was deprecated; modern photometry uses "Troland" (symbol Td) exclusively. Formula: $T = L \cdot (\pi d^2 / 4)$ where $L$ in cd/m² and $d$ in mm. OCR garbled the printed formula; reconstructed from physical definition.
- **Wavelengths in mμ (millimicrons)**:
  - *Handbook Convention*: Throughout Ch. 4, wavelengths are expressed in mμ (e.g., 380–740 mμ, 555 mμ, 590 mμ).
  - *Modern Alignment*: 1 mμ = 1 nm. All mμ values are numerically identical to nm.

### 2. Reference Data & Standard Values
- **Gullstrand Reduced Eye (Figure 4.2)**:
  - *Handbook Values*: Cornea 43 D, lens 19 D, total 58.6 D; $n_\text{cornea} = 1.376$, $n_\text{aqueous} = 1.336$, $n_\text{vitreous} = 1.337$, $n_\text{lens outer} = 1.386$, $n_\text{lens inner} = 1.406$, $n_\text{lens equiv} = 1.42$; $f_1 = 17.13$ mm, $f_2 = 24.75$ mm; 1st PP at 1.54 mm, 2nd PP at 7.62 mm, 1st NP at 7.30 mm from cornea.
  - *Editorial Note*: Consistent with Gullstrand (1909) and LeGrand reduced eye constants. The lens Abbe number $\nu = 48.3$ matches documented ocular chromatic dispersion. 2nd Nodal Point (N2) at 7.62 mm — coincides with 2nd Principal Point (standard result for object in air).
- **Stiles-Crawford Effect (§4.4.5.1)**:
  - *Handbook Values*: 1 mm→90%, 2 mm→70%, 3 mm→40%, 4 mm→20%.
  - *Editorial Note*: Consistent with the Stiles-Crawford function $\eta(\rho) = 10^{-\alpha\rho^2}$ with $\alpha \approx 0.05$ per mm². Photopic (daylight/cone) vision only.

### 3. Age Data Citation
- **Illumination doubling (§4.8.2, Figure 4.13)**:
  - *Source*: "One experimenter" — identified by Figure 4.13 caption as O.W. Richards, *American Journal of Optometry*, 1958.
  - *Modern status*: Still cited qualitatively in human factors literature; 13 years is the specific value from Richards' data.

---

## Chapter 5: Fundamental Methods of Ray Tracing

### 1. Mathematical Formulations & Sign Conventions
- **3D Skew Ray Direction Cosines (Eqs. 1–15)**:
  - *Handbook Formulation*: Direction cosines $(K, L, M)$ where $M$ is along the optical axis $Z$. Refraction uses invariant $\Gamma = n_1\cos I' - n_0\cos I$.
  - *Editorial Note*: Exact and standard in classical vector ray tracing literature (Feder, Spencer-Murty).
- **Aspheric Deformation Coefficients (Eq. 16)**:
  - *Handbook Formulation*: $Z = \frac{cS^2}{1 + \sqrt{1 - c^2S^2}} + eS^4 + fS^6 + gS^8 + hS^{10}$.
  - *Modern Mapping*: Coefficients $(e, f, g, h)$ correspond to modern even-aspheric polynomial terms $(A_4, A_6, A_8, A_{10})$.
- **Paraxial Refraction Sign Convention (Eq. 57)**:
  - *Handbook Formulation*: $(nu)_k = (nu)_{k-1} + y_kc_k(n_{k-1} - n_k)$.
  - *Modern Alignment*: Matches Conrady / Frankford Arsenal convention where $u$ is ray angle/slope; identical to $(nu)_k = (nu)_{k-1} - y_k\phi_k$ where $\phi_k = c_k(n_k - n_{k-1})$.
- **Coddington Equations (Eqs. 45–46)**:
  - *Handbook Formulation*: Sagittal $\frac{n_0}{D_0} + \frac{n_1}{D_1} = \frac{\Gamma}{r}$; Tangential $\frac{n_0\cos^2 I}{D_0^T} + \frac{n_1\cos^2 I'}{D_1^T} = \frac{\Gamma}{r}$.
  - *Editorial Note*: Right-hand side is identically $\Gamma / r = (n_1\cos I' - n_0\cos I)/r$.

### 2. Historical Hand-Computing Shortcuts
- **PR Method (§5.6.5, Table 5.5)**:
  - Invariant $P = n_0 r \sin I = n_1 r \sin I'$ represents the optical impact parameter about the center of curvature and is strictly invariant across refraction (self-check property).
  - Pre-computed constants $R = 1/(n_0 r)$ and $-R' = -1/(n_1 r)$ enabled hand computation in 40–60 seconds per surface.

---

## Chapter 6: First Order Optics

### 1. Mathematical Formulations & Invariants
- **Optical Invariant Terminology (§6.3, Eq. 6)**:
  - *Handbook Formulation*: $\Phi = \bar{y}(nu) - y(n\bar{u}) = \begin{vmatrix} \bar{y} & n\bar{u} \\ y & nu \end{vmatrix}$.
  - *Nomenclature Mapping*: Cited interchangeably in the handbook as the "optical invariant", "Smith-Helmholtz invariant", and "Lagrange invariant". Modern literature typically designates optical invariant by $H$ or $\mathcal{L}$ and reserves $\Phi$ for total optical power.
- **Mirror Cardinal Points & Folding (§6.8)**:
  - *Handbook Convention*: Uses $n_{+1} = -n$ upon reflection with negative axial thicknesses.
  - *Geometric Result*: For a single spherical mirror, $f' = r/2$ and all six cardinal points ($F_1, F_2, P_1, P_2, N_1, N_2$) coincide at the center of curvature.
- **Secondary Spectrum Universal Scaling (§6.10.8.3, Eq. 49)**:
  - *Formula*: $\text{TAch}_{F-D} \approx f' / 2200$.
  - *Physical Basis*: Arises from the near-constant partial dispersion ratio slope $(\tilde{P}_a - \tilde{P}_b)/(\nu_a - \nu_b) \approx -1/2200$ across all standard optical glasses.

---

## Chapter 11: Telescope Objectives

### 1. Mathematical Formulations & Equations
- **Achromatic Doublet Power Distribution (Eqs. 6–7)**:
  - *Formulas*: $\phi_a = \phi \cdot \nu_a / (\nu_a - \nu_b)$; $\phi_b = -\phi \cdot \nu_b / (\nu_a - \nu_b)$.
  - *Editorial Note*: Standard achromatic doublet power split; consistent with ch06 derivation. Sign is correct: crown (a) is positive, flint (b) is negative.
- **Petzval Sum for Achromat (Eq. 8)**:
  - *Handbook Formulation*: $\Sigma P = -\phi \cdot (\nu_a/n_a - \nu_b/n_b) / (\nu_a - \nu_b)$.
  - *Editorial Note*: The Petzval sum for a thin lens is $\phi/n$, so $\Sigma P = \phi_a/n_a + \phi_b/n_b$. Substituting the achromatic powers gives $\Sigma P = \phi \cdot (\nu_a/n_a - \nu_b/n_b)/(\nu_a - \nu_b)$. The handbook carries an overall minus sign; this likely reflects a sign convention where $\Sigma P > 0$ denotes field curvature toward the lens. Verify against ch06 sign convention.
- **Zonal Aberration Tolerance (§11.3.3.1)**:
  - *Handbook Formula*: $(Y_k)_\text{zone} = 4.6\lambda / L_{k-1}$, where $L_{k-1}$ is the longitudinal focus shift of the marginal ray relative to paraxial.
  - *Editorial Note*: Derived from the Rayleigh $\lambda/4$ OPD criterion via the transverse-OPD relation. The constant 4.6 is consistent with OPD $\approx Y_k \cdot Y_1/(2f')$ at the 0.707-zone. Not immediately obvious from first principles — flag for validator.
- **OPD from Transverse Aberration (§11.4.6, Eq. 72)**:
  - *Handbook Formula*: $\text{OPD} = Y_k \cdot Y_1 / (2f')$.
  - *Editorial Note*: Standard Conrady/Hopkins relation between transverse ray error $Y_k$ at the image plane (for a ray entering at pupil height $Y_1$) and wavefront OPD for a focus-shift-like aberration. Valid in the paraxial/small-angle limit.
- **Triplet Apochromat Equations (Eqs. 14–22)**:
  - *Handbook Formulation*: Three-lens power distribution from three simultaneous color-correction conditions (A′, e, g wavelengths). The system determinant is $\Delta = \det[\tilde{P}^*_i, \tilde{P}^{**}_i, 1]_{i=a,b,c}$.
  - *Editorial Note*: For secondary color correction, the three glasses must be collinear in the $P^*$ vs $P^{**}$ diagram ($\Delta = 0$). Individual element powers are computed by Cramer's rule. The total power $\phi = \phi_a + \phi_b + \phi_c$ is an independent constraint, giving the full solution.

### 2. Nomenclature & Historical Notation
- **Herzberger P\*/P\*\* Notation**:
  - *Handbook Convention*: $P^*$ and $P^{**}$ are Herzberger's normalized partial dispersion coordinates, defined in M. Herzberger, *Optica Acta*, **6**, 197 (1959).
  - *Modern Alignment*: Modern glass catalogs (Schott, Ohara) use $\Delta P_{g,F}$ or $\Delta P_{F,e}$ (anomalous partial dispersion relative to the "normal glass line"). The P\*/P\*\* diagram is the precursor to the modern $P_{g,F}$ vs $\nu$ Abbe diagram with the normal glass line.
- **Glass Types Referenced (§11.4.5)**:
  - F-1 (dense flint), KzFS-4 (short-flint special, anomalous dispersion), PKS-1 (phosphate crown special). All are 1960s Schott designations. KzFS-4 and PKS-1 are anomalous-dispersion glasses, which is why they are usable in apochromat triplets.

### 3. OCR Quality & Corrections
- **Tables 11.3–11.4** (38 + 16 thin-lens doublet types): Numerical data well captured; column headers garbled (systematic OCR issue with table headers). Values verified by spot-check against PDF scans.
- **Table 11.12** (doublet vs. triplet power comparison): OCR flagged as EQUATION placeholders 68–71. Correct values from scan: doublet $\phi_a = 0.21380$, $\phi_b = -0.1138$, $\phi = 0.1$; triplet $\phi_a = 0.2812$, $\phi_b = -0.4747$, $\phi_c = 0.2935$, $\phi = 0.1$.
- **Table 11.13** (PKS-1-first triplet lens spec): OCR shows last air thickness as "9.2728" — confirmed from PDF as back focal distance, not a physical inter-element thickness.
- **Systematic**: Chapter header garbled as "MiL>- HOBK~14"; gutter artifacts `i `, `| ` throughout (strip in cleanup pass).
- **TABLE false positives**: Pages 23–25 have multiple TABLE placeholders from figure gridlines. The actual figure is a meridional ray plot (Figure 11.13) not a data table; flagged for manual extraction.

### 4. Secondary Spectrum Threshold (§11.4.6)
- *Handbook Result*: At f/16.7, a simple doublet with focal length $f' < 65.8$ cm has secondary spectrum OPD $< \lambda/4$ (Rayleigh-diffraction-limited). No secondary correction needed below this threshold.
- *Derivation*: $\text{OPD} = Y_k \cdot Y_1/(2f')$. For the sample doublet: OPD = 0.038λ at $f' = 10$ cm. Scaling to $\lambda/4$: $f'_\text{threshold} = (0.25/0.038) \times 10\text{ cm} = 65.8\text{ cm}$.
- *Modern Relevance*: Quantitative rule rarely stated explicitly in modern texts. Provides a clear go/no-go criterion before deciding whether to design an apochromat.

---

## Chapter 24: Design Phase Optical Tests

### 1. Mathematical Notation & Errata
- **Seidel Tolerance Table, "Focal range" inconsistency (§24.2.3, p. 24-3, Eqs. 4 and 6)**:
  - *Handbook Entry*: Eq.(4) states "Focal range $= \lambda/N'\sin U'_m$" (first power of sine); Eq.(6) restates the identical quantity ("permissible $X'$ = focal range") as "$\lambda/N'\sin^2 U_m$" (squared).
  - *Editorial Note*: These two printed forms are inconsistent with each other. Eq.(6)'s squared form is the one consistent with the chapter's own Eqs.(1), (2), and (5) (all $\sin^2 U'_m$) and with the standard optical-engineering result that diffraction depth of focus scales as $1/NA^2$, not $1/NA$ (cf. gem 16.7, $|z| \le \lambda/(2\,NA^2)$). Eq.(4) is almost certainly a dropped exponent in the original 1962 typesetting. Substituting $\sin U'_m \approx 1/(2\cdot f/\#)$ into the correct (squared) form gives depth of focus $\approx 4\lambda(f/\#)^2$ — the Lost Gems catalog (gem 24.1) previously stated $8\lambda(f/\#)^2$, which matches neither printed form; corrected to $4\lambda(f/\#)^2$.

### 2. OCR Quality & Corrections
- **Figure 24.2 label misread as equation (p. 24-6)**: OCR flagged a fragment of the ray-diagram point labels (E, P, K, D, B, F, C, L, u, Pr) as "EQUATION 6: le =". This is figure-label noise, not a real equation.
- **Airy disk value (p. 24-5, Table 24.1 caption)**: OCR rendered the micron sign as a digit, garbling "4.0µ" as "4.01". Confirmed 4.0µ from the scan; consistent with the value already correctly transcribed elsewhere on the same page (§24.4.1, "diameter of the Airy disk is 4.0 microns").
