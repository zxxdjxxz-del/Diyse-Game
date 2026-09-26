#!/usr/bin/env python3
"""Compile current Chapters 0-3 dialogue atomics into canonical Godot runtime Resources.

Source authority is docs/03_DIALOGUE/PRODUCTION/CHAPTER_##. The generated runtime layer
lives under game/content/dialogue/current/ and is the game-facing wording mirror.

The compiler is intentionally strict:
- current atomics are the only spoken-wording authority;
- speaker labels must be ALL-CAPS inline Markdown dialogue labels;
- all current spoken lines must compile in exact order and wording;
- walking/traversal dialogue and active-combat dialogue are not runtime scene modes;
- generated Resources embed source/spoken hashes;
- legacy S001-S021 Resources are not used as input.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PROD = ROOT / "docs/03_DIALOGUE/PRODUCTION"
OUT_ROOT = ROOT / "game/content/dialogue/current"
EXPECTED_TOTAL_SPOKEN = 2021

DIALOGUE_RE = re.compile(r"^\*\*([^*\n]+):\*\*\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")

# Chapter 3 current structure recruits Nimera permanently in B06.
# Protected First Command Warden messages compile as B14 spoken dialogue.
DURABLE_FLAGS: dict[tuple[str, str], list[str]] = {
    ("00", "P07"): [
        "ROSTER_ADD_ILYRA_PERMANENT",
        "STORY_CHAPTER_00_COMPLETE",
        "ROUTE_BRACKENWALL_UNLOCKED",
        "UNLOCK_C01_SIX_MINUTES",
    ],
    ("01", "B08"): ["ROSTER_ADD_TORREN_PERMANENT"],
    ("01", "B12"): [
        "STORY_CHAPTER_01_COMPLETE",
        "UNLOCK_C02_TORRENS_VERSION_OF_DINNER",
        "UNLOCK_C03_WHAT_THE_MAP_SAYS",
        "UNLOCK_C04_NOT_PROFESSIONALLY",
    ],
    ("02", "B15"): [
        "STORY_CHAPTER_02_COMPLETE",
        "UNLOCK_C05_STILL_BURNS",
    ],
    ("03", "B06"): ["ROSTER_ADD_NIMERA_PERMANENT"],
    ("03", "B15"): [
        "STORY_CHAPTER_03_COMPLETE",
        "UNLOCK_C06_NIMERA_TAKES_OVER_A_TABLE",
        "UNLOCK_C07_ILYRA_AND_NIMERA",
    ],
}


@dataclass(frozen=True)
class SceneSource:
    chapter: str
    slot_id: str
    source_path: Path
    scene_kind: str
    spec_path: Path | None = None


class CompileError(RuntimeError):
    pass


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def quote(value: str) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def gd_value(value: Any) -> str:
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


def slug(value: str, upper: bool = False) -> str:
    normalized = NON_ALNUM_RE.sub("_", value.casefold()).strip("_")
    if not normalized:
        normalized = "scene"
    return normalized.upper() if upper else normalized


def speaker_id(label: str) -> str:
    return slug(label.strip())


def display_name(label_or_id: str) -> str:
    return label_or_id.replace("_", " ").strip().title()


def is_spoken_label(label: str) -> bool:
    return bool(re.search(r"[A-Z]", label)) and label == label.upper()


def chapter_dir(chapter: str) -> Path:
    return PROD / f"CHAPTER_{chapter}"


def unique_glob(directory: Path, pattern: str) -> Path:
    matches = sorted(p for p in directory.glob(pattern) if p.is_file())
    if len(matches) != 1:
        rels = [str(p.relative_to(ROOT)) for p in matches]
        raise CompileError(f"{directory.relative_to(ROOT)} / {pattern!r}: expected one file, found {len(matches)}: {rels}")
    return matches[0]


def source_set() -> list[SceneSource]:
    scenes: list[SceneSource] = []

    ch0 = chapter_dir("00")
    for n in range(1, 8):
        scenes.append(SceneSource("00", f"P{n:02d}", unique_glob(ch0, f"P{n:02d}_*.md"), "mandatory"))
    scenes.append(SceneSource("00", "C01", unique_glob(ch0, "C01_SIX_MINUTES_*.md"), "character_life"))

    ch1 = chapter_dir("01")
    for n in range(1, 13):
        scenes.append(SceneSource(
            "01",
            f"B{n:02d}",
            unique_glob(ch1, f"BEAT_{n:02d}_*_DRAFT_*.md"),
            "mandatory",
            unique_glob(ch1, f"BEAT_{n:02d}_*_SPEC.json"),
        ))
    scenes.extend([
        SceneSource("01", "C02", unique_glob(ch1, "C03_TORRENS_VERSION_OF_DINNER_*DRAFT*.md"), "character_life", unique_glob(ch1, "C03_TORRENS_VERSION_OF_DINNER_*SPEC.json")),
        SceneSource("01", "C03", unique_glob(ch1, "C04_WHAT_THE_MAP_SAYS_*DRAFT*.md"), "character_life", unique_glob(ch1, "C04_WHAT_THE_MAP_SAYS_*SPEC.json")),
        SceneSource("01", "C04", unique_glob(ch1, "C05_NOT_PROFESSIONALLY_*DRAFT*.md"), "character_life", unique_glob(ch1, "C05_NOT_PROFESSIONALLY_*SPEC.json")),
    ])

    ch2 = chapter_dir("02")
    for n in range(1, 16):
        scenes.append(SceneSource("02", f"B{n:02d}", unique_glob(ch2, f"CH02_B{n:02d}_*_DIALOGUE.md"), "mandatory"))
    scenes.append(SceneSource("02", "C05", unique_glob(ch2, "C05_STILL_BURNS_DIALOGUE.md"), "character_life"))

    ch3 = chapter_dir("03")
    for n in range(1, 16):
        scenes.append(SceneSource(
            "03",
            f"B{n:02d}",
            unique_glob(ch3, f"BEAT_{n:02d}_*_DRAFT_*.md"),
            "mandatory",
            unique_glob(ch3, f"BEAT_{n:02d}_*_SPEC.json"),
        ))
    scenes.extend([
        SceneSource("03", "C06", unique_glob(ch3, "H01_NIMERA_TAKES_OVER_A_TABLE_DRAFT_*.md"), "character_life", unique_glob(ch3, "H01_NIMERA_TAKES_OVER_A_TABLE_SPEC.json")),
        SceneSource("03", "C07", unique_glob(ch3, "H03_ILYRA_AND_NIMERA_DRAFT_*.md"), "character_life", unique_glob(ch3, "H03_ILYRA_AND_NIMERA_SPEC.json")),
    ])

    expected_counts = {"00": 8, "01": 15, "02": 16, "03": 17}
    for chapter, expected in expected_counts.items():
        got = sum(1 for scene in scenes if scene.chapter == chapter)
        if got != expected:
            raise CompileError(f"Chapter {int(chapter)} source set changed: expected {expected}, got {got}")
    return scenes


def source_title(text: str, fallback: str) -> str:
    h1 = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == 1:
            h1.append(match.group(2).strip())
    if len(h1) >= 2:
        return h1[1]
    if h1:
        return h1[0]
    return fallback


def load_spec(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise CompileError(f"Invalid scene spec JSON: {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise CompileError(f"Scene spec must be an object: {path.relative_to(ROOT)}")
    return value


def normalize_readiness(value: str) -> str:
    upper = value.strip().upper()
    if upper.startswith("RED"):
        return "RED"
    if upper.startswith("AMBER"):
        return "AMBER"
    return "GREEN"


def scene_mode(scene: SceneSource, source_text: str) -> tuple[str, bool, dict[str, str], dict[str, str]]:
    if scene.scene_kind == "character_life":
        return (
            "character_life_hub_camp",
            True,
            {"during_scene": "not_applicable", "after_scene": "not_applicable"},
            {"control_mode": "hub"},
        )
    # Dialogue never runs during player-controlled traversal. Route dialogue must
    # already be authored as a stop scene before it reaches the runtime compiler.
    # Active combat likewise never hosts spoken dialogue; pre/post battle scenes
    # compile as ordinary authored stop scenes.
    return (
        "full_authored_stop_scene",
        True,
        {"during_scene": "temporarily_suppress_trigger", "after_scene": "restore_prior_pressure"},
        {"control_mode": "exploration"},
    )


def production_cost(spec: dict[str, Any]) -> str:
    raw = str(spec.get("production_cost_ceiling", "economical")).casefold()
    if "bespoke" in raw:
        return "bespoke"
    if "moderate" in raw:
        return "moderate"
    return "economical"


def parse_spoken(scene: SceneSource, source_text: str) -> tuple[list[dict[str, Any]], dict[str, str]]:
    current_section = ""
    beats: list[dict[str, Any]] = []
    labels: dict[str, str] = {}

    for line_no, raw in enumerate(source_text.splitlines(), start=1):
        heading = HEADING_RE.match(raw)
        if heading:
            current_section = heading.group(2).strip()
            continue

        match = DIALOGUE_RE.match(raw)
        if not match:
            continue
        label = match.group(1).strip()
        if not is_spoken_label(label):
            continue

        sid = speaker_id(label)
        labels.setdefault(sid, label)
        beats.append({
            "speaker_id": sid,
            "text": match.group(2).strip(),
            "cues": {
                "pause_ms": 80,
                "interrupt": False,
                "implementation_flags": ["IN_WORLD_DIALOGUE"],
                "source_section": current_section,
                "source_speaker_label": label,
                "source_path": str(scene.source_path.relative_to(ROOT)),
                "source_line": line_no,
            },
        })

    if not beats:
        raise CompileError(f"No spoken dialogue found in {scene.source_path.relative_to(ROOT)}")

    durable = DURABLE_FLAGS.get((scene.chapter, scene.slot_id), [])
    if durable:
        beats[-1]["cues"]["implementation_flags"] = list(dict.fromkeys(
            list(beats[-1]["cues"]["implementation_flags"]) + durable
        ))

    for index, beat in enumerate(beats, start=1):
        beat["beat_id"] = f"CH{scene.chapter}_{scene.slot_id}_L{index:04d}"
    return beats, labels


def scene_identifier(scene: SceneSource, title: str) -> str:
    return f"CH{scene.chapter}_{scene.slot_id}_{slug(title, upper=True)}"[:95].rstrip("_")


def location_identifier(title: str) -> str:
    return f"LOC_{slug(title, upper=True)}"[:95].rstrip("_")


def spoken_fingerprint(beats: list[dict[str, Any]]) -> str:
    payload = "\n".join(f"{beat['speaker_id']}\t{beat['text']}" for beat in beats)
    return sha256_text(payload)


def render_scene(
    scene: SceneSource,
    title: str,
    spec: dict[str, Any],
    beats: list[dict[str, Any]],
    source_sha: str,
    spoken_sha: str,
    participants: list[str],
) -> str:
    scene_id = scene_identifier(scene, title)
    source_text = scene.source_path.read_text(encoding="utf-8")
    mode, movement_lock, encounter_policy, return_to_gameplay = scene_mode(scene, source_text)
    context = spec.get("scene_context_seed", {})
    readiness = normalize_readiness(str(context.get("dialogue_readiness", "GREEN"))) if isinstance(context, dict) else "GREEN"
    story_position = str(spec.get(
        "story_position",
        f"Chapter {int(scene.chapter)} — {scene.slot_id} — {title}",
    ))
    authoring_notes = (
        f"CURRENT runtime dialogue compiled from {scene.source_path.relative_to(ROOT)}. "
        "docs/03_DIALOGUE/PRODUCTION is exact spoken-wording authority; legacy S001-S021 "
        "Resources are not source authority. "
        f"Source SHA-256: {source_sha}. Spoken-sequence SHA-256: {spoken_sha}. "
        f"Spoken lines: {len(beats)}."
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
        f'chapter_id = "chapter_{scene.chapter}"',
        f"scene_kind = {quote(scene.scene_kind)}",
        f"location_id = {quote(location_identifier(title))}",
        f"trigger_id = {quote(f'trigger.chapter_{scene.chapter}.{scene.slot_id.casefold()}')}",
        f"completion_flag = {quote(f'scene.ch{scene.chapter}_{scene.slot_id.casefold()}.complete')}",
        "participants = Array[String]([" + ", ".join(quote(item) for item in participants) + "])",
        f"story_position = {quote(story_position)}",
        f"scene_mode = {quote(mode)}",
        f"movement_lock = {gd_value(movement_lock)}",
        f"dialogue_readiness = {quote(readiness)}",
        f"production_cost_tier = {quote(production_cost(spec))}",
        f"encounter_policy = {gd_value(encounter_policy)}",
        f"return_to_gameplay = {gd_value(return_to_gameplay)}",
        'cutscene_tier = "C0"',
        'vfx_tier = "V1"',
        f"authoring_notes = {quote(authoring_notes)}",
        "beats = [",
        ",\n".join(rendered_beats),
        "]",
        "",
    ])


def render_registry(labels: dict[str, str]) -> str:
    entries = [
        {"character_id": sid, "display_name": display_name(label), "portraits": {}}
        for sid, label in labels.items()
    ]
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


def expected_outputs() -> tuple[dict[Path, str], dict[str, Any]]:
    outputs: dict[Path, str] = {}
    manifest: dict[str, Any] = {
        "schema": "diyse_current_runtime_dialogue_manifest_v1",
        "source_authority": "docs/03_DIALOGUE/PRODUCTION",
        "expected_total_spoken": EXPECTED_TOTAL_SPOKEN,
        "chapters": {},
    }
    total_spoken = 0
    global_sequence: list[str] = []

    by_chapter: dict[str, list[SceneSource]] = {}
    for scene in source_set():
        by_chapter.setdefault(scene.chapter, []).append(scene)

    for chapter in ("00", "01", "02", "03"):
        chapter_out = OUT_ROOT / f"chapter_{chapter}"
        labels: dict[str, str] = {}
        chapter_manifest = {
            "registry_path": f"res://game/content/dialogue/current/chapter_{chapter}/chapter_{chapter}_dialogue_registry.tres",
            "scenes": [],
        }

        for scene in by_chapter[chapter]:
            source_text = scene.source_path.read_text(encoding="utf-8")
            spec = load_spec(scene.spec_path)
            title = source_title(source_text, scene.slot_id)
            beats, scene_labels = parse_spoken(scene, source_text)
            for sid, label in scene_labels.items():
                labels.setdefault(sid, label)
            if isinstance(spec.get("participants"), list):
                for participant in spec["participants"]:
                    sid = slug(str(participant))
                    labels.setdefault(sid, str(participant).replace("_", " "))

            participants: list[str] = []
            if isinstance(spec.get("participants"), list):
                for participant in spec["participants"]:
                    sid = slug(str(participant))
                    if sid not in participants:
                        participants.append(sid)
            for beat in beats:
                sid = beat["speaker_id"]
                if sid not in participants:
                    participants.append(sid)

            source_sha = sha256_text(source_text)
            spoken_sha = spoken_fingerprint(beats)
            total_spoken += len(beats)
            global_sequence.extend(f"{beat['speaker_id']}\t{beat['text']}" for beat in beats)

            resource_path = chapter_out / f"{scene.slot_id}.tres"
            outputs[resource_path] = render_scene(
                scene, title, spec, beats, source_sha, spoken_sha, participants
            )

            chapter_manifest["scenes"].append({
                "slot_id": scene.slot_id,
                "scene_id": scene_identifier(scene, title),
                "title": title,
                "scene_kind": scene.scene_kind,
                "source_path": str(scene.source_path.relative_to(ROOT)),
                "source_sha256": source_sha,
                "spoken_lines": len(beats),
                "spoken_sha256": spoken_sha,
                "resource_path": f"res://{resource_path.relative_to(ROOT).as_posix()}",
            })

        registry_path = chapter_out / f"chapter_{chapter}_dialogue_registry.tres"
        outputs[registry_path] = render_registry(labels)
        manifest["chapters"][f"chapter_{chapter}"] = chapter_manifest

    manifest["total_spoken"] = total_spoken
    manifest["global_spoken_sha256"] = sha256_text("\n".join(global_sequence))
    if total_spoken != EXPECTED_TOTAL_SPOKEN:
        raise CompileError(
            f"Current runtime compile found {total_spoken} spoken lines; expected {EXPECTED_TOTAL_SPOKEN}."
        )

    readme = """# Current runtime dialogue mirror

This directory is generated from docs/03_DIALOGUE/PRODUCTION/CHAPTER_00 through
CHAPTER_03. Those atomics remain exact spoken-wording authority.

manifest.json is the game-facing catalog for the current Chapters 0-3 dialogue.
The older sibling game/content/dialogue/chapter_00 through chapter_03 S-scene
Resources are retained only as legacy implementation/proof assets and must not be used
as current dialogue wording authority.

Regenerate with:

python tools/dialogue/compile_current_runtime_dialogue.py
"""
    outputs[OUT_ROOT / "README.md"] = readme
    outputs[OUT_ROOT / "manifest.json"] = json.dumps(
        manifest, ensure_ascii=False, sort_keys=True, indent=2
    ) + "\n"
    return outputs, manifest


def write_outputs(outputs: dict[Path, str]) -> None:
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    for path, rendered in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")


def check_outputs(outputs: dict[Path, str]) -> list[str]:
    failures: list[str] = []
    expected_paths = {path.relative_to(OUT_ROOT) for path in outputs}
    actual_paths = {
        path.relative_to(OUT_ROOT)
        for path in OUT_ROOT.rglob("*")
        if path.is_file()
    } if OUT_ROOT.exists() else set()

    for path in sorted(expected_paths - actual_paths):
        failures.append(f"missing generated runtime file: {path}")
    for path in sorted(actual_paths - expected_paths):
        failures.append(f"unexpected generated runtime file: {path}")

    for path, wanted in outputs.items():
        if not path.is_file():
            continue
        got = path.read_text(encoding="utf-8")
        if got != wanted:
            failures.append(f"stale generated runtime file: {path.relative_to(ROOT)}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify committed runtime mirror without writing")
    args = parser.parse_args()

    try:
        outputs, manifest = expected_outputs()
    except CompileError as exc:
        print(f"runtime dialogue compile error: {exc}", file=sys.stderr)
        return 2

    if args.check:
        failures = check_outputs(outputs)
        if failures:
            for failure in failures:
                print(failure, file=sys.stderr)
            return 1
        print(
            f"Current runtime dialogue mirror is synchronized: "
            f"{manifest['total_spoken']} spoken lines across "
            f"{sum(len(ch['scenes']) for ch in manifest['chapters'].values())} scenes."
        )
        return 0

    write_outputs(outputs)
    print(
        f"Compiled current runtime dialogue mirror: "
        f"{manifest['total_spoken']} spoken lines across "
        f"{sum(len(ch['scenes']) for ch in manifest['chapters'].values())} scenes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
