"""Reporting helpers for simulation-readiness audit results.

This module summarizes parser/source issues. It does not parse or own Diyse
canon; source adapters remain under tools.diysim.sources.
"""
from __future__ import annotations

from collections import Counter, defaultdict

from ..sources.readiness import ReadinessIssue, SimulationReadinessReport


def _selected_issues(report: SimulationReadinessReport, severity: str) -> tuple[ReadinessIssue, ...]:
    if severity == "parser_gap":
        return report.parser_gaps
    if severity == "source_gap":
        return report.source_gaps
    if severity == "all":
        return report.all_issues
    raise ValueError(f"unsupported readiness severity: {severity}")


def readiness_issue_breakdown(report: SimulationReadinessReport, *, severity: str = "parser_gap") -> dict[str, object]:
    issues = _selected_issues(report, severity)
    by_code = Counter(issue.code for issue in issues)
    by_domain = Counter(issue.domain for issue in issues)
    code_domains: dict[str, Counter[str]] = defaultdict(Counter)
    for issue in issues:
        code_domains[issue.code][issue.domain] += 1

    return {
        "severity": severity,
        "count": len(issues),
        "by_code": dict(sorted(by_code.items(), key=lambda item: (-item[1], item[0]))),
        "by_domain": dict(sorted(by_domain.items(), key=lambda item: (-item[1], item[0]))),
        "code_domains": {
            code: dict(sorted(domains.items(), key=lambda item: (-item[1], item[0])))
            for code, domains in sorted(code_domains.items(), key=lambda item: (-sum(item[1].values()), item[0]))
        },
    }


__all__ = ["readiness_issue_breakdown"]
