# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse: 2.5D JRPG Clean Active Master Canon v1.34** and newer controlling project authority when supplied or referenced.
3. **Diyse Active Technical Annex v1.34** for exact numerical/effect and accepted implementation rules.
4. **Diyse Active Dialogue Development Annex v1.1** for dialogue craft when applicable.
5. `docs/ACTIVE_CANON.md` and `docs/IMPLEMENTATION_STATUS.md` as repository implementation summaries.
6. Relevant subsystem specification under `docs/`.
7. Existing production code and the accepted regression tests.
8. Historical prototype material only when explicitly requested.

Do not use an older implementation to override a newer design rule.

## Current phase rule

Step 7B.5 technical feasibility is **COMPLETE / PASS**. The accepted 7B.5 tests and real-device behavior are now a regression baseline, not an open experiment queue.

Step 7C full Dialogue-First Scene Writing remains **ON HOLD until explicit user authorization**. Engineering work may prepare generic systems/data interfaces without silently beginning final scene scripting.

## No invention policy

When a required detail is missing:

- use a clearly labeled placeholder if the milestone allows one;
- isolate it in data/configuration;
- document the assumption;
- do not present the placeholder as canon.

Never invent a permanent mechanic merely to unblock coding.

## Proven-architecture protection

Do not casually replace or bypass architecture already accepted through 7B.5:

- 2.5D world-space exploration on real 3D fields;
- authored dialogue with no player response system;
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

Do not create one bespoke class per content record unless behavior genuinely requires code.

## Testing rule

Separate simulation from presentation enough that core logic can be validated without waiting on animations.

The accepted Step 7B.5 regression suite must remain green during production unless a newer approved authority intentionally changes the rule under test. Add new tests as production systems become more complete; do not weaken existing tests merely to make a new implementation pass.

## Android rule

Desktop-only success is provisional for controls, layout, performance, persistence, lifecycle or platform integration. The project has already demonstrated repeatable Android ARM64 builds and real-device acceptance; future platform-facing changes must preserve that expectation.

## Proof-content rule

The following are replaceable, non-canon fixtures and must not be mistaken for permanent content authority:

- graybox field geometry;
- placeholder character sprites/portraits;
- disposable proof dialogue;
- Raider proof enemies/stats;
- `Proof Strike`;
- temporary flat damage/reward values;
- proof chest/state flags;
- temporary debug/button UI.

## Historical code rule

`zxxdjxxz-del/Diyse` is not a dependency and must not be added as a submodule, package, source-copy location, or automatic migration source.

If an old idea is worth preserving, re-derive the requirement and implement it cleanly in Godot unless a task explicitly authorizes code reuse.