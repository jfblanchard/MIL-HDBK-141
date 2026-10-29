# LLM Exchanges — MIL-HDBK-141

This folder holds prompts sent to external LLMs and their responses,
used as a scientific validation layer on top of the main VLM pass.

---

## Workflow

```
1. Claude (Sonnet) does full VLM pass on a chapter:
   - Corrects ocr_output/chNN.md
   - Enriches gems in analysis/LOST_GEMS_CATALOG.md
   - Writes chapter summary

2. Claude writes a timestamped validation prompt:
   exchanges/YYYYMMDD_chNN_validate_prompt.md

3. User pastes prompt into external LLM (e.g. DeepSeek v4 Flash)

4. User saves the response as:
   exchanges/YYYYMMDD_chNN_validate_response.md

5. Claude reads the response, checks findings, incorporates
   confirmed corrections, dismisses false positives, commits.
```

---

## File naming convention

```
YYYYMMDD_chNN_validate_prompt.md    ← prompt sent to external LLM
YYYYMMDD_chNN_validate_response.md  ← external LLM's reply
```

Example:
```
20260825_ch01_validate_prompt.md
20260825_ch01_validate_response.md
```

If a chapter needs a follow-up round (e.g. a disputed equation):
```
20260825_ch01_validate_prompt_r2.md
20260825_ch01_validate_response_r2.md
```

---

## What the validator is asked to do

The validation prompt instructs the external LLM to:

1. **Check equations** — verify each LaTeX equation against optical
   engineering first principles and standard references (Hecht, Smith,
   Kingslake, Born & Wolf). Flag any that look wrong or suspicious.

2. **Check gem claims** — verify each rule of thumb / formula / data
   table. Is the stated range / approximation / criterion correct?
   Any important caveats missing?

3. **Check chapter summary** — is it accurate, complete, and fair
   to the chapter content?

4. **Output format** — structured PASS / FLAG / QUERY per item,
   with brief justification. Flagged items get a suggested correction.

---

## What the validator is NOT asked to do

- Transcribe from scan images (it can't see them)
- Rewrite or reformat the content
- Verify OCR prose accuracy (that's Claude's job from the scan)

---

## Editorial notes / validation summary

The external LLM (Gemini) may maintain a running editorial notes and validation
summary document across chapters. If so, note its filename in this README when
known, and Claude will check it at the start of each session for accumulated
findings and patterns.

---

## External LLM used

- **Gemini 3.7 Flash High** (via Windsurf Cascade) — primary scientific validator
- Other models may be used for specific tasks (noted in prompt file)
