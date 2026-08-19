# Diyse — AI Engineering Rules

`AGENTS.md` is the root agent contract. This file expands the working method.

## Authority order for implementation work

1. New explicit user instruction for the current task.
2. **Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.73 / Audit88** and newer controlling project authority.
3. `docs/ACTIVE_CANON.md`, `docs/PRESENTATION_RULES.md`, `docs/IMPLEMENTATION_STATUS.md` and the relevant completed-chapter package under `docs/chapters/`.
4. `docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md` when touching Chapters 0–4 presentation/runtime implementation.
5. Compatible accepted technical annex/proof authority for exact system behavior only where it does not conflict with Audit88.
6. Compatible completed dialogue-study craft authority and exact production source material.
7. Relevant subsystem specification under `docs/`.
8. Existing production code and accepted regression tests interpreted through current authority.
9. Historical prototype/recovery material only when explicitly requested or explicitly inherited.

Do not use an older implementation, proof fixture, stale document, legacy identifier or superseded numeric table to override newer authority.

## Current phase rule

- Step 7B.5 technical feasibility remains COMPLETE / PASS as historical Android engineering evidence where compatible with current authority.
- Step 7B.6 production handoff remains COMPLETE / PASS.
- Chapters 0–4 are COMPLETE/CLOSED in story/dialogue/gameplay authority.
- Chapters 0–4 HD-2D Conversion Audit Pass 1 is COMPLETE / APPROVED.
- Cross-chapter HD-2D consistency/cost consolidation is PASS / GREEN.
- Chapter 5 — **The Mountain Engine** — is the next inherited exact scene-production / HD-2D production-audit frontier unless the user explicitly redirects work.

## HD-2D authority

Diyse's active presentation target is **HD-2D**.

Older active `2.5D` and `3D` language is superseded. Historical proof documents may remain unchanged where they serve as provenance, but engineering must not reintroduce their retired presentation assumptions.

Current production targets:

- ~80 px field characters;
- ~200 px battle characters;
- large high-resolution dialogue portraits;
- authored layered field environments;
- bounded cameras and restrained parallax;
- selective geometry for traversal/collision/occlusion only;
- four active party members staggered left / enemies right / open center battle lane;
- small reusable battle-background families derived from field geography;
- exact visual masters control derivatives;
- exact Yahtrea world-map geography remains controlling.

## Completed-chapter implementation workflow

For follow-on implementation in Chapters 0–4:

- start from the relevant chapter exact source/lock and current validated Resource set where one exists;
- read the Audit88 HD-2D conversion record;
- preserve approved scene purpose, protected lines/beats, pair progression, knowledge firewalls, geography, roster changes, combat handoffs and outcomes;
- implement maps, presentation consumers, encounter transitions, hub states, final assets and VFX according to Audit88;
- update stable IDs/internal handles only through bounded consumer-audited changes;
- run relevant chapter source-parity/continuity validators and broader regression after meaningful changes.

A missing world map, trigger consumer, portrait asset, battle background or presentation executor is **not evidence that dialogue/canon is missing**.

## New-authoring workflow

For Chapter 5+ new scene work, use the chapter-level process in `docs/SCENE_AUTHORING_STANDARD.md`: one branch/PR per chapter or substantial narrative block, scene-level review/checkpointing, whole-chapter continuity/voice/pacing review, then appropriate Godot/Android gating and authority/archive checkpoint.

## No invention policy

When required implementation detail is missing, use a clearly labeled placeholder only when the milestone permits it, isolate it in data/configuration, document the assumption and do not present it as canon.

Never invent permanent mechanics, dialogue, lore, characters, relationships, Card identities, Prime rules, story outcomes or presentation lore merely to unblock coding.

## Proven-architecture protection

Do not casually replace accepted behavior:

- authored dialogue with no player response system;
- stable-ID Resource-backed dialogue with portrait registry indirection and structural validation;
- discrete-round combat with enemy action locking and Item / Defend / Speed resolution;
- deterministic automatic hostile retargeting;
- unlimited data-driven Standard Cards;
- directly controlled Prime replacement/suspension/return architecture where compatible with current Prime rules;
- versioned plain-data persistence separate from scene nodes;
- Android as a first-class build/test target.

Do **not** protect retired presentation assumptions merely because they existed in the old proof. Current art/presentation must follow Audit87/Audit88 HD-2D grammar.

## HD-2D cost discipline

Prefer reusable authored composition over simulation.

Use:

- regional environment kits;
- small battle-background families;
- reusable body animation families;
- portrait acting;
- prop/environment state swaps;
- selective background loops;
- audio to imply offscreen scale;
- modular Face/Card/Prime and elemental VFX;
- one evolving Cresthaven master hub;
- one common transition architecture;
- one reusable nonlethal battle-resolution path.

Avoid by default:

- fully modeled cities;
- seamless giant dungeons only to imply scale;
- free-camera field navigation;
- fluid/crowd/destruction/chain/cloth/hair simulation;
- one bespoke battle arena per formation;
- one bespoke actor animation per Ability;
- six complete independent pipelines for six elements;
- new full boss bodies for same-body/same-HP threshold changes.

## Production tier discipline

Use:

- C0 Conversational
- C1 Staged
- C2 Dramatic
- C3 Spectacle
- V1 Common
- V2 Face/class identity
- V3 Named signature
- V4 Prime/boss spectacle

Most scenes are C0–C1. C3/V4 are rare. Preserve late-game escalation room.

## Random encounters

Random encounters remain the ordinary hostile-exploration layer where canon supports them.

- Chapter 0 remains the seven-authored-tutorial-encounter exception.
- Chapter 1 onward uses the campaign-standard fast random encounter transition in approved hostile areas.
- Safe/story pockets suppress triggering.
- Do not replace random encounters with roaming visible enemies without explicit canon revision.
- Do not hardcode expected encounter counts in scene authority; derive testing expectations from actual geometry and rates.

## Nonlethal presentation

Where authored outcomes are restraint, retreat, stabilization or lawful de-escalation, use the reusable nonlethal resolution grammar rather than generic death/loot/victory presentation.

Examples in completed Chapters 0–4 include Briarhide outcomes, Caelora authority encounters, Elder Briarhide and Elemental Hexarch.

## Boss/form classification

Before implementing a threshold, identify the canon category:

1. **Same-body / same-HP escalation** — state/component/overlay/lighting/idle changes only.
2. **Genuine new form** — fresh body/HP only where canon defines a genuinely new combat problem, as with Sixfold Crucible Form II.
3. **Prime-scale entity** — use the reusable Prime manifestation pipeline.

Never add an HP bar, transform, threshold action or Prime refresh that canon does not define.

## Prime chronology / presentation

- S021 identifies/unlocks Last Sentinel without manifestation.
- S022 Elder Briarhide is the first verified modern Prime manifestation.
- Optional content may not create an earlier manifestation.

Technical presentation:

command accepted → authored light/camera yield → exact Prime manifestation → one legal action → impact → dismissal → normal battle frame returns.

Do not turn Prime use into a detached cinematic that bypasses legal combat resolution.

## Chapter 0 compatibility boundary

The live S004/S005 Resource/test set may still contain the old internal label `Broken Champion's Ward`. Current canon treats the event only as an incomplete green/gold protective Card response, not Prime/Last Sentinel activation or bearer confirmation.

A bounded cleanup must update matched internal handles together and preserve approved behavior unless a separate balance decision changes it.

Legacy stable IDs may retain retired historical geography strings. Stable IDs are implementation handles, not player-facing geography authority. Current formal geography is **Edgelands / Diysereach / Southhold**.

## Critical geography boundary

Chapter 3 is:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**.

Never collapse Cresthaven into the Old City.

The post-Warden sequence is fixed: command-record room proves false-order assembly; Torren copies routing geometry; party returns to Mirena; Mirena identifies Cresthaven; overnight stop; S021 next morning with Mirena already establishing headquarters.

## Current numerical/system corrections

- Absolute character level cap: **60**; Worldframe Depths remains Level 50.
- Cards: **30 Standard + 12 Prime = 42 total**.
- Standard Cards are unlimited-use.
- Permanent commands: Attack / Ability / Card / Item / Defend.
- Current Story Primes: Last Sentinel / Last Measure / Last Convergence / Last Scribe / Last Sanctuary / Last Erasure.
- Faces/colors: Might Ruby; Elements Emerald; Grace Blue; Resource Gold; Change Fuchsia; Ruin Purple.

## Scope discipline

For each task:

- identify the exact subsystem being changed;
- avoid unrelated refactors;
- preserve public interfaces unless intentionally changing them;
- add/update deterministic tests where practical;
- report temporary shortcuts;
- distinguish production content from fixtures;
- distinguish canon closure, HD-2D conversion authority and runtime implementation status.