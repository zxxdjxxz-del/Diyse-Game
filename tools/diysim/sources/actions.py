"""Parse common authored action fields from repository prose.

The parser defines field grammar only. It does not provide fallback combat
values: absent fields remain absent so callers can report repository gaps.
Dynamic element descriptors remain dynamic until encounter state resolves them.
"""
from __future__ import annotations
from dataclasses import dataclass
import re

from .repo import SourceGapError

_FIXED_ELEMENTS = {"neutral", "colorless", "fire", "ice", "lightning", "earth", "ruin"}


@dataclass(frozen=True)
class AuthoredActionSource:
    name: str
    raw_text: str
    target_scope: str | None
    damage_kind: str | None
    element: str | None
    element_mode: str | None
    element_source: str | None
    power: int | None
    base_hit: int | None
    weight: int | None
    physical_weight: float | None
    magical_weight: float | None
    status_chances: tuple[tuple[str, int], ...]

    @property
    def has_resolved_damage_axis(self) -> bool:
        return self.damage_kind is not None

    @property
    def has_element_identity(self) -> bool:
        return self.element is not None or self.element_mode == "dynamic"

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


def _normalize_dynamic_element_source(token: str) -> str | None:
    normalized = re.sub(r"\s+", " ", token.strip().lower())
    aliases = {
        "current expression": "current_expression",
        "current element": "current_element",
        "current gallery element": "current_gallery_element",
        "assigned element": "assigned_element",
        "current forecast element": "current_forecast_element",
        "forecast element": "forecast_element",
        "selected element": "selected_element",
        "chosen element": "chosen_element",
    }
    if normalized in aliases:
        return aliases[normalized]
    if "element" in normalized or "expression" in normalized or "forecast" in normalized:
        return normalized.replace(" ", "_")
    return None


def _parse_damage_identity(raw_text: str) -> tuple[str | None, str | None, str | None, str | None, float | None, float | None]:
    match = re.search(r"\b(Physical|Magical|Hybrid)\s*/\s*([^;\n]+)", raw_text, re.I)
    if not match:
        return None, None, None, None, None, None

    damage_kind = match.group(1).lower()
    remainder = match.group(2).strip()
    element_token = re.split(r"\s+/\s+", remainder, maxsplit=1)[0].strip().strip("*.,")

    fixed = re.fullmatch(
        r"(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)(?:(\d{1,3})/(\d{1,3}))?",
        element_token,
        re.I,
    )
    if fixed:
        element = fixed.group(1).lower()
        physical_weight = None
        magical_weight = None
        if fixed.group(2) is not None and fixed.group(3) is not None:
            physical_weight = int(fixed.group(2)) / 100.0
            magical_weight = int(fixed.group(3)) / 100.0
        return damage_kind, element, "fixed", None, physical_weight, magical_weight

    dynamic_source = _normalize_dynamic_element_source(element_token)
    if dynamic_source is not None:
        return damage_kind, None, "dynamic", dynamic_source, None, None

    # The damage axis is still authored even when the post-slash identity uses a
    # syntax the parser does not understand yet. Do not guess the element.
    return damage_kind, None, None, None, None, None


def _parse_target_scope(raw_text: str) -> str | None:
    lowered = re.sub(r"\s+", " ", raw_text.lower())
    all_patterns = (
        "all conscious party members",
        "all party members",
        "all conscious targets",
        "all targets",
        "all enemies",
        "all allies",
    )
    if any(pattern in lowered for pattern in all_patterns) or "per target" in lowered:
        return "all"

    one_patterns = (
        "one conscious target",
        "one conscious party member",
        "one party member",
        "one target",
        "one enemy",
        "one ally",
        "single target",
        "single party member",
        "fixed visible target",
        "fixed target",
        "sealed character only",
    )
    if any(pattern in lowered for pattern in one_patterns):
        return "one"
    return None


def parse_authored_action_text(name: str, raw_text: str) -> AuthoredActionSource:
    damage_kind, element, element_mode, element_source, physical_weight, magical_weight = _parse_damage_identity(raw_text)

    power = re.search(
        r"\bPower\s*:?\s*(?:\*\*)?(\d+)(?:\*\*)?|(?:\*\*)?(\d+)\s+Power(?:\s+per\s+target)?(?:\*\*)?",
        raw_text,
        re.I,
    )
    hit = re.search(r"\bBase Hit\s*:?\s*(?:\*\*)?(\d+)(?:\*\*)?", raw_text, re.I)
    weight = re.search(r"(?:\*\*)?(\d+)\s+weight(?:\*\*)?", raw_text, re.I)

    statuses: list[tuple[str, int]] = []
    for chance, status in re.findall(
        r"(?:\*\*)?(\d+)%\s+(?:base\s+)?(Burn|Freeze|Stun|Staggered|Bleed)(?:\*\*)?",
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
        target_scope=_parse_target_scope(raw_text),
        damage_kind=damage_kind,
        element=element if element in _FIXED_ELEMENTS else None,
        element_mode=element_mode,
        element_source=element_source,
        power=power_value,
        base_hit=int(hit.group(1)) if hit else None,
        weight=int(weight.group(1)) if weight else None,
        physical_weight=physical_weight,
        magical_weight=magical_weight,
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
