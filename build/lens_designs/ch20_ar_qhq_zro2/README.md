# Fig 20.44: measured reflectance of a quarter-half-quarter antireflection coating, MgF2 + ZrO2 + CeF3 on glass

Measured data (ref. 31), no formula: traced from docs/scans/ch20.pdf page 38 (400 dpi) with `ch20_ar_qhq_zro2_trace.py`
(digitize.py: affine pixel-to-data fit to 40 grid intersections, which absorbs the scan's tilt; hand-read guide snapped onto the ink).
Fit residual 2.3 mu in x and 0.0002 in R, so the curves are good to about 0.5 percent of either axis span; the trace is in `trace.csv`.
Three curves as printed: the coating's reflectance (solid), absorption in the coating (short dashed curve, 400-450 mu) and the
uncoated-glass level (dashed, a flat R = 0.041). The reflectance touches zero from about 700 to 755 mu and runs along the frame there. Axes as printed: 400-900 mu, R 0 to .05. The scan's graph-paper grid is not redrawn.
Spec correction: gap_pages_figure_specs.md gives 400-750 mu and R in percent to 2.0; the scan reads 400-900 mu and R to .05.
