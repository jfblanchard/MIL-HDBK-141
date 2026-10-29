# Fig 20.97: measured spectral transmittance of some infrared band pass filters, complete with auxilliaries (sic)

Measured data (Bausch and Lomb), no formula: traced from docs/scans/ch20.pdf page 72 (400 dpi) with `ch20_ir_bandpass_trace.py`.
Ticks but no grid: affine fit to 16 ticks (digitize.tick_axes; the 10-micron tick is too faint to find and was skipped),
residual 0.03 micron in x and 0.007 in T, so the curves are good to about 0.5 percent of either span (`trace.csv`).
Five filters as printed, all solid, unlabelled on the scan; peaks about .57 (8.1 microns), .51 (8.9), .47 (10.0), .38 (10.9)
and .33 (12.0). A faint dotted fold line in the scan at 10.43 microns is masked; the curves crossing it are bridged. The scan's in-figure heading 'Measured transmittance of a series of band pass filters complete with
auxiliaries' repeats the caption and is dropped (house style: no in-figure title). Axes as printed: 6-14 microns, T 0 to 1.00.
Spec correction: gap_pages_figure_specs.md gives 1-5 microns and T to 80 percent; the scan reads 6-14 microns, T to 1.00.
