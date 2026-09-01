from __future__ import annotations

from pathlib import Path

from tools.diysim.sources.readiness import audit_owner_file, audit_simulation_readiness


def test_owner_audit_separates_source_gaps_from_parser_gaps(tmp_path: Path) -> None:
    owner = tmp_path / "enemy.md"
    owner.write_text(
        "# Synthetic Enemy\n\n"
        "| HP | ATK | DEF | Spirit | SPD | EVA | SR |\n"
        "|---:|---:|---:|---:|---:|---:|---:|\n"
        "| 100 | 20 | 10 | 10 | 12 | 0 | 0 |\n\n"
        "## Complete Strike\n"
        "- one party member\n- Physical / Neutral\n- **120 Power**\n- Base Hit **100**\n\n"
        "## Missing Power\n"
        "- one party member\n- Physical / Neutral\n- Base Hit **100**\n\n"
        "## Prose Analogue\n"
        "- one party member\n- **90 Power**\n- Base Hit **100**\n",
        encoding="utf-8",
    )

    result = audit_owner_file(owner, domain="synthetic", repo_root=tmp_path)
    codes = {(issue.severity, issue.code) for issue in result.issues}

    assert result.direct_damage_sections == 3
    assert ("source_gap", "damage_power_missing") in codes
    assert ("parser_gap", "damage_identity_unresolved") in codes


def test_current_repo_readiness_scans_all_combat_owner_families() -> None:
    report = audit_simulation_readiness()

    assert report.files_scanned > 0
    assert report.direct_damage_sections > 0
    for domain in (
        "ordinary_enemies",
        "support_objects",
        "elites",
        "story_bosses",
        "regional_hunts",
        "major_hunts",
    ):
        assert domain in report.by_domain
        assert report.by_domain[domain]["files"] > 0


def test_current_repo_has_no_simulation_readiness_gaps() -> None:
    report = audit_simulation_readiness()

    assert report.source_gaps == ()
    assert report.parser_gaps == ()
    assert report.ready_files == report.files_scanned


def test_supported_bounded_replays_do_not_require_a_fixed_target_scope() -> None:
    report = audit_simulation_readiness()
    replay_subjects = {
        "Recorded Echo",
        "Replayed Role",
        "Devoured Replay",
        "Calamity Replay",
        "Deep Duplicate",
    }

    inherited_target_gaps = [
        issue
        for issue in report.parser_gaps
        if issue.subject in replay_subjects and issue.code == "target_scope_unresolved"
    ]
    assert inherited_target_gaps == []


def test_complete_functional_analogue_system_resolves_warden_variant_headings() -> None:
    report = audit_simulation_readiness()
    analogue_subjects = {
        "Recorded Physical Analogue",
        "Recorded Magical Analogue",
        "Recorded Hybrid Analogue",
        "Recorded Analogue",
    }

    analogue_gaps = [
        issue
        for issue in report.parser_gaps
        if issue.subject in analogue_subjects
        and issue.path.endswith("FIRST_COMMAND_WARDEN.md")
    ]
    assert analogue_gaps == []


def test_complete_dynamic_multihit_packages_resolve_major_hunt_action_headings() -> None:
    report = audit_simulation_readiness()
    dynamic_subjects = {"Confluence Spear", "Confluence Rupture"}

    dynamic_gaps = [
        issue
        for issue in report.parser_gaps
        if issue.subject in dynamic_subjects
        and issue.domain == "major_hunts"
    ]
    assert dynamic_gaps == []
