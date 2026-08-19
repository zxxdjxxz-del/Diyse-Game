# Diyse — Current Implementation Status

**Written authority checkpoint:** v1.73 / Audit88  
**Presentation target:** HD-2D  
**Step 7B.5:** COMPLETE / historical technical PASS on real Android hardware, interpreted through current HD-2D authority  
**Step 7B.6:** COMPLETE / PASS — production dialogue authoring handoff locked  
**Story/dialogue production authority:** Chapters 0–4 COMPLETE/CLOSED  
**HD-2D Conversion Audit Pass 1:** Chapters 0–4 COMPLETE / APPROVED  
**Cross-chapter HD-2D consistency/cost consolidation:** COMPLETE / PASS / GREEN  
**Next inherited production-audit / scene-production frontier:** Chapter 5 — The Mountain Engine  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Completion states must remain separate

The repository uses distinct completion states. Do not conflate them.

1. **Authoring/canon closure:** Chapters 0–4 have approved story, dialogue, continuity, relationship, gameplay and production authority.
2. **HD-2D conversion closure:** Audit88 defines how completed Chapters 0–4 are staged/implemented in the active HD-2D grammar without rewriting them.
3. **Repository line-complete source:** Chapters 1–4 have exact approved scene-level Markdown under `docs/chapters/dialogue/`.
4. **Runtime dialogue Resource integration:** Chapters 0–3 have validated production `.tres` scene sets. Chapter 4 has production conversion/static validation present where currently implemented; in-engine runtime smoke completion remains separate QA.
5. **Final presentation implementation:** maps, final field/battle sprites, portraits, battle backgrounds, VFX, encounter consumers, world triggers and hub services remain runtime production work where not already present.

A missing final asset or consumer is not evidence that approved dialogue/canon is missing.

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
| Chapter 4 authoring/static conversion checkpoint | AUTHORING CLOSED | S022–S026 + C08/C09/H05 + Crown Prototype exact source locked; static Resource/source validation present where implemented; runtime smoke remains QA |
| Audit87 Step 1 | PASS | HD-2D Production Grammar and legacy presentation closure |
| Audit88 Step 2 | PASS / GREEN | Chapters 0–4 HD-2D Conversion Audit Pass 1 + cross-chapter consistency/cost consolidation |

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

Historical validated merge remains accepted.

### Chapter 0 compatibility cleanup

The live S004/S005 Resource metadata/validator still contains the historical internal label `Broken Champion's Ward` and older Champion/Prime-negative flags.

Current canon interpretation:

- incomplete green/gold **protective Card response**;
- not Prime activation;
- no bearer/Last Sentinel confirmation;
- no voice/warrior/manifestation;
- old internal Champion naming is not player-facing canon.

A future bounded Resource+validator cleanup may neutralize matched internal names while preserving the approved S004→S005 temporary protection behavior unless a separate balance authority revises it.

### Chapter 0 HD-2D conversion

Audit88 locks:

- Convoy Road / Wreck Field / Recovery Line / Triage-Safe Camp families;
- three principal battle-background families;
- seven authored tutorial encounters and **no normal random-encounter table**;
- S004 C2/V2 incomplete response;
- Riftmaw same-HP authored state escalation;
- no realtime destruction or chain simulation.

## Chapter 1 checkpoint

Closed set: **S007–S011 + C03–C05**.  
Exact source: `docs/chapters/dialogue/chapter_01/`.  
Production Resources: `game/content/dialogue/chapter_01/`.

Deterministic generation/validation remains the accepted source-parity and continuity baseline.

Audit79 exact C04 remains controlling: **“Old whore.” / “Bitch.”**

### Chapter 1 HD-2D conversion

Audit88 locks:

- Edgelands Settlement / Wooded Route / Hollow Watch / Ancient Route-Wayfinder families;
- campaign-standard fast random-battle transition beginning after Brackenwall's east gate;
- Torren absent from battle presentation before recruitment;
- Castellan as layered same-HP state escalation;
- Wayfinder as bespoke environmental peak and reusable Ancient cartographic master source.

## Chapter 2 checkpoint

Closed set: **S012–S016 + C06/C07**.  
Exact source: `docs/chapters/dialogue/chapter_02/`.  
Production Resources: `game/content/dialogue/chapter_02/`.

Audit78 C07 Rewrite Draft 2 remains controlling: **wet sleeves**, no dream disclosure, Torren's late-night weed use treated as ordinary/non-impairing, lit from existing coals, **no modern lighter**.

### Chapter 2 HD-2D conversion

Audit88 locks:

- Dunmere Waterworks / Sunken Archive / Prisoner-Transfer Service / Red Transfer Bastion / Extraction Causeway families;
- reusable water/wet library instead of fluid simulation;
- oversized layered Archive Leviathan using water occlusion to sell scale;
- reusable Black Host environment grammar;
- evacuation scale through limited sprites/silhouettes/audio/state changes;
- Rhazek exact Chapter-2 visual state and same-bar Ruin/armor escalation.

## Chapter 3 checkpoint

Closed set: **S017–S021 + H01–H04**.  
Exact source: `docs/chapters/dialogue/chapter_03/`.  
Production Resources: `game/content/dialogue/chapter_03/`.

Hard geography remains:

**Caelora → Old City / Suppressed Archives → separate Cresthaven**.

Corrected end-state sequence remains exact: post-Warden command-record room proves false-order assembly; Torren copies routing geometry; party returns to Mirena; Mirena identifies Cresthaven; party stops for the night; S021 begins next morning with Mirena already establishing headquarters.

S021 unlocks Last Sentinel without manifesting it.

### Chapter 3 HD-2D conversion

Audit88 locks:

- Caelora Civic-Judicial / Old City-Suppressed Archive / Deep Command Station / Cresthaven Establishment State 1 families;
- old “large 3D Warden chamber” wording replaced by layered HD-2D hero composition;
- choose-four visual/runtime distinction after Nimera joins;
- Warden copies function rather than character body choreography;
- Cresthaven built as one evolving reusable hub.

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

### Chapter 4 HD-2D conversion

Audit88 locks:

- Cresthaven Lower Grounds / Ivorybridge / Annex Approach-Regulation Terraces / Sixfold Annex / Regulation Core families;
- first Last Sentinel manifestation as **C3/V4** and reusable Prime presentation pipeline;
- full permanent Vaelira HD-2D production package at recruitment;
- modular six-element effect/environment library;
- Hexarch one living-human base + elemental overlays;
- genuine Crucible Form II body using one base + six independent inherited-trait modules;
- Crown Prototype reuse through Annex assets.

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

Historical proof architecture remains useful only where it supports current behavior without forcing the retired visual target.

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

For **Chapters 0–4 follow-on implementation**, start from their exact approved source/validated Resources and the Audit88 HD-2D conversion record. Wire maps, world triggers, battle-background consumers, presentation assets, encounter transitions, Cresthaven states and other runtime systems without changing approved wording/story/gameplay.

For **new scene/production work**, the inherited next frontier is Chapter 5 — The Mountain Engine, unless the user explicitly redirects the task.

## Non-canon technical fixtures

Graybox maps, placeholder sprites/portraits, disposable proof dialogue, `PROOF_SCHEMA`, proof enemies/stats, `Proof Strike`, temporary flat damage/rewards, proof flags/state and debug UI remain replaceable non-canon fixtures.