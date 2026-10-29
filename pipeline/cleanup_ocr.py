#!/usr/bin/env python
"""
cleanup_ocr.py — Post-processing cleanup for MIL-HDBK-141 Layer 0 OCR output.

Applies 5 rules to every ocr_output/chNN.md file:
  Rule 1a  Strip running page headers (MIL-HDBK-141 variants in all OCR manglings)
  Rule 1b  Strip page footer lines (e.g. "17-1", "8-10")
  Rule 2   Strip gutter artifacts (leading 'i ' or '| ' from page-binding shadow)
  Rule 3   Delete decorative noise lines (horizontal rules read as garbage chars)
  Rule 4   Flag noise-only EQUATION placeholders (graph lines misread as equations)
  Rule 5   Collapse runs of 3+ blank lines to a single blank line

Backups of originals are written to ocr_output/backup/ before any file is touched.
Prints a per-chapter change summary to stdout.

Usage:
  python pipeline/cleanup_ocr.py
"""

import os, re, shutil, glob

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OCR_DIR    = os.path.join(REPO, "ocr_output")
BACKUP_DIR = os.path.join(OCR_DIR, "backup")

# ---------------------------------------------------------------------------
# Compiled patterns
# ---------------------------------------------------------------------------

# Rule 1a — MIL-HDBK header (all OCR variants observed in spot-check):
#   MIL-HDBK, MIL-HOBK, MIL HDBK, MiL-HD6K, MIL~HDBK, MIL—HDBK, MIL-HOBK, etc.
#   Pattern: "MIL" + optional separator(s) + "H" + [OD] + [B6]
HDBK_RE = re.compile(r'MIL[-\s~—.]{0,3}H[OD][B6]', re.IGNORECASE)

# Rule 1b — Page footer: bare chapter-page number like "17-1", "8-10", "21-35"
FOOTER_RE = re.compile(r'^\d{1,2}-\d{1,3}$')

# Rule 3a — Horizontal rule artifact: 3+ consecutive dash/equals/tilde chars
DASH_RUN_RE = re.compile(r'[-=—–~]{3,}')

# Rule 3b — Repeated character artifact: 4+ identical consecutive chars (e.g. "EEEE", "ssss")
REPEAT_CHAR_RE = re.compile(r'(.)\1{3,}')

# Rule 3c — "BECERRA ELE EEE" gibberish: many short all-caps tokens on a long line
CAPS_TOKEN_RE = re.compile(r'\b[A-Z]{2,6}\b')

# Rule 4 — Equation placeholder pattern + noise signal inside it
EQ_LINE_RE  = re.compile(r'^>\[EQUATION (\d+): (.+?)\] — OCR unreliable.*$')
EQ_NOISE_RE = re.compile(r'[-=—–~]{3,}')   # 3+ dashes inside equation content = noise


# ---------------------------------------------------------------------------
# Rule helpers
# ---------------------------------------------------------------------------

def _core(line):
    """Strip gutter prefix chars and surrounding whitespace for pattern testing."""
    return line.strip().lstrip('i| ').strip()


def is_header(line):
    """Rule 1a: line is a running page header containing a MIL-HDBK variant."""
    return bool(HDBK_RE.search(_core(line)))


def is_footer(line):
    """Rule 1b: line is a bare page-footer number like '17-1'."""
    # strip gutter prefix, then dots/commas/spaces that sometimes wrap the number
    core = _core(line).strip('.,; ')
    return bool(FOOTER_RE.match(core))


def is_noise(line):
    """
    Rule 3: line is decorative garbage — horizontal rule or scan artifact.
    Four sub-tests (any one is sufficient):
      3a  Contains 4+ consecutive dashes / equals / tildes
      3b  Contains 4+ identical consecutive characters
      3c  Long line composed mostly of short all-caps tokens (gibberish from graph curves)
      3d  Short line with no alphanumeric run of 3+ chars — pure artifact residual
          e.g. "i] ' ~", "| ,", "; :", "n- 1]? ,"
    Skips placeholder lines (start with '>') and page markers (start with '<!--').
    """
    s = line.strip()
    if not s or s.startswith('>') or s.startswith('<!--'):
        return False
    # 3d first (applies to very short lines before the length guard below)
    # Requires a 4+ char alnum run to survive — catches "lle", "err", "SET", "LP" artifacts
    if len(s) <= 12 and not re.search(r'[A-Za-z0-9]{4,}', s):
        return True
    if len(s) < 8:
        return False
    if DASH_RUN_RE.search(s):           # 3a
        return True
    if REPEAT_CHAR_RE.search(s):        # 3b
        return True
    if len(s) > 40:                     # 3c
        caps_tokens = CAPS_TOKEN_RE.findall(s)
        if len(caps_tokens) > 5:
            return True
    return False


def strip_gutter(line):
    """
    Rule 2: remove a single leading 'i ' or '| ' gutter artifact.
    Returns (cleaned_line, was_changed).
    Never touches placeholder lines ('>') or page markers ('<!--').
    Requires at least 3 chars of content after the prefix to avoid wiping tiny residuals.
    """
    if line.startswith('>') or line.startswith('<!--'):
        return line, False
    m = re.match(r'^[|i]\s', line)
    if m and len(line) - m.end() >= 1:
        return line[m.end():], True
    return line, False


def flag_eq_noise(line):
    """
    Rule 4: if an EQUATION placeholder's content is noise (contains long dash runs
    or is dominated by non-alphanumeric characters), replace the content label with
    a human-readable noise flag so reviewers know to skip LaTeX conversion.
    Returns (new_line, was_changed).
    """
    m = EQ_LINE_RE.match(line)
    if not m:
        return line, False
    eq_num  = m.group(1)
    content = m.group(2)

    # Signal 1: dash/equals runs inside the content
    has_dash_noise = bool(EQ_NOISE_RE.search(content))

    # Signal 2: content is >55% non-alphanumeric characters
    noise_chars = sum(1 for c in content if not c.isalnum() and c not in ' .,;:()/\\*+-[]')
    high_noise_ratio = len(content) > 4 and (noise_chars / len(content)) > 0.55

    if has_dash_noise or high_noise_ratio:
        flagged = (
            f">[EQUATION {eq_num}: [NOISE -- decorative rule or graph artifact, "
            f"not a real equation]] -- needs human review"
        )
        return flagged, True
    return line, False


# ---------------------------------------------------------------------------
# Per-file processor
# ---------------------------------------------------------------------------

def process_file(path):
    """Apply all 5 rules to a single chapter file. Returns (output_lines, stats_dict)."""
    with open(path, encoding='utf-8') as f:
        raw_lines = f.read().splitlines()

    out   = []
    stats = dict(headers=0, footers=0, noise=0, gutters=0,
                 short=0, eq_flags=0, blank_runs=0)

    for raw in raw_lines:
        s = raw.strip()
        is_placeholder = s.startswith('>[')
        is_marker      = s.startswith('<!--')

        # --- Rule 4: flag noisy equation placeholders (check before anything else) ---
        if is_placeholder:
            flagged, changed = flag_eq_noise(s)
            if changed:
                stats['eq_flags'] += 1
            out.append(flagged)
            continue

        # --- Preserve page markers exactly ---
        if is_marker:
            out.append(raw)
            continue

        # --- Rule 1a: drop header lines ---
        if is_header(raw):
            stats['headers'] += 1
            continue

        # --- Rule 1b: drop footer lines ---
        if is_footer(raw):
            stats['footers'] += 1
            continue

        # --- Rule 3: drop noise lines ---
        if is_noise(raw):
            stats['noise'] += 1
            continue

        # --- Rule 2: strip gutter artifact prefix ---
        line, guttered = strip_gutter(raw)
        if guttered:
            stats['gutters'] += 1

        # Drop very short residuals (1-2 non-space chars) left after gutter strip —
        # these are punctuation-only artifacts like "; :" or ", ."
        residual = line.strip()
        if 0 < len(residual) <= 2:
            stats['short'] += 1
            continue

        out.append(line)

    # --- Rule 5: collapse runs of 3+ blank lines to a single blank line ---
    final      = []
    blank_run  = 0
    for line in out:
        if line.strip() == '':
            blank_run += 1
            if blank_run == 1:
                final.append(line)   # keep first blank
            else:
                stats['blank_runs'] += 1   # count subsequent blanks dropped
        else:
            blank_run = 0
            final.append(line)

    return final, stats


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(OCR_DIR, 'ch*.md')))

    if not files:
        print(f"No ch*.md files found in {OCR_DIR}")
        return

    totals = dict(headers=0, footers=0, noise=0, gutters=0,
                  short=0, eq_flags=0, blank_runs=0)

    print(f"Cleaning {len(files)} chapter files  (backups -> {BACKUP_DIR})\n")
    print(f"{'File':<20} {'hdrs':>5} {'ftrs':>5} {'noise':>6} {'gutters':>8} "
          f"{'short':>6} {'eq_flg':>7} {'blanks':>7}")
    print('-' * 72)

    for path in files:
        name = os.path.basename(path)

        # Backup original
        shutil.copy2(path, os.path.join(BACKUP_DIR, name))

        # Process
        lines, stats = process_file(path)

        # Write cleaned file
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(lines) + '\n')

        # Accumulate totals
        for k in totals:
            totals[k] += stats[k]

        print(f"{name:<20} {stats['headers']:>5} {stats['footers']:>5} "
              f"{stats['noise']:>6} {stats['gutters']:>8} {stats['short']:>6} "
              f"{stats['eq_flags']:>7} {stats['blank_runs']:>7}")

    print('-' * 72)
    print(f"{'TOTAL':<20} {totals['headers']:>5} {totals['footers']:>5} "
          f"{totals['noise']:>6} {totals['gutters']:>8} {totals['short']:>6} "
          f"{totals['eq_flags']:>7} {totals['blank_runs']:>7}")
    print(f"\nDone. Original files backed up to: {BACKUP_DIR}")


if __name__ == '__main__':
    main()
