"""Parse common authored action fields from repository prose.

The parser defines field grammar only. It does not provide fallback combat
values: absent fields remain absent so callers can report repository gaps.
"""
from __future__ import annotations
from dataclasses import dataclass
import re

from .repo import SourceGapError


@dataclass(frozen=True)
class AuthoredActionSource:
    name: str
    raw_text: str
    target_scope: str | None
    damage_kind: str | None
    element: str | None
    power: int | None
    base_hit: int | None
    weight: int | None
    status_chances: tuple[tuple[str, int], ...]

    def missing(self, *fields: str) -> tuple[str, ...]:
        return tuple(field for field in fields if getattr(self, field) is None)


def find_named_action_line(text: str, name: str) -> str:
    """Find a bold-heading or bold-inline authored action definition line."""
    patterns = (
        rf"\*\*{re.escape(name)}\*\*\s*\n-\s*([^\n]+)",
        rf"-\s*\*\*{re.escape(name)}\*\*\s*[—-]\s*([^\n]+)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    raise SourceGapError(f"Missing exact action line for {name}")


def parse_authored_action_text(name: str, raw_text: str) -> AuthoredActionSource:
    damage = re.search(
        r"\b(Physical|Magical|Hybrid)\s*/\s*(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)\b",
        raw_text,
        re.I,
    )
    power = re.search(r"\bPower\s*\*\*(\d+)\*\*|\*\*(\d+)\s+Power(?:\s+per\s+target)?\*\*", raw_text, re.I)
    hit = re.search(r"\bBase Hit\s*\*\*(\d+)\*\*", raw_text, re.I)
    weight = re.search(r"\*\*(\d+)\s+weight\*\*", raw_text, re.I)

    target_scope = None
    lowered = raw_text.lower()
    if "all conscious" in lowered or "all enemies" in lowered or "all allies" in lowered:
        target_scope = "all"
    elif "one conscious" in lowered or "one enemy" in lowered or "one ally" in lowered:
        target_scope = "one"

    statuses: list[tuple[str, int]] = []
    for chance, status in re.findall(
        r"\*\*(\d+)%\s+(?:base\s+)?(Burn|Freeze|Stun|Staggered|Bleed)\*\*",
        raw_text,
        re.I,
    ):
        statuses.append((status.lower(), int(chance)))

    power_value = None
    if power:
        power_value = int(power.group(1) or power.group(2))

    return AuthoredActionSource(
        name=name,
        raw_text=raw_text,
        target_scope=target_scope,
        damage_kind=damage.group(1).lower() if damage else None,
        element=damage.group(2).lower() if damage else None,
        power=power_value,
        base_hit=int(hit.group(1)) if hit else None,
        weight=int(weight.group(1)) if weight else None,
        status_chances=tuple(statuses),
    )


def load_named_action_source(text: str, name: str) -> AuthoredActionSource:
    return parse_authored_action_text(name, find_named_action_line(text, name))


__all__ = [
    "AuthoredActionSource",
    "find_named_action_line",
    "load_named_action_source",
    "parse_authored_action_text",
]
