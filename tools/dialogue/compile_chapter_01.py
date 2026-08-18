#!/usr/bin/env python3
"""Compile the locked Chapter 1 Markdown dialogue sources into Godot dialogue Resources.

The Markdown files remain the wording authority. This compiler copies every speaker line
verbatim, carries source staging/prose into cue metadata, and adds only implementation IDs,
registry IDs, and durable handoff flags already required by the Chapter 1 lock.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "docs/chapters/dialogue/chapter_01"
OUTPUT_DIR = ROOT / "game/content/dialogue/chapter_01"

SCENES = {
    "S007": {"kind": "mandatory", "location": "LOC_BRACKENWALL", "trigger": "trigger.chapter_01.s007"},
    "S008": {"kind": "mandatory", "location": "LOC_HOLLOW_WATCH", "trigger": "trigger.chapter_01.s008"},
    "S009": {"kind": "mandatory", "location": "LOC_GREENHOLLOW", "trigger": "trigger.chapter_01.s009"},
    "S010": {"kind": "mandatory", "location": "LOC_BRIAR_PASSAGE", "trigger": "trigger.chapter_01.s010"},
    "S011": {"kind": "mandatory", "location": "LOC_WAYFINDER_JUNCTION", "trigger": "trigger.chapter_01.s011"},
    "C03": {"kind": "character_life", "location": "LOC_CHAPTER_01_ROADSIDE_REST", "trigger": "trigger.chapter_01.c03.after_s011"},
    "C04": {"kind": "character_life", "location": "LOC_BRACKENWALL_ROUTE_ROOM", "trigger": "trigger.chapter_01.c04.after_s011"},
    "C05": {"kind": "character_life", "location": "LOC_BRACKENWALL_SUPPLY_MEDICAL", "trigger": "trigger.chapter_01.c05.after_s011"},
}

SPEAKER_IDS = {
    "CYANIS": "cyanis",
    "ILYRA": "ilyra",
    "MAEVRA": "maevra",
    "TORREN": "torren",
    "CUSTODY OFFICER": "custody_officer",
    "SERGEANT": "sergeant",
    "SCOUT": "scout",
    "EDDA": "edda",
    "INJURED CIVILIAN": "injured_civilian",
    "RUNNER": "runner",
}

DISPLAY_NAMES = {
    "cyanis": "Cyanis",
    "ilyra": "Ilyra",
    "maevra": "Maevra",
    "torren": "Torren",
    "custody_officer": "Custody Officer",
    "sergeant": "Sergeant",
    "scout": "Scout",
    "edda": "Edda",
    "injured_civilian": "Injured Civilian",
    "runner": "Runner",
}

DURABLE_FLAGS = {
    "S007": ["PARTY_ADD_MAEVRA_GUEST"],
    "S009": ["ROSTER_ADD_TORREN_PERMANENT"],
    "S011": [
        "STORY_CHAPTER_01_COMPLETE",
        "ROUTE_DUNMERE_UNLOCKED",
        "UNLOCK_C03_TORRENS_VERSION_OF_DINNER",
        "UNLOCK_C04_WHAT_THE_MAP_SAYS",
        "UNLOCK_C05_TWO_PROFESSIONALS_COMPLAINING_ABOUT_CYANIS",
        "DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES",
    ],
}

DIALOGUE_RE = re.compile(r"^\*\*([^*\n]+):\*\*\s*(.*)$")


def quote(value: str) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def gd_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return quote(value)
    if isinstance(value, list):
        return "[" + ", ".join(gd_value(item) for item in value) + "]"
    if isinstance(value, dict):
        return "{" + ", ".join(f"{quote(key)}: {gd_value(item)}" for key, item in value.items()) + "}"
    raise TypeError(f"Unsupported Godot literal: {type(value)!r}")


def parse_scene(scene_id: str, source: str):
    lines = source.splitlines()
    current_section = ""
    pending: list[str] = []
    beats: list[dict] = []
    section_had_spoken = False
    last_beat: dict | None = None

    def flush_pending() -> None:
        nonlocal pending
        text = "\n".join(pending).strip()
        pending = []
        if not text:
            return
        if last_beat is not None and section_had_spoken:
            last_beat["cues"]["staging_after"] = text
            return
        if current_section:
            beats.append({
                "speaker_id": "",
                "text": "",
                "cues": {
                    "pause_ms": 120,
                    "staging": text,
                    "interrupt": False,
                    "implementation_flags": ["SOURCE_STAGING"],
                    "source_section": current_section,
                },
            })

    for line in lines:
        if line.startswith("### "):
            flush_pending()
            current_section = line[4:].strip()
            section_had_spoken = False
            last_beat = None
            continue
        if line.startswith("## "):
            flush_pending()
            current_section = line[3:].strip()
            section_had_spoken = False
            last_beat = None
            continue

        match = DIALOGUE_RE.match(line) if current_section else None
        if match:
            staging = "\n".join(pending).strip()
            pending = []
            source_speaker = match.group(1).strip()
            if source_speaker not in SPEAKER_IDS:
                raise ValueError(f"{scene_id}: unmapped dialogue speaker {source_speaker!r}")
            cues = {
                "pause_ms": 80,
                "interrupt": False,
                "implementation_flags": ["IN_WORLD_DIALOGUE"],
                "source_section": current_section,
            }
            if staging:
                cues["staging"] = staging
            beat = {"speaker_id": SPEAKER_IDS[source_speaker], "text": match.group(2).strip(), "cues": cues}
            beats.append(beat)
            last_beat = beat
            section_had_spoken = True
            continue

        if not current_section:
            continue
        if not line.strip():
            if pending and pending[-1] != "":
                pending.append("")
        else:
            pending.append(line.rstrip())

    flush_pending()

    for beat in beats:
        cues = beat["cues"]
        combined = (str(cues.get("source_section", "")) + "\n" + str(cues.get("staging", ""))).upper()
        flags = list(cues.get("implementation_flags", []))
        if "PLAYER CONTROL" in combined:
            flags.append("RETURN_PLAYER_CONTROL")
        if "ENCOUNTER STATE: SAFE" in combined:
            flags.append("SAFE_DIALOGUE_POCKET")
        if "BOSS" in combined and "BOSS" in str(cues.get("source_section", "")).upper():
            flags.append("BOSS_HANDOFF")
        if "AUTHORED" in str(cues.get("source_section", "")).upper() and ("ENCOUNTER" in combined or "BOSS" in combined):
            flags.append("AUTHORED_ENCOUNTER_HANDOFF")
        cues["implementation_flags"] = list(dict.fromkeys(flags))

    if scene_id in DURABLE_FLAGS:
        beats[-1]["cues"]["implementation_flags"] = list(dict.fromkeys(
            list(beats[-1]["cues"].get("implementation_flags", [])) + DURABLE_FLAGS[scene_id]
        ))

    for index, beat in enumerate(beats, start=1):
        beat["beat_id"] = f"{scene_id}_B{index:03d}"
    return beats


def render_scene(scene_id: str, beats: list[dict]) -> str:
    info = SCENES[scene_id]
    participants: list[str] = []
    spoken_fingerprint: list[str] = []
    for beat in beats:
        speaker_id = beat["speaker_id"]
        if speaker_id and speaker_id not in participants:
            participants.append(speaker_id)
        if speaker_id:
            spoken_fingerprint.append(f"{speaker_id}\t{beat['text']}")
    digest = hashlib.sha256("\n".join(spoken_fingerprint).encode("utf-8")).hexdigest()
    notes = (
        f"Chapter 1 exact Resource conversion from docs/chapters/dialogue/chapter_01/{scene_id}.md "
        "under Complete Master Canon v1.64 / Audit79. Spoken text is line-complete and must not be rewritten. "
        "Source production/staging prose is preserved in beat cue metadata; source subsection names are carried in cues.source_section. "
        "Portrait slots remain empty until approved registry expressions/assets are wired. "
        f"Spoken-sequence SHA-256: {digest}."
    )

    rendered_beats = []
    for beat in beats:
        rendered_beats.append(gd_value({
            "beat_id": beat["beat_id"],
            "speaker_id": beat["speaker_id"],
            "text": beat["text"],
            "left": {},
            "right": {},
            "active_side": "none",
            "advance_mode": "manual",
            "cues": beat["cues"],
        }))

    return "\n".join([
        '[gd_resource type="Resource" script_class="DiyseDialogueSceneDefinition" load_steps=2 format=3]',
        "",
        '[ext_resource type="Script" path="res://game/dialogue/dialogue_scene_definition.gd" id="1_scene"]',
        "",
        "[resource]",
        'script = ExtResource("1_scene")',
        "schema_version = 1",
        f"scene_id = {quote(scene_id)}",
        'chapter_id = "chapter_01"',
        f"scene_kind = {quote(info['kind'])}",
        f"location_id = {quote(info['location'])}",
        f"trigger_id = {quote(info['trigger'])}",
        f"completion_flag = {quote('scene.' + scene_id.lower() + '.complete')}",
        "participants = Array[String]([" + ", ".join(quote(item) for item in participants) + "])",
        f"authoring_notes = {quote(notes)}",
        "beats = [",
        ",\n".join(rendered_beats),
        "]",
        "",
    ])


def render_registry(participant_order: list[str]) -> str:
    entries = [{"character_id": cid, "display_name": DISPLAY_NAMES[cid], "portraits": {}} for cid in participant_order]
    return "\n".join([
        '[gd_resource type="Resource" script_class="DiyseDialoguePortraitRegistry" load_steps=2 format=3]',
        "",
        '[ext_resource type="Script" path="res://game/dialogue/dialogue_portrait_registry.gd" id="1_registry"]',
        "",
        "[resource]",
        'script = ExtResource("1_registry")',
        "entries = [",
        ",\n".join(gd_value(entry) for entry in entries),
        "]",
        "",
    ])


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    participant_order: list[str] = []
    for scene_id in SCENES:
        source_path = SOURCE_DIR / f"{scene_id}.md"
        source = source_path.read_text(encoding="utf-8")
        beats = parse_scene(scene_id, source)
        for beat in beats:
            speaker_id = beat["speaker_id"]
            if speaker_id and speaker_id not in participant_order:
                participant_order.append(speaker_id)
        (OUTPUT_DIR / f"{scene_id}.tres").write_text(render_scene(scene_id, beats), encoding="utf-8")
        print(f"compiled {scene_id}: {len(beats)} beats, {sum(1 for b in beats if b['speaker_id'])} spoken")

    (OUTPUT_DIR / "chapter_01_dialogue_registry.tres").write_text(render_registry(participant_order), encoding="utf-8")
    print(f"compiled Chapter 1 registry: {len(participant_order)} speakers")


if __name__ == "__main__":
    main()
