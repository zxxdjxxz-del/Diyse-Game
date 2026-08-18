#!/usr/bin/env python3
"""Compile locked Chapter 3 Markdown dialogue sources into Godot dialogue Resources.

The Markdown files remain exact wording authority. This compiler copies every approved
spoken line verbatim, preserves source staging/prose in cue metadata, and adds only
implementation IDs/flags required by the Chapter 3 implementation lock.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "docs/chapters/dialogue/chapter_03"
OUTPUT_DIR = ROOT / "game/content/dialogue/chapter_03"

SCENES = {
    "S017": {"kind": "mandatory", "location": "LOC_CAELORA_CONTAINMENT", "trigger": "trigger.chapter_03.s017"},
    "S018": {"kind": "mandatory", "location": "LOC_CAELORA_JUDICIAL_CAUSEWAY", "trigger": "trigger.chapter_03.s018"},
    "S019": {"kind": "mandatory", "location": "LOC_OLD_CITY_SUPPRESSED_ARCHIVES", "trigger": "trigger.chapter_03.s019"},
    "S020": {"kind": "mandatory", "location": "LOC_OLD_CITY_COMMAND_STATION", "trigger": "trigger.chapter_03.s020"},
    "S021": {"kind": "mandatory", "location": "LOC_CRESTHAVEN", "trigger": "trigger.chapter_03.s021.next_morning"},
    "H01": {"kind": "character_life", "location": "LOC_CRESTHAVEN_ARCHIVE_COMMON", "trigger": "trigger.chapter_03.h01.after_s019.at_cresthaven"},
    "H02": {"kind": "character_life", "location": "LOC_CRESTHAVEN_RECORDS_ROOM", "trigger": "trigger.chapter_03.h02.after_s018.at_cresthaven"},
    "H03": {"kind": "character_life", "location": "LOC_CRESTHAVEN_MEDICAL", "trigger": "trigger.chapter_03.h03.after_s019.at_cresthaven"},
    "H04": {"kind": "character_life", "location": "LOC_CRESTHAVEN_COMMON", "trigger": "trigger.chapter_03.h04.after_s021"},
}

DISPLAY_OVERRIDES = {
    "cyanis": "Cyanis",
    "ilyra": "Ilyra",
    "torren": "Torren",
    "maevra": "Maevra",
    "nimera": "Nimera",
    "mirena": "Mirena",
    "lysara": "Lysara",
}

DURABLE_FLAGS = {
    "S018": ["UNLOCK_H02_TORREN_MAEVRA_UNSUPERVISED"],
    "S019": [
        "PARTY_NIMERA_PERMANENT_JOINED",
        "FORMATION_CHOOSE_FOUR_ENABLED",
        "UNLOCK_H01_NIMERA_TAKES_OVER_A_TABLE",
        "UNLOCK_H03_ILYRA_AND_NIMERA",
    ],
    "S020": [
        "STATE_FIRST_COMMAND_WARDEN_DEFEATED",
        "STATE_FALSE_ORDER_ASSEMBLY_PROVED",
        "STATE_TORREN_ROUTE_SKETCH_ACQUIRED",
        "STATE_CRESTHAVEN_IDENTIFIED",
    ],
    "S021": [
        "STORY_CHAPTER_03_COMPLETE",
        "PRIME_LAST_SENTINEL_RECOVERED",
        "CRESTHAVEN_PHASE_01_OPERATIONAL",
        "UNLOCK_H04_LAST_SENTINEL_IS_NOT_INVITED",
        "UNLOCK_HUNT_03_ARCHIVE_JUDGMENT_ENGINE",
        "DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES",
    ],
}

INLINE_DIALOGUE_RE = re.compile(r"^\*\*([^*\n]+):\*\*\s*(.*)$")


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


def speaker_id(source_label: str) -> str:
    value = source_label.strip().lower()
    value = value.replace("’", "").replace("'", "")
    value = value.replace("—", " ").replace("–", " ").replace("/", " ")
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    if not value:
        raise ValueError(f"Could not normalize source speaker label {source_label!r}")
    return value


def display_name(source_label: str, normalized: str) -> str:
    if normalized in DISPLAY_OVERRIDES:
        return DISPLAY_OVERRIDES[normalized]
    return source_label.title()


def parse_scene(scene_id: str, source: str):
    lines = source.splitlines()
    current_section = ""
    pending: list[str] = []
    beats: list[dict] = []
    section_had_spoken = False
    last_beat: dict | None = None
    display_by_id: dict[str, str] = {}

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

    def append_dialogue(source_speaker: str, text: str, staging: str = "") -> None:
        nonlocal last_beat, section_had_spoken
        sid = speaker_id(source_speaker)
        display_by_id.setdefault(sid, display_name(source_speaker, sid))
        cues = {
            "pause_ms": 80,
            "interrupt": False,
            "implementation_flags": ["IN_WORLD_DIALOGUE"],
            "source_section": current_section,
            "source_speaker_label": source_speaker,
        }
        if staging:
            cues["staging"] = staging
        if source_speaker == "WOMAN'S VOICE":
            cues["delivery"] = "offscreen"
        beat = {"speaker_id": sid, "text": text, "cues": cues}
        beats.append(beat)
        last_beat = beat
        section_had_spoken = True

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
        if not current_section:
            continue

        inline = INLINE_DIALOGUE_RE.match(line)
        if inline:
            staging = "\n".join(pending).strip()
            pending = []
            append_dialogue(inline.group(1).strip(), inline.group(2).strip(), staging)
            continue

        if not line.strip():
            if pending and pending[-1] != "":
                pending.append("")
        else:
            pending.append(line.rstrip())

    flush_pending()

    for beat in beats:
        cues = beat["cues"]
        combined = (
            str(cues.get("source_section", ""))
            + "\n"
            + str(cues.get("staging", ""))
            + "\n"
            + str(cues.get("staging_after", ""))
        ).upper()
        section = str(cues.get("source_section", "")).upper()
        flags = list(cues.get("implementation_flags", []))
        if "PLAYER CONTROL" in combined or "CONTROL RESUMES" in combined or "CUT TO PLAYER CONTROL" in combined:
            flags.append("RETURN_PLAYER_CONTROL")
        if "NO RANDOM" in combined or "ENCOUNTER SUPPRESSION" in combined or "SAFE" in section:
            flags.append("SAFE_DIALOGUE_POCKET")
        if "AUTHORED ENCOUNTER #" in combined or "AUTHORED COMMAND-PRESSURE ENCOUNTER" in combined:
            flags.append("AUTHORED_ENCOUNTER_HANDOFF")
        if "BOSS — FIRST COMMAND WARDEN" in combined or "BOSS - FIRST COMMAND WARDEN" in combined:
            flags.extend(["BOSS_HANDOFF", "WARDEN_ONE_HP_BAR"])
        if scene_id == "S020" and "THRESHOLD" in section:
            flags.append("WARDEN_SAME_BAR_STATE_CHANGE")
        if scene_id == "S019" and "PERMANENT PARTY MEMBER JOINED" in combined:
            flags.append("PARTY_NIMERA_PERMANENT_JOINED")
        if scene_id == "S019" and "FORMATION UNLOCK" in combined:
            flags.append("FORMATION_CHOOSE_FOUR_ENABLED")
        if scene_id == "S020" and "/PREVIOUS ERROR/" in combined and "/LAST SENTINEL CONFIRMED/" in combined:
            flags.append("LAST_SENTINEL_EXACT_MACHINE_OUTPUT")
        if scene_id == "S020" and "THE ROOM BEHIND THE WARDEN" in section:
            flags.append("POST_WARDEN_COMMAND_RECORD_ROOM")
        if scene_id == "S020" and "PROOF OF ASSEMBLY" in section:
            flags.append("FALSE_ORDER_ASSEMBLY_EVIDENCE")
        if scene_id == "S020" and "TORREN NOTICES A MAP" in section:
            flags.append("TORREN_ROUTE_SKETCH")
        if scene_id == "S020" and "RETURN TO CAELORA" in section:
            flags.append("RETURN_TO_CAELORA_BEFORE_CRESTHAVEN")
        if scene_id == "S020" and "STOP FOR THE NIGHT" in section:
            flags.append("NO_CRESTHAVEN_TRAVEL_UNTIL_NEXT_MORNING")
        if scene_id == "S021" and "CRESTHAVEN, NEXT MORNING" in section:
            flags.append("CRESTHAVEN_NEXT_MORNING_ARRIVAL")
        if scene_id == "S021" and "UNLOCK, NOT MANIFESTATION" in section:
            flags.extend(["LAST_SENTINEL_RECOVERED_NOT_MANIFESTED", "PRIME_UNLOCK_UI_HANDOFF"])
        if scene_id == "S021" and "THE OLD CITY BRANCH CAN WAIT" in section:
            flags.append("HUNT_03_RETURN_ROUTE_AVAILABLE")
        cues["implementation_flags"] = list(dict.fromkeys(flags))

    if scene_id in DURABLE_FLAGS and beats:
        beats[-1]["cues"]["implementation_flags"] = list(dict.fromkeys(
            list(beats[-1]["cues"].get("implementation_flags", [])) + DURABLE_FLAGS[scene_id]
        ))

    for index, beat in enumerate(beats, start=1):
        beat["beat_id"] = f"{scene_id}_B{index:03d}"
    return beats, display_by_id


def render_scene(scene_id: str, beats: list[dict]) -> str:
    info = SCENES[scene_id]
    participants: list[str] = []
    spoken_fingerprint: list[str] = []
    for beat in beats:
        sid = beat["speaker_id"]
        if sid and sid not in participants:
            participants.append(sid)
        if sid:
            spoken_fingerprint.append(f"{sid}\t{beat['text']}")
    digest = hashlib.sha256("\n".join(spoken_fingerprint).encode("utf-8")).hexdigest()
    notes = (
        f"Chapter 3 exact Resource conversion from docs/chapters/dialogue/chapter_03/{scene_id}.md "
        "under Complete Master Canon v1.64 / Audit79, Chapter transcript checkpoint Audit77 plus the bounded S020→S021 Cresthaven correction. "
        "Spoken text is line-complete and must not be rewritten. Source staging/prose is preserved in cue metadata. "
        "H01/H02/H03 preserve their earlier eligibility flags but require Cresthaven location access before playback. "
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
        'chapter_id = "chapter_03"',
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


def render_registry(participant_order: list[str], displays: dict[str, str]) -> str:
    entries = [{"character_id": cid, "display_name": displays.get(cid, cid.replace("_", " ").title()), "portraits": {}} for cid in participant_order]
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
    displays: dict[str, str] = {}
    for scene_id in SCENES:
        source_path = SOURCE_DIR / f"{scene_id}.md"
        source = source_path.read_text(encoding="utf-8")
        beats, scene_displays = parse_scene(scene_id, source)
        if not beats:
            raise ValueError(f"{scene_id}: compiler produced no beats")
        displays.update(scene_displays)
        for beat in beats:
            sid = beat["speaker_id"]
            if sid and sid not in participant_order:
                participant_order.append(sid)
        (OUTPUT_DIR / f"{scene_id}.tres").write_text(render_scene(scene_id, beats), encoding="utf-8")
        print(f"compiled {scene_id}: {len(beats)} beats, {sum(1 for b in beats if b['speaker_id'])} spoken")

    (OUTPUT_DIR / "chapter_03_dialogue_registry.tres").write_text(render_registry(participant_order, displays), encoding="utf-8")
    print(f"compiled Chapter 3 registry: {len(participant_order)} speakers")


if __name__ == "__main__":
    main()
