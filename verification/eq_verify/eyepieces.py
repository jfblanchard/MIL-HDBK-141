"""Parse the nine eyepiece prescriptions (ch14 Tables 14.1-14.9) and trace them paraxially.

Table convention (ch14 §14.2.1): rows are surfaces listed from the exit-pupil (eye) side; t and glass
are for the space AFTER the surface; the last t is the distance from the last surface to the field stop
(eyepiece focal plane). Glass code 517645 -> n_d = 1.517, nu = 64.5.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def glass_n(code):
    m = re.match(r"\s*(\d{6})", code)
    return 1.0 + int(m.group(1)[:3]) / 1000.0 if m else 1.0


def parse_ch14():
    text = (ROOT / "ocr_output/ch14.md").read_text()
    out = {}
    for m in re.finditer(r"\*\*Table (14\.\d) — Lens constants for the (.+?) eyepiece\.\*\*(.+?)\$\\Sigma P = (-?[\d.]+)\$, \$\\gamma = ([\d.]+)\$", text, re.S):
        tid, name, body, sp, g = m.groups()
        rows = []
        for line in body.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 3 and re.match(r"^[−\-]?[\d.]+$", cells[0]):
                c = float(cells[0].replace("−", "-"))
                t = None if cells[1] in ("—", "-") else float(cells[1])
                rows.append((c, t, cells[2]))
        out[tid] = dict(name=name, rows=rows, sigmaP=float(sp), gamma=float(g))
    return out


def system(rows):
    """-> list of (c, t_after, n_before, n_after)."""
    s, n_prev = [], 1.0
    for c, t, glass in rows:
        n_after = glass_n(glass) if glass not in ("—", "-") and not glass.startswith("Air") else 1.0
        s.append((c, t, n_prev, n_after))
        n_prev = n_after
    return s


def paraxial(rows):
    """Parallel ray from the eye side: EFL, back focal distance from the last surface, Petzval sum (eye side)."""
    y, nu, first_y = 1.0, 0.0, 1.0
    surf = system(rows)
    for k, (c, t, n0, n1) in enumerate(surf):
        nu = nu + y * c * (n0 - n1)
        if k < len(surf) - 1:
            y = y + t / n1 * nu
    u = nu / surf[-1][3]
    efl = -first_y / u
    bfd = -y / u
    petz = sum(c * (n1 - n0) / (n0 * n1) for c, t, n0, n1 in surf)
    return efl, bfd, petz


if __name__ == "__main__":
    for tid, d in parse_ch14().items():
        efl, bfd, p = paraxial(d["rows"])
        print(tid, d["name"], f"EFL={efl:.4f} BFD={bfd:.4f} lastT={d['rows'][-1][1]} SigmaP(obj side)={-p:.4f} printed={d['sigmaP']} "
              f"gamma={-1 / (efl * -p):.3f} printed={d['gamma']}")
