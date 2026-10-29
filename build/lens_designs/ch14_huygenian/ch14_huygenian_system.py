"""ch14 Table 14.1 Huygenian eyepiece (Figure 14.1), drawn and re-traced in OptiLand.

Book: f = 2.54 cm, exit pupil 5 mm at 0.292 cm from the eye lens (Fig 14.1), sum P = -0.5538,
gamma = 0.711, designed for a 10X telescope (objective f = 25.4 cm). The field stop lies between
the lenses, so the eyepiece's focus is virtual: 0.718 cm inside the last surface.
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from common import ch14_eyepiece, draw_ch14_eyepiece, petzval, row, write_readme  # noqa: E402

ROWS = [(0, 0.3, "517645"), (-0.9519, 2.31, None), (0, 0.45, "517645"), (-0.6732, -0.7183, None)]  # last t: to focus
BOOK = dict(f=25.4, exit_pupil=2.92, sigmaP=-0.5538, gamma=0.711, objective=254.0, stop_to_field_lens=2.68)


def build():
    return ch14_eyepiece(ROWS, BOOK["exit_pupil"] / 10, "Huygenian eyepiece, MIL-HDBK-141 Table 14.1")


if __name__ == "__main__":
    o = build()
    p = o.paraxial
    f, F2, xpl = float(p.f2()), float(p.F2()), float(p.XPL())
    sp = -petzval(o) * 10                       # 1/cm, book sign (traced from the objective side)
    z = o.surfaces.positions.ravel()
    stop_to_lens = float(z[4] - z[-1])          # field stop to field lens plane face
    lines = [row("EFL", BOOK["f"], f, " mm"),
             row("focus from image surface", 0.0, F2, " mm"),
             row("field stop before field lens", BOOK["stop_to_field_lens"], stop_to_lens, " mm"),
             row("sum P", BOOK["sigmaP"], sp, " /cm", "{:.4f}"),
             row("gamma = -1/(f sum P)", BOOK["gamma"], -1 / (f / 10 * sp), "", "{:.3f}"),
             row("exit pupil imaged to (objective at f_o = 254 mm past field stop)", BOOK["objective"], xpl, " mm", "{:.1f}")]
    print("\n".join(lines))
    draw_ch14_eyepiece(o, HERE / "ch14_huygenian_layout.png", 5, ("0.292", 1, 2), ("0.268", 6, 4))
    write_readme(HERE / "README.md", [
        "# ch14 Huygenian eyepiece",
        "- **Source:** MIL-HDBK-141 (1962) ch14, Table 14.1 and Figure 14.1 (p.14-2).",
        "- **Input:** c = 0, -0.9519, 0, -0.6732 /cm; t = 0.3, 2.31, 0.45 cm; both lenses glass 517645; exit pupil 5 mm at 0.292 cm; mm in the model.",
        "- **Drawn** (book style, `BOOK_QUALITY_RECIPE.md`; vector `.pdf` + 600 dpi `.png`): `ch14_huygenian_layout`, Fig 14.1 redrawn in the book's orientation (exit pupil left, light travelling toward the eye), 4.8 in wide at true scale: axial pair through the 5 mm exit pupil and the 15 deg chief ray, field stop between the lenses with the book's 0.292 and 0.268 cm distances, surfaces 1-6 numbered as in `build()` (1 = exit pupil, 2-5 lenses, 6 = field stop), 5 mm bar.",
        "- **OptiLand vs book:** " + "; ".join(lines) + ". The stop at the printed exit pupil re-images onto the objective of the 10X design, confirming the 0.292 cm eye relief.",
    ])
