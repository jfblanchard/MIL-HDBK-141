# Fig 20.101: measured spectral transmittance of a Fabry-Perot type multilayer filter, and a parallel resonant circuit

Measured data (Dr. C. Alley), no formula: traced from docs/scans/ch20.pdf page 75 (400 dpi) with `ch20_fp_multilayer_trace.py`.
Ticks but no grid: affine fit to 14 ticks (digitize.tick_axes), residual 0.14 mu in x and 0.0015 in T, so the curve is good to
about 0.5 percent of either span (`trace.csv`). From the trace: T_max = .845 at 796.9 mu, half width about 5.7 mu (794.0-799.8).
The printed lambda_0 tick (796.5 mu, inside the bottom edge), the T_max leader and the Delta lambda_1/2 arrows (at T = .42) are
placed where the scan has them. Outside 788-809 mu the curve lies on the frame's zero line and is not redrawn.
The circuit is the scan's own schematic (the caption's 'A parallel resonant circuit'): two terminals feeding a capacitor and
an inductor in parallel, labelled as printed; it is a symbol drawing, not to scale. Axes as printed: 780-820 mu, T 0 to 1.0.
