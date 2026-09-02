from __future__ import annotations

import json

import pytest

from tools.diysim.cli import main


def test_cli_class_state_can_unlock_full_donor_ordinary_snapshot(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--checkpoint",
        "end_ch8",
        "--character",
        "Cyanis",
        "--route",
        "mandatory",
        "--class-choice",
        "Cyanis=Crest Arcanist",
        "--class-state",
        "Cyanis:base=5300,subclass=950",
        "--equipment-choice",
        "Cyanis:weapon=Veycross Battlestaff",
        "--equipment-choice",
        "Cyanis:armor=Arcanist Weave",
        "--equipment-choice",
        "Cyanis:secondary=Swift Focus",
        "--format",
        "json",
        "--strict",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert len(payload) == 1
    row = payload[0]
    assert row["Checkpoint"] == "End Ch8"
    assert row["Character"] == "Cyanis"
    assert row["Class"] == "Crest Arcanist"
    assert row["Weapon"] == "Veycross Battlestaff"
    assert row["Armor"] == "Arcanist Weave"
    assert row["Secondary"] == "Swift Focus"
    assert row["Authority Complete"] is True
    assert row["Source Gaps"] == ""


def test_cli_class_state_requires_exact_named_checkpoint() -> None:
    with pytest.raises(SystemExit, match="--class-state requires --checkpoint"):
        main([
            "progression-audit",
            "--chapter",
            "8",
            "--character",
            "Cyanis",
            "--class-state",
            "Cyanis:base=5300,subclass=950",
        ])


def test_cli_class_state_rejects_nonmandatory_route() -> None:
    with pytest.raises(SystemExit, match="supports --route mandatory only"):
        main([
            "progression-audit",
            "--checkpoint",
            "end_ch8",
            "--route",
            "best_available",
            "--character",
            "Cyanis",
            "--class-state",
            "Cyanis:base=5300,subclass=950",
        ])


def test_cli_class_state_rejects_impossible_checkpoint_total() -> None:
    with pytest.raises(SystemExit, match="only 1300 mandatory CEXP"):
        main([
            "progression-audit",
            "--checkpoint",
            "end_ch8",
            "--character",
            "Cyanis",
            "--class-state",
            "Cyanis:base=6000,subclass=1000",
        ])


def test_cli_class_state_is_repeatable_for_campaign_snapshot(capsys) -> None:
    exit_code = main([
        "progression-audit",
        "--checkpoint",
        "end_ch8",
        "--class-choice",
        "Cyanis=Crest Arcanist",
        "--class-choice",
        "Ilyra=Vowblade",
        "--class-state",
        "Cyanis:base=5300,subclass=950",
        "--class-state",
        "Ilyra:base=5300,subclass=950",
        "--format",
        "json",
    ])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    rows = {row["Character"]: row for row in payload}
    assert rows["Cyanis"]["Class"] == "Crest Arcanist"
    assert rows["Ilyra"]["Class"] == "Vowblade"
    assert rows["Torren"]["Class Selection"] == "Base floor"


def test_cli_character_rejects_class_state_for_other_character() -> None:
    with pytest.raises(SystemExit, match="choices for other characters: Ilyra"):
        main([
            "progression-audit",
            "--checkpoint",
            "end_ch8",
            "--character",
            "Cyanis",
            "--class-state",
            "Ilyra:base=5300,subclass=950",
        ])


def test_cli_rejects_duplicate_class_state() -> None:
    with pytest.raises(SystemExit, match="duplicate --class-state for Cyanis"):
        main([
            "progression-audit",
            "--checkpoint",
            "end_ch8",
            "--class-state",
            "Cyanis:base=5300,subclass=950",
            "--class-state",
            "Cyanis:base=5300,subclass=950",
        ])
