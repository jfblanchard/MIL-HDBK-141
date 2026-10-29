# Fig 20.87: measured spectral transmittance of a multilayer heat reflecting filter

Measured data (Balzers), no formula: traced from docs/scans/ch20.pdf page 66 (400 dpi) with `ch20_heat_filter_balzers_trace.py`.
Affine pixel-to-data fit to 144 grid intersections; the graph paper is hand-ruled and uneven, so the residual is 6 mu in x and
0.01 in T: the curve is good to about 1 percent of either axis span (`trace.csv`). The ripple band (400-720 mu) was guided from
4x zooms of the scan. From 850 to 1050 mu the curve lies on the frame's zero line (T under .01) and is drawn there.
Axes as printed: 350-1200 mu (labels 400-1100), T 0 to 1.0. The scan's graph-paper grid is not redrawn.
Spec correction: gap_pages_figure_specs.md says low IR transmittance through 1200 mu; the scan shows T rising again past
1100 mu to about .5 at the 1200 mu frame edge.
