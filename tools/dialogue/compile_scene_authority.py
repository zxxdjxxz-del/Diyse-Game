#!/usr/bin/env python3
"""Compile current Diyse repository authority into a Scene Orchestrator request seed.

This tool is intentionally deterministic and retrieval-free. A scene spec names the exact
current owning Markdown sections that matter for the scene. The compiler then:
- verifies every source lives in active current authority rather than archive/working/history;
- extracts exact Markdown sections without silently widening to the whole file;
- packages current participant character authority;
- verifies any preserved exact-line anchor against a current 03_DIALOGUE source;
- fingerprints every source, participant profile, scene spec, and resulting bundle;
- emits a request object accepted by the current Dialogue Scene Orchestrator.

The compiler does not invent live gameplay state, map state, encounter pressure, memories,
or staging tiers. Those remain runtime/game-side inputs.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SPEC_SCHEMA = "diyse_scene_authority_spec_v1"
AUTHORITY_PACKET_SCHEMA = "diyse_scene_authority_packet_v1"
COMPILER_VERSION = "1.2.0"

CANON_STATUS_PATH = "docs/00_MASTER_CONTROL/CURRENT_CANON_STATUS.md"

SAFE_CHARACTER_ID = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
SAFE_SCENE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,95}$")
CHAPTER_ID = re.compile(r"^chapter_(0[0-9]|1[0-3])$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

# These are routing paths only. The files themselves remain the character authority.
CHARACTER_SOURCES = {
    "cyanis": "docs/01_CHARACTERS/PLAYABLE/Cyanis.md",
    "ilyra": "docs/01_CHARACTERS/PLAYABLE/Ilyra.md",
    "torren": "docs/01_CHARACTERS/PLAYABLE/Torren.md",
    "nimera": "docs/01_CHARACTERS/PLAYABLE/Nimera.md",
    "vaelira": "docs/01_CHARACTERS/PLAYABLE/Vaelira.md",
    "seyrik": "docs/01_CHARACTERS/PLAYABLE/Seyrik.md",
    "maevra": "docs/01_CHARACTERS/SUPPORTING/Maevra.md",
    "kessara": "docs/01_CHARACTERS/SUPPORTING/Kessara.md",
    "talia": "docs/01_CHARACTERS/SUPPORTING/Talia_Rell.md",
    "edda": "docs/01_CHARACTERS/SUPPORTING/Edda_Harth.md",
    "mirena": "docs/01_CHARACTERS/SUPPORTING/Crown_Princess_Mirena_Ceryth.md",
    "lysara": "docs/01_CHARACTERS/SUPPORTING/Queen_Lysara_Ceryth.md",
    "alaric": "docs/01_CHARACTERS/SUPPORTING/Prince_Alaric_Ceryth.md",
    "nalia": "docs/01_CHARACTERS/SUPPORTING/Princess_Nalia_Ceryth.md",
    "othmar": "docs/01_CHARACTERS/ANTAGONISTS/Chancellor_Othmar_Calder.md",
    "rhazek": "docs/01_CHARACTERS/ANTAGONISTS/Commander_Rhazek.md",
    "zevraya": "docs/01_CHARACTERS/ANTAGONISTS/Matron_Zevraya.md",
    "varkesh": "docs/01_CHARACTERS/ANTAGONISTS/Marshal_Varkesh.md",
    "vaelkor": "docs/01_CHARACTERS/ANTAGONISTS/Emperor_Vaelkor_Draeven.md",
    "reconstituted_entity": "docs/01_CHARACTERS/ANTAGONISTS/Reconstituted_Entity.md",
}

PERMANENT_SIX = {"cyanis", "ilyra", "torren", "nimera", "vaelira", "seyrik"}
RELATIONSHIP_MAP_PATH = "docs/01_CHARACTERS/RELATIONSHIPS/PERMANENT_SIX_RELATIONSHIP_MAP.md"

# Current cross-domain guardrails that are small enough and important enough to package
# automatically for every authored story scene. Exact scene facts still come from scene specs.
DEFAULT_GLOBAL_SOURCES: list[dict[str, Any]] = [
    {
        "path": "docs/00_MASTER_CONTROL/CURRENT_CANON_STATUS.md",
        "sections": [
            "Repository / authority state",
            "Current project locks",
            "Current Card / Face locks",
            "Current class / progression locks",
        ],
        "role": "master_control_guardrail",
    },
    {
        "path": "docs/00_MASTER_CONTROL/AUTHORITY_AND_CHANGE_CONTROL.md",
        "sections": ["Current authority precedence", "No silent resurrection"],
        "role": "authority_precedence",
    },
    {
        "path": "docs/00_MASTER_CONTROL/CANON_QUICK_REFERENCE.md",
        "sections": ["Party", "Chapters", "Combat", "Cards", "Economy"],
        "role": "current_terminology_guardrail",
    },
    {
        "path": "docs/02_STORY/DIALOGUE_HANDOFF.md",
        "sections": ["Global chapter-end cleanup handoff", "Historical closed dialogue", "Later dialogue"],
        "role": "story_dialogue_handoff",
    },
    {
        "path": "docs/03_DIALOGUE/DIALOGUE_MASTER_INDEX.md",
        "sections": ["Dialogue Engine hard rules"],
        "role": "dialogue_regeneration_rule",
    },
    {
        "path": "docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md",
        "sections": [
            "Critical current override: Story Prime access",
            "Critical current override: currency",
            "Critical current override: final chapter IDs",
        ],
        "role": "implementation_guardrail",
    },
]

FORBIDDEN_AUTHORITY_PREFIXES = (
    "docs/90_WORKING/",
    "docs/99_ARCHIVE/",
    "docs/03_DIALOGUE/LINE_COMPLETE/",
    "docs/chapters/",
)

FORBIDDEN_AUTHORITY_PATHS = {
    # This current file is an index of historical exact-source provenance, not scene authority.
    "docs/03_DIALOGUE/EXACT_SOURCE_MANIFEST.md",
}


class CompileError(RuntimeError):
    pass


def _norm_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _normalize_character_id(value: str) -> str:
    cid = value.strip().lower().replace(" ", "_")
    if not SAFE_CHARACTER_ID.fullmatch(cid):
        raise CompileError(f"Invalid participant ID: {value!r}")
    return cid


def _normalize_repo_path(value: str) -> str:
    raw = value.strip().replace("\\", "/")
    path = Path(raw)
    if not raw or path.is_absolute() or ".." in path.parts:
        raise CompileError(f"Unsafe repository path: {value!r}")
    normalized = path.as_posix()
    if not normalized.startswith("docs/"):
        raise CompileError(f"Authority source must live under docs/: {normalized}")
    if normalized in FORBIDDEN_AUTHORITY_PATHS:
        raise CompileError(f"Historical provenance index is not scene authority: {normalized}")
    for prefix in FORBIDDEN_AUTHORITY_PREFIXES:
        if normalized.startswith(prefix):
            raise CompileError(
                f"Historical/working source is not legal current scene authority: {normalized}"
            )
    return normalized


def _read_text(root: Path, repo_path: str) -> str:
    normalized = _normalize_repo_path(repo_path)
    disk_path = root / normalized
    if not disk_path.is_file():
        raise CompileError(f"Authority source does not exist: {normalized}")
    return disk_path.read_text(encoding="utf-8")


def extract_markdown_section(text: str, heading: str) -> str:
    wanted = _norm_heading(heading)
    lines = text.splitlines()
    matches: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match and _norm_heading(match.group(2)) == wanted:
            matches.append((index, len(match.group(1))))

    if not matches:
        raise CompileError(f"Markdown heading not found: {heading!r}")
    if len(matches) > 1:
        raise CompileError(f"Markdown heading is ambiguous: {heading!r}")

    start, level = matches[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        match = HEADING_RE.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    return "\n".join(lines[start:end]).strip() + "\n"


def _compile_source_record(root: Path, source: dict[str, Any], category: str) -> dict[str, Any]:
    if not isinstance(source, dict):
        raise CompileError(f"{category} source must be an object")
    path = _normalize_repo_path(str(source.get("path", "")))
    full_text = _read_text(root, path)
    role = str(source.get("role", category)).strip() or category

    whole_file = bool(source.get("whole_file", False))
    sections_value = source.get("sections", [])
    if isinstance(sections_value, str):
        sections = [sections_value]
    elif isinstance(sections_value, list):
        sections = [str(value) for value in sections_value]
    else:
        raise CompileError(f"{path}: sections must be a string or list")

    if whole_file and sections:
        raise CompileError(f"{path}: choose whole_file or sections, not both")
    if not whole_file and not sections:
        raise CompileError(f"{path}: source requires explicit sections or whole_file=true")

    selections: list[dict[str, Any]] = []
    if whole_file:
        selections.append(
            {
                "section": None,
                "text": full_text,
                "sha256": _sha256_text(full_text),
            }
        )
    else:
        for heading in sections:
            selected = extract_markdown_section(full_text, heading)
            selections.append(
                {
                    "section": heading,
                    "text": selected,
                    "sha256": _sha256_text(selected),
                }
            )

    return {
        "category": category,
        "role": role,
        "path": path,
        "file_sha256": _sha256_text(full_text),
        "selections": selections,
    }


def _derive_canon_snapshot_id(root: Path) -> str:
    status = _read_text(root, CANON_STATUS_PATH)
    match = re.search(r"v(\d+\.\d+)\s*/\s*Audit(\d+)", status, flags=re.IGNORECASE)
    if not match:
        raise CompileError("Could not derive current canon snapshot from CURRENT_CANON_STATUS.md")
    return f"v{match.group(1)}-Audit{match.group(2)}"


def _character_source_map(spec: dict[str, Any]) -> dict[str, str]:
    result = dict(CHARACTER_SOURCES)
    overrides = spec.get("participant_profile_sources", {})
    if not isinstance(overrides, dict):
        raise CompileError("participant_profile_sources must be an object")
    for raw_id, raw_path in overrides.items():
        cid = _normalize_character_id(str(raw_id))
        path = _normalize_repo_path(str(raw_path))
        if not path.startswith("docs/01_CHARACTERS/"):
            raise CompileError(f"Participant profile source must be in 01_CHARACTERS: {path}")
        result[cid] = path
    return result


def _compile_participant_profiles(
    root: Path,
    participants: list[str],
    source_map: dict[str, str],
) -> dict[str, dict[str, Any]]:
    profiles: dict[str, dict[str, Any]] = {}
    for cid in participants:
        path = source_map.get(cid)
        if not path:
            raise CompileError(
                f"No current character authority route for {cid!r}; add participant_profile_sources"
            )
        text = _read_text(root, path)
        profiles[cid] = {
            "schema": "diyse_participant_profile_source_v1",
            "character_id": cid,
            "source_path": path,
            "file_sha256": _sha256_text(text),
            "authority_text": text,
        }
    return profiles


def _participant_profile_fingerprints(
    profiles: dict[str, dict[str, Any]],
) -> dict[str, dict[str, str]]:
    return {
        cid: {
            "source_path": str(profile["source_path"]),
            "file_sha256": str(profile["file_sha256"]),
        }
        for cid, profile in sorted(profiles.items())
    }


def _compile_exact_anchors(
    root: Path,
    spec: dict[str, Any],
    participants: list[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    anchors_value = spec.get("exact_line_anchors", [])
    if not isinstance(anchors_value, list):
        raise CompileError("exact_line_anchors must be a list")

    anchors: list[dict[str, Any]] = []
    provenance: list[dict[str, Any]] = []
    for index, raw in enumerate(anchors_value, start=1):
        if not isinstance(raw, dict):
            raise CompileError(f"exact_line_anchors[{index}] must be an object")
        speaker_id = _normalize_character_id(str(raw.get("speaker_id", "")))
        if speaker_id not in participants:
            raise CompileError(f"Exact-line anchor speaker is not a participant: {speaker_id}")
        text = str(raw.get("text", ""))
        if not text:
            raise CompileError(f"exact_line_anchors[{index}] text is required")
        source = raw.get("source")
        if not isinstance(source, dict):
            raise CompileError(
                f"exact_line_anchors[{index}] requires a current 03_DIALOGUE source proof"
            )
        source_path = _normalize_repo_path(str(source.get("path", "")))
        if not source_path.startswith("docs/03_DIALOGUE/"):
            raise CompileError(f"Exact-line anchor source must live in current 03_DIALOGUE: {source_path}")
        source_record = _compile_source_record(root, source, "exact_anchor_provenance")
        searchable = "\n".join(
            selection["text"] for selection in source_record["selections"]
        )
        if text not in searchable:
            raise CompileError(
                f"Exact-line anchor text was not found verbatim in its current source: {text!r}"
            )
        anchors.append(
            {
                "speaker_id": speaker_id,
                "text": text,
                "required": bool(raw.get("required", True)),
                "note": str(raw.get("note", "")).strip() or None,
            }
        )
        provenance.append(source_record)
    return anchors, provenance


def validate_spec(spec: dict[str, Any]) -> None:
    if not isinstance(spec, dict):
        raise CompileError("Scene authority spec must be a JSON object")
    if spec.get("schema") != SPEC_SCHEMA:
        raise CompileError(f"Unsupported scene authority spec schema: {spec.get('schema')!r}")

    scene_id = str(spec.get("scene_id", ""))
    if not SAFE_SCENE_ID.fullmatch(scene_id):
        raise CompileError(f"Invalid scene_id: {scene_id!r}")
    chapter_id = str(spec.get("chapter_id", ""))
    if not CHAPTER_ID.fullmatch(chapter_id):
        raise CompileError(f"Invalid chapter_id: {chapter_id!r}")
    if not str(spec.get("story_position", "")).strip():
        raise CompileError("story_position is required")
    if not str(spec.get("scene_purpose", "")).strip():
        raise CompileError("scene_purpose is required")

    continuity_namespace = str(spec.get("continuity_namespace", "story"))
    if continuity_namespace not in {"story", "sandbox"}:
        raise CompileError("continuity_namespace must be story or sandbox")
    if "production_ready" in spec and not isinstance(spec["production_ready"], bool):
        raise CompileError("production_ready must be a bool")

    participants = spec.get("participants")
    if not isinstance(participants, list) or not participants:
        raise CompileError("participants must be a non-empty list")

    story_sources = spec.get("story_sources")
    if not isinstance(story_sources, list) or not story_sources:
        raise CompileError("story_sources must be a non-empty list")
    for source in story_sources:
        if not isinstance(source, dict):
            raise CompileError("story_sources entries must be objects")
        path = _normalize_repo_path(str(source.get("path", "")))
        if not path.startswith("docs/02_STORY/"):
            raise CompileError(f"Story source must live in current 02_STORY: {path}")

    additional = spec.get("additional_authority_sources", [])
    if not isinstance(additional, list):
        raise CompileError("additional_authority_sources must be a list")
    if not isinstance(spec.get("scene_context_seed", {}), dict):
        raise CompileError("scene_context_seed must be an object")
    if not isinstance(spec.get("person_runtime_contexts", {}), dict):
        raise CompileError("person_runtime_contexts must be an object")
    for raw_id, raw_context in spec.get("person_runtime_contexts", {}).items():
        _normalize_character_id(str(raw_id))
        if not isinstance(raw_context, dict):
            raise CompileError(
                f"person_runtime_contexts[{raw_id!r}] must be an object"
            )
        memory_policy = raw_context.get("memory_authorization", {})
        if memory_policy is not None and not isinstance(memory_policy, dict):
            raise CompileError(
                f"person_runtime_contexts[{raw_id!r}].memory_authorization must be an object"
            )
    if not isinstance(spec.get("current_floor_state", {}), dict):
        raise CompileError("current_floor_state must be an object")
    if not isinstance(spec.get("allowed_information_transfers", []), list):
        raise CompileError("allowed_information_transfers must be a list")

    try:
        max_beats = int(spec.get("max_beats", 18))
    except (TypeError, ValueError) as exc:
        raise CompileError("max_beats must be an integer") from exc
    if max_beats < 1 or max_beats > 32:
        raise CompileError("max_beats must be between 1 and 32")
    if str(spec.get("production_cost_ceiling", "economical")) not in {
        "economical",
        "moderate",
        "bespoke",
    }:
        raise CompileError("production_cost_ceiling must be economical, moderate, or bespoke")


def compile_spec_data(spec: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    validate_spec(spec)
    canon_snapshot_id = _derive_canon_snapshot_id(root)

    participants: list[str] = []
    for raw in spec["participants"]:
        cid = _normalize_character_id(str(raw))
        if cid not in participants:
            participants.append(cid)

    person_runtime_contexts: dict[str, dict[str, Any]] = {}
    for raw_id, raw_context in spec.get("person_runtime_contexts", {}).items():
        cid = _normalize_character_id(str(raw_id))
        if cid not in participants:
            raise CompileError(
                f"person_runtime_contexts contains nonparticipant character: {cid}"
            )
        person_runtime_contexts[cid] = copy.deepcopy(raw_context)

    # Safe default: authored story scenes do not receive persistent story memory unless
    # the scene spec explicitly authorizes it. The Orchestrator adds the hard scene
    # identity context and other empty runtime dimensions as needed.
    for cid in participants:
        context = person_runtime_contexts.setdefault(cid, {})
        context.setdefault("memory_authorization", {"mode": "none"})

    source_records: list[dict[str, Any]] = []
    for source in DEFAULT_GLOBAL_SOURCES:
        source_records.append(_compile_source_record(root, source, "global_guardrail"))
    for source in spec["story_sources"]:
        source_records.append(_compile_source_record(root, source, "story_authority"))
    for source in spec.get("additional_authority_sources", []):
        source_records.append(_compile_source_record(root, source, "scene_specific_authority"))

    permanent_present = [cid for cid in participants if cid in PERMANENT_SIX]
    if len(permanent_present) >= 2:
        source_records.append(
            _compile_source_record(
                root,
                {
                    "path": RELATIONSHIP_MAP_PATH,
                    "whole_file": True,
                    "role": "permanent_six_relationship_authority",
                },
                "relationship_authority",
            )
        )

    source_map = _character_source_map(spec)
    participant_profiles = _compile_participant_profiles(root, participants, source_map)
    participant_fingerprints = _participant_profile_fingerprints(participant_profiles)
    anchors, anchor_provenance = _compile_exact_anchors(root, spec, participants)
    source_records.extend(anchor_provenance)

    spec_sha256 = _sha256_text(_canonical_json(spec))
    authority_packet: dict[str, Any] = {
        "schema": AUTHORITY_PACKET_SCHEMA,
        "compiler_version": COMPILER_VERSION,
        "canon_snapshot_id": canon_snapshot_id,
        "scene_id": spec["scene_id"],
        "chapter_id": spec["chapter_id"],
        "scene_spec_sha256": spec_sha256,
        "participant_profile_sources": participant_fingerprints,
        "source_records": source_records,
        "compiler_guards": {
            "active_docs_only": True,
            "archive_sources_rejected": True,
            "working_sources_rejected": True,
            "historical_line_complete_sources_rejected": True,
            "historical_exact_source_manifest_rejected": True,
            "exact_anchors_require_current_03_dialogue_proof": True,
            "missing_markdown_section_is_fatal": True,
            "no_silent_whole_file_fallback": True,
            "runtime_state_not_invented": True,
        },
    }
    authority_packet["bundle_sha256"] = _sha256_text(_canonical_json(authority_packet))

    request_id = str(spec.get("request_id", "")).strip()
    if not request_id:
        request_id = f"authority:{spec['scene_id']}:{authority_packet['bundle_sha256'][:12]}"

    request_seed = {
        "request_id": request_id,
        "scene_id": spec["scene_id"],
        "continuity_namespace": str(spec.get("continuity_namespace", "story")),
        "story_position": spec["story_position"],
        "canon_snapshot_id": canon_snapshot_id,
        "participants": participants,
        "participant_profiles": participant_profiles,
        "person_runtime_contexts": person_runtime_contexts,
        "scene_purpose": spec["scene_purpose"],
        "authority_packet": authority_packet,
        "scene_context": copy.deepcopy(spec.get("scene_context_seed", {})),
        "current_floor_state": copy.deepcopy(spec.get("current_floor_state", {})),
        "allowed_information_transfers": copy.deepcopy(
            spec.get("allowed_information_transfers", [])
        ),
        "exact_line_anchors": anchors,
        "max_beats": int(spec.get("max_beats", 18)),
        "production_cost_ceiling": str(spec.get("production_cost_ceiling", "economical")),
    }

    return {
        "schema": "diyse_scene_authority_compilation_v1",
        "compiler_version": COMPILER_VERSION,
        "production_ready": bool(spec.get("production_ready", True)),
        "request_seed": request_seed,
        "dynamic_runtime_requirements": [
            "live persistent Person-Agent revisions/state and safe memory indexes are fetched by the Orchestrator",
            "persistent story memory is unavailable unless person_runtime_contexts explicitly authorizes it",
            "historical/regeneration scenes should authorize memory by explicit IDs or source scene IDs rather than all_committed_story",
            "current recent-gameplay/combat/fatigue state must be supplied or merged at build time when relevant",
            "live encounter pressure must be supplied at build time when relevant",
            "runtime map/cell/area-phase facts must be supplied when they are not already locked by the scene spec",
            "game-side cutscene/VFX tiers remain explicit authoring metadata and are not inferred here",
        ],
    }


def compile_spec_file(path: Path, root: Path = ROOT) -> dict[str, Any]:
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CompileError(f"Scene spec does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CompileError(f"Scene spec is not valid JSON: {path}: {exc}") from exc
    return compile_spec_data(spec, root=root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Path to diyse_scene_authority_spec_v1 JSON")
    parser.add_argument("--output", "-o", type=Path, help="Write compiled JSON to this path")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    args = parser.parse_args(argv)

    try:
        compiled = compile_spec_file(args.spec)
    except CompileError as exc:
        print(f"authority compiler error: {exc}", file=sys.stderr)
        return 2

    if args.compact:
        rendered = json.dumps(compiled, ensure_ascii=False, sort_keys=True)
    else:
        rendered = json.dumps(compiled, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
