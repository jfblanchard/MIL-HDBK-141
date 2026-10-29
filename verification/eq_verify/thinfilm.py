"""Normal-incidence characteristic-matrix thin-film calculator (independent reference for ch20/ch21).

Layer matrix (book ch20 Eq 8 form):  [[cos d, j sin d / n], [j n sin d, cos d]],  d = 2 pi n t / lambda.
Stack listed from the incidence side; substrate index ns, incident medium n0.
"""
import numpy as np


def layer(n, d):
    return np.array([[np.cos(d), 1j * np.sin(d) / n], [1j * n * np.sin(d), np.cos(d)]])


def stack(layers, g=1.0):
    """layers: list of (n, optical thickness in quarter waves at lambda0); g = lambda0/lambda."""
    M = np.eye(2, dtype=complex)
    for n, q in layers:
        M = M @ layer(n, q * np.pi / 2 * g)
    return M


def RT(M, n0, ns):
    B, C = M @ np.array([1.0, ns])
    r = (n0 * B - C) / (n0 * B + C)
    t = 2 * n0 / (n0 * B + C)
    return abs(r) ** 2, (ns / n0) * abs(t) ** 2


def book_RT(M, n0, ns, ks=0.0):
    """ch20 Eqs 9-11 with M = [[A, jB], [jC, D]]."""
    A, B, C, D = M[0, 0].real, M[0, 1].imag, M[1, 0].imag, M[1, 1].real
    X, U, Y, V = n0 * A + n0 * ks * B, ns * D, n0 * ns * B, C - ks * D
    R = ((X - U) ** 2 + (Y - V) ** 2) / ((X + U) ** 2 + (Y + V) ** 2)
    T = 4 / (2 + A ** 2 * n0 / ns + D ** 2 * ns / n0 + C ** 2 / (n0 * ns) + B ** 2 * n0 * ns)
    return R, T
