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
_NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}


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
    power_mode: str | None
    base_hit: int | None
    weight: int | None
    physical_weight: float | None
    magical_weight: float | None
    hit_count_min: int | None
    hit_count_max: int | None
    status_chances: tuple[tuple[str, int], ...]

    @property
    def has_resolved_damage_axis(self) -> bool:
        return self.damage_kind is not None

    @property
    def has_element_identity(self) -> bool:
        return self.element is not None or self.element_mode == "dynamic"

    @property
    def is_multihit(self) -> bool:
        return (self.hit_count_max or 1) > 1

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
    normalized = normalized.replace("'s", "")
    aliases = {
        "current expression": "current_expression",
        "current element": "current_element",
        "current standard element": "current_standard_element",
        "current gallery element": "current_gallery_element",
        "current visible standard element": "current_visible_standard_element",
        "assigned element": "assigned_element",
        "current forecast element": "current_forecast_element",
        "forecast element": "forecast_element",
        "selected element": "selected_element",
        "chosen element": "chosen_element",
        "currently active chamber element": "current_active_chamber_element",
        "current active chamber element": "current_active_chamber_element",
        "that chamber element": "active_chamber_element",
        "current inherited element": "current_inherited_element",
    }
    if normalized in aliases:
        return aliases[normalized]
    if "element" in normalized or "expression" in normalized or "forecast" in normalized:
        return re.sub(r"[^a-z0-9]+", "_", normalized).strip("_")
    return None


def _parse_explicit_weights(raw_text: str) -> tuple[float | None, float | None]:
    match = re.search(
        r"(\d{1,3})%\s*(?:ATK|Attack)\s*/\s*(\d{1,3})%\s*(?:MAG|Magic)",
        raw_text,
        re.I,
    )
    if not match:
        return None, None
    return int(match.group(1)) / 100.0, int(match.group(2)) / 100.0


def _parse_dynamic_element_from_prose(raw_text: str) -> str | None:
    patterns = (
        r"uses?\s+(?:the\s+)?([^\n;.]*?(?:element|expression|forecast))\b",
        r"each hit uses\s+([^\n;.]*?element)\b",
    )
    for pattern in patterns:
        match = re.search(pattern, raw_text, re.I)
        if match:
            source = _normalize_dynamic_element_source(match.group(1))
            if source is not None:
                return source

    # Some current owner sheets put the dynamic identity on its own authored
    # line immediately after the damage school, e.g. "Magical" followed by
    # "current inherited element". This is a declaration, not a fallback.
    for line in raw_text.splitlines():
        token = line.strip().lstrip("- ").strip().strip("*.,:;— ")
        source = _normalize_dynamic_element_source(token)
        if source is not None and re.fullmatch(
            r"(?:current|assigned|selected|chosen|that|currently active|current active)[^\n]*(?:element|expression|forecast)",
            token,
            re.I,
        ):
            return source
    return None


def _parse_damage_identity(raw_text: str) -> tuple[str | None, str | None, str | None, str | None, float | None, float | None]:
    physical_weight, magical_weight = _parse_explicit_weights(raw_text)

    match = re.search(r"\b(Physical|Magical|Hybrid)\s*/\s*([^;\n]+)", raw_text, re.I)
    damage_kind: str | None = None
    if match:
        damage_kind = match.group(1).lower()
        remainder = match.group(2).strip()

        compact_weighted = re.match(
            r"^(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)(\d{1,3})/(\d{1,3})\b",
            remainder,
            re.I,
        )
        if compact_weighted:
            return (
                damage_kind,
                compact_weighted.group(1).lower(),
                "fixed",
                None,
                int(compact_weighted.group(2)) / 100.0,
                int(compact_weighted.group(3)) / 100.0,
            )

        parts = [part.strip() for part in re.split(r"\s*/\s*", remainder) if part.strip()]
        element_token = parts[0].strip().strip("*.,:;—- ") if parts else ""

        fixed = re.fullmatch(
            r"(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)",
            element_token,
            re.I,
        )
        if fixed:
            return damage_kind, fixed.group(1).lower(), "fixed", None, physical_weight, magical_weight

        dynamic_source = _normalize_dynamic_element_source(element_token)
        if dynamic_source is not None:
            return damage_kind, None, "dynamic", dynamic_source, physical_weight, magical_weight

    if damage_kind is None:
        standalone = re.search(r"^\s*-?\s*(Physical|Magical|Hybrid)\s*$", raw_text, re.I | re.M)
        if standalone:
            damage_kind = standalone.group(1).lower()
        else:
            hits = re.search(r"\b(?:up to\s+)?(?:\d+|one|two|three|four|five|six)\s+(Physical|Magical|Hybrid)\s+hits?\b", raw_text, re.I)
            if hits:
                damage_kind = hits.group(1).lower()

    dynamic_source = _parse_dynamic_element_from_prose(raw_text)
    if damage_kind is not None and dynamic_source is not None:
        return damage_kind, None, "dynamic", dynamic_source, physical_weight, magical_weight

    return damage_kind, None, None, None, physical_weight, magical_weight


def _explicit_target_scope(raw_text: str) -> str | None:
    """Read the action's direct target declaration before explanatory prose."""
    patterns = (
        ("all", r"^\s*-?\s*(?:target\s*:\s*)?all (?:conscious )?(?:active )?party members\b"),
        ("one", r"^\s*-?\s*target\s*:\s*one (?:established |conscious |active )*party member\b"),
        ("one", r"^\s*-?\s*one (?:established |conscious |active )*party member\b"),
        ("one", r"^\s*-?\s*(?:fixed |visibly fixed )?(?:marked )?target\s*:\s*one\b"),
    )
    matches: list[str] = []
    for scope, pattern in patterns:
        if re.search(pattern, raw_text, re.I | re.M):
            matches.append(scope)
    unique = set(matches)
    return next(iter(unique)) if len(unique) == 1 else None


def _parse_target_scope(raw_text: str) -> str | None:
    explicit = _explicit_target_scope(raw_text)
    if explicit is not None:
        return explicit

    lowered = re.sub(r"\s+", " ", raw_text.lower())
    all_patterns = (
        "all conscious party members",
        "all party members",
        "all conscious targets",
        "all targets",
        "all enemies",
        "all allies",
        "aoe record",
    )
    one_patterns = (
        "one conscious target",
        "one conscious party member",
        "one party member",
        "one target",
        "one enemy",
        "one ally",
        "single target",
        "single-target",
        "single party member",
        "fixed visible target",
        "fixed target",
        "sealed character only",
        "single-target record",
    )
    has_all = any(pattern in lowered for pattern in all_patterns) or "per target" in lowered
    has_one = any(pattern in lowered for pattern in one_patterns)
    if has_all and not has_one:
        return "all"
    if has_one and not has_all:
        return "one"
    return None


def _parse_hit_count(raw_text: str) -> tuple[int | None, int | None]:
    exact = re.search(r"\b(\d+)\s*[×x]\s*\d+\s+Power", raw_text, re.I)
    if exact:
        count = int(exact.group(1))
        return count, count

    up_to = re.search(r"\bup to\s+(\d+|one|two|three|four|five|six)\s+(?:Physical|Magical|Hybrid)?\s*hits?\b", raw_text, re.I)
    if up_to:
        token = up_to.group(1).lower()
        maximum = int(token) if token.isdigit() else _NUMBER_WORDS[token]
        return 1, maximum

    exact_words = re.search(r"\b(\d+|one|two|three|four|five|six)\s+(?:Physical|Magical|Hybrid)\s+hits?\b", raw_text, re.I)
    if exact_words:
        token = exact_words.group(1).lower()
        count = int(token) if token.isdigit() else _NUMBER_WORDS[token]
        return count, count
    return None, None


def parse_authored_action_text(name: str, raw_text: str) -> AuthoredActionSource:
    damage_kind, element, element_mode, element_source, physical_weight, magical_weight = _parse_damage_identity(raw_text)

    power = re.search(
        r"\bPower\s*:?\s*(?:\*\*)?(\d+)(?:\*\*)?|(?:\*\*)?(\d+)\s+Power(?:\s+per\s+(target|hit))?(?:\*\*)?",
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
    power_mode = None
    if power:
        power_value = int(power.group(1) or power.group(2))
        suffix = power.group(3)
        power_mode = f"per_{suffix.lower()}" if suffix else "action"

    hit_min, hit_max = _parse_hit_count(raw_text)

    return AuthoredActionSource(
        name=name,
        raw_text=raw_text,
        target_scope=_parse_target_scope(raw_text),
        damage_kind=damage_kind,
        element=element if element in _FIXED_ELEMENTS else None,
        element_mode=element_mode,
        element_source=element_source,
        power=power_value,
        power_mode=power_mode,
        base_hit=int(hit.group(1)) if hit else None,
        weight=int(weight.group(1)) if weight else None,
        physical_weight=physical_weight,
        magical_weight=magical_weight,
        hit_count_min=hit_min,
        hit_count_max=hit_max,
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
