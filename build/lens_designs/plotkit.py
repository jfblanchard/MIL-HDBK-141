"""Book-style Matplotlib plots for the Matplotlib-plot batch (ch16, ch20, ch25).

Same conventions as the OptiLand figures (common.py): Latin Modern type, black line art, 0.6 pt frame,
vector PDF + 600 dpi PNG, no in-figure title (the caption lives in the book), no grid, no colour.
`thinfilm` is a characteristic-matrix (Abeles) model used wherever the book's curve is a *computed*
thin-film result; measured curves are traced from the scan with `trace()`.
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).parent))
from common import BOOK_RC, INK, TEXT_WIDTH, save_book, write_readme  # noqa: E402,F401

plt.rcParams.update(BOOK_RC)
plt.rcParams.update({"axes.linewidth": 0.6, "xtick.direction": "in", "ytick.direction": "in",
                     "xtick.top": True, "ytick.right": True, "xtick.major.width": 0.5, "ytick.major.width": 0.5,
                     "xtick.major.size": 3, "ytick.major.size": 3, "xtick.minor.width": 0.4, "ytick.minor.width": 0.4,
                     "xtick.minor.size": 1.6, "ytick.minor.size": 1.6, "hatch.linewidth": 0.3, "legend.frameon": False})

CURVE = dict(color=INK, linewidth=0.8)
THINC = dict(color=INK, linewidth=0.5)
DASHED = dict(color=INK, linewidth=0.7, dashes=(5, 2))
DOTTED = dict(color=INK, linewidth=0.7, dashes=(1, 1.6))
LEAD = dict(arrowstyle="-", color=INK, linewidth=0.35, shrinkA=0, shrinkB=0)


def figure(width=4.8, height=3.1):
    fig, ax = plt.subplots(figsize=(width, height))
    return fig, ax


def axes_setup(ax, xlabel, ylabel, xlim, ylim, xticks=None, yticks=None, xfmt=None, yfmt=None, minor=None):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)
    if xfmt:
        ax.set_xticklabels([xfmt(v) for v in ax.get_xticks()])
    if yfmt:
        ax.set_yticklabels([yfmt(v) for v in ax.get_yticks()])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if minor:
        from matplotlib.ticker import MultipleLocator
        ax.xaxis.set_minor_locator(MultipleLocator(minor[0]))
        ax.yaxis.set_minor_locator(MultipleLocator(minor[1]))


def note(ax, text, xy, xytext=None, ha="center", va="center", size=7.5, **kw):
    """Text with an optional hairline leader to xy (data coords)."""
    if xytext is None:
        return ax.text(xy[0], xy[1], text, ha=ha, va=va, fontsize=size, **kw)
    return ax.annotate(text, xy, xytext, ha=ha, va=va, fontsize=size, arrowprops=LEAD, **kw)


def spread(values, min_sep):
    """Push sorted label positions apart so none are closer than min_sep (keeps order)."""
    v = np.array(values, dtype=float)
    idx = np.argsort(v)
    s = v[idx].copy()
    for _ in range(200):
        moved = False
        for i in range(1, len(s)):
            if s[i] - s[i - 1] < min_sep - 1e-12:
                mid = 0.5 * (s[i] + s[i - 1])
                s[i - 1], s[i] = mid - min_sep / 2, mid + min_sep / 2
                moved = True
        if not moved:
            break
    out = np.empty_like(s)
    out[idx] = s
    return out


def layer_inset(ax, rect, n1=None, ns=None, sub="Glass", ray_label=r"$\phi$", lam_note=None, ns_label=None,
                coated=True, size=6.5):
    """Small sketch of a ray hitting a single layer on a substrate (the figures' recurring inset)."""
    ia = ax.inset_axes(rect)
    ia.set_xlim(0, 15)
    ia.set_ylim(0, 7)
    ia.axis("off")
    ia.patch.set_alpha(0)
    x0, y0 = 7.25, 3.0
    arrow = dict(arrowstyle="-|>,head_length=0.4,head_width=0.16", color=INK, lw=0.5, shrinkA=0, shrinkB=0)
    inc = lambda t: (x0 - 1.7 + 1.7 * t, 5.9 - 2.9 * t)
    ref = lambda t: (x0 + 1.7 * t, y0 + 2.9 * t)
    ia.plot(*zip(inc(0), (x0, y0)), **THINC)
    ia.plot(*zip((x0, y0), ref(1)), **THINC)
    ia.annotate("", inc(0.5), inc(0.4), arrowprops=arrow)
    ia.annotate("", ref(0.7), ref(0.6), arrowprops=arrow)
    ia.plot([x0, x0], [y0, 6.5], color=INK, lw=0.4, dashes=(3, 2))
    ia.text(x0 - 0.5, 6.2, ray_label, fontsize=size, ha="right", va="center")
    ia.text(x0 + 2.4, 6.1, "Air", fontsize=size, ha="left", va="center")
    top = y0
    if coated:
        ia.add_patch(Rectangle((3.5, y0 - 0.45), 7.5, 0.45, fill=False, hatch="//////", lw=0.5, ec=INK))
        top = y0 - 0.45
    ia.add_patch(Rectangle((3.5, top - 1.2), 7.5, 1.2, fc="0.93", ec=INK, lw=0.5))
    ia.text(7.25, top - 0.6, ns_label or sub, fontsize=size, ha="center", va="center")
    if coated and n1 is not None:
        ia.text(11.3, y0 - 0.2, rf"$n_1 = {n1:.2f}$", fontsize=size, ha="left", va="center")
    if ns is not None:
        ia.text(11.3, top - 0.7, rf"$n_s = {ns:.2f}$", fontsize=size, ha="left", va="center")
    if lam_note:
        ia.text(0.1, 5.4, lam_note, fontsize=size, ha="left", va="center")
    return ia


def trace(pts, n=400, xs=None):
    """Shape-preserving (PCHIP) curve through control points read off the scan: returns xs, ys."""
    from scipy.interpolate import PchipInterpolator
    p = np.array(sorted(pts))
    if xs is None:
        xs = np.linspace(p[0, 0], p[-1, 0], n)
    return xs, PchipInterpolator(p[:, 0], p[:, 1])(xs)


def finish(fig, here, title, lines, flag=None):
    save_book(fig, Path(here) / Path(here).name)
    out = [f"# {title}", ""]
    if flag:
        out += [f"**{flag}**", ""]
    out += lines
    write_readme(Path(here) / "README.md", out)


# --- thin-film characteristic-matrix model -------------------------------------------------------
class thinfilm:
    @staticmethod
    def reflectance(n0, layers, ns, lam, phi0_deg, pol):
        """Reflectance R of a lossless stack. layers: [(n, d)] ordered from the incident medium n0 to the
        substrate ns, d in the same unit as lam. pol: 's', 'p' or 'av' (= (Rs+Rp)/2). Arrays broadcast over lam."""
        if pol == "av":
            return 0.5 * (thinfilm.reflectance(n0, layers, ns, lam, phi0_deg, "s")
                          + thinfilm.reflectance(n0, layers, ns, lam, phi0_deg, "p"))
        lam = np.asarray(lam, dtype=float)
        phi0_deg = min(phi0_deg, 89.9999)
        s0 = n0 * np.sin(np.radians(phi0_deg))

        def cosine(n):
            return np.sqrt(1 - (s0 / n) ** 2 + 0j)

        def eta(n):
            return n * cosine(n) if pol == "s" else n / cosine(n)

        m11, m12, m21, m22 = (np.ones_like(lam) + 0j, np.zeros_like(lam) + 0j,
                              np.zeros_like(lam) + 0j, np.ones_like(lam) + 0j)
        for n, d in layers:
            dl = 2 * np.pi * n * d * cosine(n) / lam
            c, s, e = np.cos(dl), np.sin(dl), eta(n)
            a11, a12, a21, a22 = c, 1j * s / e, 1j * e * s, c
            m11, m12, m21, m22 = (m11 * a11 + m12 * a21, m11 * a12 + m12 * a22,
                                  m21 * a11 + m22 * a21, m21 * a12 + m22 * a22)
        b = m11 + m12 * eta(ns)
        c = m21 + m22 * eta(ns)
        e0 = eta(n0)
        r = (e0 * b - c) / (e0 * b + c)
        return np.abs(r) ** 2


def load_trace(path):
    """Curves from a digitize trace.csv (rows: name, x, y) as {name: (x, y)} in file order."""
    out = {}
    for line in Path(path).read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        name, x, y = line.split(",")
        out.setdefault(name, ([], []))
        out[name][0].append(float(x))
        out[name][1].append(float(y))
    return {k: (np.array(v[0]), np.array(v[1])) for k, v in out.items()}
