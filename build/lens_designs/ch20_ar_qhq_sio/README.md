# Fig 20.46: measured reflectance of a quarter-half-quarter antireflection coating, MgF2 + SiO + CeF3 on glass

Measured data (ref. 31), no formula: traced from docs/scans/ch20.pdf page 38 (400 dpi) with `ch20_ar_qhq_sio_trace.py`
(digitize.py: affine pixel-to-data fit to 40 grid intersections, absorbing the scan's tilt; hand-read guide snapped onto the ink).
Fit residual 0.0004 micron in x and 0.00015 in R: the curve is good to about 0.5 percent of either axis span (`trace.csv`).
Curves as printed: the coating's reflectance (solid) and the uncoated-glass level (dashed, flat at R = 0.041).
Axes kept exactly as printed: .08 to .18 microns, R 0 to .05. (sic, as printed) The wavelength labels look wrong for a
glass AR coating (.08-.18 micron is the vacuum ultraviolet); the scale is probably not microns as labelled, but the book
gives no correction, so the printed numbers are kept. The scan's graph-paper grid is not redrawn.
Spec correction: gap_pages_figure_specs.md gives 400-750 mu and R in percent to 2.0; the scan reads .08-.18 and R to .05.
