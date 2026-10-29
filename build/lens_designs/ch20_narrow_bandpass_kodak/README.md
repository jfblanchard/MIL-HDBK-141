# Fig 20.120: measured spectral transmittance of a narrow band-pass filter with a nearly rectangular pass band

Measured data (Eastman Kodak), no formula: traced from docs/scans/ch20.pdf page 90 (400 dpi) with `ch20_narrow_bandpass_kodak_trace.py`.
Ticks but no grid: affine fit to 9 ticks (digitize.tick_axes), residual 0.0003 micron in x and 0.0007 in T: the curve is good to
about 0.5 percent of either span (`trace.csv`). Peak T = .51 at 4.50 micron, as printed. The widths do NOT match their labels:
traced 0.090 micron at T = 0.26 (printed .08) and 0.168 micron at T = .05 (printed .15).
The scan's own arrows measure 0.086 and 0.164 micron on its own axis, so the 1962 drawing is about 10 percent wider than its
labels (sic, as printed); the curve is kept as drawn and the labels as printed.
Every annotation is the scan's own: lambda_0 arrow, T_max, Delta lambda_1/2 and base band width arrows at their traced levels,
the dashed rejection limits at 4.30 and 4.70 micron with their arrows and 'Rejection Region' labels, and the rejection specs.
Axes as printed: 4.20 micron to the frame edge at 4.765, T 0 to .6.
Spec correction: gap_pages_figure_specs.md gives 500-700 mu, T to 100 percent and a flat top near 80 percent; the scan is
an infrared filter on 4.20-4.76 micron with a .51 peak and a sloping top.
