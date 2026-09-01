from __future__ import annotations

from tools.diysim.sources.abilities import load_ability_registry, load_ability_source
from tools.diysim.sources.repo import find_repo_root
from tools.diysim.sources.traits import load_trait_registry, load_trait_source


def test_ability_lookup_resolves_registry_entry_to_owner_file() -> None:
    registry = load_ability_registry()
    assert registry

    entry = registry[0]
    source = load_ability_source(entry.ability, class_name=entry.class_name)

    assert source.registry == entry
    assert source.owner_effect
    assert source.owner_mp_text
    assert (find_repo_root() / source.owner_path).is_file()
    if entry.fixed_mp is not None:
        assert source.fixed_mp == entry.fixed_mp


def test_every_registered_ability_has_a_unique_repo_owner() -> None:
    for entry in load_ability_registry():
        source = load_ability_source(entry.ability, class_name=entry.class_name)
        assert source.owner_path
        assert source.owner_effect


def test_trait_lookup_round_trips_registry_without_local_trait_values() -> None:
    registry = load_trait_registry()
    assert registry

    entry = registry[0]
    source = load_trait_source(trait_name=entry.trait_name, class_name=entry.class_name)

    assert source == entry
    assert source.ranks
    assert all(rank.effect for rank in source.ranks)
