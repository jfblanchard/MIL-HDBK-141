"""Book-convention paraxial trace (Eqs 5-56, 5-57):  y = y_-1 + (t_-1/n_-1)(n_-1 u_-1);  nu = n_-1 u_-1 + y c (n_-1 - n)."""
import numpy as np

# Table 6.6 three-element lens (the Taylor triplet used throughout ch05/06/10), object 25 units left of surface 1
T66 = dict(c=[0.25285, -0.01474, -0.19942, 0.25973, 0.05065, -0.24588],
           t=[25.0, 0.6, 1.06541, 0.15, 1.13691, 0.6, 14.05015],   # t0 (object->s1), gaps, t6 (s6->image)
           n=[1.0, 1.62, 1.0, 1.621, 1.0, 1.62, 1.0])


def trace(c, t, n, y0, nu0):
    """Returns per-surface y (surfaces 1..k) and nu after each surface; last entry = image-plane y."""
    ys, nus = [], []
    y, nu = y0, nu0
    for j, cj in enumerate(c):
        y = y + t[j] / n[j] * nu
        nu = nu + y * cj * (n[j] - n[j + 1])
        ys.append(y); nus.append(nu)
    y_img = y + t[len(c)] / n[len(c)] * nu
    return np.array(ys), np.array(nus), y_img

