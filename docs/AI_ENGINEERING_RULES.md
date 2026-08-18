# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse Clean Active Complete Master Canon v1.64 / Audit79** and any newer controlling project authority.
3. `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, and the relevant closed chapter package under `docs/chapters/`.
4. Compatible accepted technical annex/proof authority for exact system behavior, only where it does not conflict with v1.64 / Audit79 or newer corrections.
5. Compatible completed dialogue-study craft authority and exact production source material.
6. Relevant subsystem specification under `docs/`, including `DIALOGUE_AUTHORING_SCHEMA.md` for production dialogue.
7. Existing production code and accepted regression tests, interpreted through current authority.
8. Historical prototype/recovery material only when explicitly requested or when a current authority explicitly inherits a compatible clause.

Do not use an older implementation, proof fixture, stale document, legacy identifier, or superseded numeric table to override a newer design rule.

## Current phase rule

Step 7B.5 technical feasibility is COMPLETE / PASS. Its accepted tests and real-device behavior are a technical regression baseline, not current whole-project canon and not an open experiment queue.

Step 7B.6 production handoff is COMPLETE / PASS. Dialogue uses stable-ID Resources and portrait-registry indirection rather than embedding final text/assets into generic UI code.

**Chapters 0–3 are COMPLETE/CLOSED authoring authority and their dialogue Resource conversions are complete/validated.**

- Chapter 0 is complete/merged as validated Resources at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`, subject to later canon compatibility overlays.
- Chapter 1 S007–S011 + C03–C05 is converted/validated with exact source parity and chapter continuity.
- Chapter 2 S012–S016 + C06/C07 is converted/validated with exact source parity and chapter continuity.
- Chapter 3 S017–S021 + H01–H04 is converted/validated with exact source parity, corrected Cresthaven geography/handoff, Warden limits, Last Sentinel timing, and optional-scene locks.
- There is **no remaining Chapters 0–3 dialogue-Resource conversion backlog**.
- Chapter 4 — **The Seventh Reaction** — is the next exact scene-authoring frontier.

## Closed-chapter implementation workflow

For follow-on implementation in Chapters 0–3:

- start from the relevant `docs/chapters/CHAPTER_0X_COMPLETE.md` and exact source/validated Resource set;
- preserve approved scene purpose, protected lines/beats, pair progression, knowledge firewalls, geography, roster changes, combat handoffs, and affordable-2.5D staging;
- wire world triggers, presentation consumers, encounter transitions, hub services, and final assets without changing approved wording;
- update stable IDs or internal handles only through bounded, consumer-audited technical changes;
- run the relevant chapter continuity/source-parity validators and broader regression after meaningful changes.

A missing world map, trigger consumer, portrait asset, or presentation executor is **not evidence that the dialogue or canon is missing**.

## New-authoring workflow

For Chapter 4+ new scene work, use the chapter-level process proven earlier: one branch/PR per chapter or substantial narrative block, scene-level review/checkpointing, chapter continuity/voice/runtime review, then exact-head Godot + Android gating and one authority/archive checkpoint.

## No invention policy

When a required implementation detail is missing, use a clearly labeled placeholder only when the milestone permits it, isolate it in data/configuration, document the assumption, and do not present it as canon. Never invent permanent mechanics, dialogue, lore, characters, relationships, Card identities, Prime rules, or story outcomes merely to unblock coding.

## Proven-architecture protection

Do not casually replace or bypass accepted architecture:

- 2.5D world-space exploration on real 3D fields;
- authored dialogue with no player response system;
- stable-ID Resource-backed production dialogue with portrait registry indirection and structural validation;
- discrete-round combat with enemy action locking and Item / Defend / Speed resolution;
- deterministic automatic hostile retargeting;
- unlimited data-driven Standard Cards;
- directly controlled Prime replacement/suspension/return architecture where compatible with current Prime-state rules;
- versioned plain-data persistence separate from scene nodes;
- Android as a first-class build/test target.

Chapter 0's complete dialogue/Resource/continuity validation and Chapters 1–3 exact source-parity/continuity gates remain accepted regression baselines. If newer authority changes an accepted behavior, update code, documentation, and tests deliberately together.

## Chapter 0 compatibility boundary

The live S004/S005 Resource/test set still contains the old internal label `Broken Champion's Ward`. **v1.64 / Audit79** supersedes that as canon terminology: the phenomenon is only an incomplete green/gold protective response from the sealed Card, not a Prime/Last Sentinel activation or bearer confirmation.

Do not blindly rename just the Resource or just the validator. A bounded cleanup must change matched internal handles together and preserve the approved temporary S004→S005 protection behavior unless a separate balance decision changes it.

Some old stable IDs also retain retired historical geography strings such as `BORDERLANDS`. Stable IDs are implementation handles, not formal Realm authority. Current geography is **Edgelands / Diysereach / Southhold**. Renaming a stable ID requires an audited consumer migration; leaving the legacy string in an internal ID does not restore the retired geography term to canon.

## Critical geography boundary

Chapter 3 is **Caelora → Old City / Suppressed Archives → separate Cresthaven**. Never collapse Cresthaven into the Old City during implementation.

The post-Warden sequence is fixed: command-record room proves false-order assembly; Torren copies map-like routing geometry; party returns to Mirena; Mirena identifies Cresthaven as an abandoned Crown outpost; party stops overnight; S021 begins next morning with Mirena already establishing the headquarters.

## Current numerical/system corrections that override old technical material

- Absolute character level cap: **60**; Worldframe Depths remains specifically Level 50.
- Cards: **30 Standard + 12 Prime = 42 total**.
- Standard Cards are unlimited-use; four Standard slots per permanent character.
- Current Story Primes: Last Sentinel / Last Measure / Last Convergence / Last Scribe / Last Sanctuary / Last Erasure.
- Current Prime states are controlled by v1.64 / Audit79; old two-round Recovered, old First Champion naming, old 70/80/90 HP rules, and boss-form refresh rules are superseded.
- Current exact once-per-battle Prime scope and the other items explicitly listed OPEN in v1.64 must remain OPEN rather than being filled from old proof documents.

## Scope discipline

For each task identify the exact subsystem being changed, avoid unrelated refactors, preserve public interfaces unless intentionally changing them, add/update deterministic tests where practical, report temporary shortcuts, and distinguish production content from fixtures.
