# MIL-HDBK-141 — Scientific Validation Response: Chapter 13 (Mirror and Prism Systems)
**Date:** 2026-09-06
**Chapter:** 13 — Mirror and Prism Systems (pages 13-1 to 13-52)
**Validator model:** Devin / DeepSeek V4 Flash Low
**Stage:** Scientific validation of VLM pass output (EQ-A…EQ-G, GEM-13.1…13.9, Summary, Tables)

---

## 1. Equations

ITEM: EQ-A — Vector law of reflection (Eq. 1–2, §13.2.2.1)
STATUS: PASS
FINDING: The recursion $\vec{S}_i = \vec{S}_{i-1} + \Gamma_i\vec{M}_i$ with $\Gamma_i = -2\rho_i = -2(\vec{S}_{i-1}\cdot\vec{M}_i)$ is algebraically identical to the standard vector law of reflection $\vec{S}_1 = \vec{S}_0 - 2(\vec{S}_0\cdot\vec{M})\vec{M}$, which is invariant under reversal of the normal's sign.

ITEM: EQ-B — Worked mirror-normal example (§13.2.2.2)
STATUS: PASS
FINDING: Verified by substitution: for $\vec{S}_0=\vec{k}$ and $\vec{S}_1=\tfrac{1}{\sqrt2}(\vec{i}+\vec{j})$, solving $\rho_1=M_z$, $\Gamma_1=-2M_z$, and the unit-vector constraint $\tfrac{1}{8M_z^2}+\tfrac{1}{8M_z^2}+\tfrac{1}{4M_z^2}=1$ gives $M_z=1/\sqrt2$ and $\vec{M}=-\tfrac12\vec{i}-\tfrac12\vec{j}+\tfrac{1}{\sqrt2}\vec{k}$; this normal correctly reflects the +Z ray into the XY plane at 45° to X, and the stated plane intercepts ($1/M_x=-2$, $1/M_y=-2$, $1/M_z=\sqrt2$) are self-consistent.

ITEM: EQ-C — Plane-distance and normal-vector sign pattern (Eqs. 7–9c)
STATUS: QUERY
FINDING: Eq. (8a–c) are confirmed correct: substituting the foot $\vec{P}=(-D/F^2)(A,B,C)$ into the plane equation gives $A P_x+B P_y+C P_z = -D$, so $P_x=-DA/F^2$ is the true perpendicular foot. Eq. (9a–c) with all-negative signs is a valid unit normal, self-consistent with (8) only under the convention $\vec{P} = -P\vec{M}$ (normal pointing back toward the origin/incident side), which matches the reflection-normal convention used in the worked example (EQ-B) and in Eqs. (13)–(16),(19). The alternative all-positive form $M_x=+A/F$ is equally valid under $\vec{P}=+P\vec{M}$. A *mixed* sign pattern is genuinely inconsistent and would give a wrong foot-of-perpendicular. Claude's normalization to a uniform sign was the correct call, but the exact printed sign pattern cannot be resolved from the corrected OCR alone; recommend a one-line editorial note stating the $\vec{P}=\pm P\vec{M}$ convention rather than asserting either form as uniquely correct.

ITEM: EQ-D — Image-sphere rotation-doubling relation (§13.5.2.3)
STATUS: PASS
FINDING: Arithmetic verified: $\tan\theta = \tan 30°/\sin 45° = 0.57735/0.70711 = 0.81650$ (text 0.81657, rounding), $\theta = 39.23°$ (text 39.2°), image rotation $2\theta = 78.5°$ (text 78.4°, rounding). Special cases are consistent: $\phi=0$ gives $\theta=0$ (erect in the horizontal plane, as stated in §13.5.2.2) and the $2\theta$ factor is the standard exact mirror-rotation doubling applied to the image sphere.

ITEM: EQ-E — Reduced (air-equivalent) prism thickness (§13.8.3.1)
STATUS: PASS
FINDING: Both relations are standard paraxial results for a plane-parallel block: the axial image shift is $t(n-1)/n$ and the reduced (air-equivalent) thickness is $t/n$, consistent with the thick-lens/reduced-distance convention used in ch06.

ITEM: EQ-F — Third-order prism aberrations independent of $y_1$ (Table 13.1)
STATUS: FLAG
FINDING: The conclusion (position independence) is correct physics, and the final totals are right — independently deriving the Seidel surface contributions (Welford-type $S_I,S_{II},S_{III}$ for a planar surface, $c=0$) reproduces $\Sigma B=-t\,u_0^4(n^2-1)/n^3$, $\Sigma F=-t\,u_0^3\bar{u}_0(n^2-1)/n^3$, $\Sigma C=-t\,u_0^2\bar{u}_0^2(n^2-1)/n^3$, all with the $y_1/\bar{y}_1$ terms cancelling. However, the *printed* surface-1 F coefficient $(n-1)/n$ does NOT cancel the surface-2 $y_1$ term: $\tfrac{n^2-1}{n^2}-\tfrac{n-1}{n}=\tfrac{n-1}{n^2}\neq0$, so as typed $\Sigma F$ retains $y_1u_0^2\bar{u}_0(n-1)/n^2$. The correct surface-1 F coefficient (and the analogous surface-2 S coefficient, currently $(n-1)$) should read $(n^2-1)/n^2$ for the cancellation to work. Recommend correcting Table 13.1's F and S intermediate rows; the B, C rows and all final totals are consistent.

ITEM: EQ-G — Interpupillary-distance hinge angle (§13.10.21)
STATUS: PASS
FINDING: Arithmetic verified: $\cos\theta_M = 2.283/2.835 = 0.80529$, $\theta_M = \arccos(0.80529) = 36.37° = 36°22'03''$ (correct); $D_m=58$ mm / $D_M=72$ mm is a reasonable adult IPD design span (see GEM-13.8).

---

## 2. Gems

ITEM: GEM-13.1 — Even/odd reflection parity
STATUS: PASS
FINDING: Correct and exceptionless for any sequence of flat-mirror reflections: the reflection matrix $R=I-2\vec{M}\vec{M}^T$ has eigenvalues $\{1,1,-1\}$ (det = $-1$), so $N$ reflections give det $=(-1)^N$ = $+1$ (even, right-handed) or $-1$ (odd, left-handed).

ITEM: GEM-13.2 — Mirror-rotation-doubling rule
STATUS: PASS
FINDING: Correct and exact for a flat mirror (the 2:1 relation follows from the reflection law for any angle, not just small angles).

ITEM: GEM-13.3 — Mirror-folding/unfolding; curved-mirror power
STATUS: PASS
FINDING: The unfolded curved-mirror equivalence $\phi=-2n/R$ is correct: a spherical mirror has focal length $f=-R/2$ (R positive for concave) and paraxial power $\phi=n/f=-2n/R$.

ITEM: GEM-13.4 — Prism family quick-selector t/n values
STATUS: PASS
FINDING: Spot checks are internally consistent with $t/n = t/1.5170$: Porro pair $4.60/1.517=3.032$ ✓, Amici $1.7071/1.517=1.1253$ ✓, Penta $3.4142/1.517=2.2506$ ✓, right-angle $1.00/1.517=0.6592$ ✓; the ordering (least glass path for the single-reflection right-angle, most for the retroreflecting Porro pair) is physically plausible.

ITEM: GEM-13.5 — Roof-angle tolerance ±3–4 arcseconds
STATUS: PASS
FINDING: Physically plausible and consistent with both 1962 and modern practice: a split-aperture roof prism (beam divided by the roof edge) requires the 90° roof angle held to roughly ±3–5 arcsec to avoid image doubling, achievable with standard interferometric/polishing control; a full-aperture roof (roof outside the beam) has a much looser tolerance, matching §13.7.4.3.

ITEM: GEM-13.6 — Tunnel diagram / non-parallel faces → dispersion
STATUS: PASS
FINDING: Valid design check: if the unfolded entrance and exit faces are not parallel, the prism behaves as a wedge (thin-prism) and introduces angular/color dispersion; parallel faces give no net deviation. Minor caveat (not an error): a parallel-face block still produces a small chromatic difference in lateral displacement, but no dispersion in the deviation sense.

ITEM: GEM-13.7 — Dove prism requires collimated light
STATUS: PASS
FINDING: Correct standard practice: the (Harting-)Dove and Double-Dove prisms have non-parallel faces (wedge-like tunnel diagram) and must be used in parallel light; the Pechan, Reversion, and K-mirror equivalents tolerate convergent/divergent light, matching §13.10.10–13.10.13.

ITEM: GEM-13.8 — Interpupillary distance 58–72 mm
STATUS: PASS
FINDING: Reasonable and still standard for adult IPD design; it is a common binocular adjustment span, slightly conservative on the low end versus modern 5th-percentile adult data (~55 mm) but appropriate for a military population and consistent with the era.

ITEM: GEM-13.9 — Prism aberration independent of axial position
STATUS: PASS
FINDING: The underlying physics is correct and independently verified (see EQ-F): a perpendicular plane-parallel prism's third-order contribution depends only on $t$, $n$, $u_0$, $\bar{u}_0$. The gem rests on the Table 13.1 cancellation, so it should be noted as contingent on correcting the F/S intermediate coefficients.

---

## 3. Summary

ITEM: Chapter summary — §13.1–13.10 scope
STATUS: PASS
FINDING: The summary accurately represents the chapter: vector/matrix reflection and handedness via the determinant sign, the image-sphere tool with the $\tan\theta=\tan\phi/\sin\omega$ relation, two-mirror systems, the 45°-90°-45° prism as right-angle/Porro/Dove, Amici roof prisms and their roof tolerance, the tunnel diagram and reduced thickness $t/n$, position-independent third-order prism aberrations, and the data-sheet catalog. Minor count nitpick: §13.10 actually holds 27 data-sheet subsections (§13.10.2–13.10.28), so "28-entry catalog" in the prompt is off by one and "~20 named prism systems" slightly undercounts.

---

## 4. Tables

ITEM: Table 13.1 — Third-order aberration contributions
STATUS: FLAG
FINDING: As noted in EQ-F, the F-row surface-1 coefficient $(n-1)/n$ (and the analogous surface-2 S coefficient $(n-1)$) are inconsistent with the matching $(n^2-1)/n^2$ pattern in the B and C rows and with the stated totals; with the printed coefficients the $y_1$ term does not cancel. Suggest $(n^2-1)/n^2$ for both; the final $\Sigma B$, $\Sigma F$, $\Sigma C$ and the position-independence claim remain correct.

ITEM: §13.10 data-sheet dimension arithmetic and $t/n$ values
STATUS: PASS
FINDING: Every tabulated reduced thickness satisfies $t/n = t/1.5170$ (e.g. §13.10.2 3.0324, §13.10.7 1.1253, §13.10.14 2.2506, §13.10.22 1.0347, §13.10.23 1.4951, §13.10.26 1.8086, §13.10.28 2.9098), and the dimension relations (Porro $B=1.4142A$, $t=2(2A+3a)$; Schmidt $D=1.4142A+2.3890a$; Pechan $t=4.6213A$) are internally consistent.

ITEM: §13.10.10 Harting-Dove and §13.10.11 Double-Dove closed-form path-length formulas
STATUS: FLAG
FINDING: The transcribed closed-form for $t$ does not reproduce the (internally consistent) tabulated value: the Dove formula $t=\tfrac{n(A+2a)}{\sin\theta\sqrt{n^2-\sin^2\theta}-\sin\theta}$ evaluates to ~6.90, not 3.7165. The correct form is $t=\tfrac{n(A+2a)}{\sin\theta(\sqrt{n^2-\sin^2\theta}-\sin\theta)}$, which yields the stated multiplier 3.3787 (a dropped $\sin\theta$ factor in the denominator). Likewise the Double-Dove $t=\tfrac{nA}{2\sin\theta\sqrt{n^2-\sin^2\theta}-\sin\theta}$ (gives 1.2738) should read $t=\tfrac{nA}{2\sin\theta(\sqrt{n^2-\sin^2\theta}-\sin\theta)}$ to match $t=nAC=1.6893$. The tabulated $t$, $t/n$ and $t=nAC$ relations are correct; only the closed-form transcriptions are off. Also minor: in §13.10.10 the E relation $1.4142(A+2a)=1.4849$ is internally wrong (1.4142×1.1=1.5556); it should be $(A+a)/\cos\theta = 1.4142(A+a) = 1.4849$. And in §13.10.26 a stray t value appears as "2.7431" beside the correct 2.7437.

---

## 5. Overall Assessment

High confidence in the chapter's scientific accuracy. Every item of fundamental physics was verified correct: the vector law of reflection and its recursion, the worked mirror-normal solution (EQ-B), the foot-of-perpendicular geometry (Eq. 8), the reduced-thickness and image-shift formulas, the mirror-rotation doubling, the curved-mirror power equivalence $\phi=-2n/R$, the exact even/odd handedness rule via $\det R = (-1)^N$, the split-aperture roof tolerance of ±3–4 arcsec, the Dove-in-collimated-light requirement, and the 58–72 mm IPD span. The chapter's central claim that a plane-parallel prism's third-order aberration is position-independent is correct and was independently reproduced. The issues found are localized and non-fundamental: (1) Table 13.1 has an internal coefficient inconsistency in the F and S rows (should be $(n^2-1)/n^2$; final totals are correct); (2) the Dove and Double-Dove closed-form path-length formulas each lost a $\sin\theta$ factor and need re-checking against the scan; (3) one sign-convention subtlety in Eq. (9) versus Eq. (8) (a QUERY, both uniform-sign conventions are defensible; the all-negative form is self-consistent under the standard "normal toward the incident side" convention); and (4) a few trivial typos in the dimension annotations. No physics errors affecting design conclusions were found; recommend correcting the flagged Table 13.1 coefficients and re-transcribing the two Dove-formula closed forms against the original scan.
