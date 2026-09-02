from __future__ import annotations

import json

from tools.diysim.cli import main


def test_progression_audit_chapter0_json_is_source_complete(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "0",
        "--format",
        "json",
        "--strict",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert [row["Character"] for row in payload] == ["Cyanis", "Ilyra"]
    assert all(row["Authority Complete"] for row in payload)
    assert payload[0]["Class Selection"] == "Base floor"
    assert payload[0]["HP"] == 231
    assert payload[1]["SPR"] == 59


def test_progression_audit_markdown_has_requested_stat_columns(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "0",
        "--format",
        "markdown",
    ])
    output = capsys.readouterr().out
    assert exit_code == 0
    assert "| Chapter | Checkpoint | Route | Character |" in output
    assert "| HP | MP | ATK | MAG | DEF | SPR | SPD | EVA | Status Resistance |" in output
    assert "Crestblade" in output
    assert "Warding Focus" in output


def test_progression_audit_strict_reports_later_authority_gap(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "2",
        "--character",
        "Cyanis",
        "--format",
        "json",
        "--strict",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 2
    assert payload[0]["Level"] == 9
    assert "later_mandatory_loadout_map_missing" in payload[0]["Source Gaps"]


def test_progression_audit_best_available_uses_live_weapon_timing(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "5",
        "--character",
        "Cyanis",
        "--route",
        "best_available",
        "--format",
        "json",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload[0]["Weapon"] == "Deepforge Blade"
    assert "armor_availability_timing_missing" in payload[0]["Source Gaps"]
    assert "ORDINARY_WEAPONS.md" in payload[0]["Source Paths"]


def test_progression_audit_named_checkpoint_uses_internal_chapter13_level(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--checkpoint",
        "ch13_last_shelter",
        "--character",
        "Cyanis",
        "--route",
        "best_available",
        "--format",
        "json",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload[0]["Checkpoint"] == "Last Shelter"
    assert payload[0]["Level"] == 60
    assert payload[0]["Weapon"] == "Deepforge Blade"
    assert "armor_availability_timing_missing" in payload[0]["Source Gaps"]


def test_progression_audit_explicit_subclass_uses_selected_stat_package(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "7",
        "--character",
        "Cyanis",
        "--class-choice",
        "Cyanis=Crest Arcanist",
        "--format",
        "json",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert payload[0]["Class"] == "Crest Arcanist"
    assert payload[0]["Class Selection"] == "Explicit"
    assert "selected_class_route_missing" not in payload[0]["Source Gaps"]
    assert "CREST_ARCANIST.md" in payload[0]["Source Paths"]


def test_progression_audit_accepts_repeatable_campaign_class_choices(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--chapter",
        "7",
        "--class-choice",
        "Cyanis=Crest Arcanist",
        "--class-choice",
        "Ilyra=Vowblade",
        "--format",
        "json",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    rows = {row["Character"]: row for row in payload}
    assert rows["Cyanis"]["Class"] == "Crest Arcanist"
    assert rows["Ilyra"]["Class"] == "Vowblade"
    assert rows["Torren"]["Class Selection"] == "Base floor"


def test_progression_audit_rejects_subclass_before_volition() -> None:
    try:
        main([
            "progression-audit",
            "--chapter",
            "6",
            "--character",
            "Cyanis",
            "--class-choice",
            "Cyanis=Crest Arcanist",
        ])
    except SystemExit as exc:
        assert "before the Sixfold Volition" in str(exc)
    else:
        raise AssertionError("expected SystemExit")


def test_progression_audit_rejects_wrong_owner_class() -> None:
    try:
        main([
            "progression-audit",
            "--chapter",
            "7",
            "--character",
            "Cyanis",
            "--class-choice",
            "Cyanis=Vowblade",
        ])
    except SystemExit as exc:
        assert "not a selectable class for Cyanis" in str(exc)
    else:
        raise AssertionError("expected SystemExit")


def test_progression_audit_rejects_duplicate_class_choice() -> None:
    try:
        main([
            "progression-audit",
            "--chapter",
            "7",
            "--class-choice",
            "Cyanis=Crest Knight",
            "--class-choice",
            "Cyanis=Crest Arcanist",
        ])
    except SystemExit as exc:
        assert "duplicate --class-choice for Cyanis" in str(exc)
    else:
        raise AssertionError("expected SystemExit")


def test_progression_audit_rejects_unknown_campaign_class_choice() -> None:
    try:
        main([
            "progression-audit",
            "--chapter",
            "7",
            "--class-choice",
            "Fake=Crest Knight",
        ])
    except SystemExit as exc:
        assert "Unknown permanent character in class choices: Fake" in str(exc)
    else:
        raise AssertionError("expected SystemExit")


def test_progression_audit_rejects_unrelated_choice_with_character_filter() -> None:
    try:
        main([
            "progression-audit",
            "--chapter",
            "7",
            "--character",
            "Cyanis",
            "--class-choice",
            "Ilyra=Vowblade",
        ])
    except SystemExit as exc:
        assert "choices for other characters: Ilyra" in str(exc)
    else:
        raise AssertionError("expected SystemExit")


def test_progression_audit_rejects_chapter_and_named_checkpoint_together() -> None:
    try:
        main([
            "progression-audit",
            "--chapter",
            "13",
            "--checkpoint",
            "ch13_last_shelter",
        ])
    except SystemExit as exc:
        assert "mutually exclusive" in str(exc)
    else:
        raise AssertionError("expected SystemExit")
