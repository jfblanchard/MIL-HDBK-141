# Book-quality lens drawings: the recipe

The standard every optical schematic in this edition follows. Set on the hardest case, the ch23
microscope (`ch23_microscope/`); copy `draw_objective()` and `draw_microscope()` there as templates.

## Principle

Geometry from the OptiLand prescription, rays from OptiLand's real trace, everything visual from
`common.py`. Do not use `optic.draw()` for book figures: its framing, grid, gray fill and color
cycle are software defaults, not drawing conventions. The physics stays in `build()`; the drawing
code never changes optical data.

## Running

If the environment's optiland editable install points at a stale path, imports fail. Run
every script through the launcher, which falls back to a local optiland checkout
(override with `OPTILAND_SRC`):

```bash
cd MIL-HDBK-141
env -u PYTHONPATH python3 \
    build/lens_designs/run.py build/lens_designs/<name>/<name>_system.py
```

## Conventions

| Item | Rule | Helper |
|---|---|---|
| Size | Draw at final print size. Full width = `TEXT_WIDTH` (6.5 in); a single element or compact group about 4.5-5 in. Height follows from the data at true scale, never chosen by hand. | `book_axes(width, xlim, ylim)` |
| Scale | 1:1 aspect always. Long systems (tube, relay, telescope) keep true scale in each segment and cut the empty stretch out, marked with break lines. Never stretch y. | `broken_axes(width, segments, ylim)` |
| Frame | No axes, ticks, grid or title. The caption lives in the PDF. A scale bar replaces the axes. | `scale_bar(ax, z, y, mm)` |
| Framing | `xlim`/`ylim` hug the drawing plus the label band; output cropped with `bbox_inches="tight", pad_inches=0.02`. | `save_book()` |
| Type | Latin Modern Roman (matches the pdflatex body), 8 pt labels, 6.5 pt surface numbers, mathtext `cm`. Plain text, no TeX escapes. | `BOOK_RC` |
| Lenses | Light gray fill (0.92) with 0.6 pt black outline, flat rims; cemented groups share one diameter, so the cement line reads as an interface. Clear apertures come from the traced rays (x1.06 + small margin), capped at 0.99 R. | `clear_apertures()`, `draw_lenses()` |
| Other media | Cover glass, oil, windows: thin-outline slabs (`MEDIUM`), a darker fill for liquids. | `draw_slab()` |
| Optical axis | Gray dash-dot centre line, behind everything. | automatic |
| Rays | Axial (marginal) rays solid black 0.55 pt; chief ray dashed black; the rest of an off-axis bundle thin gray. One small arrowhead per ray family, early in the path, shows the direction. Include a two-line key whenever more than one style appears. | `trace()`, `draw_rays(..., arrow_at=)`, `AXIAL`/`CHIEF`/`OFFAXIS` |
| Surface numbers | The OptiLand surface index from the script's `build()` (0 = object), so the drawing, the script and `optic.info()` agree. One row above the system, auto-spread so no two collide, each tied to its surface rim by a hairline leader. | `number_surfaces(ax, edges, y, min_sep)` |
| Labels | Lower-case anatomical names (objective, field lens, eye lens, eyepoint, diaphragm, specimen) with hairline leaders, no arrowheads. Place them in empty space so leaders never cross a ray. | `label(ax, text, xy, xytext)` |
| Numbers on the figure | Only values the book itself prints on that figure, or that its text states for it (N.A. 1.25 from 23.3.4). Never print an OptiLand value as a label; the deltas belong in the README. | |
| Output | `<name>.pdf` (vector, fonts embedded, for the book) + `<name>.png` at 600 dpi (review). | `save_book(fig, path)` |

## What changed for ch23 (before / after)

**Before:** `save_layout()` wrapped `optic.draw()`: 14x4 in and 8x4 in panoramic plots at 150 dpi,
axes in mm with grid, a title inside the figure, gray translucent lenses, three fields in the
default blue/orange/green with no key, no surface numbers, no labels. The whole-microscope view was
20:1 with the objective a smudge at the left edge.

**After:**
- `common.py` gained the book-drawing layer above (`BOOK_RC`, styles, `book_axes`, `broken_axes`,
  `trace`, `draw_rays`, `sag`, `clear_apertures`, `elements`, `draw_lenses`, `draw_slab`,
  `number_surfaces`, `label`, `scale_bar`, `save_book`). `save_layout()` is unchanged, so the other
  four systems still run as before until they are converted.
- `run.py` added: the launcher that works around the dangling editable optiland install.
- `ch23_microscope_system.py`: optics and printed numbers untouched; the two `save_layout()` calls
  became `draw_objective()` (Fig 23.7 redrawn: axial bundle at N.A. 1.25, cover glass and oil
  film, surfaces 1-11, the book's "174.90 to image plane", 2 mm bar) and `draw_microscope()` (full
  width, objective and eyepiece at one true scale with the tube cut out, axial pair plus chief ray
  to the eyepoint, Fig 23.8's 11.08 mm diaphragm at the traced focal plane, surfaces 12-15, key,
  5 mm bar).

## Converted systems

All five are done: ch23 (above), then ch12 relay (`draw_relay`, ideal lenses via `thin_lens`, `dimension`
for D), ch14 Huygenian and Ramsden (shared `draw_ch14_eyepiece`: light travels toward the eye, so rays
use `draw_rays(..., reverse=True)`; the book's own distances go in with `dimension`; diaphragms with
`stop_bars`), and ch15 telescope (`draw_telescope`, `broken_axes` with the tube cut out).

## Construction schematics (no prescription)

Interferometers, test benches and illuminators have no lens data in the book. Draw them with `schem.py`: ideal thin lenses
(`tlens`), mirrors, plates and 45 degree splitters at the geometry the figure defines, rays computed from that geometry, the same
styles and type as above. Print only the symbols the caption names; exaggerated angles and gaps are stated in the folder README.
If the spec gives neither a prescription nor enough geometry, write `FLAG-UNABLE` in the folder README instead of inventing it.

## Checklist: every figure, before it ships

1. **True scale, no dead space.** Aspect 1:1 (or true-scale broken segments), width set by the
   page rule, nothing but the drawing and its labels inside the crop.
2. **No software look.** No axes, ticks, grid, in-figure title, color, or default legend box. Black
   line art on white, Latin Modern type, vector PDF with embedded fonts.
3. **Every surface numbered** by its OptiLand index, every element or part named, and every ray
   style in use explained by a key.
4. **Nothing collides.** View the 600 dpi PNG at full size: no text touching text, lines or rays;
   no leader crossing a ray; arrowheads not doubled.
5. **Numerically honest.** Every number on the figure is printed by the book for that figure (or
   stated in its text), and the script's printed book-vs-OptiLand lines still match the README.
