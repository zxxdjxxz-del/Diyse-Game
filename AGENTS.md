# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code or production content, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/chapters/README.md` and the completed chapter file relevant to the task
4. the subsystem document relevant to the task
5. `docs/TECHNICAL_PROOF.md` when the task touches architecture proven in Step 7B.5
6. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before dialogue Resource work

If a task conflicts with these files or with a newer explicit user instruction, stop and flag the conflict. Do not silently reinterpret canon.

## Current authority state

- Whole-project written authority: **Diyse Clean Active Complete Master Canon v1.60 / Audit75**.
- Date: August 17, 2026.
- Chapters **0, 1, 2, and 3 are COMPLETE/CLOSED** at story, dialogue, continuity, relationship, and affordable-2.5D production-authority level.
- Chapter 0 exact Resource/cue wording remains the merged Resource set at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5` where compatible with later canon.
- Chapters 1–3 are closed authoring authority but are **not yet fully converted/validated as production `.tres` Resources in this repository**. Translating them into the accepted schema is implementation work, not a dialogue rewrite.
- Chapter 4 — **The Seventh Reaction** — is the next exact scene-level authoring frontier.
- Step 7B.5 technical feasibility: COMPLETE / PASS on real Android hardware.
- Step 7B.6 production authoring handoff: COMPLETE / PASS.
- Accepted 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`.
- Accepted 7B.6 production-handoff implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

## Completed early-chapter rule

Do **not** repeatedly recover, re-author, or re-audit Chapters 0–3 as if their dialogue were missing. Use the closed authority packages in `docs/chapters/`.

A bounded implementation correction may update IDs, Resource metadata, internal labels, cue support, or staging feasibility without reopening the approved scene purpose, protected lines/beats, pair progression, geography, or knowledge firewall.

Chapter 0 has one known later-canon compatibility issue: the live validated S004/S005 Resources still contain the historical internal label `Broken Champion's Ward` and related old Champion/Prime-negative implementation wording. Current canon treats that phenomenon only as an incomplete green/gold protective response from the sealed Card. The old label is not player-facing canon. Any cleanup must preserve the already-approved S004→S005 temporary protection behavior unless a separate balance change revises it.

## Critical Chapter 3 geography

Chapter 3 travel is:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**

Cresthaven is not a room, wing, chamber, or district inside the Old City. S021 and H04 occur at the separate Cresthaven site.

## Step 7C / dialogue workflow

Use the chapter-level workflow proven by Chapter 0:

- one production branch/PR per chapter or comparable substantial narrative block;
- review/checkpoint implementation against the already-approved scene authority;
- one chapter tracker rather than a new issue/PR for every scene;
- scene-specific validation plus a whole-chapter continuity/repetition/voice/runtime pass;
- full Godot and Android regression at the chapter checkpoint, or earlier only when engine/schema/platform behavior changes;
- one authority/archive checkpoint after the chapter/substantial milestone is implemented.

For Chapters 1–3, **do not seek new prose approval merely because Resource conversion is pending**. Preserve the closed chapter packages.

## Hard rules

- This is a fresh Godot/GDScript implementation.
- Do not copy/port code from the older `zxxdjxxz-del/Diyse` repository unless explicitly authorized for named reuse.
- Diyse is 2.5D: 3D environments/depth/lighting/traversal + stylized 2D/2.5D character performance and portraits.
- Dialogue is one authored continuity. No dialogue wheels, response menus, tone selection, morality/affinity responses, persuasion trees, or romance routes.
- Production dialogue uses stable-ID `DiyseDialogueSceneDefinition` Resources. Never embed canon scene text or portrait paths into generic engine code.
- Combat is discrete round-based command combat, not real-time/timeline combat.
- Maximum active party: four.
- Permanent battle commands: Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource. Do not invent character-specific gauges.
- Standard Cards are unlimited-use and data-driven.
- Prime Manifestations use the accepted directly controlled replacement/suspension architecture.
- Persistent game state remains versioned plain data separate from scene nodes.
- Do not invent mechanics, terminology, characters, Cards, classes, resources, story outcomes, or missing dialogue to fill gaps.
- Keep systems and authored content separate; prefer data-driven definitions.
- Do not optimize around placeholder assets in a way that blocks final assets.
- Do not change canon/specification documents as an accidental side effect of code work.

## Current foundation corrections implementation must respect

- Absolute character level cap: **60**. Chapters 11–12 carry progression beyond 50; no Level 61+, prestige tier, or postgame progression campaign.
- Worldframe Depths remains specifically a **Level-50 optional-major challenge**.
- Standard Cards: **30** total; Prime Cards: **12** total.
- Permanent class pairs: Cyanis Crest Knight → Crest Magus; Ilyra Blue Warden → Vowblade; Torren War Archer → Routeweaver; Nimera Cardweaver → Sixfold Knight; Vaelira Green Arcanist → Prism Archer; Seyrik Ruin Vanguard → Ruin Reclaimer.
- Story Primes: Last Sentinel / Last Measure / Last Convergence / Last Scribe / Last Sanctuary / Last Erasure.
- Faces/colors: Might Ruby; Elements Emerald; Grace Blue; Resource Gold; Change Fuchsia; Ruin Purple.

## Affordable 2.5D behavior

If a scene requires unique animation only because prose describes many micro-actions, simplify the physical staging and preserve the dialogue/meaning. Prefer reusable poses, portraits, props, camera inserts, authored environment states, VFX, layered crowds, and silence. Do not add physics destruction, fluid simulation, crowd AI, or bespoke actor-body mimicry when prepared states can communicate the same result.

## Engineering behavior

- Implement one bounded milestone at a time.
- Preserve deterministic behavior where combat rules require it.
- Add deterministic validation for pure logic/content contracts where practical.
- Keep platform-specific code isolated and Android first-class.
- Prefer simple readable GDScript over clever abstractions.
- Keep exploration, dialogue, combat, save/state, UI, and content loading separable.
- Mark temporary shortcuts clearly; they are not canon.

## Accepted-proof regression rule

Steps 7B.5 and 7B.6 are closed. Chapter 0's complete Resource/continuity gate is an accepted production regression baseline. Do not regress the proven exploration/dialogue/combat/Card/Prime/persistence architecture or production dialogue Resource contract merely because later chapters are more complex.

Temporary proof fixtures remain replaceable and non-canon.