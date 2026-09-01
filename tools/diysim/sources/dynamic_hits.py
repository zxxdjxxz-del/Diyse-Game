"""Parse authored current-element + next-element multihit command packages."""
from __future__ import annotations

from dataclasses import dataclass
import re

from .actions import parse_authored_action_text

_STANDARD_CYCLE = ("fire", "ice", "lightning", "earth")


@dataclass(frozen=True)
class DynamicElementHitRuleSource:
    name: str
    raw_text: str
    target_scope: str | None
    damage_kind: str | None
    per_hit_powers: tuple[int, ...]
    base_hit: int | None
    element_cycle: tuple[str, ...]
    current_then_next: bool
    linked_status_chance: int | None
    max_new_harmful_statuses: int | None

    @property
    def complete(self) -> bool:
        return (
            self.target_scope in {"one", "all"}
            and self.damage_kind in {"physical", "magical", "hybrid"}
            and len(self.per_hit_powers) >= 2
            and self.base_hit is not None
            and self.element_cycle == _STANDARD_CYCLE
            and self.current_then_next
            and self.linked_status_chance is not None
            and self.max_new_harmful_statuses is not None
        )


def _clean(text: str) -> str:
    return re.sub(r"[*_`]", "", text)


def parse_dynamic_element_hit_rule_text(name: str, raw_text: str) -> DynamicElementHitRuleSource:
    cleaned = _clean(raw_text)
    ordinary = parse_authored_action_text(name, raw_text)

    damage_kind = ordinary.damage_kind
    if damage_kind is None:
        match = re.search(r"\b(?:two[- ]hit|2[- ]hit)\s+(Physical|Magical|Hybrid)\s+command\b", cleaned, re.I)
        if match:
            damage_kind = match.group(1).lower()

    numbered_hits = re.findall(
        r"\bhit\s*\d+\b[^\n]*?\b(\d+)\s+Power\b",
        cleaned,
        re.I,
    )
    per_hit_powers = tuple(int(value) for value in numbered_hits)

    base_hit_match = re.search(r"Base Hit\s*:?\s*(\d+)\s*per hit", cleaned, re.I)
    base_hit = int(base_hit_match.group(1)) if base_hit_match else ordinary.base_hit

    cycle_text = cleaned.casefold()
    has_cycle = all(element in cycle_text for element in _STANDARD_CYCLE) and "→" in cleaned
    current_then_next = bool(
        re.search(r"current(?:\s+Foundation Storm)?\s+element", cleaned, re.I)
        and re.search(r"next\s+element", cleaned, re.I)
    )

    linked = re.search(r"linked harmful status at\s*(\d+)%", cleaned, re.I)
    max_status = re.search(r"Maximum:\s*\n?>?\s*(\d+) newly inflicted harmful status", cleaned, re.I)

    return DynamicElementHitRuleSource(
        name=name,
        raw_text=raw_text,
        target_scope=ordinary.target_scope,
        damage_kind=damage_kind,
        per_hit_powers=per_hit_powers,
        base_hit=base_hit,
        element_cycle=_STANDARD_CYCLE if has_cycle else (),
        current_then_next=current_then_next,
        linked_status_chance=int(linked.group(1)) if linked else None,
        max_new_harmful_statuses=int(max_status.group(1)) if max_status else None,
    )


__all__ = ["DynamicElementHitRuleSource", "parse_dynamic_element_hit_rule_text"]
