"""Verification registry. Chapter modules (ck_chNN.py) call these to record a method + result for
display blocks, addressed by chapter and in-chapter sequence number K (the -KKK suffix of the id).

Results:
  VERIFIED      the check ran and the equation holds (symbolic identity, book numbers reproduce,
                or matches an independently known standard form, inspected term by term)
  DEFINITION    defines a symbol / states a convention or a boundary condition; nothing to derive
  FLAG          the check found a discrepancy (reason in notes)
  NOT VERIFIED  no check performed (reason in notes)
"""
import json, traceback
from pathlib import Path
import sympy as sp

HERE = Path(__file__).parent
EQS = {e["id"]: e for e in json.load(open(HERE / "equations.json"))}
BY_CK = {(e["ch"], int(e["id"].rsplit("-", 1)[1])): e["id"] for e in EQS.values()}
LEDGER = {}


def _ids(ch, ks):
    if isinstance(ks, int):
        ks = [ks]
    out = []
    for k in ks:
        if isinstance(k, tuple):  # inclusive range
            out += [BY_CK[(ch, j)] for j in range(k[0], k[1] + 1)]
        else:
            out.append(BY_CK[(ch, k)])
    return out


def put(ch, ks, method, result, note):
    for i in _ids(ch, ks):
        LEDGER[i] = dict(method=method, result=result, note=note)


def run(fn):
    """Run a check function; True -> pass, False/exception -> fail (with message)."""
    try:
        r = fn()
        if isinstance(r, sp.Basic):
            r = bool(sp.simplify(r) == 0)
        return bool(r), ""
    except Exception as ex:  # a crashing check is a failed check, never a pass
        return False, f"check raised {type(ex).__name__}: {ex}"


def zero(expr):
    """Symbolic zero test with a numeric fallback at random points."""
    e = sp.simplify(expr)
    if e == 0:
        return True
    import random
    syms = list(e.free_symbols)
    for _ in range(6):
        sub = {s: sp.Rational(random.randint(11, 97), random.randint(7, 31)) for s in syms}
        v = complex(e.subs(sub).evalf())
        if abs(v) > 1e-9:
            return False
    return True


def close(a, b, rel=0.005, abs_=0.0):
    a, b = float(a), float(b)
    return abs(a - b) <= max(rel * max(abs(a), abs(b)), abs_)


PENDING = []


def finalize():
    """Run deferred checks (lets a module register a check above the helper it calls)."""
    while PENDING:
        PENDING.pop(0)()


def sym(ch, ks, fn, note):
    PENDING.append(lambda: _sym(ch, ks, fn, note))
    put(ch, ks, "symbolic (sympy)", "NOT VERIFIED", "pending")


def _sym(ch, ks, fn, note):
    ok, msg = run(fn)
    put(ch, ks, "symbolic (sympy)", "VERIFIED" if ok else "FLAG", note if ok else f"{note} -- CHECK FAILED {msg}")


def num(ch, ks, fn, note):
    PENDING.append(lambda: _num(ch, ks, fn, note))
    put(ch, ks, "numeric (book values)", "NOT VERIFIED", "pending")


def _num(ch, ks, fn, note):
    ok, msg = run(fn)
    put(ch, ks, "numeric (book values)", "VERIFIED" if ok else "FLAG", note if ok else f"{note} -- CHECK FAILED {msg}")


def ref(ch, ks, note):
    put(ch, ks, "reference (standard form)", "VERIFIED", note)


def defn(ch, ks, note="definition / convention"):
    put(ch, ks, "reference (definition)", "DEFINITION", note)


def flag(ch, ks, method, note):
    put(ch, ks, method, "FLAG", note)


def nv(ch, ks, reason):
    put(ch, ks, "none", "NOT VERIFIED", reason)


EXTRA = {}


def extra(rid, ch, method, ok, note):
    """Supplementary row for a book equation verified from the scan (not a transcription block)."""
    EXTRA[rid] = dict(ch=ch, method=method, result="VERIFIED" if ok else "FLAG", note=note)
