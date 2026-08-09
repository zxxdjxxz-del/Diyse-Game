# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse: 2.5D JRPG Clean Active Master Canon v1.35** and newer controlling project authority when supplied or referenced.
3. **Diyse Active Technical Annex v1.35** for exact numerical/effect, accepted implementation, and production authoring-interface rules.
4. **Diyse Active Dialogue Development Annex v1.2** for dialogue craft and the locked Step 7C authoring contract when applicable.
5. `docs/ACTIVE_CANON.md` and `docs/IMPLEMENTATION_STATUS.md` as repository implementation summaries.
6. Relevant subsystem specification under `docs/`, including `DIALOGUE_AUTHORING_SCHEMA.md` for production dialogue.
7. Existing production code and the accepted regression tests.
8. Historical prototype material only when explicitly requested.

Do not use an older implementation to override a newer design rule.

## Current phase rule

Step 7B.5 technical feasibility is **COMPLETE / PASS**. The accepted 7B.5 tests and real-device behavior are now a regression baseline, not an open experiment queue.

Step 7B.6 production handoff is **COMPLETE / PASS**. Production dialogue must use the accepted stable-ID Resource contract and portrait-registry indirection rather than embedding final scene text/assets into generic UI code.

Step 7C Dialogue-First Scene Writing is **ACTIVE / AUTHORIZED as of August 8, 2026**. Begin with Chapter 0 S001–S006, then C01 and C02 unless the user explicitly changes the order. Authorization opens scene writing but does not pre-approve draft wording or permit silent canon changes.

## No invention policy

When a required detail is missing:

- use a clearly labeled placeholder if the milestone allows one;
- isolate it in data/configuration;
- document the assumption;
- do not present the placeholder as canon.

Never invent a permanent mechanic merely to unblock coding.

## Proven-architecture protection

Do not casually replace or bypass architecture already accepted through 7B.5 and 7B.6:

- 2.5D world-space exploration on real 3D fields;
- authored dialogue with no player response system;
- stable-ID Resource-backed production dialogue with portrait registry indirection and structural validation;
- discrete-round combat with enemy action locking and Item / Defend / Speed resolution;
- deterministic automatic hostile retargeting;
- unlimited data-driven Standard Cards;
- directly controlled Prime replacement/suspension/return behavior;
- versioned plain-data persistence separate from scene nodes;
- Android as a first-class build/test target.

A newer approved authority may change one of these rules, but any such change must update documentation and regression tests deliberately.

## Scope discipline

For each task:

- identify the exact subsystem being changed;
- avoid unrelated refactors unless required for correctness;
- preserve public interfaces unless the task intentionally changes them;
- add or update tests for deterministic logic;
- report temporary shortcuts explicitly;
- distinguish production content from test fixtures.

For Step 7C, keep each scene draft bounded. A draft becomes approved production dialogue only after canon/voice review and structural validation.

## Architecture direction

Prefer separable modules for:

- game/session state;
- save/load;
- content/data loading;
- exploration;
- interaction;
- dialogue;
- combat state/resolution;
- combat actions/effects;
- Cards;
- Primes;
- AI decision logic;
- UI/presentation;
- Android/platform integration.

Avoid one monolithic scene script controlling unrelated systems.

## Data-driven rule

Final authored content should be representable as data/resources wherever practical, including characters, Abilities, Cards, Items, enemies, encounters, dialogue records, and world-state definitions.

Production dialogue specifically uses `DiyseDialogueSceneDefinition` Resources and registered portrait/expression IDs. Do not create one bespoke class per scene or hard-code canon scene text into the runner.

Do not create one bespoke class per content record unless behavior genuinely requires code.

## Testing rule

Separate simulation from presentation enough that core logic can be validated without waiting on animations.

The accepted Steps 7B.5 and 7B.6 regression suite must remain green during production unless a newer approved authority intentionally changes the rule under test. Add new tests as production systems become more complete; do not weaken existing tests merely to make a new implementation pass.

## Android rule

Desktop-only success is provisional for controls, layout, performance, persistence, lifecycle or platform integration. The project has already demonstrated repeatable Android ARM64 builds and real-device acceptance; future platform-facing changes must preserve that expectation.

## Proof-content rule

The following are replaceable, non-canon fixtures and must not be mistaken for permanent content authority:

- graybox field geometry;
- placeholder character sprites/portraits;
- disposable proof dialogue and `PROOF_SCHEMA`;
- proof portrait registry/cues;
- Raider proof enemies/stats;
- `Proof Strike`;
- temporary flat damage/reward values;
- proof chest/state flags;
- temporary debug/button UI.

## Historical code rule

`zxxdjxxz-del/Diyse` is not a dependency and must not be added as a submodule, package, source-copy location, or automatic migration source.

If an old idea is worth preserving, re-derive the requirement and implement it cleanly in Godot unless a task explicitly authorizes code reuse.