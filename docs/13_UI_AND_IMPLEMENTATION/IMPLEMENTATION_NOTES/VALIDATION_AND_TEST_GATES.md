# Implementation Notes — Validation & Test Gates
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


Current repository has automated validation for important foundations.

## Save
`tests/save/validate_save_load.gd`
Validates:
- missing-save safe failure;
- full state round-trip;
- pre-Kessara schema-v1 compatibility;
- invalid JSON rejection;
- future schema rejection;
- transient encounter exclusion.

## Combat
`tests/combat/validate_round_combat.gd`
Covers proof of:
- Item/Defend priority;
- Speed order;
- tie behavior;
- enemy action lock timing;
- one selected party action;
- hostile retarget;
- Card/Prime proof behavior.

Important:
some Prime expectations in this historical proof test are now stale and must be rewritten when production Prime logic is reconciled.

## Random encounter handoff
`tests/encounters/validate_transient_random_encounter_loop.gd`
Validates:
- field → generated combat → field;
- victory reward handoff;
- flee return;
- encounter-pressure return behavior;
- no invalid payloads.

## Dialogue
Current validators cover:
- authoring schema;
- scene Resource validity;
- exact source parity for completed chapters;
- chapter continuity;
- runner behavior.

## Presentation
HD-2D validators cover:
- presentation metadata;
- environment-state definitions;
- reusable encounter presentation;
- current tier vocabulary.

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

## Required next-generation UI tests
When production UI is built, add tests for:
- no Mastery Point widgets/fields;
- current class unlock display;
- 3 Standard + 2 Prime slots;
- no Accessory slot;
- two-slot equipment commitments;
- Auren display;
- current Prime availability/cooldown;
- current names/terminology;
- save-schema migrations;
- final PONR warning gating.
