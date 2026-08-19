# Diyse-Game

Clean Godot production repository for **Diyse**, an **HD-2D**, party-based, command-driven turn-based JRPG targeting Android.

This repository is the active implementation line. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source unless an explicit task authorizes named reuse.

## Current authority and phase

- Written whole-project authority: **Diyse: HD-2D JRPG Clean Active Complete Master Canon v1.73 / Audit88** (August 19, 2026).
- Audit88: **Chapters 0–4 HD-2D Conversion and Cost-Consolidation Closure**.
- Audit87 makes **HD-2D** the sole active presentation target; older active `2.5D` and `3D` presentation language is superseded.
- Chapters **0–4 are COMPLETE/CLOSED** at story/dialogue/gameplay authority level and have passed HD-2D Conversion Audit Pass 1 plus cross-chapter consistency/cost consolidation.
- Chapter 5 — **The Mountain Engine** — is the next inherited exact scene-production / HD-2D production-audit frontier unless the user explicitly redirects work.
- Exact visual masters remain controlling over derivative HD-2D sprites/portraits/cut-ins.
- The exact approved Yahtrea world map remains spatially authoritative and may not be reinterpreted by presentation conversion.

Controlling repository authority:

- `docs/ACTIVE_CANON.md`
- `docs/PRESENTATION_RULES.md`
- `docs/canon/AUDIT88_CHAPTERS_00_04_HD2D_CONVERSION_AND_COST_CONSOLIDATION_CLOSURE.md`
- `docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`
- `docs/IMPLEMENTATION_STATUS.md`

## Current HD-2D production baseline

- Field characters: approximately **80 px**.
- Battle characters: approximately **200 px**.
- Dialogue: large high-resolution portraits.
- Battle composition: up to four active party members staggered on the **left**, enemies on the **right**, open center action/VFX lane.
- Normal field staging: authored layered environments, bounded camera language, foreground/background/parallax depth and selective geometry.
- Random encounters remain the ordinary hostile-exploration layer where approved.
- Chapter 0 is the explicit tutorial exception: seven authored encounters, no normal random-encounter table.
- Android/APK remains the target.
- Target runtime: approximately **25 hours**.
- Absolute character level cap: **60**.
- Permanent commands: **Attack / Ability / Card / Item / Defend**.

## Production tier vocabulary

- C0 — Conversational
- C1 — Staged
- C2 — Dramatic
- C3 — Spectacle
- V1 — Common
- V2 — Face/class identity
- V3 — Named signature
- V4 — Prime/boss spectacle

In the completed early game, S022's first Last Sentinel manifestation is the first approved V4 event.

## Current chapter authority state

| Chapter | Authoring/canon | HD-2D conversion | Runtime dialogue status |
|---|---|---|---|
| Ch0 — The Broken Convoy | CLOSED | PASS / approved | COMPLETE / MERGED / historically validated |
| Ch1 — Brackenwall and the Wayfinder | CLOSED / line-complete repo source | PASS / approved | COMPLETE / exact source-parity + continuity validated |
| Ch2 — The Drowned Oath | CLOSED / line-complete repo source | PASS / approved | COMPLETE / exact source-parity + continuity validated |
| Ch3 — The Old City and Last Sentinel | CLOSED / line-complete corrected repo source | PASS / approved | COMPLETE / exact source-parity + continuity/Cresthaven validation |
| Ch4 — The Seventh Reaction | CLOSED / exact production source | PASS / approved | production conversion/static validation present where implemented; in-engine smoke remains separate QA |
| Ch5 — The Mountain Engine | next inherited production frontier | pending whole-game/Ch5+ audit | future implementation |

Chapter 3 geography remains a hard lock:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**.

S021 identifies/unlocks Last Sentinel without manifesting it. S022's Elder Briarhide encounter is the first verified modern Prime manifestation.

## Proven technical chain

**Step 7B.5 remains COMPLETE / PASS as historical technical evidence on real Android hardware**, and **Step 7B.6 remains COMPLETE / PASS** for the production dialogue Resource handoff.

Those proofs continue to protect accepted gameplay/runtime behavior where compatible with current authority, including:

- authored portrait dialogue with no player dialogue choices;
- discrete-round combat;
- maximum four active characters;
- unlimited data-driven Standard Cards;
- direct-control Prime replacement/suspension/return architecture;
- deterministic hostile retargeting;
- versioned save/load persistence;
- Android build/deployment viability.

Their old active 2.5D/real-3D art-direction statements are superseded by Audit87/Audit88 and must not be treated as current presentation authority.

Historical accepted checkpoints:

- pre-documentation 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`
- 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`
- Chapter 0 production merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`
- Chapter 1 dialogue Resource merge: `f1cd2cd9152e4b7ca7e63bea6469c5b326494120`
- Chapter 2 dialogue Resource merge: `29e7ced1e92d32e2a6a235a6efab2b8a320a36f6`
- Chapter 3 dialogue Resource merge: `5bda1b4641f7762ab07f6e0d98faff953daf5c2e`

## Completed Chapters 0–4 HD-2D conversion

The approved production record is:

`docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

It locks:

- regional reusable environment families rather than chapter-specific one-use megamaps;
- a common field/battle transition architecture;
- small battle-background families derived from field geography;
- one permanent party-left/enemy-right combat frame;
- reusable nonlethal battle-resolution presentation;
- modular Face/Card/Prime VFX;
- modular six-element VFX/environment technology;
- a reusable Prime manifestation pipeline;
- one evolving Cresthaven master hub;
- Android-conscious cost scaling;
- same-body vs genuine-new-form vs Prime-scale boss implementation categories.

The conversion is presentation/implementation authority only. It does not rewrite approved scenes.

## Baseline rules

- Engine: Godot 4.x production line / GDScript.
- Platform: Android, landscape.
- Presentation: **HD-2D**.
- Dialogue: fully authored; no player dialogue choices.
- Production dialogue: stable-ID `DiyseDialogueSceneDefinition` Resources with `DiyseDialoguePortraitRegistry` indirection.
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

For Chapters 0–4 follow-on implementation:

1. read the current chapter source/lock;
2. read the Audit88 HD-2D conversion record;
3. preserve exact approved wording/story/gameplay;
4. implement maps, presentation assets, battle backgrounds, world triggers, VFX, encounter transitions and hub states according to the approved HD-2D grammar;
5. run the relevant content/regression gates.

For new story/scene production, move to Chapter 5 rather than re-authoring completed Chapters 0–4 unless the user explicitly reopens them.

## Proof-content warning

Passing technical proof validates architecture and accepted behavior, **not** temporary prototype content. Graybox geometry, placeholder sprites/portraits, proof dialogue, `PROOF_SCHEMA`, proof enemies, `Proof Strike`, flat proof damage/rewards, proof flags/cues and debug UI remain non-canon replaceable fixtures.

Read `AGENTS.md`, `docs/ACTIVE_CANON.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/PRESENTATION_RULES.md`, `docs/chapters/README.md`, `docs/chapters/dialogue/README.md` and the relevant subsystem rules before implementation.