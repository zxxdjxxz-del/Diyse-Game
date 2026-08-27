# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.03 / Audit118**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters **0–4** remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapters 0–4 HD-2D Conversion Audit Pass 1: COMPLETE / APPROVED.
- Cross-chapter HD-2D consistency/cost consolidation for Chapters 0–4: COMPLETE / PASS / GREEN.
- Shared HD-2D runtime foundation: IMPLEMENTED.
- Chapters 0–4 HD-2D presentation sidecars/environment-state hookup: IMPLEMENTED at code/resource layer where previously recorded.
- Final visual asset replacement remains production work where not already implemented.
- Detailed late-game scene/runtime implementation remains pending; current macro authority is chapter-correct under Audit113.
- Exact ordinary-equipment and surviving-Relic numerical/source authority is now closed under **Audit118**; runtime/data implementation may use those values directly.
- Exact 17-piece Legacy raw-stat/capstone-perk values remain pending approval and must not be implemented from working v600 yet.

## Current late-game chapter structure

Chapter 10 — The Last Blank was inserted after Chapter 9.

Current operational interpretation:

- **Chapter 10 — The Last Blank** — story architecture locked under Audit112; detailed line-complete/runtime implementation pending.
- **Chapter 11** — Crown Engine / Calder / Custodian / Truth; current macro scope, detailed scene production pending.
- **Chapter 12 — The Reforged March** — final Black Host campaign / Varkesh / Vhalmarch Forward Hub / Vorathen / Vaelkor / cleanup.
- **Chapter 13 — The Last Command** — final Ancient domain / Last Weapon / Entity / Final Severance / ending.

Pre-insertion mapping:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Current files:
- `docs/chapters/chapter_10/CHAPTER_10_THE_LAST_BLANK_STORY_STRUCTURE_LOCK.md`
- `docs/chapters/chapter_11/CHAPTER_11_CURRENT_SCOPE.md`
- `docs/chapters/chapter_12/CHAPTER_12_REFORGED_MARCH_FORWARD_HUB_AND_CLEANUP_LOCK.md`
- `docs/chapters/chapter_13/CHAPTER_13_MACRO_STORY_STRUCTURE_LOCK.md`

Do not wire runtime content against the old `chapter_11 = Forward Hub/Vaelkor` or `chapter_12 = final domain` numbering.

## Current point of no return

Audit109 controls:

**Last Shelter → Reactor Galleries = true irreversible threshold.**

Launching Chapter 13 is deliberate but not itself irreversible. Any runtime gate that immediately disables all world return at Chapter-13 start is stale and must not be implemented.

## Late-game encounter-role mapping

### Chapter 12
- dedicated conventional Black Host Elite role remains separate from Hunts;
- **Regional Hunt #11 — Throne of Emperor Vaelkor** belongs to current Chapter 12;
- Vaelkor mandatory climax remains **Emperor of the Reforged Host → Sovereign Panoply Unbound**.

### Chapter 13
- Regional Hunt: **none**;
- Elite: **Devourer of Names**;
- Calamity Memory: enemy/special-enemy ecosystem role, not Elite;
- mandatory guardian: **Last Weapon Archon**;
- final boss: exactly **Reconstituted Entity → The Last Command**, two genuine full-health forms, no third form.

No runtime implementation claim is implied by these story/category locks.

## Current Story Prime / final-act terminology

Use:
- Last Sentinel / Might
- Last Convergence / Elements
- Last Sanctuary / Grace
- **Last Cartographer / Acuity**
- Last Scribe / Change
- Last Erasure / Ruin

Do not implement the superseded `Resource / Last Measure` final-act role.

## Current world terminology

Use:
- **Yahtrenhold**
- **Black Host Territory**
- **The Westways**
- **The Greyspires**
- **The Blackspine**
- **Westguard**
- **Vhalmarch**

Do not restore `The Crownhold`, `Blackstone` as the formal region label, `Westreach`, or `Black Mountains` in current-facing content.

## Current system baselines

- Player level cap: **70**.
- Base/Subclass class cap: **CL13**.
- Active battle party: maximum four.
- Simultaneously active enemies: maximum eight.
- Standard Cards: **24**, reusable and MP-consuming.
- Prime Cards: **12**.
- No Ability or Ultimate requires a specific equipped weapon once learned.
- MP remains the universal ordinary Ability resource; no personal combat gauges.
- Random encounters remain core campaign grammar where approved.
- **Synthesis is removed.** Do not implement a Synthesis node, Synthesis MP, or Synthesis-based Legacy gate.

## Current equipment implementation baseline — Audit117/118

Current active equipment catalog:
- **38 ordinary**
- **36 Relics**
- **17 native Legacies**
- **91 total**

Audit118 is the current exact data authority for:
- all 38 ordinary stat lines;
- current ordinary Ch2–8 first-acquisition sources;
- Cresthaven ordinary backfill/relative-value rules;
- all 36 surviving Relic stat/Trait packages;
- all 36 Relic Ch6–12 first-acquisition homes;
- current native Legacy Traits;
- exact 30 Forge Component source-role assignments.

Audit117 remains compatible authority for:
- Synthesis removal;
- CL7 Subclass Mastery 3 donor-Relic permission;
- CL11 Subclass Mastery 4 donor-Legacy permission;
- native Legacy completion architecture;
- 17-Legacy package count/slot structure.

Slot rules that must not regress:
- Ilyra: Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow: Weapon + Secondary.
- Vaelira Arcane Staff: one-slot Primary; Focus legal.
- Seyrik Two-Handed Sword: Weapon + Secondary.
- Nimera ordinary/surviving Relic Conduits: one-slot.
- Nimera native Legacy Conduit: **Weapon + Secondary**.

The exact working-v600 Legacy raw-stat and Max-HP/Max-MP/Accuracy/Evasion assignments are **not yet canon**.

## HD-2D runtime foundation

The accepted shared runtime foundation remains under `game/presentation/`, including:
- 1920×1080 reference composition support;
- ~80 px field-character helper targets;
- ~200–220 px battle-character target direction;
- four party-left battle anchors / enemy-right anchors / protected center action lane;
- authored environment-state definitions;
- encounter/scene presentation metadata;
- Prime visual suspension/return hooks;
- Android decorative quality profiles;
- six-element presentation family support.

Exact final art remains separate from the proven runtime architecture.

## Historical technical chain

The following remain accepted as historical engineering evidence where compatible with current authority:
- Step 7B.5 gameplay baseline: `f68e0f7300f3f9a2463e75d0eb8a1a8b4d877c22`
- Step 7B.6 implementation merge: `96c6bdc77f39c988f2185634b4e51546f2a0d76b`
- Chapter 0 production merge: `ce21b5dc4f9e4ea7c8fb8d74f812587437b48dd5`
- Chapter 1 dialogue Resource merge: `f1cd2cd9152e4b7ca7e63bea6469c5b326494120`
- Chapter 2 dialogue Resource merge: `29e7ced1e92d32e2a6a235a6efab2b8a320a36f6`
- Chapter 3 dialogue Resource merge: `5bda1b4641f7762ab07f6e0d98faff953daf5c2e`

Historical presentation-specific 2.5D/3D assumptions remain superseded by HD-2D.

## Chapter 0–4 dialogue / production status

- Chapter 0: S001–S006 + C01/C02 — historical validated runtime set retained where compatible.
- Chapter 1: S007–S011 + C03–C05 — line-complete source + production Resources.
- Chapter 2: S012–S016 + C06/C07 — line-complete source + production Resources.
- Chapter 3: S017–S021 + H01–H04 — corrected line-complete source + production Resources.
- Chapter 4: S022–S026 + C08/C09/H05 + Crown Prototype — exact production source closed; runtime/static conversion present where implemented.

A presentation sidecar does not by itself lock final ordinary-enemy or Elite placement.

## Current production boundaries

Do not silently invent:
- late-game exact scene IDs/dialogue before those chapters enter explicit scene production;
- Chapter-10 reward/card allocation not already explicitly locked by later authority;
- final Level-70 EXP/CEXP curve;
- **pending Legacy raw-stat/capstone-perk numbers**;
- late-game enemy/boss numerical tuning;
- return-path implementation details before their production pass.

Do **not** treat ordinary-equipment or surviving-Relic stats as open anymore; Audit118 is controlling for those exact values.

## Current authoritative documents

- `docs/ACTIVE_CANON.md`
- `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`
- `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT112_CHAPTER_10_THE_LAST_BLANK_MIRENA_EASTERN_WAYFINDER_CALDER_AND_BURIED_REGISTRY_CLOSURE.md`
- `docs/canon/AUDIT111_FINAL_WORLD_MAP_REGION_TERMINOLOGY_AND_VISUAL_AUTHORITY_CLOSURE.md`
- `docs/canon/AUDIT109_WORLD_MAP_ROAD_TRAVEL_AND_LAST_SHELTER_POINT_OF_NO_RETURN_CLOSURE.md`
- `docs/chapters/README.md`

Implementation should always prefer current operational chapter files and later audit overlays over historical pre-insertion numbering.
