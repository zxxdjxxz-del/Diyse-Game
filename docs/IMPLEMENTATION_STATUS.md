# Diyse — Current Implementation Status

**Authority checkpoint:** v1.35 / Audit47  
**Step 7B.5:** COMPLETE / PASS on real Android hardware  
**Step 7B.6:** COMPLETE / PASS — production dialogue authoring handoff locked  
**Step 7C:** ACTIVE / AUTHORIZED August 8, 2026  
**Current Step 7C milestone:** Chapter 0 S001 — Opening  
**Active repository:** `zxxdjxxz-del/Diyse-Game`  
**Accepted 7B.5 gameplay baseline:** `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`  
**Accepted 7B.6 implementation merge:** `96c6bdc77f39c988f2185634b4e51546f2a0d76b`

## Proven technical chain

| Gate | Status | Accepted proof |
|---|---|---|
| 7B.5A | PASS | Clean Godot 2.5D field architecture, camera and collision |
| 7B.5B | PASS | Android touch movement, boundaries and repeatable APK pipeline |
| 7B.5C | PASS | Authored portrait dialogue, expressions, silent reactions, no choices, control return |
| 7B.5D | PASS | Four-character discrete-round combat and deterministic priority/tie rules |
| 7B.5E | PASS | Unlimited data-driven Standard Card path and automatic hostile retargeting |
| 7B.5F | PASS | Bearer-locked direct-control Prime replacement/suspension/return architecture |
| 7B.5G | PASS | Versioned plain-data save/load and persistence across full Android app close/relaunch |
| 7B.6 | PASS | Stable-ID dialogue scene Resources, portrait registry, authoring template, schema validation and Resource-to-runner integration |

## Accepted implementation behaviors

### Exploration / 2.5D

The active Godot line supports real 3D fields/depth/lighting/collision with stylized 2D/2.5D character presentation and Android touch movement. The proof visuals are replaceable fixtures, not final art direction.

### Dialogue

Generic authored dialogue can be world-triggered, display portraits/expressions, present silent reaction beats, lock exploration input and return control cleanly. No player response architecture exists or should be introduced.

Production dialogue has an accepted handoff contract:

- scene content is stored as `DiyseDialogueSceneDefinition` Resources;
- scene/beat/character/expression/trigger/completion IDs are stable semantic handles;
- portrait asset paths resolve through `DiyseDialoguePortraitRegistry` rather than living inside authored scenes;
- cue metadata is kept separate from spoken text and emitted for later staging/camera/movement consumers;
- the generic runner consumes Resource-backed scenes without character-specific script logic;
- forbidden choice/response/branch keys fail validation.

See `DIALOGUE_AUTHORING_SCHEMA.md`, `STEP_7C_AUTHORING_TEMPLATE.md` and `PRODUCTION_HANDOFF_7B6.md`.

### Combat

The accepted resolver uses discrete rounds, enemy action locking before player confirmation, Item priority, Defend priority, then Speed ordering with the current tie rules. Four permanent characters are active at maximum.

A queued player hostile action whose original enemy target is defeated before resolution automatically retargets to the next living enemy in encounter-slot order, wrapping if necessary. Only the target changes.

### Standard Cards

Standard Cards can be data-driven, unlimited-use and integrated with the ordinary resolver without charges, Essence, Card ranks or per-battle Standard-use counters.

### Prime Manifestations

Prime activation, pending state, party suspension, direct player control, Prime-only command selection, hostile targeting of the Prime, finite duration and party return are proven without replacing the ordinary round system.

### Persistence

Persistent state is kept separate from scene nodes and serialized as versioned plain data under Godot `user://`. Representative gameplay state survives a full Android app close/relaunch. Missing, malformed and unsupported-future-version saves fail safely.

## Non-canon technical fixtures

Do not preserve these as authored game content merely because they exist in the proof:

- graybox map/obstacle/chest geometry;
- placeholder Cyanis/Torren world sprites and portraits;
- disposable proof dialogue;
- `PROOF_SCHEMA` and its proof registry/cues;
- Raider proof enemies/stats;
- `Proof Strike`;
- temporary flat damage values;
- temporary 30 XP / 42 gold battle rewards and proof chest rewards;
- proof-specific flags/state labels;
- temporary button/debug HUD.

## Regression expectation

The automated tests accepted through Steps 7B.5 and 7B.6 are the project regression baseline. Production work should extend them rather than bypass or weaken them.

## Remaining production scope

The technical and handoff PASS does not mean the game is content-complete. Normal production still includes final visual/audio/UI work, final formulas, complete character kits/equipment/enemies/encounters, all 24 Standard Cards, all 12 Prime implementations, Chapters 0–12, Character-Life scenes, broader device/performance QA and release hardening.

## Narrative production

The dialogue study is complete, technical feasibility is proven, and the production scene-data contract is locked. **Step 7C was explicitly authorized by the user on August 8, 2026 and is now active.**

Work begins chronologically with Chapter 0 S001–S006, followed by C01 and C02 unless the user changes the order. A draft scene is not canon merely because it exists in a branch: each scene must pass canon/voice review and structural validation before approval/integration.