# MIL-HDBK-141 — Scientific Validation Response: Chapter 3 (Considerations of Physical Optics)
**Date:** 2026-08-25  
**Chapter:** 03 — Considerations of Physical Optics (pages 3-1 to 3-7)  
**Validator model:** Cascade / Gemini  
**Stage:** Scientific validation of VLM pass output  

---

## 1. Specific Questions

ITEM: Question 1 — Phase velocity derivation in Equation (8)
STATUS: PASS
FINDING: Differentiating the wavefront equation $knz + \phi - \omega t = \text{const}$ with respect to time yields $kn(dz/dt) - \omega = 0 \implies dz/dt = \omega/(kn) = \lambda/(nT) = c/n = v$; derivation is exact.

ITEM: Question 2 — Fringe width formula in Equation (35)
STATUS: PASS
FINDING: Confirmed exact: setting phase progression $kn\Delta x\sin\theta = 2\pi$ with $k = 2\pi/\lambda$ yields $h = \Delta x = \lambda/(n\sin\theta)$ without approximation.

ITEM: Question 3 — Incoherent superposition via phase averaging
STATUS: PASS
FINDING: Averaging $\cos\delta$ over a uniform random phase distribution $[0, 2\pi]$ yields $\overline{\cos\delta} = 0$, recovering the linear superposition of time-averaged energy $W = \frac{1}{2}(a_1^2 + a_2^2) = W_1 + W_2$.

ITEM: Question 4 — Proportionality constant convention in wave energy ($W = a^2/2$)
STATUS: PASS
FINDING: Setting proportionality constant to unity ($\propto E^2 \to W_i = E^2$, $\bar{W} = a^2/2$) is standard pedagogical practice in physical optics (Born & Wolf, Goodman) and internally consistent throughout the chapter.

ITEM: Question 5 — Small-angle plane approximation in Equation (34)
STATUS: PASS
FINDING: Correct: neglecting the axial phase term $knz(1-\cos\theta) \approx \pi n z \theta^2 / \lambda$ requires observations constrained to transverse planes near $z = 0$ ($|z| \ll \lambda / (\pi n \theta^2)$).

ITEM: Question 6 — Nyquist sampling criterion in Gem 3.1
STATUS: PASS
FINDING: A spatial interference pattern with fringe period $h$ (spatial frequency $f_x = 1/h$) requires sensor pixel pitch $\le h/2$ to satisfy the Nyquist-Shannon limit and prevent moiré/aliasing.

---

## 2. Equations Validation

ITEM: Equation (1) — Refractive index definition ($n = c / v_\text{phase}$)
STATUS: PASS
FINDING: Standard definition of phase refractive index.

ITEM: Equation (2) — Phase velocity ($v = \nu\lambda = c/n$)
STATUS: PASS
FINDING: Standard dispersion-free phase velocity relationship.

ITEM: Equation (3) — Medium wavelength ($\lambda = \lambda_0 / n$)
STATUS: PASS
FINDING: Correct relationship between vacuum and medium wavelengths at constant temporal frequency.

ITEM: Equation (4) — Plane wave electric field ($E(z,t) = a\cos(knz + \phi - \omega t)$)
STATUS: PASS
FINDING: Standard real sinusoidal plane wave propagating in $+Z$ direction.

ITEM: Equation (7) — Wavefront surface condition ($knz + \phi - \omega t = w$)
STATUS: PASS
FINDING: Exact definition of constant phase surface.

ITEM: Equation (8) — Phase velocity from wavefront ($dz/dt = \omega/(kn) = c/n$)
STATUS: PASS
FINDING: Rigorous kinematic evaluation of wavefront velocity.

ITEM: Equation (9) — Arbitrary direction plane wave ($E = a\cos[kn(px+qy+rz)+\phi-\omega t]$)
STATUS: PASS
FINDING: Exact 3D directional cosine representation of a planar wavefront.

ITEM: Equation (13) — Instantaneous wave energy ($W_i = E^2 = a^2\cos^2(\Phi-\omega t)$)
STATUS: PASS
FINDING: Standard instantaneous quadratic energy density representation.

ITEM: Equations (14) & (16) — Time-averaged energy ($W = a^2/2$)
STATUS: PASS
FINDING: Exact cycle average of $\cos^2(\Phi - \omega t)$ over period $T$.

ITEM: Equation (24) — Collinear coherent interference ($W = \frac{1}{2}[a_1^2 + 2a_1 a_2\cos\delta + a_2^2]$)
STATUS: PASS
FINDING: Exact two-beam interference equation for parallel-polarized collinear waves.

ITEM: Equations (25) & (26) — Constructive & destructive limits ($W_\text{max}, W_\text{min}$)
STATUS: PASS
FINDING: Exact extrema corresponding to $\cos\delta = \pm 1$.

ITEM: Equation (29) — Incoherent wave superposition ($W = \frac{1}{2}(a_1^2 + a_2^2)$)
STATUS: PASS
FINDING: Correct representation of statistical energy superposition.

ITEM: Equation (33) — Non-collinear coherent interference
STATUS: PASS
FINDING: Exact 2D spatial interference intensity distribution for waves crossing at angle $\theta$.

ITEM: Equation (34) — Small-angle interference approximation ($2W = a_1^2 + a_2^2 + 2a_1 a_2\cos(\delta - 2\pi n x\theta / \lambda)$)
STATUS: PASS
FINDING: Valid paraxial and near-plane approximation.

ITEM: Equation (35) — Interferometer fringe width ($h = \Delta x = \lambda / (n\sin\theta)$)
STATUS: PASS
FINDING: Exact spatial recurrence period for two-beam interferometry.

---

## 3. Gem Claims Validation

ITEM: Gem 3.1 — Interferometer fringe width formula ($h = \lambda/(n\sin\theta)$)
STATUS: PASS
FINDING: Mathematically sound and widely used in Twyman-Green, Mach-Zehnder, and Fizeau interferometry; small-angle expansion $h \approx \lambda/(n\theta)$ has $< 0.35\%$ error at $\theta = 0.14\text{ rad} \approx 8^\circ$. Worked example ($\lambda = 0.633\,\mu\text{m}, \theta = 1\text{ mrad} \to 0.633\text{ mm}$) and Nyquist detection rule ($\text{pitch} \le h/2$) are exact.

---

## 4. Chapter Summary

ITEM: Chapter Summary
STATUS: PASS
FINDING: Accurately and completely summarizes the scope of physical optics fundamentals, wave mechanics, interference equations, and the diffraction basis of optical resolution.

---

## 5. Overall Assessment

Chapter 3 is scientifically rigorous and completely accurate. The progression from Maxwellian plane-wave kinematics to time-averaged energy densities, statistical incoherence, non-collinear interference geometry, and the fundamental fringe-width formula ($h = \lambda/(n\sin\theta)$) is validated with zero mathematical or physical errors.
