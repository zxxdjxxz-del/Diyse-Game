# Diyse-Game

Clean Godot production repository for **Diyse**, a 2.5D, party-based, command-driven turn-based JRPG targeting Android.

This repository is the active implementation line. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source unless an explicit task authorizes a named reuse.

## Current authority and phase

- Written whole-project authority: **Diyse Clean Active Complete Master Canon v1.64 / Audit79** (August 18, 2026).
- Chapters **0–3 are COMPLETE/CLOSED** at story, dialogue, continuity, relationship, and affordable-2.5D production-authority level.
- Chapter 0 is also complete/merged as validated Godot production Resources at `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`, subject to later canon compatibility overlays.
- Chapters 1–3 now have **line-complete approved repository dialogue sources** under `docs/chapters/dialogue/`, but still require Resource conversion/implementation validation. That work must translate the approved chapters without re-authoring them.
- Chapter 4 — **The Seventh Reaction** — is the next exact scene-level authoring frontier.
- Completed Chapter 0–3 repository authority packages live in `docs/chapters/`; exact Chapters 1–3 scene wording lives in `docs/chapters/dialogue/`.

**Step 7B.5 is COMPLETE / PASS on real Android hardware.** The clean Godot architecture proved 2.5D exploration, authored portrait dialogue, discrete-round combat, unlimited data-driven Standard Cards, direct-control Prime replacement, deterministic hostile retargeting, and versioned save/load persistence across app close/relaunch.

**Step 7B.6 is COMPLETE / PASS.** Production dialogue uses a stable-ID Resource contract, portrait-registry indirection, schema validation, generic Resource-to-DialogueRunner integration, and the Step 7C authoring template. Accepted 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.

Accepted pre-documentation 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1b4d877c22`.

## Current chapter implementation state

| Chapter | Authoring/canon | Godot Resource integration |
|---|---|---|
| Ch0 — The Broken Convoy | CLOSED | COMPLETE / MERGED / historically validated |
| Ch1 — Brackenwall and the Wayfinder | CLOSED / line-complete repo source | pending conversion/validation |
| Ch2 — The Drowned Oath | CLOSED / line-complete repo source | pending conversion/validation |
| Ch3 — The Old City and Last Sentinel | CLOSED / line-complete corrected repo source | pending conversion/validation |
| Ch4 — The Seventh Reaction | next authoring frontier | future |

Chapter 3 geography is a hard lock: **Caelora → Old City / Suppressed Archives → separate Cresthaven**. The corrected S020→S021 handoff proves the false order's assembly in the post-Warden command room, has Torren copy a routing map, returns the party to Mirena, identifies Cresthaven as an abandoned Crown outpost in Southhold, and begins S021 the next morning with Mirena already establishing the site as the party's working headquarters.

## Chapter 0 compatibility note

The live S004/S005 Resources still contain the historical internal implementation label `Broken Champion's Ward`. Current canon treats the same early phenomenon only as an **incomplete green/gold protective response from the sealed Card**, not a Prime/Last Sentinel activation or bearer confirmation. The old label is not player-facing canon. A later bounded Resource+validator cleanup may neutralize those internal names without rewriting Chapter 0 dialogue or silently changing the approved temporary protection behavior.

## Baseline rules

- Engine line: Godot 4.7.x stable; accepted proof target Godot 4.7.1.
- Language: GDScript.
- Platform target: Android, landscape.
- Presentation: 2.5D — 3D environments/depth/lighting/traversal with stylized 2D/2.5D character presentation and illustrated portraits where appropriate.
- Dialogue: fully authored; no player dialogue choices.
- Production dialogue: stable-ID `DiyseDialogueSceneDefinition` Resources with `DiyseDialoguePortraitRegistry` asset indirection.
- Combat: discrete round-based command combat.
- Maximum active party: four.
- Permanent commands: Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource; no character-specific combat gauges.
- Absolute character level cap: **60**; no Level 61+ or prestige tier.
- Worldframe Depths remains a Level-50 optional-major challenge.
- Cards: **30 Standard + 12 Prime**.
- Standard Cards are unlimited-use.
- Story Primes: Last Sentinel / Last Measure / Last Convergence / Last Scribe / Last Sanctuary / Last Erasure.
- If a queued player hostile action's original target is defeated before resolution, use the accepted encounter-slot retarget behavior unless an authored effect explicitly overrides it.
- Keep authored content data-driven where practical and never invent mechanics/canon to make implementation easier.

## Production workflow

For Chapters 1–3, start from the relevant `docs/chapters/CHAPTER_0X_COMPLETE.md` implementation lock/index and the exact scene file under `docs/chapters/dialogue/`. Convert the closed material into the existing dialogue Resource schema. Resource implementation can make bounded technical/staging fixes, but it must preserve exact approved wording, protected beats, pair progression, knowledge firewalls, party-state changes, geography, and scene outcomes.

For new dialogue authoring, begin with Chapter 4 rather than repeating Chapters 1–3.

## Proof-content warning

Passing technical proof validates architecture and accepted behavior, **not** temporary prototype content. Graybox geometry, placeholder sprites/portraits, proof dialogue, `PROOF_SCHEMA`, proof enemies, `Proof Strike`, flat proof damage/rewards, proof flags/cues, and debug UI remain non-canon replaceable fixtures.

Read `AGENTS.md`, `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/chapters/README.md`, `docs/chapters/dialogue/README.md`, `docs/DIALOGUE_AUTHORING_SCHEMA.md`, `docs/STEP_7C_AUTHORING_TEMPLATE.md`, and the relevant subsystem rules before implementation.
