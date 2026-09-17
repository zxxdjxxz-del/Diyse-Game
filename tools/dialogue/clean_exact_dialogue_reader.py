#!/usr/bin/env python3
"""Remove writer/gameplay-facing prose from the generated Chapters 0–3 reader.

The dialogue synchronizer intentionally derives its DOCX from the atomic dialogue files.
Those atomics also contain production-facing prose. This post-generation cleanup removes
that presentation metadata from the reader while preserving every spoken dialogue
paragraph in the exact same order and wording.
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
READER = ROOT / "build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx"

FULL_SKIP_HEADING_TERMS = (
    "production draft",
    "dialogue engine production draft",
    "person-brain",
    "role-balance note",
    "performance note",
    "performance check",
    "audit note",
    "audit check",
    "knowledge check",
    "knowledge checkpoint",
    "world-state checkpoint",
    "continuity note",
    "current production state",
    "conflict order",
    "gameplay",
    "optional gameplay",
    "boss handoff",
    "presentation check",
    "character check",
    "reveal-boundary check",
)

DROP_PROSE_PHRASES = (
    "player",
    "implementation",
    "encounter authority",
    "story authority",
    "authority owns",
    "field model",
    "field models",
    "portrait",
    "dialogue box",
    "presentation",
    "animation",
    "cutscene",
    "choreography",
    "targeting",
    "tuning",
    "rewards",
    "exact mechanics",
    "hp bar",
    "random-encounter",
    "random encounter",
    "tutorial",
    "production",
    "authored",
    "scripted",
    "dialogue layer",
    "dialogue manuscript",
    "story state",
    "visible controllable",
    "commandable party",
    "party field",
    "current mandatory objective",
    "standard jrpg confirmation",
    "area implementation",
    "no elaborate",
    "no bespoke",
    "is required",
    "are required",
    "required.",
    "required visual",
    "required traversal section",
    "no new required combat",
    "is needed",
    "are needed",
    "needed.",
    "as much as needed",
    "does not require",
    "not required",
    "not needed",
    "may appear",
    "may be visible",
    "may be present",
    "may already be",
    "may occur",
    "control returns",
    "control resumes",
    "control pauses",
    "control begins",
    "gameplay",
    "handoff",
    "story trigger",
    "scene trigger",
    "departure trigger",
    "trigger fires",
    "objective",
    "prop routine",
    "prop animation",
    "equipment animation",
    "weapon-ready pose",
    "the scene ends",
    "scene ends",
    "the exchange ends",
    "the scene is allowed",
    "this is a genuine medical/travel question",
    "this is a normal authored boss encounter",
    "this is an authored boss encounter",
    "this is boss animation",
    "battle presentation",
    "combat proceeds under",
    "battle event",
    "exact defeat animation",
    "mid-battle dialogue",
    "the joke benefits",
    "the opening stays quick",
    "stays quick because",
    "chapter 1 owns",
    "chapter 2 owns",
    "chapter 3 owns",
    "chapter-1 owns",
    "chapter-2 owns",
    "production/encounter name",
    "writer-facing",
    "person-brain",
    "role-balance",
)

DROP_EXACT_PREFIXES = (
    "Scene ends.",
    "The scene ends",
    "Gameplay continues",
    "Gameplay resumes",
    "Story Handoff",
    "Handoff —",
    "Chapter-",
    "Pipeline:",
    "Current mandatory objective:",
    "Transition into:",
    "Objective:",
)

FILEPATH_RE = re.compile(r"^(?:docs|build|tools)/[A-Za-z0-9_./\-]+$")
DIALOGUE_PREFIX_RE = re.compile(r"^.+:\s*$")


def is_heading(paragraph) -> bool:
    return bool(
        paragraph.style
        and paragraph.style.name
        and paragraph.style.name.startswith("Heading")
    )


def is_dialogue(paragraph) -> bool:
    if not paragraph.runs:
        return False
    first = paragraph.runs[0]
    return bool(first.bold and DIALOGUE_PREFIX_RE.match(first.text))


def remove_paragraph(paragraph) -> None:
    element = paragraph._element
    element.getparent().remove(element)
    paragraph._p = paragraph._element = None


def replace_paragraph_text(paragraph, text: str) -> None:
    for run in paragraph.runs:
        run.text = ""
    if paragraph.runs:
        paragraph.runs[0].text = text
    else:
        paragraph.add_run(text)


def clean_heading_text(text: str) -> str:
    cleaned = text.strip()
    patterns = (
        r"^Story Trigger\s*[—-]\s*",
        r"\s*[—-]\s*Story Trigger$",
        r"^Final Push\s*[—-]\s*Story Trigger$",
        r"\s*[—-]\s*Optional Character-Life Trigger$",
        r"^Optional Character-Life Trigger\s*[—-]\s*",
        r"^Camp\s*[—-]\s*Optional Character-Life Trigger$",
        r"^Authored Stop\s*[—-]\s*",
        r"^Scripted Battle Event\s*[—-]\s*",
        r"\s*[—-]\s*Player Preparation Window$",
        r"^Authored(?:\s+Combat|\s+Opening|\s+Disengagement)?\s*[—-]?\s*",
    )
    for pattern in patterns:
        updated = re.sub(pattern, "", cleaned, flags=re.IGNORECASE).strip(" —-")
        if updated != cleaned:
            cleaned = updated or "Camp"
    return cleaned


def should_drop_prose(text: str, skip_non_dialogue: bool) -> bool:
    stripped = text.strip()
    low = stripped.lower()
    if not stripped:
        return False
    if skip_non_dialogue:
        return True
    if FILEPATH_RE.match(stripped):
        return True
    if any(stripped.startswith(prefix) for prefix in DROP_EXACT_PREFIXES):
        return True
    if low.startswith("pipeline:"):
        return True
    if any(phrase in low for phrase in DROP_PROSE_PHRASES):
        return True
    if low.startswith(
        (
            "rehearsal-first ",
            "dialogue engine ",
            "person-brain ",
            "production ",
            "gameplay ",
            "story trigger ",
        )
    ):
        return True
    return low in {"scene ends", "scene ends."}


def main() -> int:
    if not READER.exists():
        raise RuntimeError(f"Generated reader does not exist: {READER.relative_to(ROOT)}")

    document = Document(READER)
    dialogue_before = [p.text for p in document.paragraphs if is_dialogue(p)]

    skip_non_dialogue = False
    for index, paragraph in enumerate(list(document.paragraphs)):
        text = paragraph.text.strip()

        # Preserve the title/subtitle/explanatory note on the cover page.
        if index <= 2:
            continue

        if is_heading(paragraph):
            low = text.lower()
            cleaned = clean_heading_text(text)
            cleaned_low = cleaned.lower()

            # Story labels wrapped in production language are retained under a clean title.
            if cleaned != text and cleaned and "player preparation window" not in cleaned_low:
                skip_non_dialogue = False
                replace_paragraph_text(paragraph, cleaned)
                continue

            if any(term in low for term in FULL_SKIP_HEADING_TERMS) or "guided traversal dialogue" in low:
                remove_paragraph(paragraph)
                skip_non_dialogue = True
                continue

            if "handoff" in low or low.startswith("pipeline:"):
                remove_paragraph(paragraph)
                skip_non_dialogue = False
                continue

            skip_non_dialogue = False
            continue

        # Spoken lines are inviolable. The cleaner may remove prose around them, never the line.
        if is_dialogue(paragraph):
            continue

        if should_drop_prose(text, skip_non_dialogue):
            remove_paragraph(paragraph)

    dialogue_after = [p.text for p in document.paragraphs if is_dialogue(p)]
    if dialogue_before != dialogue_after:
        raise RuntimeError(
            "Reader cleanup changed spoken dialogue; refusing to save "
            f"({len(dialogue_before)} before vs {len(dialogue_after)} after)."
        )

    document.save(READER)
    print(
        f"Reader presentation cleanup complete; preserved {len(dialogue_after)} spoken dialogue lines exactly."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
