# Fig 20.47: measured spectral reflectivity of single and triple-layer antireflection coatings

Measured data (Fish-Schurman), no formula: traced from docs/scans/ch20.pdf page 38 (400 dpi) with `ch20_ar_single_triple_trace.py`.
This plot has tick marks but no grid, so the pixel-to-data map is an affine fit to 16 ticks (digitize.tick_axes, residual
0.4 mu in x and 0.0002 in R); the curves are good to about 0.5 percent of either axis span (`trace.csv`).
Three curves as printed: triple layer (solid), quarter-wave MgF2 (dashed) and the uncoated-glass reflectance (solid, near the top,
falling slightly from .0415 to .040 across the band). Labels and leaders as on the scan; the scan's 'Uncoated Class' is a misprint
of 'Uncoated Glass' and is printed corrected. Axes as printed: 400-750 mu (labels every 100, ticks every 50), R 0 to .04.
Spec correction: gap_pages_figure_specs.md gives R in percent to 5 and 4000-7000 A; the scan reads R to .04 and 400-750 mu,
and the MgF2 minimum is about .0135, not 1.25 percent at 5500 A as the spec words it (close, but in different units).
