#!/usr/bin/env python3
"""Restore the approved world intro and currently validated encounter bridges to the Ch0-3 reader.

Run after presentation cleanup/heading normalization and before layout repair.
All 2,015 spoken lines are immutable.
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.shared import Pt

ROOT = Path(__file__).resolve().parents[2]
READER = ROOT / "build/dialogue/DIYSE_Chapters_00-03_Spoiler_Free_Exact_Dialogue_Reader.docx"
INTRO = ROOT / "docs/04_WORLD_AND_LORE/PLAYER_FACING_WORLD_INTRO.md"
CH0 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_00.md"
CH1 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_01.md"
CH2 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_02.md"
CH3 = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/CHAPTER_ENEMIES/CHAPTER_03.md"
CH1_FORMATIONS = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_01_FORMATIONS.md"
CH2_FORMATIONS = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_02_FORMATIONS.md"
CH3_FORMATIONS = ROOT / "docs/09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_03_FORMATIONS.md"

EXPECTED_DIALOGUE_LINES = 2015
LABEL_RE = re.compile(r"^.+:\s*$")

# target heading, inserted heading, body paragraphs, owning source, required authority terms
BRIDGES = (
    ("Cyanis Solo", "Opening Ambush", (
        "Combat 1 — Cyanis solo: Black Host Raider + Black Host Crossbowman.",
        "Combat 2 — Cyanis solo: Black Host Raider + Black Host Shieldbearer.",
        "Combat 3 — Cyanis solo: 2 War Hounds.",
        "Chapter 0 uses authored/tutorial encounters rather than the normal random-encounter cadence.",
    ), CH0, ("Black Host Raider", "Black Host Crossbowman", "Black Host Shieldbearer", "2 War Hounds")),
    ("Hound Pressure", "Wreck Field", (
        "Combat 4 — Cyanis solo: Black Host Crossbowman + War Hound.",
        "Combat 5 — Cyanis solo: one lone War Hound threatening the survivor route.",
    ), CH0, ("Black Host Crossbowman + War Hound", "1 War Hound")),
    ("The Pursuer", "Concealed Ruin Vanguard", (
        "Combat party: Cyanis + Ilyra.",
        "Enemy: Ruin Vanguard Pursuer. The pursuer's identity remains unknown to the party.",
    ), CH0, ("Ruin Vanguard Pursuer",)),
    ("Final Push", "Broken Convoy", (
        "Combat party: Cyanis + Ilyra.",
        "Boss encounter: Riftmaw + Battle Sorcerer.",
    ), CH0, ("Riftmaw", "Battle Sorcerer")),

    ("Halfway Stop", "Enemy Roster — Northern Briar Passage", (
        "Thicket Stalker • Vine Creeper • Bullhog",
    ), CH1, ("Thicket Stalker", "Vine Creeper", "Bullhog")),
    ("Hollow Watch Reveal", "Enemy Roster — Hollow Watch Surface", (
        "Black Host Raider • Black Host Crossbowman • Black Host Shieldbearer",
    ), CH1, ("Black Host Raider", "Black Host Crossbowman", "Black Host Shieldbearer")),
    ("Garrison Discovery", "Hollow Watch Excavation Combat", (
        "Underground random encounters use Construct only.",
        "Shield Construct is a fixed authored stronger encounter; it is not random and not a miniboss.",
    ), CH1, ("Construct", "Shield Construct")),
    ("First Clear Sighting", "Boss — Thornhide", (
        "Thornhide",
    ), CH1, ("Thornhide",)),
    ("First Clear Sighting", "Enemy Roster — Southern Briar", (
        "Thicket Stalker • Vine Creeper • Bullhog • Needlewing • Burrowclaw • Barkling",
    ), CH1, ("Thicket Stalker", "Vine Creeper", "Bullhog", "Needlewing", "Burrowclaw", "Barkling")),

    ("Sealed Side Door", "Enemy Roster — Old Waterworks", (
        "Bogshell • Cistern Leech • Needlewing",
        "Later hot-runoff / steam / mineral sectors add Scaldback. Scaldback is an ordinary enemy, not a Regional Hunt.",
    ), CH2, ("Bogshell", "Cistern Leech", "Needlewing", "Scaldback")),
    ("Leviathan Chamber Approach", "Boss — Archive Leviathan", (
        "Archive Leviathan",
    ), CH2, ("Archive Leviathan",)),
    ("Threshold", "Enemy Roster — Sunken Archive", (
        "Bogshell • Cistern Leech • Needlewing • Arcdrift",
        "Arcdrift is the Archive-specific ordinary identity. Memory Scribe is retired from Chapter 2.",
    ), CH2, ("Bogshell", "Cistern Leech", "Needlewing", "Arcdrift")),
    ("The Alarm", "Enemy Roster — Old Bastion", (
        "Black Host Shieldbearer • Black Host Crossbowman • Battle Sorcerer • Black Host Raider • War Hound",
    ), CH2, ("Black Host Shieldbearer", "Black Host Crossbowman", "Battle Sorcerer", "Black Host Raider", "War Hound")),
    ("Authority", "Boss — Commander Rhazek — Bastion Master", (
        "Commander Rhazek — Bastion Master",
    ), CH2, ("Commander Rhazek", "Bastion Master")),

    ("Short Stop — Route Marks", "Enemy Roster — Lower Archives", (
        "Construct • Shield Construct • Flash Drone • Arcdrift",
        "This is the opening Beat-6 Archive pool. Ruin Spider, Scriptshade, and Maul Construct are deliberately held back.",
    ), CH3, ("Construct", "Shield Construct", "Flash Drone", "Arcdrift")),
    ("Card Cases", "Enemy Roster — Buried Collections", (
        "Construct • Shield Construct • Flash Drone • Arcdrift • Ruin Spider",
        "Ruin Spider enters in the Buried Collections. Scriptshade and Maul Construct remain held back.",
    ), CH3, ("Construct", "Shield Construct", "Flash Drone", "Arcdrift", "Ruin Spider")),
    ("Working Seal", "Enemy Roster — Hall of Seals", (
        "Construct • Shield Construct • Flash Drone • Arcdrift • Ruin Spider • Scriptshade",
        "Scriptshade enters in the Hall of Seals. Maul Construct remains held back until the Deep Archives.",
    ), CH3, ("Construct", "Shield Construct", "Flash Drone", "Arcdrift", "Ruin Spider", "Scriptshade")),
    ("Short Stop — Old Copying Floor", "Enemy Roster — Deep Archives", (
        "Construct • Maul Construct • Flash Drone • Arcdrift • Ruin Spider • Scriptshade",
        "Maul Construct enters here. Once it enters, Shield Construct leaves the Deep Archives random pool.",
    ), CH3, ("Construct", "Maul Construct", "Flash Drone", "Arcdrift", "Ruin Spider", "Scriptshade")),
    ("Memory Construct", "Boss — Memory Construct", (
        "Memory Construct",
        "Mandatory authored boss only. The immediate pre-boss staging pocket is safe from random encounters.",
    ), CH3, ("Memory Construct",)),
    ("Short Ancient Dungeon — Tower Foundation", "Enemy Roster — Cresthaven Ancient Tower Base", (
        "Construct • Shield Construct • Maul Construct • Flame Construct • Blade Drone • Ruin Spider",
        "Tower Foundation starts at 4–5 bodies; later Command Interior formations may reach 6. The immediate Authority Construct approach is safe.",
    ), CH3, ("Construct", "Shield Construct", "Maul Construct", "Flame Construct", "Blade Drone", "Ruin Spider")),
    ("Authority Construct", "Boss — Authority Construct", (
        "Authority Construct",
        "Mandatory authored boss only. PREVIOUS ERROR → LAST SENTINEL CONFIRMED remains the protected shutdown order.",
    ), CH3, ("Authority Construct",)),

)

FORMATION_AUTHORITIES = (
    (CH1_FORMATIONS, ("Briar Passage — first / northern traversal", "Hollow Watch — surface / Black Host", "Hollow Watch — excavation / ancient defenses", "Southern Briar Passage", "Shield Construct", "Thornhide")),
    (CH2_FORMATIONS, ("Old Waterworks", "Sunken Archive", "Old Bastion", "Arcdrift", "Full Bastion Response")),
    (CH3_FORMATIONS, (
        "Caelora Archives",
        "Beat 6 — Lower Archives subzone",
        "Beat 6 — Buried Collections subzone",
        "Beat 6 — Hall of Seals subzone",
        "Beat 7 — Deep Archives",
        "Memory Construct",
        "Cresthaven Ancient tower base",
        "Authority Construct",
    )),

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


def insert_after(document: Document, anchor, text: str, style: str | None = None):
    paragraph = document.add_paragraph(text, style=style)
    anchor._p.addnext(paragraph._p)
    return paragraph


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
    if not out or out[-1] != "Mostly not metaphorically.":
        raise RuntimeError("World intro no longer ends on Nimera's approved sign-off")
    return out


def validate_authority() -> None:
    for authority, needles in FORMATION_AUTHORITIES:
        authority_text = authority.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in authority_text:
                raise RuntimeError(
                    f"Current formation authority {authority.relative_to(ROOT)} no longer contains {needle!r}"
                )

    ch2_text = CH2.read_text(encoding="utf-8")
    ch3_formations = CH3_FORMATIONS.read_text(encoding="utf-8")

    if "no Caelora → Cresthaven road encounters" not in ch3_formations:
        raise RuntimeError("Chapter-3 no-road-combat firewall is missing from current formation authority")
    if "Retired from current Chapter-2 placement:" not in ch2_text or "- Redwater Initiate." not in ch2_text:
        raise RuntimeError("Waterworks Redwater retirement firewall is missing from current Chapter-2 authority")
    if "There is no Hold the Junction" not in ch2_text:
        raise RuntimeError("Hold-the-Junction retirement firewall is missing from current Chapter-2 authority")

    cache = {}
    for _target, title, body, owner, needles in BRIDGES:
        owner_text = cache.setdefault(owner, owner.read_text(encoding="utf-8"))
        for needle in needles:
            if needle not in owner_text:
                raise RuntimeError(f"{title}: current owning authority no longer contains {needle!r}")
        joined = " ".join(body)
        if title == "Enemy Roster — Old Waterworks" and "Redwater Initiate" in joined:
            raise RuntimeError("Redwater Initiate must not be auto-placed in Waterworks")
        if title.startswith("Enemy Roster —") and "Way-Fort" in joined:
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
        f"Reader enrichment complete: world intro + {len(BRIDGES)} localized enemy/encounter blocks; "
        f"{len(after)} spoken lines preserved exactly."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
