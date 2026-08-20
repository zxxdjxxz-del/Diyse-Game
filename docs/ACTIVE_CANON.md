# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with newer authority, the newer authority wins.

## Current written authority

- **Whole-project root:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.82 / Audit97 — Campaign EXP Economy, Optional Progression and Battle-Pacing Closure**.
- **Date:** August 20, 2026.
- Immediate inherited chain:
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

## Audit97 progression model — controlling

Diyse uses two distinct level references:

- **Campaign-only level:** produced by mandatory story content plus normal campaign-route random encounters, with no Hunts or other optional/backtracking combat.
- **Recommended / optional-content level:** readiness target after substantial optional engagement.

Mandatory story content must remain beatable on the campaign-only curve. Optional progression can legitimately make mandatory encounters easier.

### Campaign-only progression

- Ch0: **no levels / no EXP progression**.
- Ch1: 1→5.
- Ch2: 5→9.
- Ch3: 9→13.
- Ch4: 13→17.
- Ch5: 17→22.
- Ch6: 22→27.
- Ch7: 27→32.
- Ch8: 32→37.
- Ch9: 37→42.
- Ch10: 42→47.
- Ch11: 47→**52**.
- **Campaign-only Chapter 12 entry = Level 52.**
- Ch12 campaign-only completion ≈ **Level 55**.

### Recommended / optional-content readiness

- Ch1 start 1; Ch2 5; Ch3 9; Ch4 13; Ch5 17; Ch6 23; Ch7/post-Accord 29; Ch8 35; Ch9 41; Ch10 47; Ch11 ~54.
- **Recommended Chapter 12 launch = Level 59.**
- **Worldframe readiness = Level 60.**

Audit96's phrase “Chapter 12 begins at Level 59” is superseded as a campaign-guaranteed statement; it now means recommended launch readiness. Audit96's ~54 Chapter 11 start is likewise a recommended optional-content target, not the campaign-only start.

## EXP formula — controlling

Character-level cumulative EXP:

**Cumulative EXP for Level L = 100 × (L − 1)^2**

Key totals:
- Level 52 = **260,100 EXP**;
- Level 55 = **291,600 EXP**;
- Level 59 = **336,400 EXP**;
- Level 60 = **348,100 EXP**.

EXP at Level 60 does not create Level 61+ progression.

## Campaign battle pacing — controlling

The mandatory-story route targets **165 ordinary random battles across Chapters 1–12**, including ordinary battles while traveling between mandatory destinations.

Campaign ordinary-battle targets:
- Ch1 10; Ch2 11; Ch3 11; Ch4 12; Ch5 14; Ch6 15; Ch7 16; Ch8 16; Ch9 16; Ch10 17; Ch11 17; Ch12 10.
- Total = **165**.
- Practical normal-route tuning tolerance: approximately **165 ± 8**.

The 165 excludes Hunt-route combat, Major-Hunt destination combat, other optional/backtracking combat, Elites, named encounters, bosses, Hunts, and Chapter 0 authored tutorial encounters.

## Campaign EXP budget — controlling

Through Chapter 11:
- **260,100 total campaign EXP** → campaign-only Level 52 entering Chapter 12.
- **169,000 EXP** from 155 campaign ordinary battles.
- **91,100 EXP** from mandatory named/story encounters.

Chapter 12 adds **31,500 mandatory EXP**:
- 10 ordinary battles = 19,000;
- Devourer of Names = 2,400;
- Last Weapon Archon = 3,400;
- Reconstituted Entity → The Last Command = 6,700, awarded only after The Last Command is defeated.

Campaign-only completion therefore lands around Level 55.

## Optional EXP economy — controlling

Pre-Chapter-12 optional combat pool = **105,000 EXP**:
- 11 Regional Hunts + Hunt-specific route combat = **42,000**;
- Major Hunts #1–#5 + destination combat = **43,000**;
- other optional/backtracking combat = **20,000**.

From campaign-only Level 52:
- Level 59 requires **76,300 optional EXP** (~73% of the pool);
- Level 60 requires **88,000 optional EXP** (~84% of the pool).

This intentionally makes substantial optional play necessary for the recommended finale level and **most** meaningful optional combat necessary to cap before the finale. Worldframe is excluded from the EXP needed to reach Level 60.

### Regional Hunt EXP packages

1. Cistern Devourer — 1,000
2. Transfer Executioner — 1,500
3. Archive Judgment Engine — 1,900
4. Crown Prototype — 2,400
5. Whitehorn Ravager — 3,000
6. Winterglass Titan — 3,700
7. Rift Gate Colossus — 4,300
8. Rift Siege Beast — 5,000
9. Mercyfallen Behemoth — 5,700
10. Authority Remnant — 6,400
11. Throne of Emperor Vaelkor — 7,100

Total = **42,000**. Packages include the boss plus Hunt-specific route combat; exact route-vs-boss splits remain implementation data unless separately locked.

### Major Hunt EXP packages before Worldframe

1. Ashen Whitehorn — 4,200
2. Crownless Siege Marshal → Crownless War Engine — 5,600
3. Concordance Guardian — 7,200
4. Worldscar Leviathan — 10,000
5. Final Archive Arbiter — 16,000

Total = **43,000**. Major Hunt #6 / Worldframe remains a Level-60 challenge and is excluded from the EXP needed to reach Level 60.

### Other optional/backtracking pool

- Budget = **20,000 EXP across approximately 18 optional ordinary battles**.
- Exact encounter identities/routes are open and must attach to real optional spaces rather than being invented solely to satisfy the math.

## Encounter-strength grammar — controlling after Audit97

Enemies should generally feel stronger than a campaign-only party. There is **no dynamic level scaling**.

For mandatory campaign roles, the balance reference is the campaign-only expected party at the authored placement:
- ordinary enemy ≈ +1 equivalent;
- strong ordinary / formation anchor ≈ +2;
- named miniboss ≈ +2 to +3;
- Elite ≈ +3;
- mandatory story boss ≈ +4 to +5.

Audit96's Ch5–Ch12 ordinary-enemy and Elite numeric tables are superseded wherever they assumed the recommended/optional-content curve as the mandatory campaign reference. Exact fixed per-Elite values may be data-authored later while preserving the +3 rule.

Mandatory story-boss climax equivalents now use campaign-only progression:
- Ch1 5→9; Ch2 9→13–14; Ch3 13→17; Ch4 17→21–22; Ch5 22→26–27; Ch6 27→31–32; Ch7 32→36–37; Ch8 37→41–42; Ch9 42→46–47; Ch10 47→51–52; Ch11 52→56–57; Ch12 campaign-only 52→~55 with final-sequence pressure around 58–60+ equivalent.

Optional challenge rules remain:
- Regional Hunt ≈ recommended level +4;
- Major Hunt ≈ +5 early / +6 late;
- Worldframe ≈ **67-equivalent** against a Level-60 party.

Optional-content players can legitimately overlevel mandatory ordinary enemies, Elites, and bosses. That is an intended reward for optional engagement.

## Ordinary formation EXP bands — controlling

Formation totals, not per-enemy values:
- Ch1 80 / 100 / 120
- Ch2 210 / 280 / 350
- Ch3 350 / 470 / 590
- Ch4 460 / 610 / 760
- Ch5 640 / 860 / 1,070
- Ch6 760 / 1,020 / 1,280
- Ch7 870 / 1,160 / 1,440
- Ch8 1,020 / 1,360 / 1,700
- Ch9 1,170 / 1,560 / 1,950
- Ch10 1,250 / 1,660 / 2,080
- Ch11 1,390 / 1,850 / 2,320
- Ch12 1,420 / 1,900 / 2,380

Columns are light / standard / heavy. Normal campaign mix target ≈ **25% / 55% / 20%**.

## Regional Hunt recommended player levels — inherited Audit96

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

## Major Hunt recommended player levels — inherited Audit96/Audit95

1. Ashen Whitehorn — 21
2. Crownless Siege Marshal → Crownless War Engine — 27
3. Concordance Guardian — 34
4. Worldscar Leviathan — 46
5. Final Archive Arbiter — 58
6. The Unfinished World → Worldheart — 60

Audit95 unlocks, locations, Prime rewards, boss architecture, and Worldframe dual-gate logic remain unchanged.

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
- Worldframe Depths is inside Final Archives and opens only when both Final Archive Arbiter has been cleared **and** Vaelkor has been defeated.
- The six Major-Hunt bosses sit outside Audit93's 160 chapter-production combat-identity basis; all-in distinct combat-encounter identity count is 166.

## Enemy asset reuse — inherited Audit94

Production targets for the Audit93 160-identity chapter roster:
- roughly 40–45 true/near palette-material swaps;
- roughly 60% / about 96 identities avoid a completely new base sprite/rig through reuse;
- only roughly 20–25 identities should read to players as obvious palette swaps;
- most reuse should be disguised through low-cost gear, material, VFX, animation, pose, or silhouette differentiation;
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
- Chapter 5 — **The Mountain Engine** — remains the next inherited exact scene-production / HD-2D production-audit frontier, but Audit91 requires a beat-level rewrite/reconciliation before line-complete dialogue.
- Chapter 9 route is Larkspire / Equal Mercy → Last Sanctuary → Crownfall invasion → Mercy Is Not Surrender; Rhazek/Bastion Devourer is the mandatory Crownfall climax; Mercyfallen Behemoth is Hunt #9.
- Chapter 11 macro structure remains Audit89-locked: Varkesh capture precedes Forward Hub; Vaelkor two-form climax; post-Vaelkor cleanup; deliberate Chapter 12 launch.
- Chapter 12 remains Audit89-locked: no Regional Hunt; Devourer of Names Elite; Last Weapon Archon mandatory guardian; Reconstituted Entity → The Last Command; modern Final Severance; no third form.

## Implementation boundary after Audit97

Audit97 now locks:
- the EXP formula;
- campaign ordinary-battle baseline;
- campaign-only progression and Chapter 12 entry at 52;
- recommended Chapter 12 launch at 59;
- campaign and optional EXP pools;
- Hunt EXP packages;
- Chapter 12 EXP package;
- ordinary formation reward bands;
- campaign-only relative-strength reference for mandatory combat.

Still open for implementation/playtest:
- per-enemy EXP weights that sum into formation totals;
- exact Hunt route-vs-boss EXP splits where not separately locked;
- raw final HP/Attack/Defense/Magic/Spirit/Speed constants;
- exact area-specific RNG/formation distributions;
- exact placement/identity of the 20,000-EXP optional non-Hunt pool;
- micro-adjustments that preserve the locked cumulative targets.

Omission from this implementation-facing summary does not erase compatible older canon. Exact approved visual masters and newer explicit user corrections always control conflicts.
