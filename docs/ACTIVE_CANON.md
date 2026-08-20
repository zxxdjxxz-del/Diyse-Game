# Diyse — Active Engineering Canon Guardrails

This is an implementation-facing summary. It does **not** replace the authoritative Complete Master Canon or newer explicit user corrections. If this summary conflicts with newer authority, the newer authority wins.

## Current written authority

- **Whole-project root:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.81 / Audit96 — Level Progression, Hunt Difficulty and Encounter Strength Closure**.
- **Date:** August 20, 2026.
- Immediate inherited chain:
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

Current canon files:
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

## Audit96 level progression — controlling

- **Chapter 0 has no player levels and no leveling progression.**
- **Chapter 1 begins at Level 1.**
- Expected progression:
  - Ch1: 1–5
  - Ch2: 5–9
  - Ch3: 9–13
  - Ch4: 13–17
  - Ch5: 17–23
  - Ch6: 23–29
  - Sixfold Accord / Ch7: ~29–35
  - Ch8: 35–41
  - Ch9: 41–47
  - Ch10: 47–54
  - Ch11: ~54–59
  - **Ch12 begins at 59** and occupies the near-cap 59–60 space.
- Chapter 11 therefore begins around **Level 54**.
- Worldframe Depths / The Unfinished World → Worldheart is a **recommended Level-60** challenge. All older Level-50 and provisional Level-58 Worldframe references are superseded.

## Regional Hunt recommended player levels — controlling

1. Cistern Devourer — **7**
2. Transfer Executioner — **11**
3. Archive Judgment Engine — **15**
4. Crown Prototype — **20**
5. Whitehorn Ravager — **26**
6. Winterglass Titan — **32**
7. Rift Gate Colossus — **38**
8. Rift Siege Beast — **44**
9. Mercyfallen Behemoth — **50**
10. Authority Remnant — **57**
11. Throne of Emperor Vaelkor — **60**

The first three sit +2 above associated chapter completion; Hunts #4–#10 sit approximately +3; Hunt #11 is constrained by the Level-60 cap. Recommended levels are readiness targets, not hard access gates.

## Major Hunt recommended player levels — controlling

1. Ashen Whitehorn — **21**
2. Crownless Siege Marshal / Crownless War Engine — **27**
3. Concordance Guardian — **34**
4. Worldscar Leviathan — **46**
5. Final Archive Arbiter — **58**
6. The Unfinished World / Worldheart — **60**

Audit95 unlocks, locations, Prime rewards, boss architecture, and Worldframe dual-gate logic remain unchanged.

## Encounter-strength grammar — controlling

Enemies should generally feel stronger than the party. Expected player level means the party is prepared, not numerically equal.

Internal strength-equivalent benchmarks:
- ordinary enemy: ~+1 over expected player;
- strong ordinary / formation anchor: ~+2;
- named miniboss: ~+2 to +3;
- Elite: ~+3;
- mandatory story boss: ~+4 to +5;
- Regional Hunt: ~+4 over its recommended player level;
- Major Hunt: ~+5 early and ~+6 late;
- Worldframe: Level-60 party versus roughly **67-equivalent** encounter pressure.

These are internal balance references, not displayed enemy levels. They may exceed 60 without creating player Level 61+ progression. Audit96 introduces **no dynamic level scaling**; fixed authored tuning remains the rule.

Broad damage/durability targets are documented in Audit96. Formation synergy and mechanics are preferred over pure HP inflation.

## Enemy / Elite / Hunt role closure — Audit93

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

## Hunt totals and Major Hunt architecture — Audit95

- Exactly **11 Regional Hunts**.
- Exactly **6 Major Hunts**.
- Exactly **17 Hunt-class optional encounters = 11 Regional + 6 Major**.
- Major Hunts are optional and not required to launch Chapter 12.
- Worldframe Depths is inside Final Archives and opens only when both Final Archive Arbiter has been cleared **and** Vaelkor has been defeated.
- The six Major-Hunt bosses sit outside Audit93's 160 chapter-production combat-identity basis; all-in distinct combat-encounter identity count is 166.

## Enemy asset reuse — Audit94

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

## Implementation boundary after Audit96

Audit96 locks target player-level progression and relative encounter pressure. The following remain implementation/balance work:
- exact EXP formulas and per-enemy EXP awards;
- raw final HP/Attack/Defense/Magic/Spirit/Speed constants;
- exact reward EXP and drop values;
- final per-encounter data-table numbers and playtest tuning.

Those values must be derived from Audit96 rather than reopening its level targets or encounter hierarchy.

Omission from this implementation-facing summary does not erase compatible older canon. Exact approved visual masters and newer explicit user corrections always control conflicts.