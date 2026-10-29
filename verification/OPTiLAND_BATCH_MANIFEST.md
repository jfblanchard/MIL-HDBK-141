# OptiLand schematic batch: manifest

Classifies every spec in `gap_pages_figure_specs.md`, `ch22_25_figure_specs.md` and
`last2_gap_pages_figure_specs.md` (104 entries) into exactly one bucket. Status column is updated
as figures are built (`DONE <sha>`, `TODO`, or `FLAGGED`).

**Build mode.** The specs name components and symbols but print no radii, glasses or spacings, except
where noted. These figures are therefore drawn as true-scale *constructions*: ideal thin lenses
(`thin_lens`), plane/spherical mirrors, plates and beam splitters placed at the geometry the figure
defines (45 degree splitters, equal arm lengths, conjugate points), with rays computed from the
geometry. Every printed label is a symbol the caption/spec names; no invented numbers. Where a
figure needs a real prescription or mechanical dimensions the spec does not give, it is
`OptiLand-schematic (FLAGGED)` and is not built.

Bucket totals (104 entries): OptiLand-schematic 57 (42 built, 13 flagged, 2 not started) / Matplotlib-plot 29 (all built) /
Halftone-photo 11 / 3D-coordinate 5 / Table 2.

## OptiLand-schematic

`Resembles` = existing system whose prescription/drawing pattern applies (ch12 relay, ch14
eyepieces, ch15 telescope, ch23 microscope), otherwise `-`.

### Chapter 16

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 16.3 | `ch16_young` | Young's two-pinhole experiment | S0, S1, S2, separation d, screen distance D >> d, path difference xd/D, fringe width lambda D/d | - | DONE 80323f5 |
| 16.4 | `ch16_lloyd` | Lloyd's mirror | source S1 at height h over mirror, virtual S2 at -h, screen at D, pi phase shift at mirror edge | - | DONE 80323f5 |
| 16.6 | `ch16_fresnel_mirrors` | Fresnel double mirror | source S, mirrors M1 M2 at small angle theta, virtual S1 S2, d = 2 a theta | - | DONE 80323f5 |
| 16.7 | `ch16_interface` | amplitude r, t at an interface | n0, n1, i0, i1, A0, rA0, tA0, normal | - | DONE 80323f5 |
| 16.11 | `ch16_fizeau_setup` | Fizeau fringes, wedge between S1 and S2 | pinhole at focus of L1, 45 deg splitter, wedge angle alpha, viewing lens L2 | - | DONE 80323f5 |
| 16.12 | `ch16_michelson` | Michelson interferometer | S, L1, M0 splitter at 45, compensator C, M1 (d1), M2 (d2), L2, eye | - | DONE 80323f5 |
| 16.13 | `ch16_fringe_localization` | where Fizeau fringes localize | wedge alpha, S1, S2, rays meeting at P | - | DONE |
| 16.14 | `ch16_newton_rings` | Newton's rings arrangement | 45 deg plate, plano-convex lens radius R on flat, microscope, t(r) = r^2/2R | - | DONE 6700189 |
| 16.15 | `ch16_sagitta` | sagitta method, spherical reference | R1, R2, y, s1 = y^2/2R1, s2 = y^2/2R2 | - | DONE 6700189 |
| 16.16 | `ch16_twyman_green` | Twyman-Green for a lens | pinhole, L1, splitter M0, flat mirror, test lens LT + sphere mirror, L2 | - | DONE 80323f5 |
| 16.24 | `ch16_reflect_microscope` | vertical illuminator microscope for reflected fringes | eyepiece, tube, objective, 45 deg reflector, lamp + condenser, stage | ch23 objective/eyepiece | DONE |
| 16.27 | `ch16_film_step` | fringe shift by a film step | wedge alpha, film t, x -> x + Dx, d = m lambda/2 | - | DONE 6700189 |
| 16.32 | `ch16_huygens_integral` | Huygens integral conventions | surface sigma, d sigma, n, P0, P, r0, r, theta0, theta | - | DONE 6700189 |
| 16.36 | `ch16_objective_focal` | axisymmetric objective, focal coordinates | pupil radius a, wavefront W radius R, focus O', (x', y', z'), P', R' | - | DONE 6700189 |
| 16.37 | `ch16_resolution` | two self-luminous points resolved | O, P, angle theta, D = 2a, f, dy' = f theta | - | DONE 80323f5 |

### Chapter 20

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 20.1 | `ch20_dichroic` | color-selective beam splitter | 45 deg coated plate, white in, blue transmitted, red + green reflected | - | DONE 6861f5d |
| 20.2 | `ch20_cold_mirror` | cold mirror + heat reflector in a projector | lamp, cold mirror, condenser, hot mirror, film | - | DONE 6861f5d |
| 20.88 | `ch20_camera_finder` | beam splitter diverts image to viewfinder | objective, 45 deg splitter, film, ground glass, field lens, eyepiece | - | DONE 6861f5d |
| 20.98 | `ch20_fabry_perot` | Fabry-Perot interferometer | two plates, gap t_g, angle theta, delta = 2 n t_g cos theta, lens, P | - | DONE 6861f5d |
| 20.99 | `ch20_fp_collimated` | collimated illumination of an FP filter | pinhole at focus of L1, normal incidence, L2, aperture | - | DONE 6861f5d |

### Chapter 21

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 21.2 | `ch21_fresnel_notation` | Fresnel coefficient notation | planar boundary, media (n0, K0)/(n1, K1), i0, i1, p = sin i0, q = cos i0 | - | DONE 6861f5d |
| 21.5 | `ch21_layer_flow` | flow conditions at layers nu-1 and nu | d_{nu-1}, d_nu, tau, r, rho = r/tau | - | DONE 6861f5d |

### Chapter 22

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 22.1 | `ch22_image_converter` | image converter system | objective assembly (4 elements + red filter), tube, field lens, 2 prisms, 4 element magnifier | - | FLAGGED: the spec names the objective assembly (4 elements + red filter), tube, field lens, two prisms and a 4-element magnifier but gives no radii, glasses, spacings or prism dimensions |
| 22.2 | `ch22_aspheric_magnifier` | aspheric magnifier | phosphor, field lens, eye lens, 2 aspheric surfaces | ch14 eyepiece pattern | FLAGGED: field lens and eye lens are named with two aspheric surfaces, but no radii, thicknesses or aspheric coefficients are given |
| 22.3 | `ch22_scanning` | three scanning systems (single, linear, mosaic) | objective, reticle, field lens, detector, fields of view | - | DONE 1d108f0 |
| 22.4 | `ch22_immersed_detector` | flat vs hemispherical immersion | critical angle i_c, hemisphere, n^2 gain | - | FLAGGED: the spec is ambiguous about the dashed "image in space" versus solid "immersed image" ray cones |

### Chapter 23

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 23.2 | `ch23_compound_microscope` | transmitted-light compound microscope | lamp, lamp condensers, substage condenser, slide, cover slip, objective, Huygenian eyepiece, eye | ch23 microscope + ch14 Huygenian | FLAGGED: the illumination train (lamp condensers, substage condenser) has no prescription |
| 23.3 | `ch23_microscope_cutaway` | mechanical stand + optical features | tube length 160 mm, virtual image distance ~250 mm | ch23 microscope | FLAGGED: a mechanical stand cutaway with no dimensions beyond tube length 160 mm and virtual image distance ~250 mm |
| 23.4 | `ch23_kohler` | Kohler illumination, unfolded | conjugate sets (field, aperture); solid vs dashed rays | ch23 microscope | DONE 1d108f0 |
| 23.5 | `ch23_vertical_illumination` | vertical illuminator | light source, field iris, condensers, aperture stop, 45 deg semi-reflector, objective, specimen | - | DONE 1d108f0 |
| 23.9 | `ch23_ramsden_section` | Ramsden eyepiece section | d, r.i., F.L., E.L., eye point | ch14 Ramsden | FLAGGED: needs a mechanical barrel section with no dimensions |
| 23.10 | `ch23_high_eyepoint` | high eye-point compensating eyepiece | d, r.i., F.L. doublet, E.L. cemented group | - | FLAGGED: field lens doublet and eye lens group are named but have no prescription |
| 23.12 | `ch23_darkfield_central_stop` | refracting condenser, central stop | stop, condenser lenses, slide, specimen, objective | - | DONE 1d108f0 |
| 23.13 | `ch23_darkfield_aspheric` | paraboloid and cardioid condensers | paraboloid wall, cardioid + spherical surface, oil | - | FLAGGED: paraboloid and cardioid condenser surfaces have no conic constants or dimensions in the spec |
| 23.15 | `ch23_ultramicroscope` | slit ultramicroscope | A arc, B condensing lens, C cross slit, D objective, E cell, F microscope | - | DONE 1d108f0 |
| 23.19 | `ch23_ao_baker` | AO Baker interference microscope | mirror, polarizer, condenser, plates, objective, 1/4 wave plate, analyzer, eyepiece | - | FLAGGED: component prescriptions (condenser, objective, birefringent plates) are not given |
| 23.20 | `ch23_shearing_doublefocus` | shearing vs double-focus ray paths | birefringent plates, object/reference foci | - | DONE 1d108f0 |
| 23.22 | `ch23_petrographic` | petrographic microscope | 17 listed components, no values | - | FLAGGED: seventeen components are listed with no prescriptions or spacings |

### Chapter 24

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 24.2 | `ch24_phase_front` | constant-phase front from ray data | planes P-P, E-E, points K D B F C and primed, optical system box | - | DONE 1d108f0 |

### Chapter 25

| Figure | Script folder | Shows | Key values from spec | Resembles | Status |
|---|---|---|---|---|---|
| 25.2 | `ch25_nodal_slide` | focal length by nodal slide | S, Lc, Lx, rotation axis at N2, eye | - | DONE 4699d2f |
| 25.4 | `ch25_astigmatism_grid` | astigmatism with a grid reticle | R, Lc, Lx, microscope M, eye | - | DONE 4699d2f |
| 25.5 | `ch25_distortion_nodal` | distortion by nodal slide | f, beta, f sec beta, y = f tan beta | - | DONE 4699d2f |
| 25.8 | `ch25_pulfrich` | Pulfrich refractometer | n_s = sqrt(n_p^2 - sin^2 i_r), sub-figures a-d | - | FLAGGED: sub-figure (a) is an instrument drawing with no dimensions |
| 25.9 | `ch25_fizeau_normal` | Fizeau/Newton fringes, 45 deg plate | R, L, G, P, P1, P2, S1, S2, d, dust | - | DONE 4699d2f |
| 25.10 | `ch25_fizeau_near_normal` | near-normal illumination | R, L, G, eye, S1, S2, d, dust | - | DONE 4699d2f |
| 25.11 | `ch25_newton_contact` | surfaces for Newton's fringes | Q, S1 convex, S2, O, d | - | DONE 4699d2f |
| 25.12 | `ch25_fizeau_interferoscope` | Fizeau interferoscope | H, collimator, prism, A, P1, P2, S1, S2, S11, tables T1 T2, screws L1 L2 | - | FLAGGED: mechanical table, leveling-screw and V-groove detail with no dimensions |
| 25.13 | `ch25_modified_michelson` | modified Michelson | H, F, O, compensator, A, B, Q, M | - | DONE 4699d2f |
| 25.14 | `ch25_michelson_fizeau` | Michelson as a Fizeau method | O, A, B, OA = OB, S1, S2, S2' | - | DONE 4699d2f |
| 25.15 | `ch25_twyman_green_plate` | Twyman-Green for a plate | source, H, collimator, O, M1, M2, L1, L2, A, B, P, telescope | - | DONE 4699d2f |
| 25.16 | `ch25_tg_prism` | end mirror relocation for prisms | M1 at B and B', M2 at A | - | DONE 4699d2f |
| 25.17 | `ch25_tg_immersion` | immersion method | E, F, oil, P, M1 at B | - | DONE 4699d2f |
| 25.18 | `ch25_tg_spherical_aberration` | TG for spherical aberration of a lens | H, L, e, f, C, M1 (convex), M1' (concave), B | - | DONE 4699d2f |
| 25.20 | `ch25_ann_arbor` | Ann Arbor autocollimation test | plane mirror, lens, F, tester, P | - | DONE 4699d2f |
| 25.24 | `ch25_foucault` | Foucault test of a mirror | lamp, prism, pinhole, F, knife edge K, eye | - | DONE 4699d2f |
| 25.25 | `ch25_foucault_sensitivity` | slope error theta gives 2 theta | O, theta, F, F', 2 theta | - | DONE 4699d2f |
| 25.29 | `ch25_gaviola` | Gaviola caustic technique | true/observed facet normal, (xi, eta), eye | - | FLAGGED: the spec does not fix the geometry of the true/observed facet normals and the (xi, eta) caustic coordinates well enough to draw it without inventing it |

### Partial builds and notes

Built, with something from the spec not reproduced (stated at the top of each folder's README):
21.5 (boundary ratios rho = r/tau with angled vectors), 22.3 (scan arrow of panel b, detector leads),
23.4 (objective and eyepiece are ideal thin lenses, not the ch23 prescription), 23.15 (slit inset),
23.20 (recombination above the upper plate), 24.2 (ray-length labels u, Pr, L), 16.32 (theta0 drawn
against the outward normal), 25.11 (S2 drawn flat). Figures 16.13 and 16.24 are now drawn (pure schem constructions, no prescription).

## Matplotlib-plot (29, separate batch)

29 DONE, 0 TODO, 0 FLAGGED. `computable` = redrawn from a closed form (thin-film characteristic matrix,
Airy, Rayleigh); `traced` = measured data digitized from the scan with `build/lens_designs/digitize.py`
(affine fit to grid or ticks, guides snapped onto the ink; each folder has `<name>_trace.py` and `trace.csv`);
`hand-read` = control points read off zooms where snapping could not separate the curves. Each folder's
README states the source page, calibration residual, accuracy and any correction to the spec. The specs in
`gap_pages_figure_specs.md` had the wrong axes for most of the measured ch20 plots; the scans were followed.

| Figure | Script folder | Method | Status |
|---|---|---|---|
| 16.2 | `ch16_fizeau_notation` | schematic | DONE 066f1f0 (the scan's 16.2 is a Fizeau notation diagram, not the plot the spec describes; built with schem.py) |
| Table 16.1 | `ch16_rayleigh_curve` | computable | DONE 6a8f5af |
| 16.19 | `ch16_fabry_perot_fringes` | computable | DONE 6a8f5af |
| 16.26 | `ch16_narrow_fringes` | line drawing | DONE 066f1f0 |
| 20.8 | `ch20_eff_thickness` | computable | DONE e3e0dae |
| 20.18 | `ch20_single_layer_angles` | computable | DONE e3e0dae |
| 20.19 | `ch20_single_layer_ns151` | computable | DONE e3e0dae |
| 20.20 | `ch20_single_layer_ns168` | computable | DONE e3e0dae |
| 20.21 | `ch20_single_layer_65` | computable | DONE e3e0dae |
| 20.22 | `ch20_single_layer_rav` | computable | DONE e3e0dae |
| 20.23 | `ch20_single_layer_as2s3` | computable | DONE e3e0dae |
| 20.24 | `ch20_single_layer_ge` | computable | DONE e3e0dae |
| 20.44 | `ch20_ar_qhq_zro2` | traced | DONE 34e3c9b |
| 20.45 | `ch20_ar_qhq_nd2o3` | traced | DONE 34e3c9b |
| 20.46 | `ch20_ar_qhq_sio` | traced | DONE 34e3c9b (x labels .08-.18 micron kept as printed, sic) |
| 20.47 | `ch20_ar_single_triple` | traced | DONE 34e3c9b |
| 20.59 | `ch20_stack_3to1` | computable | DONE e3e0dae |
| 20.60 | `ch20_stack_60deg` | computable | DONE e3e0dae |
| 20.85 | `ch20_heat_filter_kodak` | traced | DONE 2aa957d |
| 20.86 | `ch20_blue_ir_reflector` | traced | DONE 2aa957d |
| 20.87 | `ch20_heat_filter_balzers` | traced | DONE 2aa957d |
| 20.95 | `ch20_qw_stack_reflect` | traced | DONE 6acffab |
| 20.96 | `ch20_bandpass_balzers` | hand-read | DONE fe65077 (hand-read control points + PCHIP; about 1.5 percent) |
| 20.97 | `ch20_ir_bandpass` | traced | DONE b6e356a |
| 20.100 | `ch20_fp_transmission` | computable | DONE e3e0dae |
| 20.101 | `ch20_fp_multilayer` | traced | DONE 893e8ad (with the circuit inset) |
| 20.120 | `ch20_narrow_bandpass_kodak` | traced | DONE 2c684be (drawn widths about 10 percent over the printed labels, sic) |
| 20.121 | `ch20_nine_layer_bandpass` | traced | DONE 9e116c3 ('.12 mu' half width probably a misprint for 1.2, sic) |
| 25.27 | `ch25_foucault_isophotes` | computable | DONE 066f1f0 (Linfoot closed form; matches the scan's curve to about 5 percent) |

## Halftone-photo (scan crop)

24.1, 25.1, 25.6 (engraving), 25.7, 25.21, 25.23, 25.26 (shaded discs), 25.31, 25.32, 25.34, 25.35.

## 3D-coordinate

16.1, 16.33, 16.34, 25.19, 25.22.

## Table

Table 20.1 (substrate materials) — DONE, transcribed to markdown in ocr_output/ch20.md; Table 20.3 (effective indices at 65 degrees) — DONE, transcribed to markdown in ocr_output/ch20.md.
