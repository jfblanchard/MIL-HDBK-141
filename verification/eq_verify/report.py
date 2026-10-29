"""Write verification/EQUATION_VERIFICATION.md from the ledger.  Run: env -u PYTHONPATH python report.py"""
import re
from collections import Counter, defaultdict
from pathlib import Path
import run_all  # noqa: F401  (imports every ck_*.py and runs the deferred checks)
import ledger

OUT = Path(__file__).resolve().parents[1] / "EQUATION_VERIFICATION.md"
ORDER = ["VERIFIED", "FIXED", "DEFINITION", "FLAG", "NOT VERIFIED"]


def eq_type(e, r):
    if r["result"] == "DEFINITION":
        return "definition"
    body = re.sub(r"\\tag\{[^}]*\}", "", e["latex"])
    if len(re.findall(r"\d+\.\d+", body)) >= 2 or "°" in body:
        return "worked example"
    return "relation"


def cell(s):
    return s.replace("|", "\\|").replace("\n", " ")


rows, by_ch = [], defaultdict(Counter)
for k in sorted(ledger.EQS):
    e, r = ledger.EQS[k], ledger.LEDGER[k]
    tag = f" ({e['tag']})" if e["tag"] else ""
    rows.append(f"| {k}{tag} | {e['ch'][2:]} | {eq_type(e, r)} | {r['method']} | {r['result']} | {cell(r['note'])} |")
    by_ch[e["ch"]][r["result"]] += 1
tot = Counter(r["result"] for r in ledger.LEDGER.values())
xtot = Counter(x["result"] for x in ledger.EXTRA.values())
flags = {k: r for k, r in ledger.LEDGER.items() if r["result"] == "FLAG"}
sic = sorted(k for k, r in flags.items() if "sic" in r["note"])
fid = sorted(k for k, r in flags.items() if r["note"].startswith("FIDELITY"))
other = sorted(set(flags) - set(sic) - set(fid))

L = ["# MIL-HDBK-141 Equation Verification Ledger", "",
     "Every display equation (`$$...$$`) in `ocr_output/chNN.md`, checked from the transcribed LaTeX. "
     "Scan pages were opened only where a check disagreed with the text and the cause (transcription vs. 1962 print) "
     "had to be settled; those rows say `+ scan` in the method column.", "",
     "Checks are executable: `verification/eq_verify/ck_chNN.py` (one module per chapter group), registry `ledger.py`, "
     "run with `env -u PYTHONPATH python run_all.py`; this file is written by `report.py`.", "",
     "## Methods", "",
     "- **symbolic (sympy)**: the equation is derived from its predecessors, or both sides are shown identical (symbolic zero, "
     "with a random-rational numeric fallback).",
     "- **numeric (book values)**: the book's own worked numbers are recomputed; or, for ch21 coatings, the book's recursions are "
     "compared with an independent characteristic-matrix reference (`multilayer.py`, Macleod convention) on 12 random absorbing "
     "stacks at oblique incidence.",
     "- **reference (standard form)**: checked term by term against the established textbook form.",
     "- **definition**: defines a symbol, convention, or boundary condition; nothing to derive.", "",
     "## Results", "",
     "- **VERIFIED**: the check ran and the equation holds.",
     "- **FIXED**: a transcription error found by the check, corrected against the scan in an earlier commit, and re-verified.",
     "- **FLAG**: a real discrepancy. Notes marked `1962 ORIGINAL (sic ...)` are errors in the printed book, confirmed on the scan "
     "and kept as printed; notes marked `FIDELITY` are ch05 transcription paraphrases that do not match the book.",
     "- **NOT VERIFIED**: no check possible from the text (reason given).", "",
     "## Source corrections already committed (re-verified here)", "",
     "- `0b840e3` ch06: A/B linearity coefficients, Eq 32 sign, Eq 33a, secondary-spectrum 1/2200 statement (6 rows, FIXED).",
     "- `96b8d4b` ch16 Eq 167: restored `n` in the J1 argument denominator (row ch16-p51-207, FIXED).",
     "- `fcc9a85` ch21: render fix only (duplicate `\\tag` on Eq 113); no content change.", "",
     "## Per-chapter summary", "",
     "| ch | blocks | " + " | ".join(ORDER) + " |", "|---|---|" + "---|" * len(ORDER)]
for ch in sorted(by_ch):
    c = by_ch[ch]
    L.append(f"| {ch[2:]} | {sum(c.values())} | " + " | ".join(str(c[o]) for o in ORDER) + " |")
L.append(f"| **all** | **{sum(tot.values())}** | " + " | ".join(f"**{tot[o]}**" for o in ORDER) + " |")
L += ["", "## Errors in the 1962 original (kept as printed)", ""]
for k in sic:
    L.append(f"- `{k}`: {ledger.LEDGER[k]['note']}")
L += ["", "## Supplementary checks (book equations not present as display blocks)", "",
      "| id | ch | method | result | notes |", "|---|---|---|---|---|"]
for k, x in sorted(ledger.EXTRA.items()):
    L.append(f"| {k} | {x['ch'][2:]} | {x['method']} | {x['result']} | {cell(x['note'])} |")
L += ["", "## Ledger", "", "| Eq id | chapter | type | method | result | notes |", "|---|---|---|---|---|---|"] + rows
checked = tot["VERIFIED"] + tot["FIXED"]
L += ["", "## Totals", "",
      f"- Display blocks: **{sum(tot.values())}** (all accounted for).",
      f"- VERIFIED {tot['VERIFIED']} · FIXED {tot['FIXED']} · DEFINITION {tot['DEFINITION']} · FLAG {tot['FLAG']} · "
      f"NOT VERIFIED {tot['NOT VERIFIED']}.",
      f"- Checked and holding (VERIFIED + FIXED): **{checked}**; plus {tot['DEFINITION']} definitions = "
      f"{checked + tot['DEFINITION']} of {sum(tot.values())} clean.",
      f"- FLAG breakdown: {len(sic)} rows are confirmed 1962 print errors; {len(fid)} are ch05 transcription-fidelity "
      f"problems; {len(other)} other ({', '.join(other)}).",
      f"- Supplementary: {len(ledger.EXTRA)} rows ({xtot['VERIFIED']} VERIFIED, {xtot['FLAG']} FLAG).", ""]
OUT.write_text("\n".join(L))
print(OUT, dict(tot), "sic", len(sic), "fidelity", len(fid))
