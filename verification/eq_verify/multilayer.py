"""Oblique-incidence multilayer optics in the book's ch21 conventions, plus an independent reference.

Book (ch21): fields ~ e^{-i w t}, complex index m = n(1 + iK), p0 = sin i0,
  M_v = (m_v^2 - m_0^2 p0^2)^{1/2}              (Eq 19; Im >= 0 branch, Eq 19a for evanescent)
  W_v = (M_{v-1} - M_v)/(M_{v-1} + M_v)          (Eq 20, E perpendicular to plane of incidence, 's')
  F_v = (m_v^2 M_{v-1} - m_{v-1}^2 M_v)/(m_v^2 M_{v-1} + m_{v-1}^2 M_v)   (Eq 21, H perpendicular, 'p')
  beta_v = 4 pi M_v d_v / lambda                  (Eq 56)
  rho_{v-1} = (rho_v e^{i beta_v} + W_v)/(1 + W_v rho_v e^{i beta_v}),  rho_N = W_{N+1}   (Eqs 50, 51)

Reference: Macleod's characteristic-matrix method written in the e^{+i w t}, N = n - ik convention
(so every book quantity enters conjugated). Nothing below the REFERENCE line uses a book formula.
"""
import numpy as np


def Mv(m, m0, p0):
    M = np.sqrt(m * m - (m0 * p0) ** 2 + 0j)
    return M if M.imag >= 0 else -M


def book(m, d, lam, p0, pol="s"):
    """m: [m0, m1..mN, m_{N+1}] complex; d: [d1..dN]. Returns rho0 (or gamma0), list of W/F, betas, Ms."""
    M = [Mv(x, m[0], p0) for x in m]
    if pol == "s":
        W = [None] + [(M[v - 1] - M[v]) / (M[v - 1] + M[v]) for v in range(1, len(m))]
    else:
        W = [None] + [(m[v] ** 2 * M[v - 1] - m[v - 1] ** 2 * M[v]) / (m[v] ** 2 * M[v - 1] + m[v - 1] ** 2 * M[v]) for v in range(1, len(m))]
    N = len(d)
    beta = [None] + [4 * np.pi * M[v] * d[v - 1] / lam for v in range(1, N + 1)]
    rho = W[N + 1]
    rhos = {N: rho}
    for v in range(N, 0, -1):
        e = np.exp(1j * beta[v])
        rho = (rho * e + W[v]) / (1 + W[v] * rho * e)
        rhos[v - 1] = rho
    return rho, W, beta, M, rhos


# ----------------------------- REFERENCE --------------------------------------------------------
def reference_RT(m, d, lam, p0, pol="s"):
    """Macleod characteristic matrix, e^{+iwt}; incident medium assumed non-absorbing."""
    N_ = [np.conj(x) for x in m]
    n0 = N_[0].real
    cos = [np.sqrt(1 - (n0 * p0 / x) ** 2 + 0j) for x in N_]
    cos = [c if (c * x).imag <= 0 else -c for c, x in zip(cos, N_)]   # decaying in the -i convention
    eta = [x * c for x, c in zip(N_, cos)] if pol == "s" else [x / c for x, c in zip(N_, cos)]
    Bm = np.eye(2, dtype=complex)
    for j in range(1, len(d) + 1):
        dl = 2 * np.pi * N_[j] * cos[j] * d[j - 1] / lam
        Bm = Bm @ np.array([[np.cos(dl), 1j * np.sin(dl) / eta[j]], [1j * eta[j] * np.sin(dl), np.cos(dl)]])
    B, C = Bm @ np.array([1, eta[-1]])
    r = (eta[0] * B - C) / (eta[0] * B + C)
    T = 4 * eta[0].real * eta[-1].real / abs(eta[0] * B + C) ** 2
    return abs(r) ** 2, T


def random_stack(rng, N, absorbing=True, p0=None):
    m = [1.0 + 0j] + [complex(rng.uniform(1.3, 2.4), rng.uniform(0, 0.08) if absorbing else 0) for _ in range(N)]
    m.append(complex(rng.uniform(1.4, 1.9), rng.uniform(0, 0.05) if absorbing else 0))
    d = list(rng.uniform(40, 400, N))
    return m, d, rng.uniform(400, 800), (rng.uniform(0, 0.8) if p0 is None else p0)
