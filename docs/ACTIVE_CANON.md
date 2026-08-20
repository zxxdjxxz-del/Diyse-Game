# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with newer authority, the newer authority wins.

## Current written authority

- **Whole-project root:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.83 / Audit98 — Random-Encounter Pressure, Revised EXP Curve and Hunt-Economy Reconciliation**.
- **Date:** August 20, 2026.
- Immediate inherited chain:
  - v1.82 / Audit97 — Campaign EXP Economy, Optional Progression and Battle-Pacing Closure;
  - v1.81 / Audit96 — Level Progression, Hunt Difficulty and Encounter Strength Closure;
  - v1.80 / Audit95 — Major Hunt Architecture and Unlock Closure;
  - v1.79 / Audit94 — Enemy Asset Reuse and Palette-Swap Production Efficiency Lock;
  - v1.78 / Audit93 — Whole-Game Enemy Production and Encounter Architecture Closure;
  - v1.77 / Audit92 — Chapter 9 Crownfall Invasion, Rhazek Climax, and Larkspire Hunt Lock;
  - v1.76 / Audit91 — Seyrik Pre-Reveal, Black Host Advancement, and Chapter 5 Beat-Rewrite Gate Lock;
  - v1.75 / Audit90 — Chapters 0–7 Enemy Production and Terminology Lock;
  - v1.74 / Audit89 — Chapters 11–12 Macro Story Structure and Final-Act Causality Lock;
  - v1.73 / Audit88 — Chapters 0–4 HD-2D Conversion and Cost-Consolidation Closure;
  - v1.72 / Audit87 — HD-2D Production Grammar and Legacy Presentation Language Closure;
  - v1.71 / Audit86 — Cyanis Exact Visual Authority Lock;
  - v1.70 / Audit85 — Yahtrea Exact World Map Visual and Spatial Authority Lock.

Current canon files include:
- `docs/canon/AUDIT98_RANDOM_ENCOUNTER_EXP_AND_HUNT_ECONOMY_RECONCILIATION.md`
- `docs/canon/AUDIT97_CAMPAIGN_EXP_ECONOMY_OPTIONAL_PROGRESSION_AND_BATTLE_PACING_CLOSURE.md`
- `docs/canon/AUDIT96_LEVEL_PROGRESSION_HUNT_DIFFICULTY_AND_ENCOUNTER_STRENGTH_CLOSURE.md`
- `docs/canon/AUDIT95_MAJOR_HUNT_ARCHITECTURE_AND_UNLOCK_CLOSURE.md`
- `docs/canon/AUDIT94_ENEMY_ASSET_REUSE_AND_PALETTE_SWAP_PRODUCTION_EFFICIENCY_LOCK.md`
- `docs/canon/AUDIT93_WHOLE_GAME_ENEMY_PRODUCTION_AND_ENCOUNTER_ARCHITECTURE_CLOSURE.md`
- `docs/canon/AUDIT92_CHAPTER_9_CROWNFALL_INVASION_RHAZEK_CLIMAX_AND_LARKSPIRE_HUNT_LOCK.md`
- `docs/canon/AUDIT91_SEYRIK_PRE_REVEAL_BLACK_HOST_ADVANCEMENT_AND_CHAPTER_5_BEAT_REWRITE_GATE_LOCK.md`
- `docs/canon/AUDIT90_CHAPTERS_00_07_ENEMY_PRODUCTION_AND_TERMINOLOGY_LOCK.md`
- `docs/canon/AUDIT89_CHAPTERS_11_12_MACRO_STORY_STRUCTURE_AND_FINAL_ACT_CAUSALITY_LOCK.md`

## Presentation and project foundation

- Diyse is an **HD-2D JRPG**. Retired active 2.5D/3D presentation language does not control new work.
- Field characters target approximately **80 px**; battle characters approximately **200 px**; dialogue uses large high-resolution portraits.
- Standard combat frame: up to four active party members staggered left, enemies right, open center action/VFX lane.
- Target runtime: approximately **25 hours**.
- Platform target: Android / APK, landscape.
- Permanent roster: exactly six; maximum active battle party: four.
- Dialogue is one authored continuity; no dialogue wheel, morality route, affinity-response system, romance route/system, or selectable protagonist personality.
- Absolute player level cap: **60**. No Level 61+, prestige leveling, or separate postgame leveling campaign.
- Cleared-save `WORLD_AFTER` free roam exists; no separate postgame progression campaign.

## Audit98 progression model — controlling

Diyse distinguishes:

- **Campaign-only level:** produced by mandatory story content plus normal campaign-route random encounters, with no Hunts or other optional/backtracking combat.
- **Recommended / optional-content level:** a descriptive readiness reference for players who engage substantially with optional content.

Mandatory story content must remain beatable on the campaign-only curve. Optional progression can legitimately make mandatory encounters easier.

### Campaign-only progression

- Ch0: **no levels / no EXP progression**.
- Ch1: 1→~5.
- Ch2: ~5→~9.
- Ch3: ~9→~13.
- Ch4: ~13→~17.
- Ch5: ~17→~22.
- Ch6: ~22→~27.
- Ch7: ~27→~32.
- Ch8: ~32→~37.
- Ch9: ~37→~42.
- Ch10: ~42→**~47**.
- Ch11: ~47→**~53**.
- **Campaign-only Chapter 12 launch = around Level 53.**
- Ch12 campaign-only completion ≈ **Level 55**.

### Descriptive optional/readiness progression

Late-game reference:
- End Ch10 campaign-only ~47; most optional **~50–51**.
- End Ch11 / Ch12 launch campaign-only ~53; most optional **~56–57**.
- End Ch12 campaign-only ~55; most optional **~59–60**.
- A 100% player may already be **Level 60 before Chapter 12**.
- Worldframe readiness remains **Level 60** and Worldframe is not required to reach Level 60.

Recommended values are **not hard gates or exact arithmetic obligations**.

## EXP curve — controlling

Levels 1–17 retain:

**Cumulative EXP(L) = 100 × (L − 1)^2**

From the L17→18 level-up onward:

- base increment = `100 × (2L − 1)`;
- multiplier = `1 + 0.35 × (L − 17) / 42` for L≥17;
- round the final level-up cost to the nearest 100 EXP.

The multiplier rises from 1.00× at L17 to 1.35× at L59.

Key cumulative totals:
- L17 = **25,600**;
- L22 = **44,400**;
- L27 = **69,300**;
- L32 = **100,600**;
- L37 = **138,800**;
- L42 = **184,300**;
- L47 = **237,600**;
- L50 = **273,500**;
- L53 = **312,400**;
- L55 = **340,000**;
- L56 = **354,400**;
- L59 = **399,600**;
- L60 = **415,400**.

EXP at Level 60 creates no Level 61+ progression.

## Campaign battle pacing — controlling

The mandatory-story route targets approximately **210 ordinary random encounters across Chapters 1–12**.

Chapter centers:
- Ch1 18; Ch2 19; Ch3 19; Ch4 19; Ch5 20; Ch6 19; Ch7 19; Ch8 18; Ch9 16; Ch10 17; Ch11 18; Ch12 8.
- Total = **210 expected**, not guaranteed.

The 210 excludes Hunt-route combat, Major-Hunt destination combat, other optional/backtracking combat, Elites, named encounters, bosses, Hunts, and Chapter 0 authored tutorial encounters.

There is no hidden chapter quota and no forced exit catch-up battle.

## Random encounter pressure — controlling

Random encounters remain random, using hidden **eligible-movement-distance pressure**.

- no pressure while standing still;
- menus/cutscenes/dialogue pause pressure;
- sprinting cannot reduce encounters per unit distance;
- victory resets pressure and grants grace;
- immediate back-to-back encounters are suppressed;
- long droughts become increasingly unlikely;
- exploration/backtracking naturally creates more encounters.

No battle can trigger before ~0.35 normalized spacing S. Trigger chance rises at ~0.10S checks from 3% at 0.35S through 80% at 1.65S+, targeting mean spacing near 1.00S with no hard forced encounter.

Successful flee gives short grace without a full pressure reset; failed flee does not reset. Same-ecology transitions preserve pressure. Safe rooms may reset. Authored and random battle modes must not stack.

Encounter selection:

**pressure trigger → area → Light/Standard/Heavy roll → weighted local formation pool**

Avoid exact consecutive formation repeats when alternatives exist.

## Active-enemy cap — controlling

Maximum **8 simultaneously active enemies**.

True summons/adds count toward 8; VFX-only entities do not. Reinforcements may enter after space opens, so total participants over a whole battle may exceed 8 while simultaneous active enemies may not.

Typical progression:
- Ch1 2–3, max 4;
- Ch2 3–4, max 4;
- Ch3 3–4, max 5;
- Ch4 4–5, max 6;
- Ch5 5–6, max 7;
- Ch6 5–7, max 8;
- Ch7–11 generally 6–8, max 8;
- Ch12 generally 5–8, max 8.

## Campaign EXP budgets — controlling

Chapter totals:
- Ch1 1,600;
- Ch2 4,800;
- Ch3 8,000;
- Ch4 11,200;
- Ch5 18,800;
- Ch6 24,900;
- Ch7 31,300;
- Ch8 38,200;
- Ch9 45,500;
- Ch10 **53,300**;
- Ch11 **74,800**;
- Ch12 **34,800**.

Cumulative:
- end Ch10 = **237,600**;
- end Ch11 / Ch12 launch = **312,400**;
- expected end Ch12 = **~347,200**, around mid-Level 55.

### Ordinary formation anchors

Whole-formation Light / Standard / Heavy anchors:
- Ch1 45 / 55 / 70;
- Ch2 130 / 165 / 200;
- Ch3 215 / 280 / 315;
- Ch4 315 / 375 / 460;
- Ch5 460 / 610 / 710;
- Ch6 650 / 850 / 995;
- Ch7 830 / 1,050 / 1,250;
- Ch8 1,070 / 1,360 / 1,600;
- Ch9 1,480 / 1,825 / 2,265;
- Ch10 1,835 / 2,300 / 2,640;
- Ch11 2,075 / 2,600 / 3,100;
- Ch12 2,080 / 2,600 / 3,120.

Chapter-wide L/S/H weights:
- Ch1 25/55/20;
- Ch2 25/55/20;
- Ch3 22/55/23;
- Ch4 20/55/25;
- Ch5 18/55/27;
- Ch6 18/55/27;
- Ch7 17/55/28;
- Ch8 17/55/28;
- Ch9 22/55/23;
- Ch10 19/55/26;
- Ch11 22/55/23;
- Ch12 22.5/55/22.5.

Individual formations may vary modestly around anchors if the weighted expectation remains on budget.

## Optional EXP economy — controlling

Pre-Chapter-12 optional leveling pool = **107,100 EXP**:
- 11 Regional Hunts + Hunt-route combat = **46,700**;
- Major Hunts #1–#5 + destination/route combat = **40,400**;
- other optional/backtracking combat = **20,000**.

Worldframe is excluded from the EXP needed to reach Level 60.

### Regional Hunt EXP packages

1. Cistern Devourer — **1,000**
2. Transfer Executioner — **1,500**
3. Archive Judgment Engine — **1,900**
4. Crown Prototype — **2,200**
5. Whitehorn Ravager — **2,700**
6. Winterglass Titan — **3,400**
7. Rift Gate Colossus — **4,500**
8. Rift Siege Beast — **6,000**
9. Mercyfallen Behemoth — **6,800**
10. Authority Remnant — **7,900**
11. Throne of Emperor Vaelkor — **8,800**

Total = **46,700**.

Route planning means:
- Regional #1–#3 about 2 expected route encounters;
- Regional #4–#11 generally 1–2, planning mean ~1.5;
- actual route battles remain random and geometry-driven.

### Major Hunt EXP packages before Worldframe

1. Ashen Whitehorn — **4,200**
2. Crownless Siege Marshal → Crownless War Engine — **5,000**
3. Concordance Guardian — **5,900**
4. Worldscar Leviathan — **12,300**
5. Final Archive Arbiter — **13,000**

Total = **40,400**.

Working route centers are approximately 3 / 3 / 3 / 4 / 3 for Major Hunts #1–#5.

Major Hunt #6 / Worldframe is a Level-60 challenge and is excluded from reach-Level-60 math.

### Other optional/backtracking pool

- **20,000 EXP across approximately 18 optional ordinary battles**.
- Exact encounter identities/routes must attach to real optional spaces rather than being invented solely to satisfy math.

## Hunt recommended player levels — inherited Audit96

Regional:
1. Cistern Devourer — 7
2. Transfer Executioner — 11
3. Archive Judgment Engine — 15
4. Crown Prototype — 20
5. Whitehorn Ravager — 26
6. Winterglass Titan — 32
7. Rift Gate Colossus — 38
8. Rift Siege Beast — 44
9. Mercyfallen Behemoth — 50
10. Authority Remnant — 57
11. Throne of Emperor Vaelkor — 60

Major:
1. Ashen Whitehorn — 21
2. Crownless Siege Marshal → Crownless War Engine — 27
3. Concordance Guardian — 34
4. Worldscar Leviathan — 46
5. Final Archive Arbiter — 58
6. The Unfinished World → Worldheart — 60

Recommended levels are readiness references, not access gates.

## Hunt access versus natural clear — Audit98 clarification

Unlock timing and natural clear timing are distinct. Fixed authored difficulty means a Hunt may unlock before a campaign-only player is near its recommended level; later return is expected behavior, not a failure.

Audit95 unlocks, locations, Prime rewards, boss architecture, and Worldframe dual-gate logic remain unchanged.

## Encounter-strength grammar

There is **no dynamic level scaling**.

Mandatory combat uses the Audit98 campaign-only party curve:
- ordinary enemy ≈ +1 equivalent;
- strong ordinary / formation anchor ≈ +2;
- named miniboss ≈ +2 to +3;
- Elite ≈ +3;
- mandatory story boss ≈ +4 to +5.

Audit97 fixed late-game strength numbers that specifically assumed Level-52 Chapter-12 entry are superseded where necessary; author exact fixed values against the revised ~Level-53 launch reference.

Optional challenge grammar remains:
- Regional Hunt ≈ recommended level +4;
- Major Hunt ≈ +5 early / +6 late;
- Worldframe ≈ **67-equivalent** against a Level-60 party.

## Enemy / Elite / Hunt role closure — inherited Audit93

- Whole-game enemy-production and encounter-role audit across Chapters 0–12 is closed.
- Final Chapter 6 name: **Weather Crown Shield Guard**.
- Final Chapter 11 Elite name: **Lord-Marshal Kharvek**.
- Chapter 12 final-domain names: **Hunger Aspect, Ruin Aspect, Silence Aspect, Fear Aspect**.
- Chapter 9 Elite: Ruin Breach Captain.
- Chapter 10 Elite: Perfect Administrator.
- Chapter 11 Elite: Lord-Marshal Kharvek.
- Chapter 12 Elite: Devourer of Names.
- Elite ≠ Regional Hunt ≠ mandatory story boss unless explicit authority says otherwise.
- Regional Hunts end at #11 Throne of Emperor Vaelkor; Chapter 12 has no Regional Hunt.

## Hunt totals and Major Hunt architecture — inherited Audit95

- Exactly **11 Regional Hunts**.
- Exactly **6 Major Hunts**.
- Exactly **17 Hunt-class optional encounters = 11 Regional + 6 Major**.
- Major Hunts are optional and not required to launch Chapter 12.
- Worldframe Depths opens only after both Final Archive Arbiter clear and Vaelkor defeat.
- Six Major-Hunt bosses remain outside Audit93's 160 chapter-production combat-identity basis; all-in combat-encounter identity count remains 166.

## Enemy asset reuse — inherited Audit94

Production targets for the Audit93 160-identity chapter roster:
- roughly 40–45 true/near palette-material swaps;
- roughly 60% / about 96 identities avoid a completely new base sprite/rig through reuse;
- only roughly 20–25 identities should read to players as obvious palette swaps;
- shared assets never imply shared lore identity.

## World / map authority

The exact user-approved Yahtrea map from August 19, 2026 remains the controlling surface-world visual/spatial master. Do not move, regenerate, reinterpret, simplify, relabel, add, remove, or reconnect geography unless explicitly approved.

Formal modern Realms:
- **Edgelands** — west;
- **Diysereach** — north;
- **Southhold** — south/east and includes Caelora.

The Black Mountains lie west outside Yahtrea and are Black Host territory.

## Chapter status / production frontier

- Chapters **0–4 are COMPLETE/CLOSED** in story/dialogue/gameplay authority and have passed HD-2D Conversion Audit Pass 1 plus cross-chapter consistency/cost consolidation.
- Chapter 2 S015/B003 unnamed masked SECOND OFFICER is Seyrik Rell; dialogue remains unchanged and identity remains unrevealed in-scene.
- Chapter 5 — **The Mountain Engine** — remains the next inherited exact scene-production / HD-2D production-audit frontier, subject to Audit91's beat-level rewrite/reconciliation gate.
- Chapter 9 route is Larkspire / Equal Mercy → Last Sanctuary → Crownfall invasion → Mercy Is Not Surrender; Rhazek/Bastion Devourer is the mandatory Crownfall climax; Mercyfallen Behemoth is Hunt #9.
- Chapter 11 remains Audit89-locked: Varkesh capture precedes Forward Hub; Vaelkor two-form climax; post-Vaelkor cleanup; deliberate Chapter 12 launch.
- Chapter 12 remains Audit89-locked: no Regional Hunt; Devourer of Names Elite; Last Weapon Archon mandatory guardian; Reconstituted Entity → The Last Command; modern Final Severance; no third form.

## Implementation boundary after Audit98

Audit98 now locks:
- ~210 expected campaign random encounters;
- hidden distance-based encounter pressure;
- 8 simultaneously active enemy maximum;
- Chapter-5-onward EXP acceleration;
- revised campaign-only progression and Chapter-12 launch around Level 53;
- chapter EXP budgets and current formation anchors;
- descriptive optional progression bands;
- normalized Hunt EXP packages and 107,100 pre-Ch12 optional pool;
- completionist pre-Ch12 Level-60 allowance;
- Worldframe exclusion from reach-Level-60 math.

Still implementation/playtest territory:
- exact per-area S calibration from real route distance;
- exact formation membership and local weights where not already authored;
- individual formation reward variation around chapter anchors;
- raw final HP/Attack/Defense/Magic/Spirit/Speed constants;
- exact optional-route geometry where not separately locked;
- final per-Hunt route-vs-boss EXP splits consistent with package totals;
- performance validation of 4-party + 8-enemy VFX-heavy late-game battles on target Android hardware.

Omission from this implementation-facing summary does not erase compatible older canon. Exact approved visual masters and newer explicit user corrections always control conflicts.
