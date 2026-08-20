# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with newer authority, the newer authority wins.

## Current written authority

- **Whole-project root:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.84 / Audit99 — Random-Encounter Runtime Implementation and Production-Readiness Closure**.
- **Date:** August 20, 2026.
- Immediate inherited chain:
  - v1.83 / Audit98 — Random-Encounter Pressure, Revised EXP Curve and Hunt-Economy Reconciliation;
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
- `docs/canon/AUDIT99_RANDOM_ENCOUNTER_RUNTIME_IMPLEMENTATION_AND_PRODUCTION_READINESS_CLOSURE.md`
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

- Diyse is an **HD-2D JRPG**.
- Field characters target approximately **80 px**; battle characters approximately **200 px**; dialogue uses large high-resolution portraits.
- Standard combat frame: up to four active party members staggered left, enemies right, open center action/VFX lane.
- Target runtime: approximately **25 hours**.
- Platform target: Android / APK, landscape.
- Permanent roster: exactly six; maximum active battle party: four.
- Dialogue is one authored continuity; no dialogue wheel, morality route, affinity-response system, romance route/system, or selectable protagonist personality.
- Absolute player level cap: **60**. No Level 61+, prestige leveling, or separate postgame leveling campaign.
- Cleared-save `WORLD_AFTER` free roam exists; no separate postgame progression campaign.

## Audit98 progression/economy model — inherited and controlling

Audit99 does not change Audit98's progression math.

Campaign-only progression reference:
- Ch0: no levels / no EXP progression;
- Ch1 ~1→5;
- Ch2 ~5→9;
- Ch3 ~9→13;
- Ch4 ~13→17;
- Ch5 ~17→22;
- Ch6 ~22→27;
- Ch7 ~27→32;
- Ch8 ~32→37;
- Ch9 ~37→42;
- Ch10 ~42→**47**;
- Ch11 ~47→**53**;
- Ch12 launch around **53**;
- Ch12 campaign-only completion around **55**.

Descriptive optional/readiness reference:
- End Ch10 most-optional roughly **50–51**;
- Ch12 launch most-optional roughly **56–57**;
- End Ch12 most-optional roughly **59–60**;
- a 100% player may already be **Level 60 before Chapter 12**;
- Worldframe is not required to reach Level 60.

Recommended levels are descriptive readiness references, not hard gates.

## EXP curve — inherited Audit98

Levels 1–17 retain:

**Cumulative EXP(L) = 100 × (L − 1)^2**

From L17→18 onward:
- base increment = `100 × (2L − 1)`;
- multiplier = `1 + 0.35 × (L − 17) / 42` for L≥17;
- implementation rounds the final level-up cost **half-to-even to the nearest 100 EXP** so the locked milestone table is reproduced exactly.

Key totals:
- L17 25,600;
- L22 44,400;
- L27 69,300;
- L32 100,600;
- L37 138,800;
- L42 184,300;
- L47 237,600;
- L50 273,500;
- L53 312,400;
- L54 326,000;
- L55 340,000;
- L56 354,400;
- L59 399,600;
- L60 415,400.

## Campaign random-battle pacing — inherited Audit98

Expected mandatory-route ordinary random encounters:
- Ch1 18; Ch2 19; Ch3 19; Ch4 19; Ch5 20; Ch6 19; Ch7 19; Ch8 18; Ch9 16; Ch10 17; Ch11 18; Ch12 8.
- Total = **approximately 210 expected**, never a fixed quota.

The 210 excludes Hunt-route combat, Major-Hunt destination combat, other optional/backtracking combat, Elites, named encounters, bosses, Hunts, and Chapter 0 authored tutorial encounters.

There is no hidden exit catch-up quota.

## Random encounter pressure — design and implementation controlling

Random encounters remain random and use hidden **eligible-movement-distance pressure**.

- pressure comes from actual resolved horizontal displacement after collision resolution;
- standing still does not count;
- wall-pushing with zero displacement does not count;
- vertical-only displacement does not count;
- movement-disabled displacement does not count;
- menus/cutscenes/dialogue/authored pauses suspend pressure;
- sprinting cannot reduce encounters per unit distance;
- no encounter can trigger before approximately 0.35S;
- trigger chance rises in 0.10S checks to 80% at 1.65S+;
- there is no hard forced encounter;
- victory resets pressure;
- successful flee resumes near 0.65S with 0.20S grace;
- failed flee does not reset accumulated pressure;
- exact consecutive formation repeats are suppressed when alternatives exist.

Selection flow:

**pressure trigger → area → Light/Standard/Heavy → weighted local formation pool**

## Active-enemy cap — controlling

Maximum **8 simultaneously active enemies**.

True summons/adds count toward 8; VFX-only entities do not. Reinforcements may enter after space opens, so total participants over the whole fight may exceed 8 while simultaneous active enemies may not.

Typical chapter formation grammar remains:
- Ch1 2–3, max 4;
- Ch2 3–4, max 4;
- Ch3 3–4, max 5;
- Ch4 4–5, max 6;
- Ch5 5–6, max 7;
- Ch6 5–7, max 8;
- Ch7–11 generally 6–8, max 8;
- Ch12 generally 5–8, max 8.

## Optional EXP economy — inherited Audit98

Pre-Chapter-12 optional leveling pool = **107,100 EXP**:
- 11 Regional Hunts + Hunt-route combat = **46,700**;
- Major Hunts #1–#5 + route/destination combat = **40,400**;
- other optional/backtracking combat = **20,000**.

Worldframe is excluded from the EXP needed to prove Level-60 reachability.

Regional Hunt packages:
1. Cistern Devourer — 1,000
2. Transfer Executioner — 1,500
3. Archive Judgment Engine — 1,900
4. Crown Prototype — 2,200
5. Whitehorn Ravager — 2,700
6. Winterglass Titan — 3,400
7. Rift Gate Colossus — 4,500
8. Rift Siege Beast — 6,000
9. Mercyfallen Behemoth — 6,800
10. Authority Remnant — 7,900
11. Throne of Emperor Vaelkor — 8,800

Major Hunt packages before Worldframe:
1. Ashen Whitehorn — 4,200
2. Crownless Siege Marshal → Crownless War Engine — 5,000
3. Concordance Guardian — 5,900
4. Worldscar Leviathan — 12,300
5. Final Archive Arbiter — 13,000

## Hunt totals / fixed-difficulty rules — inherited

- Exactly **11 Regional Hunts**.
- Exactly **6 Major Hunts**.
- Exactly **17 Hunt-class optional encounters**.
- No dynamic level scaling.
- Hunt recommended levels are readiness references, not access gates.
- Worldframe Depths opens only after both Final Archive Arbiter clear and Vaelkor defeat.
- Chapter 12 has no Regional Hunt.

Regional recommended levels: 7 / 11 / 15 / 20 / 26 / 32 / 38 / 44 / 50 / 57 / 60.

Major recommended levels: 21 / 27 / 34 / 46 / 58 / 60.

## Audit99 runtime implementation closure — controlling

The tested runtime chain now exists through:

**resolved player movement**
→ eligible horizontal distance
→ area S conversion
→ Audit98 pressure
→ L/S/H tier
→ weighted legal formation
→ anti-repeat
→ transient encounter payload
→ generated 1–8-enemy battle state
→ victory/engineering flee
→ field return with pressure restoration.

The following are implemented and no longer considered pending:
- Audit98 balance/runtime helper layer;
- reusable field encounter controller;
- actual post-collision eligible-distance feed;
- generated random-formation battle-state adapter;
- transient field → combat → field random-encounter handoff;
- reusable area encounter-tuning Resource;
- area ecology transition behavior.

## Area encounter-tuning contract — controlling

Area tuning contains:
- tuning ID;
- chapter;
- random-area ID;
- `world_units_per_s`;
- enabled/disabled state;
- entry transition mode;
- calibration state.

Calibration states:
- `engineering_only`;
- `awaiting_geometry`;
- `production_calibrated`.

An enabled area may not remain `awaiting_geometry`.

Transition modes:
- **same ecology:** preserve pressure; no extra grace;
- **new ecology:** preserve pressure and add **0.10S** ecology-transition grace;
- **safe reset:** clear pressure, grace, and immediate anti-repeat history.

The current Greenhollow proof value **20 world units = 1S** is engineering-only and non-canon.

## Transient encounter/save boundary — controlling

Current generated random encounters use runtime-only transient encounter state across scene transitions.

- transient encounter request/return state is not serialized;
- loading a save clears stale transient encounter state;
- encounter-pressure persistence itself remains a future dedicated save-schema decision.

## Chapter 1–4 random formation implementation status

Current executable local random-formation catalogs exist for exactly these 10 areas:

Chapter 1:
- `ch01_brackenwall`
- `ch01_greenhollow`
- `ch01_hollow_watch`

Chapter 2:
- `ch02_dunmere_waterworks`
- `ch02_sunken_archive`
- `ch02_red_transfer_bastion`

Chapter 3:
- `ch03_way_fort`
- `ch03_suppressed_archives`
- `ch03_command_station`

Chapter 4:
- `ch04_reaction_annex`

These use approved ordinary/carryover enemy identities, exclude authored non-random categories, obey active-enemy caps, and use Audit98 formation EXP anchors.

## Enemy production boundary — controlling status

Enemy architecture/identity planning is substantially closed by Audits 90/93/94/95/96/98.

Still open unless separately locked at narrower scope:
- final ordinary-enemy HP/Attack/Defense/Magic/Spirit/Speed;
- final ordinary-enemy move kits;
- final AI priorities/reactions;
- final elemental/status weakness/resistance tables;
- final drops/materials/gold;
- Chapters 5–12 random-formation catalogs;
- final Elite executable packages;
- final Regional/Major Hunt executable packages;
- final mandatory-boss executable packages;
- final enemy sprites/animations/hit/death/VFX hookup;
- 4-party + 8-enemy target-Android performance tuning.

Current Greenhollow proof enemy stats are **engineering-only, non-canon, and not final balance**.

## Enemy asset reuse — inherited Audit94

For the Audit93 160-identity chapter roster:
- roughly 40–45 true/near palette-material swaps;
- roughly 60% / about 96 identities should avoid a completely new base sprite/rig through reuse;
- only roughly 20–25 should read to players as obvious palette swaps;
- shared assets never imply shared lore identity.

## Item/equipment production boundary — Audit99

Audit99 does not invent a new item catalog.

Compatible earlier equipment-system rules remain inherited, including:
- open equipment and persistent unlocked abilities;
- Subclass selection controlling its stat package, Trait, and Subclass-only abilities;
- donor / Legacy architecture;
- Legacy equipment bonuses applying to any legal wearer;
- Nimera's Conduit concept;
- Torren Routeweaver's inherited access to the relevant Nimera Base equipment concept;
- Cards remaining separate from normal inventory/equipment.

The **production item catalog/economy remains open** unless an individual item is separately locked elsewhere.

The next dedicated item audit must resolve:
- item taxonomy and practical total count;
- consumables;
- weapon progression;
- armor;
- accessories;
- Conduits;
- Legacy production stats where open;
- materials/drop economy;
- shops and prices;
- treasure/chest distribution;
- sell values;
- status cures/use restrictions;
- Hunt/boss non-EXP item rewards;
- crafting/upgrade rules only if retained after audit;
- item IDs/icons/descriptions/sorting/runtime/save representation.

No large genre-conventional item count or crafting system is canon by assumption.

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
- Chapter 9 route remains Larkspire / Equal Mercy → Last Sanctuary → Crownfall invasion → Mercy Is Not Surrender; Rhazek/Bastion Devourer is the mandatory Crownfall climax; Mercyfallen Behemoth is Hunt #9.
- Chapter 11 remains Audit89-locked: Varkesh capture precedes Forward Hub; Vaelkor two-form climax; post-Vaelkor cleanup; deliberate Chapter 12 launch.
- Chapter 12 remains Audit89-locked: no Regional Hunt; Devourer of Names Elite; Last Weapon Archon mandatory guardian; Reconstituted Entity → The Last Command; modern Final Severance; no third form.

## Current production readiness / next frontier

The repository does **not** yet contain Chapter 1–4 final production traversal `.tscn` maps with real authored geometry suitable for production S calibration.

Therefore still open:
- first reusable production traversal-scene shell;
- first production map geometry and real `world_units_per_s` calibration;
- production enemy combat-data schema/final-stat methodology;
- Chapters 1–4 final ordinary-enemy combat data;
- Chapters 5–12 local formation catalogs;
- Elite/Hunt/boss executable production packages;
- full item/equipment catalog and economy audit;
- encounter-pressure save persistence if later desired;
- final flee-success/player-facing UI;
- final defeat/game-over behavior;
- target-Android high-density battle performance pass.

Omission from this implementation-facing summary does not erase compatible older canon. Exact approved visual masters and newer explicit user corrections always control conflicts.
