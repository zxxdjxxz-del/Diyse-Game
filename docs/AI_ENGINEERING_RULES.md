# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse: 2.5D JRPG Clean Active Master Canon v1.36** and newer controlling project authority when supplied or referenced.
3. **Diyse Active Technical Annex v1.36** for exact numerical/effect, accepted implementation, production-authoring-interface, and Chapter 0 validation rules.
4. **Diyse Active Dialogue Development Annex v1.3** for dialogue craft, the locked authoring contract, and approved Chapter 0 production dialogue when applicable.
5. `docs/ACTIVE_CANON.md` and `docs/IMPLEMENTATION_STATUS.md` as repository implementation summaries.
6. Relevant subsystem specification under `docs/`, including `DIALOGUE_AUTHORING_SCHEMA.md` for production dialogue.
7. Existing production code and accepted regression tests.
8. Historical prototype material only when explicitly requested.

Do not use an older implementation to override a newer design rule.

## Current phase rule

Step 7B.5 technical feasibility is **COMPLETE / PASS**. Its accepted tests and real-device behavior are a regression baseline, not an open experiment queue.

Step 7B.6 production handoff is **COMPLETE / PASS**. Production dialogue must use the stable-ID Resource contract and portrait-registry indirection rather than embedding final scene text/assets into generic UI code.

Step 7C is **ACTIVE**. Chapter 0 S001–S006 plus C01/C02 is **COMPLETE / APPROVED / MERGED** at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`. The next mandatory production block is **Chapter 1 S007–S011**.

## Chapter-level production workflow

The default workflow proven by Chapter 0 is:

- one branch/PR per chapter or comparable substantial narrative block;
- one chapter tracker instead of per-scene PR/issue churn;
- individual scene review/checkpointing before advancing;
- scene-specific validation as content is authored;
- whole-chapter continuity/repetition/voice/runtime review after the chapter's scene set is approved;
- full Godot + Android regression only at the chapter checkpoint unless engine/schema/platform behavior changes earlier;
- one authority/archive checkpoint after the chapter/substantial milestone completes.

## No invention policy

When a required detail is missing, use a clearly labeled placeholder only if the milestone allows it, isolate it in data/configuration, document the assumption, and do not present the placeholder as canon. Never invent a permanent mechanic merely to unblock coding.

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

Chapter 0's complete dialogue/resource/continuity validation is now also an accepted production regression baseline. A newer approved authority may change these rules, but any such change must update documentation and regression tests deliberately.

## Scope discipline

For each task identify the exact subsystem being changed, avoid unrelated refactors, preserve public interfaces unless intentionally changing them, add/update deterministic tests, report temporary shortcuts, and distinguish production content from fixtures.

For Step 7C, a scene becomes approved production dialogue only after canon/voice review and structural validation. A chapter becomes production-complete only after the chapter-level continuity pass and exact-head regression gate.

## Architecture direction

Prefer separable modules for game/session state, save/load, content/data loading, exploration, interaction, dialogue, combat state/resolution, combat actions/effects, Cards, Primes, AI decision logic, UI/presentation, and Android/platform integration. Avoid one monolithic scene script controlling unrelated systems.

## Data-driven rule

Final authored content should be data/resources wherever practical. Production dialogue specifically uses `DiyseDialogueSceneDefinition` Resources and registered portrait/expression IDs. Do not create one bespoke class per scene or hard-code canon scene text into the runner.

## Testing rule

Separate simulation from presentation enough that core logic can be validated without animation timing. The accepted 7B.5, 7B.6, and Chapter 0 production-dialogue regression suites must remain green unless a newer approved authority intentionally changes the rule under test. Do not weaken tests merely to make new content pass.

## Android rule

Desktop-only success is provisional for controls, layout, performance, persistence, lifecycle or platform integration. The project has demonstrated repeatable Android ARM64 builds and real-device acceptance. Chapter-level dialogue-only work does not require an APK after every scene; the exact final chapter head must still pass Android export unless a newer workflow explicitly changes that requirement.

## Proof-content rule

Graybox field geometry, placeholder character sprites/portraits, disposable proof dialogue and `PROOF_SCHEMA`, proof portrait registry/cues, Raider proof enemies/stats, `Proof Strike`, temporary flat damage/reward values, proof chest/state flags, and temporary debug/button UI remain replaceable non-canon fixtures.

## Historical code rule

`zxxdjxxz-del/Diyse` is not a dependency and must not be added as a submodule, package, source-copy location, or automatic migration source. Re-derive any useful old requirement and implement it cleanly in Godot unless a task explicitly authorizes code reuse.