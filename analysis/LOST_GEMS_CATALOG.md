# Lost Gems of MIL-HDBK-141
## Catalog of Practical Rules, Shortcuts, and Efficiency Techniques

> "Hand-computing forced engineers to be extremely efficient: rules of thumb, shortcuts,
> nomograms, graphical methods, and consolidated reference data. Modern practice 'just
> plugs big equations into a computer' and has lost many of these efficiency techniques."

This catalog extracts the practical, usable techniques from MIL-HDBK-141 (1962) that
remain valuable today for fast design estimates, sanity checks, and physical intuition.

---

## Catalog format

Each entry:
- **N.M** — chapter-scoped ID (e.g., 17.3 = Chapter 17, Gem 3)
- **Title** — short name for the technique
- **Source** — chapter, section, page reference
- **Category** — one of:
  - `rule-of-thumb` — quick estimate without full calculation
  - `shortcut-formula` — simplified equation for a common special case
  - `reference-data` — consolidated table / material properties
  - `design-heuristic` — practical design guidance / decision rule
  - `graphical-method` — nomogram or graphical calculation aid
  - `sanity-check` — quick test to verify a design or result
- **The Gem** — the rule/method stated clearly and usably
- **When to use it** — what problem it solves, under what conditions
- **Modern relevance** — why this is still useful with computers
- **Accuracy / caveats** — known limits, failure modes
- **Dependencies** — `[NEEDS FIGURE NNN]` or `[NEEDS EQUATION NNN]` if incomplete

---


## Chapters mined

| Chapter | Title | Gems |
|---------|-------|------|
| Chapter 02 | Fundamentals of Geometrical Optics | 2.1 - 2.3 |
| Chapter 03 | Considerations of Physical Optics | 3.1 |
| Chapter 04 | Visual Optics | 4.1 - 4.8 |
| Chapter 05 | Fundamental Methods of Ray Tracing | 5.1 - 5.2 |
| Chapter 06 | First-Order Optics | 6.1 - 6.3 |
| Chapter 07 | Simple Thin Lens Optical Systems | 7.1 - 7.3 |
| Chapter 08 | Aberration Analysis and Third-Order Theory | 8.1 - 8.5 |
| Chapter 09 | Method of Lens Design | 9.1 - 9.4 |
| Chapter 10 | Triplet Objective Design | 10.1 - 10.5 |
| Chapter 11 | Telescope Objectives | 11.1 - 11.4 |
| Chapter 12 | Lens Relay Systems | 12.1 - 12.7 |
| Chapter 13 | Mirror and Prism Systems | 13.1 - 13.9 |
| Chapter 14 | Eyepieces | 14.1 - 14.10 |
| Chapter 15 | Complete Telescope | 15.1 - 15.6 |
| Chapter 16 | Applications of Physical Optics | 16.1 - 16.7 |
| Chapter 17 | Optical Materials | 17.1 - 17.8 |
| Chapter 18 | Atmospheric Optics | 18.1 - 18.9 |
| Chapter 19 | Optics for Missile Tracking | 19.1 - 19.9 |
| Chapter 20 | Applications of Thin Film Coatings | 20.1 - 20.10 |
| Chapter 21 | Coating of Optical Surfaces | 21.1 - 21.6 |
| Chapter 22 | Infrared Optical Design | 22.1 - 22.6 |
| Chapter 23 | Microscope Optics | 23.1 - 23.8 |
| Chapter 24 | Design Phase Optical Tests | 24.1 - 24.3 |
| Chapter 25 | Production Phase Optical Tests | 25.1 - 25.8 |
| Chapter 26 | Evaluation Phase Optical Tests | 26.1 - 26.5 |
| Chapter 01 | Introduction | -- (no gems) |
| Chapter 27 | Appendix: Trig Tables | -- (no gems) |

---

## The Gems

<!-- ================================================================ -->
<!-- CHAPTER 02 -- FUNDAMENTALS OF GEOMETRICAL OPTICS -->
<!-- ================================================================ -->

### 2.1
**Title:** Quick-reference refractive indices for 10 common optical materials

**Source:** ch02, §2.5.3, Table 2.2, page 2-5

**Category:** `reference-data`

**The Gem:**
Ten-material quick-reference table of refractive indices at visible wavelengths (except
Silicon, which is quoted at infrared). All values are relative to air ($n_\text{air} = 1.0003$).

| Material | $n$ |
|----------|-----|
| Vacuum | 1.000 |
| Air | 1.0003 |
| Water | 1.33 |
| Fused quartz | 1.46 |
| Borosilicate crown glass | 1.51 |
| Ordinary crown glass | 1.52 |
| Canada balsam (cement) | 1.53 |
| Light flint glass | 1.57 |
| Dense barium crown | 1.62 |
| Extra dense flint | 1.72 |
| Silicon (infrared) | 3.4 |

Canada balsam ($n = 1.53$) sits between the two crown glasses, making cemented
interfaces nearly invisible and minimizing surface losses. Silicon's $n = 3.4$ is a
quick reminder that IR materials live in a completely different index regime.

For detailed multi-wavelength data on optical glasses, see the full glass catalog
(Table 2.4, p. 2-8), which lists indices at 11 Fraunhofer wavelengths, Abbe number,
partial dispersion, specific gravity, stain and dimming class, and bubble code.

**When to use it:**
- Back-of-envelope estimates of refraction, reflection loss, or critical angle
- Quick checks of index-matching situations (cement selection, immersion media)
- Sanity check that a quoted index is in the right ballpark for a material class

**Modern relevance:**
These are the same materials optical engineers still reach for in quick estimates.
While full glass catalogs have thousands of entries, this table covers the majority
of mental estimation tasks.

---

### 2.2
**Title:** TIR critical angle: sin(Ic) = 1/n; crown glass Ic ≈ 41° — the prism design rule

**Source:** ch02, §2.4.1–2.4.2, Table 2.1, pages 2-4 to 2-5

**Category:** `shortcut-formula`

**The Gem:**
Total internal reflection (TIR) occurs when a ray inside glass strikes a glass-to-air
interface at an angle of incidence exceeding the critical angle $I_c$:

$$\sin I_c = \frac{n_1}{n_0} = \frac{1}{n_\text{glass}}$$

where $n_0 = n_\text{glass}$ (denser medium) and $n_1 = 1$ (air). The full table of
critical angles (Table 2.1, p. 2-4) — originally in radians, converted here to degrees:

| $n$ | $I_c$ (rad) | $I_c$ (°) | | $n$ | $I_c$ (rad) | $I_c$ (°) |
|-----|------------|-----------|--|-----|------------|-----------|
| 1.50 | 0.729728 | 41.81° | | 1.61 | 0.670168 | 38.39° |
| 1.51 | 0.723820 | 41.47° | | 1.62 | 0.665286 | 38.11° |
| 1.52 | 0.718020 | 41.14° | | 1.63 | 0.660481 | 37.84° |
| 1.53 | 0.712324 | 40.81° | | 1.64 | 0.655753 | 37.57° |
| 1.54 | 0.706730 | 40.49° | | 1.65 | 0.651099 | 37.30° |
| 1.55 | 0.701234 | 40.17° | | 1.66 | 0.646517 | 37.04° |
| 1.56 | 0.695834 | 39.87° | | 1.67 | 0.642005 | 36.78° |
| 1.57 | 0.690526 | 39.57° | | 1.68 | 0.637562 | 36.53° |
| 1.58 | 0.685308 | 39.27° | | 1.69 | 0.633186 | 36.28° |
| 1.59 | 0.680177 | 38.98° | | 1.70 | 0.628875 | 36.04° |
| 1.60 | 0.675132 | 38.68° | | | | |

Key prism check: a 45–45–90 prism in crown glass ($n \approx 1.52$, $I_c = 41.1°$)
provides TIR at the hypotenuse face because $45° > I_c$. This is why right-angle prisms
act as perfect reflectors with no metal coating.

[FIGURE: Ray diagram showing TIR at a glass-air interface. Horizontal boundary with glass below (label n_glass) and air above (label n=1). Incident ray from below at angle I > I_c measured from the surface normal. Reflected ray shown, no transmitted ray. Label I_c on the boundary as a dashed reference ray at grazing exit (90°). Clean schematic, no shading.]

**When to use it:**
- Checking whether a prism face angle exceeds $I_c$ (TIR guaranteed if angle > $I_c$)
- Selecting glass type when a specific critical angle is required
- Designing Porro, Dove, Abbe, or Pechan prism systems

**Modern relevance:**
TIR prisms remain standard for low-loss beam folding in binoculars, periscopes, and
laser systems. The $1/n$ formula and this table are the essential first check before
any ray-trace.

**Accuracy / caveats:**
- $I_c$ varies slightly with wavelength (dispersion) — keep a few degrees of margin
- Near $I_c$, Fresnel phase shifts are significant and affect polarization state

---

### 2.3
**Title:** Glass type number: 6-digit code encodes n and v — read any glass spec at a glance

**Source:** ch02, §2.7.2 and §2.7.4, pages 2-6 to 2-7

**Category:** `design-heuristic`

**The Gem:**
The Abbe constant (v-number) quantifies a glass's chromatic dispersion:

$$\nu = \frac{n_D - 1}{n_F - n_C}$$

where $n_D$ is the index at the sodium D line (589 nm), $n_F$ at hydrogen F (486 nm),
and $n_C$ at hydrogen C (656 nm). High $\nu$ = low dispersion (crown); low $\nu$ =
high dispersion (flint).

Each optical glass is then identified by a **6-digit type number**:
- **First 3 digits:** first three rounded digits of $(n_D - 1) \times 1000$ (refractivity)
- **Last 3 digits:** first three rounded digits of $\nu$

Example (from §2.7.4): $n_D = 1.51250$, $\nu = 60.5$ → type **513605**
- Refractivity: $(1.51250 - 1) \times 1000 = 512.50$ → rounds to **513**
- $\nu = 60.5$ → **605**
- Type number: **513605**

Quick reads:
- High first 3 digits (e.g., **720**xxx) → high-index glass ($n \approx 1.72$, dense flint)
- High last 3 digits (e.g., xxx**640**) → low dispersion, crown-type ($\nu \approx 64$)
- Low last 3 digits (e.g., xxx**250**) → high dispersion, flint-type ($\nu \approx 25$)

So **517642** is $n \approx 1.517$, $\nu \approx 64.2$ (borosilicate crown).
**805255** is $n \approx 1.805$, $\nu \approx 25.5$ (very dense, highly dispersive flint).

[FIGURE: Abbe diagram (glass map). Horizontal axis: Abbe v-number from 80 (left) to 20 (right), labeled "v (Abbe number) — low dispersion to high dispersion". Vertical axis: refractive index n from 1.45 (bottom) to 1.95 (top). Scatter plot of glass types as dots. Crown glasses clustered at upper-left (high v, moderate n); flints at lower-right (low v, high n). Label the two regions "Crown" and "Flint". Mark example point 517642 (v=64.2, n=1.517). Diagonal boundary separating crown from flint families shown as dashed line. Clean, publication-quality, no gridlines.]

**When to use it:**
- Decoding a 6-digit glass code from any lens prescription or spec sheet
- Estimating chromatic properties without looking up a table
- Quickly placing a glass in crown vs. flint territory from its type number alone

**Modern relevance:**
This encoding is used today in Zemax, CODE V, and every major optical design package.
The Abbe diagram uses exactly $n$ vs $\nu$ as its axes. Knowing how to decode a 6-digit
glass number is essential for reading any historical or modern optical prescription.

---


<!-- ================================================================ -->
<!-- CHAPTER 03 -- CONSIDERATIONS OF PHYSICAL OPTICS -->
<!-- ================================================================ -->

### 3.1
**Title:** Interferometer fringe width from beam angle: h = λ/(n sin θ)

**Source:** ch03, §3.3.3.2–3.3.3.3, page 3-7 (eq. 35)

**Category:** `shortcut-formula`

**The Gem:**
When two coherent plane waves cross at angle $\theta$ in a medium of refractive index $n$,
fringes repeat whenever $kn\,\Delta x\sin\theta = 2\pi$, giving fringe width (eq. 35):

$$h = \frac{\lambda}{n \sin\theta}$$

For small angles ($\theta$ in radians, $\sin\theta \approx \theta$) — valid to 1% for
$\theta < 0.14$ rad (8°):

$$h \approx \frac{\lambda}{n\,\theta}$$

In air ($n = 1$): $h \approx \lambda/\theta$.

**Worked example:** $\lambda = 0.633\ \mu\text{m}$ (HeNe), $\theta = 1\ \text{mrad}$
$\Rightarrow h = 0.633\ \text{mm/fringe}$

[FIGURE: Two plane wavefronts W1 and W2 crossing at small angle theta in an X-Z coordinate plane (after Fig. 3.3). Wavefront W1 propagates along Z-axis; W2 tilted at angle theta above it. Mark point A on Z-axis where wavefronts intersect, and point P on W2. Show fringe spacing h as a horizontal double-arrow between consecutive bright fringes in the interference zone. Label lambda, theta, and h. Minimal, schematic, no shading.]

**When to use it:**
- Setting mirror tilt in a Twyman-Green, Fizeau, or Mach-Zehnder interferometer to
  produce a desired fringe density (e.g., 2 fringes/mm across the aperture)
- Sampling check: fringe period $h$ must be $\geq 2\times$ the detector pixel pitch
  (Nyquist) before any phase-stepping algorithm can work
- Angular sensitivity: one fringe shift corresponds to $\Delta\theta = \lambda/(nh)$

**Modern relevance:**
This formula is the first thing to reach for when setting up or interpreting any
two-beam interferometer. Even with phase-shifting software, the nominal fringe spacing
must satisfy the detector Nyquist limit — this sets it in one step.

**Accuracy / caveats:**
- Use exact $\sin\theta$ form for $\theta > 8°$; approximation fails above that
- Assumes plane waves; curved wavefronts (e.g., near focus) produce curved fringes
  that distort as $\theta$ and distance from focus increase (§3.3.3.4)

---


<!-- ================================================================ -->
<!-- CHAPTER 04 -- VISUAL OPTICS -->
<!-- ================================================================ -->

### 4.1
**Title:** Eyepiece diopter range rule — covering the user population

**Source:** ch04, §4.3.3.4, page 4-3

**Category:** `rule-of-thumb`

**The Gem:**
When designing a focusable eyepiece for an optical instrument, the diopter adjustment
range needed to cover the user population (for myopia/hyperopia only — astigmats must
wear glasses) is:

| Diopter range | % of spectacle prescriptions covered |
|---------------|--------------------------------------|
| ±1 D          | ~70% |
| ±2 D          | ~85% |
| ±4 D          | ~98% |

Recommendation: use **±2 D** for most military/general-purpose instruments; **±4 D** for
instruments expected to be used without glasses (e.g., field artillery, vehicle optics).

**When to use it:**
- Setting the diopter travel spec for any focusable eyepiece
- Deciding whether to design for spectacle users (astigmats keep glasses on regardless)
- Justifying eyepiece range spec to a customer

**Modern relevance:**
These percentages appear to still be representative of the general population.
The same ±2/±4 diopter heuristic appears in modern MIL-SPEC eyepiece requirements.

**Accuracy / caveats:**
- These cover only spherical refractive error (myopia/hyperopia). Astigmats (§4.3.3.3)
  need their spectacles regardless — design for sufficient eye relief to accommodate them.
- Night use: add at least −2 D extra range for empty-field/night myopia (see 4.5).

---

### 4.2
**Title:** Exit pupil sizing rules for visual instruments

**Source:** ch04, §4.4.2 and §4.4.2.4, pages 4-4 to 4-5

**Category:** `design-heuristic`

**The Gem:**
The eye's pupil varies from **2 mm** (bright light, elderly) to **8 mm** (darkness, young).
Under average conditions: **3.5–4 mm**. Resolution degrades outside the 3–4 mm range.

Exit pupil sizing rules:
1. **For maximum illumination**: exit pupil ≥ largest expected eye pupil (8 mm for night,
   4 mm for day). Light is then limited only by the instrument aperture.
2. **If exit pupil > eye pupil**: the effective entrance pupil (for axial bundles) =
   eye pupil diameter × magnification. Oversizing the exit pupil relaxes eye placement
   precision at the cost of a larger objective.
3. **If exit pupil < eye pupil**: light to the retina is limited by the instrument exit
   pupil — you are "throwing away" collected light.
4. **For diffraction-limited vision**: pupil ≤ 2 mm means diffraction matters at the retina.

**When to use it:**
- Sizing telescope/binocular objectives: exit_pupil = D_obj / magnification
- Checking whether the instrument is illumination-limited or resolution-limited at night
- Designing for specific age groups (elderly pupils don't open past ~3 mm)

**Modern relevance:**
The same exit-pupil rules govern all modern telescopes, rangefinders, and weapon sights.
This gives the quantitative basis for why tactical night-vision devices need large exit pupils.

---

### 4.3
**Title:** Stiles-Crawford effect — pupil-edge light is wasted

**Source:** ch04, §4.4.5.1, page 4-7

**Category:** `reference-data`

**The Gem:**
Light entering the eye near the edge of the pupil is less effective at stimulating the
retina than light entering through the center. This is the **Stiles-Crawford effect**
(photopic/daylight vision only — does not apply at night/scotopic):

| Distance from pupil center | Relative effectiveness |
|---------------------------|----------------------|
| 0 mm (center)             | 100% |
| 1 mm                      | ~90% |
| 2 mm                      | ~70% |
| 3 mm                      | ~40% |
| 4 mm                      | ~20% |

**When to use it:**
- Calculating effective light throughput to the retina for large-exit-pupil instruments
- Explaining why extra exit pupil diameter beyond 4 mm gives diminishing returns
- Stray light analysis: edge-of-pupil light contributes less to the signal image

**Modern relevance:**
The Stiles-Crawford effect is still quantitatively valid and used in visual science
and precise photometry of the eye. For instrument design it shows that an 8 mm exit
pupil delivers substantially less than 4× the retinal illuminance of a 4 mm pupil.

**Accuracy / caveats:**
- Only for photopic (daylight/cone) vision. At scotopic (night/rod) levels the effect
  essentially vanishes — all rays entering the pupil are equally effective.

---

### 4.4
**Title:** Visual acuity numbers — fovea, falloff, and vernier

**Source:** ch04, §4.4.5, pages 4-7 to 4-8

**Category:** `reference-data`

**The Gem:**
Key visual acuity figures for optical instrument design:

| Task | Threshold |
|------|-----------|
| Foveal resolution (two points / grating) | **1 arcminute** (≈ 70 µm at 250 mm) |
| Acuity at 5° from fovea | **25%** of foveal (≈ 4 arcmin effective) |
| Acuity at 10° from fovea | **7%** of foveal (≈ 14 arcmin effective) |
| Vernier acuity (line misalignment detection) | **4 arcseconds** |
| Thin wire against bright sky (detection) | **0.5 arcsecond** (detection, not resolution) |
| Standard 20/20 letter detail | 1 arcminute |

Critical design implications:
- Only the **central ~1°** of field needs diffraction-limited or tight aberration correction;
  the eye cannot exploit full acuity at the field edge.
- **Vernier tasks** (scale readings, alignment reticles) are ~15× more sensitive than
  two-point resolution — always use vernier-type reticles for precision measurement.
- Horizontal/vertical features are seen ~3× better than features at 60°/120° to horizontal.

**When to use it:**
- Allocating aberration budget: central field tighter, edge field looser
- Choosing reticle design: vernier/line alignment vs. grating/letter resolution
- Specifying the field-of-view zone that requires full optical quality

**Modern relevance:**
These numbers are foundational to display design, head-mounted optics, and any
human-factors analysis of visual instruments. The vernier acuity advantage is
exploited in precision alignment optics (autocollimators, sighting telescopes).

---

### 4.5
**Title:** Night myopia — the eye at rest does not focus at infinity

**Source:** ch04, §4.4.4.1 and §4.4.4.3, pages 4-6 to 4-7

**Category:** `design-heuristic`

**The Gem:**
When viewing an empty field (darkness, featureless sky, instrument with no reticle),
the eye does **not** focus at infinity. It relaxes to a "resting" focus of approximately
**1 meter**. This is called:
- **Empty-field myopia** (bright empty field)
- **Night myopia** (dark field; compounded by large-pupil spherical aberration and Purkinje shift)

Total night myopia: typically **−0.5 to −2 diopters** relative to daytime infinity focus.

Practical design rules:
1. Eyepiece adjustment must include **at least −2 diopters** for instruments designed
   for night use (§4.4.4.3).
2. Telescopes without reticles used at night will appear slightly out of focus to users
   who do not actively re-focus for night conditions.
3. A visible reticle forces the eye to focus at the correct plane — an extra benefit of
   illuminated reticles beyond their marking function.

**When to use it:**
- Specifying eyepiece diopter travel for night-use instruments
- Explaining to users why a daytime-focused instrument looks blurry at night
- Designing reticle illumination (a reticle anchors accommodation at the right diopter)

**Modern relevance:**
Night vision systems, weapon sights, and military observation instruments routinely
specify −2 D extra range. The underlying physiology is unchanged.

---

### 4.6
**Title:** Binocular instrument design tolerances

**Source:** ch04, §4.7.5, pages 4-17 to 4-18

**Category:** `design-heuristic`

**The Gem:**
Comfortable binocular vision through an instrument requires strict tolerances:

| Parameter | Tolerance |
|-----------|-----------|
| Magnification difference between eyes | ≤ 2% (some fail at 0.5%) |
| Light level difference between eyes | ≤ 10% |
| Vertical prismatic imbalance | ≤ 0.5 prism diopter |
| Horizontal prismatic imbalance | ≤ ~0.5 p.d. (slightly more tolerable) |
| Image twist / torsion | Minimize; any observable twist causes strain |
| Interpupillary distance (IPD) range | **50–76 mm** |

Oculars must be **matched pairs** — small residual differences between nominally
identical oculars accumulate to magnification differences that exceed tolerance.

**When to use it:**
- Setting optical performance specs for binoculars, rangefinders, stereoscopic instruments
- Evaluating whether a beam splitter is suitable (must be neutral — chromatic splitters
  cause different accommodation in each eye, definite strain)
- Checking whether a design including astigmatic correction is usable binocularly

**Modern relevance:**
These tolerances are essentially unchanged in current military binocular standards
(MIL-PRF-10592). The 76 mm IPD upper limit is still standard. The 2% magnification
tolerance is cited in ISO 14132.

**Accuracy / caveats:**
- Individual variation is large: some people fail at 0.5%, others tolerate slightly
  more than 2%. Spec to 2% for general populations.

---

### 4.7
**Title:** Dark adaptation timeline and the red-light trick

**Source:** ch04, §4.5.2 and §4.5.2.1, page 4-11

**Category:** `design-heuristic`

**The Gem:**
The eye's dark adaptation follows a two-stage process:
1. **Cone adaptation**: rapid gain for the first ~10 minutes in darkness
2. **Rod adaptation**: slower gain continuing to ~1 hour in darkness

Key numbers:
- Useful night vision: available after **~30 minutes** in red light or darkness
- Maximum dark adaptation: **~1 hour** (little further improvement after this)
- Rods peak sensitivity: **~510 nm** (blue-green; the Purkinje shift from 555 nm)
- **Rods are nearly blind to wavelengths > 590 nm** (deep red/orange)

**The red-light trick:** Red illumination (λ > 590 nm) allows normal work (map
reading, instrument panels, cockpit tasks) while simultaneously dark-adapting the
rods. On entering darkness, useful night vision is available almost immediately.

**When to use it:**
- Specifying instrument panel / reticle illumination for night operations
- Designing cockpit or command-post lighting where night vision must be preserved
- Advising operators on required adaptation time before night missions

**Modern relevance:**
Red instrument panels and red safety lighting in military contexts are a direct
application. Modern red-light headlamps for astronomy, military, and SAR are
grounded in this physiology.

**Accuracy / caveats:**
- The 590 nm cutoff is conservative; 620–660 nm red is reliably safe. Deep red LEDs
  at 660 nm are standard for this purpose.
- Dark adaptation is impaired by vitamin A deficiency and some drugs.

---

### 4.8
**Title:** Age-based illumination doubling rule

**Source:** ch04, §4.8.2, pages 4-18 to 4-19

**Category:** `rule-of-thumb`

**The Gem:**
The illumination required for equivalent visual performance **doubles approximately
every 13 years of age**. An observer at age 60 needs roughly 4× the illumination
that a 20-year-old needs for the same task.

Contributing factors: smaller maximum pupil, yellowing lens (absorbs blue/violet),
declining retinal efficiency, and increased glare sensitivity.

**When to use it:**
- Designing instrument panels, reticles, or displays for a mixed-age user population
- Specifying minimum scene luminance in performance standards
- When the user population includes personnel over 50, budget extra illumination margin

**Modern relevance:**
Still cited in human-factors literature. Military optics designed for sustained
operations must account for a population from 18 to 55+ years.

---


<!-- ================================================================ -->
<!-- CHAPTER 05 -- FUNDAMENTAL METHODS OF RAY TRACING -->
<!-- ================================================================ -->

### 5.1
**Title:** PR method — fastest hand meridional ray trace

**Source:** ch05, §5.6.5, pages 5-22 to 5-26

**Category:** `shortcut-formula`

**The Gem:**
The **PR method** reduces meridional ray tracing to 4 equations and a pre-calculated
table of lens constants. An experienced computer achieves **40–60 seconds per surface**
with a desk calculator.

Pre-calculate once per lens surface:
```
R  = 1 / (n_prev · r)     (for incidence)
R' = 1 / (n_next · r)     (for refraction)
n·(r - r_next - t)        (transfer constant)
```

Trace each ray:
```
sin I  = P · R                            (angle of incidence)
sin I' = P · R'                           (Snell's law; P = CA · n is conserved)
U      = U_prev - (I - I')               (new slope angle)
P_next = P - (r - r_next - t) · n·sin U  (transfer P to next surface)
```

where P = CA · n = perpendicular distance from center of curvature to ray, scaled
by index; U = slope angle of ray; CA = closest approach distance from center of
curvature to the ray.

**When to use it:**
- Quick hand trace of a meridional ray through a multi-element system
- Checking computer output against a hand calculation
- When no software is available in the field

**Modern relevance:**
Faster to set up for a single spot-check than entering into a full lens design program.
The pre-calculated constants also give intuitive feel for how much each surface bends
the ray.

**Accuracy / caveats:**
- 6 significant figures required throughout
- Loss of precision if r becomes very large (nearly-plane surface) — use alternate form
- Plane surfaces need separate handling (use Q/tan U instead of P)
- Does not handle skew rays — use full direction-cosine equations for skew

[NEEDS FIGURE — Figure 5.12 and 5.13: PR method geometry and transfer diagram]

---

### 5.2
**Title:** Graphical Snell's law — two-circle ray tracing construction

**Source:** ch05, §5.7, pages 5-26 to 5-27

**Category:** `graphical-method`

**The Gem:**
Any refraction at a spherical surface can be solved graphically with two concentric
circles and a straight-edge — no trigonometry needed:

1. Draw two concentric circles with radii proportional to n₁ and n₂
2. Draw a line through the center **parallel to the incident ray**
3. Where this line intersects the n₁ circle, draw a line toward the **center of curvature**
4. Where this direction line intersects the n₂ circle, draw a line from the
   center of the circles through it — this is the **refracted ray direction**

Shortcut: place the center of the circles on the incident ray, n₁ units to the left
of the surface intersection point. This eliminates drawing the n₁ circle.

**When to use it:**
- Rapid layout and visualization of refraction without calculation
- Teaching Snell's law physically
- Quick sanity check on which way a surface bends a ray

**Modern relevance:**
Best way to build physical intuition for ray-surface interaction. For checking by
inspection whether a lens layout is plausible.

**Accuracy / caveats:**
- Graphical accuracy limit: ~1% (see 6.3) — layout/visualization only.

[NEEDS FIGURE — Figure 5.15: the concentric-circle construction]

---


<!-- ================================================================ -->
<!-- CHAPTER 06 -- FIRST-ORDER OPTICS -->
<!-- ================================================================ -->

### 6.1
**Title:** Paraxial ray trace format — the systematic two-row layout

**Source:** ch06, §6.2.2, pages 6-1 to 6-2

**Category:** `shortcut-formula`

**The Gem:**
Any optical system can be traced paraxially with just two computed constants per
surface/space:

    c(n' - n)   [refraction power at each surface]
    t/n         [reduced distance for each space]

Layout the system as alternating rows of surfaces (c, n) and spaces (t), fill in
these two constants, then trace a ray by applying the refraction and transfer
equations repeatedly. The format makes the computation a systematic table fill-in
rather than equation solving.

Transfer:   y_{k+1} = y_k + (t_k/n_k) · (nu)_k
Refraction: (nu)' = (nu) - y · c(n'-n)

**When to use it:**
- Hand-tracing any paraxial ray through a multi-element system
- Quick first-order layout check before running a lens design program
- Teaching/verifying a computer result against manual calculation

**Modern relevance:**
This exact format is what lens design programs compute internally. Understanding it
gives physical insight into why aberration contributions are surface-by-surface additive.
Valuable for interpreting software output and for quick back-of-envelope layouts.

[NEEDS FIGURE — Table 6.1 ray trace format diagram showing the alternating row layout with arrow flow]

---

### 6.2
**Title:** Two-ray rule — any paraxial ray as a linear combination

**Source:** ch06, §6.2.3 (implied throughout)

**Category:** `rule-of-thumb`

**The Gem:**
Once you have traced any TWO linearly independent paraxial rays through a system,
you can find the path of ANY other paraxial ray without additional tracing — it is
simply a linear combination of the two known rays.

In practice: trace the **axial ray** (starts on axis, aims at pupil edge) and the
**chief ray** (starts at field edge, passes through stop center). All other rays
are linear combinations of these two.

**When to use it:**
- After tracing two reference rays, read off f-number, magnification, pupil location,
  field stop, chromatic aberration — all from the same trace data.
- Checking whether a ray will miss an aperture: express it as a linear combo and
  inspect the heights at each surface.

**Modern relevance:**
This principle underlies the "two-ray" construction in all paraxial optics. It's why
lens design programs only need to trace two paraxial rays to characterize the full
first-order properties. Knowing this lets you extract maximum information from minimum
calculation.

---

### 6.3
**Title:** Graphical ray tracing accuracy limit

**Source:** ch06, §6.1.2, page 6-1

**Category:** `sanity-check`

**The Gem:**
Graphical (drawing-board) ray tracing is limited to approximately **1% accuracy**.

Rule: if your design tolerance is tighter than 1%, graphical tracing is only useful
for layout and visualization — use numerical tracing for any quantitative result.
If your tolerance is looser than 1%, graphical tracing may be sufficient for a
preliminary decision.

**When to use it:**
- Deciding how much effort to put into a preliminary layout
- Explaining to a customer why a back-of-envelope layout isn't sufficient for their spec
- Setting expectations when reviewing a hand-drawn optical layout

**Modern relevance:**
In the age of CAD, the "graphical" limit now corresponds to free-hand sketching or
rough CAD without proper surface modelling. The 1% rule is still a good intuitive
bound for "sketch-level" accuracy.

---


<!-- ================================================================ -->
<!-- CHAPTER 07 -- SIMPLE THIN LENS OPTICAL SYSTEMS -->
<!-- ================================================================ -->

### 7.1
**Title:** Magnifier relaxed-eye design rule — image at infinity is optimal

**Source:** ch07, §7.2.5, pages 7-3 to 7-4

**Category:** `design-heuristic`

**The Gem:**
A simple magnifier has two limiting magnifying powers:
- **Minimum MP** (relaxed eye, image at infinity): `MP_min = V/f'`
- **Maximum MP** (accommodated eye, image at near point −V): `MP_max = V/f' + 1`

where V = 250 mm (standard near-point), f' = focal length.

The gain from accommodation is only **~10%** (e.g. for f' = 1 inch: 10× vs 11×).
This small gain is not worth the sustained eye strain from accommodation.

**Design rule:** Design magnifiers and visual eyepieces so the **final image is at
infinity** (afocal adjustment — object at front focal point). The relaxed-eye
condition gives minimum MP but maximum observer comfort.

**When to use it:**
- Setting object distance and focal length for any magnifier or eyepiece
- Explaining to operators why forcing focus closer than infinity causes fatigue
- Designing adjustable-focus eyepieces: infinity should be at or near mid-travel

**Modern relevance:**
Every modern eyepiece in telescopes, microscopes, and military instruments is designed
for afocal output. This gem explains WHY and by how much.

---

### 7.2
**Title:** f-number of a lens element from paraxial angle change

**Source:** ch07, §7.3.5, page 7-4

**Category:** `shortcut-formula`

**The Gem:**
The working f-number of a thin lens element can be read directly from the paraxial
ray trace — no physical diameter measurement needed:

    f-number = 0.5 / |Δ(nu)|

where `Δ(nu) = (nu)_after - (nu)_before` is the change in the paraxial reduced angle
through the element (the change in the quantity nu = n × angle).

From a paraxial trace table, compute f-number for the axial ray AND the chief ray
separately — the smaller f-number reveals which ray bundle is working harder and
where aberration correction is most demanding.

**Example (from Table 7.3 in text):**
Microscope (NA = 0.25): objective f/1.82, eyepiece f/1.09 for the chief ray.
The eyepiece is the harder element to correct despite having lower overall power.

**When to use it:**
- Identifying the hardest-working element in a system
- Deciding which element to split into two doublets
- Setting minimum element diameter after the paraxial trace is complete

**Modern relevance:**
Built into every lens design program's output table. Understanding it lets you
read element difficulty from a paraxial table before running a full design.

---

### 7.3
**Title:** Symmetric field-lens — lateral color cancellation condition

**Source:** ch07, §7.3.7.4, pages 7-7 to 7-8

**Category:** `shortcut-formula`

**The Gem:**
Lateral color (transverse chromatic aberration) from two eyepiece lenses can be
**exactly cancelled** without achromatizing either lens, using the symmetry condition:

1. Place the two lenses so the chief ray height `ȳ` has **equal magnitude but
   opposite sign**: `ȳ_field = −ȳ_eye`
2. Use lenses of the **same glass** (same Abbe V-value)
3. Bend each lens to equalize the chief ray deflection: `|Δ(nū)|_field = |Δ(nū)|_eye`

Under these conditions the lateral color contribution `ȳ·φ/V` is equal and opposite
for the two lenses → exact cancellation.

In practice: place a positive field lens just before the intermediate image (where
the axial ray height equals the eyelens axial ray height), and let the chief ray
sign reverse across the image plane.

**When to use it:**
- Designing two-element eyepieces (Ramsden, Huygens, Kellner): choose lens positions
  to achieve the sign-flip condition
- Explaining why classic eyepiece spacings are what they are
- Quick check: if `ȳ` changes sign between two positive lenses of the same glass,
  they are canceling lateral color

**Modern relevance:**
This is the underlying principle of all classic eyepiece designs. Modern multi-element
eyepieces use the same concept extended to more elements.

**Accuracy / caveats:**
- Exact cancellation requires same glass (same V). For different glasses, match
  `ȳ·φ/V` products explicitly.
- This does not correct axial color — the objective must be achromatized separately.

---


<!-- ================================================================ -->
<!-- CHAPTER 08 -- ABERRATION ANALYSIS AND THIRD-ORDER THEORY -->
<!-- ================================================================ -->

### 8.1
**Title:** Spot diagram as the primary ray-trace quality metric

**Source:** ch08, §8.2, pages 8-1 to 8-2

**Category:** `design-heuristic`

**The Gem:**
Plot all traced rays as dots in the paraxial image plane (the spot diagram). The
spread and shape of the dot cluster immediately shows:
- Total geometric blur size
- Which ray zones are worst (edge, mid, paraxial)
- Presence and type of aberration (coma = comet tail, astigmatism = two separated blurs, etc.)
- Energy encircled in any given diameter (count dots in concentric circles)

Quick energy estimate: if N dots are plotted uniformly in the pupil, dots within
radius r contain fraction (r/r_max)² of the total energy (for uniform pupil illumination).

**When to use it:**
- First qualitative assessment of a new lens design
- Comparing two designs without computing aberration coefficients
- Quick check of whether performance is diffraction-limited or aberration-limited

**Modern relevance:**
Spot diagrams are still the standard first-look diagnostic in every modern lens
design program (Zemax, CODE V, etc.). This section explains the physical meaning
that the software just plots automatically.

[NEEDS FIGURE — Fig 8.1(a) entrance pupil spot diagram and 8.1(b) image plane spot diagram]
[NEEDS FIGURE — Fig 8.2 energy distribution curve]

✓ Confirmed via ch08 deep pass (§8.2.1, §8.2.3.1, pages 8-1/8-2, verified from scan): a spot diagram plots ray
intersections in the paraxial image plane for a uniform pupil grid, and the energy distribution curve is
obtained by counting spots inside concentric circles (192 pupil points in Fig 8.1(a), so each spot is 1/192
of the energy; Fig 8.2 rises to about 50% at 20 microns and about 83% at 105 microns).
Supplement / correction: the "(r/r_max)² of the energy" estimate is NOT in ch08. The book counts image-plane
spots within circles drawn around the center of concentration (§8.2.3.1); a pupil-radius rule of that form
applies only to a perfect (aberration-free) mapping. The "coma = comet tail, astigmatism = two blurs"
reading is standard practice, not text from ch08 (Fig 8.1(b) itself is a coma-like flare). ch08 §8.2.3.2
adds that the spot diagram shows how much the image spreads but not why, which motivates the ray-fan plots of §8.3.

---

### 8.2
**Title:** Third-order spherical aberration sign convention and undercorrection rule

**Source:** ch08, §8.5.1.5–8.5.1.6, page 8-7

**Category:** `design-heuristic`

**The Gem:**
A single positive (converging) lens always has **negative** third-order spherical
aberration coefficient b₃ — this is called "undercorrected" spherical aberration.
Rays at the edge focus closer to the lens than paraxial rays.

Quick sign rules:
- Single positive lens → undercorrected (b₃ < 0)
- Single negative lens → overcorrected (b₃ > 0)
- To correct spherical aberration: combine positive and negative elements, or
  use an aspheric surface

**When to use it:**
- Predicting aberration sign before tracing: saves setup time
- Choosing initial form (meniscus, biconvex, etc.) based on desired aberration balance
- Explaining to a customer why a simple singlet can't be made diffraction-limited

**Modern relevance:**
These sign conventions are identical in modern software. Understanding them prevents
sign errors when interpreting design program output.

✓ Confirmed via ch08 deep pass: §8.5.1.6 (page 8-7) states the sign rule verbatim ("the third order coefficient, b3,
is negative and the lens is said to be undercorrected ... because a single positive lens has spherical aberration
of this sign"), for the fit basis Eq 8-(1) $Y_k - \bar{Y}_k = b_1 Y_1 + b_3 Y_1^3 + b_5 Y_1^5 + O(7)$.
Supplements: (i) $b_3$ follows from surface sums, $b_3 = -\Sigma B / [2 n_{k-1} u_{k-1} y_1^3]$ with $B = S i^2$
(§8.5.2.1-8.5.2.2, Eqs 3-5); for the Taylor triplet of Table 8.2, $\Sigma B = -0.00641$, $b_3 = -0.006341$;
(ii) the fifth-order coefficient there is positive ($b_5 = +0.002818$, "overcorrected"), so the marginal
zone comes back to focus at $Y_1 = 1.5$ (§8.5.1.6, §8.5.2.3); (iii) "negative lens gives $b_3 > 0$" is
not stated in ch08 but follows from the sign of $B$ (in Table 8.2 the two surfaces of the negative middle
element supply all the positive $B$).

---

### 8.3
**Title:** Stop shift equations — changing aperture stop without re-optimizing

**Source:** ch08, §8.9.5, page 8-18

**Category:** `shortcut-formula`

**The Gem:**
If you move the aperture stop of a system (changing which ray is the chief ray),
the third-order aberration coefficients transform by a parameter Q = shift amount.
The new coefficients are:

    ΣB* = ΣB                    (spherical aberration unchanged)
    ΣF* = Q·ΣB + ΣF             (coma changes)
    ΣC* = Q²·ΣB + 2Q·ΣF + ΣC   (astigmatism changes)
    ΣE* = Q³·ΣB + 3Q²·ΣF + Q·Σ(3C+PΦ²) + ΣE  (distortion changes)
    ΣP* = ΣP                    (Petzval curvature unchanged)

Key insight: **spherical aberration and Petzval curvature are invariant to stop
position. Coma, astigmatism, and distortion change.**

**When to use it:**
- Predicting how moving a pupil affects off-axis aberrations without re-tracing
- Choosing stop position to zero out coma or distortion
- Understanding why telecentric systems (stop at front focal plane) have special properties

**Modern relevance:**
These equations are still used in manual sensitivity analysis and in understanding
what a lens design program is doing when it varies stop position.

✓ Confirmed via ch08 deep pass: Eqs 8-(18) through 8-(21a) (page 8-18) are transcribed from the scan and match this
gem exactly; they also follow algebraically from the shifted-chief-ray polynomial Eq 8-(17) (page 8-17), which
was re-derived by substituting $Y_1 = Y_1' + Q y_1 (\bar{Y}_o/\bar{y}_o)$ into Eqs (6)+(8).
Supplements: (i) $Q$ is defined precisely as $Q = \bar{y}_1^{*}/y_1$, the ratio of the new chief ray's height in the
original entrance pupil to the axial marginal ray height there (not a generic "shift amount"); (ii) the same
transformation for the first-order chromatic coefficients is $a^{*} = a$ (axial color unchanged) and
$b^{*} = Qa + b$ (lateral color shifts), Eqs 8-(22) and 8-(23); (iii) the thin lens versions are
Eqs 8-(40) through 8-(49). The telecentric remark in "When to use it" is standard optics, not ch08 text.

---

### 8.4
**Title:** The optical invariant — the conservation law of paraxial optics

**Source:** ch06, §6.3.2–6.3.5, pages 6-5 to 6-6

**Category:** `shortcut-formula`

**The Gem:**
For any two paraxial rays (axial ray: height y, angle nu; chief ray: height ȳ, angle n̄ū)
traced through an optical system, the quantity:

    Φ = y(nu) - ȳ(nū)

is constant — it has the same numerical value at every surface and every space in the
system. This is the **optical invariant** (also called the Smith-Helmholtz or Lagrange
invariant).

Consequences you can read off immediately from this single number:
- **Lateral magnification**: m = (n₀u₀) / (nₖuₖ₋₁)  [ratio of axial ray angles, entrance to exit]
- **Image height**: Yₖ = Φ / (nₖuₖ₋₁)  [given the invariant and exit angle]
- **étendue**: Φ² is proportional to the optical throughput (étendue) — conserved through lossless systems
- **Telescope magnifying power**: MP = ū_exit / ū_entry = y₁/ȳ₁  [for afocal system]

**When to use it:**
- Computing image height or magnification without completing a full ray trace
- Checking that a design is self-consistent (Φ should be identical at every surface)
- Quick sizing of field stops, relay lenses, or telescope objectives
- Verifying computer output: compute Φ at two surfaces and confirm they match

**Modern relevance:**
The optical invariant is the single most powerful shortcut in first-order optics.
Modern lens design software computes it automatically, but knowing what it means
lets you immediately estimate image size, pupil size, and magnification from a
partial layout — before the design is complete.

**Accuracy / caveats:**
- Exact for paraxial (first-order) optics; approximate for real (finite-angle) rays.
- Sign conventions must be consistent: y below axis is negative, angles measured from axis.

[DEEP-PASS NOTE, ch08: source of this gem is ch06, outside the ch08 deep pass, but ch08 states the invariant and
allows a numeric check. Eq 8-(35) (page 8-19) gives $\Phi = \bar{y}\,u_{-1} - y\,\bar{u}_{-1} = \bar{y}\,u - y\,\bar{u}$ (air).
The expression written above, $y(nu) - \bar{y}(n\bar{u})$, pairs each height with its OWN ray's angle and is
not invariant (a translation $t$ changes it by $t(u^2 - \bar{u}^2)$); the invariant pairs each height with the
OTHER ray's angle. Numeric confirmation from Table 8.2 (the triplet, $y_1 = 1.5$, $u_1 = 0$, $\bar{y}_1 = 0$,
$\bar{u}_1 = 0.36397$): $\Phi = -y_1\bar{u}_1 = -0.5460$, which reproduces the $\phi\Phi$ row of Table 8.4 for all three
lenses, and the image height $\bar{Y}_k = \Phi/(n_{k-1}u_{k-1}) = -0.5460/(-0.15) = 3.640$ matches
the tabulated 3.63966. Recommend correcting the displayed formula when the ch06 deep pass reaches this gem.]

---

### 8.5
**Title:** The "easiest operation first" rule for reverse ray tracing

**Source:** ch06, §6.2.2.2, page 6-2

**Category:** `rule-of-thumb`

**The Gem:**
When working backwards through the paraxial ray trace table (e.g. given image data,
find a surface curvature or spacing), the correct formula is always the one that
requires the fewer write-down steps on a calculator.

Specifically: if computing c (surface curvature) from known ray data, the correct
formula is **(nu - n₋₁u₋₁) / y** divided by **(n' - n)**, NOT y divided by the
difference — because the former can be computed without writing an intermediate
result, while the latter requires it.

Similarly, to find t/n from two known heights: compute **(y₂ - y₁)** first, then
divide by **(nu)** — the operation that avoids writing down the difference is the wrong
order.

**When to use it:**
- Hand calculation or mental arithmetic when solving for unknowns in a layout
- Teaching paraxial optics — helps students remember which formula applies
- Checking a formula before coding: the "easier" version is always correct

**Modern relevance:**
The underlying principle — that the natural computational order of the correct formula
matches the physical causality — is a useful sanity check even when using symbolic
math software. If you have to invent an intermediate variable, you probably have
the formula backwards.

[DEEP-PASS NOTE, ch08: source is ch06 §6.2.2.2; nothing in ch08 confirms or contradicts this gem.]

---


<!-- ================================================================ -->
<!-- CHAPTER 09 -- METHOD OF LENS DESIGN -->
<!-- ================================================================ -->

**Chapter 9 summary (deep pass, verified from the 12-page scan).** Chapter 9 codifies the 1962 iterative
method of lens design as nine steps: choose a lens type (the step that "requires the most experience"),
solve a first order thin lens layout, solve a third order thin lens layout, convert to a thick lens and
compute its aberrations, trace a few meridional and skew fans, adjust the third order coefficients to
balance the higher orders, compute spot diagrams and energy distributions, evaluate the image, and loop
back (usually to step 4). Its technical core is the set of linearized aberration equations 9-(1) to 9-(7),
which relate changes in $\Sigma B, \Sigma F, \Sigma C, \Sigma E, \Sigma P, \Sigma a, \Sigma b$ to changes in curvature,
thickness, index and dispersion, together with the recipe a 1962 computer program used to solve them
(perturb each parameter by 0.01%, finite-difference the derivatives, solve for the changes, iterate). It
contrasts this with the pre-computer split: correct $a$, $b$, $P$ (and $E$) with powers and spacings, then
correct $B$, $F$, $C$ by bending.

The rest of the chapter is evaluation practice. Section 9.2.5 gives a standard ray plan (three axial rays at
1.0, 0.7 and 0.5 of the pupil radius in D, F and C light; three obliquities with at least five meridional
rays each; three skew rays per obliquity) and a standard plot scale (0.01 division = 1 cm = 100 microns).
Figure 9.1 shows how to read the plot (a too-negative Petzval sum tilts the skew curves; over-corrected
spherical aberration ruins the upper meridional rays). Section 9.2.8 judges the image by energy
distribution against the diffraction curve of a perfect lens (Fig 9.2, first dark ring at $Z = 3.83$),
combines the two with $Z_{G+D} = \sqrt{Z_G^2 + Z_D^2}$ (Fig 9.3), and introduces the MTF as the Fourier
transform of the energy distribution (Figs 9.4-9.5). Section 9.3 restates 26 equations from Sections 5, 6
and 8 as a one-page reference. There are no tables. Candidate gems not yet catalogued: the standard ray
plan and plot scale (9.2.5.2-9.2.5.3), overlaying the perfect-lens energy curve on the design's curve
(9.2.8.3), and the automatic differential-coefficient loop (9.2.4.12).

### 9.1
**Title:** Lens bending — shape change without focal length change

**Source:** ch09, §9.2.4.10, page 9-3

**Category:** `shortcut-formula`

**The Gem:**
**Lens bending** changes a lens's surface curvatures (c₁, c₂) while keeping the
focal length fixed. For a thin lens: power φ = (c₁ − c₂)(n − 1). As long as
(c₁ − c₂) is constant, φ is unchanged for any value of c₁.

What bending changes vs. what it preserves:

| Quantity | Changed by bending? |
|----------|---------------------|
| Focal length / power φ | No |
| Petzval curvature P | No |
| Axial & lateral color (a, b) | No (thin lens) |
| Spherical aberration B | Yes — strongly |
| Coma F | Yes |
| Astigmatism C | Yes |

This decouples the first-order design (focal lengths, colors, Petzval) from the
third-order monochromatic design. Fix focal lengths first; bend to hit B, F, C targets.

**Best-form single lens** (minimum spherical aberration for object at infinity):
approximately plano-convex, convex side facing the long conjugate.

**When to use it:**
- After fixing focal lengths and glass types, bend to correct spherical aberration/coma
- Setting rational starting curvatures for computer optimization
- Interpreting what an optimizer is doing when it varies curvatures

**Modern relevance:**
Every modern lens design program bends implicitly when curvatures are variables.
Knowing bending theory gives a rational starting point and helps debug optimization.

**Accuracy / caveats:**
- For thick lenses, keeping (c₁ − c₂) constant slightly changes focal length (principal
  plane positions shift). Solve for c₂ so the paraxial exit angle is unchanged.

✓ Confirmed via ch09 deep pass (§9.2.4.10, pages 9-3 to 9-4, verified from scan): bending is "changing the
shape of a lens without affecting its focal length", using $\phi = (c_1 - c_2)(n-1)$ (Eq 6-(22)). Bending
"has no effect on $a$, $b$ and $P$ for a thin lens and a very small effect in a thick lens" and "affects
primarily $B$, $F$, and $C$", which matches the change table above row for row. The thick lens caveat is
printed as: keeping $(c_1 - c_2)$ constant is not quite the same as fixing the focal length because $f'$
depends on $t$ as well as $(c_1 - c_2)$, so solve for the second curvature to keep the axial ray at a
constant angle with the axis.
[DEEP-PASS NOTE, ch09: the "Best-form single lens ... approximately plano-convex" line is NOT in ch09 (the
chapter never discusses single-lens shape). The ch08 deep pass checked Eq 8-(24) numerically: for $n = 1.5$
and an object at infinity, $B$ is stationary at $c_1 = 1.714/f'$ ($R_1 = 0.583 f'$, $|R_2| = 3.5 f'$), a
biconvex lens, so plano-convex is a near-best form rather than the optimum. The source line should read
"pages 9-3 to 9-4" (the sentence begins at the foot of page 9-3).]

---

### 9.2
**Title:** Diffraction limit check — 2–5 wavelength wavefront rule

**Source:** ch09, §9.2.8.2, page 9-7

**Category:** `sanity-check`

**The Gem:**
Geometric (ray-trace) analysis is reliable only when the system is NOT diffraction-limited:

> **If wavefront departure from a perfect sphere > 2–5 wavelengths:**
> Geometric energy distribution is the accurate performance predictor.
>
> **If wavefront departure < 2–5 wavelengths:**
> Diffraction dominates; geometric spot sizes are overly optimistic. Use wave-optics.

Conrady's wavefront tolerance (referenced in §9.2.8.2) is the classic boundary:
a system meeting it is essentially diffraction-limited.

**When to use it:**
- Deciding whether to run a full MTF/PSF diffraction analysis
- Justifying to a customer that a geometric specification is sufficient
- Setting the aberration design target: if W > 5λ, tighten geometry; if W < 2λ,
  further geometric correction gives no benefit

**Modern relevance:**
All modern lens design programs flag the diffraction-vs-geometry boundary.
The 2–5λ criterion (or λ/4 Maréchal criterion for Strehl ratio) is still standard.

✓ Confirmed via ch09 deep pass (§9.2.8.2, page 9-7, verified from scan): the printed rule is "one does not need
to worry about diffraction effects if the wavefront departs from a perfect sphere by more than two to five
wavelengths", with the departure computable from ray trace data by the method of H. H. Hopkins (Wave Theory
of Aberrations, 1950, pp. 21-23), and "a designer should be familiar with the wavefront tolerances suggested
by Conrady" (Applied Optics and Optical Design, Part 1, pp. 126-141).
[DEEP-PASS NOTE, ch09, FLAG (over-reading, not a formula error): the book states only the upper bound
($W > 2$ to $5\lambda$, diffraction may be ignored). It gives no numerical Conrady tolerance, never mentions
the $\lambda/4$ Marechal criterion, and does not say that below $2$ to $5\lambda$ "diffraction dominates" or that
below $2\lambda$ "further geometric correction gives no benefit". Those are catalog extensions and are too
strong: between about $\lambda/4$ and $2$ to $5\lambda$ both geometry and diffraction matter (see gem 9.3).
Suggest rewording "When to use it" to say diffraction must be considered once $W$ falls below roughly $2$ to
$5\lambda$.]

---

### 9.3
**Title:** Geometric + diffraction combined spot size estimate

**Source:** ch09, §9.2.8.3, page 9-7

**Category:** `shortcut-formula`

**The Gem:**
When geometric and diffraction spot sizes are comparable, estimate the real spot
by combining in quadrature:

    Z_GD ≈ sqrt(Z_G² + Z_D²)

where:
- `Z_G` = geometric spot diameter (from ray trace / spot diagram)
- `Z_D` = diffraction Airy disk diameter = **2.44 · λ · f#**
- `Z_GD` = estimated real spot diameter

**Quick check:**
- `Z_G >> Z_D`: aberration-dominated → improve the geometry
- `Z_G << Z_D`: diffraction-limited → improving geometry won't help
- `Z_G ≈ Z_D`: both matter → use `Z_GD`

**When to use it:**
- Quick estimate of actual resolution when near the diffraction limit
- Comparing geometric and diffraction contributions in a single number
- System-level budgets (combining optical spot with detector pixel size)

**Modern relevance:**
This quadrature approximation appears in imaging-system textbooks and is still
used for informal performance estimation across cameras and sensors.

**Accuracy / caveats:**
- Approximation only (true combined profile is a convolution, not quadrature).
- Does not account for aberration character (coma, defocus have different profiles).

✓ Confirmed via ch09 deep pass (§9.2.8.3, pages 9-7 to 9-8, verified from scan): $Z = \pi Y_e d/(\lambda \ell')$
($Y_e$ exit pupil radius, $d$ spot diameter, $\ell'$ exit pupil to image plane at perfect focus); first dark
ring at $Z = 3.83$, so $d = (3.83\lambda/\pi)(\ell'/Y_e) = 1.22\,\lambda\ell'/Y_e$; and $Z_{G+D} = \sqrt{Z_G^2 + Z_D^2}$
(page 9-8), given as the way to "estimate the energy concentration" when the geometrical curve crosses the
diffraction curve (Fig 9.3). Arithmetic check: $3.83/\pi = 1.219$, and with $D = 2Y_e$ this is
$2.44\,\lambda\ell'/D = 2.44\,\lambda\,(f/\#)$, so the gem's $Z_D = 2.44\lambda f/\#$ is the correct diameter of the
first dark ring.
Supplements: (i) the formula is on page 9-8 (the definition of $Z$ starts on 9-7), not 9-7 alone. (ii) In the
book $Z_G$, $Z_D$, $Z_{G+D}$ are spot diameters in $Z$ units ($Z \propto d$), so the quadrature works equally in
microns. (iii) The book does not say at which energy level to combine. Reading Fig 9.3 at 300 dpi, the dashed
"Estimated Actual Image" curve is reproduced to within about 10% in $Z$ by applying the quadrature at equal
percent energy (60%: $Z_G \approx 4.5$, $Z_D \approx 1.85$ give 4.9, curve about 4.9; 70%: 5.85 and 2.1 give 6.2,
curve about 6.4; 40%: 1.1 and 1.4 give 1.8, curve about 1.95). So $Z_D = 2.44\lambda f/\#$ is right only at the
first-dark-ring (about 84%) level; compare it with the geometric diameter that encloses the same fraction.
(iv) The quadrature-versus-convolution caveat is standard practice, not ch09 text.

---

### 9.4
**Title:** Pre-computer two-step lens design: focal lengths first, bending second

**Source:** ch09, §9.2.4.8–9.2.4.11, pages 9-3 to 9-4

**Category:** `design-heuristic`

**The Gem:**
Before computers, experienced designers solved the multi-variable lens optimization
problem by separating it into two sequential, decoupled steps:

**Step 1 — First-order + Petzval correction** (variables: focal lengths, spacings, glass):
Adjust by trial-and-error to achieve correct focal length, Petzval sum, axial color,
and lateral color. Glass is discrete (catalog steps). Experienced designers did this
intuitively ("a few jabs and you're there").

**Step 2 — Third-order B, F, C correction** (variable: element shapes via bending):
With focal lengths fixed, bend 3 elements to set up 3 equations in 3 unknowns for
spherical aberration, coma, and astigmatism. Or just "jiggle it" — adjust curvatures
by trial while watching B, F, C converge.

Designer slang: **"jiggle it"** or **"poke at it"** — building a feel for how each
surface curvature moves each aberration, then exploiting that feel to converge.

**Why this maps to modern work:**
Step 1 = first-order solver (EFL, BFD, color solves). Step 2 = damped least-squares
optimization over curvatures. The "jiggle" intuition is what separates a designer
who understands physics from one who just runs code.

**When to use it:**
- Approaching a new design from scratch: do Step 1 analytically, Step 2 by bending
- Debugging a computer-optimized lens: identify which variables affect which aberrations
- Teaching lens design: Step 1/Step 2 decomposition makes the problem tractable

✓ Confirmed in outline via ch09 deep pass (§§9.2.4.8-9.2.4.11, pages 9-3 to 9-4, verified from scan): before
large computers, designers "separat[ed] the problem into two parts. First, a solution was found which corrected
$a$, $b$, and $P$, with some consideration given to $E$. Second, this solution was corrected for $B$, $F$, and
$C$." Part one used the focal lengths and spacings (glass index and dispersion were usually not varied "because
glasses are manufactured in finite steps"); part two used bending, by setting up three simultaneous equations,
which experienced designers "seldom actually solved" but approached by trial and error.
[DEEP-PASS NOTE, ch09, FLAG (wording, not a formula): (i) the quotation "a few jabs and you're there" does NOT
appear in ch09; the printed sentence is "It is surprising how rapidly an experienced designer can adjust
variables and arrive at a solution without actually solving the above equations" (§9.2.4.9). (ii) The slang is
printed "jiggle in" or "poke at it", not "jiggle it" (§9.2.4.11). (iii) Step 1 targets are $a$, $b$, $P$ and $E$
(distortion, "some consideration"); "focal length" as a target is our paraphrase. (iv) "Bend 3 elements" is
not stated; the book says only that three simultaneous equations were set up and that "many of the possible
degrees of freedom were not used". (v) The "damped least-squares" mapping is ours: §9.2.4.12 describes an
undamped linearized scheme (Eqs 1-7; perturb each $c$ or $t$ by 0.01%, finite-difference the derivatives, solve
for the changes; minimum sum of squared parameter changes if there are more variables than equations, least
squares on the aberration residuals if fewer) and warns it may fail to converge when the targets are far
from the starting system. Glass was not a variable in 1962 programs.]

---


<!-- ================================================================ -->
<!-- CHAPTER 10 -- TRIPLET OBJECTIVE DESIGN -->
<!-- ================================================================ -->

### 10.1
**Title:** Negative lens minimum thickness — 1/10 diameter rule

**Source:** ch10, §10.4.1.1

**Category:** `rule-of-thumb`

**The Gem:**
When designing a triplet (or any multi-element lens including a negative element),
the minimum center thickness of a **negative (diverging) lens** should be at least:

    t_min ≥ D / 10

where D is the lens clear aperture diameter. This ensures the element has mechanical
rigidity and avoids a dangerously thin edge at the center.

For a lens where the thinnest point is at the edge (a negative meniscus), this rule
applies to the **minimum edge thickness**, not the center.

**When to use it:**
- Setting up starting geometry for a negative element in any triplet or multi-element design
- Checking that an optimizer hasn't produced a mechanically unrealizable thin lens
- Initial thickness budget when element diameters are known but focal lengths are not yet fixed

**Modern relevance:**
Lens design programs will happily produce negative lenses with t → 0 unless constrained.
This rule gives a rational lower bound before entering optimization.

**Accuracy / caveats:**
- For large-diameter elements (>100 mm) or soft materials (plastics, fluorite),
  use a more conservative limit (D/8 or even D/6) to prevent warping and coating stress.

---

### 10.2
**Title:** Triplet glass rule — use identical glass for both positive elements

**Source:** ch10, §10.2.2.1

**Category:** `design-heuristic`

**The Gem:**
In a triplet (positive–negative–positive), the two **positive crown elements should
use the same glass type**. This is not just a cost/inventory convenience — it is
optically motivated:

1. **Lateral color** is determined by `ȳ·φ/V` for each element. With identical V for
   both crowns and a properly placed negative (different V), lateral color can be
   eliminated while independently correcting axial color.
2. **Petzval sum** depends only on powers and indices; same glass for both crowns
   simplifies the Petzval equation to one free variable (the negative element index).
3. **Bending freedom**: with symmetric glass choice, the designer retains full bending
   freedom on both crown elements independently, giving 2 free variables for coma
   and spherical correction.

**When to use it:**
- Starting a triplet design from scratch: choose one crown glass, one flint glass
- Evaluating whether an existing triplet glass choice is sub-optimal
- Understanding why most classic triplets (Cooke, Tessar) use only two glass types

**Modern relevance:**
All standard triplet starting points in lens design software use this glass pairing.
Violating it (three different glasses) adds complexity without optical benefit in most
cases.

---

### 10.3
**Title:** Deliberate under-correction of 3rd-order aberration to balance 5th order

**Source:** ch10, §10.5.1

**Category:** `design-heuristic`

**The Gem:**
At large apertures, **5th-order spherical aberration is significant and has the opposite
sign to 3rd-order** in most lens forms. If you zero the 3rd-order aberration exactly,
5th-order residual becomes the dominant error and limits performance.

Better strategy:
1. **Leave a deliberate residual of 3rd-order undercorrection** (b₃ slightly negative)
2. Choose the magnitude so that 3rd and 5th order aberrations **partially cancel** in
   the zone where the energy concentration is highest
3. The balanced blur is smaller than if either order were minimized alone

The optimal balance point (Strehl maximization) is roughly:
- Residual 3rd-order = **−0.5 × (5th-order contribution)** in sign and magnitude

**When to use it:**
- Final stages of a triplet or doublet design at f/3.5 or faster
- When ray fan shows residual "turned-down edge" (5th-order signature)
- When tightening 3rd-order correction makes overall performance worse (paradox explained here)

**Modern relevance:**
Modern optimizers with wave-optics merit functions do this automatically, but without
understanding the 3rd/5th balance the designer can't explain optimizer behavior or set
rational constraints.

---

### 10.4
**Title:** "Boxing in" — plot aberrations vs. one parameter to bracket the solution

**Source:** ch10, §10.2.2.4

**Category:** `design-heuristic`

**The Gem:**
When a design has one remaining free variable (a curvature, spacing, or glass property),
plot **two aberration quantities against that variable** on the same axes and read off
the crossing point — the design that satisfies both constraints simultaneously.

Classic triplet application:
- X-axis: secondary color (TAch_F−D) or ΣP (Petzval sum)
- Y-axis: spherical aberration or coma residual
- Vary the negative element curvature or glass V-number
- Two curves cross where both are simultaneously corrected

This is the pre-computer substitute for a 2×2 simultaneous equation solve. The graph
immediately shows whether a feasible solution exists (curves cross) and whether it is
unique (curves are nearly parallel = multiple solutions or near-singular system).

**When to use it:**
- When you have one free variable and two performance constraints
- Diagnosing whether a design is over-constrained (curves don't cross)
- Understanding the "design space" before committing to a solution

**Modern relevance:**
Equivalent to a 1D sensitivity scan in a modern optimizer. Still the fastest way to
understand single-variable tradeoffs and present design choices to a customer.

---

### 10.5
**Title:** Left-hand vs. right-hand triplet solutions — both always exist, R≈1 is near-optimal

**Source:** ch10, §10.8.1

**Category:** `design-heuristic`

**The Gem:**
For any triplet design, there are always **two solutions** — "left-hand" and
"right-hand" — that are mirror images of each other (reverse the element order and
flip all curvatures). Both have identical on-axis performance.

The shape parameter **R = (c₁ + c₂) / (c₁ − c₂)** controls the bend of each element
(analogous to the bending parameter X for a singlet). For a triplet:

- **R = 0**: symmetric element (equiconvex or equiconcave)
- **R ≈ +1 or −1**: one plane surface (plano-convex / plano-concave)

**Near-optimal bending** for minimum zonal spherical aberration in a triplet typically
occurs near **|R| = 1** for the positive elements — i.e., the plano-convex form with
the plane face toward the parallel-light gap. This is not a coincidence: the plane face
produces zero deviation there, minimizing higher-order contributions.

**When to use it:**
- Choosing initial curvatures for a triplet: start with plano-convex crowns
- When two solutions from a solver look identical on paper (L/R symmetry explains it)
- Deciding which hand to use for assembly orientation (mechanical clearance may differ)

**Modern relevance:**
Modern solvers often find both solutions in a multi-start optimization. This gem
explains why and how to choose between them.

---


<!-- ================================================================ -->
<!-- CHAPTER 11 -- TELESCOPE OBJECTIVES -->
<!-- ================================================================ -->

### 11.1
**Title:** Fraunhofer doublet orientation — low-dispersion positive element in front

**Source:** ch11, §11.2.2.3, §11.2.3.1

**Category:** `design-heuristic`

**The Gem:**
A cemented achromatic doublet (crown + flint) can be oriented two ways:
- **Fraunhofer form**: crown (low-dispersion) element **in front** (facing the long conjugate)
- **Steinheil form**: flint element in front

**Rule:** Put the positive, low-dispersion element in front. The book's reasoning is
about the **axial rays**: the left-hand solution with the positive lens in front "has
the most favorable shape for the passage of the axial rays", which is why most
telescope objectives are of this type (§11.2.2.3). The book also finds that solutions
with the negative lens in front "appear to offer no advantages over the Fraunhofer
type" and drops them from further discussion (§11.2.3.1).

The handbook gives no off-axis, coma, or field-angle argument for the choice, and no
quantitative field-of-view advantage. Treat the rule as a default shape preference
grounded in the on-axis ray path, not as a field-coverage rule.

**When to use it:**
- Orienting a doublet in a telescope, binocular, or collimator design: start with the
  positive low-dispersion element facing the long conjugate
- Deviate (negative element in front, often called the Steinheil form in modern usage;
  the book does not use that name) only with a specific reason the handbook does not supply

**Modern relevance:**
Nearly all modern commercial doublets ship in the Fraunhofer orientation. This explains
why, and when to deviate.

✓ Confirmed via ch11 deep pass: §11.2.2.3 (page 11-4) verified verbatim against scan.
✓ Confirmed 2026-09-18 by independent re-derivation (Devin + Claude-agree): mechanism
reworded to the book's own axial-ray reasoning; the earlier chief-ray/angle-of-incidence
mechanism and the "1.5–2× field" figure are not in the chapter and were removed.

---

### 11.2
**Title:** Petzval curvature scaling — eyepiece dominates; objective contribution shrinks as 1/MP

**Source:** ch11, §11.1.3.6–11.1.3.8

**Category:** `shortcut-formula`

**The Gem:**
In a visual telescope (objective + eyepiece), the total Petzval field curvature seen
at the eyepiece exit is:

    α_y ∝ φ_e · (1/γ_e − 1/(γ_o·MP))                                  (Eq. 3 bracket)

where P_o = −φ_o/γ_o and P_e = −φ_e/γ_e (γ_o ≈ 1.5 for a doublet; γ_e ≈ 0.7–2.6 for
eyepieces), and MP is the magnifying power. The objective-to-eyepiece contribution
ratio is therefore

    |objective / eyepiece| = γ_e / (γ_o · |MP|)    →    1/|MP| when γ_o = γ_e

The suppression is **linear in MP**, not quadratic. For γ_o = γ_e = 1.5:
- MP = 10×: objective contributes ~10% of the eyepiece term (~10× smaller)
- MP = 6×: ~17% (~6× smaller)
- MP = 2×: 50% (not negligible)

The objective term enters with the opposite sign for erect (positive-MP) instruments
and the same sign for inverting (negative-MP) ones; Table 11.1 uses negative MP.

**Implication:** At high power the **objective's Petzval curvature is a minor
contribution**. The book's conclusion (§11.1.3.8): for high-power telescopes the
objective adds a negligible amount of field curvature, which is why most telescopes use
simple doublets; at low power one must consider a flatter-field objective. Spend the
field-curvature effort on the eyepiece, and on the objective only when a reticle sits in
its focal plane (§11.1.3.7) or the power is low.

The handbook gives no numeric MP or |P_obj|/|P_eye| threshold for "negligible".

**When to use it:**
- Deciding whether to use a doublet or more complex objective
- Allocating field curvature between objective and eyepiece
- Evaluating whether an existing objective's Petzval spec matters for a visual instrument

**Modern relevance:**
This scaling still applies in any compound visual instrument. Modern designs often waste
engineering effort on objective field curvature that is negligible in the system.

✓ Confirmed via ch11 deep pass: Eqs. 1-3 (§11.1.3.1-11.1.3.4, page 11-1/11-2) transcribed
and verified from scan.
✓ Confirmed 2026-09-18 by independent re-derivation (Devin + Claude-agree): the Eq. (3)
bracket gives 1/MP suppression, and it reproduces Table 11.1 exactly (α = 0.0315·(2/3)(1−1/MP)
rad → 108′, 87′, 79′ at MP = −2, −5, −10). The earlier "1/MP²", "100× smaller", and
"P_obj ≤ 0.5·P_eye at MP ≥ 3" quick-check were unsupported and removed.

---

### 11.3
**Title:** Zonal aberration tolerance for diffraction-limited doublet

**Source:** ch11, §11.3.3.1–11.3.3.2

**Category:** `sanity-check`

**The Gem:**
A doublet corrected to zero third-order spherical aberration always has residual
**zonal aberration** (5th-order residual). The doublet is diffraction-limited when:

    (Y_k)_zone = 4.6λ / L_{k-1}

where:
- `(Y_k)_zone` = transverse zonal ray error (same length units as λ), with the marginal
  ray at Y₁max adjusted to Y_k = 0
- `L_{k-1}` = **optical direction cosine of the emerging ray** at the marginal aperture,
  ≈ sin U′ ≈ 1/(2·f/#). It is dimensionless, not a focus shift.
- λ = wavelength

Because L ≈ 1/(2·f/#), the tolerance depends on f-number only, not on focal length:
(Y_k)_zone ≈ 4.6λ · 2·(f/#) ≈ 9.2·λ·(f/#).

Worked examples:
- Book (Table 11.6, f/3.57, L ≈ 0.14, λ = 0.5893 µm): 4.6 × 0.5893 / 0.14 ≈ 19.4 µm = 0.0194 mm
- f/10 (L ≈ 0.05, λ = 0.55 µm): 4.6 × 0.55 / 0.05 ≈ 50 µm ≈ 0.05 mm

**When to use it:**
- Checking whether a doublet design is truly diffraction-limited, not just 3rd-order corrected
- Setting the tolerance on zonal aberration in a specification
- Deciding whether to use an air-spaced doublet (better zonal) vs. cemented

**Modern relevance:**
Lens design programs report the zonal ray error directly. This formula tells you the
allowable value without running a full wave-optics calculation.

✓ Confirmed via ch11 deep pass: the tolerance equation $(Y_k)_{zone} = 4.6\lambda/L_{k-1}$
(§11.3.3.1, page 11-12) transcribed and verified from scan.
✓ Confirmed 2026-09-18 by independent re-derivation (Devin + Claude-agree): the book
defines L_{k-1} as the emerging ray's optical direction cosine (0.14 ≈ 1.4/10 = 1/(2×3.57)
for Table 11.6), so the earlier "focus shift" gloss and the 0.01 mm f/10 example were wrong.

---

### 11.4
**Title:** Air-spacing a doublet to reduce zonal spherical aberration

**Source:** ch11, §11.3.4.3

**Category:** `design-heuristic`

**The Gem:**
Introducing an **air space** between the crown and flint elements of a doublet gives
an additional degree of freedom that allows the 5th-order (zonal) spherical aberration
to be reduced independently of the 3rd-order correction.

The book reports that the zonal aberration is reduced "to a remarkable degree" by
this method (§11.3.4.3, Figures 11.4–11.6) but gives no single reduction factor.

Design sequence for air-spaced doublets:
1. Correct 3rd-order spherical + chromatic aberration by choosing glass and bending
2. Adjust the air-gap to reduce zonal: larger gap generally reduces the zonal residual
   but increases higher-order coma
3. Balance: the optimum gap depends on the glass pair. In Table 11.9's optimized
   solutions (f′ = 10 cm) the air space t₂ runs from about zero (a few solutions print
   ≈0 or slightly negative) up to 0.74 cm, i.e. roughly 0.4–7.4% of f′, and is largest
   for the largest Δν (Δν = 36.7 gives 7.4%; Δν ≈ 28 gives ≈0.4% or less)

**When to use it:**
- Any objective faster than f/8 in visible light where diffraction quality is needed
- When a cemented design fails the zonal tolerance (11.3)
- Comparing bid designs: an air-spaced doublet at same f/# will outperform cemented

**Modern relevance:**
All high-quality telescope objectives (APO doublets, survey telescope primaries) are
air-spaced for exactly this reason. This gem explains the physical mechanism.

**Accuracy / caveats:**
- Air-spaced doublets are sensitive to element tilt (decenter adds coma). Alignment
  tolerance must be tighter than for cemented.

✓ Confirmed via ch11 deep pass: §11.3.4.3 (page 11-12) transcribed and verified from scan.
✓ Confirmed 2026-09-18 by independent re-derivation (Devin + Claude-agree), including a
re-read of the Table 11.9 t₂ column against the scan: the "3–5×" figure and "typically
1–3%" range are not in the chapter and were replaced by the table's actual span.

---

### 11.5
**Title:** Secondary spectrum threshold — when correction is not worth it (f' < 65.8 cm at f/16.7)

**Source:** ch11, §11.4.6, page 11-25

**Category:** `sanity-check`

**The Gem:**
A simple achromatic doublet has residual **secondary spectrum** (chromatic error that
a normal two-glass achromat cannot eliminate). Before designing an apochromat triplet,
check whether the secondary spectrum is even visible:

$$\text{OPD}_\text{secondary} = Y_k \cdot \frac{Y_1}{2f'}$$

For the standard doublet, the secondary-spectrum focus shift is $f'/2200$ (longitudinal;
see §6.10.8 and Eq. 13). At f-number $F$ the marginal ray meets the axis at slope
$\tan U' \approx 1/(2F)$, so the **transverse** aberration is

$$Y_k \approx \frac{f'}{2200}\cdot\frac{1}{2F} = \frac{f'}{4400\,F}$$

The marginal ray height is $Y_1 = f'/(2F)$, so

$$\text{OPD} = Y_k \cdot \frac{Y_1}{2f'} = \frac{f'}{4400\,F}\cdot\frac{f'}{2F}\cdot\frac{1}{2f'} = \frac{f'}{17{,}600\,F^2}$$

At f/16.7 ($F^2 = 278.9$) this is $\text{OPD} \approx f'/4.9\times10^{6}$. The book's own
number uses its ray-traced $Y_k = 0.00015$ cm for $f' = 10$ cm, giving OPD = 0.038
wavelengths (λ = 0.5893 µm).

Setting OPD = λ/4 (Rayleigh criterion): OPD grows linearly with $f'$, so

$$f'_\text{threshold} = 10\text{ cm}\times\frac{0.25}{0.038} \approx 65.8\text{ cm}$$

(The closed form $f'/4.9\times10^{6}$ with λ = 0.55 µm gives about 67 cm, the same
answer to within the rounding of $Y_k$.)

**Rule:** At f/16.7, a doublet with $f' < 65.8$ cm has secondary spectrum
**below the Rayleigh diffraction limit** — no apochromatic correction is needed.
To gain a 2× improvement over a doublet, the triplet must be scaled to $f' > 131.6$ cm.

Scaling with f-number: from OPD $= f'/(17{,}600\,F^2)$ the threshold focal length
scales as $F^2$.

**When to use it:**
- Go/no-go check before committing to apochromat design
- Deciding whether expensive anomalous-dispersion glass is justified
- Comparing doublet vs. triplet bids: if f' < threshold, the doublet wins on cost/complexity

**Modern relevance:**
Modern software will show secondary spectrum, but this formula gives a quantitative
threshold without running a design. The result — "no point correcting secondary spectrum
below 65.8 cm at f/16.7" — is rarely stated explicitly in modern texts but is directly
derivable from the Rayleigh criterion and the universal 1/2200 secondary spectrum rule.

**Accuracy / caveats:**
- Threshold scales with wavelength and f-number; formula above is for visible (0.55 µm)
- Rayleigh λ/4 is a practical, not physical, limit — some applications require tighter OPD
- For non-visual applications (photographic, UV, IR), the threshold focal length changes

✓ Confirmed via ch11 deep pass: OPD equation (§11.4.6, page 11-25) transcribed and
verified from scan.
✓ Confirmed 2026-09-18 by independent re-derivation (Devin + Claude-agree): the earlier
intermediate step (f′/73,480) was transverse aberration mislabeled as OPD and did not
reproduce 65.8 cm; the chain above does. Final numbers (0.038λ, 65.8 cm, 131.6 cm, 7.9 cm)
are unchanged and match §11.4.6.

---

### 11.6
**Title:** Herzberger P\*/P\*\* collinearity rule — three-glass apochromat selection on the glass map

**Source:** ch11, §11.4.2–11.4.3, Eqs. 14–22; M. Herzberger, *Optica Acta* **6**, 197 (1959)

**Category:** `design-heuristic`

**The Gem:**
Three thin, closely spaced glasses can bring F, D, and C to a common focus (Eqs. 14–16).
Two different determinants then govern the result; the book uses the symbol Δ only for
the first.

**1. Δ (Eq. 20): element powers.** Δ = det[P̃\*, ν, 1] is the triangle area of the three
glasses on the **P̃\* vs ν** plot, and each element power is $\phi_i \propto 1/\Delta$
(Eqs. 17–19). A larger triangle means smaller, better-balanced element powers.

$$\Delta = \begin{vmatrix} \tilde{P}^*_a & \nu_a & 1 \\ \tilde{P}^*_b & \nu_b & 1 \\ \tilde{P}^*_c & \nu_c & 1 \end{vmatrix} \neq 0$$

**2. Eq. (21)/(22) numerator: residual at a fourth wavelength λ.** With $\tilde{P}^{**} =
\tilde{P}_{\lambda-D}$, the residual transverse aberration at λ is proportional to

$$D_\lambda = \begin{vmatrix} \tilde{P}^*_a & \tilde{P}^{**}_a & 1 \\ \tilde{P}^*_b & \tilde{P}^{**}_b & 1 \\ \tilde{P}^*_c & \tilde{P}^{**}_c & 1 \end{vmatrix} \Big/ \Delta$$

$D_\lambda$ vanishes when the three glasses are **collinear on the P̃\* vs P̃\*\* diagram**
(Fig. 11.11), so that λ also shares the common focus. Herzberger's notation:
$\tilde{P}^*$ and $\tilde{P}^{**}$ are normalized partial dispersions, precursors of the
modern $\Delta P_{g,F}$ anomalous-dispersion values.

**Practical implications:**
- Nearly all standard glasses lie on a single "normal glass line". Three glasses on
  that line are collinear on the P̃\* vs ν plot too, so Δ → 0 and the element powers
  become singular (infinite). "Any three normal glasses" therefore does **not** work;
  the statement holds only for non-collinear triples (finite-area triangle in P̃\*–ν).
- Glasses **off** the normal line (anomalous dispersion: FK, PK, fluorite, KzFS types)
  give a finite triangle and manageable power distribution
- Fixing a non-collinear P̃\*–ν triple fixes F, D, C focus; how well a further
  wavelength λ focuses is set separately by $D_\lambda$ (Fig. 11.11: the book's sample
  glasses are not collinear on P̃\*–P̃\*\*, leaving residuals at A′, e, g)

**Glass selection recipe (from §11.4.2):**
1. Plot candidate glasses on the P\* vs P\*\* diagram (or equivalent modern $P_{g,F}$ vs ν map)
2. Pick one anomalous-dispersion glass far from the normal line
3. The other two glasses can be from the normal glass line
4. Compute element powers from Cramer's rule; reject solutions with |φ_element| >> φ_total

**When to use it:**
- First pass at glass selection for a triplet apochromat before any numerical optimization
- Explaining why most apochromats require at least one special/anomalous glass
- Evaluating whether a new glass type enables a better-balanced apochromat

**Modern relevance:**
The modern equivalent is the $P_{g,F}$ vs $\nu$ Abbe diagram with the "normal glass line"
marked. Anomalous-dispersion glasses (ED glass, fluorite, FPL-53, etc.) are the current
industry standard for apochromatic triplets for exactly the reason this gem explains.
The Herzberger P\*/P\*\* notation has been superseded but the geometric collinearity
argument is unchanged.

**Accuracy / caveats:**
- The collinearity condition is necessary but not sufficient: even with collinear glasses,
  the resulting element powers may be so extreme as to make the triplet impractical
- Higher-order (5th-order) spherical aberration may dominate if element powers are large
  — the handbook's sample design (§11.4.5) shows this forces large f-numbers (f/11–f/16.7)

✓ Confirmed via ch11 deep pass: Eqs. 14-22 (§11.4.2-11.4.3.5, pages 11-19/11-21) and
the Table 11.13/11.14 sample-design data (page 11-23/11-24) transcribed and verified
from scan, matching the f/11-f/16.7 result.
✓ Confirmed 2026-09-18 by independent re-derivation (Devin + Claude-agree): wording
corrected so element powers scale as 1/Δ (area scales as Δ), the two determinants are
distinguished, and the "any three normal glasses" claim is restricted to non-collinear
triples. The earlier headline ("primary and secondary corrected iff Δ = 0 on P̃\*–P̃\*\*")
conflated the two; per Eqs. 15–16 and 22, F/D/C correction needs Δ ≠ 0 and the P̃\*–P̃\*\*
collinearity condition governs the residual at a further wavelength.

---


<!-- ================================================================ -->
<!-- CHAPTER 12 -- LENS RELAY SYSTEMS -->
<!-- ================================================================ -->

### 12.1
**Title:** Relay system fundamental tradeoff — secondary color vs. field curvature

**Source:** ch12, §12.4.6 and §12.7.4

**Category:** `design-heuristic`

**The Gem:**
In any lens relay system there is an **inescapable tradeoff**:

> **Any design change that reduces secondary color will increase field curvature,
> and vice versa.**

Mechanisms:
- Reducing secondary color → shorten element focal lengths (more power per element)
  → more Petzval curvature per element
- Reducing field curvature → use special glass with higher effective index ng
  → changes dispersion balance → more secondary color

**Quantitative rule (secondary color in a relay):**
    TAch_F-D ≈ u₀ · D / 2200          (cm; two doublets butted together, no air gap)

where u₀ = marginal ray angle (= exit pupil radius / relay length), D = total relay
length. Reducing secondary color requires reducing u₀ (smaller exit pupil) OR using
special glass — both have costs.

**A second, no-redesign lever — separate the doublets:**
If the two relay doublets are kept afocal (parallel light between them) but pulled
apart by a free-space gap d, the secondary color drops to:

    TAch_F-D ≈ u₀ · (D − d) / 2200

Increasing d costs nothing optically in the gap itself (free space has no dispersion),
but it forces each doublet's focal length to shrink to keep the total length D fixed —
which is exactly what raises the Petzval sum. This is the same tradeoff in a directly
tunable form: dial in d to trade secondary color for field curvature without changing
aperture or speed.

**When to use it:**
- Justifying a relay design that has residual secondary color (field curvature was the priority)
- Deciding whether to spec secondary color or field curvature as the harder constraint
- Understanding why complex relay designs (with special glass) have degraded field flatness
- Tuning an existing doublet-relay layout by adjusting the inter-doublet air gap d rather
  than re-optimizing the glass

**Modern relevance:**
This tradeoff persists in borescopes, endoscopes, periscopes, and relay trains in
any optical instrument. Engineers who don't know it waste time fighting a fundamental
limitation.

---

### 12.2
**Title:** Double-relay Petzval penalty — 6× more field curvature, same secondary color

**Source:** ch12, §12.6.5

**Category:** `shortcut-formula`

**The Gem:**
If the relay train is split into **two half-length relays** (with a field lens between)
to reduce lens diameter, the field curvature increases drastically:

| Quantity | Single relay | Double relay |
|----------|-------------|--------------|
| Max lens diameter | D_lens | D_lens / 2 |
| Secondary color (TAch) | baseline | **same** |
| Petzval field curvature | P | **6 × P** |

The 6× factor comes from:
- Each relay element is 2× shorter → 2× more Petzval each → relay contribution ×4
- Field lens adds as much as one relay element → +2× → total ×6

**Design rule:** Never split a relay unless the lens diameter constraint is hard and
unavoidable. The field curvature penalty is severe and usually harder to correct than
the original diameter problem.

**When to use it:**
- Comparing single vs. double relay options in a periscope or borescope design
- Justifying why a larger (single) relay is better than two smaller ones
- Predicting the field curvature penalty before running a full design

---

### 12.3
**Title:** Field-of-view reduction in relay — don't stop it down for free field

**Source:** ch12, §12.6.6

**Category:** `design-heuristic`

**The Gem:**
If a relay system produces a blurred field edge but the eyepiece is capable of showing
a wider (blurred) field, **do not add a stop to cut off the blurred field edge**.

Reasoning:
- A stop at the intermediate field plane adds no optical quality benefit
- The relay aberrations still exist for rays that do pass through
- The cost (hardware, alignment) is non-trivial
- The user loses field of view with no resolution benefit at the center

**Rule:** The field of a visual instrument should **not** be reduced if the extra
blurred field can be obtained at no increase in cost and instrument size.

Exception: if the blurred edge creates confusion (overlapping objects, bright
artifacts) that impairs the user's interpretation of the center image, a stop is
justified. For most observation tasks, wide-but-blurry is preferred to narrow-but-sharp.

**When to use it:**
- Finalizing relay field stop specifications
- Customer discussions: "why is the edge soft?" → because stopping down trades
  field for nothing
- Periscope and borescope design tradeoff presentations

---

### 12.4
**Title:** Relay Petzval contribution — negligible when < 50% of eyepiece contribution

**Source:** ch12, §12.3.4

**Category:** `sanity-check`

**The Gem:**
A relay objective does not need a low-Petzval design if its Petzval contribution is
small compared to the eyepiece's:

    |P_relay| ≤ 0.5 × |P_eyepiece|  →  relay Petzval is negligible

Worked example (from text): Erfle eyepiece has P_eye = −0.2125 cm⁻¹. A pair of
f/3.5, 35 cm doublets gives P_relay = −0.038 cm⁻¹ — only 18% of the eyepiece
contribution → negligible. Standard doublet objectives are sufficient.

**When to use it:**
- Quick go/no-go check before deciding to use a field-flattened relay objective
- Prioritizing design effort: if relay P < 50% of eyepiece P, optimize the eyepiece first
- Avoiding over-engineering: triplet or double-Gauss relay is only needed when
  doublet relay fails this test

**Modern relevance:**
This threshold applies to any instrument with a compound objective + eyepiece. It
prevents gold-plating the objective when the eyepiece is the bottleneck.

---

### 12.5
**Title:** Trim the exit pupil to kill secondary color — no redesign needed

**Source:** ch12, §12.4.4

**Category:** `rule-of-thumb`

**The Gem:**
Secondary color in a relay scales linearly with the marginal ray angle u₀ (equivalently,
with exit pupil diameter). If the residual chromatic blur is objectionable, **stopping
down the exit pupil** is a free, no-redesign fix:

Worked example: u₀ = 0.14 gives a 7 mm exit pupil (desirable for max light transmission)
and 6.6 arcmin of secondary color blur (noticeable but tolerated). Reducing the exit
pupil to 2 mm — still large enough that the observer's own eye resolution is the limit,
not the pupil — cuts the secondary color proportionally, down to 2.2 arcmin.

**When to use it:**
- A visual instrument's secondary color is marginal/objectionable and a full redesign
  (special glass, relay resizing) isn't justified
- Trading light transmission for image quality in low-light-tolerant applications
  (daylight sights, high-magnification scopes)
- Quick sanity check: is the current exit pupil larger than it needs to be for the
  observer's eye, leaving margin to trade away?

**Modern relevance:**
The human eye's pupil rarely exceeds ~2–3 mm in bright conditions and ~5–7 mm fully
dark-adapted; oversized exit pupils in a visual design are wasted light-gathering that
could instead be spent buying back chromatic performance. Still a standard lever in
riflescope, periscope, and binocular design today.

**Accuracy / caveats:**
- Only applies to visual (eye-limited) systems; a photographic/sensor relay has no such
  "free" pupil margin — the sensor collects whatever light the pupil passes
- Below ~2 mm exit pupil, diffraction and reduced light transmission become the limiting
  factors instead

---

### 12.6
**Title:** Symmetric doublet pairing cancels coma "for free"

**Source:** ch12, §12.5

**Category:** `design-heuristic`

**The Gem:**
When two **identical** lens elements are faced toward each other in mirror-image
orientation around a symmetric (unit-magnification, afocal) relay, **coma cancels
between them regardless of how well-corrected either element is individually.**

Worked example (from text): bending a doublet solution until the curvature facing the
parallel-light side is c₁ = 0 (making the positive element a plano-convex singlet)
destroys the doublet's own coma correction. But butting two such bent doublets together
front-to-front lets the two plane surfaces contact, forming a single equiconvex lens
from the two positive elements. The uncorrected coma of one doublet is equal and
opposite to the other's — **it subtracts to zero by symmetry**, while spherical
aberration (an even-symmetry aberration) simply adds.

**When to use it:**
- Reducing element/surface count in a symmetric relay without reintroducing coma
- General classical-design principle: any strictly symmetric system (same magnification
  magnitude in front of and behind the stop, mirrored elements) has zero coma and zero
  distortion by construction — this is the same principle behind symmetric wide-field
  and process lenses
- Deciding which aberrations you still need to independently control (spherical, since
  it does NOT cancel) after exploiting symmetry for coma

**Modern relevance:**
The symmetry principle is a foundational classical design shortcut still used to seed
starting points for lens optimizers — it hands you coma- and distortion-free designs
"for free" before a single ray is traced, and it also predicts what will NOT cancel
(spherical, and field curvature) so optimization effort can be focused correctly.

**Accuracy / caveats:**
- True symmetry requires equal magnitude conjugates on each side (unit magnification
  here); breaks down as soon as the magnification deviates from exact symmetry
- Higher-order spherical aberration still accumulates and may dominate — the text notes
  the resulting triplet-like relay has "considerably more higher order spherical
  aberration than the two doublets," so this trades coma for a spherical-aberration risk

---

### 12.7
**Title:** Never put an optical surface at an internal focal plane — it collects dust in sharp focus

**Source:** ch12, §12.6.8

**Category:** `rule-of-thumb`

**The Gem:**
In any relay or field-lens design, **avoid placing a lens surface directly at an
intermediate (internal) focal/image plane.** Any dust, scratches, or coating defects
on that surface will be imaged in perfect focus onto the final image, right along with
the scene.

**When to use it:**
- Placing field lenses, reticles, or graticules — offset the surface slightly from the
  exact conjugate, or accept the defocus cost if the surface must carry a reticle pattern
- Periscope, borescope, endoscope, and any relay-train design with accessible internal
  image planes
- Root-causing a field-defect complaint on a shipped instrument that traces back to a
  lens surface at (or too near) an internal focal plane

**Modern relevance:**
Identical failure mode still bites modern designs: sensor cover glass, field lenses,
and reticle substrates placed exactly at a field stop or image plane will image dust and
scratches with full sharpness. A deliberate small defocus offset is the standard fix.

---


<!-- ================================================================ -->
<!-- CHAPTER 13 -- MIRROR AND PRISM SYSTEMS -->
<!-- ================================================================ -->

### 13.1
**Title:** Even/odd reflection parity — predicting image handedness

**Source:** ch13, §13.4.4.2

**Category:** `rule-of-thumb`

**The Gem:**
Every mirror reflection **reverses the handedness** of the image (switches a
right-handed coordinate system to left-handed and vice versa). After N reflections:

- **N even** → final image has the **same handedness as the object** (right-reading,
  erect coordinate system) — same as a refracting system
- **N odd** → final image has **reversed handedness** (mirror-image, left-reading)

Quick consequence table:

| N reflections | Example | Image type |
|---------------|---------|------------|
| 0 | Pure refracting system | Erect (same hand) |
| 1 | Single flat mirror | Reversed (mirror image) |
| 2 | Porro prism, periscope | Erect again |
| 3 | Roof Porro, dove prism | Reversed again |
| 4 | Porro + roof | Erect |

**Practical use:** Count the reflections (not the prism elements — a roof adds two
reflections from a single prism). If the count is wrong, add or remove one flat mirror
in the folding path to fix handedness without changing the optical path length.

**When to use it:**
- Designing erecting systems (rifle scopes, binoculars, periscopes)
- Checking prism train handedness before prototype build
- Quickly diagnosing an image inversion problem in a prism/mirror system

**Modern relevance:**
Optical design software tracks handedness automatically, but this rule is the fastest
way to check it mentally and avoids errors when modifying a system.

---

### 13.2
**Title:** Mirror rotation rule — rotating a mirror by θ moves the image by 2θ

**Source:** ch13, §13.5.1.3

**Category:** `shortcut-formula`

**The Gem:**
When a flat mirror is rotated by angle **θ** (about any axis in the mirror plane),
the reflected beam rotates by **2θ**:

    Δ(image angle) = 2 × Δ(mirror angle)

This is an exact geometric result (not a small-angle approximation) for a flat mirror.
It follows directly from the reflection law: angle of reflection = angle of incidence.

**Key applications:**
1. **Scanning mirrors** (galvanometers, MEMS): mirror scan of θ gives image scan of 2θ.
   Angular resolution of scanner = half the mirror angular resolution.
2. **Alignment**: tilting a mirror by 1 arcminute to correct image pointing moves
   the image by 2 arcminutes.
3. **Kinematic mounts**: a mirror on a single-axis adjustment requires half the
   angular travel to achieve a given beam correction.
4. **Autocollimator**: reads 2× the mirror rotation — built into the calibration.

**When to use it:**
- Sizing scanner actuator travel for a MEMS or galvo beam-steering system
- Computing pointing correction from a mirror tilt measurement
- Calibrating a mirror-based alignment telescope or autocollimator

**Modern relevance:**
Identical in current scanning and beam-steering systems. The 2× factor is often
forgotten when converting between mirror angle and beam angle in pointing budgets.

---

### 13.3
**Title:** Mirror folding-out principle — analyze any mirror system as a refracting system

**Source:** ch13, §13.2 (referencing back to §5.1.2.2)

**Category:** `design-heuristic`

**The Gem:**
Any system of flat mirrors can be **"unfolded"** — replaced by an equivalent straight
optical axis with refracting (transmitting) elements in place of each mirror:

1. At each mirror, replace the mirror with a **transmitting plane** at the same
   location
2. "Unfold" the optical path by reflecting the downstream elements through the mirror plane
3. The resulting straight system has the same first-order properties (focal length,
   object/image positions, magnification) as the folded mirror system
4. Aberration analysis of the unfolded system is valid (adding a flat mirror
   introduces no aberrations)

**This means:** Any paraxial or aberration analysis method developed for refracting
systems applies immediately to mirror systems after unfolding. No special mirror
formulas needed.

**Extension (curved mirrors):** A curved mirror of radius R in medium n is equivalent
to a refracting surface of power φ = −2n/R (negative because reflection reverses
the direction). Unfold and treat as a thin lens.

**When to use it:**
- Analyzing a periscope, Porro prism chain, or any folded relay
- Applying paraxial trace methods to a mirror-based system
- Checking whether a prism introduces aberrations (flat-sided prisms: none;
  curved prisms: use equivalent lens)

**Modern relevance:**
All modern lens design programs unfold mirror systems internally. This gem explains
what the software is doing and why flat mirrors can be replaced with "dummy" surfaces
in CODE V, Zemax, etc.

**Accuracy / caveats:**
- Valid only for flat mirrors. Curved mirrors do introduce aberrations — the equivalent
  thin-lens power formula applies, but higher-order terms differ from a refracting surface.
- The unfolded path length must equal the physical path length for correct image location.

---

### 13.4
**Title:** Prism family quick-selector — deviation angle, image orientation, and glass-path cost

**Source:** ch13, §13.10.2–13.10.28 (Prism Data Sheets)

**Category:** `reference-data`

**The Gem:**
MIL-HDBK-141 catalogs ~20 named reflecting-prism designs, each solving a different
combination of (beam deviation angle, image orientation, and size/weight budget).
Rather than deriving a new fold from scratch, pick the closest match from this
consolidated table (t/n normalized to entrance aperture A = 1.00, BK7-type glass
n = 1.517 unless noted):

| Prism | Deviation δ | Image orientation | Relative glass path (t/n) |
|---|---|---|---|
| Right-angle prism | 90° | Invert (or revert, rotated 90°) | 0.66 |
| Amici (roof) | 90° | Invert **and** revert | 1.13 |
| Frankford Arsenal No. 1 | 115° | Revert only | 1.03 |
| Frankford Arsenal No. 2 | 60° | Invert and revert | 1.50 |
| Penta prism | 90° (fixed, self-compensating) | Neither invert nor revert | 2.25 |
| Schmidt prism | 45° | Invert and revert | 2.25 |
| Frankford Arsenal No. 3 | 90° horiz. + 45° vert. | Invert and revert | 2.25 |
| Frankford Arsenal No. 5 | 90° horiz. + 60° vert. | Invert and revert | 1.81 |
| Frankford Arsenal No. 6 | 90° horiz. + 60° vert. | Invert only | 2.42 |
| Frankford Arsenal No. 4 | 90° horiz. + 45° vert. | Revert only | 2.91 |
| Frankford Arsenal No. 7 | 90° horiz. + 45° vert. | Neither (normal image) | 2.91 |
| Wollaston prism | 90° | Neither (rarely used — awkward shape) | 3.18 |
| Porro prism pair | 0° (direct vision, laterally displaced) | Invert and revert | 3.03 |
| Abbe/Porro modification | 0° (direct vision, displaced) | Invert and revert | 3.03 |
| Abbe prism, type A or B | 0° (direct vision) | Invert and revert | 3.43 |
| Leman prism | 0° (lateral shift = 3A) | Invert and revert | 3.43 |
| Reversion prism | 0° (works in converging/diverging light) | Revert or invert (selectable) | 3.43 |
| Pechan prism | 0° (works in converging/diverging light) | Invert or revert (selectable) | 3.05 |
| Harting-Dove prism | 0° (parallel light only) | Invert or revert (selectable) | 2.45 |
| Double Dove prism | 0° (parallel light only, half the length of a Dove) | Invert or revert (selectable) | 1.11 |

**When to use it:**
- First-pass prism selection before opening a lens-design program's prism library
- Trading off glass volume/weight against required deviation angle and orientation
- Recognizing when a compound (out-of-plane) deviation — e.g., 90° horizontal +
  45° vertical — already has an off-the-shelf one-piece solution (FA prisms 3–7)

**Modern relevance:**
These forms are still the building blocks inside every prism library in CODE V,
Zemax, and OpticStudio. The table collapses a chapter of individual derivations
into one lookup, which is exactly the kind of "computer normally does this" shortcut
useful for a fast first cut or a sanity check on a vendor's proposed prism.

**Accuracy / caveats:**
- t/n values scale with n; a prism cut from a different glass will have a different
  reduced thickness for the same physical size (see the Harting-Dove glass table in
  §13.10.10 for a worked comparison across n = 1.517–1.720).
- "Deviation" here is the nominal design angle from the data sheet; achievable
  angles can be adjusted by changing the prism's internal refracting angles.

---

### 13.5
**Title:** Roof-angle tolerance — beam-splitting roof prisms need 90° ± 3–4 arcseconds

**Source:** ch13, §13.7.4.3

**Category:** `rule-of-thumb`

**The Gem:**
A roof prism (Amici-type) can be used two ways:
1. **Full-aperture roof** (Fig. 13.21 style): the roof edge falls at one side of
   the beam and does not split it. Roof-angle errors merely shift the exit pupil —
   loose tolerances are fine, but the prism must be large enough to clear the whole
   beam without the roof intruding.
2. **Split-aperture roof** (Fig. 13.22 style, the common configuration): the roof
   edge sits in the middle of the beam and actively splits it in half. Any error
   from exactly 90° on the roof angle causes the two half-beams to double the
   image. To keep the doubling below the resolution of the system, **the roof
   angle must be held to 90° ± 3 to 4 arcseconds**.

**When to use it:**
- Specifying roof-prism angle tolerances on a drawing (this is *the* tight
  tolerance that drives roof-prism cost)
- Deciding whether a compact split-roof design is worth its manufacturing cost
  versus a larger full-aperture roof or a Porro pair
- Diagnosing double images/ghosting in binoculars or spotting scopes with roof
  prisms — first suspect is roof-angle error, not stray reflections

**Modern relevance:**
Unchanged today: roof-prism angle is still specified in arcseconds and is the
single largest cost driver (interferometric testing, selective polishing) in
roof-prism binoculars versus Porro-prism binoculars of equal aperture.

---

### 13.6
**Title:** Tunnel diagram — treat any prism as an equivalent block of glass, air-equivalent thickness t/n

**Source:** ch13, §13.8.1–13.8.3

**Category:** `design-heuristic`

**The Gem:**
Any prism, however many internal reflections it has, can be "unfolded" into a
**tunnel diagram**: repeatedly mirror-image the prism's exit faces around each
reflecting surface until the whole light path becomes one straight line. The
folded prism then behaves exactly like a flat block of glass of physical
thickness t (the total glass path length) and index n:

- Ray tracing: refract once at the (unfolded) entrance face, travel in a
  straight line, refract once at the exit face — no need to trace each
  individual internal reflection.
- **Reduced (apparent, air-equivalent) thickness = t/n.** From the outside, the
  prism displaces an image by only t/n, not t — exactly like any thick glass
  plate (§6 thick-lens relation). This is the number to budget when computing
  total optical path length or back-focal clearance in a system that includes
  the prism.
- **Design check:** if the entrance and exit faces of the tunnel diagram come
  out *parallel*, the prism introduces no angular color/dispersion. If they are
  not parallel, the prism acts as a weak wedge/spectroscope element — a red
  flag for an erecting or folding prism that is supposed to be color-neutral.
- **Ghost-reflection check:** rays that graze close to an internal edge in the
  tunnel diagram (e.g., near the hypotenuse corner of a Porro prism) are at risk
  of an extra unwanted internal reflection ("ghost ray") producing a faint
  double image; the fix is a small chamfer/notch cut into the physical prism at
  that corner.

**When to use it:**
- Laying out any new folded-prism design by hand or as a sanity check on
  software output
- Estimating the physical glass path (weight, absorption, back-focal budget) a
  candidate prism will add to a system
- Auditing a prism design for hidden dispersion (non-parallel faces) or ghost
  paths before cutting glass

**Modern relevance:**
Every lens design program treats prisms internally as unfolded glass blocks —
this is the manual version of that process, and it is still the fastest way to
eyeball a prism's optical-path cost or spot a wedge/ghost problem without
running a full ray trace.

---

### 13.7
**Title:** Dove prism needs collimated light — use Pechan or Reversion prism instead in convergent/divergent beams

**Source:** ch13, §13.10.10, §13.10.12, §13.10.13

**Category:** `design-heuristic`

**The Gem:**
The classic **Dove prism** (single reflection off the base, refraction through two
sloped end faces) is the simplest way to rotate an image by rotating the prism
about its own axis — but it **only works correctly in strictly parallel
(collimated) light**. In converging or diverging light the sloped entrance/exit
faces introduce significant aberration, and the handbook states this
restriction explicitly for both the single Dove and the Double Dove (silvered,
half-length) variants.

If the image-rotation function is needed at a location in the system where the
beam is **not** collimated — e.g., to save space by putting it near a focus
instead of in an afocal relay — use one of the modified forms instead:
- **Pechan prism** (two elements split by a ~0.002" air gap, four internal
  reflections) — same rotation function, works in convergent or divergent light.
- **Reversion prism** (modified Abbe type A, two cemented elements, three
  reflections) — also convergent/divergent-light capable, but will displace the
  line of sight by 2× any vertical centering error (it will not deviate it).

**When to use it:**
- Choosing an image-derotator for a system where the Dove prism's parallel-light
  requirement can't be met by the packaging (e.g., a compact periscope or borescope)
- Diagnosing unexpected aberration/image blur that appears only when a Dove
  prism is moved out of the collimated section of a system
- Budgeting alignment tolerance: a Reversion prism's centering error costs you
  2× in line-of-sight displacement, so center it at least as carefully as a
  single mirror

**Modern relevance:**
Image de-rotators (K-mirrors, Pechan prisms) are still selected on exactly this
basis in modern instruments — Pechan/K-mirror assemblies are the standard choice
whenever a rotating image is needed anywhere but a truly collimated space.

---

### 13.8
**Title:** Interpupillary distance range — design binocular/dual-eyepiece spacing for 58–72 mm

**Source:** ch13, §13.10.21

**Category:** `reference-data`

**The Gem:**
For any binocular, dual-eyepiece telescope, or binocular microscope, the
optical centers of the two eyepieces must be adjustable across the human
interpupillary distance (IPD) range:

    D_min = 58 mm = 2.283 in
    D_max = 72 mm = 2.835 in

The handbook's worked binocular-prism hinge mechanism (Carl Zeiss
binocular-ocular system, rotating two rhomboid-prism halves about a central
axis) uses this range directly to size the hinge rotation angle:

$$\cos\theta_M = \frac{D_{min}}{D_{max}} = \frac{2.283}{2.835} = 0.805 \;\Rightarrow\; \theta_M = 36°22'$$

**When to use it:**
- Sizing the mechanical adjustment range of any binocular hinge, prism-shift
  mechanism, or dual-channel eyepiece carriage
- Quick sanity check that a dual-optical-path instrument can actually be used
  by the full range of adult users
- Back-calculating the needed prism/mirror rotation for a given IPD adjustment
  mechanism, using the cosine relation above

**Modern relevance:**
The 58–72 mm range is still the standard design figure for binocular and
dual-eyepiece IPD adjustment (modern ergonomic standards sometimes extend the
low end to ~55 mm for smaller users, but 58–72 mm remains the classic
reference span).

---

### 13.9
**Title:** A prism's aberration contribution doesn't depend on where it sits in the beam

**Source:** ch13, §13.9.1–13.9.2

**Category:** `sanity-check`

**The Gem:**
For a prism (or any parallel-faced glass block) with entrance and exit faces
perpendicular to the optical axis, the third-order aberration contributions
(spherical, coma, astigmatism — Table 13.1: ΣB, ΣF, ΣC) depend **only on the
prism's thickness t and index n and the local ray angles $u_0$, $\bar u_0$ —
not on the prism's axial position** within the converging/diverging beam.
Two consequences:
- **You can freely relocate the prism** along the beam (to fit packaging or
  reduce its clear aperture) without having to recompute its aberration
  contribution, as long as its thickness and orientation are unchanged.
- **If the prism is truly in the collimated section of the system** (parallel
  entrance and exit rays, perpendicular faces), it contributes exactly zero
  aberration — the ordinary justification for folding a telescope or periscope
  with prisms placed between the objective and the first intermediate image.

**Accuracy / caveats:**
- This invariance holds only while the prism's faces stay perpendicular to the
  local optical axis. Tilting the prism (angular misalignment) changes its
  effective thickness and introduces asymmetric aberration — this is *not*
  invariant with position.
- Lateral (off-axis) displacement of the prism can vignette part of the beam
  (equivalent to introducing an off-center stop) even though the on-axis
  aberration formula is unchanged.

**When to use it:**
- Deciding where in a folded system to physically locate a prism for packaging
  reasons, without reopening the aberration budget
- Explaining why moving a fold prism closer to or farther from a lens group,
  by itself, does not change image quality (only tilt/decenter does)

**Modern relevance:**
Lens-design software confirms this automatically, but it is a useful mental
model when laying out mechanical packaging around an existing optical
prescription — the prism is one of the few elements you can slide along the
beam "for free."

---


<!-- ================================================================ -->
<!-- CHAPTER 14 -- EYEPIECES -->
<!-- ================================================================ -->

### 14.1
**Title:** Eye relief minimum — 10–12 mm from last glass surface

**Source:** ch14, §14.1.1, page 14-1

**Category:** `rule-of-thumb`

**The Gem:**
The exit pupil of a visual instrument must be located at least **10–12 mm** from the
last glass surface of the eyepiece. This is the closest a normal eye can comfortably
approach the eyepiece while maintaining a full view of the field.

This is a hard mechanical constraint, not a preference:
- < 10 mm: eye physically cannot reach the exit pupil → vignetting
- 10–12 mm: minimum comfortable range for bare-eye users
- ≥ 20 mm: required for spectacle wearers (glass surfaces sit ~12–15 mm in front of
  the cornea, consuming half the minimum allowance)

**When to use it:**
- Any eyepiece design: check eye relief before declaring a design complete
- Specifying required eye relief for a user population (bare-eye vs. spectacle)
- Evaluating a commercial eyepiece for military/field use (spectacle wearers need ≥20 mm)

**Modern relevance:**
Still the universal constraint. All eyepiece data sheets list eye relief in mm. The
10–12 mm lower bound is unchanged since 1962; the ≥20 mm spectacle requirement is
now codified in many MIL-SPECs.

**Accuracy / caveats:**
- Assumes standard adult eye geometry. Children and some adults can approach closer.
- "Eye relief" as listed by manufacturers is measured to the exit pupil point — the
  actual clearance to the last glass surface is what must meet the 10–12 mm bound.

---

### 14.2
**Title:** Apparent field 30°–60° — the anti-tunnel-vision rule

**Source:** ch14, §14.1.2, page 14-1

**Category:** `rule-of-thumb`

**The Gem:**
An eyepiece should provide a **total apparent field of view of 30° to 60°**. Outside
this range:

- **< 30° apparent field**: observer has the subjective impression of looking down a
  narrow tunnel toward a small distant opening — psychologically uncomfortable and
  makes target acquisition harder
- **30°–60°**: comfortable, immersive viewing
- **> 60°**: can be achieved (ultra-wide designs exist) but requires complex, expensive
  eyepiece designs and often involves significant edge distortion

The apparent field is related to the true field by: `Apparent field ≈ MP × true field`
(magnification × object-space field angle). A narrow true field at high magnification
can still give acceptable apparent field.

**When to use it:**
- Setting eyepiece apparent-field spec for any visual instrument
- Evaluating whether an existing eyepiece family is adequate for the application
- Explaining to a customer why a small-field eyepiece at high magnification feels
  claustrophobic even if the resolution is good

**Modern relevance:**
The 30°–60° comfort zone is unchanged. Modern wide-field eyepieces (80°+) violate
the upper bound but require correspondingly complex designs — this gem gives the
"good-enough" baseline that avoids the complexity.

---

### 14.3
**Title:** Don't design a new eyepiece — modify an existing one

**Source:** ch14, §14.1.2, page 14-1

**Category:** `design-heuristic`

**The Gem:**
> "Very little can be done to improve the existing [eyepiece] designs appreciably,
> nor is this a particularly fruitful area for a designer to spend time on. A more
> practical approach is to use or modify one of the existing designs."

Eyepieces are fully constrained by:
1. Desired apparent field (sets chief ray angle)
2. Eye relief requirement (sets back focal distance)
3. Exit pupil size (sets aperture of chief ray cone)
4. Correction of lateral color, field curvature, distortion

After 60+ years of refinement (to 1962; now 120+), classic eyepiece forms have been
pushed essentially to their design limits. Starting from scratch almost always re-derives
a known form.

**When to use it:**
- Budget/schedule pressure: select the classic form closest to your spec and bend to fit
- Evaluating a request to "design a better Erfle": the correct answer is "modify a known Erfle"
- Allocating design effort: spend it on the objective or relay system, not the eyepiece

**Modern relevance:**
Computer optimization has enabled a few genuinely new wide-field eyepiece forms
(Nagler, Ethos, etc.), but these required exceptional effort and resources. For
defense instrument work the classic forms remain the right starting point.

---

### 14.4
**Title:** Eyepiece type selection guide — comparative properties of classic designs

**Source:** ch14, §§14.3–14.11, pages 14-2 to 14-20

**Category:** `reference-data`

**The Gem:**
Summary of the seven classic eyepiece designs described in ch14, all benchmarked at
f = 2.54 cm, 10× telescope, 5 mm exit pupil:

| Eyepiece | Max ½-field | Eye relief | Lateral color | Petzval (y) | Key feature |
|----------|-------------|------------|---------------|-------------|-------------|
| Huygenian | ±15° | ~3 mm | Corrected (whole) | 0.711 (worst) | Low cost; field stop between lenses |
| Ramsden | ±15° | ~12 mm | Not corrected | 1.07 | Reticle-capable; flat field |
| Kellner | ±20° | ~7 mm | Partially corrected | 1.047 | Most common moderate-wide |
| Orthoscopic | ±25° | ~20 mm | Very well corrected | 1.25 | Long eye relief |
| Plossl (Symmetrical) | ±25° | ~20 mm | Well corrected | 1.307 | Best overall imagery of the simple types |
| Erfle | ±30° | medium | Large (prism compensates) | 1.853 | Standard wide-angle; most common |
| Modified Erfle | ±30° | good | Better than Erfle | 1.78 | Improved Erfle; large distortion OK |
| Berthele | ±25° | — | Poor | 1.920 | Low Petzval at cost of lateral color |
| Wild | ±36° | — | — | 2.560 (best) | Ultra-low Petzval; complex; 7 elements |

Notes on the **y parameter** (Petzval radius / focal length):
- Higher y = smaller field curvature = flatter field
- y < 1: significant field curvature; y > 1.5: acceptably flat for most uses
- The Wild eyepiece achieves y = 2.56 using strongly curved outer surfaces; the element
  nearest the field stop must be **bubble-free glass** (bubbles are sharply in focus there)

**When to use it:**
- First step in any eyepiece selection: match the apparent field requirement to the table
- Tradeoff: long eye relief (Orthoscopic/Plossl) vs. wide field (Erfle/Wild)
- If field curvature is the constraint: choose Berthele, Erfle, or Wild (high y)

---

### 14.5
**Title:** Huygenian eyepiece — do not use with a reticle

**Source:** ch14, §14.3.2, page 14-2

**Category:** `design-heuristic`

**The Gem:**
The Huygenian eyepiece places the **field stop between its two lenses** (the field lens
and the eye lens). The intermediate image — and any reticle in the field stop — is
viewed through the **eye lens alone**.

Consequence: the eye lens is a singlet and introduces lateral color. A reticle or
cross-hair at the field stop will therefore appear **with colored fringes** (not color-free).

**Rule:** Do not use the Huygenian eyepiece when a reticle, graticule, or cross-hair
must be viewed without color. Use the Ramsden or Kellner instead (both place the field
stop outside the optics where all elements are in the viewing path, providing the
same chromatic correction as the on-axis image).

Exception: special applications (§23.3.5.2) where color on the reticle is acceptable
or the instrument is monochromatic.

**When to use it:**
- Instrument spec includes a reticle: eliminate the Huygenian immediately
- Cost-driven selection that lands on Huygenian: flag the reticle incompatibility
- Evaluating a low-cost catalog instrument for ranging/aiming use: check eyepiece type

**Modern relevance:**
This rule appears in modern eyepiece selection guides. The Huygenian's low cost is
attractive; this gem is the reason it is rejected for any precision aiming instrument.

---

### 14.6
**Title:** Prism system compensates eyepiece lateral color — design them together

**Source:** ch14, §14.9.2, page 14-9

**Category:** `design-heuristic`

**The Gem:**
In a telescope or binocular that includes a **prism erecting system**, the prism
glass introduces its own lateral color (the prism is a thick dispersive element
for off-axis chief rays). This lateral color has the **opposite sign** to most
wide-angle eyepiece residuals.

Design consequence: when designing the Erfle or similar wide-angle eyepiece for
use with a prism system, do **not** over-correct the lateral color in the eyepiece
alone. Leave a controlled residual — the prism will compensate it in the complete
system.

Quantitative context: §14.9.2 does not give a specific lateral color value for the
Erfle in isolation — it states only that the color is "fairly large in the version
described" (Figure 14.21 shows the curve growing substantially by 30° half field)
and that the prism system compensates the residual in the complete instrument.

**When to use it:**
- Designing an eyepiece for a prism-erecting telescope (binocular, spotting scope,
  periscope with prism erector)
- Evaluating an eyepiece data sheet: large lateral color in isolation is acceptable
  if the instrument includes dispersive prisms
- Never over-specify eyepiece lateral color for a prism instrument — you'll be
  under-correcting the prism contribution and wasting design freedom

**Modern relevance:**
This compensation principle is used in all modern prism-erecting instruments. Lens
design programs compute the combined residual correctly when the full system is modeled,
but this gem explains why an "uncorrected" eyepiece can be the right choice.

**Accuracy / caveats:**
- Depends on prism glass type, prism path length, and field angle. Must verify for
  the specific prism material; compensation is not exact for all field angles.

---

### 14.7
**Title:** Erfle first-surface proximity trap — closer field stop = dust in focus

**Source:** ch14, §14.9.2, page 14-9

**Category:** `design-heuristic`

**The Gem:**
The Petzval curvature of an Erfle eyepiece can be reduced by moving the focal plane
(field stop) **closer to the first lens surface**. This looks attractive on paper — it
reduces the y parameter and flattens the field.

**The trap:** Any dust, scratches, or bubbles on the first surface will come
**sharply into focus** for the observer. The closer the surface to the focal plane,
the more visible the contamination.

Two additional (sounder) ways to reduce Petzval in the Erfle:
1. **Increase negative element thickness** (element closest to exit pupil) and make
   that surface concave instead of plane — reduces Petzval without moving the focal
   plane, at the cost of some eye relief
2. **Add a field-flattener** element near the focal plane — but then dust on the
   field-flattener is still in focus (same trap, different surface)

**Rule:** Never move a refracting surface close to a focal plane to gain Petzval
correction without also specifying a contamination-protection strategy (sealed
housing, hard coating, frequent cleaning access).

**When to use it:**
- Evaluating an Erfle or similar wide-field eyepiece design that shows suspiciously
  low Petzval: check the first-surface-to-focal-plane distance
- Field-flattener designs: the field-flattener is always near the focal plane —
  specify cleanability in the housing design
- Any design review where a surface is within ~2 mm of a focal plane

**Modern relevance:**
The same trap catches designers using field-flatteners in camera lenses and projection
systems. The rule is identical: proximity to a focal plane = dust visibility.

---

### 14.8
**Title:** Comparing eyepiece designs — normalize to the same focal length and exit pupil first

**Source:** ch14, §14.2.1, page 14-1

**Category:** `design-heuristic`

**The Gem:**
Every eyepiece in this chapter is deliberately benchmarked under identical conditions:
**focal length 2.54 cm, exit pupil diameter 5 mm, used with a 10× (MP = 10) telescope.**
Only with this normalization do the $\Sigma P$ (Petzval sum), $\gamma$, and aberration
curves become directly comparable across designs — a Huygenian and a Wild eyepiece
built at different focal lengths would show different absolute aberration numbers
even if their intrinsic quality (in field-angle and f/# terms) were identical.

**Rule:** Before comparing $\Sigma P$, $\gamma$, eye relief, or aberration-curve
amplitudes between two eyepiece datasheets (vendor catalogs, patents, other design
references), check that they share the same focal length and exit pupil diameter —
or rescale before comparing. $\Sigma P$ and eye relief scale roughly linearly with
focal length; $\gamma$ (a ratio of radius to focal length) is scale-invariant and is
therefore the more robust figure of merit for cross-design comparison.

**When to use it:**
- Comparing eyepieces from different manufacturers or design eras
- Building a lookup table of eyepiece "types" for a design library (use $\gamma$
  and eye-relief-in-focal-lengths as the scale-free columns, not raw eye relief in mm)
- Reproducing or extending Table in GEM-14.4 with additional eyepiece designs

**Modern relevance:**
Lens design software reports Petzval sum and other system quantities in the units of
the current lens (whatever focal length it happens to be scaled to). This gem is the
reminder to normalize before treating catalog numbers as comparable.

---

### 14.9
**Title:** Low-Petzval eyepieces built from strongly curved surfaces need bubble-free glass near the field stop

**Source:** ch14, §14.11.2 (Wild eyepiece), page 14-18

**Category:** `sanity-check`

**The Gem:**
The Wild eyepiece achieves the lowest Petzval curvature in the chapter ($\gamma = 2.56$,
best of the nine designs) by using **strongly curved outer surfaces** on its lens
elements. This has a manufacturing consequence the handbook flags explicitly: the
element **nearest the field stop** must be glass that is **free of bubbles** —
because that element sits so close to the focal plane that any bubble in the glass
is imaged sharply and becomes visible to the observer.

**Rule:** When a design pushes Petzval correction via strongly curved surfaces close
to a focal plane (field lens elements, field-flattener elements), add a bubble/inclusion
inspection requirement to the glass spec for that specific element — not just the
usual cosmetic scratch-dig callout, which may not catch internal bubbles.

**When to use it:**
- Writing the optical spec / bill of materials for any high-$\gamma$, low-field-curvature
  eyepiece or field-lens design
- Reviewing a vendor's glass QC plan for elements adjacent to a real image plane
- Diagnosing a field complaint of "spots in the field of view" that move with the eye —
  check for bubbles in the element nearest the focal plane, not just dust on the surface

**Modern relevance:**
Same physics as the surface-dust trap in GEM-14.7, but for **internal** glass defects
rather than surface contamination. Both stem from the same root cause: any flaw located
near a real focal plane is imaged in sharp focus.

---

### 14.10
**Title:** Orthoscopic eyepiece — check the tangential field curve at full field, it can fly backward

**Source:** ch14, §14.6.2, page 14-8

**Category:** `sanity-check`

**The Gem:**
The orthoscopic eyepiece has excellent lateral color correction and long eye relief,
but the handbook flags one specific weakness: **"the T [tangential] field has a
tendency to fly backward rapidly."** This means the tangential astigmatic field curve
can reverse direction and grow quickly past the nominal design field angle (visible
in Figure 14.12), rather than degrading gracefully like the sagittal curve.

**Rule:** When evaluating or re-optimizing an orthoscopic-type eyepiece (triplet field
lens + singlet eye lens), always check the tangential field curve specifically at and
just beyond the intended maximum field angle — a design that looks acceptable at the
nominal ±25° can already be degrading rapidly in T just past it, unlike designs (Plössl,
Erfle) where S and T degrade together.

**When to use it:**
- Extending an orthoscopic design to a wider field than originally specified
- Field-testing/QC of an orthoscopic eyepiece near the edge of its rated field
- Choosing between orthoscopic and Plössl for a given field spec: Plössl is the safer
  choice if the full rated field must be used hard, per §14.7.2's "overall imagery better"

**Accuracy / caveats:**
- This is specific to the classic orthoscopic (Abbe) form; modified/multi-element
  "orthoscopic-type" eyepieces from other sources may not share this exact behavior.

---


<!-- ================================================================ -->
<!-- CHAPTER 15 -- COMPLETE TELESCOPE -->
<!-- ================================================================ -->

### 15.1
**Title:** Erfle eye relief ≈ 0.8 × focal length — minimum focal length from eye relief spec

**Source:** ch15, §15.3.2.2, page 15-1

**Category:** `shortcut-formula`

**The Gem:**
For an Erfle eyepiece, the eye relief is approximately **0.8 of the focal length**:

    eye_relief ≈ 0.8 × f_eyepiece

Rearranged: **f_min = eye_relief_min / 0.8**

Example from the chapter: minimum eye relief required = 2.0 cm →
minimum focal length = 2.0 / 0.8 = **2.5 cm**. This immediately sets the eyepiece
focal length floor without running a full design.

Combined with the magnification requirement (MP = f_obj / f_eye), this gives
the minimum objective focal length:

    f_obj_min = MP × (eye_relief_min / 0.8)

**When to use it:**
- First step of any telescope design: set f_eye from eye relief, then f_obj from MP
- Checking whether a specified eye relief is achievable with a given Erfle form
- Sizing a telescope layout before any raytracing

**Modern relevance:**
The Erfle family (and Modified Erfle) still obeys this 0.8× rule closely. For
Plossl and Orthoscopic eyepieces the ratio is higher (~0.7–0.75 — slightly shorter
eye relief per focal length); for Huygenian it is very low (~0.5 or less).

**Accuracy / caveats:**
- The 0.8 factor is for a standard Erfle at a 5 mm exit pupil. For larger exit pupils
  (wider objective) the ratio may drop slightly.
- Verify against actual design data; use as a first-estimate only.

---

### 15.2
**Title:** Porro prism reduced path length — L' = 4A/n

**Source:** ch15, §15.4.1, page 15-2

**Category:** `shortcut-formula`

**The Gem:**
A Porro prism system of aperture diameter A and glass index n has an **equivalent
air-space length** (reduced path length) of:

    L' = 4A / n

This is the length of air that the prism replaces in a folded telescope — the number
that appears in the first-order layout as the prism block thickness.

Example from the chapter: A = 2.9 cm, n = 1.5725 → L' = 4 × 2.9 / 1.5725 = **7.38 cm**

The physical prism is 11.6 cm total, but optically it acts like 7.38 cm of air.

**Why 4A/n:** A Porro prism has 4 reflections with path lengths proportional to A;
the glass slows the optical path by a factor of n → reduced length = (physical path) / n
≈ 4A / n.

**When to use it:**
- First-order layout of any Porro prism telescope: add L' = 4A/n as an air block
  between objective and eyepiece
- Sizing the objective-to-eyepiece separation (back focal distance must accommodate L')
- Checking whether a prism system fits within an overall instrument length budget

**Modern relevance:**
All telescope layout tools (CODE V, Zemax) represent glass blocks by their reduced
thickness. This formula gives the right number to enter without computing the full
prism geometry.

**Accuracy / caveats:**
- L' = 4A/n is a Porro-specific approximation. Other prism types (Abbe-Koenig,
  roof Porro, Dove) have different path-length formulas — see ch13 tables.
- The factor 4 assumes a standard two-prism Porro erecting system.
- **Glass selection:** the chapter specifies a glass with high transmission,
  relatively low dispersion, and an index high enough to guarantee total internal
  reflection at all ray angles through the prism. The worked example uses glass
  type 573574 (six-digit code = $n_d$, $V_d$ →  $n_d$ ≈ 1.573, $V_d$ ≈ 57.4),
  consistent with the n = 1.5725, ν = 57.4 prism block in Table 15.1.



---

### 15.3
**Title:** 50% vignetting at field edge is acceptable for prism sizing

**Source:** ch15, §15.4.1, page 15-2

**Category:** `design-heuristic`

**The Gem:**
When sizing Porro prisms (or any erecting prism system) in a telescope, allow
**up to 50% vignetting at the edge of the field** to limit prism size.

This is not a compromise of image quality at the center — vignetting only reduces
illumination toward the field edge. For a visual observation telescope:
- Central image: full aperture, full illumination — unaffected
- Field edge: illumination falls to 50% — still bright enough for most uses
- The prism aperture can be reduced significantly (often 20–30% smaller) vs.
  the zero-vignetting case

**Rule of thumb:** A prism aperture sized to the axial beam diameter (ignoring the
chief ray excursion to the field edge) gives roughly 50% edge vignetting automatically.

**When to use it:**
- Sizing Porro prisms in the preliminary design phase
- Deciding whether to use a larger (heavier/more expensive) prism for zero vignetting
  or a smaller prism with 50% edge vignetting
- Writing the vignetting spec for a military optical instrument

**Modern relevance:**
Military optical standards routinely allow 50% vignetting at the full field. This
gem gives the physical justification and connects it to prism sizing.

**Accuracy / caveats:**
- 50% vignetting is in illumination (area), not diameter. In intensity it appears
  as a gradual darkening toward the edge — usually unnoticed in high-luminance scenes.
- For photography or radiometric applications requiring uniform illumination, vignetting
  limits are much tighter and this allowance does not apply.

---

### 15.4
**Title:** Telescope design sequence — correct eyepiece first, then objective

**Source:** ch15, §§15.4.3–15.4.4 and §15.5.1, pages 15-3 to 15-4

**Category:** `design-heuristic`

**The Gem:**
The correct two-pass sequence for designing a complete telescope system:

**Pass 1 — Eyepiece (parallel rays in from eye side):**
1. Correct **astigmatism** and **lateral color** in the eyepiece to spec
2. Accept residual spherical and coma in the eyepiece (controlled in the objective)
3. Note: distortion in the eyepiece is tied to astigmatism — once astigmatism is
   set, distortion is determined. Do not attempt to correct distortion independently.

**Pass 2 — Objective (parallel rays in from object side):**
4. With eyepiece aberrations fixed, readjust the objective to correct **axial color**,
   **spherical aberration**, and **coma** for the complete telescope
5. The objective is the right place to correct these because it has fewer constraints
   and more bending freedom than the eyepiece

**Integration check:**
- Design each unit separately with parallel rays into the focal plane
- Match transverse ray errors at the intermediate focal plane
- Insert a **dummy surface at the intermediate focal plane** when tracing the full system
  — this lets you read intermediate image errors without stopping the trace

**When to use it:**
- Starting a telescope design: don't optimize objective and eyepiece simultaneously
- Debugging a telescope performance issue: attribute astigmatism/lateral color to
  eyepiece; attribute spherical/axial color to objective
- Allocating design effort: eyepiece controls field correction; objective controls axial

**Modern relevance:**
This is still the standard "split design" workflow used in modern telescope design.
The dummy surface trick is a Zemax/CODE V standard technique.

---

### 15.5
**Title:** Wide-angle exit pupil rule — large exit pupil prevents iris rollout

**Source:** ch15, §15.5, page 15-3

**Category:** `design-heuristic`

**The Gem:**
The eye's iris (pupil) is **not located at the center of rotation of the eye**. When
the eye rotates to view objects near the edge of the field, the iris moves laterally
— it can roll out of alignment with the instrument's exit pupil, cutting off the beam
entirely.

Consequence: in a wide-angle telescope (apparent field > ~40°), if the exit pupil is
small, the observer loses the image completely when looking toward the field edge —
and in a binocular, cannot move the eye to compensate because both eyes are constrained.

**Design rule:** For wide-angle telescopes, **maintain the largest exit pupil
compatible with the objective size**. A larger exit pupil provides lateral tolerance
for iris displacement during eye rotation.

Quantitative context: the center of rotation of the eye is approximately 13–14 mm
behind the cornea; the iris sits close to the cornea (~3 mm behind it), so it is
roughly 10–11 mm **in front of** the center of rotation. At 30° eye rotation, the
iris shifts ~5–6 mm laterally relative to the optical axis — comparable to the
exit pupil diameter in typical designs.

**When to use it:**
- Wide-angle telescope and binocular designs with apparent field > 30°
- Specifying exit pupil diameter for weapons sights (eye must move behind the eyepiece)
- Evaluating binocular designs where both exit pupils must simultaneously capture both
  eyes even when the observer looks obliquely

**Modern relevance:**
This iris-offset effect is why modern wide-field military binoculars specify
exit pupils of 5–7 mm even at daylight conditions where a 2 mm pupil would suffice
photometrically.

---

### 15.6
**Title:** Edge-of-field philosophy — wide-but-blurry beats narrow-but-sharp

**Source:** ch15, §15.5, page 15-3

**Category:** `design-heuristic`

**The Gem:**
A telescope is used for **acute vision primarily within ±12° apparent field** of center.
The field edge serves a different purpose: detecting motion and cueing the eye to
re-center on a target of interest.

This leads to a fundamental design philosophy:

> **"A telescope should always be designed for as wide a field as possible, even if
> astigmatism and distortion may become large. The limit should be set by the size of
> the instrument and the cost, rather than by the image quality."**

Practical implications:
- A T-S astigmatic split of 3.7 diopters at 30° half-field (the example in the chapter)
  is acceptable — standard, even, for a well-corrected telescope
- Focusing in 0.8 diopters from the paraxial focus gives essentially astigmatism-free
  imagery within ±20° apparent field — the full zone used for critical observation
- The outer field (20°–30°) is blurred but still useful for motion detection
- This is far better than restricting the field stop to get sharp edges

**When to use it:**
- Setting eyepiece field stop diameter: err on the large side
- Responding to a customer who wants sharp edge-of-field: explain the observational
  physiology (acute vision zone vs. motion zone)
- Evaluating a telescope against a competitor's: check useful-field criterion (±12°
  sharp), not just raw field of view

**Modern relevance:**
The ±12° acute-vision zone is consistent with modern vision science. This philosophy
underpins the design of all modern wide-field military and sporting optics.

---


<!-- ================================================================ -->
<!-- CHAPTER 16 -- APPLICATIONS OF PHYSICAL OPTICS -->
<!-- ================================================================ -->

### 16.1
**Title:** λ/2 per fringe — the fundamental rule of interferometric surface testing

**Source:** ch16, §16.2.1.4 and §16.12.1.4, pages 16-4 and 16-19

**Category:** `rule-of-thumb`

**The Gem:**
In any Fizeau-type interferometer (two surfaces in near-contact in air), each
interference fringe is the locus of points where the **air gap d is constant**.
Moving from one bright fringe to the next corresponds to a gap change of exactly
**λ/2**:

    Δd per fringe = λ/2

This is exact for normal incidence (cos i' = 1) in air (n = 1).

Practical consequences:
- Count fringes across a surface → immediately know peak-to-valley error in λ/2 units
- 1 fringe of error = λ/2 ≈ 275 nm (visible, green light)
- To measure surface to λ/10: detect fringe positions to λ/20 ≈ 14 nm (achievable visually)
- A perfectly flat surface gives straight, evenly spaced fringes; any curvature or
  irregularity bends the fringes

**Extension — Newton's rings:** when testing a curved surface against a flat,
fringes form concentric rings. Dark ring radii: **r_v = √(vλR)** where v = 0,1,2,…
and R is the surface radius. Measure ring radii → compute R directly.

**When to use it:**
- Interpreting any optical flatness test (shop test of flats, prisms, windows)
- Quick estimate of surface error from a fringe photograph: count fringe deviations
- Setting up a Fizeau test: fringe density = 1 fringe / (λ/2 × wedge_angle_radian)

**Modern relevance:**
Unchanged. Every interferogram in Zemax, ZYGO, or 4D Technology is calibrated on
this λ/2 rule. The shop-floor version (bare-eye Fizeau test) uses this directly.

---

### 16.2
**Title:** OPD formula for a dielectric plate — δ = 2n·d·cos(i')

**Source:** ch16, §16.9.1, pages 16-14 to 16-15 (Equations 49–50)

**Category:** `shortcut-formula`

**The Gem:**
The optical path difference (OPD) between the ray reflected from the front surface
and the ray reflected from the back surface of a dielectric plate of index n,
thickness d, at angle of refraction i' is:

    δ = 2 · n · d · cos(i')

For a plate immersed in a single medium (same material on both sides), the total
phase difference includes a π phase flip from one of the two reflections:

    Δ(phase) = (4π/λ) · n · d · cos(i') + π

which gives destructive interference (dark fringe) at normal incidence when:

    2nd = vλ,  v = 0, 1, 2, ...

and constructive when:

    2nd = (v + ½)λ

**When to use it:**
- Thin-film coating design: set d = λ/(4n) for quarter-wave layer (antireflection or HR)
- Predicting whether a plate will transmit or reflect at a given wavelength
- Understanding Fabry-Perot etalon resonance conditions
- Interpreting Fizeau and Newton fringe patterns in glass plates

**Modern relevance:**
This is the foundational formula for all thin-film optics. Quarter-wave layers
(d = λ/4n), half-wave layers, and multi-layer stacks all follow from it.

**Accuracy / caveats:**
- Assumes normal to small-angle incidence; for large i' use cos(i') explicitly
- Phase change accounting: need to track which reflections carry the π flip (see 16.3)

---

### 16.3
**Title:** Phase change on reflection rule — π at denser medium, 0 at rarer

**Source:** ch16, §16.8.1.2, page 16-13 (Equation 45)

**Category:** `rule-of-thumb`

**The Gem:**
When light reflects at an interface between two non-absorbing media:

- **Reflection from a denser medium** (going from low n to high n): phase change = **π** (half wavelength)
- **Reflection from a rarer medium** (going from high n to low n): phase change = **0**
- **Transmission through any interface**: phase change = **0** (always)

Practical consequences for thin films:
- Air-glass interface (from air): π flip → glass surface reflects with phase inversion
- Glass-air interface (from glass): 0 → back surface reflects without inversion
- Net: for an uncoated glass plate, the two reflected beams differ in phase by π → dark
  fringe at zero thickness (central Newton ring is dark)
- For a soap film or oil slick: same rule — dark center for glass/film/glass stack

**When to use it:**
- Predicting whether the central fringe in any thin-film test is bright or dark
- Designing antireflection coatings: a single quarter-wave layer of intermediate n
  puts both reflected beams in phase opposition → cancellation
- Explaining color of oil slicks, soap bubbles, and AR coatings to clients

**Modern relevance:**
Identical in modern thin-film software. Getting the sign wrong (forgetting the π flip)
is one of the most common errors in hand calculations of thin-film performance.

---

### 16.4
**Title:** Haidinger fringe blink counting — measuring plate non-parallelism by eye

**Source:** ch16, §16.11.1.4, page 16-17

**Category:** `graphical-method`

**The Gem:**
A simple technique for measuring the **departure from parallelism** of a glass plate,
using only an extended monochromatic source and the unaided eye:

1. View the plate against a monochromatic extended source (sodium lamp, filtered LED),
   with the eye focused approximately at the plate (~3 feet distance)
2. Observe circular Haidinger fringes centered on the observer's line of sight
3. Slide the plate across the field of view in a straight line (perpendicular to the line of sight)
4. Count the number of times the **central fringe blinks** (goes dark-bright-dark) as the
   plate traverses the field

Each complete blink cycle = the optical path through the plate has changed by **λ/2**.

Thickness variation Δd over the traverse:

    Δd = N · λ / (2n)

where N = number of blink cycles, λ = wavelength, n = plate index.

**When to use it:**
- Quick shop inspection of parallel plate quality (windows, beam splitters, filters)
- Checking wedge in optical flat blanks without a formal interferometer
- Any situation requiring a fast go/no-go parallelism test with minimal equipment

**Modern relevance:**
This test requires only a sodium lamp and bare eyes — no interferometer, no mounting.
Still used in optics shops as a first-pass filter before committing to formal testing.

**Accuracy / caveats:**
- Counts must be made with the plate moving steadily and uniformly
- Angular resolving power of the eye (~1 arcmin) limits the minimum detectable fringe
  to plates thinner than ~1.8 mm in green light (see §16.11.1.3 example)
- For thicker plates, fringes are too fine to resolve with the unaided eye — use a
  Fizeau interferometer instead

---

### 16.5
**Title:** Fringe shift = film thickness — t = (Δx/h) · (λ/2)

**Source:** ch16, §16.18.1.2, pages 16-39 to 16-40 (Equations 129–130)

**Category:** `shortcut-formula`

**The Gem:**
To measure the **thickness t of a thin film** deposited on a surface using multiple-beam
or two-beam interference fringes:

1. Orient fringes perpendicular to the film edge
2. Measure the fringe width h (distance from one fringe to the next, in same units)
3. Measure the fringe shift Δx at the film edge (how much one fringe is displaced)
4. The film thickness is:

        t = (Δx / h) · (λ/2)

   or equivalently:  t = (Δx / h) · (λ / 2n) for a film of index n (when measuring in
   reflected light and the space between interferometer surfaces is the film material)

**When to use it:**
- Measuring step heights of evaporated films, polished layers, or surface machining
- Calibrating coating deposition rates
- Quick thickness measurement without a profilometer or ellipsometer

**Limitations of method:**
- Fringe shift Δx must be < h (i.e., film thickness < λ/2); for thicker films use the
  channeled-spectrum method (§16.19) which avoids order ambiguity
- Surface roughness limits accuracy: polished glass surfaces have 10–60 Å peak-to-valley
  roughness that wiggles the fringes

**Modern relevance:**
This fringe-shift method is still used for step-height measurement in thin-film labs
when a stylus profilometer is not available. The formula is unchanged. Accuracy of
~10 Å is achievable with a micrometer eyepiece.

---

### 16.6
**Title:** Rayleigh resolution limit — 0.61λ/NA — and the Sparrow physical limit

**Source:** ch16, §16.27, pages 16-57 to 16-58 (Equations 200, 203)

**Category:** `shortcut-formula`

**The Gem:**
The **Rayleigh criterion** for the minimum resolvable separation of two self-luminous
point sources through a circular aperture:

Linear resolution in object space:

    r₀ = 0.61λ / NA

Angular resolution (small angles, telescope):

    θ₀ = 1.22λ / D

where:
- NA = numerical aperture of the objective (= n·sin U_max)
- D = aperture diameter
- λ = wavelength

**The Sparrow (physical) limit** is more conservative: two points are just unresolvable
when the combined intensity distribution shows no dip between them. For Airy-type
objectives this occurs at **0.78 Airy units** (vs. 1.00 for Rayleigh). In practice,
resolutions of ~0.81 Airy units have been achieved with highly corrected objectives.

Summary:
- Rayleigh criterion: r₀ = 0.61λ/NA (conservative; 26% dip between peaks)
- Sparrow limit: r₀ = 0.47λ/NA (physical minimum; no dip — contrast = 0)
- Practical limit with excellent objectives: ~0.50λ/NA

**When to use it:**
- Setting optical system aperture for a required resolution
- Comparing sensor pixel size to diffraction limit (Nyquist must be ≤ r₀/2)
- Explaining why bigger apertures are needed for finer resolution

**Modern relevance:**
This is the most-cited formula in imaging system design. The Sparrow limit (often
forgotten) sets the true information-theoretic bound. Both are still correct.

**Validation note (2026-09-12):** the Rayleigh/Dawes-type terms are confirmed; the exact
Sparrow-limit coefficient (0.78 Airy units / 0.47λ/NA) is plausible but not independently
verified to high precision — treat as approximate pending a primary-source check.

---

### 16.7
**Title:** Depth of focus from diffraction theory — ∝ λ/NA² (not λ/NA)

**Source:** ch16, §16.28, pages 16-59 to 16-60 (Equations 213–215)

**Category:** `shortcut-formula`

**The Gem:**
The **diffraction-limited depth of focus** (maximum out-of-focus displacement before the
on-axis energy density drops to 81% of peak) is:

    |z| ≤ λ / (2 · NA²)

where NA is the image-space numerical aperture (NA = n·p_m).

This is the Rayleigh depth-of-focus criterion derived from wave optics.

Key insight: **depth of focus scales as NA⁻², not NA⁻¹**. This is fundamentally different
from the geometric-optics result which gives depth ∝ NA⁻¹. At high NA, diffraction
limits depth far more severely than geometry predicts.

Example: objective with NA = 0.1, λ = 0.55 µm:
    z_max = 0.55 / (2 × 0.01) = **27.5 µm**

Same system, NA = 0.3:
    z_max = 0.55 / (2 × 0.09) = **3.1 µm** — 9× shallower, not 3×.

**When to use it:**
- Setting focus tolerance for a camera, microscope, or sensor system
- Comparing diffraction depth of focus to mechanical focus stability budget
- Explaining why high-NA objectives require much tighter focus control than NA predicts
  naively

**Modern relevance:**
This NA² scaling is standard in microscopy (where it is known as the "Rayleigh range
for depth of field") and in lithography (where depth of focus = k₂λ/NA²). Getting
the NA exponent wrong leads to order-of-magnitude errors in focus tolerance budgets.

---


<!-- ================================================================ -->
<!-- CHAPTER 17 -- OPTICAL MATERIALS -->
<!-- ================================================================ -->

### 17.1
**Title:** Normal-incidence reflection loss from refractive index alone

**Source:** ch17, §17.2.2, page 17-1

**Category:** `shortcut-formula`

**The Gem:**
For light hitting a glass surface at normal incidence (or close to it), the fraction
reflected at a single air-glass interface is:

    R = ((n - 1) / (n + 1))²

where n is the refractive index of the glass. No angles needed.

**When to use it:**
- Quick estimate of reflection loss from any uncoated surface
- Estimating how much AR coating benefit you get (R_coated vs R_bare)
- Checking whether reflection loss matters for a given glass type
- Works for any single interface between air (or vacuum, n=1) and a medium of index n

**Modern relevance:**
Still the fastest way to sanity-check coating specifications or estimate stray-light
budget contributions from uncoated surfaces. Useful in the field or when a full Fresnel
calculation is overkill for a rough estimate.

**Accuracy / caveats:**
- Valid only at normal (or near-normal) incidence. At oblique angles use full Fresnel equations.
- For a complete lens element (two surfaces, multiple reflections), total internal transmittance
  is approximately T ≈ (1-R)² for thin elements (ignoring multiple reflections).
- For a more precise multi-pass calculation see §17.2.3.4, eq. (7)-(9).

**Worked example (from text):**
Dense flint glass, n = 1.720 → R = ((1.720-1)/(1.720+1))² = (0.720/2.720)² = 7.0%
Same glass at 2.5 microns, n = 1.673 → R = 6.3%

---

### 17.2
**Title:** Thick-sample absorption: separating reflection loss from bulk absorption

**Source:** ch17, §17.2.3.3–17.2.3.5, pages 17-2 to 17-3

**Category:** `shortcut-formula`

**The Gem:**
When a spectrophotometer gives you the total transmittance T_oo of a glass sample,
and you know the surface reflectivity R, the internal (bulk) transmittance T is:

    T_oo ≈ T(1-R)²          [simplified, ignoring multiple reflections]

Rearranged to find T from a measurement:

    T ≈ T_oo / (1-R)²

Then the absorption coefficient (base-10) β is:

    β = -log₁₀(T) / thickness

And you can predict any other thickness t:

    transmittance(t) = 10^(-β·t)   [internal, no surface losses]

**When to use it:**
- You have a spectrophotometer curve for one thickness and need to predict another
- Comparing glasses for a thicker element than the catalog sample
- Deciding whether low-reflection coatings will help more than switching glass types

**Modern relevance:**
Glass catalog data is still given at standard sample thicknesses. This chain of
calculations lets you predict performance at your actual element thickness without
a new measurement — saves a fabrication test run.

**Accuracy / caveats:**
- The simplified form ignores light re-reflected at the second surface back through
  the medium. Use the exact form (eq. 7–9 in source) if R is large (>5%) or precision matters.
- β varies with wavelength; run this at each wavelength of interest.

**Worked example (from text):**
Ordinary plate glass, 6.18 mm thick, T_oo = 88.3% at 600 nm, n ≈ 1.52 → R = 4.3%
→ T = 0.964 → β = 0.00257/mm
→ At 25.4 mm with 1% AR coatings: 84% total transmission.
Waterwhite plate, **6.61 mm thick** (a different sample thickness than the ordinary plate —
do not reuse 6.18 mm here; the problem statement rounds this to "6.6mm"): T_oo = 91.4%, same
R = 4.3% → computed T ≈ 0.998. This is so close to unity that the source deliberately does
not trust it to that precision; it instead assumes the conservative bound **T ≥ 0.995** and
computes β from that: β = -log₁₀(0.995)/6.61mm ≈ 0.00033/mm.
→ At 25.4 mm: ≥96% total transmission (matches source, §17.2.3.5).
*Takeaway: waterwhite gains ~12 percentage points over ordinary plate at 25 mm thickness.*
*(Validation note 2026-09-12: an earlier version of this entry incorrectly reused the 6.18 mm
ordinary-plate thickness for the waterwhite sample and used the literal computed T=0.998
instead of the source's conservative T=0.995; the β figure of 0.00033/mm itself was already
correct, but the shown derivation didn't reproduce it. Corrected and re-confirmed to the
precise 6.61mm figure against the scan during the LaTeX transcription pass, ocr_output/ch17.md
§17.2.3.5.)*

---

### 17.3
**Title:** Metal mirror selection rules by wavelength region

**Source:** ch17, §17.7.3, page 17-8 to 17-9

**Category:** `design-heuristic`

**The Gem:**
For choosing a bare metal reflective coating:

| Wavelength region | Best choice | Rule |
|-------------------|-------------|------|
| Ultraviolet (<0.35 µm) | **Aluminum** | Only metal with high UV reflectance; all others drop sharply |
| Visible (0.4–0.7 µm) | Al or Ag | Al: ~88-92%; Ag: ~95-99% but tarnishes |
| Near IR (1–2 µm) | Ag, Au, Cu, or Al | All four >95%; Al is 2-3% lower |
| Far IR (>3 µm, especially 10 µm) | Any of the four | All reach 98-99%; even Rh hits ~96% |

General rule: **aluminum for broadband / UV-critical use; silver for visible/near-IR
reflectance-critical use (protected environment); gold for mid-IR.**

**When to use it:**
- First-pass mirror coating selection
- Deciding whether a gold coating adds real value over aluminum for an IR system
- Checking whether UV reflectance is the binding constraint

**Modern relevance:**
The basic physics hasn't changed. Still the correct first-order guide for selecting
evaporated metal coatings before diving into multilayer designs.

**Accuracy / caveats:**
- Values are for freshly deposited films; aged/oxidized surfaces differ.
- Aluminum tarnishes slowly in normal air (forms thin Al₂O₃ which is mostly benign).
- Silver tarnishes rapidly unless protected — not suitable for exposed first-surface mirrors.
- For precision values see Figure 17.2. [NEEDS FIGURE — reflectance curves Ag/Al/Au/Cu/Rh vs 0.22-10µm]

---

### 17.4
**Title:** When to ignore wavelength variation of reflection coefficient

**Source:** ch17, §17.2.2, page 17-1

**Category:** `design-heuristic`

**The Gem:**
The reflection coefficient R = [(n-1)/(n+1)]² varies with wavelength because n varies.
However, for most optical glasses in the visible region, the change in R across the
waveband is small enough to use a single midband value.

Rule: **use a single R value when the index change across your waveband is small relative
to (n-1)**. For most crown glasses (n ≈ 1.52, dn ≈ 0.01 across visible), this is ~1%
relative variation in R — negligible for most budgets.

**When to use it:**
- Deciding how much effort to put into wavelength-dependent reflection modeling
- Setting up a stray-light budget with a single reflection factor per surface

**Accuracy / caveats:**
- Breaks down for high-dispersion glass (dense flint) over wide wavelength ranges,
  as shown in the worked example: 7.0% at D-line vs 6.3% at 2.5 µm.
- Always reconsider for broadband IR systems where index variation is large.

---

### 17.5
**Title:** Thermal expansion matching rule for cemented/mounted optics

**Source:** ch17, §17.5.1 item (3), page 17-5

**Category:** `design-heuristic`

**The Gem:**
When mounting or cementing an optical element, the coefficient of thermal expansion
(CTE) of the optical material should be matched to the CTE of the cell or cement.

Practical rule: **mismatch in CTE between element and mount/cement causes stress that
either fractures the element (large mismatch, rapid thermal shock) or degrades figure
(moderate mismatch, slow temperature change)**. For precision instruments over a wide
temperature range, match CTEs to within a factor of ~2.

**When to use it:**
- Selecting glass type when the mount material is constrained
- Evaluating risk when using a "better" optical glass that has a very different CTE
- Airborne / military instruments subject to wide temperature swings

**Modern relevance:**
Still the first-order rule for optomechanical design. CTE matching remains the dominant
driver in athermalization of precision systems.

---

### 17.6
**Title:** Hardness vs environment tradeoff for optical material selection

**Source:** ch17, §17.5.1 items (5)-(6), page 17-5

**Category:** `design-heuristic`

**The Gem:**
Two competing surface quality concerns for optical material selection:

- **Soft materials** (e.g. some IR crystals, plastics): prone to scratches and sleeks
  during polishing; avoid in exposed locations subject to abrasion (domes, windows).
- **Hard materials** (e.g. fused quartz): difficult and slow to grind and polish;
  cost and schedule impact.

Quick selection filter: **if the element will be exposed to airborne abrasion or frequent
handling, eliminate any material with Knoop hardness < ~400 unless no alternative exists.**

**When to use it:**
- Dome/window material selection for airborne systems
- Deciding whether to specify a hard protective coating (e.g. DLC) on a soft substrate
- Evaluating risk of soft IR materials (e.g. ZnSe, chalcogenides) in field equipment

---

### 17.7
**Title:** Plastics vs glass: when the weight saving is real

**Source:** ch17, §17.6.2.3, pages 17-7

**Category:** `design-heuristic`

**The Gem:**
Optical plastics (acrylics, styrenes) have specific gravity 1.05–1.19, vs 2.48 for
crown glass and 3.41 for dense flint. Weight savings of 50-75% per element are possible.

But the weight saving is only real if:
1. You can tolerate the index shift with temperature and humidity (plastics are very sensitive)
2. The element doesn't need tight figure stability over temperature
3. Scratch resistance is acceptable for the application

Rule: **plastics are viable for simple, non-critical elements (viewfinders, box camera
lenses, singlet meniscus objectives) but not for precision or environmental-exposure systems.**

**Modern relevance:**
Injection-molded plastic optics are now used widely in consumer electronics. This entry
gives the 1962 baseline — the tradeoffs are identical today (index/humidity sensitivity,
scratch resistance). The rule holds.

---

### 17.8
**Title:** UV material quick-reference table

**Source:** ch17, Table 17.1, page 17-8

**Category:** `reference-data`

**The Gem:**
Materials suitable for the UV region (shorter than 0.36 µm), with key properties:

| Material | n_D | v-value | UV cutoff | Max piece size | Notes |
|----------|-----|---------|-----------|---------------|-------|
| Sodium Chloride (NaCl) | 1.544 | 42.8 | 0.25 µm | 7.5 in | Highly water-soluble |
| Potassium Bromide (KBr) | 1.560 | 33.4 | 0.21 µm | 7.5 in | Highly water-soluble |
| Potassium Iodide (KI) | 1.667 | 23.2 | 0.25 µm | 7.5 in | Highly water-soluble |
| Lithium Fluoride (LiF) | 1.392 | 99.3 | 0.11 µm | 6.0 in | |
| Calcium Fluoride (CaF₂) | 1.434 | 95.1 | 0.125 µm | 6.0 in | |
| Fused Quartz (SiO₂) | 1.458 | 87.8 | 0.22 µm | Several in | |
| Barium Fluoride (BaF₂) | 1.474 | 81.8 | 0.145 µm | — | |

**When to use it:**
First-pass UV material screening. CaF₂ and fused quartz are the workhorse choices;
LiF reaches deepest UV but is fragile. Halide salts (NaCl, KBr, KI) are usable only
in sealed, dry environments.

**Modern relevance:**
This table is still essentially correct for deep UV optics. The same materials are
used in DUV lithography (CaF₂ at 193 nm), UV spectroscopy, and laser optics.

---


<!-- ================================================================ -->
<!-- CHAPTER 18 -- ATMOSPHERIC OPTICS -->
<!-- ================================================================ -->

### 18.1
**Title:** Filter decision rules for visual instruments vs. sky background

**Source:** ch18, §18.3.2, pages 18-4 to 18-5

**Category:** `design-heuristic`

**The Gem:**
Three-case filter selection rule for visual optical instruments used against sky backgrounds:

| Target | Sky background | Best filter choice |
|--------|---------------|-------------------|
| White, bright | Clear blue sky | Red or yellow (darkens sky relative to target) |
| Dark | Clear blue sky | None ("clear" — no filter improves this) |
| Any | White/overcast sky | None (color filters give no improvement) |
| Colored | Any | Filter that darkens target MORE than background |

Key insight: **dark objects against blue sky cannot be improved by any color filter**. The
"blue myopia" of the eye is not reliably compensated by filters in practice. Accept the
clear condition.

**When to use it:**
- Specifying or evaluating filter kit for binoculars, riflescopes, spotting scopes
- Any visual instrument used for target acquisition against sky

**Modern relevance:**
These rules remain correct. The temptation to always specify a haze filter is wrong: for
dark targets against blue sky it does nothing, and for white-sky backgrounds filters are
useless. Simple three-row decision table saves testing time.

---

### 18.2
**Title:** Fog, cloud, and rain extinction is filter-independent (10–40 µm rule)

**Source:** ch18, §18.2.2.12, pages 18-3 to 18-4

**Category:** `rule-of-thumb`

**The Gem:**
When scattering particles are **10–40 µm or larger** (fog droplets, cloud, rain), extinction
is essentially **constant across the entire 0.4–5.5 µm range (±10%)**. No color filter
provides meaningful penetration improvement.

Contrast with small-particle haze (<1 µm): Rayleigh scattering follows lambda^-4, so red
light is scattered ~10x less than violet — filters DO work.

Decision rule:
- Particle size << lambda (haze, dust < 1 µm) -> minus-blue or red filter helps significantly
- Particle size >> lambda (fog, cloud, rain >= 10 µm) -> no filter provides penetration benefit

**When to use it:**
- Before specifying haze/penetration filters — check whether the dominant obscurant is
  large-particle (fog, rain) or small-particle (haze, smoke)
- Evaluating claims about "fog-penetrating" visible-spectrum filters

**Modern relevance:**
Counterintuitive and frequently mis-specified. Modern IR systems bypass this limit by
moving to wavelengths where the atmosphere has absorption windows; but in the visible,
the physics is the same as in 1962.

**Accuracy / caveats:**
- Applies to visible + near-IR (0.4–5.5 µm range confirmed by measurement)
- Heavy smoke can have mixed particle sizes — behavior intermediate

---

### 18.3
**Title:** Wratten filter numbers for aerial photography "looking up"

**Source:** ch18, §18.4.2.3, pages 18-5 to 18-6

**Category:** `reference-data`

**The Gem:**
Specific Kodak Wratten filter recommendations for cameras tracking missiles/satellites
(sky background):

| Target type | Sky | Recommended filter | Avoid |
|-------------|-----|--------------------|-------|
| White/spectrally flat | Blue clear sky | Wratten 25 or 29 (red) | Blue filter (reduces contrast) |
| Dark | Blue clear sky | Wratten 47 (blue) | Red filter |
| White, gray, or dark | White/overcast | No filter helpful | Any color filter |
| Colored | Any | Filter that darkens target more than sky | — |

Note: photographic materials do not suffer from "blue myopia" — the blue channel gives as
good or better tone scale than red, so Wratten 47 is a valid choice for dark targets
(unlike visual instruments where the eye itself limits blue performance).

**When to use it:**
- Specifying filters for missile tracking cameras, satellite surveillance cameras
- Any upward-looking photographic instrument

**Modern relevance:**
Specific filter numbers remain available. The decision logic is directly applicable to
monochrome CMOS sensors with external filter wheels.

---

### 18.4
**Title:** Yellow/orange filter: standard compromise for aerial haze (looking down)

**Source:** ch18, §18.4.3.2, page 18-6

**Category:** `design-heuristic`

**The Gem:**
For downward-looking aerial cameras in haze conditions:
- **Red filter** -> best haze elimination (Rayleigh lambda^-4 gives most contrast gain)
- **Red filter drawback** -> natural vegetation (green foliage) appears too dark,
  impeding photo interpretation
- **Standard compromise** -> **yellow or orange filter** balances haze rejection against
  acceptable greenery rendering

Ground scene contrast ratios are very low (~log 0.1), so even modest haze elimination
is significant.

**When to use it:**
- Aerial survey cameras, reconnaissance cameras where scene includes vegetation
- Any camera "looking down" in haze requiring photo interpretation of terrain/vegetation

**Modern relevance:**
Direct filter guidance applicable to modern aerial and UAV camera systems. The
vegetation-darkening problem with red filters is still real (near-IR channels avoid it,
but visible-band imagery must use this compromise).

---

### 18.5
**Title:** 2-inch / 10x aperture-and-power immunity rule for atmospheric turbulence

**Source:** ch18, §18.3.1.2, page 18-4

**Category:** `rule-of-thumb`

**The Gem:**
Visual optical instruments with:
- Aperture <= **2 inches** (50 mm), AND
- Magnification <= **10x**, AND
- Used at elevation angles > **15 degrees**

are **not greatly affected** by differences in air density, inhomogeneity, or turbulence.

Instruments larger than this are affected roughly **proportionally to their aperture**.

**When to use it:**
- Deciding whether atmospheric "seeing" needs to be a design constraint
- Hand binoculars (7x50, 10x50) at field elevation angles -> generally immune
- Setting expectations for a spotting scope vs. a large observation telescope

**Modern relevance:**
Immediate sanity check for field instrument specifications. A 50 mm binocular at 10x
on a 20-degree target elevation is not seeing-limited; a 150 mm spotting scope at 60x is.

---

### 18.6
**Title:** Smaller aperture can outresolve larger aperture in poor atmospheric seeing

**Source:** ch18, §18.5.2.5 and §18.5.3.2, pages 18-7 to 18-8

**Category:** `design-heuristic`

**The Gem:**
In poor atmospheric seeing, **theoretical resolution is almost never achieved** with large
apertures, and smaller instruments frequently deliver better actual resolution:

- Hale 200-inch telescope: theoretical 0.04" arc, actual seeing disk **~2.5" arc** (60x worse)
- 36-inch telescope: theoretical <0.15" arc, actual **2.0–5.0" arc** seeing disk

Reason: the larger the aperture, the lower the probability that the air column over the
full aperture is homogeneous within a quarter-wavelength path difference at any moment.

Practical implication: **stopping down a large telescope to a sub-aperture diameter can
improve actual image quality** in poor seeing, because the probability of local homogeneity
is higher over a smaller patch of sky.

**When to use it:**
- Planning observation campaigns with large aperture instruments
- Choosing aperture for field use where atmospheric conditions are uncontrolled
- Explaining why a small amateur telescope sometimes shows better planetary detail than
  a large one

**Modern relevance:**
Adaptive optics (AO) systems were developed specifically to overcome this limit. But
without AO, the 1962 rule still applies: do not over-specify aperture for ground-based
systems unless seeing compensation is part of the system design.

---

### 18.7
**Title:** Use neutral density filters, not aperture stops, for brightness reduction

**Source:** ch18, §18.3.3.1, page 18-5

**Category:** `design-heuristic`

**The Gem:**
When reducing image brightness is required in high-background or high-scatter conditions:
- **Use a neutral density filter** — reduces brightness without affecting resolving power
  or optical contrast
- **Do NOT reduce aperture** (aperture stop, iris) — reduces brightness but also reduces
  both resolving power (diffraction limit) and contrast

Key reason: in high-scatter environments the eye exit pupil should always be **fully
filled** to maintain contrast. Physical aperture reduction shrinks the exit pupil below
the eye pupil, compounding the contrast loss from scatter.

**When to use it:**
- Bright daylight use of high-power telescopes or spotting scopes
- Any situation where scatter has already reduced contrast and additional brightness
  reduction is needed
- Specifying filter kits for visual instrument systems

**Modern relevance:**
Directly applicable to modern camera and telescope systems. Camera designers sometimes
reduce aperture (increase f/#) instead of using ND filters, at a resolution penalty
that is rarely accounted for in the system performance budget.

---

### 18.8
**Title:** Modest vacuum (1 PSIA) restores image quality degraded by tube currents

**Source:** ch18, §18.6.2.2, page 18-8

**Category:** `design-heuristic`

**The Gem:**
Thermal tube currents — air convection inside telescope tubes caused by temperature
differences — can severely degrade image quality. The fix does **not** require a hard
vacuum. Evacuating the light-path volume to just **1 PSIA** (vs. ~14.7 PSIA atmospheric)
is sufficient to restore image quality nearly to the pre-heating level.

Demonstration experiment: a 3–4 inch telescope under knife-edge autocollimation test
shows nearly complete image degradation when the tube is heated by a flame. Evacuating to
1 PSIA restores image quality, provided the objective can withstand the pressure
differential (or a thick window is placed near the objective).

**When to use it:**
- High-performance ground-based telescopes in thermally variable environments
- Missile tracking telescopes in sun-exposed installations
- Any precision optical system where thermal stability of the air path is in question

**Modern relevance:**
Vacuum telescope tubes are used in solar telescopes (e.g., GREGOR solar telescope)
exactly for this reason. The 1 PSIA threshold means a relatively simple seal and
pump suffice — full hard vacuum is overkill.

**Accuracy / caveats:**
- Requires objective or window that can sustain ~13.7 PSI pressure differential
  without optical deformation

---

### 18.9
**Title:** Solar insolation is mostly visible, not IR — white paint needs visual reflectivity

**Source:** ch18, §18.6.2.4, page 18-9

**Category:** `rule-of-thumb`

**The Gem:**
Solar insolation spectrum breakdown (peak up to 0.028 cal/cm^2/s):
- **>90% of solar energy is below 2 µm**
- **>80% of solar energy is below 1 µm** (i.e., in the visible + near-UV range)

Common misconception corrected: the old idea that solar heating is mostly from infrared,
so only good IR reflectivity is needed in instrument white paint, is wrong. Because ~80%
of the energy is below 1 µm, **good visual (VIS) reflectivity is equally required** for
an effective thermal control paint.

**When to use it:**
- Specifying exterior paint or coating for field instruments exposed to direct sunlight
- Designing thermal control for optical instruments, housings, telescope tubes, domes
- Evaluating white paint specifications — demand both VIS and NIR reflectivity data

**Modern relevance:**
This is the same principle used in spacecraft thermal control (solar absorptance alpha must
be minimized across the full solar spectrum, not just IR). For ground instruments it is
still widely misunderstood. A paint that looks white to the eye but has poor NIR
reflectivity can absorb significant solar energy.

---


<!-- ================================================================ -->
<!-- CHAPTER 19 -- OPTICS FOR MISSILE TRACKING -->
<!-- ================================================================ -->

## Chapter 19 — Optics for Missile Tracking

Chapter 19 bridges classical astronomical telescope design and high-speed military aerospace tracking, analyzing how to balance the extreme and often contradictory requirements of long focal length (100–500 inches), large physical aperture (18–31 inches), wide field of view, high relative aperture (up to f/1), and rapid frame-rate recording on 70 mm film. The chapter establishes the ~12-inch physical aperture crossover where refractive designs yield to all-reflective and catadioptric architectures due to secondary spectrum and blank manufacturing limits. For refractors, it details how internal air spacing (the Clark lens principle) selectively alters zonal and chromatic ray heights at the negative element, providing the exact degrees of freedom needed to eliminate both the ~0.7-zone spherical bulge and sphero-chromatism.

For reflective and catadioptric systems, the chapter derives the fundamental coma-limited field scaling for paraboloids ($v = (f/a)^2 / 25$ inches), details the Cassegrain two-mirror family (standardizing on 4× secondary magnification and paraboloid-hyperboloid conics for coma freedom), and demonstrates how the opposite-sign Petzval curvature of concave mirrors ($P = 2Nc$) enables flat-field catadioptric combinations. It develops the Stop-Shift and Aspheric Placement Principles that govern Schmidt cameras, oblate-spheroid variants (halving tube length from $2f$ to $1f$), and Ross-Baker corrector combinations. Finally, it surveys major operational missile tracking instruments—the 20-inch f/1 Baker-Nunn satellite camera ($31^\circ \times 5^\circ$ curved film format), the 24-inch ROTI Mark II (100"–500" EFL with conjugate-stop aspheric Biotar relays and radar-driven focus wedges), the 18-inch IGOR, and the 30-inch f/3.3 S.M.T. Mangin system.

### 19.1
**Title:** Paraboloid coma-limited useful field scales as (f/#)^2 — the mirror field formula

**Source:** ch19, §19.3.2.3, pages 19-8 to 19-9, Eq. (3)

**Category:** `shortcut-formula`

**The Gem:**
The useful coma-limited field of view of a paraboloidal mirror (where resolution across
the field meets the Rayleigh diffraction limit) is:

$$v = \frac{(f/a)^2}{25} = \frac{(f/\#)^2}{25} \quad \text{(inches)}$$

where $v$ is the linear size (diameter) of the useful field in inches, $f$ is the focal length, and $a$ is the aperture diameter.

Three confirmation points from the chapter:
- f/5 mirror $\rightarrow$ useful field = $5^2/25 = 1.00\text{ inch}$ (confirmed in text)
- f/10 mirror $\rightarrow$ useful field = $10^2/25 = 4.00\text{ inches}$ (confirmed in text)
- Mt. Palomar f/3.3, 200-inch ($f = 660\text{ in}$) $\rightarrow$ useful field = $3.3^2/25 = 0.44\text{ inch}$ ($\approx 0.002\text{ rad} \approx 7\text{ arcmin}$, resolving better than $0.025\text{ arcsec}$)

Field scales as $(f/\#)^2$ because tangential coma grows linearly with field angle and inversely with $(f/\#)^2$. Doubling the f/# quadruples the usable linear field.

**When to use it:**
- Estimating useful field of a new paraboloid or Newtonian reflector without ray tracing
- Deciding between a paraboloid and a Schmidt when wide field is needed
- Checking whether a proposed field size exceeds the coma limit before detailed design

**Modern relevance:**
Unchanged physics — directly applicable to any coma-limited paraboloid (telescope,
satellite tracker, lidar receiver). The Schmidt telescope was invented precisely to
extend beyond this limit; comparing this formula to required field size instantly
tells you whether a catadioptric corrector is needed.

**Accuracy / caveats:**
- Assumes pure paraboloid with stop at mirror; catadioptric correctors change the limit
- Formula is in inches; field scales as $(f/\#)^2$ regardless of units — normalize from
  these data points for SI use
- **Validation note (2026-09-12):** re-deriving from the coma-vs-Airy-disk criterion stated
  in the text gives a linear field that scales as $(f/\#)^3$, not $(f/\#)^2$ — the worked
  examples only confirm the $F^2/25$ arithmetic, not the underlying derivation. The rule is
  still used as-is (it matches the historical text and similar $(f/\#)^2$ rules appear
  elsewhere in amateur/professional telescope literature with denominators in the 9–25
  range), but treat it as unverified pending a check of the full derivation on the scan.

---

### 19.2
**Title:** Reflective vs. refractive system crossover at ~12-inch aperture

**Source:** ch19, §19.1.3, page 19-2

**Category:** `design-heuristic`

**The Gem:**
The crossover aperture between refractive and reflective primaries is approximately
**12 inches (300 mm)**:

- **Aperture $\le$ 12 inches (300 mm):** refractive systems favored
  - Greater mechanical stability
  - Greater depth of focus
  - Superior (cleaner) diffraction pattern (no central obscuration)
  - Easier alignment and maintenance

- **Aperture > 12 inches (300 mm):** reflective systems favored
  - Dramatically smaller and lighter
  - No chromatic aberration or secondary spectrum
  - No glass blank quality constraints at large size
  - Practical necessity at large scale

At larger apertures, the balance "is so decidedly reversed that reflective systems have enjoyed an almost complete monopoly" in 20th-century astronomy.

**When to use it:**
- First system architecture decision for a long-focal-length imaging system
- Evaluating whether to invest in aberration-correction effort for a refractive primary
- Setting scope of color correction work (only needed for refractive primaries)

**Modern relevance:**
The 12-inch crossover still holds for general-purpose imaging. All large telescope
programs (ELT, TMT, JWST) are reflective for exactly these reasons. For military and
space instruments, the weight and color-freedom arguments are even stronger.

---

### 19.3
**Title:** Air-spaced doublet (Clark lens) controls zonal spherical AND sphero-chromatism

**Source:** ch19, §19.2.3 to §19.2.5, pages 19-2 to 19-6

**Category:** `design-heuristic`

**The Gem:**
Two secondary aberrations plague large-aperture refractive objectives (focal lengths
$> 12\text{ inches}$ at f/8 or slower):

1. **Zonal spherical aberration** — characteristic bulge at ~0.7 zone caused by
   imbalance between Seidel and higher-order terms in crown vs. flint elements
2. **Sphero-chromatism** — spherical aberration that varies with wavelength (C and F
   rays have different residual spherical curves)

Both can be controlled by **air-spacing the doublet** (the Clark lens principle):

- **Zonal fix:** Air space allows the ~0.7-zone ray to converge less rapidly than the marginal ray before striking the negative element. The negative element then acts at a higher relative zone and applies more overcorrection — reducing or eliminating the zonal bulge.
- **Sphero-chromatism fix:** Air space causes the F (blue) ray to bend more steeply than the C (red) ray, striking the negative element lower than the C ray. F gets less overcorrection, compensating the natural overcorrection-of-blue tendency of a cemented doublet.

**Practical extension:** A three-element form (split positive crown into two + one negative flint) provides more degrees of freedom — milder curves, better zonal and color balance, easier mounting. This form was used for a 40-inch f/6 and a 24-inch f/5.6 missile tracking lens achieving straight spherical aberration curves at all visible wavelengths (no zonal bulge).

**When to use it:**
- Long-focal-length refractive objectives at f/8 or slower where secondary aberrations
  dominate the on-axis error budget
- Any doublet showing zonal bulge or sphero-chromatism as the residual error
- As a design diagnostic: try an air space before adding more elements

**Modern relevance:**
Air-spaced doublets and triplets are standard in high-performance photographic objectives
and apochromatic telescope lenses. The Clark lens principle explains why modern Zeiss,
Canon, and Nikon apochromats air-space their critical elements.

---

### 19.4
**Title:** Aspheric surface at the stop corrects spherical aberration without affecting off-axis aberrations

**Source:** ch19, §19.4.1, page 19-11

**Category:** `design-heuristic`

**The Gem:**
A fundamental principle of aspheric surface placement:

> "Any change in form, without a change in the vertex radius, has no effect on the
> off-axis Seidel coefficients for an optical surface located at the stop position."

Aspherizing a surface at the stop corrects **spherical aberration only** — coma,
astigmatism, field curvature, distortion, and lateral color are all unchanged.

This is the theoretical basis of the Schmidt corrector plate. The plate sits at the
center of curvature of the spherical mirror (which is the stop for that arrangement),
correcting the mirror spherical without introducing any off-axis aberrations.

Corollary from the Seidel stop-shift rules:
- Coma change from stop shift is proportional to the spherical coefficient
- Astigmatism change is proportional to the coma coefficient
Therefore: fix spherical first (aspheric at stop), then adjust coma/astigmatism via
stop position shift — a clean two-step design sequence.

**When to use it:**
- Choosing where to place an aspheric element: try the stop position first
- Schmidt telescope design: corrector at center of curvature (the stop)
- Adaptive optics: deformable mirror at the pupil plane corrects wavefront error
  without introducing field-dependent aberrations
- Any system where spherical correction must not disturb a balanced off-axis design

**Modern relevance:**
Used constantly in modern lens design software and in adaptive optics. Pupil-plane
phase plates exploit this rule. It is foundational and cannot be derived from intuition.

---

### 19.5
**Title:** Concave mirror Petzval curvature is opposite sign to positive lens — enables flat-field catadioptrics

**Source:** ch19, §19.3.3.6, page 19-10, Eq. (8)

**Category:** `design-heuristic`

**The Gem:**
Petzval field curvature of a reflecting surface:

$$P = 2 N c$$

where $N$ is the refractive index of the surrounding medium ($N = 1$ in air) and $c = 1/r$ is surface curvature.

For a **concave mirror** (converging), this Petzval contribution is **convex toward
incident light** — the opposite sign from a converging refracting lens (which contributes
Petzval curvature that is concave toward incident light).

Key consequence: **combining reflective and refractive powered elements can cancel
Petzval curvature and produce a flat field**, even though each subsystem alone strongly
curves the focal surface.

This is why catadioptric systems (Schmidt-Cassegrain, Maksutov, Ross corrector) can
achieve flat fields that neither a pure mirror nor a pure lens system can provide with
the same element count.

**When to use it:**
- Designing a catadioptric system where flat field is required
- Estimating the sign and power of refractive field corrector needed for a mirror system
- Understanding why adding a Ross/Wynne corrector lens to a telescope flattens the field

**Modern relevance:**
All modern Schmidt-Cassegrain and Ritchey-Chretien designs exploit this sign reversal.
The formula $P = 2Nc$ is standard for fast Petzval budget estimates before committing
to full optimization.

---

### 19.6
**Title:** Schmidt tube = 2x focal length; oblate spheroid variant halves tube to 1x focal length

**Source:** ch19, §19.4.2.5 to §19.4.2.7, pages 19-12 to 19-13

**Category:** `design-heuristic`

**The Gem:**
Standard Schmidt telescope packaging constraint:
- Corrector plate must sit at the **center of curvature** of the spherical mirror
- Center of curvature is at distance $2f$ from the mirror vertex
- Therefore: **Schmidt tube length = 2 × focal length** — unavoidably long

Also: to prevent vignetting, the primary mirror must be **larger than the clear aperture**
(Mt. Palomar Schmidt: 48-inch aperture, 72-inch primary = 1.5× oversize).

**Oblate spheroid variant — half the tube:**
Replace the spherical primary with an oblate spheroid (coefficient of $y^4$ term
$> 1/(8r^3)$ — more curved than a sphere). This surface has 2× the spherical aberration
of a sphere. By the Seidel stop-shift principle, coma can be corrected by moving the
stop only to the **focus** (not center of curvature) — **halving the tube length to $1f$**.

Trade-off: oblate spheroid corrects only half the astigmatism of the full Schmidt.
A slight over-shift of the stop (beyond focus) can reduce residual astigmatism at the
cost of some residual coma — a compromise.

**When to use it:**
- Initial packaging estimate for Schmidt-type systems: plan for tube = $2f$
- When packaging is constrained: oblate spheroid primary allows tube = $1f$
- Evaluating Schmidt variants for tracking cameras and wide-field surveys

**Modern relevance:**
The $2f$ length constraint is why Schmidt telescopes are rarely built above ~1 m aperture
(the tube becomes unmanageable). Compact variants (Houghton, Maksutov) use refracting
correctors to reduce this length.

---

### 19.7
**Title:** Cassegrain secondary magnification is typically 4x; paraboloid-hyperboloid is standard coma-free form

**Source:** ch19, §19.3.3.1 and §19.3.3.4, pages 19-9 to 19-10

**Category:** `reference-data`

**The Gem:**
Two standard design facts for Cassegrain two-mirror systems:

**1. Secondary magnification — favorite value is 4x:**
The secondary mirror magnifies the primary focal length, multiplying both the effective
focal length and f/# by the same factor. The preferred value is 4× (though variable).
- Example: f/3 primary + 4× secondary $\rightarrow$ f/12 system at long effective focal length
- Enables large effective focal lengths from compact primary mirrors

**2. Standard mirror form for coma freedom:**
Among all Cassegrain two-mirror combinations giving zero spherical aberration, the form
most nearly free from coma is:
- **Primary: paraboloid** with intermediate focus at $F_1$
- **Secondary: hyperboloid** with foci at $F_1$ and the final focus $F_2$

This paraboloid-hyperboloid combination is used in "all designs known to the author"
(as of 1962), except extremely slow (large f/#) systems where two spherical mirrors
suffice because spherical aberration is negligible.

**When to use it:**
- First-pass Cassegrain layout: assume 4× secondary magnification, then optimize
- Choosing mirror conic sections: start with paraboloid + hyperboloid
- Reading telescope data sheets: check effective focal length / primary focal length
  against the ~4× nominal

**Modern relevance:**
Standard in all modern Cassegrain and Ritchey-Chretien telescopes. The classical
paraboloid-hyperboloid form is the Dall-Kirkham variant; the Ritchey-Chretien uses
hyperboloid + hyperboloid for improved off-axis correction at the cost of more
demanding mirror fabrication.

---

### 19.8
**Title:** Schmidt corrector neutral zone at 0.8 aperture minimizes axial chromatic aberration

**Source:** ch19, §19.4.2.3, page 19-12

**Category:** `design-heuristic`

**The Gem:**
When profiling a Schmidt corrector plate, placing the zero-slope (parallel face) neutral zone at the center ($y = 0$) causes pure negative power and maximum chromatic aberration.

By adding a slight positive central curvature, the neutral zone (inflection point of zero power) is shifted outward:

> "With the parallel zonal section approximately 0.8 of the distance from the center to the margin, the plate imparts the minimum axial color to the beam."

This splits the plate into a central positive zone and a marginal negative zone, reducing peak optical path difference and minimizing secondary chromatic aberration (color-spherical aberration) by approximately a factor of 4.

**When to use it:**
- Profiling Schmidt corrector plates or aspheric phase corrector plates
- Balancing monochromatic wavefront correction against chromatic defocus
- Specifying aspheric fourth-order coefficients: $z = \frac{y^4 - k y_0^2 y^2}{4(n-1)R^3}$ with $k \approx 1.0$ (neutral zone at $y \approx 0.707 y_0$) to $k \approx 1.28$ (neutral zone at $0.80 y_0$)

**Modern relevance:**
Standard profile design equation for all astronomical Schmidt plates, Schmidt-Cassegrains (Celestron/Meade), and lidar corrector plates.

---

### 19.9
**Title:** Conjugate pupil-plane aspheric correction eliminates full-aperture corrector plates in relay systems

**Source:** ch19, §19.5.2.6, page 19-17

**Category:** `design-heuristic`

**The Gem:**
By Principle 3 (§19.4.1), an aspheric profile placed at an aperture stop or conjugate pupil plane corrects spherical aberration without affecting off-axis Seidel aberrations.

In large, multi-focal-length tracking telescopes (such as the 24-inch ROTI Mark II), placing a massive 24-inch Schmidt plate at the entrance window is eliminated by:
1. Creating an internal conjugate pupil plane at the center of the relay/reimaging lens (the Biotar group).
2. Placing the aspheric correction directly on the small, innermost glass surfaces adjacent to this conjugate stop.

This corrects zonal spherical aberration across multiple turret magnifications (100" to 500" EFL) using small, easily manufactured internal elements while keeping the primary paraboloid available for uncorrected broadband/infrared use.

**When to use it:**
- Designing multi-configuration or turret optical relays with front reflective primaries
- Sizing aspheric correctors: replace large primary-aperture plates with compact pupil-relay aspherics
- Dual-mode visible/IR tracking systems where front refracting correctors must be avoided

**Modern relevance:**
Universal principle in modern zoom lenses, aerial reconnaissance cameras, and adaptive optics pupil relays.

---


<!-- ================================================================ -->
<!-- CHAPTER 20 -- APPLICATIONS OF THIN FILM COATINGS -->
<!-- ================================================================ -->

### 20.1
**Title:** Fresnel surface reflectivity formula with values for common optical glasses

**Source:** ch20, §20.3.1, page 20-21 (Eq. 21)

**Category:** `shortcut-formula`

**The Gem:**
Reflectivity of an uncoated surface at normal incidence:

  R = (n_substrate - n_0)² / (n_substrate + n_0)²

where n_0 is the incident medium (air = 1.00) and n_substrate is the glass index.

Ready-to-use values for common optical glasses:
- Crown glass (n = 1.51): **R = 4.12%** per surface
- Flint glass (n = 1.58): **R = 5.05%** per surface
- Dense flint / sapphire (n = 1.70): **R = 6.72%** per surface *(corrected 2026-09-12: ((0.70/2.70)² = 0.0672; the previously stated 6.44% does not follow from n=1.70 via this formula)*
- Arsenic trisulfide glass (n = 2.40): **R = 17%** per surface
- Silicon (n = 3.50): **R = 30.7%** per surface
- Germanium (n = 4.05): **R = 36.4%** per surface

For a lens with N elements (2N surfaces) all uncoated, transmission = (1 - R)^(2N).
A 5-element (10-surface) lens in crown glass: T ≈ (0.9588)^10 = 0.65 — 35% lost to reflection alone.

**When to use it:**
- Quick budget for uncoated transmission loss in any optical system
- Deciding whether AR coatings are worth adding
- Estimating ghost image intensities (each ghost surface reflects R of the transmitted beam)

**Modern relevance:**
Faster to look up or calculate than running a coating simulation. The per-surface loss
numbers are the designer's first sanity check before specifying AR coatings. High-index
IR materials (Ge, Si) make this formula essential — an uncoated Ge window loses >53%
of transmitted light at two surfaces.

---

### 20.2
**Title:** Ideal single-layer AR coating: n_film = √(n₀·n_substrate); MgF₂ as the practical choice for glass

**Source:** ch20, §20.3.3.2.2, page 20-22 (Eq. 26)

**Category:** `shortcut-formula`

**The Gem:**
For zero reflectivity at a single wavelength, a quarter-wave film must satisfy:

  n_film = √(n_incident × n_substrate)

For air on crown glass (n_substrate = 1.51):
  n_ideal = √(1.00 × 1.51) = **1.23**

No durable thin-film material has n = 1.23. The practical choices:

| Film | n | Notes |
|------|---|-------|
| Cryolite | 1.35 | Closest to ideal; soft, slightly water-soluble — limited field use |
| Magnesium fluoride (MgF₂) | 1.38 | Standard choice: hard, durable, adheres well, survives abrasion |

MgF₂ on n = 1.51 glass at quarter-wave thickness (λ₀ = 550 nm):
- Minimum reflectivity ≈ **1.2%** (vs. 4.1% uncoated) — about 3× better
- The 1.2% residual is the price of using n = 1.38 instead of the ideal 1.23

For higher-index substrates (n > 1.70), MgF₂ gets closer to ideal and AR efficiency improves.
For very high-index IR materials (Ge, Si), film materials exist with n near √n_substrate —
near-zero R is achievable.

**When to use it:**
- Specifying a single-layer AR coating: always start with MgF₂ at QWOT = λ₀/4
- Choosing λ₀: center on the wavelength of peak source energy or detector sensitivity
- Checking if a more complex coating is needed: if 1% residual R is acceptable, MgF₂ suffices

**Modern relevance:**
MgF₂ single-layer AR coating is still the default for broad-wavelength-range applications and
for non-critical surfaces. The √(n₀·ns) formula is the starting point for any AR coating design.

---

### 20.3
**Title:** Silver beam splitter loses 1/3 to absorption; dielectric BS absorbs <1%

**Source:** ch20, §20.7.2.1, page 20-67

**Category:** `rule-of-thumb`

**The Gem:**
**Silver 50/50 beam splitter (typical rule of thumb):**
- Reflects: ~1/3 of incident light
- Transmits: ~1/3 of incident light
- Absorbs: ~1/3 of incident light

This 1/3 absorption loss is the fundamental inefficiency of metal beam splitters.

**Dielectric multilayer 50/50 beam splitter:**
- Reflects: ~50%
- Transmits: ~50%
- Absorbs: <1% (typically)

The dielectric beam splitter is far more efficient. Drawback: its R and T depend on
wavelength and polarization; at 45° incidence R_s ≠ R_p, introducing polarization.

**Polarization caveat:** A dielectric BS with R_avg = 50% may have R_s = 10%, R_p = 90%.
If the source or scene is polarized (sky, wet surfaces), the reflectivities differ in the
two arms of the system — critical to check in interferometers, cameras, and rangefinders.

**When to use it:**
- Quickly estimating light budget when silver BS is used: assume 33% loss per BS
- Choosing between silver and dielectric: if light budget is tight, use dielectric
- Designing for polarization-sensitive applications: always check R_s and R_p separately

**Modern relevance:**
The 1/3 rule appears in optical engineering references but is often forgotten in system
budgets. Even with modern coatings, a silver BS in a multi-pass system accumulates large losses.

---

### 20.4
**Title:** Thin film coating materials reference: refractive indices and transparency ranges

**Source:** ch20, §20.2.4.1, Table 20.2, pages 20-15 to 20-16

**Category:** `reference-data`

**The Gem:**
Key evaporated thin-film materials with refractive index and useful wavelength range
(for a film of quarter-wave optical thickness):

| Material | n | Transparent from | Transparent to | Notes |
|----------|---|-----------------|----------------|-------|
| Cryolite / Chiolite | 1.35 | <200 nm | 10 µm | Soft, slightly soluble; chiolite preferred in IR |
| Magnesium fluoride (MgF₂) | 1.38 | 230 nm | 5 µm | Hard, durable; standard low-n coating |
| Thorium fluoride (ThF₄) | 1.45 | <200 nm | 10 µm | Hard, good UV-IR range |
| Silicon monoxide (SiO) | 1.45–1.90 | 350 nm | 8 µm | **n varies with O₂ pressure during evap** |
| Sodium chloride (NaCl) | 1.54 | 180 nm | >15 µm | Lab only — water soluble |
| Zirconium dioxide (ZrO₂) | 2.10 | 300 nm | >7 µm | Hard, good mid-range high-n |
| Zinc sulfide (ZnS) | 2.30 | 400 nm | 14 µm | Standard high-n, slight compressive stress |
| Cerium dioxide (CeO₂) | 2.30 | 400 nm | 5 µm | Hard, good visible high-n |
| Titanium dioxide (TiO₂) | 2.40–2.90 | 400 nm | >7 µm | High n, dispersive in blue |
| Silicon (Si) | 3.50 | 900 nm | 8 µm | Very high n for near-IR |
| Germanium (Ge) | 3.80–4.20 | 1400 nm | >20 µm | Highest available n, far IR |
| Lead telluride (PbTe) | 5.2–10 | 3900 nm | >2 µm | Extreme n for far IR |

**Critical practical note on SiO:** The refractive index of silicon monoxide varies from
1.45 to 1.90 depending on the partial pressure of oxygen during evaporation. Films with
n > 1.75 absorb below 500 nm (yellowish appearance). Control O₂ partial pressure to
set the desired n.

**When to use it:**
- First step in any thin-film design: check available n values at the required wavelength
- IR filter design: choose from ZnS, Ge, PbTe for high-n; cryolite or NaCl for low-n
- Hard coating requirement: MgF₂, ZrO₂, CeO₂, TiO₂, Ge, Si are the durable options

**Modern relevance:**
This consolidated table remains the starting point for any thin-film design. The index values
and transmission ranges shown here are still broadly representative of what commercial coaters use.

---

### 20.5
**Title:** Film cracking thickness limit: MgF₂ and CeO₂ crack above ~1 µm physical thickness

**Source:** ch20, §20.2.4.2.5, page 20-18

**Category:** `design-heuristic`

**The Gem:**
Evaporated thin films develop mechanical stress during deposition. Most materials are
in tensile stress (the film wants to contract). If the film grows too thick, stress exceeds
adhesion and the film cracks or peels.

**Practical cracking limits:**
- Magnesium fluoride (MgF₂): cracks when physical thickness > **~1 µm**
- Cerium dioxide (CeO₂): same, ~1 µm limit
- Zinc sulfide (ZnS): compressive stress (opposite sign) — much less prone to cracking;
  can be evaporated thicker, making it preferred for mid-IR designs
- Silicon monoxide (SiO): low stress, can be made quite thick

**Consequence for IR coatings:** A quarter-wave layer at 10 µm has physical thickness ≈
10/(4 × n) µm. For MgF₂ (n = 1.38): t_phys = 1.81 µm — already over the cracking limit.
Hence MgF₂ cannot be used as a primary layer beyond ~5–6 µm IR.

**Stress compensation trick:** Pair a tensile-stress material (e.g., MgF₂) next to a
compressive-stress material (ZnS) with thicknesses chosen so net stress cancels.

**When to use it:**
- IR coating design: check physical thickness against cracking limits before finalizing
- Specifying material pairs: if one layer is near its limit, add a ZnS layer to compensate
- Explaining coating failures: peeling or crazing after deposition → stress exceeded adhesion

**Modern relevance:**
Still a real constraint for IR multilayers. Coating houses routinely manage stress balance
in thick IR coatings, but knowing the ~1 µm rule helps identify the risk early in design.

---

### 20.6
**Title:** Half-wave absentee layer: a λ/2 film contributes nothing to reflectivity at that wavelength

**Source:** ch20, §20.1.5.2.2, page 20-8

**Category:** `design-heuristic`

**The Gem:**
Any dielectric film whose optical thickness equals λ/2, λ, 3λ/2, 2λ, … has a
characteristic matrix equal to the identity matrix at that wavelength. It is therefore
**optically absent** — it contributes nothing to the reflectivity of the stack.

This "absentee layer" principle has two immediate uses:

**1. Simplifying analysis:** To find T_max of a Fabry-Perot filter at its design wavelength,
remove the half-wave spacer layer (it is absentee), then remove any other half-wave
combinations that result — the stack reduces to just the two mirror coatings back-to-back.

**2. Protective overcoats without optical penalty:** A half-wave SiO layer on an aluminum
mirror does not change the mirror's reflectivity at the design wavelength but provides
abrasion and chemical protection.

**3. Design degree of freedom:** Insert a half-wave layer anywhere in a stack to provide
mechanical support or control stress without altering the filter's spectral transmission
at the design wavelength.

**Quick check:** For a film with QWOT = λ₀/4, the film is absentee at λ = λ₀/2 (g = 2.0),
λ₀/4 (g = 4.0), etc. in the reflectivity vs. g = λ₀/λ plots.

**When to use it:**
- Analyzing a complex multilayer: start by removing all absentee layers at the wavelength of interest
- Specifying protective overcoats: choose thickness = λ/2 at center wavelength
- Explaining why a thick protective layer doesn't ruin reflectivity

**Modern relevance:**
Used in every thin-film design software. Understanding it analytically lets you reduce
a 15-layer stack to a 3-layer equivalent for quick estimates at a specific wavelength.

---

### 20.7
**Title:** Quarter-half-quarter (QHQ) broadband AR: R < 0.5% across the entire visible spectrum

**Source:** ch20, §20.3.5.3, pages 20-36 to 20-38

**Category:** `design-heuristic`

**The Gem:**
A three-layer quarter-half-quarter (QHQ) antireflection coating reduces reflectivity
below 0.5% (R < 0.005) across the entire visible spectrum (400–700 nm):

  Structure: Air | λ/4 low-n | λ/2 mid-n | λ/4 low-n | Glass

Practical example recipes (from measured data, Hass 1962):
- MgF₂ + ZrO₂ + CeF₃ on glass (Fig. 20.44)
- MgF₂ + Nd₂O₃ + CeF₃ on glass (Fig. 20.45)
- MgF₂ + SiO + CeF₃ on glass (Fig. 20.46)

Compared to single-layer MgF₂:
- Single MgF₂: R ≈ 1.2% at design λ, rises to 3–4% at band edges
- QHQ triple-layer: R < 0.5% across the full visible — roughly 5–8× better

**Trade-off:** The QHQ coating has sharp reflectivity rise outside its design band (from
g ≈ 0.6 to g ≈ 1.2, about one octave). Single-layer MgF₂ never exceeds uncoated
reflectivity; the QHQ can exceed it outside the design band.

**When to use it:**
- Multi-element camera or photographic lenses where flare and ghost images matter
- Any system where visible-band throughput must be maximized (R < 0.5% per surface)
- Standard camera lens AR coating: QHQ or its derivatives are the baseline

**Modern relevance:**
The QHQ structure is the ancestor of all modern "multicoating" (MC) lens designations.
Modern coatings have evolved to 5-7 layers for even better performance, but QHQ
remains the minimum for calling a lens "multicoated."

---

### 20.8
**Title:** Quarter-wave stack high-reflectance zone width formula

**Source:** ch20, §20.4.1.4, page 20-39 (Eq. 39)

**Category:** `shortcut-formula`

**The Gem:**
For a quarter-wave stack (alternating H and L layers, each of QWOT = λ₀/4), the
half-width of the high-reflectance zone in units of g = λ₀/λ is:

  Δg = (2/π) × arcsin |(n_H - n_L) / (n_H + n_L)|

The total width of the high-reflectance zone is 2Δg.

**Example values:**

| Materials | n_H | n_L | Δg | Full zone width |
|-----------|-----|-----|----|-----------------|
| ZnS / MgF₂ (visible) | 2.30 | 1.38 | 0.161 | 32% of λ₀ |
| TiO₂ / MgF₂ (visible) | 2.40 | 1.38 | 0.170 | 34% |
| Ge / ZnS (IR) | 4.05 | 2.30 | 0.178 | 36% |
| Ge / cryolite (IR) | 4.05 | 1.35 | 0.333 | 67% |

*(Corrected 2026-09-12: recomputing Δg=(2/π)arcsin|(n_H-n_L)/(n_H+n_L)| for the two IR
pairs did not reproduce the previously stated 0.273/55% and 0.434/87% — those numbers
are ~50% too high. The visible-band rows (ZnS/MgF₂, TiO₂/MgF₂) check out exactly.)*

**Key design facts from this formula:**
1. The zone width depends only on the index **ratio** n_H/n_L, not the absolute values.
2. A quarter-wave stack always has the **widest** possible high-reflectance zone
   for a given pair of materials — 2:1 and 3:1 stacks are narrower.
3. Adding more periods (more layer pairs) increases peak reflectivity but does NOT
   widen the zone — only changing materials changes the width.

**When to use it:**
- Specifying a long-pass or short-pass filter: check if the zone width covers the required
  rejection band with the chosen materials
- Comparing two material pairs: compute Δg to see which gives wider coverage
- Designing broadband mirrors: choose materials with large index ratio for wide zone

**Modern relevance:**
This formula remains the key first-pass check for any stack-based reflector or filter.
It predicts behavior without running a full thin-film simulation.

---

### 20.9
**Title:** Overcoated aluminum mirrors reach 99.4% reflectivity; bare Al gives ~90%

**Source:** ch20, §20.8.1.3, page 20-69

**Category:** `reference-data`

**The Gem:**
Reflectivity of aluminum mirror coatings in the visible (400–800 nm):

| Mirror type | Reflectivity | Notes |
|-------------|--------------|-------|
| Bare aluminum | ~90% | Naturally self-protecting via thin Al₂O₃ layer |
| Al + SiO protective overcoat | 78–90% | SiO may reduce R at some wavelengths |
| Al + 6-layer ZnS/MgF₂ dielectric stack | **99.4–99.6%** | Measured by Jenkins (1958) |
| Bare silver (fresh) | ~95% in red, lower in blue | Deteriorates; not durable |
| Rhodium | ~80–85% | Durable in harsh environments (salt water) |

**Impact of multiple reflections:**
With N mirror surfaces in the beam, throughput = R^N.

| R per surface | 4 reflections | 8 reflections |
|---------------|---------------|---------------|
| 90% (bare Al) | 66% | 43% |
| 99.5% (overcoated) | 98% | 96% |

For a periscope or multi-fold optical path with 8 mirrors: bare Al loses 57%; overcoated
loses only 4%.

**When to use it:**
- Multi-bounce systems (periscopes, laser cavities, multi-pass cells): bare Al is inadequate
- System throughput budget: use 90% for unspecified Al mirrors, 99.4% for specified overcoated
- Choosing rhodium vs. Al: rhodium if exposure to salt spray or harsh chemicals

**Modern relevance:**
Dielectric-overcoated aluminum is standard for high-performance laser and telescope optics.
The 99.4% figure is still achievable with modern ZnS/MgF₂ or equivalent stacks.

---

### 20.10
**Title:** Fabry-Perot interference filter angle-tuning and collimation requirements

**Source:** ch20, §20.10.5.3, page 20-86

**Category:** `design-heuristic`

**The Gem:**
Tilting a Fabry-Perot (FP) interference filter shifts its pass band to **shorter wavelengths**
(blue shift) because the effective optical path decreases with oblique incidence.

**Practical tuning rule:**
Tilting by ~10° shifts the pass band by a few nanometers (exact shift depends on filter
order and index). Use this to fine-tune a filter to an exact wavelength without remaking it.

**Example:** A filter with pass band at 550 nm can be tuned to the mercury green line at
546.1 nm by tilting ~10° or less.

**Collimation requirement for narrow-band filters:**
In a convergent beam (f/N), rays hit the filter at a range of angles, each shifted by a
different amount → the pass band **broadens asymmetrically** toward shorter wavelengths.

**Design correction for f/2 beam (Lissberger & Wilcock, 1959):**
Place the filter's Tmax at λ₀ = 502 nm if the goal is 500 nm response in an f/2 beam.
(The 2 nm offset compensates the blue-shift broadening of a fast convergent beam.)

**Collimation rule:** The narrower the filter bandwidth, the more collimated the beam must be.
Filters with Δλ < 1 nm should be used only in well-collimated beams (f/20 or slower).

**When to use it:**
- Fine-tuning a filter to an exact emission line: tilt instead of ordering a new filter
- Placing a filter in a converging beam: shift Tmax slightly red at normal incidence to compensate
- Specifying illumination for narrowband work: match collimation to bandwidth requirement

**Modern relevance:**
The blue-shift-with-tilt behavior is still the dominant practical constraint on using
narrowband interference filters. Every solar telescope and narrowband imager uses this
to tune H-alpha or Ca K filters to the exact line center.

---


<!-- ================================================================ -->
<!-- CHAPTER 21 -- COATING OF OPTICAL SURFACES -->
<!-- ================================================================ -->

### 21.1
**Title:** R_min formula for non-ideal monolayer AR coating

**Source:** ch21, §21.6.3.2, page 43 (eq. 179)

**Category:** `shortcut-formula`

**The Gem:**
For a quarter-wave monolayer that cannot meet the zero-reflectance condition (n₁ ≠ √(n₀·n₂)),
the minimum achievable reflectance at normal incidence is:

    R_min = [(n₁² - n₀·n₂) / (n₁² + n₀·n₂)]²

Practical example — MgF₂ (n₁ = 1.38) on crown glass (n₂ = 1.52) in air (n₀ = 1):

    R_min = [(1.904 - 1.52) / (1.904 + 1.52)]² ≈ 1.26%

The coating reduces surface reflectance from 4.1% (bare glass) to ~1.26%, but cannot reach zero.
Zero would require the ideal n₁ = √1.52 = 1.233 — not available as a rugged deposited film.

**When to use it:**
- Estimating the AR performance limit of any available monolayer material before running spectral simulations
- Deciding whether a bilayer is required (when single-layer R_min is still too high)
- Measuring n₁ of an evaporated film from spectrophotometer data: solve for n₁ given measured R_min

**Modern relevance:**
Instantly quantifies the fundamental limit of any single-layer coating given real material choices.
Replaces a full spectral calculation when you only need to know if a monolayer is even worth trying.

**Accuracy / caveats:**
- Normal incidence formula; at oblique incidence, replace indices with effective M values
- Assumes non-absorbing film and substrate
- Evaporated film indices typically lower than bulk; measure n₁ for accurate results

---

### 21.2
**Title:** TiO₂ inner-layer thickness is universal across all common glasses in bilayer AR

**Source:** ch21, §21.7.3.2, page 55

**Category:** `design-heuristic`

**The Gem:**
In a TiO₂/MgF₂ bilayer AR coating (n_TiO₂ ≈ 2.50, n_MgF₂ ≈ 1.38) on glass in air, the
required optical path of the inner TiO₂ layer for zero reflectance is nearly constant at:

    p₁ ≈ 15.5° = 0.043λ  (optical path fraction)

across the full range of ordinary optical glasses (n = 1.50 to 1.70). This has been confirmed
experimentally. The corresponding physical thickness is only 0.043λ/2.50 = 0.017λ — a very
thin inner layer.

The outer MgF₂ layer thickness must be tuned per glass type (it controls the wavelength of
minimum reflectance) but the inner TiO₂ layer is fixed.

**Practical note:** CeO₂ is preferred over TiO₂ in practice — it can be evaporated as a
dielectric without post-deposition heating and oxidation. Reapply eqs. (185)–(186) using
CeO₂ optical constants to obtain the (slightly different) universal inner-layer thickness.

**When to use it:**
- Designing bilayer AR coatings for multiple glass types from one chamber run
- Estimating TiO₂ (or CeO₂) layer thickness without solving the full bilayer equations
- Checking whether a single inner-layer thickness can serve a mixed-glass product line

**Modern relevance:**
This universality simplifies production: one inner-layer thickness serves an entire glass catalog.
The insight still applies to modern high-n / low-n bilayer AR designs (e.g., Ta₂O₅ / SiO₂).

---

### 21.3
**Title:** Equivalent quarter-wave bilayer replaces unavailable film index (Jupnik's principle)

**Source:** ch21, §21.9.2–21.9.3, page 67 (eq. 201–202)

**Category:** `design-heuristic`

**The Gem:**
Any quarter-wave layer of "unavailable" refractive index n₃ can be replaced by a two-layer
quarter-wave bilayer (n'₁, n'₂) that is optically equivalent at the design wavelength, provided:

    n'₁ · n'₂ = n₃²   →   n'₁ / n'₂ = n₃² / (n'₁)²

One index can be freely chosen (e.g., set n'₂ = 1.384 for MgF₂). Then:

    n'₁ = n₃² / n'₂

**Jupnik's quadrilayer example:** A QHQ trilayer with ideal n₃ = √(n₁·n₂) is replaced by a
four-layer system where the unavailable quarter-wave layer is substituted with an equivalent
MgF₂/intermediate-index bilayer. Result: R < 0.1% over 0.45–0.70 µm using only available
materials (MgF₂, ZnS, and one intermediate material around n ≈ 1.55).

**When to use it:**
- When the target quarter-wave index is not available as a durable, non-absorbing deposited film
- Designing high-performance AR coatings with a limited material palette
- Applies to any single quarter-wave layer in any multilayer design (not just AR coatings)

**Modern relevance:**
Available film materials have not expanded dramatically since 1962. Achieving an effective
index through layer equivalence is still the primary workaround for index gaps in the
material library, and is used routinely in modern coating design software.

---

### 21.4
**Title:** Single-layer AR at 45° incidence fails on crown glass — rugged films below n = 1.30 unavailable

**Source:** ch21, §21.6.7, pages 47–48

**Category:** `design-heuristic`

**The Gem:**
For a single-layer AR coating at 45° angle of incidence on spectacle crown glass (n = 1.52):
- The s-polarized (E-perpendicular) reflectance requires film index n₁ → 1.2 to drop below 1%
- No rugged deposited film with n < 1.30 is available (MgF₂ is the softest limit at n = 1.38)
- Therefore a single-layer AR coating cannot achieve low reflectance on crown glass at 45°

The p-polarized (H-perpendicular) component approaches zero at Brewster's angle naturally
and is not the limiting factor. The problem is entirely in the s-polarization.

**Exception:** High-index substrates (n ≥ 3.45, e.g., silicon, germanium) are more tractable —
available film materials (n ≈ 1.7–2.0) can achieve single-layer AR at oblique incidence.

**When to use it:**
- Before investing time in single-layer AR designs for prisms, beamsplitter plates, or any
  surface used at oblique incidence with low-index glass
- Ruling out monolayer solutions quickly: if n₁ < 1.30 is required, a bilayer is needed
- IR optics on high-index substrates are the exception where single-layer oblique AR works

**Modern relevance:**
The materials limitation is unchanged. This rule prevents wasted design effort and directs
the engineer immediately toward bilayer or V-coat configurations for oblique-incidence AR.

---

### 21.5
**Title:** High-reflector stack rule: maximize n_H/n_L ratio; 11-layer ZnS/MgF₂ stack exceeds silver

**Source:** ch21, §21.10.4–21.10.6, pages 69–71 (eq. 212)

**Category:** `rule-of-thumb`

**The Gem:**
For an alternating quarter-wave high/low index stack (HL)^M H (N = 2M+1 layers total):

1. **To maximize R for fewest layers:** maximize n_H/n_L
2. **Layer order:** start with high-n layer on the substrate when n_H > n_L

Closed-form reflectance at design wavelength λ₀ (N = 2M+1 odd, stack HLHL…H adjacent
to the substrate, illuminated from medium n₀):

    Y = n_H² · (n_H/n_L)^(N-1) / n_sub      (equivalent admittance seen by the incident medium)
    ρ₀ = (n₀ - Y) / (n₀ + Y)                 R = |ρ₀|²

*(Corrected 2026-09-12: the previously stated form, ρ₀=[n₀(n_H/n_L)^N - n_sub]/[n₀(n_H/n_L)^N + n_sub],
does not reproduce the worked example below — it gives R≈98.3%, not 99.46%. The equivalent-admittance
form above does reproduce it exactly and is the standard result for a terminated quarter-wave stack.)*

Worked example — (HL)⁵H with ZnS/MgF₂ (n_H = 2.35, n_L = 1.38) on glass (n_sub = 1.52):

    Y = 2.35² × (2.35/1.38)^10 / 1.52 ≈ 745.2
    ρ₀ = (1 - 745.2)/(1 + 745.2) = -0.9973   |ρ₀|² = 0.9946  →  T = 0.54%  at λ₀ = 750 nm

This exceeds the reflectance of evaporated silver (~90–96%), and the dielectric stack has
zero absorption and excellent durability.

**When to use it:**
- Estimating how many layers needed for a target reflectance before full simulation
- Comparing dielectric HR coating vs. metallic mirror performance
- Selecting n_H/n_L material pair for a given reflectance target

**Modern relevance:**
Equation (212) gives peak reflectance in closed form with no iteration — a fast sanity check
for laser mirror and cold-mirror designs. Modern LIDT-critical systems use dielectric HR stacks
almost exclusively; this rule guides initial layer count estimation.

[NEEDS FIGURE 21.36]

---

### 21.6
**Title:** Thin-film interference filter half-width formula and design trade-offs

**Source:** ch21, §21.10.8.3–21.10.8.5, pages 75–77 (eq. 225–227)

**Category:** `shortcut-formula`

**The Gem:**
For a Fabry-Perot thin-film interference filter (symmetric HR multilayer stacks flanking
a spacer of optical order ν):

    |Δλ| = (λ₀/ν) · (1 - |ρ₀|²) / (π · |ρ₀|)

where |ρ₀| is the amplitude reflectance of each HR stack at λ₀.

To narrow the pass band:
- Increase |ρ₀|: add more layers to each HR stack
- Increase ν: use a thicker spacer (at cost of extra subsidiary pass bands)

**Worked example** — ZnS/MgF₂, 7-layer HR stacks (n_H=2.35, n_L=1.38), half-wave spacer:

    |ρ₀| = 0.9899,  ν = 1  →  |Δλ| = 36.2 Å
    ν = 3 (triple-wave spacer)  →  |Δλ| = 12.1 Å

Below 1 Å half-width becomes very difficult with dielectric stacks alone.

**Watch out for subsidiary pass bands:** A second pass band appears at wavelength λ_sub where
2·n_s·d_s = (ν+1)·λ_sub. For ν = 3, this lies near λ₀·(3/4) — must be blocked by a
separate blocking filter.

**When to use it:**
- Rapid pass-band estimation before running full multilayer simulation
- Trade-off analysis: bandwidth vs. layer count, or bandwidth vs. spacer order
- Identifying whether a single-cavity design meets requirements or a multi-cavity is needed

**Modern relevance:**
This is the standard Fabry-Perot finesse equation applied to thin-film stacks and remains
the go-to formula for first-pass filter bandwidth estimation in spectroscopy instrument design.

---


<!-- ================================================================ -->
<!-- CHAPTER 22 -- INFRARED OPTICAL DESIGN -->
<!-- ================================================================ -->

### 22.1
**Title:** IR resolution degradation rule: 5× coarser at 3 µm, 18× coarser at 10 µm

**Source:** ch22, §22.6.2.1, page 22-6

**Category:** `rule-of-thumb`

**The Gem:**
Diffraction-limited angular resolution scales linearly with wavelength. Relative to 0.56 µm
(mid-visible reference):

| Wavelength | Relative resolution loss |
|------------|--------------------------|
| 3 µm       | **5× coarser**           |
| 10 µm      | **18× coarser**          |

There is no gain from correcting aberrations below the diffraction limit — stop when the
Rayleigh criterion is satisfied for the operating wavelength.

**When to use it:**
- Quickly estimating achievable angular resolution for any IR system
- Deciding when to stop aberration correction in an IR design
- Warning system proposers what resolution is physically achievable

**Modern relevance:**
A fast sanity check when transitioning a visible-band design to IR, or when evaluating
detector pixel size relative to the diffraction spot. The 18× figure at 10 µm is often
surprising to engineers new to IR optics.

**Accuracy / caveats:**
- Based on 0.56 µm reference; scale proportionally for other visible wavelengths
- Applies to circular apertures with Rayleigh criterion; Strehl-based limits scale the same way

---

### 22.2
**Title:** Ordinary optical glass usable to 2.7 µm; flints transmit better than crowns near the cutoff

**Source:** ch22, §22.2.4, page 22-1

**Category:** `reference-data`

**The Gem:**
Ordinary optical glass absorption as a function of wavelength:

- Transmits satisfactorily: **≤ 2.0 µm**
- Absorption begins noticeably: **~2.0 µm**
- Absorption becomes severe: **~2.6–2.7 µm** (varies by glass type)
- Hard cutoff — do not use ordinary glass: **beyond 2.7 µm**

In the marginal 2.0–2.7 µm zone, **flints transmit slightly better than crowns**.
Evaluate individual glass types — there is meaningful variability within each class.

It may still be worth using ordinary glass up to ~3.5 µm if the combination of source
spectrum, filters, atmosphere, and detector response means only a small fraction of the
system response is lost — evaluate case by case.

**When to use it:**
- Deciding whether ordinary glass is acceptable for a 1–3 µm system
- Selecting between crown and flint types near the absorption edge
- Assessing whether a small loss of detector response is an acceptable trade for using ordinary glass

**Modern relevance:**
Directly applicable today — the glass absorption cutoff is a fixed material property.
The flint-vs-crown transmission edge advantage is a useful shortcut when evaluating glass
substitutions in 1.5–2.5 µm systems.

---

### 22.3
**Title:** Near-IR achromatization (0.8–1.2 µm) requires ~2× stronger element powers than visible

**Source:** ch22, §22.2.3, page 22-1

**Category:** `design-heuristic`

**The Gem:**
Crown and flint glass V-values (Abbe numbers) converge in the near-IR: the dispersion
ratio between crown and flint approximately halves compared to the visible band. To
achromatize a doublet in the 0.8–1.2 µm band, individual element focal lengths must be
roughly **twice as short** (twice the power) as in a visible achromat of the same system
focal length.

Worked example — 100 mm FL doublet, light barium crown (1.5725/57.4) + dense flint (1.6170/36.6):

| Band | Crown FL | Flint FL |
|------|----------|----------|
| Visible (C–F lines) | 36 mm | 57 mm |
| Near-IR (0.8–1.2 µm) | 19 mm | 23 mm |

Consequence: the strong curves required for near-IR achromatization often force replacement
of a single crown element with two elements to avoid high-order aberrations.

**When to use it:**
- Estimating aberration budgets for near-IR refracting systems
- Anticipating when a visible design must be restructured for near-IR use
- Deciding early whether a reflecting primary is preferable (completely eliminates this problem)

**Modern relevance:**
A quick pre-design estimate before entering a full IR lens optimization. The ~2× rule saves
time when evaluating whether an existing visible design can be adapted for 0.8–1.2 µm use.

---

### 22.4
**Title:** Mid-IR Abbe number ratio can reach 46:1 — far exceeding the visible limit of 2.4:1

**Source:** ch22, §22.2.5, page 22-2

**Category:** `reference-data`

**The Gem:**
The range of V-value (Abbe number) ratios available for achromatization:

| Band | Max V-ratio (crown:flint) |
|------|--------------------------|
| Visible | ~2.4:1 |
| Mid-IR (3.5–5.5 µm) | up to **46:1** (Si positive + suitable negative) |

This enormous dispersion contrast in the mid-IR allows achromatization with much weaker
individual element powers than in the visible — the opposite of the near-IR convergence
problem (22.3).

In practice, material availability for a given application (environmental, mechanical,
cost constraints) usually restricts the designer to only a few usable materials, so the
theoretical freedom is rarely fully exploited. When glass selection is constrained, a
reflecting primary with refracting correctors is often the practical alternative.

**When to use it:**
- Estimating how easily a mid-IR system can be achromatized
- Selecting material pairs to maximize V-ratio in the 3.5–5.5 µm band
- Justifying a Si-based design element when chromatic correction is the priority

**Modern relevance:**
Calibrates intuition: designers assuming mid-IR chromatic correction is harder than visible
are wrong for the 3.5–5.5 µm band. The 46:1 V-ratio is an under-appreciated design freedom.

---

### 22.5
**Title:** Optical immersion multiplies IR detector light-receiving ability by n²

**Source:** ch22, §22.6.7.7–22.6.7.8, pages 22-11 to 22-12

**Category:** `shortcut-formula`

**The Gem:**
A detector optically immersed in a medium of refractive index n can receive up to **n² times**
more flux than the same detector in air — for the same detector area. This follows from the
second law of thermodynamics (étendue / brightness conservation argument).

Practical implementation: place the detector at the center of a **hemisphere** of the immersion
material. All rays entering the flat face of the hemisphere strike the curved surface at
normal incidence and reach the detector at angles up to ~90°, fully realizing the n² gain.

Key examples:

| Material | n | Immersion gain (n²) |
|----------|----|---------------------|
| Air (none) | 1.0 | 1× |
| BaF₂ | ~1.5 | ~2.3× |
| Strontium titanate | 2.2 | **4.8×** |
| Germanium | ~4.0 | **~16×** |

**When to use it:**
- When detector area must be minimized (for maximum detectivity) but sufficient flux collection is required
- When étendue budget analysis (§22.6.6) shows the detector area needed in air is too large
- As an alternative to enlarging the collecting aperture when detectivity is the bottleneck

**Modern relevance:**
Standard practice in high-performance IR detector design. The n² gain is easily overlooked,
and the hemisphere geometry is the key to achieving it fully. With Ge (n ≈ 4) giving ~16×,
immersion can replace a 4× aperture area increase.

**Accuracy / caveats:**
- n² is the thermodynamic upper limit; in practice k × n² where k = 0.5–0.75 is achievable
  (angles of incidence ≥ 45° for k = 0.5; ≥ 60° for k = 0.75)
- Substrate must transmit the target IR band AND provide mechanical support for the detector
- A plane-parallel substrate in air limits gain to 1× (critical angle blocks high-angle rays) —
  only the hemisphere geometry realizes the full n² factor

**✓ Confirmed 2026-09-13 via deep pass:** ch22's étendue derivation (Eq. 1, page 22-6),
F_s = πIn²A, is the flux-collection formula this gem's n² gain is derived from — direct
equation-level confirmation of the thermodynamic argument.

---

### 22.6
**Title:** Place IR photoconductive detector at image of entrance aperture, not at focal plane

**Source:** ch22, §22.6.4.9, page 22-7

**Category:** `design-heuristic`

**The Gem:**
Photoconductive IR detectors (lead sulfide, lead selenide, etc.) have non-uniform responsivity
across their surface: local "hot spots" and geometry effects near the bias contact leads mean
that where radiation falls matters, not just total flux. To avoid this degrading performance:

**Do not place the detector at or near a focal (image) plane.**
Instead, place it at an **image of the entrance aperture** of the system.

When the condenser forms an aperture image on the detector, the radiation from each point
in the field of view is spread across the full detector area — averaging out non-uniformity.
At a focal plane, one small spot concentrates all flux from one field point, hitting only
the local region around the optical axis.

**When to use it:**
- Designing the condenser/relay system that feeds any IR photoconductive cell
- Any scanning system where the target moves relative to the detector
- Whenever using a detector with known contact-lead geometry or non-uniform response

**Modern relevance:**
Still applicable to modern photoconductors and some photodiode configurations. The principle
(aperture image on detector = spatial averaging of responsivity) is not always taught in
optical design courses. Many systems inadvertently use a focal-plane detector and suffer
unexplained non-uniformity or scan-position-dependent sensitivity.

---


<!-- ================================================================ -->
<!-- CHAPTER 23 -- MICROSCOPE OPTICS -->
<!-- ================================================================ -->

### 23.1
**Title:** Maximum useful microscope magnification = 1000 × NA

**Source:** ch23, §23.2.2, page 23-2

**Category:** `rule-of-thumb`

**The Gem:**
The highest useful magnification of a compound microscope (in diameters) is approximately
**1000 times the numerical aperture** of the objective:

    MP_max ≈ 1000 × NA

Beyond this, magnification is "empty" — it enlarges the image without resolving more detail.
Lower magnifications (even down to 25×) are valid for larger specimens.

**When to use it:**
- Quickly checking whether a specified magnification is achievable with a given objective NA
- Specifying the maximum eyepiece power for a given objective
- Explaining to a system engineer why a high-magnification low-NA objective is useless

**Modern relevance:**
Still the standard quick-check rule. Any magnification beyond 1000 × NA wastes photons
and adds no information. Useful when selecting objective/eyepiece combinations for new
microscope configurations.

---

### 23.2
**Title:** Microscope resolution limit: d = λ / (NA_obj + NA_cond)

**Source:** ch23, §23.2.5.2, page 23-3

**Category:** `shortcut-formula`

**The Gem:**
The minimum resolvable separation between two points in a compound microscope is:

    d = λ / (NA_obj + NA_cond)

where λ is the wavelength of light, NA_obj is the numerical aperture of the objective,
and NA_cond is the numerical aperture of the substage condenser illuminating the specimen.

Special case — coherent illumination (NA_cond → 0):

    d = λ / NA_obj    (Rayleigh limit for coherent illumination)

Practical optimum: match NA_cond = NA_obj, giving:

    d = λ / (2 × NA)

**When to use it:**
- Sizing the objective NA needed to resolve a given feature size
- Estimating resolution for a given λ and NA combination
- Checking whether a condenser NA is matched to the objective (common mismatch error)

**Modern relevance:**
Fundamental formula unchanged. Still the first calculation in any microscope resolution
specification. The two-aperture form (obj + cond) is often forgotten in modern practice,
where only the objective NA is quoted.

**Accuracy / caveats:**
- Applies to incoherent (or partially coherent) illumination with matched condenser NA
- For coherent illumination, use d = λ / NA_obj (Rayleigh); for fully incoherent, d = 0.61λ / NA (Abbe)
- The formula as stated is the Abbe two-beam limit for matched illumination

---

### 23.3
**Title:** Kohler illumination required for photomicrography; critical illumination only for low-power visual work

**Source:** ch23, §23.3.2.2, page 23-5

**Category:** `design-heuristic`

**The Gem:**
Two illumination modes and when to use each:

| Mode | What it does | Use when |
|------|-------------|----------|
| **Critical illumination** | Images light source directly onto specimen | Low-power visual work only; fast to set up |
| **Kohler illumination** | Images condenser iris on specimen; images lamp filament on substage iris; produces uniform field | Photomicrography; any quantitative measurement; high-power work |

Critical illumination rule: an imperfect source (e.g., ground glass with granules) will print
its structure onto the image unless defocused — at which point uniformity improves but illuminance
drops. Only acceptable when the source is intrinsically very uniform (ribbon filament lamp).

Kohler illumination rule: **always use Kohler when the field must be uniformly illuminated.**
The substage iris adjusts the illuminating cone angle (contrast/resolution trade-off);
the lamp iris adjusts the illuminated field size.

**When to use it:**
- Setting up any microscope for photomicrography or measurement
- Diagnosing non-uniform illumination in an existing setup
- Choosing which illuminator design to specify for a new instrument

**Modern relevance:**
Kohler illumination is still the standard for any serious microscopy. The decision rule
(critical for rough visual, Kohler for everything else) prevents the common mistake of
trying to use critical illumination for documentation or analysis.

---

### 23.4
**Title:** Achromat objective construction recipe: element count scales with NA

**Source:** ch23, §23.3.4.3, page 23-8

**Category:** `reference-data`

**The Gem:**
Minimum optical construction for achromatic microscope objectives by NA:

| Focus (FL) | NA | Minimum construction |
|------------|-----|----------------------|
| 32–48 mm   | < 0.25 | 1 cemented doublet |
| 16 mm      | 0.25 | 2 cemented doublets |
| 8 mm       | 0.50 | Front + Middle + Back (no 2nd front) |
| 4 mm       | 0.66 | Front + 2nd Front + Middle + Back |
| 1.8 mm     | 1.25 | Front + 2nd Front + doublet Middle + doublet Back |

Front = hemispherical or hyper-hemispherical front element (the critical performance element).
2nd Front = meniscus element.
Middle and Back = cemented doublets.

Complexity increases with NA because: (1) the hemispherical front alone has large residual
aberrations that must be corrected downstream, and (2) the sine condition must be satisfied
for aplanatic imaging at high NA.

**When to use it:**
- Estimating design complexity (and cost) of a new objective at a given NA
- Sanity-checking a submitted design for adequate element count
- Quickly assessing whether an existing design can be adapted to a higher NA

**Modern relevance:**
While computer optimization now determines the final design, this recipe gives the correct
starting point complexity. Attempting to meet NA > 0.5 with fewer elements than listed is
a strong predictor of failure to converge.

---

### 23.5
**Title:** Huygenian vs Ramsden eyepiece selection: use Ramsden when a reticle is needed

**Source:** ch23, §23.3.5.2–23.3.5.3, pages 23-10 to 23-11

**Category:** `design-heuristic`

**The Gem:**
Aberration and use comparison of the two standard microscope eyepieces:

| Property | Huygenian (negative) | Ramsden (positive) |
|----------|---------------------|-------------------|
| Lateral color | Fully corrected | More than Huygenian |
| Longitudinal color | Large | ~½ of Huygenian |
| Spherical aberration | More | ~⅕ of Huygenian |
| Distortion (pincushion) | Larger | ~½ of Huygenian |
| Coma | Present | None |
| Eye relief | Short (problem at f < 1 in) | 50% greater than Huygenian |
| External reticle | No (focal plane inside system) | **Yes (focal plane outside system)** |

Decision rule:
- **Observation only** → Huygenian (best lateral color, most common)
- **Reticle or crosshair needed** → Ramsden (focal plane is accessible outside the lens)
- **Apochromatic objective** → use a compensating eyepiece (not either of the above)

**When to use it:**
- Selecting a standard eyepiece for a new or reconfigured microscope
- Specifying eyepiece type in a system procurement document
- Diagnosing why a reticle image appears colored or distorted (wrong eyepiece type)

**Modern relevance:**
The selection logic is unchanged. Ramsden eyepieces (and their derivatives) remain the
standard for measurement eyepieces with built-in scales. The compensating eyepiece is
standard for apochromats — this three-way choice must be made explicitly.

---

### 23.6
**Title:** Darkfield rule: objective NA must be less than the inner cone NA; use funnel stop above NA 0.7

**Source:** ch23, §23.4.2–23.4.3, pages 23-12 to 23-13

**Category:** `design-heuristic`

**The Gem:**
For darkfield microscopy, the illuminating condenser delivers a hollow cone of light to
the specimen. The objective must collect only the scattered/diffracted light, not the
direct beam. This requires:

    NA_objective < NA_inner (obscured central zone of condenser)

Standard practice:
- Hollow cone numerical apertures: **0.7 (inner) to 1.25 (outer)**
- Objectives with **NA > 0.7 must be equipped with a funnel stop** to reduce their
  effective NA below 0.7
- Lower NA_obj → less scattered light collected → lower image brightness; this limits
  the resolving power available in darkfield

For high-power darkfield:
- Use a **reflecting darkfield condenser** (paraboloid or cardioid type) — far better
  corrected for spherical and chromatic aberration than a refracting condenser with
  central stop
- Oil immersion between condenser and slide is required for high-NA work (prevents
  total internal reflection at the glass surface)

**When to use it:**
- Setting up darkfield illumination on any microscope
- Selecting objectives compatible with a given darkfield condenser
- Specifying a darkfield condenser for a new instrument

**Modern relevance:**
The NA constraint is fundamental and unchanged. The funnel stop requirement for objectives
above NA 0.7 is often overlooked when setting up darkfield illumination, causing a bright
central spot to ruin contrast.

---

### 23.7
**Title:** Phase vs interference microscopy choice: phase is qualitative; interference is quantitative

**Source:** ch23, §23.7.2.1, pages 23-20 to 23-21

**Category:** `design-heuristic`

**The Gem:**
Both phase and interference microscopes make transparent specimens visible, but they differ
in critical ways:

| Property | Phase microscopy | Interference microscopy |
|----------|-----------------|------------------------|
| Contrast mechanism | Direct + deviated beams recombined after phase plate | Two coherent beams; one through specimen, one reference |
| Haloes around features | **Yes** (unavoidable artifact) | **No** |
| Quantitative path measurement | No (shows path differences but not magnitude) | **Yes** — measures optical path length (OPL) |
| Refractive index measurement | No | Yes (if thickness known, or with known-medium immersion) |
| Color contrast | No | Yes (with white light) |
| Instrument complexity | Lower (adds annular diaphragm + phase plate to standard microscope) | Higher |
| Convert from brightfield | Yes (add phase condenser + phase objective) | No |

Key formula for interference measurement:
- If specimen thickness t is known: n = OPL/t
- If immersed in medium of known n_medium: both n and t can be solved simultaneously

**When to use it:**
- Choosing between phase and interference microscope for a new application
- Deciding when to invest in an interference microscope (quantitative measurement of transparent specimens)
- Explaining the halo artifact to users who mistake it for a real feature

**Modern relevance:**
Phase contrast remains the workday tool for cell biology; interference (DIC, quantitative phase imaging) is used wherever measurement is needed. The selection logic is the same as in 1962 — phase for visualization, interference for measurement.

---

### 23.8
**Title:** Fluorescence microscopy: use achromatic objectives and Abbe condensers, not apochromats

**Source:** ch23, §23.9.2.3, page 23-24

**Category:** `design-heuristic`

**The Gem:**
For fluorescence microscopy, **achromatic objectives and Abbe condensers are preferred** over
apochromatic (or other highly corrected) objectives and condensers.

Reason: highly corrected objectives often contain **fluorescent optical materials** (certain
types of glass or crystal used to achieve secondary chromatic correction) that produce their
own fluorescence background under ultraviolet illumination. This autofluorescence introduces
glare and reduces image contrast/visibility.

Additional note:
- An Abbe condenser at **NA 1.40 concentrates more energy on the specimen** than the
  standard NA 1.25 condenser — use the higher-NA Abbe condenser when excitation efficiency matters
- Use a **front-surface aluminized mirror** (more efficient than silvered mirror) for the
  lamp reflector

**When to use it:**
- Specifying or selecting objectives for a fluorescence microscope
- Diagnosing unexpected background glow in a fluorescence setup
- Choosing between achromat and apochromat when the application is fluorescence

**Modern relevance:**
Modern fluorescence objectives are explicitly specified as "fluorite-free" or tested for
autofluorescence. The principle remains the same: highly corrected optics that use
fluorescent materials are counterproductive in fluorescence microscopy. This is a non-obvious
selection constraint that the 1962 text captured correctly.

---


<!-- ================================================================ -->
<!-- CHAPTER 24 -- DESIGN PHASE OPTICAL TESTS -->
<!-- ================================================================ -->

### 24.1
**Title:** Seidel aberration tolerances from the Rayleigh λ/4 criterion

**Source:** ch24, §24.2.3, page 24-3

**Category:** `shortcut-formula`

**The Gem:**
The Rayleigh criterion (max path deviation ≤ λ/4 for a "good" image) translates into
specific tolerances on each Seidel aberration. Here N' is the refractive index in image
space, U'_m is the marginal ray angle in image space, and λ is the wavelength:

| Aberration | Tolerance formula |
|------------|------------------|
| Primary marginal spherical (LA') | LA' ≤ 4λ / (N' sin²U'_m) |
| Primary zonal spherical (LZA', with LA'=0) | LZA' ≤ 6λ / (N' sin²U'_m) |
| Primary coma (Coma_s) | Coma_s ≤ ±λ / (2N' sin U'_m) |
| Focal range (depth of focus) | Δf = λ / (N' sin²U'_m) |
| Astigmatism (Ast's) | Ast's ≤ λ / (4N' sin²U'_m) |
| Curvature of field (X') | X' ≤ focal range = λ / (N' sin²U'_m) |

For a system in air (N' = 1), sin U'_m ≈ 1/(2 × f/#):
- Focal range ≈ 4λ(f/#)²   *(corrected 2026-09-12, see validation note below)*

**When to use it:**
- Setting a pass/fail threshold on calculated Seidel aberrations during lens design
- Estimating the depth of focus for any lens without full wave optics
- Quick check on whether a residual aberration will visibly degrade image quality

**Modern relevance:**
These are still the standard first-pass aberration tolerances used in lens design. The
focal range formula (depth of focus = 4λ(f/#)²) appears in every imaging textbook.
Knowing the individual Seidel formulas allows rapid tolerance assignment before
setting up a full optimization run.

**Accuracy / caveats:**
- Assumptions: focal range ≪ focal length; field angle small enough that sin²(U'_m) ≈ ¼ sin²(U'_m) is not needed
- These are λ/4 wave criteria — they represent a theoretical standard that may be too tight or too loose in practice (see 24.2)
- For N' = 1 (air): sin U'_m = NA = 1/(2 × f/#) for object at infinity
- **Validation note (2026-09-12, resolved against scan p.24-3):** the handbook itself
  prints two inconsistent forms of "focal range" — Eq.(4) uses sinU'_m (first power),
  while Eq.(6) restates the identical quantity with sin²U_m. Eq.(6)'s form is the one
  consistent with Eqs.(1)/(2)/(5) and with the standard optics result that depth of
  focus scales as 1/NA² (see gem 16.7); it's almost certainly a dropped exponent in the
  original 1962 typesetting of Eq.(4). Using Eq.(6)'s form gives 4λ(f/#)², not the 8λ(f/#)²
  previously stated here — corrected. See `analysis/EDITORIAL_NOTES.md` chapter 24 entry.
- **Re-confirmed 2026-09-13** via the ch24 deep LaTeX pass (commit e5bbdb0): all six
  Seidel tolerance equations transcribed directly from the scan; the Eq.(4)/Eq.(6)
  sin vs. sin² discrepancy is preserved exactly as printed in the 1962 source
  (`ocr_output/ch24.md`, tags 4 and 6) — the editorial correction above stands.

---

### 24.2
**Title:** Seidel tolerance calibration: spherical too loose for fast systems; coma must reach zero; astigmatism tolerance is 2× too tight

**Source:** ch24, §24.2.4, page 24-3

**Category:** `design-heuristic`

**The Gem:**
The Rayleigh λ/4 Seidel tolerances (24.1) require correction factors in practice:

| Aberration | Tolerance behavior | Practical guidance |
|------------|-------------------|-------------------|
| Spherical aberration | **Too loose** for fast systems (f/# ≲ 5) — by factor of **4 or more** | Tighten tolerance for fast lenses; microwave antenna designers (electrically fast apertures) found this empirically |
| Coma | **Too loose** for visual systems | Reduce coma sensibly to **zero** — do not accept the full λ/4 allowance |
| Astigmatism | **Too tight** | Exceeding the astigmatic tolerance by a factor of **2× still gives good results** in most systems |

Summary: when designing to the Seidel tolerances, apply these correction factors:
- Fast systems: demand spherical aberration ≤ ¼ of the λ/4 tolerance
- All visual systems: target coma → 0, not coma → λ/(2NA)
- Astigmatism: the computed tolerance can be relaxed by up to 2× without visible penalty

**When to use it:**
- Reviewing a lens design that nominally passes the λ/4 Seidel checks but may still perform poorly
- Setting optimization targets in a lens design program
- Allocating aberration budgets across elements (tighten spherical and coma, relax astigmatism)

**Modern relevance:**
These calibration factors are rarely stated explicitly in modern lens design texts, which tend to
present the λ/4 rule as absolute. Knowing that coma must be driven to zero (not just within
tolerance) and that astigmatism tolerance is conservative can save significant optimization
time by pointing the designer toward the right targets.

---

### 24.3
**Title:** Spot diagram is only valid for aberration-limited systems — compare to Airy disk before trusting it

**Source:** ch24, §24.3.3, page 24-4

**Category:** `sanity-check`

**The Gem:**
A spot diagram (geometric ray intercept plot) is a geometrical optics tool. It is only
meaningful when the system is **aberration-limited** — i.e., the aberrations are large
compared to the diffraction limit.

Decision rule:
- If the **spot diagram diameter ≥ Airy disk diameter**: aberration-limited → spot diagram valid
- If the **spot diagram diameter ≤ Airy disk diameter**: diffraction-limited → spot diagram misleading; use wave optics (OPD / Strehl / PSF)

Reference data point (NBS 6" f/3.5 aerial camera lens):
- Airy disk diameter: **4.0 µm** (= 2.44λ f/# = 2.44 × 0.55 µm × 3.5 ≈ 4.7 µm; the 4.0 µm value is at the operating wavelength used)
- 80% encircled energy spot diameter: **3.93 µm** (from spot diagram)
- Agreement confirms the lens is near-diffraction-limited and the spot diagram still correctly predicts the diffraction PSF in this case

**When to use it:**
- Deciding whether to run a wave optics (OPD / Strehl) analysis or whether the spot diagram is sufficient
- Checking whether an "improved" design is actually better or just has a smaller spot that still exceeds the Airy disk
- Flagging high-precision aspheric designs where all aberrations have been removed except color — here spot diagrams give only a rough first approximation

**Modern relevance:**
Many lens designers reflexively look at RMS spot radius without checking whether they are
aberration- or diffraction-limited. The Airy disk comparison is a 5-second check that prevents
misinterpretation of spot data in near-diffraction-limited systems.

**Accuracy / caveats:**
- Airy disk diameter = 2.44 λ (f/#) for a circular unobscured aperture
- The threshold is a guideline; systems within a factor of 2 of the Airy disk are in a
  mixed regime where both spot and wave optics analyses are useful

---


<!-- ================================================================ -->
<!-- CHAPTER 25 -- PRODUCTION PHASE OPTICAL TESTS -->
<!-- ================================================================ -->

### 25.1
**Title:** Always specify the exact reference point for focal length — ambiguity causes assembly failure

**Source:** ch25, §25.2.1, page 25-1

**Category:** `design-heuristic`

**The Gem:**
Focal length is meaningless without an unambiguous statement of the point from which it
is measured. Two documented real-world failures from this ambiguity:

1. **Aerial camera lens**: designer measured focal length from the secondary principal point;
   machinist measured from the rear lens surface. Both lens and camera body were fabricated
   on these different bases simultaneously. The principal point lay several inches inside the
   lens — result: completely blurred image, system had to be scrapped.

2. **Missile-tracking system**: optical designer measured focal point from the front surface;
   machinists assumed it was measured from the rear surface of a thick mirror. The 1-inch
   central thickness of the mirror caused major performance failure when assembled.

Required specifications (always state all of these explicitly):
- **Effective focal length (EFL)** — measured from the second principal point
- **Back focal length (BFL)** — measured from the rear vertex of the last surface
- **Front focal length (FFL)** — measured from the front vertex
- **Reference surface** — which surface the machinist should measure from

**When to use it:**
- Writing any optical specification or drawing
- Handing off a design from optical designer to mechanical engineer
- Receiving a lens prescription and checking that all three focal length conventions are stated

**Modern relevance:**
This ambiguity still causes failures. CAD models place lens reference datums differently
from optical design software. Any time a focal length value crosses an organizational
boundary (designer → machinist, OEM → integrator), verify which reference is intended.

---

### 25.2
**Title:** Newton's fringes 7-rule interpretation guide for optical shop testing

**Source:** ch25, §25.8.1.2, page 25-9

**Category:** `reference-data`

**The Gem:**
When two surfaces (test surface S₁ and reference flat S₂) are placed in close contact and
illuminated with nearly monochromatic light, the resulting Fizeau/Newton's fringes follow
these rules:

| Rule | Statement |
|------|-----------|
| (a) Contrast | Fringes have best contrast when both surfaces have similar reflectance; focus on the air film between surfaces |
| (b) Viewing angle | Fringe position is nearly independent of viewing angle when the air gap is small; view approximately normal to the surfaces |
| (c) **Contour lines** | **Each fringe marks the locus of points where the air gap d is a particular constant** (fringes = contour map of the surface error) |
| (d) **Pressure test** | **Pressing on a convex area causes its surrounding fringes to move outward** (gap d stays constant); use this to identify high and low areas |
| (e) Adjacent fringe spacing | Passing from one fringe to the next (same bright or dark), the gap d changes by **λ/2** |
| (f) Bright-to-dark spacing | Passing from bright to adjacent dark fringe, the gap changes by **λ/4** |
| (g) Dark fringe condition | Dark fringes at d = νλ/2 (ν = 0, 1, 2, …); bright at d = μλ/4 (μ = 1, 3, 5, …) for non-absorbing glass surfaces |

Rules (c) and (d) are most important to the optical worker — they enable interpretation
of which areas are high and which are low.

**When to use it:**
- Interpreting Newton's fringes in any contact flat-testing setup
- Identifying convex vs concave surface errors during optical polishing
- Setting up and reading any Fizeau interferometer

**Modern relevance:**
Newton's fringe testing remains the standard method in optical shops for surface flatness
and radius matching. These 7 rules are the complete interpretation guide — mastering them
eliminates confusion about fringe direction, fringe spacing, and what pressure tests reveal.

**✓ Confirmed 2026-09-13 via deep pass:** rule (g)'s dark/bright fringe conditions are
transcribed directly from the scan as Eqs. (3)–(6) of ch25 (`ocr_output/ch25.md`),
including the plate-immersion form with refractive index n (nd = νλ/2, nd = μλ/4) —
exact equation-level match, both the plain-air-gap and immersed-plate cases.

---

### 25.3
**Title:** Interferometric flatness specification: Newton fringes per unit length; "uniform color" for highest grade

**Source:** ch25, §25.8.1.3–25.8.1.5, pages 25-10 to 25-11

**Category:** `reference-data`

**The Gem:**
Three levels of flatness specification using Newton's fringes:

**Standard grade — Newton fringes per inch:**
Specify maximum number of Newton's fringes visible per inch (or per specified dimension)
over the tested surface. Each fringe represents a height change of λ/2 in the air gap.

**High grade — fringe straightness:**
For high-quality optical flats, specify that "fringe shift from straightness shall not exceed
h/N over a stated diameter", where h = fringe width (spacing) and N is the tolerance factor.
- Fringe shift ≤ h/5: clearly detectable and measurable limit
- Fringe shift ≤ h/10: difficult to detect — practical lower limit for this technique

**Highest grade — "uniform color":**
When the two surfaces are brought so nearly parallel that a single broad fringe spreads
over the entire surface, specify that "the surface shall be polished to a uniform color"
(same color = same air gap everywhere = flat to within a fraction of a fringe).
This is the highest achievable standard in contact interferometry.

For spherical surfaces: replace the reference flat with a test glass having the desired radius.
At the match radius, a single fringe of uniform color specifies the surface as essentially a
perfect sphere matching the test glass.

**When to use it:**
- Writing or interpreting flatness/sphericity tolerances on optical drawings
- Specifying acceptance criteria for polished optical surfaces
- Choosing the appropriate test method (contact flat vs. interferoscope) for a given tolerance

**Modern relevance:**
"N fringes per inch" and "uniform color" remain standard optical shop specification language.
Knowing the sensitivity limit (h/10 per fringe) helps set realistic tolerances — specs tighter
than h/10 cannot be verified with this method and require interferoscope or phase-shifting
interferometry.

---

### 25.4
**Title:** Foucault test sensitivity: 10⁻⁵ rad slope errors visible; 10⁻⁶ rad detectable on long mirrors

**Source:** ch25, §25.10.1.4, page 25-25

**Category:** `sanity-check`

**The Gem:**
The Foucault knife-edge test is extraordinarily sensitive to surface slope errors. A slope
angle error θ on a mirror surface produces a lateral displacement of the focal spot of:

    Δx = R × 2θ

where R is the radius of curvature of the surface (= 2f for a mirror).

Sensitivity benchmarks:
- **10⁻⁵ radians (about 2 arc-seconds)**: barely detectable on a surface with small radius of curvature, clearly visible on larger systems
- **10⁻⁶ radians**: easily seen on long focal length mirrors (e.g., large telescope primaries) — this is about 0.21 arc-seconds

Requirements: only a pinhole, a knife edge, the optic, and the observer's eye. No additional optics needed.

The Foucault test inspects zonal contributions individually rather than their integrated sum,
making it more diagnostic than the star test for locating specific surface errors.

**When to use it:**
- Evaluating any mirror surface during or after fabrication
- Choosing whether Foucault or star test is more appropriate (Foucault = zonal detail; star = integrated performance)
- Setting expectations for what slope errors are detectable before polishing is complete

**Modern relevance:**
Foucault testing remains the standard shop test for large mirrors (telescopes, laser optics).
The 10⁻⁶ rad sensitivity — achievable with no instrumentation beyond a pinhole and a razor blade — makes it one of the most sensitive optical tests ever devised per unit of equipment cost.

**Accuracy / caveats:**
- The simple geometric interpretation breaks down near the diffraction limit — quantitative Foucault analysis requires Linfoot's wave-optics treatment
- Low-reflectance surfaces are difficult to test (use a slit instead of a pinhole for more light)
- Edge of a circular mirror shows a bright ring even in a perfect mirror (Rayleigh/Linfoot effect) — do not interpret as a zonal error
- The chapter's own worked example (§25.10.1.4: R = "ten", θ = 10⁻⁵ rad ⇒ deflection "10⁻⁴ inches or .025 mm")
  is internally inconsistent by roughly a factor of 10 (10⁻⁴ in ≈ 0.00254 mm, not 0.025 mm) — printed as-is in
  the source; the Δx = R×2θ formula itself is unaffected

**✓ Confirmed 2026-09-13 via deep pass:** the Δx = R×2θ geometry is confirmed by the
Figure 25.24 caption transcribed from the scan (page 25), which explicitly labels the
deflected focal point at angle 2θ from the correct focus; Linfoot's wave-optics
illumination integral for the diffraction-limited edge case is transcribed as Eq. (11)
of ch25 (`ocr_output/ch25.md`), confirming the caveat above is the same Linfoot treatment
the source itself uses.

**✓ Re-verified 2026-09-13 via independent validation:** the scan confirms "10⁻⁶ radians"
(not 10⁻⁷ as an earlier transcription pass mis-recorded); corrected here and in
`ocr_output/ch25.md` §25.10.1.4.

---

### 25.5
**Title:** Star test zonal interpretation rule: bright ring inside focus = short focus (positive); outside = long (negative)

**Source:** ch25, §25.11.6.4, page 25-34

**Category:** `design-heuristic`

**The Gem:**
For the star test (a star or artificial star viewed through the lens or telescope under test),
the key interpretation rules for spherical aberration zones are:

**Rule:**
- Bright ring or zone seen **inside focus** → that zone focuses **shorter** than paraxial (positive zonal spherical)
- Bright ring or zone seen **outside focus** → that zone focuses **longer** than paraxial (negative zonal spherical)

**Technique:**
- Examine the image **out of focus**, not at focus — out-of-focus inspection is more sensitive
- Move far enough from focus that **several rings are visible** — this gives maximum sensitivity and the clearest aberration signature
- For a perfect lens, the image expands **concentrically and uniformly** through focus; any departure from this symmetry indicates aberration
- Marginal spherical: bright ring near center inside focus (edge rays focus shorter); opposite outside
- Zonal spherical: bright ring in intermediate zone position inside/outside focus

**Diagnosis shortcuts (from Taylor's classic photographs):**
- Uniform concentric expansion through focus → perfect lens
- Non-concentric expansion → misalignment (squaring-on error)
- Focus into two lines at right angles → astigmatism
- Bright concentrated center inside focus, diffuse outside → positive marginal spherical
- Isolated bright ring inside focus → zonal spherical

**When to use it:**
- Diagnosing aberrations in a telescope objective or camera lens at the optical bench
- Distinguishing marginal vs zonal spherical aberration during lens adjustment
- Verifying correct assembly after squaring-on

**Modern relevance:**
Star testing with an artificial star remains a standard quick aberration diagnostic — the
only instrument needed is a high-power eyepiece. The in-focus/out-of-focus asymmetry
comparison is faster and more informative than any single in-focus image.

---

### 25.6
**Title:** Coma causes asymmetric boresight error; astigmatism does not — critical distinction for targeting systems

**Source:** ch25, §25.4.1, page 25-4

**Category:** `design-heuristic`

**The Gem:**
For optical systems used in pointing, tracking, or targeting, **coma is uniquely dangerous**
because it degrades the image **asymmetrically** relative to the principal ray.

| Aberration | Image degradation | Effect on pointing/boresight |
|------------|------------------|------------------------------|
| Spherical | Symmetric around axis | No boresight error (can center symmetric blur) |
| Astigmatism | Symmetric (two focal lines equidistant from principal ray) | No boresight error (can center disk of least confusion) |
| Coma | **Asymmetric** — characteristic comet-shaped flare | **Causes systematic boresight error** — the centroid of the image is displaced from the true target direction |
| Distortion | Position error, field-dependent | Systematic pointing error across the field |

Practical rule: for any system where pointing accuracy matters (rangefinders, fire control,
missile guidance, astronomical astrometry), **coma must be reduced essentially to zero** —
the coma tolerance from the λ/4 Rayleigh criterion (24.1) is too loose for these
applications (see also 24.2).

**When to use it:**
- Prioritizing which aberrations to control in a tracking or targeting optical system
- Reviewing a lens design where coma remains within the λ/4 tolerance but the system is used for pointing
- Writing aberration specifications for fire control or guidance optics

**Modern relevance:**
This distinction is still critical and still sometimes overlooked. Systems specified by
"resolution" (which tolerates symmetric aberrations) may still have unacceptable pointing
accuracy if coma is present. The asymmetric flare is particularly insidious because it
changes with temperature and focus shift.

---

### 25.7
**Title:** Spherometer radius of curvature from sagitta: r = d²/(6s) + s/2

**Source:** ch25, §25.7.2.2, page 25-7 (Eq. 2)

**Category:** `shortcut-formula`

**The Gem:**
A spherometer (three fixed legs + a central micrometer spindle) measures the sagitta s of
a spherical surface across a known leg span (average distance between legs, d). The radius
of curvature follows directly, with no ray tracing or iterative solving:

    r = d²/(6s) + s/2

The spindle is zeroed on a flat reference, then the surface is measured; s is the difference.
The same instrument and formula work for both convex and concave surfaces (reverse the sign
of s appropriately, per the source procedure).

**When to use it:**
- Measuring the radius of any spherical surface 1–3 inches in diameter during fabrication
- Quick shop-floor radius check without a bench autocollimator or interferometer setup
- Cross-checking a computed radius against a physical measurement before final polish

**Modern relevance:**
Mechanical spherometers (and their digital equivalents) are still standard optical-shop
equipment; this sagitta-to-radius formula is the same one built into modern digital
spherometer firmware. A useful hand-check when only calipers and a micrometer are available.

**Accuracy / caveats:**
- s ≪ d is assumed (small-sagitta approximation is exact for a true sphere, not approximate)
- For surfaces under ~1 inch diameter, the source notes a Foucault or autocollimation
  method (§25.7.2.3) is preferred over a mechanical spherometer

---

### 25.8
**Title:** Distortion from a nodal slide without a distortion-free reference lens: D_β = (R−L)/2 · sec β

**Source:** ch25, §25.6.3, page 25-6 (Eq. 1)

**Category:** `shortcut-formula`

**The Gem:**
Distortion is normally measured against a known distortion-free collimator/grid, which is
often unavailable. Washer, Tayman, and Darling's nodal-slide method measures distortion
using only the lens under test, a microscope, and a nodal slide — no reference optic needed:

1. Find focus on-axis; confirm the no-parallax (nodal) point by rotation.
2. Rotate the lens by +β, refocus longitudinally, and note the microscope's lateral
   re-centering reading, **R**.
3. Rotate the lens by −β, repeat, and note the reading **L**.
4. Distortion at angle β is:

    D_β = (R − L)/2 · sec β

**When to use it:**
- Measuring distortion in the shop when no distortion-free autocollimator/grid target exists
- Any lens already mounted on a nodal slide for focal-length or principal-point work — this
  measurement is essentially free once the slide is set up
- Spot-checking a computed distortion curve against a physical measurement at one field angle

**Modern relevance:**
The nodal-slide bench is largely superseded by MTF/distortion benches with digital imaging,
but the underlying trick — use the lens's own on-axis image as its own reference by
symmetric ± rotation — remains a useful self-calibrating technique when no external
reference standard is trusted or available.

**⚠ Query 2026-09-13 (unresolved, source ambiguity):** as printed, D_β is dimensionally a
linear focal-plane displacement (an image-height error in the units of R and L), not the
conventional dimensionless fractional distortion (y′ − f·tan β)/(f·tan β); the fractional
form would be D = (R−L)/(2f·sin β). The chapter never defines the normalization and the
scan gives no further detail, so if this gem is used for quantitative distortion values,
state the units explicitly (linear mm in the focal plane) or use the fractional form above.
See `ocr_output/ch25.md` §25.6.3 (Eq. 1) editorial note.

---


<!-- ================================================================ -->
<!-- CHAPTER 26 -- EVALUATION PHASE OPTICAL TESTS -->
<!-- ================================================================ -->

### 26.1
**Title:** Cascaded system resolution: 1/Re² = 1/R₁² + 1/R₂² + ...

**Source:** ch26, §26.1.2.6, page 26-4

**Category:** `shortcut-formula`

**The Gem:**
When multiple optical subsystems are used in series (e.g., objective + film, or camera +
atmosphere + display), the overall resolving power Re is related to the individual resolving
powers R₁, R₂, R₃, ... by:

    1/Re² = 1/R₁² + 1/R₂² + 1/R₃² + ...

This is directly analogous to the effective bandwidth of cascaded electrical amplifiers or
the effective rise-time of a chain of amplifiers — the formula is the same.

Example: an objective resolving 100 lines/mm paired with film resolving 50 lines/mm:
    1/Re² = 1/100² + 1/50² = 0.0001 + 0.0004 = 0.0005
    Re = 1/√0.0005 ≈ 45 lines/mm

The weakest component dominates — combining a 100 lp/mm lens with 50 lp/mm film gives
only 45 lp/mm, not the 50 one might naively expect.

**When to use it:**
- Quick system-level resolution budget calculation
- Deciding whether upgrading one component (lens vs film/detector) is worth it
- Checking whether the eye is limiting a visual system (compare eye resolution vs system output)

**Modern relevance:**
Used in any imaging system trade study. The formula shows diminishing returns: if the
detector already limits to 50 lp/mm, a better-than-100 lp/mm lens provides minimal benefit.
Applicable to any cascaded imaging chain (optical + sensor + display).

**Accuracy / caveats:**
- Approximate — assumes Gaussian-shaped spread functions; gives good estimates for
  planning purposes but not precise prediction when aberrations dominate
- Applies to incoherent imaging; coherent systems require wave-optics analysis

**✓ Confirmed 2026-09-13 via deep pass:** transcribed directly from the scan as Eq. (1)
of ch26 (`ocr_output/ch26.md`), 1/Re = √(1/R₁² + 1/R₂² + 1/R₃² + ...) — the equivalent
square-root form of the relation stated above.

---

### 26.2
**Title:** Visual system test rule: chart lines must subtend >60 arc-seconds at the eye

**Source:** ch26, §26.1.2.5, page 26-4

**Category:** `design-heuristic`

**The Gem:**
When testing the resolving power of a visual optical instrument (binoculars, telescopes,
periscopes), the test chart must be set up so that the lines are visible to the observer —
not so fine that the eye itself becomes the limiting element.

The human eye resolves approximately **60 arc-seconds** (1 arc-minute) per line pair under
good conditions. For the optical system to be the limiting factor (not the eye):

    chart_resolution × magnification > 60 arc-seconds per line

Equivalently: the angular size of one resolved line, as seen through the eyepiece, must
exceed 60 arc-seconds.

Practical setup check:
- If chart is at distance D and has N lines/mm, the angular subtense of one line is
  1/(N × D) radians = 206265/(N × D) arc-seconds
- Multiply by magnification M; this must exceed 60 arc-seconds

The NBS standard distance of **26 focal lengths** for photographic lens testing (§26.1.2.1)
minimizes the effect of spherical aberration on the measured resolving power.

**When to use it:**
- Setting up a resolving power test for any visual optical instrument
- Selecting the appropriate chart-to-instrument distance
- Interpreting a visual resolving power result (if result equals eye resolution ÷ magnification, the test was eye-limited)

**Modern relevance:**
Still directly applicable. Any visual instrument test that does not satisfy this condition
is measuring the observer's eye rather than the optic. The 60 arc-second threshold is
conservative; dark-adapted or fatigued observers may have limits of 90–120 arc-seconds.

---

### 26.3
**Title:** High-contrast test targets: accurate measurement; low-contrast: realistic field performance — match target to use case

**Source:** ch26, §26.1.2.3, pages 26-3 to 26-4

**Category:** `design-heuristic`

**The Gem:**
Resolving power tests with high-contrast and low-contrast targets give systematically
different results, and each has a specific role:

| Target type | Resolving power result | Best use |
|-------------|----------------------|----------|
| **High contrast** (e.g., black on white, value ~1.4 as printed — likely density/log-contrast, not a reflectance ratio; see note below) | Higher lines/mm reading | Comparative lens grading; acceptance testing; higher measurement accuracy due to steeper response curve (see Figure 26.5) |
| **Low contrast** (e.g., black on grey, ratio ~0.20) | Lower lines/mm reading | Predicting real-world performance; aerial reconnaissance targets are typically low-contrast on most flying days |

Key practical rule: **test the lens on the contrast that matches its intended use.**
A lens that passes a high-contrast test may fail in the field if the application involves
low-contrast targets (overcast day, haze, low-reflectivity terrain).

The high-contrast result is a more sensitive measurement instrument (steeper
contrast-vs-frequency curve → smaller uncertainty in the resolvability threshold).
But for acceptance to a resolution requirement, the contrast should match the
specification's assumed target contrast.

**When to use it:**
- Specifying acceptance tests: state the contrast ratio along with the lines/mm requirement
- Comparing lenses tested at different laboratories (check whether the same contrast was used)
- Diagnosing why a lens that passed lab tests underperforms in the field

**Modern relevance:**
MTF (modulation transfer function) testing at a specific modulation level is the modern
equivalent of this distinction. The principle is the same: a high-modulation test is
more sensitive; a low-modulation test predicts real-world performance. Always specify modulation.

**Note on the "1.4" figure (2026-09-13):** ch26 §26.1.2.1 prints the high-contrast value as
1.4, which cannot be a bounded (≤1) reflectance contrast ratio; it is almost certainly a
density/log-contrast figure (consistent with Figure 26.5's 0–1.5 contrast axis). State the
convention explicitly if this number is quoted downstream.

---

### 26.4
**Title:** Square wave targets can replace sine wave targets for MTF — easier to make; Coltman's formula converts

**Source:** ch26, §26.4.1.1, pages 26-20 to 26-21

**Category:** `shortcut-formula`

**The Gem:**
Sine wave targets (pure sinusoidal intensity variation) are the theoretically ideal input
for measuring the optical transfer function (OTF / MTF), but they are difficult to
fabricate to high accuracy. Square wave targets (alternating sharp black and white bars)
are much easier to produce precisely.

The square wave response r(n) at spatial frequency n can be measured directly, and the
sine wave response (MTF) R(n) can be derived from it using the Coltman formula:

    r(n) = (4/π) [ R(n) - R(3n)/3 + R(5n)/5 - R(7n)/7 + ... ]

Inverting (solving for R(n)):

    R(n) = (π/4) [ r(n) + r(3n)/3 - r(5n)/5 + r(7n)/7 - ... ]

In practice, only the first two or three terms matter because R(n) drops rapidly with frequency.

A single square wave target of spatial frequency n₀, combined with a high-quality
minifying or magnifying auxiliary optic, can cover a wide spatial frequency range by
looking at harmonics 3n₀, 5n₀, 7n₀ in the electrical spectrum.

**When to use it:**
- Building a simple MTF test bench without access to precision sine wave target fabrication
- Routine production testing where square wave bar charts (1951 USAF target) are already in use
- Deriving true MTF from a measured square wave response curve

**Modern relevance:**
Square wave (bar chart) targets are still the most common test targets in optical labs.
Modern image quality software (such as slant-edge MTF methods) extends this approach further,
but Coltman's formula remains valid and is used in any system where a bar chart is
measured and the true MTF is needed. The key insight — square wave is sufficient,
you can compute MTF from it — eliminated the need for precision sinusoidal targets.

**Accuracy / caveats:**
- The series converges quickly for well-corrected systems (R drops fast with frequency)
- Phase information is lost; the formula gives modulus of OTF only (MTF), not the full complex OTF
- If the system is nonlinear (e.g., photographic film), the analysis requires modification

**✓ Confirmed 2026-09-13 via deep pass:** both directions of Coltman's series are
transcribed directly from the scan as Eqs. (11)–(12) of ch26 (`ocr_output/ch26.md`),
using the same r(n)/R(n) notation as this gem; the underlying square-wave Fourier
expansion and the r(n)/R(n) ratio definitions are Eqs. (8)–(10) of the same chapter.

**✓ Verified 2026-09-13 via independent re-validation:** the four printed leading terms
of the inverse series (Eq. 12) are exact. Do not extend the "..." with a naive alternating
continuation: exact re-derivation gives R(n) = (π/4)[r(n) + r(3n)/3 − r(5n)/5 + r(7n)/7 +
0·r(9n)/9 + r(11n)/11 − r(13n)/13 − r(15n)/15 − r(17n)/17 + …] — the r(9n) coefficient is
exactly zero (3n×3n cross-term cancellation), and r(13n)–r(17n) are all negative. The book's
own ellipsis is safe as printed and matches this; the caution applies only if this gem is
extended past the fourth term.

---

### 26.5
**Title:** KDC visual efficiency: benchmark any instrument against the unaided eye in one number

**Source:** ch26, §26.1.4, pages 26-8 to 26-10 (Eqs. 2–3)

**Category:** `shortcut-formula`

**The Gem:**
The K.D.C. ("Kinetic Definition Chart" apparatus, §26.1.4.1–26.1.4.2 — "kinetic" from the
motorization of some of its parts, per the source) efficiency
metric reduces a visual instrument's net usefulness to a single number by comparing what
the eye alone can just detect/resolve to what the eye-plus-instrument combination achieves,
normalized by magnification:

    KDC efficiency = (α_e / (α_i · M_i)) × 100

equivalently, in terms of measured threshold sizes:

    KDC efficiency = (X_i / (M_i · X_e)) × 100

where α_e (or X_e) is the naked-eye threshold, α_i (or X_i) is the threshold through the
instrument, and M_i is the instrument's magnification. A perfect, lossless instrument that
only magnifies scores 100%; any real instrument (transmission loss, aberration, veiling
glare, exit pupil mismatch to the eye) scores lower.

**When to use it:**
- Comparing two visual instruments (binoculars, periscopes, sights) on a single figure of
  merit that already accounts for magnification, rather than comparing raw resolution
- Quick acceptance-test number for a visual instrument production run
- Diagnosing whether a design's magnification is being "wasted" by other losses

**Modern relevance:**
The same idea — normalize measured performance against both the unaided human observer
and the nominal (lossless) instrument gain — still underlies modern visual-system
figures of merit (e.g., visual MTF-based "quality factor" metrics). A single percentage
is easier to specify and inspect against than a raw resolution or MTF curve.

**Accuracy / caveats:**
- Only meaningful for visual instruments where the eye is part of the system under test —
  not applicable to photographic or electronic sensor evaluation
- Depends on the specific target/threshold convention used to establish α_e and X_e; compare
  KDC figures only when measured under the same test conditions

---
