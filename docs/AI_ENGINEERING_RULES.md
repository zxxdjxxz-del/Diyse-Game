# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. Current authoritative Diyse canon/source documents when supplied or referenced.
3. `docs/ACTIVE_CANON.md` as the repository implementation summary.
4. Relevant subsystem specification under `docs/`.
5. Existing production code and tests.
6. Historical prototype material only when explicitly requested.

Do not use an older implementation to override a newer design rule.

## No invention policy

When a required detail is missing:

- use a clearly labeled placeholder if the milestone allows one;
- isolate it in data/configuration;
- document the assumption;
- do not present the placeholder as canon.

Never invent a permanent mechanic merely to unblock coding.

## Scope discipline

For each task:

- identify the exact subsystem being changed;
- avoid unrelated refactors unless required for correctness;
- preserve public interfaces unless the task intentionally changes them;
- add or update tests for deterministic logic;
- report temporary shortcuts explicitly.

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

The technical proof should accumulate regression tests as each gate is implemented.

## Android rule

Desktop-only success is provisional. Any feature that affects controls, layout, performance, persistence, or lifecycle is not fully accepted until Android validation occurs.

## Historical code rule

`zxxdjxxz-del/Diyse` is not a dependency and must not be added as a submodule, package, source-copy location, or automatic migration source.

If an old idea is worth preserving, re-derive the requirement and implement it cleanly in Godot unless a task explicitly authorizes code reuse.
