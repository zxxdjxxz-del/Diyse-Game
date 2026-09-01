"""Associate authored stat rows with their owning section and explicit runtime role.

This source layer does not infer gameplay values from missing columns. It uses
explicit repository prose to distinguish acting combatants from passive
finite/targetable support objects when the owner states that distinction.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal
import re

from .actors import StatBlockSource, parse_stat_row
from .repo import SourceGapError

EntityRole = Literal["acting_combatant", "passive_target", "unresolved"]

_PASSIVE_PATTERNS = (
    r"take(?:s)? no independent ordinary turns?",
    r"no independent ordinary turns?",
    r"no independent turns?",
    r"does not take an independent turn",
    r"do not take an independent turn",
    r"no direct-damage action",
    r"deal(?:s)? no direct damage",
)

_ACTING_PATTERNS = (
    r"takes? (?:its|an) (?:own |independent )?(?:ordinary |normal )?turn",
    r"acts? on (?:its|an) (?:own |independent )?(?:ordinary |normal )?turn",
    r"speed-ordered turn",
)


@dataclass(frozen=True)
class EntityStatSource:
    stats: StatBlockSource
    section_heading: str
    row_label: str | None
    role: EntityRole
    role_evidence: str | None

    @property
    def is_passive(self) -> bool:
        return self.role == "passive_target"


def _cells(line: str) -> list[str]:
    return [cell.strip().strip("*") for cell in line.strip().strip("|").split("|")]


def _is_separator(line: str) -> bool:
    cells = _cells(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def _headings(lines: list[str]) -> list[tuple[int, int, str]]:
    result: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            result.append((index, len(match.group(1)), match.group(2).strip()))
    return result


def _section_for_line(lines: list[str], headings: list[tuple[int, int, str]], line_index: int) -> tuple[str, str]:
    prior = [heading for heading in headings if heading[0] < line_index]
    if not prior:
        return "<document>", "\n".join(lines)
    start_index, level, heading_text = prior[-1]
    end_index = len(lines)
    for candidate_index, candidate_level, _ in headings:
        if candidate_index > start_index and candidate_level <= level:
            end_index = candidate_index
            break
    return heading_text, "\n".join(lines[start_index:end_index])


def _classify_role(section_text: str) -> tuple[EntityRole, str | None]:
    for pattern in _PASSIVE_PATTERNS:
        match = re.search(pattern, section_text, re.I)
        if match:
            return "passive_target", match.group(0)
    for pattern in _ACTING_PATTERNS:
        match = re.search(pattern, section_text, re.I)
        if match:
            return "acting_combatant", match.group(0)
    return "unresolved", None


def _row_label(row: dict[str, str]) -> str | None:
    stat_headers = {"Lv", "Level", "HP", "MP", "ATK", "MAG", "DEF", "Spirit", "SPR", "SPD", "EVA", "SR", "Power", "Direct-damage Power"}
    for header, value in row.items():
        if header not in stat_headers and value.strip():
            return value.strip().strip("*")
    return None


def parse_entity_stat_sources(text: str) -> tuple[EntityStatSource, ...]:
    lines = text.splitlines()
    headings = _headings(lines)
    results: list[EntityStatSource] = []
    index = 0
    while index + 1 < len(lines):
        if "|" not in lines[index] or not _is_separator(lines[index + 1]):
            index += 1
            continue

        headers = _cells(lines[index])
        if "HP" not in headers:
            index += 2
            continue

        section_heading, section_text = _section_for_line(lines, headings, index)
        role, evidence = _classify_role(section_text)
        row_index = index + 2
        while row_index < len(lines) and "|" in lines[row_index] and lines[row_index].strip().startswith("|"):
            values = _cells(lines[row_index])
            if len(values) != len(headers):
                break
            row = dict(zip(headers, values))
            try:
                stat_block = parse_stat_row(row)
            except SourceGapError:
                row_index += 1
                continue
            results.append(EntityStatSource(
                stats=stat_block,
                section_heading=section_heading,
                row_label=_row_label(row),
                role=role,
                role_evidence=evidence,
            ))
            row_index += 1
        index = max(row_index, index + 2)
    return tuple(results)


__all__ = ["EntityRole", "EntityStatSource", "parse_entity_stat_sources"]
