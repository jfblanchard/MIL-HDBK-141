"""ch14 Table 14.2 Ramsden eyepiece (Figure 14.4), drawn and re-traced in OptiLand.

Book: f = 2.54 cm, exit pupil 5 mm at 1.187 cm from the first lens (Fig 14.4), field stop 0.6733 cm
past the last surface, sum P = -0.3677, gamma = 1.07, for a 10X telescope (objective f = 25.4 cm).
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from common import ch14_eyepiece, draw_ch14_eyepiece, petzval, row, write_readme  # noqa: E402

ROWS = [(0, 0.297, "517645"), (-0.5712, 2.116, None), (0.5077, 0.424, "517645"), (0, 0.6733, None)]
BOOK = dict(f=25.4, exit_pupil=11.87, bfd=6.733, sigmaP=-0.3677, gamma=1.07, objective=254.0)


def build():
    return ch14_eyepiece(ROWS, BOOK["exit_pupil"] / 10, "Ramsden eyepiece, MIL-HDBK-141 Table 14.2")


if __name__ == "__main__":
    o = build()
    p = o.paraxial
    f, F2, xpl = float(p.f2()), float(p.F2()), float(p.XPL())
    sp = -petzval(o) * 10
    lines = [row("EFL", BOOK["f"], f, " mm"),
             row("field stop past last surface", BOOK["bfd"], BOOK["bfd"] + F2, " mm"),
             row("sum P", BOOK["sigmaP"], sp, " /cm", "{:.4f}"),
             row("gamma = -1/(f sum P)", BOOK["gamma"], -1 / (f / 10 * sp), "", "{:.3f}"),
             row("exit pupil imaged to (objective at f_o = 254 mm past field stop)", BOOK["objective"], xpl, " mm", "{:.1f}")]
    print("\n".join(lines))
    draw_ch14_eyepiece(o, HERE / "ch14_ramsden_layout.png", 6, ("1.187", 1, 2), ("0.673", 5, 6), field_name="right")
    write_readme(HERE / "README.md", [
        "# ch14 Ramsden eyepiece",
        "- **Source:** MIL-HDBK-141 (1962) ch14, Table 14.2 and Figure 14.4 (p.14-4).",
        "- **Input:** c = 0, -0.5712, 0.5077, 0 /cm; t = 0.297, 2.116, 0.424 cm, field stop 0.6733 cm; glass 517645; exit pupil 5 mm at 1.187 cm; mm in the model.",
        "- **Drawn** (book style, `BOOK_QUALITY_RECIPE.md`; vector `.pdf` + 600 dpi `.png`): `ch14_ramsden_layout`, Fig 14.4 redrawn in the book's orientation (exit pupil left, light travelling toward the eye), 4.8 in wide at true scale: axial pair through the 5 mm exit pupil and the 15 deg chief ray, field stop outside the field lens with the book's 1.187 and 0.673 cm distances, surfaces 1-6 numbered as in `build()` (1 = exit pupil, 2-5 lenses, 6 = field stop), 5 mm bar.",
        "- **OptiLand vs book:** " + "; ".join(lines) + ".",
    ])
