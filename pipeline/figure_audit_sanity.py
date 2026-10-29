#!/usr/bin/env python3
"""Claude sanity pass over the Gemini figure audit (Phase 3b, 2026-09-24).

Rewrites every REWRITTEN row of verification/FIGURE_AUDIT.md in place with a verdict, plus the 11
'no figure on page' UNVERIFIED rows. Verdicts:
  CONFIRMED  Gemini's objection holds; title set to the book's printed caption.
  RESTORED   Gemini was wrong (wrong page, 80-char display truncation, or misread); original stands.
  CORRECTED  neither was right; title and note from the scan.
Titles are the printed captions, read from the scan (page given as p.CH-NN) or, where marked
'caption text', from the validated caption line in ocr_output/.
"""
import re
from collections import Counter
from pathlib import Path

AUDIT = Path(__file__).resolve().parents[1] / "verification" / "FIGURE_AUDIT.md"
C, R, X = "CONFIRMED", "RESTORED", "CORRECTED"
TXT = "caption text; Gemini's objection was the 80-char display truncation or verbosity, not a defect"
OFF = "Gemini was shown the transcription's page label; the figure is on scan p.13-{}, where Gemini itself read this caption"
OFFS = "Gemini was shown the transcription's page label; the figure is on scan p.13-{} (read there)"
F5 = "ch05 figure block is fabricated (not in the book); "

# REWRITTEN rows, in file order (0..126)
V = {
    0: (R, "Illustration of refraction.", "p.2-2; original adds 'at a plane interface' (descriptive, correct)"),
    1: (R, "Unit vectors for ray directions.", "p.2-2; original adds 'at a curved interface' (descriptive, correct)"),
    2: (C, 'Optical constants for a "standard eye."', "p.4-4; a full schematic eye (lens outer/inner n, nodal points); the spec's '(Gullstrand reduced eye)' is wrong"),
    3: (R, "Variation of some attributes of vision with luminance.", "p.4-6; spec correct, only display-truncated"),
    4: (X, "An optical system containing a mirror.", F5 + "real Fig 5.2 is on p.5-1; no 'ray transfer diagram' exists"),
    5: (X, "Cross-sectional view of a centered optical system.", F5 + "real Fig 5.4 is on p.5-4; Gemini's 5.6 is the next figure (p.5-6)"),
    6: (X, "Right-handed coordinate axes.", F5 + "real Fig 5.5 is on p.5-4"),
    7: (X, "Determination of n₋₁ cos I.", F5 + "real Fig 5.8 is on p.5-7"),
    8: (C, "Triangle for the law of refraction.", F5 + "real Fig 5.9 is on p.5-10, as Gemini read"),
    9: (X, "Step-wise approximations from tangent sphere intersection, point 0, to final intersection point.", F5 + "real Fig 5.11 is on p.5-15"),
    10: (X, "Ray tracing by the PR method.", F5 + "real Fig 5.12 is on p.5-23"),
    11: (X, "Transfer procedure for the PR method.", F5 + "real Fig 5.13 is on p.5-24 (the last ch05 figure)"),
    12: (X, "(no Figure 5.14 in the book)", F5 + "ch05 figures end at 5.13; the p.5-14 figure is 5.10"),
    13: (X, "(no Figure 5.15 in the book)", F5 + "the p.5-15 figure is 5.11"),
    14: (X, "(no Figure 5.19 in the book)", F5 + "p.5-19 holds Table 5.3"),
    15: (X, "(no Figure 5.20 in the book)", F5 + "p.5-20 holds Table 5.4"),
    16: (C, "Diagram illustrating the data used to compute the optical invariant.", "p.6-6; only the axial ray from the object base is drawn; the spec's chief ray and Φ annotation are not in the figure"),
    17: (C, "Location of first focal point, first principal point, and first focal length.", "p.6-12; spec's 'principal plane' and 'second focal length' are wrong"),
    18: (C, "The location of the principal points, focal points, and nodal points for a single mirror system.", "p.6-22; N₁N₂ at the centre of curvature, F₁F₂ at r/2, P₁P₂ at the vertex; the spec puts all six at one point"),
    19: (C, "P̃ versus ν_F-C for several glasses.", "p.6-34 (page rotated); ν = (n_D−1)/(n_F−n_C) is the horizontal axis, P̃ the vertical; the spec swaps them"),
    20: (R, "Sample lens used for numerical analysis.", "caption text; ch08 text says the figure is 'drawn to scale from Table 6.7' (Table 8.1 gives its numbers), so Gemini's 'Table 8.1' fix is wrong"),
    21: (R, "Sample plot of selected ray trace data.", TXT),
    22: (C, "Variation of distortion and spherical aberration with curvature c₂.", "p.10-14; original title 'Third order solution curves for System 10A' is not the caption"),
    23: (C, "Spot diagrams for left hand solution in Table 10.10.", "p.10-26; two rows only (t_k = −0.02, 0); the spec's third row (t = +0.02) is not in the figure"),
    24: (C, "Spot diagrams for right hand solution in Table 10.10.", "p.10-26; two rows (t_k = −0.02, 0), same as 10.10"),
    25: (R, "A plot of B_c the total spherical aberration of the negative lens as a function of φ_a.", "p.11-16; spec matches"),
    26: (R, "A plot of B_c as a function of φ_a for a triplet.", "p.11-17; spec matches"),
    27: (R, "A single reflection problem.", "p.13-3; S₀ does travel along +Z: M = (−½, −½, 1/√2) reflects +k into S₁ at 45° in the XY plane, as drawn. Gemini's −Z is wrong"),
    28: (R, "Rotation of the coordinate axes.", "p.13-8; spec matches"),
    29: (R, "Image position and orientation in the Z-plane.", "p.13-11; 'Z-plane' is printed; Gemini's 'Y-plane' is wrong"),
    30: (R, "The solid-angle image.", "p.13-14; four panels (a)-(d), as the spec says"),
    31: (R, "The Amici prism as a double reflector.", OFFS.format(18)),
    32: (R, "The Amici prism in telescope systems.", OFF.format(19)),
    33: (R, "Reflections through the Porro prism.", OFFS.format(20)),
    34: (R, "Right-angle prism tunnel diagram.", OFF.format(21)),
    35: (R, "Porro prism tunnel diagram.", OFFS.format(22)),
    36: (R, "The apparent thickness of a glass block.", OFFS.format(23)),
    37: (R, "The glass block and the convergent beam of light.", OFF.format(24)),
    38: (R, "Porro prism system.", OFF.format(26)),
    39: (R, "Porro prism tunnel diagram.", OFF.format(26)),
    40: (R, "Abbe prism, type A.", OFF.format(28)),
    41: (R, "Abbe prism, type A, tunnel diagram.", OFF.format(28)),
    42: (R, "Abbe prism, type B.", OFF.format(29)),
    43: (R, "Abbe prism, type B, tunnel diagram.", OFF.format(29)),
    44: (R, "Leman prism.", OFF.format(30)),
    45: (R, "Leman prism tunnel diagram.", OFF.format(30)),
    46: (R, "Amici prism.", OFF.format(31)),
    47: (R, "Amici prism tunnel diagram.", OFF.format(31)),
    48: (R, "Schmidt prism.", OFF.format(32)),
    49: (R, "Schmidt prism tunnel diagram.", OFF.format(32)),
    50: (R, "Right-angle prism.", OFFS.format(33)),
    51: (R, "Right-angle prism tunnel diagram.", OFFS.format(33)),
    52: (R, "Harting-Dove prism.", OFF.format(34) + "; printed name is 'Harting-Dove'"),
    53: (R, "Dove prism tunnel diagram.", OFF.format(34)),
    54: (R, "Double Dove prism.", OFFS.format(35)),
    55: (X, "(lower half of Figure 13.51, mislabeled 13.52)", "p.13-35; the orthographic hexagonal section and dimension data belong to Fig 13.51; the next block is the real 13.52"),
    56: (R, "Double Dove prism tunnel diagram.", OFFS.format(35)),
    57: (R, "Pechan prism.", OFF.format(36)),
    58: (R, "Pechan prism tunnel diagram.", OFF.format(36)),
    59: (R, "Reversion prism.", OFF.format(37)),
    60: (R, "Penta prism.", OFFS.format(38)),
    61: (R, "Penta prism tunnel diagram.", OFFS.format(38) + "; 1962 ORIGINAL (sic): printed as 'Figure 13.56' (duplicate of the reversion-prism number), should be 13.58"),
    62: (R, "The Wollaston prism.", OFF.format(39)),
    63: (R, "The Wollaston prism tunnel diagram.", OFF.format(39)),
    64: (R, "A Carl Zeiss prism system.", OFFS.format(40)),
    65: (R, "Carl Zeiss prism system tunnel diagram.", OFFS.format(40)),
    66: (R, "A Goerz prism system.", OFF.format(41)),
    67: (R, "A Goerz prism system tunnel diagram.", OFF.format(41)),
    68: (R, "An ocular prism by Zeiss.", OFF.format(42)),
    69: (R, "A Barr and Stroud ocular prism.", OFFS.format(43)),
    70: (R, "A Zeiss coincidence prism system.", OFF.format(44)),
    71: (R, "A Carl Zeiss binocular-ocular prism system.", OFF.format(45)),
    72: (R, "A Zeiss binocular-ocular prism tunnel diagram.", OFF.format(45)),
    73: (R, "Frankford Arsenal prism No. 1.", OFF.format(46)),
    74: (R, "Frankford Arsenal prism No. 1 tunnel diagram.", OFF.format(46)),
    75: (R, "Frankford Arsenal prism No. 2.", OFF.format(47)),
    76: (R, "Frankford Arsenal prism No. 2 tunnel diagram.", OFF.format(47)),
    77: (R, "Frankford Arsenal prism No. 3.", OFF.format(48)),
    78: (R, "Frankford Arsenal prism No. 3 tunnel diagram.", OFF.format(48)),
    79: (R, "Frankford Arsenal prism No. 4.", OFF.format(49)),
    80: (R, "Frankford Arsenal prism No. 4 tunnel diagram.", OFF.format(49)),
    81: (R, "Frankford Arsenal prism No. 5.", OFF.format(50)),
    82: (R, "Frankford Arsenal prism No. 5 tunnel diagram.", OFF.format(50)),
    83: (R, "Frankford Arsenal prism No. 6.", OFFS.format(51)),
    84: (R, "Frankford Arsenal prism No. 6 tunnel diagram.", OFFS.format(51)),
    85: (R, "Frankford Arsenal prism No. 7.", OFFS.format(52)),
    86: (R, "Frankford Arsenal prism No. 7 tunnel diagram.", OFFS.format(52)),
    87: (R, "Huygenian eyepiece. Distances in cm.", "p.14-2; spec's lens order is right (eye lens by the exit pupil, both plano-convex, plane sides to the eye), matching Table 14.1"),
    88: (R, "Kellner eyepiece. Distances in cm.", "p.14-6; Gemini's 'field then eye' order is wrong. Spec nits: the eye-side doublet is a 617366 flint meniscus then a 541599 biconvex crown; '0.705 cm wide' is the exit-pupil distance"),
    89: (C, "Erfle eyepiece. Distances in cm.", "p.14-14; Table 14.7 is 3 groups / 5 elements (doublet, singlet, doublet); the spec's 'five lens groups, six elements' is wrong"),
    90: (R, "Tangential rays.", "p.15-6; spec is accurate (one D curve plus F and C points per oblique panel)"),
    91: (R, "The parallel plate interferometer with nearby light source S.", "Gemini itself says the caption matches"),
    92: (C, "A second method for producing channeled spectra.", "p.16-43; the Osterberg-LaMarre attribution in the spec is supported by the text on p.16-42"),
    93: (R, "The range of commercially available glass, with respect to index and ν values.", TXT),
    94: (C, "A plot of spherical aberration of a single refracting surface.", "p.19-3; original was a caption tail split off by the parser"),
    95: (C, "Corrected doublet-surfaces 1 and 3 undercorrecting, surface 2 overcorrecting.", "p.19-3"),
    96: (C, "Single positive lens used in doublet of Figure 19.3.", "p.19-5"),
    97: (C, "Clark lens, illustrating air spacing to increase over-correction of zonal ray.", "p.19-5"),
    98: (C, "The doublet used in Figure 19.2 corrected for spherical aberration and color.", "p.19-5"),
    99: (C, "Refraction of monochromatic light by the positive element of the doublet shown in Figure 19.3.", "p.19-5"),
    100: (C, "Refraction and correction of monochromatic light by the Clark lens shown in Figure 19.6.", "p.19-5"),
    101: (C, "Curved focal surface, concave mirror.", "p.19-11"),
    102: (C, "Schmidt plate with parallel central section, (a); and parallel zonal section, (b).", "p.19-13"),
    103: (C, "Section view of a satellite-tracking camera. (Courtesy of Perkin Elmer Corp.)", "p.19-15"),
    104: (C, "A Barlow lens.", "p.19-19"),
    105: (C, "S. M. T. Optical arrangement. (Courtesy of Perkin Elmer Corp.)", "p.19-19"),
    106: (C, "Computed spectral reflectivity of a single-layer antireflection coating at φ = 0 and φ = 45°.", "p.20-26; n₁ = 1.55 on As₂S₃ glass (n_s = 2.40); the spec's n₁ = 1.90 is wrong"),
    107: (C, "Computed spectral reflectivity of a single-layer antireflection coating at φ = 0 and φ = 45°.", "p.20-26; n₁ = 1.90 on germanium (n_s = 4.05); the spec's 'n₁ = 2.40' is wrong"),
    108: (C, "Computed spectral reflectivity of an eight-layer and a twelve-layer quarter-wave stack, and the envelope of maximum reflectivity.", "p.20-43; Glass (LH)⁴ / (LH)⁶ Air, L = 1.90, H = 2.30; the spec's 4/6 layers and H = 4.30 are wrong"),
    109: (C, "Computed spectral reflectivity of a four-layer and a ten-layer quarter-wave stack, and envelope of maximum reflectivity.", "p.20-43; Glass (LH)² / (LH)⁵ Air, L = 1.35, H = 4.00"),
    110: (X, "A comparison of the wavelength (in vacuo) with the optical thickness of a basic period of a multilayer with a periodic structure, for various orders of interference.", "p.20-44; the block's text describes Fig 20.56, not 20.55 (numbering shifted by one)"),
    111: (X, "Computed spectral reflectivity of an eight-layer quarter-wave stack and its envelope of maximum reflectivity.", "p.20-44; the block's text describes Figs 20.57 (2:1 stack) and 20.58 (3:1 stack), which have no blocks of their own"),
    112: (R, "Computed spectral reflectivity of a multilayer consisting of an ensemble to two stacks.", TXT + " ('to', sic, as printed)"),
    113: (R, "An illustration of the method of computing the total transmission T₂ of a composite …", TXT),
    114: (C, "The transmission as a function of wave number of a Fabry-Perot interferometer with t_g = 0.0025 cm.", "p.20-75; the spec's 780-820 mμ wavelength axis belongs to Fig 20.101"),
    115: (C, "Measured spectral transmittance of a Fabry-Perot type filter and auxiliary blocking filter composed of ZnS and PbTe.", "p.20-85; Δλ½ = .330 μ as printed (and .051 × 6.45 μ = .329); the spec's .302 μ is wrong"),
    116: (R, "Measured spectral transmittance of a Fabry-Perot type filter at various values of φ.", TXT),
    117: (R, "Measured spectral transmittance of a Fabry-Perot type filter on a BaF2 substrate.", TXT),
    118: (R, "Notation with respect to Fresnel's coefficients for normal incidence.", TXT),
    119: (C, "Plot of the minimum reflectances |ρ₀|²min and |γ₀|²min against the refractive indices n₁ of the monolayers on spectacle crown glass at 45° angle of incidence.", "p.21-51; the n₁ axis runs 1.0-1.4; the spec's 1.0-1.3 is wrong"),
    120: (R, "Examples of basic scanning systems.", TXT),
    121: (R, "Schematic of the Pulfrich refractometer.", TXT),
    122: (R, "Foucault test appearances.", TXT),
    123: (R, "The Gaviola technique of Foucault Testing.", TXT),
    124: (R, "Star images showing various amounts of primary spherical aberration.", TXT),
    125: (C, "Frequency response of lens A .4 mm outside focus for various colors.", "p.26-16; curve 5 bottoms out near −0.08 at about 20 cycles/mm; the spec's '−0.8 near 15' is wrong"),
    126: (C, "The Lambert's test object for measuring sine wave response.", "p.26-16; a variable-area object with a sinusoidal (scalloped) edge; the spec's 'square-wave profile' is wrong"),
}

# UNVERIFIED 'no figure on page' rows, keyed by fig id
U = {
    "5.1": (X, "A cross-section view of a photographic lens.", F5 + "real Fig 5.1 is on p.5-1"),
    "5.3": (X, 'Diagram showing "folding out" of an optical system containing a mirror.', F5 + "real Fig 5.3 is on p.5-2"),
    "5.6": (X, "Diagram of a skew ray in space between the j₋₁ surface and the jth surface.", F5 + "real Fig 5.6 is on p.5-6"),
    "5.7": (X, "Some properties of a spherical surface.", F5 + "real Fig 5.7 is on p.5-7"),
    "5.10": (X, "Diagram of a skew ray in space between the j₋₁ surface and the jth aspheric surface.", F5 + "real Fig 5.10 is on p.5-14"),
    "5.16": (X, "(no Figure 5.16 in the book)", F5 + "ch05 figures end at 5.13"),
    "5.17": (X, "(no Figure 5.17 in the book)", F5 + "ch05 figures end at 5.13"),
    "5.18": (X, "(no Figure 5.18 in the book)", F5 + "ch05 figures end at 5.13"),
    "5.19": (X, "(no Figure 5.19 in the book)", F5 + "ch05 figures end at 5.13"),
    "13.35": (R, "Abbe prism system.", "Gemini was shown the transcription's page label; the figure is on scan p.13-27, where Gemini read this caption"),
    "13.36": (R, "Abbe prism system tunnel diagram.", "figure is on scan p.13-27, where Gemini read this caption"),
}


def cell(s):
    return s.replace("|", "/")


def main():
    lines = AUDIT.read_text().split("\n")
    k, out = 0, []
    for ln in lines:
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.startswith("| ") else None
        if c and len(c) >= 4 and c[3] == "REWRITTEN":
            st, title, note = V[k]
            k += 1
            ln = f"| {c[0]} | {c[1]} | {c[2]} | REWRITTEN→{st} | {cell(title)} | {cell(note)} |"
        elif c and len(c) >= 4 and c[3] == "UNVERIFIED" and "no figure on page" in ln:
            st, title, note = U[c[0]]
            ln = f"| {c[0]} | {c[1]} | {c[2]} | UNVERIFIED→{st} | {cell(title)} | {cell(note)} |"
        out.append(ln)
    assert k == len(V) == 127, k
    AUDIT.write_text("\n".join(out))
    cnt = Counter(v[0] for v in V.values())
    ucnt = Counter(v[0] for v in U.values())
    print("REWRITTEN:", dict(cnt), "UNVERIFIED(no-fig):", dict(ucnt))


if __name__ == "__main__":
    main()
