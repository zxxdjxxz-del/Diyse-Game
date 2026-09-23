#!/usr/bin/env python3
"""Restore the approved world intro and currently validated encounter bridges to the Ch0-3 reader.

Run after presentation cleanup/heading normalization and before layout repair.
All 2,038 spoken lines are immutable.
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.shared import Pt

ROOT = Path(__file__).resolve().parents[2]
READER = ROOT / "build/dialogue/DIYSE_Chapters_0-3_Spoiler_Free_Exact_Dialogue_Reader_CURRENT.docx"
INTRO = ROOT / "docs/04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md"
CH0 = ROOT / "docs/02_STORY/CHAPTERS/CHAPTER_00.md"
CH1 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_01.md"
CH2 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_02.md"
CH3 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_03.md"
PLACEMENT = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CURRENT_PLACEMENT_AND_RESOLUTION_CORRECTIONS_2026-09-12.md"
FORMATIONS = ROOT / "game/content/encounters/chapter_01_04_formations.gd"

EXPECTED_DIALOGUE_LINES = 2038
LABEL_RE = re.compile(r"^.+:\s*$")

# target heading, inserted heading, body paragraphs, owning source, required authority terms
# Chapter 3 encounter bridges are intentionally omitted until its enemy placement is migrated to the revised 15-beat story structure.
BRIDGES = (
    ("Cyanis Solo", "Opening Ambush", (
        "Combat 1 — Cyanis solo: Black Host Raider + Black Host Crossbowman.",
        "Combat 2 — Cyanis solo: Black Host Raider + Ruin Shieldbearer.",
        "Combat 3 — Cyanis solo: 2 Convoy Rift Hounds.",
        "Chapter 0 uses authored/tutorial encounters rather than the normal random-encounter cadence.",
    ), CH0, ("Black Host Raider", "Black Host Crossbowman", "Ruin Shieldbearer", "2 Convoy Rift Hounds")),
    ("Hound Pressure", "Wreck Field", (
        "Combat 4 — Cyanis solo: Black Host Crossbowman + Convoy Rift Hound.",
        "Combat 5 — Cyanis solo: one lone Convoy Rift Hound threatening the survivor route.",
    ), CH0, ("Black Host Crossbowman + Convoy Rift Hound", "one lone Convoy Rift Hound")),
    ("The Pursuer", "Concealed Ruin Vanguard", (
        "Combat party: Cyanis + Ilyra.",
        "Enemy: Ruin Vanguard Pursuer. The pursuer's identity remains unknown to the party.",
    ), CH0, ("Ruin Vanguard Pursuer",)),
    ("Final Push", "Broken Convoy", (
        "Combat party: Cyanis + Ilyra.",
        "Boss encounter: Riftmaw + Convoy War-Sorcerer.",
    ), CH0, ("Riftmaw", "Convoy War-Sorcerer")),

    ("Halfway Stop", "Random Encounters — Northern Briar Passage", (
        "Greenhollow Stalker • Thornvine Creeper • Briar Boar",
    ), CH1, ("Greenhollow Stalker", "Thornvine Creeper", "Briar Boar")),
    ("Hollow Watch Reveal", "Random Encounters — Greenhollow / Hollow Watch Approach", (
        "Greenhollow Stalker • Thornvine Creeper • Briar Boar",
    ), CH1, ("Greenhollow Stalker", "Thornvine Creeper", "Briar Boar")),
    ("Garrison Discovery", "Random Encounters — Hollow Watch", (
        "Black Host Raider • Black Host Crossbowman • Ruin Shieldbearer • Hollow Watch Sentry • Hollow Watch Ballista • Watch Captain Frame",
    ), CH1, ("Black Host Raider", "Black Host Crossbowman", "Ruin Shieldbearer", "Hollow Watch Sentry", "Hollow Watch Ballista", "Watch Captain Frame")),
    ("First Clear Sighting", "Random Encounters — Southern Briar", (
        "Greenhollow Stalker • Thornvine Creeper • Briar Boar • Needlewing • Rootmaw • Brambleback",
    ), CH1, ("Greenhollow Stalker", "Thornvine Creeper", "Briar Boar", "Needlewing", "Rootmaw", "Brambleback")),

    ("Sealed Side Door", "Random Encounters — Old Waterworks", (
        "Bogshell • Cistern Leech • Needlewing",
    ), CH2, ("Bogshell", "Cistern Leech", "Needlewing")),
    ("Threshold", "Random Encounters — Sunken Archive", (
        "Archive Current • Memory Scribe • Hollow Watch Sentry • Bogshell • Cistern Leech • Needlewing",
    ), CH2, ("Archive Current", "Memory Scribe", "Hollow Watch Sentry", "Bogshell", "Cistern Leech", "Needlewing")),
    ("The Alarm", "Random Encounters — Old Bastion", (
        "Bastion Shield Guard • Bastion Crossbow Guard • Transfer Adept • Black Host Raider",
    ), CH2, ("Bastion Shield Guard", "Bastion Crossbow Guard", "Transfer Adept", "Black Host Raider")),

)

FORMATION_AREAS = (
    "ch01_greenhollow",
    "ch01_hollow_watch",
    "ch01_briar_south",
    "ch02_dunmere_waterworks",
    "ch02_sunken_archive",
    "ch02_red_transfer_bastion",
)


def is_dialogue(paragraph) -> bool:
    if not paragraph.runs:
        return False
    first = paragraph.runs[0]
    if not first.bold or not LABEL_RE.match(first.text):
        return False
    label = first.text.strip()[:-1].strip()
    return bool(re.search(r"[A-Z]", label)) and label == label.upper()


def find_heading(document: Document, text: str):
    matches = [
        p for p in document.paragraphs
        if p.style and p.style.name.startswith("Heading") and p.text.strip() == text
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one heading {text!r}; found {len(matches)}")
    return matches[0]


def intro_text() -> list[str]:
    raw = INTRO.read_text(encoding="utf-8")
    marker = "## The World of Diyse"
    if marker not in raw:
        raise RuntimeError("World intro reader section is missing")
    body = raw.split(marker, 1)[1]
    out = []
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            break
        out.append(line.replace("**", "").replace("*", "").replace(chr(96), ""))
    if not out or out[-1] != "If I catch you using it as one, we're going to have a conversation.":
        raise RuntimeError("World intro no longer ends on Nimera's approved sign-off")
    return out


def validate_authority() -> None:
    formation_text = FORMATIONS.read_text(encoding="utf-8")
    placement = PLACEMENT.read_text(encoding="utf-8")
    for area in FORMATION_AREAS:
        if f'"{area}"' not in formation_text:
            raise RuntimeError(f"Expected encounter formation area missing: {area}")

    if "NO PLAYABLE MANDATORY CHAPTER-3 ROAD STRETCH" not in placement:
        raise RuntimeError("Chapter-3 no-road-combat firewall is missing")
    if "Redwater Initiate" not in placement or "Do not place it automatically" not in placement:
        raise RuntimeError("Waterworks Redwater placement firewall is missing")
    if "HOLD THE JUNCTION IS RETIRED" not in placement:
        raise RuntimeError("Hold-the-Junction retirement firewall is missing")

    cache = {}
    for _target, title, body, owner, needles in BRIDGES:
        owner_text = cache.setdefault(owner, owner.read_text(encoding="utf-8"))
        for needle in needles:
            if needle not in owner_text:
                raise RuntimeError(f"{title}: current owning authority no longer contains {needle!r}")
        joined = " ".join(body)
        if title == "Random Encounters — Old Waterworks" and "Redwater Initiate" in joined:
            raise RuntimeError("Redwater Initiate must not be auto-placed in Waterworks")
        if title.startswith("Random Encounters —") and "Way-Fort" in joined:
            raise RuntimeError("Way-Fort enemies must not be placed on the current mandatory Chapter-3 route")


def main() -> int:
    validate_authority()
    document = Document(READER)
    before = [p.text for p in document.paragraphs if is_dialogue(p)]
    if len(before) != EXPECTED_DIALOGUE_LINES:
        raise RuntimeError(f"Reader has {len(before)} spoken lines; expected {EXPECTED_DIALOGUE_LINES}")

    for paragraph in document.paragraphs[:12]:
        text = paragraph.text.strip()
        if text == "Spoiler-Free Exact-Dialogue Reader":
            paragraph.runs[0].text = "Spoiler-Free Story & Gameplay Read-Through — Exact Dialogue"
        elif text.startswith("Current atomic dialogue edition."):
            paragraph.runs[0].text = (
                "Current Chapters 0–3 read-through. Spoken lines are copied verbatim from the active "
                "atomic dialogue sources; current world and gameplay bridges are restored from their "
                "owning authorities; writer-facing production notes are omitted."
            )

    chapter0 = find_heading(document, "Chapter 0")
    heading = chapter0.insert_paragraph_before("The World of Diyse", style="Heading 1")
    heading.paragraph_format.space_after = Pt(8)
    for text in intro_text():
        p = chapter0.insert_paragraph_before(text)
        p.paragraph_format.space_after = Pt(7)
    chapter0.paragraph_format.page_break_before = True

    for target_text, title, body, _owner, _needles in BRIDGES:
        target = find_heading(document, target_text)
        h = target.insert_paragraph_before(title, style="Heading 3")
        h.paragraph_format.space_before = Pt(7)
        h.paragraph_format.space_after = Pt(3)
        for text in body:
            p = target.insert_paragraph_before(text)
            p.paragraph_format.space_after = Pt(3)

    after = [p.text for p in document.paragraphs if is_dialogue(p)]
    if after != before or len(after) != EXPECTED_DIALOGUE_LINES:
        raise RuntimeError("Reader enrichment altered spoken dialogue")

    document.save(READER)
    print(
        f"Reader enrichment complete: world intro + {len(BRIDGES)} encounter bridges; "
        f"{len(after)} spoken lines preserved exactly."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
