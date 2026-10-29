"""Extract every $$...$$ display block with a stable id: chNN-pPP-K (K = order within chapter)."""
import re, json, glob
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
PAGE = re.compile(r"<!--\s*=+\s*PAGE\s+(\d+)\s*=+\s*-->")
def extract():
    rows = []
    for f in sorted(glob.glob(str(ROOT / "ocr_output/ch*.md"))):
        ch = Path(f).stem.split("_")[0]
        s = open(f).read()
        pages = [(m.start(), int(m.group(1))) for m in PAGE.finditer(s)]
        for k, m in enumerate(re.finditer(r"\$\$(.+?)\$\$", s, re.S), 1):
            pg = max([p for pos, p in pages if pos < m.start()] or [0])
            body = m.group(1).strip()
            tags = re.findall(r"\\tag\{([^}]*)\}", body)
            line = s.count("\n", 0, m.start()) + 1
            rows.append(dict(id=f"{ch}-p{pg:02d}-{k:03d}", ch=ch, page=pg, line=line,
                             tag=",".join(tags), latex=body))
    return rows
if __name__ == "__main__":
    rows = extract()
    json.dump(rows, open(Path(__file__).parent / "equations.json", "w"), indent=0)
    print(len(rows))
