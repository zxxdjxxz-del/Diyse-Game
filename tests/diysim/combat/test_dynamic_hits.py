from __future__ import annotations

from tools.diysim.combat.dynamic_hits import build_current_next_hit_package, next_cycle_element


def test_standard_element_cycle_wraps_in_authored_order() -> None:
    assert next_cycle_element("fire") == "ice"
    assert next_cycle_element("ice") == "lightning"
    assert next_cycle_element("lightning") == "earth"
    assert next_cycle_element("earth") == "fire"


def test_dynamic_hit_package_materializes_current_and_next_elements() -> None:
    package = build_current_next_hit_package(
        name="Confluence Spear",
        target_scope="one",
        damage_kind="magical",
        current_element="lightning",
        per_hit_powers=(215, 215),
        base_hit=100,
        linked_status_chance=15,
        max_new_harmful_statuses=1,
    )

    assert [hit.element for hit in package.hits] == ["lightning", "earth"]
    assert [hit.power for hit in package.hits] == [215, 215]
    assert all(hit.base_hit == 100 for hit in package.hits)
    assert package.max_new_harmful_statuses == 1
