# Fig 20.85: measured spectral transmittance of a short-wave pass heat reflecting filter

Measured data (Eastman Kodak), no formula: traced from docs/scans/ch20.pdf page 66 (400 dpi) with `ch20_heat_filter_kodak_trace.py`.
Ticks but no grid: affine fit to 16 ticks (digitize.tick_axes), residual 0.001 micron in x and 0.005 in T, so the curve is good
to about 0.5 percent of either axis span (`trace.csv`). Solid measured curve to 0.83 micron, dashed beyond, as printed.
The three circled points are the scan's own (T = .70, the cut-off and the knee); the traced cut-off is at 0.678 micron, T = .30,
inside the printed .685 +- .01 micron. Notes as printed. Axes as printed: .4 to the frame edge at 1.156 micron, T 0 to .9.
The scan's duplicate 'Transmittance' label on the right frame is dropped.
Spec correction: gap_pages_figure_specs.md gives T in percent to 100 and 400-1200 mu; the scan reads T to .9, .4-1.15 micron,
and the curve climbs back to .7 near 1.05 micron (dashed), not a flat IR rejection band.
