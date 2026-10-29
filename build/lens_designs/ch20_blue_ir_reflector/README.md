# Fig 20.86: measured spectral transmittance of a multilayer which reflects the blue and near infrared

Measured data (Fish-Schurman), no formula: traced from docs/scans/ch20.pdf page 66 (400 dpi) with `ch20_blue_ir_reflector_trace.py`.
Ticks but no grid: affine fit to 17 ticks (digitize.tick_axes), residual 3 mu in x and 0.005 in T, so the curves are good to
about 0.5 percent of either axis span (`trace.csv`). Where the two curves tangle (480-530 mu) the guides were read from a 5x zoom
of the scan; through 600-700 mu the two curves lie on top of each other at T about .92 and are not separable to better than .01.
phi = 0 degrees solid, phi = 45 degrees dashed, labels as printed. Right-hand axis as printed: Reflectance = 1 - T, 0 at the top.
Axes as printed: 400-1200 mu, T 0 to 1.0.
Spec correction: gap_pages_figure_specs.md gives 350-1000 mu and a single curve; the scan has two curves (phi = 0 and 45 degrees)
on 400-1200 mu, and a second transmission band rising again beyond 1000 mu.
