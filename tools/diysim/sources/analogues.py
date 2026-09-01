"""Parse consume-on-use functional analogue rules from encounter owner prose."""
from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class FunctionalAnalogueRuleSource:
    raw_text: str
    single_power: int | None
    aoe_power: int | None
    base_hit: int | None
    physical_element: str | None
    magical_element: str | None
    hybrid_element: str | None
    hybrid_physical_weight: float | None
    hybrid_magical_weight: float | None
    record_after_completion: bool
    eligible_attack: bool
    eligible_ability: bool
    standard_card_ineligible: bool
    max_records: int | None
    collapse_multihit: bool
    clear_after_use: bool
    strips_secondary_mechanics: bool

    @property
    def complete(self) -> bool:
        return (
            self.single_power is not None
            and self.aoe_power is not None
            and self.base_hit is not None
            and self.physical_element is not None
            and self.magical_element is not None
            and self.hybrid_element is not None
            and self.hybrid_physical_weight is not None
            and self.hybrid_magical_weight is not None
            and self.record_after_completion
            and self.eligible_attack
            and self.eligible_ability
            and self.standard_card_ineligible
            and self.max_records == 1
            and self.collapse_multihit
            and self.clear_after_use
            and self.strips_secondary_mechanics
        )


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", text.casefold()))


def _variant(text: str, school: str) -> tuple[int | None, int | None, str | None, int | None]:
    block_match = re.search(
        rf"###\s+Recorded\s+{school}\s+Analogue(.*?)(?=\n###|\n##|\Z)",
        text,
        re.I | re.S,
    )
    if not block_match:
        return None, None, None, None
    block = block_match.group(1)
    single = re.search(
        rf"single-target record\s*[—-]\s*(?:{school}\s*/\s*)?(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)?\s*[—-]\s*\*\*(\d+) Power\*\*",
        block,
        re.I,
    )
    aoe = re.search(
        rf"AoE record\s*[—-]\s*(?:{school}\s*/\s*)?(Neutral|Colorless|Fire|Ice|Lightning|Earth|Ruin)?\s*[—-]\s*\*\*(\d+) Power per target\*\*",
        block,
        re.I,
    )
    hit = re.search(r"Base Hit\s*\*\*(\d+)\*\*", block, re.I)

    element = None
    if single and single.group(1):
        element = single.group(1).lower()
    elif aoe and aoe.group(1):
        element = aoe.group(1).lower()

    return (
        int(single.group(2)) if single else None,
        int(aoe.group(2)) if aoe else None,
        element,
        int(hit.group(1)) if hit else None,
    )


def _agreed_value(values: tuple[int | None, ...]) -> int | None:
    if any(value is None for value in values):
        return None
    concrete = {int(value) for value in values if value is not None}
    return next(iter(concrete)) if len(concrete) == 1 else None


def parse_functional_analogue_rule_text(raw_text: str) -> FunctionalAnalogueRuleSource:
    physical_single, physical_aoe, physical_element, physical_hit = _variant(raw_text, "Physical")
    magical_single, magical_aoe, magical_element, magical_hit = _variant(raw_text, "Magical")
    hybrid_single, hybrid_aoe, hybrid_element, hybrid_hit = _variant(raw_text, "Hybrid")

    weights = re.search(
        r"Recorded Hybrid Analogue[\s\S]*?(\d+)%\s*ATK\s*/\s*(\d+)%\s*MAG",
        raw_text,
        re.I,
    )
    cleaned = _clean(raw_text)

    max_records = 1 if "stores at most one record at a time" in cleaned else None
    record_after_completion = "after an eligible completed ordinary player action" in cleaned
    eligible_attack = "eligible: - ordinary attack" in cleaned or "eligible: ordinary attack" in cleaned
    eligible_ability = "direct-damage ability" in cleaned
    standard_card_ineligible = "never eligible: - standard card" in cleaned or "never eligible: standard card" in cleaned
    collapse_multihit = (
        "recorded multihit becomes one analogue hit" in cleaned
        and "does not inherit the original hit count" in cleaned
    )
    clear_after_use = "after use, the record clears" in cleaned
    strips_secondary_mechanics = (
        "never copies" in cleaned
        and "status riders" in cleaned
        and "penetration" in cleaned
        and "element" in cleaned
        and "multihit count" in cleaned
    )

    return FunctionalAnalogueRuleSource(
        raw_text=raw_text,
        single_power=_agreed_value((physical_single, magical_single, hybrid_single)),
        aoe_power=_agreed_value((physical_aoe, magical_aoe, hybrid_aoe)),
        base_hit=_agreed_value((physical_hit, magical_hit, hybrid_hit)),
        physical_element=physical_element,
        magical_element=magical_element,
        hybrid_element=hybrid_element,
        hybrid_physical_weight=int(weights.group(1)) / 100.0 if weights else None,
        hybrid_magical_weight=int(weights.group(2)) / 100.0 if weights else None,
        record_after_completion=record_after_completion,
        eligible_attack=eligible_attack,
        eligible_ability=eligible_ability,
        standard_card_ineligible=standard_card_ineligible,
        max_records=max_records,
        collapse_multihit=collapse_multihit,
        clear_after_use=clear_after_use,
        strips_secondary_mechanics=strips_secondary_mechanics,
    )


__all__ = ["FunctionalAnalogueRuleSource", "parse_functional_analogue_rule_text"]
