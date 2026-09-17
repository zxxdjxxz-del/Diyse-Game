#!/usr/bin/env python3
"""Clean the generated Chapters 0–3 reader without changing spoken dialogue."""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
READER = ROOT / "build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx"
DIALOGUE_PREFIX_RE = re.compile(r"^.+:\s*$")

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

DROP_EXACT = {
    "Cyanis and Ilyra are now the active combat pair.",
    "There is a real noncombat interval here.",
    "No immediate boss sting. No continuous Card ward. No second flare yet.",
    "Maevra's splint remains part of her visible Chapter-1 state.",
    "Available during the Chapter-3 cleanup window after Beat 15.",
}

PROSE_REWRITES = {
    "After the encounter, the convoy officer reaches Cyanis's side of the wreck field.":
        "After the fighting eases, the convoy officer reaches Cyanis's side of the wreck field.",
    "The Card remains inert for the entire encounter.": "The Card remains inert.",
    "Riftmaw and the War-Sorcerer are defeated in the same encounter.":
        "Riftmaw and the War-Sorcerer fall together.",
    "The final boss encounter is over.": "The fighting is over.",
    "After a short post-boss exploration stretch, the Ancient route narrows near a section where later construction presses against the older structure.":
        "After a short exploration stretch, the Ancient route narrows near a section where later construction presses against the older structure.",
    "Nimera enters combat without a recruitment discussion or order.":
        "Nimera joins the fight without discussion.",
    "No new Card event occurs. Cyanis's Card remains stable deep Ruby and put away.":
        "Cyanis's Card remains stable deep Ruby and put away.",
    "The fight is lethal. The party defeats and kills the Briarhide Stalker through ordinary combat victory.":
        "The fight is lethal. The party kills the Briarhide Stalker.",
    "BATTLE — ARCHIVE SCRIBE ENGINE": "The Archive Scribe Engine activates.",
    "Current atomic dialogue edition. Spoken lines are copied verbatim from active production sources; writer-facing audits, implementation notes, and future-facing production metadata are omitted.":
        "Current atomic dialogue edition. Spoken lines are copied verbatim from the active source scenes; writer-facing notes and future-facing metadata are omitted.",
}

HEADING_EXACT = {
    "Noncombat Reset — Triage Line": "Triage Line",
    "Mid-Battle Transition — Tears Free": "Tears Free",
    "Boss Victory": "After the Battle",
    "Boss Combat — Briarhide Stalker": "Briarhide Stalker",
    "Optional Content — Available From Camp": "Camp",
    "Boss Battle — First Command Warden": "First Command Warden",
    "Optional Character-Life — Cresthaven Supply Room": "Cresthaven Supply Room",
    "Mandatory Interaction — Rest / Advance": "Rest / Advance",
    "Party Join": "Nimera Joins",
    "Return To Cleanup": "Back to Cresthaven",
}

HEADING_REMOVE = {
    "P04 end state",
    "P05 end state",
    "P06 end state",
    "P07 end state",
    "System / Party State",
    "Beat-1 end state",
    "Beat End",
    "Scene seed",
    "Boss Combat",
    "Boss Combat — Integrated State",
    "Boss Combat — Mobile State",
    "Battle Character",
}

PRODUCTION_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"^\s*(?:Combat\s+\d+:|ACTIVE COMBAT PAIR:|BOSS COMBAT BEGINS|Permanent combat party:|Combat party:|Encounter-direction priorities:)",
        r"^\s*Combat continues\b",
        r"^\s*The party defeats it through normal boss combat\.",
        r"^\s*Maevra remains (?:a non-combat traveling companion|outside the battle party)\.",
        r"^\s*No (?:concealed Ruin Vanguard|Riftmaw|Card flare|added transformation or hidden meaning)\b",
        r"\bencounter-authorized\b",
        r"\bcurrent Chapter-\d+ story specifically\b",
        r"\bNeither fills the pause simply because dialogue is available\b",
        r"\bnoncombat reset from P05\b",
        r"\bsingle combined final boss encounter\b",
        r"\bNo explanatory dialogue fires\b",
        r"\bchapter moves back to people\b",
        r"^\s*Riftmaw and the Convoy War-Sorcerer are defeated in the combined final encounter\.",
        r"^\s*No more dialogue follows\.",
        r"\bThat is enough to establish\b",
        r"\boff the main dialogue beat\b",
        r"\bnormal Chapter-1 field state\b",
        r"\bdialogue does not repeat\b",
        r"^\s*Current atomic dialogue source\b",
        r"^\s*CHAPTER \d+ END\.$",
        r"\boptional and do not block progression\b",
        r"\bdoes not reset him to\b",
        r"\bone-word quota\b",
        r"\bvisible traversal model\b",
        r"\bsparse practical dialogue is legal\b",
        r"^\s*Short dialogue may cover the work:$",
        r"^\s*Boss encounter begins\.$",
        r"^\s*Beat \d+ ends here\b",
        r"^\s*Beat \d+ begins immediately\b",
        r"^\s*Optional short battle barks\b",
        r"\bnot mandatory timed dialogue beats\b",
        r"\bpost-battle medical check\b",
        r"\bdoes not mount another boss encounter\b",
        r"^\s*No new combat begins\.",
        r"\bnot skipped because the boss is over\b",
        r"\bdoes not automatically advance into Chapter\b",
        r"^\s*Do not create a separate\b",
        r"^\s*Beat \d+\s*[—-]\s*",
        r"^\s*Permanent combat-capable roster\b",
        r"\bNo playable road dungeon\b",
        r"\bcurrent Chapter-3 cleanup window\b",
        r"\bmajor Ancient authority confrontation of Chapter 3\b",
        r"\bIts battle identity should feel\b",
        r"^\s*The following dialogue is speech-only over active battle:$",
        r"\bsame health bar\b",
        r"\bcombat continues immediately\b",
        r"\bthe scene does not stop for a medical explanation\b",
        r"\bplayer\b",
        r"\bimplementation\b",
        r"\bencounter authority\b",
        r"\bstory authority\b",
        r"\bfield model\b",
        r"\bportrait\b",
        r"\bdialogue box\b",
        r"\bcutscene\b",
        r"\bchoreography\b",
        r"\brandom[- ]encounter\b",
        r"\btutorial\b",
        r"\bproduction\b",
        r"\bperson-brain\b",
        r"\brole-balance\b",
        r"\bgameplay\b",
    )
)


def is_heading(paragraph) -> bool:
    return bool(paragraph.style and paragraph.style.name and paragraph.style.name.startswith("Heading"))


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
    if paragraph.runs:
        paragraph.runs[0].text = text
        for run in paragraph.runs[1:]:
            run.text = ""
    else:
        paragraph.add_run(text)


def clean_heading(text: str) -> str | None:
    text = text.strip()
    if text in HEADING_REMOVE:
        return None
    if text in HEADING_EXACT:
        return HEADING_EXACT[text]

    for pattern in (
        r"^Major Story Interaction\s*[—-]\s*",
        r"^Short Story Stop\s*[—-]\s*",
        r"^Story Continuation\s*[—-]\s*",
        r"^Direct Cut\s*[—-]\s*",
        r"^Travel Cut\s*[—-]\s*",
        r"^Continuation\s*[—-]\s*",
        r"^Beat End\s*[—-]\s*",
        r"^Story Trigger\s*[—-]\s*",
        r"\s*[—-]\s*Story Trigger$",
        r"\s*[—-]\s*Optional Character-Life Trigger$",
        r"^Optional Character-Life Trigger\s*[—-]\s*",
        r"^Authored Stop\s*[—-]\s*",
        r"^Scripted Battle Event\s*[—-]\s*",
        r"^Authored(?:\s+Combat|\s+Opening|\s+Disengagement)?\s*[—-]?\s*",
    ):
        changed = re.sub(pattern, "", text, flags=re.IGNORECASE).strip(" —-")
        if changed != text:
            text = changed or "Camp"

    low = text.lower()
    if low in {"beat end", "scene seed"}:
        return None
    if any(term in low for term in FULL_SKIP_HEADING_TERMS) or "guided traversal dialogue" in low:
        return None
    if "handoff" in low or low.startswith("pipeline:"):
        return None
    return text


def should_drop_prose(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if stripped in DROP_EXACT:
        return True
    return any(pattern.search(stripped) for pattern in PRODUCTION_PATTERNS)


def main() -> int:
    if not READER.exists():
        raise RuntimeError(f"Generated reader does not exist: {READER.relative_to(ROOT)}")

    document = Document(READER)
    dialogue_before = [p.text for p in document.paragraphs if is_dialogue(p)]

    skip_non_dialogue = False
    for index, paragraph in enumerate(list(document.paragraphs)):
        text = paragraph.text.strip()

        if index <= 2:
            if text in PROSE_REWRITES:
                replace_paragraph_text(paragraph, PROSE_REWRITES[text])
            continue

        if is_heading(paragraph):
            cleaned = clean_heading(text)
            low = text.lower()
            if cleaned is None:
                remove_paragraph(paragraph)
                skip_non_dialogue = any(term in low for term in FULL_SKIP_HEADING_TERMS)
                continue
            skip_non_dialogue = False
            if cleaned != text:
                replace_paragraph_text(paragraph, cleaned)
            continue

        if is_dialogue(paragraph):
            continue

        if text in PROSE_REWRITES:
            replace_paragraph_text(paragraph, PROSE_REWRITES[text])
            continue

        if skip_non_dialogue or should_drop_prose(text):
            remove_paragraph(paragraph)

    dialogue_after = [p.text for p in document.paragraphs if is_dialogue(p)]
    if dialogue_before != dialogue_after:
        raise RuntimeError(
            "Reader cleanup changed spoken dialogue; refusing to save "
            f"({len(dialogue_before)} before vs {len(dialogue_after)} after)."
        )

    document.save(READER)
    print(f"Reader presentation cleanup complete; preserved {len(dialogue_after)} spoken dialogue lines exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
