#!/usr/bin/env python3
"""Final story-facing normalization for the generated Chapters 0-3 reader.

This is deliberately narrow and runs after clean_exact_dialogue_reader.py. It fixes
reader headings that must never ship with production-language labels and verifies that
spoken dialogue is unchanged.
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
READER = ROOT / "build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx"
EXPECTED_DIALOGUE_LINES = 3440
LABEL_RE = re.compile(r"^.+:\s*$")

HEADING_REPLACEMENTS = {
    "working royal audience": "Royal Audience",
}
FORBIDDEN_HEADING_PATTERNS = (
    re.compile(r"^working\s+royal\s+audience$", re.IGNORECASE),
    re.compile(r"^c\d+\s+function$", re.IGNORECASE),
)


def is_heading(paragraph) -> bool:
    return bool(paragraph.style and paragraph.style.name and paragraph.style.name.startswith("Heading"))


def is_dialogue(paragraph) -> bool:
    if not paragraph.runs:
        return False
    first = paragraph.runs[0]
    if not first.bold or not LABEL_RE.match(first.text):
        return False
    label = first.text.strip()[:-1].strip()
    return bool(re.search(r"[A-Z]", label)) and label == label.upper()


def replace_text(paragraph, text: str) -> None:
    if paragraph.runs:
        paragraph.runs[0].text = text
        for run in paragraph.runs[1:]:
            run.text = ""
    else:
        paragraph.add_run(text)


def main() -> int:
    if not READER.exists():
        raise RuntimeError(f"Generated reader does not exist: {READER.relative_to(ROOT)}")

    document = Document(READER)
    dialogue_before = [p.text for p in document.paragraphs if is_dialogue(p)]
    if len(dialogue_before) != EXPECTED_DIALOGUE_LINES:
        raise RuntimeError(
            f"Reader has {len(dialogue_before)} spoken lines; expected {EXPECTED_DIALOGUE_LINES}."
        )

    changed = 0
    for paragraph in document.paragraphs:
        if not is_heading(paragraph):
            continue
        key = paragraph.text.strip().casefold()
        replacement = HEADING_REPLACEMENTS.get(key)
        if replacement is not None:
            replace_text(paragraph, replacement)
            changed += 1

    dialogue_after = [p.text for p in document.paragraphs if is_dialogue(p)]
    if dialogue_before != dialogue_after:
        raise RuntimeError("Final reader heading normalization altered spoken dialogue.")

    forbidden = [
        p.text.strip()
        for p in document.paragraphs
        if is_heading(p)
        and any(pattern.search(p.text.strip()) for pattern in FORBIDDEN_HEADING_PATTERNS)
    ]
    if forbidden:
        raise RuntimeError(f"Forbidden production-facing reader headings remain: {forbidden}")

    document.save(READER)
    print(
        f"Final reader heading normalization complete; {changed} heading(s) normalized and "
        f"{len(dialogue_after)} spoken lines preserved exactly."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
