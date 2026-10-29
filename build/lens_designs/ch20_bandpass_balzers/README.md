# Fig 20.96: measured transmittance of band pass filters using both multilayer and glass absorption filters

Measured data (Balzers), no formula. Source docs/scans/ch20.pdf page 72 (400 dpi), script `ch20_bandpass_balzers_trace.py`.
HAND-READ, not snapped: the seven curves interleave dot for dot on a heavy grid, so automatic snapping jumped between them.
Control points were read off 2x zooms, mapped through an affine fit to 144 grid intersections (residual 3.5 mu, 0.011 in T)
and joined with a PCHIP interpolant; drawn back on the scan they sit on the ink. Accuracy about 1.5 percent of either span;
worst where curves overlap near T = 0 (the feet between filters 1-3), where which foot belongs to which filter is ambiguous.
Line styles follow the scan: 1, 3, 5 dash-dot; 2, 6 dotted; 4 dashed; 7 solid. Curve numbers as printed.
Axes as printed: 350-775 mu (labels 400-700), T 0 to 1.00. The scan's graph-paper grid is not redrawn.
Spec correction: gap_pages_figure_specs.md gives 300-1100 mu; the scan reads 350-775 mu, seven filters, peaks .73 to .92.
