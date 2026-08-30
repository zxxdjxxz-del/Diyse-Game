# Diyse — Enemy & Boss Mandatory-vs-Completionist Validation

**Owner:** `09_ENEMIES_AND_ENCOUNTERS` + `16_BALANCE_AND_TESTING`  
**Status:** **PAPER VALIDATION COMPLETE THROUGH CHAPTER 13 / TRUE-BATTLE FOLLOW-UP ACTIVE**  
**Prerequisite:** direct-damage Power audit **CLOSED**

## Purpose
Validate the already-authored enemy and boss roster against the actual player power available on two routes:

1. **Mandatory / critical-path party** — only guaranteed story progression and resources available before the encounter.
2. **Completionist party** — plausible use of optional quests, Hunts, stronger available equipment, Cards, Primes, Legacies, and additional EXP/CEXP available before the encounter, without assuming arbitrary grind beyond authored content.

This pass answers:
> Does the fixed encounter remain fair and appropriately threatening for the mandatory party while allowing optional progression to create a real, earned advantage?

## Power-audit boundary
The global Power-authoring audit is complete.

Therefore:
- do **not** reopen every action coefficient;
- begin from current stats, Powers, AI, action weights, forms, thresholds, statuses, targeting, supports, and formations;
- change a Power coefficient only when a specific encounter fails validation and that action is the demonstrated source of the failure;
- record such a change as **targeted balance tuning**, not as incomplete Power authoring.

## Mandatory-party baseline
For each encounter, record the guaranteed state immediately before it:
- party roster and active-party options;
- Player Level range;
- Base/Subclass access and plausible Class Levels;
- mandatory equipment tier / guaranteed Relics or Legacies;
- guaranteed Standard Cards and Prime access;
- mandatory consumable availability and reasonable stock;
- required mechanics/tutorial knowledge;
- any story-specific buffs, protections, scripted restrictions, or nonlethal victory rules.

Do not assume optional Hunt/CQ/SQ rewards for this baseline.

## Completionist baseline
For the same encounter, record the strongest **plausible authored-content** state available without grinding beyond authored content:
- optional EXP and CEXP available before the encounter;
- completed Side/Character Quests available by that point;
- cleared Regional/Major Hunts available by that point where sequence permits;
- best legitimately obtainable equipment, Relics, Legacies, Cards, and Primes;
- stronger consumable stock and economy state;
- broader build flexibility.

Completionist advantage is intentional. Do not dynamically scale the encounter to erase it.

## Validate each encounter for
### Incoming threat
- basic-hit damage;
- strongest normal action;
- AoE pressure;
- burst/telegraphed action;
- status application pressure;
- focus-fire / targeting danger;
- support-object contribution.

### Enemy durability
- mandatory route time-to-kill / rounds;
- completionist route time-to-kill / rounds;
- whether DEF/Spirit/HP create slog rather than challenge;
- whether high completionist damage skips core mechanics too reliably.

### Resource pressure
- MP expenditure;
- healing/consumable burden;
- status-clearing burden;
- Prime timing where available;
- expected recovery between formations.

### Encounter architecture
- action weights;
- phase/form thresholds;
- support spawn timing;
- finite vs respawning supports;
- fresh-body Prime refresh only where canonically allowed;
- nonlethal/protected resolution rules;
- formation synergy and action economy.

## Intended route relationship
Default goal:
- mandatory route = intended challenge tier;
- completionist route = meaningfully safer/faster;
- optional progression must feel useful;
- completionist route should not routinely erase the encounter before its defining mechanic appears, unless that is a deliberate reward for extreme late-game power;
- no dynamic level scaling.

Boss-specific historical round targets remain useful references, not universal laws for ordinary encounters.

## Tuning order
When an encounter fails, tune in this order unless evidence points elsewhere:
1. formation composition / encounter frequency;
2. AI weights / targeting / phase timing;
3. HP / DEF / Spirit / Speed / status rate;
4. ATK / MAG;
5. specific action Power;
6. major kit rewrite only if the encounter identity itself is broken.

This order prevents a closed Power audit from being needlessly reopened.

## Coverage order
Work chapter-by-chapter so progression assumptions stay synchronized:
1. Chapter 0
2. Chapter 1
3. Chapter 2
4. Chapter 3
5. Chapter 4
6. Chapter 5
7. Chapter 6
8. Chapter 7
9. Chapter 8
10. Chapter 9
11. Chapter 10
12. Chapter 11
13. Chapter 12
14. Chapter 13

At each chapter, validate:
- ordinary formations;
- Elite(s);
- authored/protected encounters;
- story boss(es);
- Regional/Major Hunts that become available in that progression window.

## Result states
Use exactly:
- **PASS** — current values work for both baselines;
- **PASS / COMPLETIONIST ADVANTAGE HIGH BUT ACCEPTABLE**;
- **ADJUSTED** — targeted tuning made and revalidated;
- **OPEN — DATA/PLACEMENT DEPENDENCY** — cannot certify yet because required story/formation/placement data is genuinely unresolved.

## Completion gate
This pass is closed only when all placed combat content has a recorded mandatory and completionist result or an explicit placement/data dependency.

After this gate:
> CEXP recalibration is **CLOSED v91**; build canonical party snapshots and begin representative true-battle simulations.

## Current progress ledger — v89
- **Chapter 0 — ADJUSTED / VALIDATED**
  - mandatory baseline = completionist baseline
  - Riftmaw HP **760 → 340**
  - 3 guaranteed Field Salves added as finite Chapter-0 field issue
  - no direct-damage Power changed
- **Chapter 1 — ADJUSTED / VALIDATED v78 Maevra-corrected**
  - actual route anchors used: Lv1 start → Lv5 end; S008 ~Lv2 mandatory / ~Lv3 high-side
  - Maevra explicitly counted before and after Torren recruitment
  - Watch Captain Frame HP **820 → 500** confirmed at ~3.8 serious rounds with Maevra
  - Cistern Devourer retained against four-person post-Torren party
  - no direct-damage Power changed
- **Chapter 2 — ADJUSTED / VALIDATED v78**
  - actual route anchors used: Lv5 start → Lv9 end
  - active party = Cyanis + Ilyra + Torren + Maevra guest
  - ordinary roster / Archive Duplicant / Rhazek / Hold the Junction / Transfer Executioner retained
  - Archive Leviathan Recorded Pattern exact effect/duration closed; same-bar emergence fixed at 45% HP
  - no direct-damage Power changed
- **Chapter 3 — ADJUSTED / VALIDATED v79**
  - actual route anchors used: Lv9 start → Lv13 end; S018 Lv9; S019 Lv9→10; S020 Lv10→11; Warden Lv11 mandatory
  - Maevra counted as guest combat option; after Nimera joins the combat roster has five available bodies but only four active
  - recovered approved Chapter-3 formation compositions into `09_ENEMIES_AND_ENCOUNTERS/ENCOUNTER_FORMATIONS/CHAPTER_03_FORMATIONS.md`
  - Grand Inquisitor Frame HP **1,450 → 1,200** to satisfy its real-access 2–4 serious-round Elite role
  - First Command Warden and Archive Judgment Engine retained
  - False-Warrant Adept remains explicit placement dependency
  - no direct-damage Power changed
- **Chapter 4 — PASS / VALIDATED v80**
  - actual route anchors used: Lv13 opening → ~Lv15 middle → Lv17 late/end
  - Maevra excluded from the default Chapter-4 balance baseline; Vaelira joins after S022; active cap remains four
  - recovered approved Reaction Annex opening/middle/late formation compositions and weights without reviving obsolete stat/EXP rows
  - ordinary roster and Annex Duelist retained
  - Elder Briarhide, Reaction Conduit, Regulation Crucible → The Seventh Reaction retained
  - Crown Prototype retained at Lv20 recommendation despite intentional earlier Lv17–18 access
  - protected Annex staff remain placement dependencies
  - no raw-stat or direct-damage Power changed
- **Chapter 5 — PASS / VALIDATED v81 WITH PLACEMENT DEPENDENCIES**
  - actual route anchors used: Lv17 start → Lv18 Furnace Tyrant → Lv20 Deepforge Colossus → Lv22 end
  - completionist comparison: Lv19 chapter entry → Lv20 Furnace Tyrant → Lv22 Deepforge Colossus
  - five permanent characters available / four active; Maevra not default Chapter-5 guest; Seyrik not playable
  - ordinary bodies, Ruin Forgemaster, Furnace Tyrant, Deepforge Colossus, and Whitehorn Ravager retained
  - Whitehorn Ravager remains recommended Lv26 despite intentional earlier Lv22–23 access
  - Highland Resistance Fighter placement and exact ordinary formations remain explicit data/story dependencies
  - no raw-stat or direct-damage Power changed
- **Chapter 6 — PASS / VALIDATED v82 WITH PLACEMENT DEPENDENCIES**
  - actual route anchors used: Lv22 start → Lv23 Crownstorm Roc → Lv24 Matron Zevraya → Lv25 Masked Seyrik → Lv27 end
  - five playable permanent characters / four active until chapter-end; Seyrik remains enemy/story identity until after his forced-disengagement encounter
  - Weather Crown and Crimson Work ordinary bodies plus Crimson Progenitor retained
  - Crownstorm Roc, Matron Zevraya → Perfected War Mother, and Masked Seyrik formally validated from the preliminary boss recertification
  - Winterglass Titan retained at Lv32 recommendation; Ashen Whitehorn retained at post-Ch6 Lv33 recommendation
  - authored-special placement and exact ordinary formations remain explicit data/story dependencies
  - no raw-stat or direct-damage Power changed
- **Mandatory story bosses Chapters 2–13 — preliminary mandatory/completionist recertification already exists and is carried forward**
  - do not automatically redo these boss bodies
  - re-open a specific boss only if the broader formation/resource validation exposes a contradiction
- **Major Hunts #1–#5 — unlock/recommended-level recertification already exists**
  - still require the full two-baseline resource/throughput certification where not explicitly recorded
- **Regional Hunts, ordinary formations, optional Elites, authored/protected content — active remaining coverage from Chapter 2 onward**

- **Chapter 7 — PASS / VALIDATED v83 WITH PLACEMENT DEPENDENCIES**
  - actual route anchors used: Lv27 start → Lv27 Chainworks → Lv30 Revision Arbiter → Lv32 end / Sixfold Volition
  - all six permanent characters available / four active; Seyrik fully playable
  - Sixfold Volition occurs only after mandatory Chapter-7 combat, so Subclasses are excluded from the chapter baseline
  - ordinary roster, authored/protected kits, First Registrar's Shade, Chainworks Behemoth, Revision Arbiter, Rift Gate Colossus, and post-Ch7 Major Hunt #2 retained
  - exact ordinary formations/authored-special placements remain dependencies
  - no raw-stat or direct-damage Power changed

- **Chapter 9 — PASS / VALIDATED v85 WITH FORMATION/HUNT-TIMING DEPENDENCIES**
  - actual route anchors used: Lv37 start → Lv37 Equal Mercy → Lv38 post-Last-Sanctuary → Lv40 Rhazek → Lv42 end
  - all six permanent characters available / four active; Subclasses legal throughout
  - ordinary roster, Mercy Warden, Relay-Fever Patient, Ruin Breach Captain, Equal Mercy Arbiter, Rhazek, Mercyfallen Behemoth, and post-Ch9 Concordance Guardian retained
  - Rhazek completionist proof validated at Lv48 without RH9 / Lv49 with RH9 because RH9 exact return trigger remains open
  - exact ordinary formations and RH9 exact S### trigger remain dependencies
  - no raw-stat or direct-damage Power changed

- **Chapter 10 — PASS / VALIDATED v86 WITH DATA DEPENDENCIES**
  - actual route anchors used: Lv42 start → Lv45 Registry Warden → Lv46 post-Warden → Lv47 end
  - completionist fixed-content anchors: ~Lv51 start → Lv54 Registry Warden → Lv55 clear
  - all six permanent characters available / four active; Subclasses legal throughout
  - all eight reused ordinary bodies retained; recovered Wayfinder/Registry compositions pass
  - Registry Warden retained and formally validated
  - Worldscar Leviathan retained at after-Ch10 recommended Lv60 and formally validated against Lv47 mandatory / Lv55–56 completionist access
  - exact eastern-forest formations and ordinary action-selection weights remain data-recovery dependencies
  - Old Relay Warden exact current raw/action sheet remains a separate quest-boss data dependency
  - no raw-stat or direct-damage Power changed


- **Chapter 11 — PASS / VALIDATED v87 WITH DATA/STORY DEPENDENCIES**
  - actual route anchors used: Lv47 start → Lv49 Calder → Lv51 Custodian → Lv52 end
  - completionist fixed-content anchors: Lv57 start → Lv59 Calder → Lv60 Custodian → Lv61 clear
  - all six permanent characters available / four active; Subclasses legal throughout
  - approved opening/middle/late formation compositions and weights recovered
  - all nine ordinary bodies retained
  - Crown Engine Technician kit retained; exact authored scene placement remains a dependency
  - Perfect Administrator, Calder → Crown-Bound Living Anchor, The Custodian, Authority Remnant, and Final Archive Arbiter carry-forward formally validated
  - exact ordinary action-selection weights and RH10 exact within-chapter access remain dependencies
  - no raw-stat or direct-damage Power changed

- **Chapter 12 — PASS / VALIDATED v88 WITH DATA/STORY/RUNTIME DEPENDENCIES**
  - actual route anchors used: Lv52 start → Lv54 Varkesh → Lv56 Vaelkor → Lv57 end
  - completionist fixed-content anchors: Lv63 start → Lv64 Varkesh → Lv66 Vaelkor → Lv66 clear; RH11 may raise pre-Vaelkor state to ~Lv67 depending timing
  - all eleven ordinary bodies and nine recovered formation compositions retained
  - Compelled Relay Bearer and Lord-Marshal Kharvek retained; Kharvek exact placement remains story-owned
  - Varkesh final capture and Vaelkor → Sovereign Panoply Unbound promoted to formal v88 validation
  - Regional Hunt #11 formally validated at Lv61–62; exact within-chapter timing remains open
  - Major Hunt #6 paper-recertified at Lv70 against ~Lv58 low-option prerequisite-clearing route / ~Lv68 exhaustive completionist; runtime duration gate remains
  - no raw-stat or direct-damage Power changed

- **Chapter 13 — PASS / VALIDATED v89 WITH DATA/RUNTIME DEPENDENCIES**
  - actual route anchors used: Lv57 start → Lv58 Last Weapon Archon → Lv60 Last Shelter/PONR → Lv61 final boss → Lv62 ending
  - completionist anchors: Lv68 chapter start → Lv69 pre-Archon without MH6 → Lv70 by Last Shelter / final boss
  - all nine ordinary bodies and recovered 3–4-body formations retained
  - Devouring Echo / Calamity Memory replay clamps retained
  - Devourer of Names, Last Weapon Archon, and Reconstituted Entity → The Last Command promoted to formal v89 validation
  - Last Shelter treated as the true recovery/loadout/PONR split
  - no raw-stat or direct-damage Power changed

Campaign paper-validation status:
> **COMPLETE THROUGH CHAPTER 13 / v89**

Next active balance frontier:
> **CEXP recalibration CLOSED v91; true-battle snapshot/simulation pass next.**


## Current chapter-validation ledger
- Chapter 0 — **VALIDATED v76**
- Chapter 1 — **VALIDATED v78 Maevra-corrected**
- Chapter 2 — **VALIDATED v78**
- Chapter 3 — **VALIDATED v79**
- Chapter 4 — **VALIDATED v80**
- Chapter 5 — **VALIDATED v81 WITH PLACEMENT DEPENDENCIES**
- Chapter 6 — **VALIDATED v82**
- Chapter 7 — **VALIDATED v83**
- Chapter 8 — **PASS / VALIDATED v84**
  - actual route anchors used: Lv32 start → Lv33 Western Rift Engine → Lv35 Varkesh → Lv37 end
  - Subclass access legal throughout; six permanent characters available / four active
  - ordinary enemies, Conqueror Legate, Western Rift Engine, Varkesh, and Rift Siege Beast retained
  - no numerical or Power changes; exact ordinary formations and RH8 within-chapter timing remain dependencies
- Chapter 9 — **PASS / VALIDATED v85**
  - actual route anchors used: Lv37 start → Lv37 Equal Mercy → Lv38 post-Last-Sanctuary → Lv40 Rhazek → Lv42 end
  - no numerical or Power changes; formation/RH9 timing dependencies retained
- Chapter 10 — **PASS / VALIDATED v86**
  - actual route anchors used: Lv42 start → Lv45 Registry Warden → Lv46 post-Warden → Lv47 end
  - no numerical or Power changes; forest-formation/action-weight and Old Relay Warden data dependencies retained
- Chapter 11 — **PASS / VALIDATED v87**
  - actual route anchors used: Lv47 start → Lv49 Calder → Lv51 Custodian → Lv52 end
  - no numerical or Power changes; recovered formation compositions; action-weight/Technician-placement/RH10-timing dependencies retained
- Chapter 12 — **PASS / VALIDATED v88**
  - no numerical or Power changes; Kharvek/RH11 timing and MH6 runtime dependencies retained
- Chapter 13 — **PASS / VALIDATED v89**
  - no numerical or Power changes; action-weight/formation-frequency and final runtime dependencies retained

Campaign planned paper validation — **COMPLETE THROUGH CHAPTER 13 / v89**

Chapter validation must always distinguish chapter-start, intermediate, and chapter-end player levels. Do not validate a whole chapter at its end-level target.
