#!/usr/bin/env python3
"""Compile locked Chapter 2 Markdown dialogue sources into Godot dialogue Resources.

The Markdown files remain exact wording authority. This compiler copies every approved
spoken line verbatim, preserves source staging/prose in cue metadata, and adds only
implementation IDs/flags required by the Chapter 2 implementation lock.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIR = ROOT / "docs/chapters/dialogue/chapter_02"
OUTPUT_DIR = ROOT / "game/content/dialogue/chapter_02"

SCENES = {
    "S012": {"kind": "mandatory", "location": "LOC_DUNMERE_WATERWORKS", "trigger": "trigger.chapter_02.s012"},
    "S013": {"kind": "mandatory", "location": "LOC_SUNKEN_ARCHIVE", "trigger": "trigger.chapter_02.s013"},
    "S014": {"kind": "mandatory", "location": "LOC_PRISONER_GALLERIES", "trigger": "trigger.chapter_02.s014"},
    "S015": {"kind": "mandatory", "location": "LOC_RED_TRANSFER_BASTION", "trigger": "trigger.chapter_02.s015"},
    "S016": {"kind": "mandatory", "location": "LOC_EXTRACTION_CAUSEWAY", "trigger": "trigger.chapter_02.s016"},
    "C06": {"kind": "character_life", "location": "LOC_DUNMERE_REST_AREA", "trigger": "trigger.chapter_02.c06.after_s016"},
    "C07": {"kind": "character_life", "location": "LOC_DUNMERE_REST_AREA", "trigger": "trigger.chapter_02.c07.after_s016"},
}

SPEAKER_IDS = {
    "CYANIS": "cyanis",
    "ILYRA": "ilyra",
    "MAEVRA": "maevra",
    "TORREN": "torren",
    "WATERMASTER": "watermaster",
    "WORKER": "worker",
    "PARTY ACTOR": "party_actor",
    "PRISONER WOMAN": "prisoner_woman",
    "PRISONER WOMAN — THROUGH DOOR": "prisoner_woman",
    "INJURED MAN": "injured_man",
    "PRISONER": "prisoner",
    "SECOND PRISONER": "second_prisoner",
    "OLDER PRISONER": "older_prisoner",
    "OFFICER": "officer",
    "SECOND OFFICER": "second_officer",
    "RHAZEK": "rhazek",
    "EVACUEE": "evacuee",
    "ILYRA / TORREN": "ilyra_torren",
}

DISPLAY_NAMES = {
    "cyanis": "Cyanis",
    "ilyra": "Ilyra",
    "maevra": "Maevra",
    "torren": "Torren",
    "watermaster": "Watermaster",
    "worker": "Worker",
    "party_actor": "Party Actor",
    "prisoner_woman": "Prisoner Woman",
    "injured_man": "Injured Man",
    "prisoner": "Prisoner",
    "second_prisoner": "Second Prisoner",
    "older_prisoner": "Older Prisoner",
    "officer": "Officer",
    "second_officer": "Second Officer",
    "rhazek": "Rhazek",
    "evacuee": "Evacuee",
    "ilyra_torren": "Ilyra / Torren",
}

DURABLE_FLAGS = {
    "S015": [
        "STATE_RHAZEK_CH02_WITHDRAWN",
        "STATE_BASTION_EXTRACTION_CONTROL_ACQUIRED",
    ],
    "S016": [
        "STORY_CHAPTER_02_COMPLETE",
        "UNLOCK_C06_THREE_PEOPLE_WHO_KNOW_EACH_OTHER_NOW",
        "UNLOCK_C07_BAD_DREAMS_NO_QUESTIONS",
        "UNLOCK_HUNT_02_TRANSFER_EXECUTIONER",
        "DO_NOT_AUTO_SKIP_CHARACTER_LIFE_SCENES",
    ],
}

INLINE_DIALOGUE_RE = re.compile(r"^\*\*([^*\n]+):\*\*\s*(.*)$")
STANDALONE_SPEAKER_RE = re.compile(r"^\*\*([^*\n]+)\*\*$")


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
    standalone_speaker: str | None = None

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
        if source_speaker not in SPEAKER_IDS:
            raise ValueError(f"{scene_id}: unmapped dialogue speaker {source_speaker!r}")
        cues = {
            "pause_ms": 80,
            "interrupt": False,
            "implementation_flags": ["IN_WORLD_DIALOGUE"],
            "source_section": current_section,
            "source_speaker_label": source_speaker,
        }
        if staging:
            cues["staging"] = staging
        if source_speaker == "PRISONER WOMAN — THROUGH DOOR":
            cues["delivery"] = "through_door"
        if source_speaker == "ILYRA / TORREN":
            cues["simultaneous_speakers"] = ["ilyra", "torren"]
        beat = {"speaker_id": SPEAKER_IDS[source_speaker], "text": text, "cues": cues}
        beats.append(beat)
        last_beat = beat
        section_had_spoken = True

    for line in lines:
        if line.startswith("### "):
            flush_pending()
            current_section = line[4:].strip()
            section_had_spoken = False
            last_beat = None
            standalone_speaker = None
            continue
        if line.startswith("## "):
            flush_pending()
            current_section = line[3:].strip()
            section_had_spoken = False
            last_beat = None
            standalone_speaker = None
            continue

        if not current_section:
            continue

        inline = INLINE_DIALOGUE_RE.match(line)
        if inline:
            staging = "\n".join(pending).strip()
            pending = []
            append_dialogue(inline.group(1).strip(), inline.group(2).strip(), staging)
            standalone_speaker = None
            continue

        standalone = STANDALONE_SPEAKER_RE.match(line)
        if standalone and standalone.group(1).strip() in SPEAKER_IDS:
            staging = "\n".join(pending).strip()
            pending = []
            if staging:
                if last_beat is not None and section_had_spoken:
                    last_beat["cues"]["staging_after"] = staging
                else:
                    beats.append({
                        "speaker_id": "",
                        "text": "",
                        "cues": {
                            "pause_ms": 120,
                            "staging": staging,
                            "interrupt": False,
                            "implementation_flags": ["SOURCE_STAGING"],
                            "source_section": current_section,
                        },
                    })
            standalone_speaker = standalone.group(1).strip()
            continue

        if standalone_speaker is not None:
            if not line.strip():
                continue
            append_dialogue(standalone_speaker, line.strip())
            standalone_speaker = None
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
        if "CONTROL RETURNS" in combined or "PLAYER CONTROL" in combined:
            flags.append("RETURN_PLAYER_CONTROL")
        if "RECOVERY POCKET" in section or "SAFE POCKET" in section or "SAFE ZONE" in combined:
            flags.append("SAFE_DIALOGUE_POCKET")
        if "BOSS" in section:
            flags.append("BOSS_HANDOFF")
        if any(token in section for token in ["AUTHORED MEMORY SCRIBE ENCOUNTER", "AUTHORED COMBAT", "HOLD THE JUNCTION"]):
            flags.append("AUTHORED_ENCOUNTER_HANDOFF")
        if "SAME-BAR THRESHOLD" in section:
            flags.append("SAME_BAR_THRESHOLD")
        if scene_id == "S016" and "HOLD THE JUNCTION" in section:
            flags.append("MANDATORY_COMBAT_01_OF_01")
        if scene_id == "S016" and "FINAL EXTRACTION THRESHOLD" in combined:
            flags.append("NO_COMBAT_AFTER_THIS_BEAT")
        cues["implementation_flags"] = list(dict.fromkeys(flags))

    if scene_id in DURABLE_FLAGS and beats:
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
        f"Chapter 2 exact Resource conversion from docs/chapters/dialogue/chapter_02/{scene_id}.md "
        "under Complete Master Canon v1.64 / Audit79, Chapter transcript checkpoint Audit78. "
        "Spoken text is line-complete and must not be rewritten. Source staging/prose is preserved in cue metadata; "
        "source subsection and source speaker labels are carried in cues. Portrait slots remain empty until approved assets are wired. "
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
        'chapter_id = "chapter_02"',
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
        if not beats:
            raise ValueError(f"{scene_id}: compiler produced no beats")
        for beat in beats:
            speaker_id = beat["speaker_id"]
            if speaker_id and speaker_id not in participant_order:
                participant_order.append(speaker_id)
        (OUTPUT_DIR / f"{scene_id}.tres").write_text(render_scene(scene_id, beats), encoding="utf-8")
        print(f"compiled {scene_id}: {len(beats)} beats, {sum(1 for b in beats if b['speaker_id'])} spoken")

    (OUTPUT_DIR / "chapter_02_dialogue_registry.tres").write_text(render_registry(participant_order), encoding="utf-8")
    print(f"compiled Chapter 2 registry: {len(participant_order)} speakers")


if __name__ == "__main__":
    main()
