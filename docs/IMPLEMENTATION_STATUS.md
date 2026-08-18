# Diyse — Current Implementation Status

**Written authority checkpoint:** v1.64 / Audit79  
**Step 7B.5:** COMPLETE / PASS on real Android hardware  
**Step 7B.6:** COMPLETE / PASS — production dialogue authoring handoff locked  
**Story/dialogue production authority:** Chapters 0–3 COMPLETE/CLOSED  
**Repository authoring source:** Chapters 1–3 line-complete under `docs/chapters/dialogue/`  
**Runtime Resource implementation:** Chapters 0–3 complete/validated  
**Closed-chapter dialogue Resource frontier:** NONE for Chapters 0–3  
**Next exact scene-authoring frontier:** Chapter 4 — The Seventh Reaction  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## The important distinction

The repository has distinct completion states and they must not be conflated:

1. **Authoring/canon closure:** Chapters 0, 1, 2, and 3 are complete at story, dialogue, continuity, relationship, knowledge-firewall, and affordable-2.5D production-authority level under v1.64 / Audit79.
2. **Repository line-complete source:** Chapters 1–3 have exact approved scene-level Markdown sources under `docs/chapters/dialogue/`.
3. **Runtime dialogue Resource integration:** Chapters 0, 1, 2, and 3 now have full approved scene sets implemented as validated `DiyseDialogueSceneDefinition` `.tres` Resources.

Chapters 1–3 were translated from their exact locked Markdown sources without re-authoring. Their permanent validators enforce exact spoken source parity and whole-chapter continuity/final-version locks.

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
| 7B.6 | PASS | Stable-ID dialogue Resources, portrait registry, authoring template, schema validation and Resource-to-runner integration |
| Step 7C Chapter 0 | PASS / MERGED | S001–S006 + C01/C02 approved and integrated; chapter continuity + Godot + Android gate passed |
| Step 7C Chapter 1 dialogue Resource checkpoint | PASS / MERGED | S007–S011 + C03–C05 compiled from exact Audit79 source; schema/source-parity + chapter continuity gate passed |
| Step 7C Chapter 2 dialogue Resource checkpoint | PASS / MERGED | S012–S016 + C06/C07 compiled from exact Audit78 source; exact source-parity + chapter continuity gate passed |
| Step 7C Chapter 3 dialogue Resource checkpoint | PASS | S017–S021 + H01–H04 compiled from corrected Audit77/v1.64 source; exact source-parity + Chapter 3 continuity/Cresthaven gate passed |

Accepted pre-documentation 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`.  
Accepted 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`.  
Accepted Chapter 0 production merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`.  
Accepted Chapter 1 dialogue Resource merge: `f1cd2cd9152e4b7ca7e63bea6469c5b326494120`.  
Accepted Chapter 2 dialogue Resource merge: `29e7ced1e92d32e2a6a235a6efab2b8a320a36f6`.

## Chapter 0 runtime checkpoint

Live Resource set:
- S001 Opening
- S002 Wreck Field exploration
- S003 Evacuation Relay decision
- S004 Field Triage Camp revelation
- S005 Confrontation
- S006 Aftermath
- C01 The Fire Is Too Close
- C02 Food After Triage

Final historical Chapter 0 validation:
- Godot Smoke Validation run `31296623423`: success.
- Android APK Proof run `31296623417`: success.
- Final accepted PR head `87157f9dae359f0b72a6ec9f5a1956d2056671cb`.
- Merge `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`.
- Android artifact ID `9033158865`.

### Chapter 0 later-canon compatibility cleanup

The live S004/S005 Resource metadata/validator still contains the historical internal label **`Broken Champion's Ward`** and related older Champion/Prime-negative flags.

Current canon interpretation:
- incomplete green/gold **protective Card response**;
- not Prime activation;
- no bearer/Last Sentinel confirmation;
- no voice/warrior/manifestation;
- old internal Champion naming is not player-facing canon.

This does **not** invalidate the Chapter 0 merge. A future bounded implementation patch should neutralize those internal names in the Resource + matching validators together while preserving the already-approved temporary S004→S005 protection behavior unless balance authority separately revises it.

## Chapter 1 dialogue Resource checkpoint

Closed set: **S007–S011 + C03–C05**.  
Exact source: `docs/chapters/dialogue/chapter_01/`.  
Production Resources: `game/content/dialogue/chapter_01/`.

Deterministic generation/validation:
- `tools/dialogue/compile_chapter_01.py` reproduces the Resource translation from the controlling Markdown.
- `tests/dialogue/validate_chapter_01_resources.gd` validates schema/metadata and every spoken speaker/text pair against source in exact order.
- `tests/dialogue/validate_chapter_01_continuity.gd` validates Maevra guest addition, Torren permanent addition, S011 handoffs, C03–C05 gates, knowledge firewall, Audit79 C04 wording, Torren's smoke/fire staging, and Harth/Solmar progression.
- Both validators are part of permanent Godot Smoke Validation.

Audit79 exact C04 remains controlling: **“Old whore.” / “Bitch.”** The older `Whore/Shore` recovery reconstruction is superseded.

## Chapter 2 dialogue Resource checkpoint

Closed set: **S012–S016 + C06/C07**.  
Exact source: `docs/chapters/dialogue/chapter_02/`.  
Production Resources: `game/content/dialogue/chapter_02/`.

Deterministic generation/validation:
- `tools/dialogue/compile_chapter_02.py` reproduces the Resource translation from the controlling Audit78 Markdown.
- `tests/dialogue/validate_chapter_02_resources.gd` validates schema/metadata and every spoken speaker/text pair against source in exact order, including the standalone/offscreen prisoner line and C06 simultaneous Ilyra/Torren line.
- `tests/dialogue/validate_chapter_02_continuity.gd` validates water-safety wording, thirty-one-transfers meaning, completed-action Memory Scribe behavior, prisoner agency, the sole `Torren!`→`Harth.` breach, Rhazek's Chapter 2 same-bar limit/withdrawal, S016's single mandatory Hold the Junction encounter, final-extraction no-combat threshold, Hunt #2 handoff, knowledge firewall, and C06/C07 locks.
- Both validators are part of permanent Godot Smoke Validation.

Audit78 C07 Rewrite Draft 2 remains controlling: **wet sleeves**, no dream disclosure, Torren's late-night weed use treated as ordinary/non-impairing, lit from existing coals, **no modern lighter**.

## Chapter 3 dialogue Resource checkpoint

Closed set: **S017–S021 + H01–H04**.  
Exact source: `docs/chapters/dialogue/chapter_03/`.  
Production Resources: `game/content/dialogue/chapter_03/`.

The Resource set contains:
- S017, S018, S019, S020, S021
- H01, H02, H03, H04
- Chapter 3 dialogue registry

Deterministic generation/validation:
- `tools/dialogue/compile_chapter_03.py` reproduces the Resource translation from the controlling corrected Audit77/v1.64 Markdown.
- `tests/dialogue/validate_chapter_03_resources.gd` validates schema/metadata and every spoken speaker/text pair against source in exact order.
- `tests/dialogue/validate_chapter_03_continuity.gd` validates containment/order-chain logic, exactly two S018 nonlethal authority encounters, Nimera permanent recruitment + choose-four, Warden one-bar/two-state behavior, exact Last Sentinel output, no S020 Prime/Might identification, the corrected S020→S021 Cresthaven sequence, Last Sentinel recovery without manifestation, H01–H04 relationship/availability locks, and separate geography.
- Both validators are part of permanent Godot Smoke Validation.

Hard geography: **Caelora → Old City / Suppressed Archives → separate Cresthaven**.

Corrected end-state implementation sequence:
- post-Warden command-record room proves how the false order was assembled from separate authentic inputs;
- Torren copies a map-like routing display;
- the party returns to Mirena with evidence + map;
- Mirena identifies **Cresthaven as an abandoned Crown outpost in Southhold** and dispatches staff/support;
- the party stops for the night;
- S021 starts the next morning with Mirena already at Cresthaven establishing it as the party's working headquarters while the investigation continues.

H01/H02/H03 preserve their approved earlier **eligibility** states but require actual Cresthaven access before playback. H04 remains post-S021 only.

S021 unlocks Last Sentinel as Recovered/usable but does not manifest it. The first later real-battle use remains the first verified modern Prime manifestation.

These dialogue Resource checkpoints do **not** mean every exploration map, encounter consumer, world trigger, final portrait asset, hub service, or presentation executor for Chapters 1–3 is complete. Those remain separate implementation work where not already present.

## Accepted implementation behaviors

### Exploration / 2.5D
Real 3D fields/depth/lighting/collision + stylized 2D/2.5D character presentation and Android movement remain the accepted architecture. Use reusable poses, portraits, props, camera inserts, prepared environment states, layered crowds, and VFX rather than bespoke physics/simulation when implementing the completed scenes.

### Dialogue
Production dialogue uses stable semantic IDs, `DiyseDialogueSceneDefinition` Resources, `DiyseDialoguePortraitRegistry`, cue metadata separate from text, generic runner integration, and schema rejection of choice/response/branch fields.

### Combat
Discrete rounds; enemy action locking before unconfirmed player commands; Item priority; Defend priority; then effective Speed with deterministic tie rules. Maximum four active. Hostile queued actions preserve the accepted automatic retarget behavior.

### Standard Cards
Current canon: **30 Standard Cards**, unlimited-use and data-driven; no charges/Essence/ranks/per-battle Standard counter.

### Prime Manifestations
Current canon: **12 Prime Cards**. Direct-control replacement/suspension/return architecture remains proven. S021 unlocks Last Sentinel without manifesting it; first actual post-S021 battle use is the first verified modern Prime manifestation.

### Persistence
Persistent state remains separate from scene nodes and serializes as versioned plain data. Existing Android close/relaunch proof remains accepted.

## Current progression corrections relevant to implementation

- Absolute character level cap: **60**.
- Chapters 11–12 extend progression beyond Level 50 toward 60.
- Worldframe Depths remains a Level-50 optional-major challenge.
- No Level 61+, prestige tier, or new equipment tier above Legacy.
- Existing Mastery schedule through Level 50 remains unchanged unless separately revised.

## Production workflow from here

For **Chapters 1–3 follow-on implementation**, treat the validated Resource sets as the dialogue baseline; wire world triggers, presentation assets, encounter transitions, Cresthaven access/services, and other consumers without changing exact wording.

For **new exact scene authoring**, begin at Chapter 4 — The Seventh Reaction, not Chapters 0–3.

## Non-canon technical fixtures

Graybox maps, placeholder sprites/portraits, disposable proof dialogue, `PROOF_SCHEMA`, Raider proof enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof flags/state and debug UI remain replaceable non-canon fixtures.
