# Implementation Notes — Validation & Test Gates

**Status:** ACTIVE IMPLEMENTATION-LEVEL TEST-GATE INDEX  
**Broader QA authority:** `../../16_BALANCE_AND_TESTING/`

Current repository validation proves important implementation foundations. It does not promote proof runtime behavior into gameplay canon.

## Save

`tests/save/validate_save_load.gd`

Validates:
- missing-save safe failure;
- state round-trip;
- supported schema-v1 compatibility;
- canonical save-path precedence plus supported filename fallback;
- supported schema-v1 Face-key normalization to the current Face set;
- `rewards.gold` input normalization to `rewards.g`;
- invalid JSON rejection;
- future schema rejection;
- transient encounter exclusion.

## Combat executable path

`tests/combat/validate_generated_encounter_battle_state.gd`

Validates the current generated-battle engineering path can execute from encounter data through battle-state construction and resolution.

Boundary:
- proof enemy data may still be involved;
- reward storage uses current `g` / **G** terminology, but proof reward amounts remain non-authoritative;
- this test does **not** certify current chapter formation authority;
- it does **not** certify the unresolved production turn-entry flow;
- it does **not** certify current Prime timing/ownership behavior or final Standard Card MP behavior.

Current production combat rules remain owned by `../../05_BATTLE_SYSTEM/`, with known runtime debt recorded in `CURRENT_CODE_DIVERGENCES.md`.

## Encounter runtime contract

`tests/encounters/validate_encounter_runtime_contract.gd`

Validates content-neutral runtime invariants:
- encounter-profile schema;
- unique IDs;
- weighted-pool integrity;
- selector legality;
- pressure-state behavior.

It deliberately does not certify chapter encounter counts, chapter formations, EXP/CEXP totals, or open Chapter-3/4 content decisions.

## Random encounter handoff

`tests/encounters/validate_transient_random_encounter_loop.gd`

Validates:
- field → generated combat → field;
- victory reward handoff;
- flee return;
- encounter-pressure return behavior;
- no invalid payloads.

Additional encounter tests cover field-controller behavior, area tuning and live resolved-movement encounter triggering.

## Dialogue

Current Python contract/compiler tests:
- `tests/dialogue/test_scene_authority_compiler.py` — repository-authority compilation and rejection boundaries;
- `tests/dialogue/test_agent_magic_card_context.py` — lived magic/Card context firewalls;
- `tests/dialogue/test_person_agent_runtime_contract.py` — Person-Agent runtime brain/memory/reliability contract.

Current Godot validators cover:
- authoring schema;
- scene Resource validity;
- exact source parity for completed chapters;
- chapter continuity;
- runtime context construction;
- map-provider request assembly;
- Orchestrator transport;
- packet import;
- field movement/encounter policy;
- controlled preview gating.

## Presentation

HD-2D validators cover:
- presentation metadata;
- environment-state definitions;
- reusable encounter presentation;
- current tier vocabulary;
- player-facing world-intro sync.

Visual capture scripts remain supporting evidence rather than automatic visual approval.

## Kessara copy service

`tests/equipment/validate_kessara_relic_copy_service.gd`

Validates:
- ownership gate;
- matching Face component;
- one copy per identity;
- quantity 2;
- 3 copies/components per Face;
- wrong-Face rejection;
- Legacy rejection.

## Required production-generation tests

As production systems replace proof runtime, add focused regression coverage for:
- current turn-entry command flow and ordering;
- current Prime availability, three-turn manifestation and three-full-normal-party-round spacing;
- Standard Card MP consumption and loadout legality;
- no Mastery Point widgets/fields;
- current class unlock display;
- 3 Standard + 2 Prime slots where currently unlocked;
- no Accessory slot;
- two-slot equipment commitments;
- player-facing **G** display;
- current names/terminology;
- save-schema migrations;
- final PONR warning gating.
