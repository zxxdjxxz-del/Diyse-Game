"""Class-Level-aware explicit donor Ordinary equipment at exact campaign checkpoints."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from ..sources.campaign_progression import load_campaign_checkpoint
from ..sources.class_equipment_access import load_character_donor_equipment_access
from ..sources.equipment import EQUIPMENT_REGISTER_PATH, load_equipment
from ..sources.equipment_availability import load_ordinary_weapon_availability
from .class_exp import ClassCexpState, class_level_from_cexp
from .class_state import validate_class_state_at_checkpoint
from .loadouts import (
    EQUIPMENT_SLOT_RULES_PATH,
    EquipmentSlot,
    ProgressionAssumption,
    ResolvedLoadout,
    _dedupe_paths,
    _native_secondary_access,
    _weapon_consumes_secondary,
    resolve_loadout_at_checkpoint,
)


def _slot_for_ordinary_item(name: str, *, root: Path | None) -> EquipmentSlot:
    item = load_equipment(name, root=root)
    if item.layer.casefold() != "ordinary":
        raise ValueError(
            f"Explicit progression equipment currently supports Ordinary gear only: {name}."
        )
    ordinary_weapon_names = {
        row.name.casefold() for row in load_ordinary_weapon_availability(root=root)
    }
    if item.name.casefold() in ordinary_weapon_names:
        return "weapon"
    if item.equipment_type.casefold() in {"shield", "focus"}:
        return "secondary"
    if "armor" in item.equipment_type.casefold():
        return "armor"
    raise ValueError(f"Could not resolve an equipment slot for ordinary item {name!r}.")


def _normalize_choices(
    equipment_choices: Mapping[str, str] | None,
) -> dict[EquipmentSlot, str]:
    result: dict[EquipmentSlot, str] = {}
    for raw_slot, raw_name in (equipment_choices or {}).items():
        slot = raw_slot.strip().casefold()
        if slot not in {"weapon", "armor", "secondary"}:
            raise ValueError(
                f"Unknown equipment slot {raw_slot!r}; use weapon, armor, or secondary."
            )
        name = raw_name.strip()
        if not name:
            raise ValueError(f"Explicit {slot} equipment name cannot be empty.")
        result[slot] = name  # type: ignore[assignment]
    return result


def _is_native_choice(
    character: str,
    slot: EquipmentSlot,
    name: str,
    *,
    root: Path | None,
) -> bool:
    item = load_equipment(name, root=root)
    if slot in {"weapon", "armor"}:
        return item.owner.casefold() == character.casefold()
    families, _ = _native_secondary_access(character, root=root)
    return item.equipment_type.casefold() in families


def _validate_donor_choice(
    character: str,
    slot: EquipmentSlot,
    name: str,
    *,
    subclass_class_level: int,
    availability_through_chapter: int,
    root: Path | None,
) -> tuple[str, list[str]]:
    item = load_equipment(name, root=root)
    actual_slot = _slot_for_ordinary_item(item.name, root=root)
    if actual_slot != slot:
        raise ValueError(f"{item.name} occupies {actual_slot}, not requested slot {slot}.")

    access = load_character_donor_equipment_access(character, root=root)
    required_cl = access.required_class_level(slot)
    if subclass_class_level < required_cl:
        raise ValueError(
            f"{item.name} requires donor {slot} access at Subclass CL{required_cl}; "
            f"{character} is only Subclass CL{subclass_class_level} at this checkpoint."
        )

    paths = [EQUIPMENT_REGISTER_PATH, access.source_path]
    if slot in {"weapon", "armor"}:
        if item.owner.casefold() != access.donor_character.casefold():
            raise ValueError(
                f"{item.name} is neither native {slot} equipment for {character} nor "
                f"ordinary donor {slot} equipment from reciprocal donor {access.donor_character}."
            )
        if slot == "weapon":
            timing = next(
                (
                    row
                    for row in load_ordinary_weapon_availability(root=root)
                    if row.character.casefold() == access.donor_character.casefold()
                    and row.name.casefold() == item.name.casefold()
                ),
                None,
            )
            if timing is None:
                raise ValueError(
                    f"No chapter availability authority was found for donor ordinary weapon {item.name}."
                )
            if timing.first_chapter > availability_through_chapter:
                raise ValueError(
                    f"{item.name} is first available in Chapter {timing.first_chapter}, after "
                    f"this checkpoint's Chapter-{availability_through_chapter} equipment cutoff."
                )
            paths.append(timing.source_path)
    else:
        donor_families, donor_paths = _native_secondary_access(
            access.donor_character,
            root=root,
        )
        family = item.equipment_type.casefold()
        if family not in donor_families:
            raise ValueError(
                f"Current authority does not prove {item.equipment_type} as the reciprocal "
                f"donor Secondary family for {access.donor_character}."
            )
        paths.extend(donor_paths)
        paths.append(EQUIPMENT_SLOT_RULES_PATH)

    return item.name, paths


def _clear_explicit_slot_gaps(
    resolved: ResolvedLoadout,
    explicit_slots: set[EquipmentSlot],
    *,
    consumes_secondary: bool,
) -> tuple:
    gaps = list(resolved.source_gaps)
    if "weapon" in explicit_slots:
        gaps = [
            gap
            for gap in gaps
            if gap.code
            not in {"weapon_availability_timing_missing", "weapon_checkpoint_granularity_missing"}
        ]
    if "armor" in explicit_slots:
        gaps = [gap for gap in gaps if gap.code != "armor_availability_timing_missing"]
    if "secondary" in explicit_slots or consumes_secondary:
        gaps = [gap for gap in gaps if gap.code != "secondary_availability_timing_missing"]

    required = {"weapon", "armor"}
    if not consumes_secondary:
        required.add("secondary")
    if required.issubset(explicit_slots):
        gaps = [
            gap
            for gap in gaps
            if gap.code
            not in {
                "guaranteed_join_loadout_missing",
                "later_mandatory_loadout_map_missing",
                "expected_loadout_policy_missing",
            }
        ]
    return tuple(gaps)


def resolve_class_aware_loadout_at_checkpoint(
    character: str,
    checkpoint_key: str,
    assumption: ProgressionAssumption = "mandatory",
    *,
    equipment_choices: Mapping[str, str] | None = None,
    class_state: ClassCexpState | None = None,
    root: Path | None = None,
) -> ResolvedLoadout:
    """Resolve explicit native/donor Ordinary gear at an exact campaign checkpoint.

    Without `class_state`, behavior is exactly the existing native-only checkpoint
    resolver. Supplying `class_state` makes it a simulation input that is first
    validated against the mandatory CEXP stream. Reciprocal donor Ordinary access
    then follows the source-backed Subclass CL1/3/5 Primary/Armor/Secondary gates.

    Class-state validation currently supports the mandatory route only because the
    repository's optional-CEXP activity/order layer is not yet wired into DiySim.

    Relic and Legacy items remain blocked here because Class Level proves only
    eligibility; actual Relic ownership and donor Legacy completion/ownership are
    separate requirements that DiySim does not yet prove.
    """
    choices = _normalize_choices(equipment_choices)
    if class_state is None:
        return resolve_loadout_at_checkpoint(
            character,
            checkpoint_key,
            assumption,
            equipment_choices=choices,
            root=root,
        )
    if assumption != "mandatory":
        raise ValueError(
            "Explicit class-state validation currently supports the mandatory route only; "
            "optional/route-specific CEXP is not yet modeled."
        )

    validate_class_state_at_checkpoint(
        character,
        checkpoint_key,
        class_state,
        root=root,
    )
    checkpoint = load_campaign_checkpoint(checkpoint_key, root=root)
    subclass_cl = class_level_from_cexp(class_state.subclass_cexp, root=root)

    native_choices: dict[str, str] = {}
    donor_choices: dict[EquipmentSlot, str] = {}
    for slot, name in choices.items():
        actual_slot = _slot_for_ordinary_item(name, root=root)
        if actual_slot != slot:
            raise ValueError(f"{name} occupies {actual_slot}, not requested slot {slot}.")
        if _is_native_choice(character, slot, name, root=root):
            native_choices[slot] = name
        else:
            donor_choices[slot] = name

    resolved = resolve_loadout_at_checkpoint(
        character,
        checkpoint_key,
        assumption,
        equipment_choices=native_choices,
        root=root,
    )
    if not donor_choices:
        return resolved

    # The only Chapter-7 exact checkpoint in current campaign authority is end-Ch7,
    # where Sixfold Volition has just made the fresh Subclass usable at CL1.
    if checkpoint.chapter < 7:
        raise ValueError("Donor equipment cannot be used before Sixfold Volition at end Chapter 7.")

    weapon = resolved.weapon
    armor = resolved.armor
    secondary = resolved.secondary
    paths = list(resolved.source_paths)
    explicit_slots: set[EquipmentSlot] = set(resolved.explicit_slots)

    for slot in ("weapon", "armor", "secondary"):
        if slot not in donor_choices:
            continue
        name, item_paths = _validate_donor_choice(
            character,
            slot,  # type: ignore[arg-type]
            donor_choices[slot],
            subclass_class_level=subclass_cl,
            availability_through_chapter=checkpoint.chapter_granular_equipment_cutoff,
            root=root,
        )
        explicit_slots.add(slot)  # type: ignore[arg-type]
        paths.extend(item_paths)
        if slot == "weapon":
            weapon = name
        elif slot == "armor":
            armor = name
        else:
            secondary = name

    consumes_secondary = _weapon_consumes_secondary(weapon, root=root)
    if consumes_secondary:
        if "secondary" in choices:
            raise ValueError(
                f"{weapon} consumes Weapon + Secondary and cannot be combined with "
                f"explicit Secondary {choices['secondary']}."
            )
        secondary = None

    gaps = _clear_explicit_slot_gaps(
        resolved,
        explicit_slots,
        consumes_secondary=consumes_secondary,
    )
    ordered_slots = tuple(
        slot for slot in ("weapon", "armor", "secondary") if slot in explicit_slots
    )
    return ResolvedLoadout(
        character=resolved.character,
        chapter=resolved.chapter,
        assumption=resolved.assumption,
        weapon=weapon,
        armor=armor,
        secondary=secondary,
        secondary_consumed_by_weapon=consumes_secondary,
        explicit_slots=ordered_slots,
        source_gaps=gaps,
        source_paths=_dedupe_paths(paths),
    )


__all__ = ["resolve_class_aware_loadout_at_checkpoint"]
