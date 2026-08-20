# Diyse — Current Implementation Status

**Written authority checkpoint:** v1.73 / Audit88  
**Presentation target:** HD-2D  
**Step 7B.5:** COMPLETE / historical technical PASS on real Android hardware, interpreted through current HD-2D authority  
**Step 7B.6:** COMPLETE / PASS — production dialogue authoring handoff locked  
**Story/dialogue production authority:** Chapters 0–4 COMPLETE/CLOSED  
**HD-2D Conversion Audit Pass 1:** Chapters 0–4 COMPLETE / APPROVED  
**Cross-chapter HD-2D consistency/cost consolidation:** COMPLETE / PASS / GREEN  
**HD-2D runtime foundation:** IMPLEMENTED  
**Chapters 0–4 HD-2D presentation sidecars/environment-state hookup:** IMPLEMENTED at code/resource layer  
**Final HD-2D visual asset/map replacement:** NOT YET IMPLEMENTED  
**Ordinary enemy roster and Elite placement:** OPEN / intentionally not encoded by this pass  
**Next inherited production-audit / scene-production frontier:** Chapter 5 — The Mountain Engine  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Completion states must remain separate

The repository uses distinct completion states. Do not conflate them.

1. **Authoring/canon closure:** Chapters 0–4 have approved story, dialogue, continuity, relationship, gameplay and production authority.
2. **HD-2D conversion authority closure:** Audit88 defines how completed Chapters 0–4 are staged/implemented in the active HD-2D grammar without rewriting them.
3. **HD-2D runtime foundation:** reusable reference composition, party/enemy battle anchors, field/battle scale helpers, authored environment-state Resources, presentation sidecars, Prime visual suspension/return hooks, Android decorative quality scaling and presentation validation are implemented.
4. **Chapter presentation hookup:** Chapters 0–4 have HD-2D scene-presentation sidecars and authored environment-state Resources at the code/resource layer. These sidecars do not contain final art and do not replace the closed dialogue Resources.
5. **Repository line-complete source:** Chapters 1–4 have exact approved scene-level Markdown under `docs/chapters/dialogue/`.
6. **Runtime dialogue Resource integration:** Chapters 0–3 have validated production `.tres` scene sets. Chapter 4 has exact production dialogue Resources/static validation present; its presentation sidecars are a separate layer.
7. **Final visual implementation:** final maps/environment art, ~80 px field sprites, ~200 px battle sprites, final portraits, final battle backgrounds, final VFX, final world/encounter consumers and final hub visuals remain production work where not already present.
8. **Enemy/Elite placement:** final ordinary-enemy roster/compositions and Elite placement remain open. This HD-2D runtime pass deliberately does not assign them.

A missing final visual asset or consumer is not evidence that approved dialogue/canon is missing. Likewise, a presentation sidecar describing `random_allowed`, `fixed_authored` or `mixed` encounter **mode** is not a final ordinary-enemy or Elite assignment.

## Runtime-conversion implementation checkpoint

The actual code-side HD-2D conversion has begun and is no longer documentation-only.

### Shared runtime foundation

Implemented under `game/presentation/`:

- `hd2d_runtime.gd`
  - 1920×1080 reference composition;
  - approximately 80 px field-character target helper;
  - approximately 200 px battle-character target helper;
  - permanent four-slot staggered party-left anchors;
  - generic enemy-right anchors;
  - protected center action lane;
  - C0–C3 / V1–V4 validation;
  - Android decorative quality profiles.
- `battle_presentation_controller.gd`
  - binds placeholder or final party/enemy `Node2D` visuals to the permanent battle anchors;
  - supports temporary Prime visual suspension/return without changing combat legality.
- `environment_state_definition.gd`
  - authored persistent environment states such as BASE / DAMAGED / CLEARED / OPEN / CLOSED / ACTIVE / INACTIVE / POST_BOSS / POST_STORY plus location-specific authored states.
- `encounter_presentation_definition.gd`
  - generic presentation categories and nonlethal/form-mode hooks;
  - intentionally does **not** own enemy IDs, Elite IDs, chapter placement, location placement, encounter tables, final stats or final visuals.
- `scene_presentation_definition.gd`
  - sidecar metadata for environment family, battle-background family, C/V tier, encounter mode and presentation tags;
  - intentionally does **not** own ordinary-enemy or Elite placement.
- `elemental_presentation_runtime.gd`
  - exactly six reusable element payload families: Fire / Ice / Lightning / Wind / Earth / Water;
  - explicitly rejects Seventh Reaction as an element.

Dialogue Resources gained backward-compatible optional presentation metadata and the DialogueRunner can emit scene-presentation metadata to consumers. Approved dialogue text was not rewritten by this runtime conversion.

### Runtime promotion history

- Shared HD-2D runtime foundation merged to `main`: `2f28894eb9d113f7a5c28f39973627c64d8891c7`.
- Chapter 0 presentation hookup merged to `main`: `e4a46ddb25b4a11e6d414d07223f8e17fe3bfdcd`.
- Chapter 1 presentation hookup merged to `main`: `e907ecdee8572b21585ffff5aa338536b0cd9b50`.
- Chapter 2 presentation hookup merged to `main`: `c6e01693a02e018fd1d90924a20e426b3e8d7434`.
- Chapter 3 presentation hookup merged to `main`: `17ee07cecd93879b3f6f7b935ca1c8a7e605b9db`.
- Chapter 4 presentation hookup is the current bounded runtime promotion; once merged, this document describes the resulting complete Chapters 0–4 code/resource-layer hookup.

Every runtime promotion must pass both the repository Godot Smoke Validation and Android APK Proof on its exact head before merge.

## Enemy / Elite / Hunt boundary

This distinction is a hard implementation guardrail for the current pass.

### Ordinary enemies

Still open unless a specific authored encounter is already protected by chapter canon. The runtime sidecars may say where random encounters are allowed/suppressed, but they do not select the final ordinary enemies, formations, stats or visuals.

### Elites

**Placement remains open.**

- No Chapter 0–4 presentation sidecar has an Elite ID or Elite placement field.
- Presentation validators reject Elite-bearing scene tags.
- No dialogue was changed to place or acknowledge a new Elite.
- Generic runtime capability may support an `elite` presentation category later, but that capability does not assign an Elite to any chapter, map, scene or encounter table.

### Hunts

Hunts remain a separate already-authored category. An already-canon Hunt may have presentation metadata without becoming an Elite. Chapter 4's Crown Prototype sidecar therefore identifies its already-locked **Hunt** status while explicitly remaining separate from Elite placement.

### Mandatory bosses/authored encounters

Existing canon-locked bosses and authored encounters may carry presentation metadata because their story placement is already protected. The runtime pass does not use them to infer or freeze the rest of the enemy roster.

## Active HD-2D authority

Controlling files:

- `docs/ACTIVE_CANON.md`
- `docs/PRESENTATION_RULES.md`
- `docs/canon/AUDIT87_HD2D_PRODUCTION_GRAMMAR_AND_LEGACY_PRESENTATION_CLOSURE.md`
- `docs/canon/AUDIT88_CHAPTERS_00_04_HD2D_CONVERSION_AND_COST_CONSOLIDATION_CLOSURE.md`
- `docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`

Core production targets:

- field characters ~80 px;
- battle characters ~200 px;
- large high-resolution dialogue portraits;
- active party left / enemies right / open center battle lane;
- layered authored environments with restrained camera/parallax/selective geometry;
- small reusable battle-background families;
- Android/APK first-class target;
- random encounters retained;
- exact visual masters and exact Yahtrea world-map geography remain controlling.

Historical `2.5D`/`3D` presentation references in old proof documents, filenames, IDs or comments are superseded as active art direction.

## Accepted technical chain

The technical chain remains accepted as engineering evidence where compatible with current authority.

| Gate | Status | Accepted proof / current interpretation |
|---|---|---|
| 7B.5A | PASS / historical | Exploration/camera/collision architecture proved on Android; old dimensional presentation specifics are superseded by HD-2D art direction |
| 7B.5B | PASS | Android touch movement, boundaries and repeatable APK pipeline |
| 7B.5C | PASS | Authored portrait dialogue, expressions, silent reactions, no choices, control return |
| 7B.5D | PASS | Four-character discrete-round combat and deterministic priority/tie rules |
| 7B.5E | PASS | Unlimited data-driven Standard Card path and automatic hostile retargeting |
| 7B.5F | PASS | Bearer-locked direct-control Prime replacement/suspension/return architecture; presentation now follows Audit88 Prime pipeline |
| 7B.5G | PASS | Versioned plain-data save/load and persistence across full Android app close/relaunch |
| 7B.6 | PASS | Stable-ID dialogue Resources, portrait registry, authoring template, schema validation and Resource-to-runner integration |
| Step 7C Chapter 0 | PASS / MERGED | S001–S006 + C01/C02 approved and integrated; chapter continuity + Godot + Android gate passed |
| Chapter 1 dialogue Resource checkpoint | PASS / MERGED | S007–S011 + C03–C05 exact source-parity + continuity validated |
| Chapter 2 dialogue Resource checkpoint | PASS / MERGED | S012–S016 + C06/C07 exact source-parity + continuity validated |
| Chapter 3 dialogue Resource checkpoint | PASS / MERGED | S017–S021 + H01–H04 corrected source-parity + continuity/Cresthaven validation passed |
| Chapter 4 authoring/static conversion checkpoint | AUTHORING CLOSED | S022–S026 + C08/C09/H05 + Crown Prototype exact source locked; production dialogue Resources/static validation present |
| Audit87 Step 1 | PASS | HD-2D Production Grammar and legacy presentation closure |
| Audit88 Step 2 | PASS / GREEN | Chapters 0–4 HD-2D Conversion Audit Pass 1 + cross-chapter consistency/cost consolidation |
| HD-2D runtime foundation | IMPLEMENTED | Shared presentation contracts, battle layout, state Resources, Prime hooks and validation implemented |
| Ch0 HD-2D presentation hookup | IMPLEMENTED / MERGED | Scene sidecars + environment states; no enemy/Elite placement |
| Ch1 HD-2D presentation hookup | IMPLEMENTED / MERGED | Scene sidecars + environment states + random-encounter boundary; no enemy/Elite placement |
| Ch2 HD-2D presentation hookup | IMPLEMENTED / MERGED | Scene sidecars + environment states + approved random/fixed boundaries; no enemy/Elite placement |
| Ch3 HD-2D presentation hookup | IMPLEMENTED / MERGED | Scene sidecars + environment states + Last Sentinel non-manifestation firewall; no enemy/Elite placement |
| Ch4 HD-2D presentation hookup | IMPLEMENTED | Scene sidecars + environment states + six-element runtime + first-Prime/Crucible/Hunt presentation constraints; no Elite placement |

Accepted historical implementation checkpoints:

- 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`
- 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`
- Chapter 0 production merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`
- Chapter 1 dialogue Resource merge: `f1cd2cd9152e4b7ca7e63bea6469c5b326494120`
- Chapter 2 dialogue Resource merge: `29e7ced1e92d32e2a6a235a6efab2b8a320a36f6`
- Chapter 3 dialogue Resource merge: `5bda1b4641f7762ab07f6e0d98faff953daf5c2e`

## Chapter 0 checkpoint

Closed set:

- S001 Opening
- S002 Wreck Field exploration
- S003 Evacuation Relay decision
- S004 Field Triage Camp revelation
- S005 Confrontation
- S006 Aftermath
- C01 The Fire Is Too Close
- C02 Food After Triage

Historical validated dialogue merge remains accepted.

### Chapter 0 compatibility cleanup

The live S004/S005 dialogue Resource metadata/validator still contains the historical internal label `Broken Champion's Ward` and older Champion/Prime-negative flags.

Current canon interpretation:

- incomplete green/gold **protective Card response**;
- not Prime activation;
- no bearer/Last Sentinel confirmation;
- no voice/warrior/manifestation;
- old internal Champion naming is not player-facing canon.

A future bounded Resource+validator cleanup may neutralize matched internal names while preserving the approved S004→S005 temporary protection behavior unless a separate balance authority revises it.

### Chapter 0 HD-2D runtime hookup

Implemented:

- Convoy Road / Wreck Field / Recovery Line / Triage-Safe Camp presentation families;
- authored environment-state Resources;
- Chapter 0 fixed-authored encounter-mode sidecars;
- explicit **NO_RANDOM** protection across all eight closed Chapter 0 scenes;
- S004 C2/V2 incomplete response metadata;
- Riftmaw same-body/same-HP presentation constraint;
- no realtime destruction or chain-simulation assumption.

Final art assets remain pending.

## Chapter 1 checkpoint

Closed set: **S007–S011 + C03–C05**.  
Exact source: `docs/chapters/dialogue/chapter_01/`.  
Production Resources: `game/content/dialogue/chapter_01/`.

Deterministic generation/validation remains the accepted source-parity and continuity baseline.

Audit79 exact C04 remains controlling: **“Old whore.” / “Bitch.”**

### Chapter 1 HD-2D runtime hookup

Implemented:

- Edgelands Settlement / Wooded Route / Hollow Watch / Ancient Route-Wayfinder sidecars and environment states;
- campaign-standard random-encounter boundary beginning after Brackenwall's east gate;
- mixed random/authored encounter modes where canon requires them;
- Torren absent-from-battle-pre-recruit presentation constraint;
- Castellan same-body/same-HP constraint;
- Wayfinder environmental/cartographic presentation lock;
- validator rejection of Elite-bearing sidecar tags.

Final enemy roster, Elite placement and final art remain pending/open.

## Chapter 2 checkpoint

Closed set: **S012–S016 + C06/C07**.  
Exact source: `docs/chapters/dialogue/chapter_02/`.  
Production Resources: `game/content/dialogue/chapter_02/`.

Audit78 C07 Rewrite Draft 2 remains controlling: **wet sleeves**, no dream disclosure, Torren's late-night weed use treated as ordinary/non-impairing, lit from existing coals, **no modern lighter**.

### Chapter 2 HD-2D runtime hookup

Implemented:

- Dunmere Waterworks / Sunken Archive / Prisoner-Transfer Service / Red Transfer Bastion / Extraction Causeway sidecars and environment states;
- S012 investigation/no-random boundary;
- S013–S015 mixed traversal/authored combat modes;
- S016 fixed-authored Hold-the-Junction-only / no-random boundary;
- water-layer reuse and non-simulation presentation tags;
- Rhazek Chapter-2 exact-state / same-body escalation constraint;
- validator rejection of Elite-bearing sidecar tags.

Final enemy roster, Elite placement and final art remain pending/open.

## Chapter 3 checkpoint

Closed set: **S017–S021 + H01–H04**.  
Exact source: `docs/chapters/dialogue/chapter_03/`.  
Production Resources: `game/content/dialogue/chapter_03/`.

Hard geography remains:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**.

Corrected end-state sequence remains exact: post-Warden command-record room proves false-order assembly; Torren copies routing geometry; party returns to Mirena; Mirena identifies Cresthaven; party stops for the night; S021 begins next morning with Mirena already establishing headquarters.

S021 unlocks Last Sentinel without manifesting it.

### Chapter 3 HD-2D runtime hookup

Implemented:

- Caelora Civic-Judicial / Old City-Suppressed Archive / Deep Command Station / Cresthaven Establishment State 1 sidecars and environment states;
- S018 exactly-two nonlethal authority-encounter presentation constraint;
- S019 choose-four / no-Ruby-Prime-network-leak firewall;
- First Command Warden one-HP/two-state and copy-function-not-choreography constraints;
- S021 Last Sentinel identified/unlocked but **NO manifestation**;
- H04 Last Sentinel case inert/no-Ruby-change lock;
- validator rejection of Elite-bearing sidecar tags.

Final enemy roster, Elite placement and final art remain pending/open.

## Chapter 4 checkpoint

Closed set: **S022–S026 + C08/C09/H05 + Crown Prototype**.  
Exact source: `docs/chapters/dialogue/chapter_04/`.

Hard locks include:

- Chapter starts with Cyanis / Ilyra / Torren / Nimera as permanent travelers; Maevra is not the default traveling member.
- Vaelira joins permanently during S022; choose-four remains active after roster reaches five.
- S022 Elder Briarhide is the first verified modern Last Sentinel manifestation.
- Last Sentinel performs one legal Prime action and dismisses in the same round; Elder Briarhide retreats alive.
- Elemental Hexarch is a harmed living researcher resolved nonlethally.
- Sixfold Crucible is a genuine two-form boss.
- Crown Prototype remains one body / one HP bar / no transformation and reveals pre-existing Relentless Flurry after first clear.
- Random-encounter quantity in Annex/Regulation traversal is area-driven, not a promised approximate count.

### Chapter 4 HD-2D runtime hookup

Implemented at code/resource layer:

- Cresthaven Lower Grounds / Ivorybridge / Annex-Regulation / Sixfold Annex / Regulation Core / Southhold roadside presentation families and environment states;
- S022 first Last Sentinel manifestation tagged **C3/V4**, Round-4-only and routed through the reusable Prime presentation pipeline;
- Vaelira recruitment/choose-four presentation state;
- modular six-element presentation runtime with exactly Fire / Ice / Lightning / Wind / Earth / Water;
- explicit rejection of Seventh Reaction as an element;
- Hexarch living-researcher/nonlethal presentation constraint;
- Sixfold Crucible genuine Form-I→Form-II constraint with fresh Form-II HP/MP and no Prime refresh;
- Crown Prototype as its already-canon **Hunt** category, one body/one HP/no transformation, separate from Elites;
- H05 reuse of Chapter 3 Cresthaven State 1;
- validator rejection of Elite-bearing sidecar tags.

Final field/battle art, final Vaelira sprites/portraits, final elemental effects, final Prime art/effects, final enemy roster and Elite placement remain pending/open.

## Cross-chapter HD-2D production architecture

Durable shared systems/families:

- Edgelands regional environment kit;
- water/wet library;
- Southhold civic material family;
- Ancient Diysean route/archive/command/regulation grammar;
- Ancient cartographic master system;
- Black Host environment family;
- Cresthaven evolving master hub;
- reusable NPC/crowd bases;
- prop/environment state pipeline;
- one permanent battle frame;
- one common transition architecture;
- reusable nonlethal-resolution presentation;
- modular Face/Card/Prime VFX architecture;
- modular six-element library;
- reusable Prime manifestation pipeline.

Boss production categories:

1. same-body / same-HP escalation;
2. genuine new form when the combat problem/body truly changes;
3. Prime-scale entity through the Prime pipeline.

## Current presentation implementation rule

Do **not** implement the historical active rule “real 3D fields + 2D/2.5D characters” as current art direction merely because older proof code/docs say so.

Current production implementation should satisfy Audit87/Audit88 HD-2D staging:

- authored layered environments;
- restrained fixed/bounded camera language;
- ~80 px field sprites;
- ~200 px battle sprites;
- large portraits;
- selective geometry only where useful;
- state swaps and reusable effect systems;
- Android performance discipline.

The runtime contracts and sidecars now exist, but placeholder/proof visuals do **not** count as the final visual conversion.

## Combat / Cards / Prime / persistence accepted behaviors

### Combat
Discrete rounds; enemy action locking before unconfirmed player commands; Item priority; Defend priority; then effective Speed with deterministic tie rules. Maximum four active. Hostile queued actions preserve accepted automatic retarget behavior.

### Standard Cards
Current canon: **30 Standard Cards**, unlimited-use and data-driven; no charges/Essence/ranks/per-battle Standard counter.

### Prime Manifestations
Current canon: **12 Prime Cards**. S021 unlocks Last Sentinel without manifestation; S022 is first verified modern Prime manifestation. Prime technical presentation follows Audit88's reusable manifestation pipeline.

### Persistence
Persistent state remains separate from scene nodes and serializes as versioned plain data. Existing Android close/relaunch proof remains accepted.

## Current progression corrections

- Absolute character level cap: **60**.
- Chapters 11–12 extend progression beyond Level 50 toward 60.
- Worldframe Depths remains a Level-50 optional-major challenge.
- No Level 61+, prestige tier or new equipment tier above Legacy.

## Production workflow from here

For **Chapters 0–4 follow-on implementation**, the presentation contracts and sidecars now provide the code/resource skeleton. Continue with actual map/environment consumers, authored camera/parallax layers, final battle-background consumers, final ~80 px field sprites, final ~200 px battle sprites, portraits, VFX, encounter transitions and hub visuals without changing approved wording/story/gameplay.

Do not fill final ordinary-enemy or Elite placement during unrelated visual/runtime implementation. Run that as its own enemy/Elite placement pass when explicitly approved.

For **new scene/production work**, the inherited next frontier is Chapter 5 — The Mountain Engine, unless the user explicitly redirects the task.

## Non-canon technical fixtures

Graybox maps, placeholder sprites/portraits, disposable proof dialogue, `PROOF_SCHEMA`, proof enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof flags/state and debug UI remain replaceable non-canon fixtures.