import math
import numpy as np
from ledger import *
from sympy import symbols, sqrt, solve, simplify

# ---------------- ch25 production-phase tests ----------------
ref("ch25", 1, "prism/goniometer geometry of Fig 25.x (not re-derived: figure-dependent)")
d, s, r = symbols("d s r", positive=True)
a = d / sqrt(3)                                   # circumradius of an equilateral leg triangle of side d
sym("ch25", 2, lambda: zero(solve((r - s) ** 2 + a ** 2 - r ** 2, r)[0] - (d ** 2 / (6 * s) + s / 2)),
    "spherometer with legs on an equilateral triangle of side d: r = a^2/(2s) + s/2 with a = d/sqrt(3)")
ref("ch25", 3, "critical-angle refractometer relation n_s = sqrt(n_p^2 - sin^2 i_r)")
ref("ch25", [4, 5, 6, 7], "thin-film/air-gap interference maxima and minima (half- and quarter-wave conditions)")
ref("ch25", 8, "optical path of a reflected film with the lambda/2 reflection phase change")
num("ch25", 9, lambda: close(0.5461e-3 / (3 * 50), 3.64e-6, 0.002) and close(0.5461e-3 / 150 * 206264.8, 0.75, 0.005),
    "0.5461e-3/(3 x 50) = 3.641e-6 rad = 0.751 arcsec")
defn("ch25", 10, "geometric equality in the figure")
ref("ch25", [11, 12], "fringe count for a thickness or index change in double pass: 2(n-1) dt/lambda, 2 dn t/lambda")
nv("ch25", [13, 14], "Hartmann-type ratio relations of the figure; the symbols eta, xi, p, g, S are defined only in the figure")
ref("ch25", [15, 16, 17, 18], "Fraunhofer diffraction as a 2-D Fourier transform with u = 2 pi x/(lambda s)")

# ---------------- ch26 evaluation-phase tests ----------------
ref("ch26", 1, "empirical root-sum-square combination of resolution limits")
defn("ch26", [2, 3, 4], "KDC efficiency and contrast definitions")
ref("ch26", [5, 6, 7], "imaging as convolution with the spread function; transfer function = its Fourier transform")
defn("ch26", 8, "sinusoidal test-object luminance")
x = np.linspace(0, 1, 4001)
sq = np.sign(np.cos(2 * np.pi * x))
ser = 4 / np.pi * sum((-1) ** k / (2 * k + 1) * np.cos((2 * k + 1) * 2 * np.pi * x) for k in range(400))
num("ch26", 9, lambda: np.mean(np.abs(sq - ser)) < 0.01,
    "square-wave Fourier series 4/pi [cos - cos3/3 + cos5/5 - ...] reproduces a +-1 square wave (400 terms, mean error < 1%)")
defn("ch26", [10, 11], "square-wave (r) and sine-wave (R) response ratios")


def coltman():
    R = lambda nu: max(0.0, 1 - nu / 50.0)              # a test sine-wave response
    r = lambda nu: 4 / np.pi * sum((-1) ** k * R((2 * k + 1) * nu) / (2 * k + 1) for k in range(200))
    Rb = lambda nu: np.pi / 4 * (r(nu) + r(3 * nu) / 3 - r(5 * nu) / 5 + r(7 * nu) / 7 + r(11 * nu) / 11 - r(13 * nu) / 13 - r(15 * nu) / 15)
    return all(abs(Rb(nu) - R(nu)) < 0.01 for nu in (4.0, 6.0, 9.0, 12.0, 20.0))


num("ch26", [12, 13], coltman,
    "Coltman pair: Eq 11 applied to a test sine response, then Eq 12 (with Coltman's continuation of the series), recovers it to < 1%")
