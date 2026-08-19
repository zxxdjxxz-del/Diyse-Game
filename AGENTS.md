# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code or production content, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/PRESENTATION_RULES.md`
4. `docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md` when touching Chapters 0–4 presentation/runtime implementation
5. `docs/chapters/README.md`, the relevant completed-chapter lock file and exact scene source under `docs/chapters/dialogue/`
6. the subsystem document relevant to the task
7. `docs/TECHNICAL_PROOF.md` only as compatible historical engineering evidence
8. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before dialogue Resource work

If a task conflicts with these files or a newer explicit user instruction, stop and flag the conflict. Do not silently reinterpret canon.

## Current authority state

- Whole-project written authority: **Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.73 / Audit88**.
- Date: **August 19, 2026**.
- Audit87 makes **HD-2D** the sole active presentation target; old active `2.5D`/`3D` presentation language is superseded.
- Chapters **0–4 are COMPLETE/CLOSED** at story/dialogue/gameplay authority level.
- Chapters **0–4 HD-2D Conversion Audit Pass 1 is COMPLETE / APPROVED**.
- Cross-chapter HD-2D consistency/cost consolidation is **PASS / GREEN**.
- Chapter 5 — **The Mountain Engine** — is the next inherited exact scene-production / HD-2D production-audit frontier unless explicitly redirected.
- Step 7B.5 remains an accepted historical Android technical regression baseline where compatible with current HD-2D authority.
- Step 7B.6 production authoring handoff remains COMPLETE / PASS.

Historical accepted implementation checkpoints:

- 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`
- 7B.6 production-handoff merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`
- Chapter 0 production merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`
- Chapter 1 dialogue Resource merge: `f1cd2cd9152e4b7ca7e63bea6469c5b326494120`
- Chapter 2 dialogue Resource merge: `29e7ced1e92d32e2a6a235a6efab2b8a320a36f6`
- Chapter 3 dialogue Resource merge: `5bda1b4641f7762ab07f6e0d98faff953daf5c2e`

## Completed Chapters 0–4 rule

Do **not** recover, re-author or re-audit Chapters 0–4 as though their story/dialogue were missing.

- Chapter 0: use validated Resource set plus later compatibility overlays.
- Chapter 1: use exact source under `docs/chapters/dialogue/chapter_01/` plus validated Resource set.
- Chapter 2: use exact source under `docs/chapters/dialogue/chapter_02/` plus validated Resource set.
- Chapter 3: use corrected exact source under `docs/chapters/dialogue/chapter_03/` plus validated Resource set.
- Chapter 4: use exact source under `docs/chapters/dialogue/chapter_04/`; runtime conversion/static validation status is recorded in `docs/IMPLEMENTATION_STATUS.md`.

For presentation/runtime implementation, use Audit88's conversion record. A bounded implementation correction may update IDs, Resource metadata, internal labels, cue support, triggers, maps, presentation consumers or staging feasibility without reopening approved wording, scene purpose, protected beats, pair progression, geography, knowledge firewall, party-state changes or outcomes.

## Critical presentation rule

Diyse is **HD-2D**.

Do not implement a retired “real 3D fields + 2D/2.5D characters” art direction merely because historical proof code/docs mention it.

Current production targets:

- field characters ~80 px;
- battle characters ~200 px;
- large high-resolution dialogue portraits;
- authored layered environments with background/midground/playable/foreground/atmosphere depth;
- bounded authored cameras and restrained parallax;
- selective geometry only where traversal/collision/occlusion needs it;
- party left / enemies right / open center combat frame;
- small reusable battle-background families derived from field geography;
- exact visual masters control all derivatives;
- exact Yahtrea world-map geography remains unchanged.

Official production tiers:

- C0 Conversational
- C1 Staged
- C2 Dramatic
- C3 Spectacle
- V1 Common
- V2 Face/class identity
- V3 Named signature
- V4 Prime/boss spectacle

## Affordable HD-2D behavior

If prose describes many micro-actions, simplify physical staging while preserving meaning.

Prefer:

- reusable stand/sit/walk/interact/cast/attack families;
- portrait/expression swaps;
- authored sprite turns/shifts;
- camera framing/pans/inserts/holds;
- ordinary reusable props;
- state-swapped doors, bridges, maps, machinery, damage and rooms;
- layered background NPC loops;
- audio to imply offscreen scale;
- modular Face/Card/Prime/elemental VFX;
- small reusable location battle-background families.

Avoid by default:

- physics destruction;
- fluid simulation;
- crowd AI/simulation;
- free-camera exploration;
- chain/cloth/hair simulation;
- bespoke body animation for every Ability;
- one unique arena per formation;
- six full environment/body pipelines for six elements;
- full-body second forms when a same-body state change is the actual mechanic.

## Battle presentation hard rules

- Discrete round-based combat, not realtime/timeline combat.
- Maximum active party: four.
- Permanent commands: **Attack / Ability / Card / Item / Defend**.
- Standard formation: legal active members staggered left; enemies right; center reserved for action/VFX.
- Undersized early parties are not recentered.
- Reserve characters are absent from the normal battle frame.
- Random encounters remain random encounters; do not replace them with visible roaming enemies without explicit canon revision.
- Chapter 0 remains the seven-authored-tutorial-encounter exception.
- Fixed encounters/bosses may use authored entrances but still resolve into the same core battle grammar.

## Boss/form implementation categories

Classify encounter transitions correctly:

1. **Same-body / same-HP escalation:** components/overlays/idle/lighting/behavior change; no unnecessary new body.
2. **Genuine new form:** new body/full HP only where canon actually defines a new combat problem, e.g. Sixfold Crucible Form II.
3. **Prime-scale entity:** use the reusable Prime presentation pipeline.

Do not add health bars, transformations, threshold attacks or Prime refreshes not present in canon.

## Prime presentation

S021 identifies/unlocks Last Sentinel without manifesting it. S022's Elder Briarhide fight is the first verified modern manifestation.

The reusable Prime presentation pipeline is:

command accepted → battlefield temporarily yields through authored camera/light → exact Prime manifestation → one legal action → impact → dismissal → normal battle presentation returns.

Do not convert Prime use into a detached prerendered movie that bypasses combat rules.

## Exact visual authority

Exact approved visual masters override incompatible prose or placeholder assets. Derivatives may simplify for output scale but must not redesign face, apparent age, silhouette, body proportions, weapon identity, palette or approved costume/armor language.

Audit86 specifically locks the current exact Cyanis visual master. The same exact-master principle applies project-wide.

## Chapter 0 compatibility boundary

The live S004/S005 Resource/test set still contains the old internal label `Broken Champion's Ward`. Current canon treats the phenomenon only as an incomplete green/gold protective response from the sealed Card, not Prime/Last Sentinel activation or bearer confirmation.

Do not rename only the Resource or only the validator. Any bounded cleanup must update matched internal handles together and preserve the approved temporary S004→S005 protection behavior unless separately revised.

Legacy stable IDs may retain retired geography strings such as `BORDERLANDS`. Stable IDs are implementation handles, not player-facing geography authority. Current formal geography is **Edgelands / Diysereach / Southhold**. Do not casually rename stable IDs without auditing all consumers.

## Chapter 3 geography and Prime chronology

Chapter 3 travel is:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**

Cresthaven is not a room, wing, chamber, district or renamed section inside the Old City.

The controlling S020→S021 sequence:

- post-Warden command-record room proves false-order assembly;
- Torren copies routing geometry;
- party returns to Mirena;
- Mirena identifies Cresthaven as an abandoned Crown outpost in Southhold;
- party stops overnight;
- S021 begins next morning with Mirena already establishing headquarters.

S021 identifies/unlocks Last Sentinel but does not manifest it. First verified modern Prime manifestation is S022.

## Chapter 4 hard production boundaries

- Start traveling permanents: Cyanis / Ilyra / Torren / Nimera.
- Maevra is not the default Chapter 4 traveling party member.
- Vaelira joins permanently during S022; roster reaches five; choose-four remains active.
- Elder Briarhide is a natural territorial animal, not corrupted/Ancient/Black Host.
- Elemental Hexarch is a living harmed researcher and resolves nonlethally.
- Seventh Reaction is not a seventh element.
- Sixfold Crucible Form I → Form II is a genuine two-form transition; Form II has fresh authored HP/MP; Prime availability does not refresh.
- Crown Prototype is one body / one HP bar / no transformation.
- Annex random encounter quantity is area-driven; do not hardcode a promised approximate count.

## Scene authoring workflow

Use `docs/SCENE_AUTHORING_STANDARD.md`.

For new exact scene work, begin with Chapter 5 unless the user explicitly redirects the task. Do not regenerate or rewrite validated/closed Chapter 0–4 text except through explicit canon revision.

## Hard system rules

- Fresh Godot/GDScript implementation; do not copy/port code from historical `zxxdjxxz-del/Diyse` unless explicitly authorized for named reuse.
- Dialogue is one authored continuity; no response wheels, tone selection, morality/affinity responses, persuasion trees or romance routes.
- Production dialogue uses stable-ID `DiyseDialogueSceneDefinition` Resources; never embed canon scene text or final portrait paths into generic engine code.
- Combat is discrete round based.
- Maximum active party four.
- Permanent commands Attack / Ability / Card / Item / Defend.
- MP is universal ordinary Ability resource; do not invent character-specific gauges.
- Standard Cards are unlimited-use and data-driven.
- Persistent game state remains versioned plain data separate from scene nodes.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, story outcomes or missing dialogue to fill gaps.
- Keep systems and authored content separate; prefer data-driven definitions.
- Do not optimize around placeholders in a way that blocks final exact assets.
- Do not change canon/specification documents as accidental side effects of code work.

## Current foundation corrections

- Absolute character level cap: **60**; Chapters 11–12 carry progression beyond 50; no Level 61+, prestige tier or postgame progression campaign.
- Worldframe Depths remains a **Level-50 optional-major challenge**.
- Cards: **30 Standard + 12 Prime = 42 total**.
- Permanent class pairs: Cyanis Crest Knight → Crest Magus; Ilyra Blue Warden → Vowblade; Torren War Archer → Routeweaver; Nimera Cardweaver → Sixfold Knight; Vaelira Green Arcanist → Prism Archer; Seyrik Ruin Vanguard → Ruin Reclaimer.
- Story Primes: Last Sentinel / Last Measure / Last Convergence / Last Scribe / Last Sanctuary / Last Erasure.
- Faces/colors: Might Ruby; Elements Emerald; Grace Blue; Resource Gold; Change Fuchsia; Ruin Purple.

## Engineering behavior

- Implement one bounded milestone at a time.
- Preserve deterministic behavior where combat rules require it.
- Add deterministic validation for pure logic/content contracts where practical.
- Keep platform-specific code isolated and Android first-class.
- Prefer simple readable GDScript over clever abstractions.
- Keep exploration, dialogue, combat, save/state, UI and content loading separable.
- Mark temporary shortcuts clearly; they are not canon.

## Accepted-proof regression rule

Steps 7B.5 and 7B.6 remain closed technical baselines. Chapters 0–3 exact dialogue Resource/continuity gates remain accepted; Chapter 4 exact authoring/static conversion authority remains closed where currently documented. Do not regress accepted exploration/dialogue/combat/Card/Prime/persistence behavior merely because later production is more complex.

Temporary proof fixtures remain replaceable and non-canon.