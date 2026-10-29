import importlib, glob, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import ledger
for m in sorted(glob.glob(str(Path(__file__).parent / "ck_*.py"))):
    importlib.import_module(Path(m).stem)
ledger.finalize()
if __name__ == "__main__":
    from collections import Counter
    print(len(ledger.LEDGER), "of", len(ledger.EQS), Counter(v["result"] for v in ledger.LEDGER.values()))
    for k, v in sorted(ledger.LEDGER.items()):
        if v["result"] == "FLAG": print("FLAG", k, v["note"][:200])
