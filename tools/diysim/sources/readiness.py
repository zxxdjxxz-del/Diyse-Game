"""Repo-wide simulation-readiness audit for enemy encounter authority.

This module never supplies gameplay fallbacks. It scans current owner files and
classifies blockers as either:
- source_gap: the owning text appears to omit information required to simulate;
- parser_gap: the text may be complete, but the generic reader cannot yet
  normalize it safely.

The audit is intentionally broader than any one encounter package.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from .actors import StatBlockSource, parse_stat_row
from .markdown import extract_markdown_tables
from .repo import RepoSourceError, SourceGapError, find_repo_root

OWNER_DOMAINS: tuple[tuple[str, str], ...] = (
    ("ordinary_enemies", "docs/09_ENEMIES_AND_ENCOUNTERS/ORDINARY_ENEMIES"),
    ("support_objects", "docs/09_ENEMIES_AND_ENCOUNTERS/SUPPORT_OBJECTS"),
    ("elites", "docs/09_ENEMIES_AND_ENCOUNTERS/ELITES"),
    ("story_bosses", "docs/09_ENEMIES_AND_ENCOUNTERS/STORY_BOSSES"),
    ("regional_hunts", "docs/09_ENEMIES_AND_ENCOUNTERS/REGIONAL_HUNTS"),
    ("major_hunts", "docs/09_ENEMIES_AND_ENCOUNTERS/MAJOR_HUNTS"),
)

_DAMAGE_RE = re.compile(
    r"\b(Physical|Magical|Hybrid)\s*/\s*(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)\b",
    re.I,
)
_POWER_RE = re.compile(r"(?:\*\*)?(\d+)\s+Power(?:\s+per\s+target)?(?:\*\*)?|Power\s*:?\s*(?:\*\*)?(\d+)(?:\*\*)?", re.I)
_BASE_HIT_RE = re.compile(r"Base Hit\s*(?:\*\*)?(\d+)(?:\*\*)?", re.I)
_NO_DAMAGE_RE = re.compile(r"Power\s*:\s*N/A\s*[—-]\s*no direct damage|Power\s+N/A", re.I)
_TARGET_ONE_RE = re.compile(r"\b(one|single)[ -](?:conscious )?(?:party member|enemy|ally|target)|\bone (?:party member|enemy|ally)\b|sealed character only", re.I)
_TARGET_ALL_RE = re.compile(r"\ball (?:conscious )?(?:party members|enemies|allies|targets)\b|per target", re.I)

_STRUCTURAL_HEADINGS = {
    "architecture", "current notes", "numerical boundary", "duration certification",
    "power-completeness verdict", "current raw line", "actual route-level reference",
    "recorded action system", "earlier ring handling → opening protection",
    "ordinary chapter-5 body", "furnace tyrant encounter instance",
}


@dataclass(frozen=True)
class ReadinessIssue:
    severity: str  # source_gap | parser_gap
    domain: str
    path: str
    subject: str
    code: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "domain": self.domain,
            "path": self.path,
            "subject": self.subject,
            "code": self.code,
            "message": self.message,
        }


@dataclass(frozen=True)
class OwnerFileReadiness:
    domain: str
    path: str
    title: str
    stat_rows: int
    action_sections: int
    direct_damage_sections: int
    issues: tuple[ReadinessIssue, ...]

    @property
    def source_gap_count(self) -> int:
        return sum(issue.severity == "source_gap" for issue in self.issues)

    @property
    def parser_gap_count(self) -> int:
        return sum(issue.severity == "parser_gap" for issue in self.issues)

    @property
    def ready(self) -> bool:
        return not self.issues

    def as_dict(self) -> dict[str, object]:
        return {
            "domain": self.domain,
            "path": self.path,
            "title": self.title,
            "stat_rows": self.stat_rows,
            "action_sections": self.action_sections,
            "direct_damage_sections": self.direct_damage_sections,
            "ready": self.ready,
            "source_gap_count": self.source_gap_count,
            "parser_gap_count": self.parser_gap_count,
            "issues": [issue.as_dict() for issue in self.issues],
        }


@dataclass(frozen=True)
class SimulationReadinessReport:
    files: tuple[OwnerFileReadiness, ...]

    @property
    def files_scanned(self) -> int:
        return len(self.files)

    @property
    def source_gaps(self) -> tuple[ReadinessIssue, ...]:
        return tuple(issue for file in self.files for issue in file.issues if issue.severity == "source_gap")

    @property
    def parser_gaps(self) -> tuple[ReadinessIssue, ...]:
        return tuple(issue for file in self.files for issue in file.issues if issue.severity == "parser_gap")

    @property
    def direct_damage_sections(self) -> int:
        return sum(file.direct_damage_sections for file in self.files)

    @property
    def ready_files(self) -> int:
        return sum(file.ready for file in self.files)

    @property
    def by_domain(self) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = {}
        for domain, _ in OWNER_DOMAINS:
            members = [file for file in self.files if file.domain == domain]
            result[domain] = {
                "files": len(members),
                "ready_files": sum(file.ready for file in members),
                "source_gaps": sum(file.source_gap_count for file in members),
                "parser_gaps": sum(file.parser_gap_count for file in members),
                "direct_damage_sections": sum(file.direct_damage_sections for file in members),
            }
        return result

    def as_dict(self, *, include_files: bool = True) -> dict[str, object]:
        payload: dict[str, object] = {
            "files_scanned": self.files_scanned,
            "ready_files": self.ready_files,
            "direct_damage_sections": self.direct_damage_sections,
            "source_gap_count": len(self.source_gaps),
            "parser_gap_count": len(self.parser_gaps),
            "by_domain": self.by_domain,
        }
        if include_files:
            payload["files"] = [file.as_dict() for file in self.files]
        return payload


def _title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    return match.group(1).strip() if match else fallback


def _heading_blocks(text: str) -> tuple[tuple[str, str], ...]:
    matches = list(re.finditer(r"^(#{2,4})\s+(.+?)\s*$", text, re.M))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(2).strip(), text[match.end():end].strip()))
    return tuple(blocks)


def _stat_rows(text: str) -> tuple[StatBlockSource, ...]:
    rows: list[StatBlockSource] = []
    for table in extract_markdown_tables(text):
        if not table or "HP" not in table[0]:
            continue
        for row in table:
            try:
                rows.append(parse_stat_row(row))
            except SourceGapError:
                continue
    return tuple(rows)


def _target_scope(block: str) -> str | None:
    if _TARGET_ALL_RE.search(block):
        return "all"
    if _TARGET_ONE_RE.search(block):
        return "one"
    return None


def _action_candidate(heading: str, block: str) -> bool:
    if heading.casefold() in _STRUCTURAL_HEADINGS:
        return False
    return bool(_DAMAGE_RE.search(block) or _POWER_RE.search(block) or _NO_DAMAGE_RE.search(block) or _BASE_HIT_RE.search(block))


def _direct_damage_block(block: str) -> bool:
    return not _NO_DAMAGE_RE.search(block) and bool(_DAMAGE_RE.search(block) or _POWER_RE.search(block))


def _audit_action(domain: str, path: str, heading: str, block: str) -> tuple[ReadinessIssue, ...]:
    if not _direct_damage_block(block):
        return ()

    issues: list[ReadinessIssue] = []
    damage = _DAMAGE_RE.search(block)
    power = _POWER_RE.search(block)
    hit = _BASE_HIT_RE.search(block)

    if damage is not None and power is None:
        issues.append(ReadinessIssue(
            "source_gap", domain, path, heading, "damage_power_missing",
            "Direct-damage section identifies a damage axis/element but has no exact numeric Power.",
        ))
    elif power is not None and damage is None:
        issues.append(ReadinessIssue(
            "parser_gap", domain, path, heading, "damage_identity_unresolved",
            "Numeric direct-damage Power is present, but the generic reader cannot resolve damage kind/element from this section alone.",
        ))

    if hit is None:
        issues.append(ReadinessIssue(
            "source_gap", domain, path, heading, "base_hit_missing",
            "Enemy/support direct-damage section has no explicit Base Hit in its owning action block.",
        ))

    if _target_scope(block) is None:
        issues.append(ReadinessIssue(
            "parser_gap", domain, path, heading, "target_scope_unresolved",
            "The generic reader cannot resolve one/all target scope from this action section.",
        ))

    return tuple(issues)


def _audit_stats(domain: str, path: str, title: str, rows: tuple[StatBlockSource, ...], direct_blocks: tuple[str, ...]) -> tuple[ReadinessIssue, ...]:
    if not direct_blocks:
        return ()
    if not rows:
        return (ReadinessIssue(
            "parser_gap", domain, path, title, "stat_block_unresolved",
            "This owner contains direct damage but the generic reader found no HP stat table in the same file; stats may be owned by another referenced file.",
        ),)

    required = {"hp", "defense", "spirit", "speed", "evasion"}
    if any(re.search(r"\bPhysical\s*/", block, re.I) for block in direct_blocks):
        required.add("attack")
    if any(re.search(r"\bMagical\s*/", block, re.I) for block in direct_blocks):
        required.add("magic")
    if any(re.search(r"\bHybrid\s*/", block, re.I) for block in direct_blocks):
        required.update(("attack", "magic"))

    issues: list[ReadinessIssue] = []
    for index, row in enumerate(rows, start=1):
        missing = sorted(field for field in required if not row.has(field))
        if missing:
            issues.append(ReadinessIssue(
                "source_gap", domain, path, f"{title} stat row {index}", "required_stats_missing",
                f"Stat row is missing fields needed by its parsed combat role: {', '.join(missing)}.",
            ))
    return tuple(issues)


def audit_owner_file(path: Path, *, domain: str, repo_root: Path) -> OwnerFileReadiness:
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(repo_root).as_posix()
    title = _title(text, path.stem)
    rows = _stat_rows(text)

    actions: list[tuple[str, str]] = []
    direct: list[tuple[str, str]] = []
    issues: list[ReadinessIssue] = []
    for heading, block in _heading_blocks(text):
        if not _action_candidate(heading, block):
            continue
        actions.append((heading, block))
        if _direct_damage_block(block):
            direct.append((heading, block))
        issues.extend(_audit_action(domain, relative, heading, block))

    issues.extend(_audit_stats(domain, relative, title, rows, tuple(block for _, block in direct)))
    return OwnerFileReadiness(
        domain=domain,
        path=relative,
        title=title,
        stat_rows=len(rows),
        action_sections=len(actions),
        direct_damage_sections=len(direct),
        issues=tuple(issues),
    )


def _should_scan(path: Path) -> bool:
    upper = path.stem.upper()
    if path.name.startswith(".") or path.name.upper() == "README.MD":
        return False
    # Aggregate registers are indexes, not one combat identity. Individual
    # owner files are audited separately and remain the simulation source.
    if "REGISTER" in upper or upper.endswith("_INDEX"):
        return False
    return True


def audit_simulation_readiness(*, root: Path | None = None) -> SimulationReadinessReport:
    repo = (root or find_repo_root()).resolve()
    files: list[OwnerFileReadiness] = []
    for domain, relative_dir in OWNER_DOMAINS:
        directory = repo / relative_dir
        if not directory.exists():
            files.append(OwnerFileReadiness(
                domain=domain,
                path=relative_dir,
                title=relative_dir,
                stat_rows=0,
                action_sections=0,
                direct_damage_sections=0,
                issues=(ReadinessIssue(
                    "source_gap", domain, relative_dir, relative_dir, "owner_directory_missing",
                    "Expected encounter owner directory does not exist.",
                ),),
            ))
            continue
        for path in sorted(directory.rglob("*.md")):
            if _should_scan(path):
                files.append(audit_owner_file(path, domain=domain, repo_root=repo))
    return SimulationReadinessReport(tuple(files))


__all__ = [
    "OWNER_DOMAINS",
    "OwnerFileReadiness",
    "ReadinessIssue",
    "SimulationReadinessReport",
    "audit_owner_file",
    "audit_simulation_readiness",
]
