#!/usr/bin/env python3
"""Render ocr_output/ch01..ch27 into build/MIL-HDBK-141.pdf via pandoc + pdflatex.

Preprocessing (source files are never modified):
  - one numbered top-level heading per chapter (book numbering 1..26, appendix unnumbered);
    the chapters' own internal headings carry the book's numbers, so they are left unnumbered
  - page markers become small right-aligned "[ch-page]" tags (map back to docs/scans)
  - [FIGURE ...] placeholder blocks become framed "TBD" boxes; [TABLE/EQUATION/NOISE ...] stay blockquotes
  - top-of-chapter provenance lines (**Source/**VLM pass/**Summary:** ...) and terminal editorial
    sections (## Gems Verified / GEM ENRICHMENT / Lost Gems / work summaries) stay in the source
    as the work record but are not printed
  - every non-ASCII character gets a \\newunicodechar mapping so pdflatex never chokes

Usage: python3 build/build_pdf.py [chNN ...]   (default: all chapters 01-27)
"""
import re, subprocess, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "ocr_output", ROOT / "build"

TITLES = {
    1: "Introduction", 2: "Fundamentals of Geometrical Optics", 3: "Considerations of Physical Optics",
    4: "Visual Optics", 5: "Fundamental Methods of Ray Tracing", 6: "First Order Optics",
    7: "Simple Thin Lens Optical Systems", 8: "Aberration Analysis and Third Order Theory",
    9: "Method of Lens Design", 10: "An Application of the Method of Lens Design",
    11: "Telescope Objectives", 12: "Lens Relay Systems", 13: "Mirror and Prism Systems",
    14: "Eyepieces", 15: "Complete Telescope", 16: "Applications of Physical Optics",
    17: "Optical Material", 18: "Atmospheric Optics", 19: "Optics for Missile Tracking",
    20: "Applications of Thin Film Coatings", 21: "Coating of Optical Surfaces",
    22: "Infrared Optical Design", 23: "Microscope Optics", 24: "Design Phase Optical Tests",
    25: "Production Phase Optical Tests", 26: "Evaluation Phase Optical Tests",
}

# Known glyphs. \ensuremath makes them valid in text and math alike.
M = lambda s: r"\ensuremath{%s}" % s
UMAP = {
    "—": "---", "–": "--", "‘": "`", "’": "'", "“": "``", "”": "''", "°": M(r"^{\circ}"),
    "−": M("-"), "×": M(r"\times"), "±": M(r"\pm"), "·": M(r"\cdot"), "≈": M(r"\approx"),
    "≠": M(r"\neq"), "≤": M(r"\leq"), "≥": M(r"\geq"), "≡": M(r"\equiv"), "≫": M(r"\gg"),
    "≪": M(r"\ll"), "∝": M(r"\propto"), "∞": M(r"\infty"), "√": M(r"\surd"), "→": M(r"\rightarrow"),
    "←": M(r"\leftarrow"), "↑": M(r"\uparrow"), "↓": M(r"\downarrow"), "∴": M(r"\therefore"),
    "∑": M(r"\sum"), "∂": M(r"\partial"), "∫": M(r"\int"), "∬": M(r"\iint"), "′": M(r"^{\prime}"),
    "″": M(r"^{\prime\prime}"), "≷": M(r"\gtrless"), "⊕": M(r"\oplus"), "⊙": M(r"\odot"),
    "⊠": M(r"\boxtimes"), "⊞": M(r"\boxplus"), "△": M(r"\triangle"), "▽": M(r"\triangledown"),
    "○": M(r"\circ"), "◇": M(r"\diamond"), "ℓ": M(r"\ell"), "µ": M(r"\mu"), "Å": r"\AA{}",
    "§": r"\S{}", "©": r"\textcopyright{}", "®": r"\textregistered{}", "™": r"\texttrademark{}",
    "¢": r"\textcent{}", "£": r"\pounds{}", "¥": r"\textyen{}", "€": r"\texteuro{}",
    "«": r"\guillemotleft{}", "»": r"\guillemotright{}", "✓": M(r"\checkmark"), "✗": M(r"\times"),
    "ȳ": M(r"\bar{y}"), "Ȳ": M(r"\bar{Y}"), "ū": M(r"\bar{u}"), "Ā": M(r"\bar{A}"), "Ē": M(r"\bar{E}"),
    "◎": M(r"\circledcirc"), "◈": M(r"\diamond"), "̃": "", "̄": "",
    "ᵦ": M(r"_{\beta}"), "ᵥ": M(r"_{v}"), "ˣ": M(r"^{x}"), "ʲ": M(r"^{j}"), "ᵀ": M(r"^{T}"),
    "⁽": M("^{(}"), "⁾": M("^{)}"), "⁻": M("^{-}"), "₋": M("_{-}"), "ₖ": M("_{k}"), "ₐ": M("_{a}"),
    " ": "~",
}
GREEK = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon", "ζ": "zeta",
         "η": "eta", "θ": "theta", "κ": "kappa", "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi",
         "π": "pi", "ρ": "rho", "σ": "sigma", "τ": "tau", "φ": "phi", "χ": "chi", "ψ": "psi",
         "ω": "omega", "Γ": "Gamma", "Δ": "Delta", "Π": "Pi", "Σ": "Sigma", "Φ": "Phi"}
UMAP.update({k: M("\\" + v) for k, v in GREEK.items()})
UMAP.update({c: M("^{%d}" % i) for i, c in enumerate("⁰¹²³⁴⁵⁶⁷⁸⁹")})
UMAP.update({c: M("_{%d}" % i) for i, c in enumerate("₀₁₂₃₄₅₆₇₈₉")})

PAGE_RE = re.compile(r"<!--\s*=+\s*PAGE\s+(\d+)\s*=+\s*-->")
BLOCK_RE = re.compile(r"^\s*>?\s*\[(FIGURE|TABLE|EQUATION|NOISE)\b")
# Provenance/editorial material: kept in ocr_output/ as the work record, stripped from the book.
# Front-matter zone = lines between the chapter title and the first real book line:
# "**Key:**" meta lines (**Source:**, **VLM pass:**, **Summary:**, ...), bullet lists, rules, blanks.
FRONTSKIP_RE = re.compile(r"^\s*$|^---+\s*$|^\*\*[^*\n]{1,60}:\*\*|^[-*]\s")
EDITORIAL_RE = re.compile(r"^##\s+(?!\d)\S*.*(gem|enrich|transcri|summar|valid|reconcil|correct|verif)", re.I)
FIG_RE = re.compile(r"\[\s*FIGURE:?\s*(.*)\]\s*$", re.S)
FIGPAGE_RE = re.compile(r"^\s*page\s*(\d+)\s*(?:,\s*\d+\s*x\s*\d+\s*px)?\s*[—–\-:,]?\s*", re.I)
FIGNUM_RE = re.compile(r"((?:Figure|Fig\.?)\s*[0-9][\w.()\-]*)")
TRIM_RE = re.compile(r"^[\s—–\-:,]+|[\s—–\-:,]+$")


def tex_escape(s):
    """Escape LaTeX specials in plain text. Unicode glyphs are left alone —
    newunicodechar mappings in the header handle them globally."""
    return (s.replace("\\", r"\textbackslash{}")
             .replace("{", r"\{").replace("}", r"\}")
             .replace("&", r"\&").replace("%", r"\%").replace("$", r"\$")
             .replace("#", r"\#").replace("_", r"\_")
             .replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}"))


def fig_frame(block_lines):
    """Render a [FIGURE ...] placeholder as a framed TBD box (raw LaTeX block).
    Returns None if the block doesn't parse, so caller can fall back to a blockquote."""
    joined = " ".join(b.lstrip(">").lstrip() for b in block_lines)
    m = FIG_RE.search(joined)
    if not m:
        return None
    inner = m.group(1).strip()
    page = None
    pm = FIGPAGE_RE.match(inner)
    if pm:
        page = str(int(pm.group(1)))
        inner = inner[pm.end():]
    nm = FIGNUM_RE.search(inner)
    if nm:
        label = nm.group(1)
        desc = TRIM_RE.sub("", inner[:nm.start()]) + " " + TRIM_RE.sub("", inner[nm.end():])
        desc = desc.strip()
    else:
        label, desc = "Figure", TRIM_RE.sub("", inner)
    src = f"book p.\\ {page}" if page else "scan"
    lines = [
        "```{=latex}",
        r"\begin{center}\setlength{\fboxsep}{1.2em}%",
        r"\fbox{\begin{minipage}{0.82\linewidth}\centering\vspace{1.2em}",
        r"{\large\bfseries " + tex_escape(label) + r"}\\[0.4em]",
        r"{\footnotesize\sffamily TBD --- figure not yet generated (" + src + r")}\\[0.8em]",
    ]
    if desc:
        lines.append(r"{\small " + tex_escape(desc) + r"}")
    lines += [
        r"\vspace{1.2em}\end{minipage}}",
        r"\end{center}",
        "```",
        "",
    ]
    return lines


def unicode_header(text):
    lines = [r"\usepackage{newunicodechar}", r"\usepackage{textcomp}", r"\usepackage{amssymb}",
             r"\usepackage{gensymb}", r"\usepackage{etoolbox}\AtBeginEnvironment{quote}{\small\sffamily}", r"\newcommand{\pagetag}[2]{\par\hfill{\scriptsize\textsf{[#1-#2]}}\par}"]
    unmapped = []
    for ch in sorted({c for c in text if ord(c) > 127}):
        if unicodedata.category(ch) == "Ll" and ch in "éöóè":
            continue  # latin accents handled natively by inputenc
        if ch in "ÅÖ":
            continue
        rep = UMAP.get(ch)
        if rep is None:  # OCR garbage glyph: show code point instead of failing the build
            rep = r"\textsf{[U+%04X]}" % ord(ch)
            unmapped.append(ch)
        lines.append(r"\newunicodechar{%s}{%s}" % (ch, rep))
    return "\n".join(lines), unmapped


def convert_chapter(path, num):
    text = path.read_text()
    out = []
    if num in TITLES:
        out.append(f"# {TITLES[num]}\n")
    else:
        out.append("# Appendix {-}\n")
    lines = text.splitlines()
    i = 0
    front_done = False  # front-matter zone ends at the first real book line
    while i < len(lines):
        line = lines[i]
        m = PAGE_RE.search(line)
        if m:
            out.append(f"\n`\\pagetag{{{num}}}{{{int(m.group(1))}}}`{{=latex}}\n")
            i += 1
            continue
        if re.match(r"^#\s", line):  # the chapter's own title line: replaced by the injected heading
            i += 1
            continue
        if not front_done and i < 40:
            if FRONTSKIP_RE.match(line):  # **Key:** provenance lines, bullets, rules, blanks
                i += 1
                continue
            front_done = True
        if re.match(r"^#{2,6}\s", line):
            if EDITORIAL_RE.match(line) and not any(re.match(r"^##\s+\d", l) for l in lines[i + 1:]):
                break  # terminal editorial/validation appendix (gems, work summaries): keep in source, not in print
            out.append(line.rstrip() + " {-}")
            i += 1
            continue
        if BLOCK_RE.match(line):
            # gather the bracketed block (may span lines) until brackets balance
            block, depth = [], 0
            while i < len(lines):
                l = lines[i].lstrip()
                if not block:
                    l = l.lstrip(">").lstrip()
                depth += l.count("[") - l.count("]")
                block.append(l)
                i += 1
                if depth <= 0:
                    break
            if re.match(r"\s*\[NOISE", block[0]):
                continue  # OCR process commentary ("nothing here" markers): kept in source, not printed
            out.append("")
            frame = fig_frame(block) if re.match(r"\s*\[FIGURE", block[0]) else None
            if frame is not None:
                out.extend(frame)
            else:
                out.extend("> " + b for b in block)
            out.append("")
            continue
        out.append(line)
        i += 1
    body = "\n".join(out)
    # internal audit-trail paths and gem cross-refs: meaningful in the repo, not in print
    body = body.replace("; reconcile shortlist: exchanges/20260920_ch08_reconcile_SHORTLIST.md", "")
    body = re.sub(r"\s*\(exchanges/\S+\.md\)", "", body)
    body = re.sub(r"\s+and\s+GEM-[\d.]+", "", body)
    body = re.sub(r"\s*\bGEM-[\d.]+\b", "", body)
    # give every $$...$$ display its own paragraph so pandoc always reads it as display math
    body = re.sub(r"[ \t]*(\$\$.+?\$\$)[ \t]*", r"\n\n\1\n\n", body, flags=re.S)
    return body + "\n\n"


def chapter_files(sel):
    files = []
    for n in range(1, 28):
        p = SRC / (f"ch{n:02d}.md" if n < 27 else "ch27_apdx.md")
        if not sel or p.stem in sel or p.stem.split("_")[0] in sel:
            files.append((p, n))
    return files


def main():
    sel = set(sys.argv[1:])
    files = chapter_files(sel)
    body = "".join(convert_chapter(p, n) for p, n in files)
    header, unmapped = unicode_header(body)
    stem = "MIL-HDBK-141" if not sel else "partial_" + "_".join(sorted(sel))
    (OUT / f"{stem}.header.tex").write_text(header + "\n")
    (OUT / f"{stem}.md").write_text(body)
    cmd = ["pandoc", str(OUT / f"{stem}.md"), "-f", "markdown-implicit_figures-auto_identifiers-yaml_metadata_block-definition_lists-fancy_lists-example_lists-raw_tex-multiline_tables-simple_tables+tex_math_dollars",
           "-s", "-o", str(OUT / f"{stem}.tex"), "--pdf-engine=pdflatex", "--toc", "--toc-depth=1",
           "--number-sections", "--top-level-division=chapter", "-H", str(OUT / f"{stem}.header.tex"),
           "-V", "title=MIL-HDBK-141 — Optical Design (Modern Engineering Edition)",
           "-V", "author=1962 original / modern transcription", "-V", "documentclass=book",
           "-V", "classoption=oneside", "-V", "geometry=margin=1in", "-V", "fontsize=10pt",
           ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("pandoc exit:", r.returncode, r.stderr[-2000:])
    if r.returncode:
        return r.returncode
    # run pdflatex directly so its own exit code is reported; three passes settle the TOC
    for n in range(3):
        p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{stem}.tex"],
                           cwd=OUT, capture_output=True, text=True, errors="replace")
        print(f"pdflatex pass {n + 1} exit:", p.returncode)
        if p.returncode:
            err = [l for l in p.stdout.splitlines() if l.startswith("!") or l.startswith("l.")]
            print("\n".join(err[:20]))
            return p.returncode
    if unmapped:
        print("unmapped glyphs shown as [U+XXXX]:", " ".join(f"U+{ord(c):04X}" for c in unmapped))
    return 0


if __name__ == "__main__":
    sys.exit(main())
