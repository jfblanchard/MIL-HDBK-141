"""Automatic arithmetic check: in any display block whose '=' / '\\approx' chain contains two or more
purely numeric members, evaluate them and confirm they agree to the precision the book printed.

A numeric member is one that sympy's LaTeX parser turns into an expression with no free symbols.
Tolerance: half a unit in the last printed decimal of the *rounder* of the two members, plus a
0.5 % allowance for intermediate rounding the book carried (hand computation, 4-6 figures).
"""
import re, json, warnings
from pathlib import Path
from sympy.parsing.latex import parse_latex
import sympy as sp

warnings.filterwarnings("ignore")
HERE = Path(__file__).parent

CLEAN = [
    (r"\\tag\{[^}]*\}", ""), (r"\\text\{[^}]*\}", ""), (r"\\mathrm\{([^}]*)\}", r"\1"),
    (r"\\(,|;|!|quad|qquad)", " "), (r"\\left|\\right", ""), (r"\\displaystyle", ""),
    (r"\\dfrac|\\tfrac", r"\\frac"), (r"\{,\}", ""), (r"\\cdot", r"\\times"),
    (r"(\d)\s*\\times\s*10\^\{?(-?\d+)\}?", r"(\1*10^{\2})"),
]


def split_chain(tex):
    """Split on top-level '=' and '\\approx' (not inside braces)."""
    parts, depth, cur, i = [], 0, "", 0
    while i < len(tex):
        c = tex[i]
        if c in "{(":
            depth += 1
        elif c in "})":
            depth -= 1
        if depth == 0 and tex.startswith(r"\approx", i):
            parts.append(cur); cur = ""; i += 7; continue
        if depth == 0 and c == "=":
            parts.append(cur); cur = ""; i += 1; continue
        cur += c
        i += 1
    parts.append(cur)
    return [p.strip(" .,;") for p in parts]


def printed_step(s):
    """Rounding step implied by a printed number, e.g. '2.54' -> 0.005."""
    nums = re.findall(r"\d+\.(\d+)", s)
    if len(re.findall(r"[\d.]+", s)) == 1 and nums:
        return 0.5 * 10 ** (-len(nums[0]))
    return 0.0


def numeric(seg):
    if not re.search(r"\d", seg) or re.search(r"[a-zA-Z]", re.sub(r"\\(frac|sqrt|times|pi|sin|cos|tan|log|ln|exp|circ|arctan|arcsin)", "", seg)):
        if not re.search(r"\\(sin|cos|tan|pi|sqrt)", seg):
            return None
    try:
        e = parse_latex(seg.replace(r"^\circ", r"*\pi/180"))
    except Exception:
        return None
    if isinstance(e, sp.Basic) and not e.free_symbols:
        try:
            v = complex(e.evalf())
            return v.real if abs(v.imag) < 1e-12 else None
        except Exception:
            return None
    return None


def check(tex):
    t = tex.replace("\n", " ")
    for a, b in CLEAN:
        t = re.sub(a, b, t)
    if r"\begin" in t:
        return None
    segs = split_chain(t)
    vals = [(s, numeric(s)) for s in segs]
    nums = [(s, v) for s, v in vals if v is not None]
    if len(nums) < 2:
        return None
    out = []
    for (s1, v1), (s2, v2) in zip(nums, nums[1:]):
        tol = max(printed_step(s1), printed_step(s2)) + 0.005 * max(abs(v1), abs(v2)) + 1e-12
        ok = abs(v1 - v2) <= tol
        out.append((ok, f"{s1.strip()} -> {v1:.6g} vs {s2.strip()} -> {v2:.6g}"))
    return out


if __name__ == "__main__":
    eqs = json.load(open(HERE / "equations.json"))
    res = {}
    for e in eqs:
        r = check(e["latex"])
        if r:
            res[e["id"]] = r
    json.dump(res, open(HERE / "auto_numeric.json", "w"), indent=1)
    bad = {k: v for k, v in res.items() if not all(ok for ok, _ in v)}
    print(len(res), "blocks with numeric chains;", len(bad), "disagree")
    for k, v in bad.items():
        print(k, [m for ok, m in v if not ok])
