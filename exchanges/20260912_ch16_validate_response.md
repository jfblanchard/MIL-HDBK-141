# Validation Response — Chapter 16: Applications of Physical Optics

**Date:** 2026-09-12
**Validator:** Claude (Sonnet 5), self-validated per `exchanges/VALIDATOR_SYSTEM_PROMPT.md`

---

### 16.1 — λ/2 per fringe + Newton's rings
**STATUS: PASS**
Standard Fizeau result: fringe = constant-gap locus, adjacent fringes differ by λ/2 air gap at normal incidence. Newton's-rings dark-ring formula $r_v=\sqrt{v\lambda R}$ correctly incorporates the π phase shift from the flat's reflection (dark center at contact point, v=0), matching the standard textbook result.

### 16.2 — Dielectric plate OPD and phase-flip bookkeeping
**STATUS: PASS**
$\delta=2nd\cos i'$ is the standard two-surface plate OPD. Checked the phase algebra: total phase $= (4\pi/\lambda)nd\cos i' + \pi$ gives destructive interference at $2nd=v\lambda$ and constructive at $2nd=(v+\tfrac12)\lambda$ — verified by direct substitution, consistent.

### 16.3 — Phase change on reflection
**STATUS: PASS**
Standard Fresnel-reflection phase convention (π reflecting off higher index, 0 off lower index, 0 in transmission). Correctly explains the dark central Newton's ring / dark center of a soap film.

### 16.4 — Haidinger blink counting
**STATUS: PASS**
Standard shop technique; Δd = Nλ/(2n) follows directly from the λ/2-per-fringe rule (16.1) applied to a moving plate. Physically sound, no computation issues.

### 16.5 — Fringe-shift thickness measurement
**STATUS: PASS**
Standard multiple-beam/Tolansky-type step-height formula; t=(Δx/h)(λ/2) is dimensionally and physically consistent with 16.1's λ/2-per-fringe basis.

### 16.6 — Rayleigh/Sparrow resolution
**STATUS: PASS (Rayleigh/Dawes-type terms), QUERY (exact Sparrow coefficient)**
$r_0=0.61\lambda/NA$ and $\theta_0=1.22\lambda/D$ are the standard Rayleigh criteria — correct. The qualitative Sparrow-limit claim (more permissive than Rayleigh, defined by zero dip in combined intensity rather than the Rayleigh "first minimum on peak" convention) is correct and well known. I can't independently confirm the specific "0.78 Airy units / 0.47λ/NA" coefficient to high precision from memory — different references give the Sparrow/Rayleigh ratio in the range of roughly 0.8–0.95 depending on aperture shape and exact definition. Recommend spot-checking this specific numeric factor against a primary source (e.g. Born & Wolf, or den Dekker & van den Bos 1997) before treating it as exact; the qualitative point stands regardless.

### 16.7 — Diffraction depth of focus, NA⁻² scaling
**STATUS: PASS**
$z\le\lambda/(2\,NA^2)$ is the standard Rayleigh quarter-wave depth-of-focus criterion; the NA⁻² (not NA⁻¹) scaling is correctly distinguished from the geometric-optics result and matches lithography/microscopy convention (DOF = $k_2\lambda/NA^2$). Worked numeric example (NA 0.1 → 27.5 µm; NA 0.3 → 3.1 µm, a 9× reduction for 3× NA) checks out arithmetically: $0.55/(2\times0.01)=27.5$; $0.55/(2\times0.09)=3.06$ ✓.

---

## LaTeX transcription priority note

None of ch16's equations have LaTeX yet (all still `[EQUATION N: ...]` placeholders). If/when a LaTeX pass is scheduled, priority should go to the equations directly underlying gems 16.1–16.2 (interference/OPD, §16.2 and §16.9) and 16.6–16.7 (resolution/depth-of-focus, §16.27–16.28, Eqs. 200/203/213–215), since those are the ones a reader would want to see in exact form. Deferred per project plan — not done in this pass.

## Overall Assessment

High confidence. All seven gems are standard, well-established physical-optics results and the internal arithmetic (worked examples) checks out. Only outstanding item is the exact Sparrow-limit numeric coefficient in 16.6, marked QUERY rather than confirmed.
