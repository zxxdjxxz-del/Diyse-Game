#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    context = (ROOT / "external-services/canary/context/magic_and_cards.yaml").read_text(encoding="utf-8")
    person_agent = (ROOT / "external-services/canary/person_agent.py").read_text(encoding="utf-8")
    orchestrator = (ROOT / "external-services/canary/scene_orchestrator.py").read_text(encoding="utf-8")
    world = (ROOT / "docs/04_WORLD_AND_LORE/LIVED_MAGIC_AND_CARD_CONTEXT.md").read_text(encoding="utf-8")
    firewall = (ROOT / "docs/04_WORLD_AND_LORE/MODERN_KNOWLEDGE_FIREWALL.md").read_text(encoding="utf-8")
    ability = (ROOT / "docs/06_CLASSES_AND_ABILITIES/ABILITY_RULES.md").read_text(encoding="utf-8")
    cards = (ROOT / "docs/07_CARDS/CARD_SYSTEM_MASTER.md").read_text(encoding="utf-8")

    # Lived magical reality.
    expect(
        "abilities_are_natural_forms_of_magic_expressed_through_the_user" in context,
        "Person Agents lost the natural-magic baseline.",
    )
    expect(
        "holding_using_the_card_grants_access_to_that_preserved_ability" in context,
        "Person Agents lost the Standard Card preserved-ability baseline.",
    )
    expect(
        "Character Abilities are natural forms of magic" in ability,
        "Class authority no longer states the lived natural-magic rule.",
    )
    expect(
        "Standard Cards are a normal, known part of modern magical life" in cards,
        "Card authority no longer states Standard Card modern normality.",
    )

    # Prime modern-history firewall.
    for text, name in ((context, "runtime context"), (world, "world authority"), (firewall, "knowledge firewall")):
        folded = text.casefold()
        expect(
            "no_one_in_known_modern_history_has_knowingly_possessed_a_prime_card" in folded
            or "no one in known modern history has knowingly possessed a prime card" in folded,
            f"{name} lost the no-known-modern-Prime-holder rule.",
        )
        expect(
            "no_one_in_known_modern_history_has_knowingly_activated_or_used_a_prime_card" in folded
            or "no one in known modern history has knowingly activated or used a prime card" in folded,
            f"{name} lost the no-known-modern-Prime-use rule.",
        )

    expect(
        "Prime_is_mentioned_only_in_a_very_small_number_of_surviving_late_Diysean_records" in context,
        "Runtime context lost sparse late-Diysean Prime provenance.",
    )
    expect(
        "what_a_Prime_actually_does" in context,
        "Runtime context lost operational Prime ignorance.",
    )

    # Chapter 0 opening Card significance must remain ordered correctly:
    # Crown-directed excavation/transport first; apparent uselessness second;
    # genuine Card anomaly only when it responds around Cyanis.
    expect(
        "the_Crown_had_the_card_excavated_and_ordered_it_transport_to_Caelora" in context,
        "Runtime context lost Crown-directed excavation/transport of the opening Card.",
    )
    expect(
        "nonactivation_is_strange_but_naturally_suggests_inert_damaged_failed_or_useless_not_secretly_powerful" in context,
        "Runtime context incorrectly treats initial Card nonactivation as hidden power.",
    )
    expect(
        "the_first_incomplete_response_is_the_first_genuine_behavioral_anomaly" in context,
        "Runtime context lost the P04 first-response anomaly threshold.",
    )
    expect(
        "**crown had the card excavated** from an ancient site" in world.casefold(),
        "World authority lost Crown-directed excavation provenance.",
    )

    # Persistent Person Agents must not see author-only Story Prime assignment.
    expect(
        'runtime_identity.pop("prime", None)' in person_agent,
        "Persistent Person Agent no longer redacts identity.prime.",
    )
    expect(
        "never infer your own future Prime association from author metadata" in person_agent,
        "Persistent Person Agent prompt lost future-Prime-association guard.",
    )

    # Profile-only Person Agents must receive a redacted character-facing profile.
    expect(
        "def profile_person_view(" in orchestrator,
        "Profile-only Person Agent redaction helper is missing.",
    )
    expect(
        '"participant_profile": profile_person_view(profiles[cid])' in orchestrator,
        "Profile-only Person Agent is no longer using the redacted profile view.",
    )
    expect(
        r'^\s*-\s*Story Prime\s*:' in orchestrator,
        "Profile-only redaction no longer strips Story Prime metadata from authority text.",
    )

    # The permanent-six author profiles still retain system metadata; redaction belongs at
    # the character-facing boundary rather than destroying useful author canon.
    for character in ("Cyanis", "Ilyra", "Torren", "Nimera", "Vaelira", "Seyrik"):
        profile = (ROOT / f"docs/01_CHARACTERS/PLAYABLE/{character}.md").read_text(encoding="utf-8")
        expect("Story Prime:" in profile, f"{character} author profile unexpectedly lost Story Prime metadata.")

    print("Diyse Agent lived-magic / Card / Prime-knowledge regression validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
