#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/dialogue/compile_scene_authority.py"
FIXTURE_PATH = ROOT / "tests/dialogue/fixtures/authority_ch1_brackenwall_protocol.json"

spec = importlib.util.spec_from_file_location("diyse_scene_authority_compiler", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load scene authority compiler module")
compiler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiler)


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_compile_error(scene_spec: dict, message: str) -> None:
    try:
        compiler.compile_spec_data(scene_spec, root=ROOT)
    except compiler.CompileError:
        return
    raise AssertionError(message)


def main() -> int:
    source_spec = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    compiled = compiler.compile_spec_data(source_spec, root=ROOT)

    expect(compiled["schema"] == "diyse_scene_authority_compilation_v1", "wrong compilation schema")
    expect(compiled["production_ready"] is False, "proof fixture must not claim production readiness")

    request = compiled["request_seed"]
    expect(request["scene_id"] == "PROOF_CH1_BRACKENWALL_PROTOCOL", "scene ID changed")
    expect(request["canon_snapshot_id"] == "v2.20-Audit135", "current canon snapshot was not derived")
    expect(request["participants"] == ["cyanis", "ilyra", "maevra"], "participant order changed")
    expect(request["exact_line_anchors"] == [], "fixture should not invent exact anchors")
    expect(request["current_floor_state"] == {}, "compiler must not invent live floor state")
    for cid in request["participants"]:
        expect(
            request["person_runtime_contexts"][cid]["memory_authorization"] == {"mode": "none"},
            f"{cid} should default to no persistent story memory without explicit authorization",
        )

    packet = request["authority_packet"]
    expect(packet["schema"] == "diyse_scene_authority_packet_v1", "wrong authority packet schema")
    expect(len(packet["bundle_sha256"]) == 64, "authority bundle fingerprint is malformed")
    expect(packet["compiler_guards"]["archive_sources_rejected"] is True, "archive guard missing")
    expect(packet["compiler_guards"]["runtime_state_not_invented"] is True, "runtime-state guard missing")

    source_records = packet["source_records"]
    paths = [record["path"] for record in source_records]
    expect(
        "docs/02_STORY/CHAPTERS/CHAPTER_01.md" in paths,
        "Chapter 1 owning story source was not compiled",
    )
    expect(
        "docs/01_CHARACTERS/RELATIONSHIPS/PERMANENT_SIX_RELATIONSHIP_MAP.md" in paths,
        "permanent-six relationship authority should be included when two permanent members are present",
    )
    for path in paths:
        expect(not path.startswith("docs/99_ARCHIVE/"), f"archive source leaked into packet: {path}")
        expect(not path.startswith("docs/90_WORKING/"), f"working source leaked into packet: {path}")
        expect(
            not path.startswith("docs/03_DIALOGUE/LINE_COMPLETE/"),
            f"historical line-complete source leaked into packet: {path}",
        )

    chapter_record = next(
        record for record in source_records if record["path"] == "docs/02_STORY/CHAPTERS/CHAPTER_01.md"
    )
    headings = [selection["section"] for selection in chapter_record["selections"]]
    expect("Beat 1 — Brackenwall / Protocol" in headings, "requested story section was not extracted")
    beat_text = next(
        selection["text"]
        for selection in chapter_record["selections"]
        if selection["section"] == "Beat 1 — Brackenwall / Protocol"
    )
    expect(
        "attempted transfer/storage separates the Card from Cyanis;" in beat_text,
        "compiled story section does not contain the current Brackenwall transfer state",
    )
    expect(
        "Card stays with Cyanis; Ilyra monitors only real changes;" in beat_text,
        "compiled story section lost the current Card custody boundary",
    )

    profiles = request["participant_profiles"]
    expect(profiles["cyanis"]["source_path"].endswith("/Cyanis.md"), "Cyanis profile route is wrong")
    expect(profiles["ilyra"]["source_path"].endswith("/Ilyra.md"), "Ilyra profile route is wrong")
    expect(profiles["maevra"]["source_path"].endswith("/Maevra.md"), "Maevra profile route is wrong")
    for profile in profiles.values():
        expect(len(profile["file_sha256"]) == 64, "participant source fingerprint is malformed")
        expect(bool(profile["authority_text"].strip()), "participant authority text is empty")

    historical = json.loads(json.dumps(source_spec))
    historical["additional_authority_sources"].append(
        {
            "path": "docs/03_DIALOGUE/LINE_COMPLETE/retired.md",
            "whole_file": True,
        }
    )
    expect_compile_error(historical, "historical line-complete authority must be rejected")

    missing_heading = json.loads(json.dumps(source_spec))
    missing_heading["story_sources"][0]["sections"] = ["THIS HEADING DOES NOT EXIST"]
    expect_compile_error(missing_heading, "missing section must fail instead of widening retrieval")

    anchored = json.loads(json.dumps(source_spec))
    anchored["participants"].append("torren")
    anchored["exact_line_anchors"] = [
        {
            "speaker_id": "cyanis",
            "text": "I bet you use that cape to sneak up on the goats you fuck.",
            "required": True,
            "source": {
                "path": "docs/03_DIALOGUE/PRODUCTION/CHAPTER_03/H01_NIMERA_TAKES_OVER_A_TABLE_DRAFT_A.md",
                "whole_file": True,
                "role": "current_exact_anchor"
            }
        }
    ]
    anchored_compiled = compiler.compile_spec_data(anchored, root=ROOT)
    expect(
        anchored_compiled["request_seed"]["exact_line_anchors"][0]["text"]
        == "I bet you use that cape to sneak up on the goats you fuck.",
        "verified current exact anchor was not preserved verbatim",
    )

    bad_anchor = json.loads(json.dumps(anchored))
    bad_anchor["exact_line_anchors"][0]["text"] = "This line is not current authority."
    expect_compile_error(bad_anchor, "unsupported exact anchor must fail verification")

    explicit_context = json.loads(json.dumps(source_spec))
    explicit_context["person_runtime_contexts"] = {
        "ilyra": {
            "memory_authorization": {
                "mode": "scene_ids",
                "authorized_scene_ids": ["CH00_S05", "CH01_S01"],
            },
            "relationship_runtime_state": {
                "chronology_stage": "chapter_01_established_party",
                "silence_comfort": "established",
            },
            "epistemic_state": {
                "route_hypothesis": {
                    "status": "inference",
                    "value": "the road may be intentionally avoided",
                }
            },
            "scene_local_state": {
                "immediate_wants": ["get through the checkpoint without unnecessary escalation"],
            },
        }
    }
    expect_compile_error(
        explicit_context,
        "Unproven manual runtime state must migrate to source-backed assertions",
    )
    explicit_context["person_runtime_contexts"] = {
        "ilyra": {"memory_authorization": {"mode": "scene_ids", "authorized_scene_ids": ["CH00_S05"]}}
    }
    explicit_compiled = compiler.compile_spec_data(explicit_context, root=ROOT)
    expect(
        explicit_compiled["request_seed"]["context_construction"]["memory_policies"]["ilyra"]
        == explicit_context["person_runtime_contexts"]["ilyra"]["memory_authorization"],
        "Explicit memory authorization policy must survive in protected construction inputs",
    )
    expect(
        explicit_compiled["request_seed"]["person_runtime_contexts"]["ilyra"]["hard_context"]["participant_id"] == "ilyra",
        "Compiler must automatically construct per-person hard context",
    )

    nonparticipant_context = json.loads(json.dumps(source_spec))
    nonparticipant_context["person_runtime_contexts"] = {
        "seyrik": {"memory_authorization": {"mode": "none"}}
    }
    expect_compile_error(
        nonparticipant_context,
        "person runtime context for a nonparticipant must fail",
    )

    malformed_context = json.loads(json.dumps(source_spec))
    malformed_context["person_runtime_contexts"] = {
        "ilyra": {"memory_authorization": ["not", "an", "object"]}
    }
    expect_compile_error(
        malformed_context,
        "malformed memory authorization must fail",
    )

    chapter4_spec_path = ROOT / "docs/03_DIALOGUE/PRODUCTION/CHAPTER_04/BEAT_01_CRESTHAVEN_MORNING_DISTURBANCE_SPEC.json"
    chapter4 = compiler.compile_spec_file(chapter4_spec_path, root=ROOT)
    chapter4_request = chapter4["request_seed"]
    expect(
        chapter4_request["scene_id"] == "CH04_BEAT01_CRESTHAVEN_MORNING_DISTURBANCE",
        "Chapter 4 Beat 1 scene authority did not compile with the expected ID",
    )
    expect(
        chapter4_request["participants"] == ["cyanis", "ilyra", "torren", "nimera"],
        "Chapter 4 Beat 1 participant order changed",
    )
    expect(
        chapter4_request["current_floor_state"]["last_sentinel_state"]
        == "LAST SENTINEL CONFIRMED is known; no verified modern manifestation; not yet Recovered",
        "Chapter 4 Beat 1 lost the unrecovered Last Sentinel opening state",
    )
    expect(
        chapter4_request["person_runtime_contexts"]["torren"]["epistemic_state"]["creature_identity"]["status"]
        == "inference",
        "Torren must not enter Beat 1 with Elder Thornhide identity promoted to known fact",
    )
    for cid in chapter4_request["participants"]:
        expect(
            chapter4_request["person_runtime_contexts"][cid]["memory_authorization"] == {"mode": "none"},
            f"Chapter 4 Beat 1 must keep persistent story memory deny-by-default for {cid}",
        )

    print("Diyse scene authority compiler validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
