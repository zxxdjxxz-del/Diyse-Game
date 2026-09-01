from __future__ import annotations

from tools.diysim.reports.readiness import readiness_issue_breakdown
from tools.diysim.sources.readiness import OwnerFileReadiness, ReadinessIssue, SimulationReadinessReport


def test_readiness_report_aggregates_without_reclassifying() -> None:
    report = SimulationReadinessReport((
        OwnerFileReadiness(
            domain="story_bosses",
            path="boss.md",
            title="Boss",
            stat_rows=1,
            action_sections=2,
            direct_damage_sections=2,
            issues=(
                ReadinessIssue("parser_gap", "story_bosses", "boss.md", "Action A", "target_scope_unresolved", "x"),
                ReadinessIssue("parser_gap", "story_bosses", "boss.md", "Action B", "target_scope_unresolved", "y"),
                ReadinessIssue("source_gap", "story_bosses", "boss.md", "Action C", "base_hit_missing", "z"),
            ),
        ),
    ))

    parser = readiness_issue_breakdown(report, severity="parser_gap")
    source = readiness_issue_breakdown(report, severity="source_gap")

    assert parser["count"] == 2
    assert parser["by_code"] == {"target_scope_unresolved": 2}
    assert parser["by_domain"] == {"story_bosses": 2}
    assert source["count"] == 1
    assert source["by_code"] == {"base_hit_missing": 1}
