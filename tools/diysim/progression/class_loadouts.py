"""Class-Level-aware explicit donor Ordinary and Relic equipment at exact checkpoints."""
from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from ..sources.campaign_progression import load_campaign_checkpoint
from ..sources.class_equipment_access import load_character_donor_equipment_access
from ..sources.equipment import EQUIPMENT_REGISTER_PATH, load_equipment
from ..sources.equipment_availability import load_ordinary_weapon_availability
from ..sources.relics import load_relic_placement, load_relic_weapon
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


def _slot_for_class_aware_item(name: str, *, root: Path | None) -> EquipmentSlot:
    item = load_equipment(name, root=root)
    layer = item.layer.casefold()
    equipment_type = item.equipment_type.casefold()
    if layer == "ordinary":
        ordinary_weapon_names = {
            row.name.casefold() for row in load_ordinary_weapon_availability(root=root)
        }
        if item.name.casefold() in ordinary_weapon_names:
            return "weapon"
        if equipment_type in {"shield", "focus"}:
            return "secondary"
        if "armor" in equipment_type:
            return "armor"
        raise ValueError(f"Could not resolve an equipment slot for ordinary item {name!r}.")
    if layer == "relic":
        if equipment_type == "weapon":
            return "weapon"
        if equipment_type == "armor":
            return "armor"
        if equipment_type in {"shield", "focus"}:
            return "secondary"
        raise ValueError(f"Could not resolve an equipment slot for Relic {name!r}.")
    if layer == "legacy":
        raise ValueError(
            f"Legacy equipment is not yet supported by class-aware progression inputs: {name}. "
            "Legacy completion/ownership must be proven separately."
        )
    raise ValueError(f"Unsupported progression equipment layer {item.layer!r}: {name}")


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


def _is_native_ordinary_choice(
    character: str,
    slot: EquipmentSlot,
    name: str,
    *,
    root: Path | None,
) -> bool:
    item = load_equipment(name, root=root)
    if item.layer.casefold() != "ordinary":
        return False
    if slot in {"weapon", "armor"}:
        return item.owner.casefold() == character.casefold()
    families, _ = _native_secondary_access(character, root=root)
    return item.equipment_type.casefold() in families


def _validate_donor_ordinary_choice(
    character: str,
    slot: EquipmentSlot,
    name: str,
    *,
    subclass_class_level: int,
    availability_through_chapter: int,
    root: Path | None,
) -> tuple[str, list[str]]:
    item = load_equipment(name, root=root)
    if item.layer.casefold() != "ordinary":
        raise ValueError(f"Expected Ordinary donor equipment, got {item.layer}: {item.name}")
    actual_slot = _slot_for_class_aware_item(item.name, root=root)
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


def _validate_relic_choice(
    character: str,
    slot: EquipmentSlot,
    name: str,
    *,
    subclass_class_level: int,
    availability_through_chapter: int,
    root: Path | None,
) -> tuple[str, list[str]]:
    item = load_equipment(name, root=root)
    if item.layer.casefold() != "relic":
        raise ValueError(f"Expected Relic equipment, got {item.layer}: {item.name}")
    actual_slot = _slot_for_class_aware_item(item.name, root=root)
    if actual_slot != slot:
        raise ValueError(f"{item.name} occupies {actual_slot}, not requested slot {slot}.")

    placement = load_relic_placement(item.name, root=root)
    if placement.chapter > availability_through_chapter:
        raise ValueError(
            f"{item.name} is first obtainable in Chapter {placement.chapter}, after this "
            f"checkpoint's Chapter-{availability_through_chapter} equipment cutoff."
        )

    # Shared Relic Shield/Focus rows do not identify one native/donor Base tradition.
    # Do not infer their class-access route merely from ordinary Secondary legality.
    if slot == "secondary":
        raise ValueError(
            f"{item.name} is a shared Relic Secondary. Current authority does not map shared "
            "Relic Secondary ownership/access to one native or reciprocal donor tradition, "
            "so DiySim will not infer its class-access route."
        )

    paths = [EQUIPMENT_REGISTER_PATH, placement.source_path, EQUIPMENT_SLOT_RULES_PATH]
    if item.owner.casefold() == character.casefold():
        if slot == "weapon":
            weapon_source = load_relic_weapon(item.name, root=root)
            paths.append(weapon_source.source_path)
        return item.name, paths

    access = load_character_donor_equipment_access(character, root=root)
    if item.owner.casefold() != access.donor_character.casefold():
        raise ValueError(
            f"{item.name} is neither a native Relic for {character} nor a Relic from reciprocal "
            f"donor {access.donor_character}."
        )
    if subclass_class_level < access.relic_class_level:
        raise ValueError(
            f"{item.name} requires donor Relic eligibility at Subclass CL{access.relic_class_level}; "
            f"{character} is only Subclass CL{subclass_class_level} at this checkpoint."
        )
    paths.append(access.source_path)
    if slot == "weapon":
        weapon_source = load_relic_weapon(item.name, root=root)
        paths.append(weapon_source.source_path)
    return item.name, paths


def _class_aware_weapon_consumes_secondary(name: str | None, *, root: Path | None) -> bool:
    if not name:
        return False
    item = load_equipment(name, root=root)
    if item.layer.casefold() == "relic" and item.equipment_type.casefold() == "weapon":
        return load_relic_weapon(item.name, root=root).consumes_secondary
    return _weapon_consumes_secondary(name, root=root)


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
    """Resolve explicit Ordinary/Relic gear at an exact campaign checkpoint.

    Without `class_state`, behavior is exactly the existing native-Ordinary-only
    checkpoint resolver. Supplying `class_state` first validates the mandatory CEXP
    state. Reciprocal donor Ordinary access then follows Subclass CL1/3/5. Explicit
    Relic choices are treated as assumed-owned inventory instances and must satisfy
    first-acquisition chapter timing; reciprocal donor Relics additionally require
    Subclass CL7 Equipment Mastery.

    Class-state validation currently supports the mandatory route only because the
    repository's optional-CEXP activity/order layer is not yet wired into DiySim.

    Legacy equipment remains blocked because CL11 proves only eligibility; actual
    Legacy project completion/ownership is a separate requirement not yet modeled.
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

    native_ordinary_choices: dict[str, str] = {}
    class_aware_choices: dict[EquipmentSlot, str] = {}
    for slot, name in choices.items():
        actual_slot = _slot_for_class_aware_item(name, root=root)
        if actual_slot != slot:
            raise ValueError(f"{name} occupies {actual_slot}, not requested slot {slot}.")
        if _is_native_ordinary_choice(character, slot, name, root=root):
            native_ordinary_choices[slot] = name
        else:
            class_aware_choices[slot] = name

    resolved = resolve_loadout_at_checkpoint(
        character,
        checkpoint_key,
        assumption,
        equipment_choices=native_ordinary_choices,
        root=root,
    )
    if not class_aware_choices:
        return resolved

    weapon = resolved.weapon
    armor = resolved.armor
    secondary = resolved.secondary
    paths = list(resolved.source_paths)
    explicit_slots: set[EquipmentSlot] = set(resolved.explicit_slots)

    for slot in ("weapon", "armor", "secondary"):
        if slot not in class_aware_choices:
            continue
        name = class_aware_choices[slot]
        item = load_equipment(name, root=root)
        if item.layer.casefold() == "ordinary":
            if checkpoint.chapter < 7:
                raise ValueError(
                    "Donor Ordinary equipment cannot be used before Sixfold Volition at end Chapter 7."
                )
            validated_name, item_paths = _validate_donor_ordinary_choice(
                character,
                slot,  # type: ignore[arg-type]
                name,
                subclass_class_level=subclass_cl,
                availability_through_chapter=checkpoint.chapter_granular_equipment_cutoff,
                root=root,
            )
        elif item.layer.casefold() == "relic":
            validated_name, item_paths = _validate_relic_choice(
                character,
                slot,  # type: ignore[arg-type]
                name,
                subclass_class_level=subclass_cl,
                availability_through_chapter=checkpoint.chapter_granular_equipment_cutoff,
                root=root,
            )
        else:
            # `_slot_for_class_aware_item` already gives a more specific Legacy error.
            raise ValueError(f"Unsupported class-aware equipment layer: {item.layer}")

        explicit_slots.add(slot)  # type: ignore[arg-type]
        paths.extend(item_paths)
        if slot == "weapon":
            weapon = validated_name
        elif slot == "armor":
            armor = validated_name
        else:
            secondary = validated_name

    consumes_secondary = _class_aware_weapon_consumes_secondary(weapon, root=root)
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
