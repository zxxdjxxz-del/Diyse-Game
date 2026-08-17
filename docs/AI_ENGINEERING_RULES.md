# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse Clean Active Complete Master Canon v1.60 / Audit75** and any newer controlling project authority.
3. `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, and the relevant closed chapter package under `docs/chapters/`.
4. Compatible accepted technical annex/proof authority for exact system behavior.
5. Compatible completed dialogue-study craft authority and production source material.
6. Relevant subsystem specification under `docs/`, including `DIALOGUE_AUTHORING_SCHEMA.md` for production dialogue.
7. Existing production code and accepted regression tests.
8. Historical prototype material only when explicitly requested.

Do not use an older implementation or stale document to override a newer design rule.

## Current phase rule

Step 7B.5 technical feasibility is COMPLETE / PASS. Its accepted tests and real-device behavior are regression baseline, not an open experiment queue.

Step 7B.6 production handoff is COMPLETE / PASS. Dialogue uses stable-ID Resources and portrait-registry indirection rather than embedding final text/assets into generic UI code.

**Chapters 0–3 are COMPLETE/CLOSED authoring authority.**

- Chapter 0 is already complete/merged as validated Resources at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`, subject to later canon compatibility overlays.
- Chapters 1–3 still need Resource conversion and implementation validation. That work is translation of closed material, not a fresh writing pass.
- Chapter 4 — The Seventh Reaction — is the next exact scene-authoring frontier.

## Closed-chapter implementation workflow

When implementing Chapters 1–3:

- start from the relevant `docs/chapters/CHAPTER_0X_COMPLETE.md`;
- preserve approved scene purpose, protected lines/beats, pair progression, knowledge firewalls, geography, roster changes, combat handoffs, and affordable-2.5D staging;
- convert to the accepted `DiyseDialogueSceneDefinition` Resource schema;
- register required IDs/portraits/state dependencies without inventing story content;
- run scene-specific validation;
- run one whole-chapter continuity/runtime pass;
- run full Godot + Android regression at the chapter implementation checkpoint unless an engine/schema/platform change requires earlier gating.

A missing `.tres` file is **not evidence that the dialogue is missing**.

## New-authoring workflow

For Chapter 4+ new scene work, use the chapter-level process proven earlier: one branch/PR per chapter or substantial narrative block, scene-level review/checkpointing, chapter continuity/voice/runtime review, then exact-head Godot + Android gating and one authority/archive checkpoint.

## No invention policy

When a required implementation detail is missing, use a clearly labeled placeholder only when the milestone permits it, isolate it in data/configuration, document the assumption, and do not present it as canon. Never invent permanent mechanics, dialogue, lore, characters, relationships, or story outcomes merely to unblock coding.

## Proven-architecture protection

Do not casually replace or bypass accepted architecture:

- 2.5D world-space exploration on real 3D fields;
- authored dialogue with no player response system;
- stable-ID Resource-backed production dialogue with portrait registry indirection and structural validation;
- discrete-round combat with enemy action locking and Item / Defend / Speed resolution;
- deterministic automatic hostile retargeting;
- unlimited data-driven Standard Cards;
- directly controlled Prime replacement/suspension/return behavior;
- versioned plain-data persistence separate from scene nodes;
- Android as a first-class build/test target.

Chapter 0's complete dialogue/Resource/continuity validation remains an accepted regression baseline. If newer authority changes an accepted behavior, update code, documentation, and tests deliberately together.

## Chapter 0 compatibility boundary

The live S004/S005 Resource/test set still contains the old internal label `Broken Champion's Ward`. Audit75 supersedes that as canon terminology: the phenomenon is only an incomplete green/gold protective response from the sealed Card, not a Prime/Last Sentinel activation or bearer confirmation.

Do not blindly rename just the Resource or just the validator. A bounded cleanup must change matched internal handles together and preserve the approved temporary S004→S005 protection behavior unless a separate balance decision changes it.

## Critical geography boundary

Chapter 3 is **Caelora → Old City / Suppressed Archives → separate Cresthaven**. Never collapse Cresthaven into the Old City during implementation.

## Scope discipline

For each task identify the exact subsystem being changed, avoid unrelated refactors, preserve public interfaces unless intentionally changing them, add/update deterministic tests where practical, report temporary shortcuts, and distinguish production content from fixtures.

For closed Chapters 1–3, canon/voice approval is already complete; implementation completion still requires valid Resources, IDs/dependencies, continuity validation, and the required regression gate.

## Architecture direction

Prefer separable modules for game/session state, save/load, content/data loading, exploration, interaction, dialogue, combat state/resolution, actions/effects, Cards, Primes, AI decision logic, UI/presentation, and Android/platform integration. Avoid one monolithic scene script controlling unrelated systems.

## Data-driven rule

Final authored content should be data/Resources wherever practical. Production dialogue specifically uses `DiyseDialogueSceneDefinition` Resources and registered portrait/expression IDs. Do not create one bespoke class per scene or hard-code canon scene text into the runner.

## Affordable 2.5D rule

If a prose beat appears to demand a unique animation for every micro-action, simplify the physical staging without changing the dialogue/meaning. Prefer reusable interaction poses, portraits, props, camera inserts, prepared environment states, VFX, layered crowds, and silence. Do not introduce fluid simulation, physics destruction, crowd AI, or actor-body mimic systems to literalize prose that can be communicated more cheaply.

## Testing rule

Separate simulation from presentation enough that core logic/content contracts can be validated without animation timing. Accepted 7B.5, 7B.6, and Chapter 0 regression suites remain green unless newer approved authority intentionally changes the rule under test. Do not weaken tests merely to make new content pass.

## Android rule

Desktop-only success is provisional for controls, layout, performance, persistence, lifecycle or platform integration. Chapter-level dialogue conversion does not require an APK after every scene, but the exact final chapter implementation head must pass the required Android export unless the workflow is explicitly revised.

## Proof-content rule

Graybox geometry, placeholder sprites/portraits, disposable proof dialogue and `PROOF_SCHEMA`, proof registry/cues, Raider proof enemies/stats, `Proof Strike`, temporary flat values/rewards, proof flags, and debug UI remain replaceable non-canon fixtures.

## Historical code rule

`zxxdjxxz-del/Diyse` is not a dependency and must not be added as a submodule, package, source-copy location, or automatic migration source. Re-derive any useful old requirement and implement it cleanly in Godot unless a task explicitly authorizes named code reuse.