from __future__ import annotations

from tools.diysim.encounters.formation_catalog import (
    build_formation_catalog,
    discover_formation_paths,
)
from tools.diysim.reports.formation_runtime_coverage import formation_runtime_coverage_dict


def test_all_authored_numbered_chapter_formation_sources_are_discovered():
    paths = discover_formation_paths()
    assert len(paths) == 13
    assert not any(path.endswith("CHAPTER_00_FORMATIONS.md") for path in paths)
    for chapter in range(1, 14):
        expected = f"CHAPTER_{chapter:02d}_FORMATIONS.md"
        assert any(path.endswith(expected) for path in paths)


def test_every_formation_is_explicitly_ready_or_blocked():
    formations = build_formation_catalog()
    assert formations
    for formation in formations:
        if formation.runtime_ready:
            assert not formation.blockers
            assert all(member.enemy is not None for member in formation.members)
            assert all(member.enemy.kind in {"generic", "formation"} for member in formation.members if member.enemy)
        else:
            assert formation.blockers


def test_formation_coverage_report_totals_reconcile():
    report = formation_runtime_coverage_dict(include_formations=False)
    assert report["total_formations"] > 0
    assert report["runtime_ready"] + report["blocked"] == report["total_formations"]
    assert 0.0 <= report["coverage_rate"] <= 1.0
    assert report["formation_source_chapters"] == [str(chapter) for chapter in range(1, 14)]
    assert report["chapters_without_formation_source"] == ["0"]
    by_chapter = report["by_chapter"]
    assert set(by_chapter) == {str(chapter) for chapter in range(14)}
    assert by_chapter["0"] == {"total": 0, "runtime_ready": 0, "blocked": 0}
    assert sum(item["total"] for item in by_chapter.values()) == report["total_formations"]
    assert sum(item["runtime_ready"] for item in by_chapter.values()) == report["runtime_ready"]
    assert sum(item["blocked"] for item in by_chapter.values()) == report["blocked"]


def test_command_screen_is_runtime_ready_in_repo_wide_catalog():
    command_screen = next(
        formation for formation in build_formation_catalog()
        if formation.name == "Command Screen" and formation.source_path.endswith("CHAPTER_03_FORMATIONS.md")
    )
    assert command_screen.runtime_ready
