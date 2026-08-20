# Audit98 — Random-Encounter Pressure, Revised EXP Curve and Hunt-Economy Reconciliation

**Authority:** Diyse: HD-2D JRPG Clean Active Complete Master Canon **v1.83 / Audit98**  
**Date:** August 20, 2026  
**Status:** **LOCKED / CONTROLLING** for campaign ordinary-random-battle density, hidden encounter-pressure behavior, maximum active enemy count, the Chapter-5-onward character EXP curve, revised campaign-only progression, normalized Hunt EXP packages, optional-progression interpretation, and Worldframe exclusion from Level-60 reachability math.

Audit98 inherits all compatible v1.82/Audit97, v1.81/Audit96, v1.80/Audit95, v1.79/Audit94, v1.78/Audit93, and earlier canon unless explicitly superseded below.

## 0. Authority contract

Audit98 changes progression/economy and random-encounter pacing only. It does **not** rewrite story, dialogue, Hunt identities, locked Hunt unlock gates, protected Cards/Primes, boss forms/mechanics, enemy-production identity counts, fixed-authored encounter strength, the Level-60 cap, or the four-active-party limit.

Where Audit98 conflicts with Audit97's 165-battle baseline, unchanged quadratic late-game EXP curve, campaign-only Chapter-12 entry at Level 52, old Hunt package totals, old ordinary formation reward bands, or any exact arithmetic interpretation of optional/recommended levels, **Audit98 supersedes those statements**.

## 1. Campaign ordinary-random-battle baseline

The mandatory campaign route targets approximately **210 ordinary random encounters across Chapters 1–12**.

This is an expected first-time traversal center, not a fixed quota. A real run may finish above or below it.

| Chapter | Expected campaign ordinary encounters |
|---:|---:|
| Ch1 | 18 |
| Ch2 | 19 |
| Ch3 | 19 |
| Ch4 | 19 |
| Ch5 | 20 |
| Ch6 | 19 |
| Ch7 | 19 |
| Ch8 | 18 |
| Ch9 | 16 |
| Ch10 | 17 |
| Ch11 | 18 |
| Ch12 | 8 |
| **Total** | **210** |

The 210 includes mandatory-route travel, fields, roads, dungeons, fortresses, and other story traversal. It excludes Regional-Hunt route combat, Major-Hunt route/destination combat, other optional/backtracking ordinary combat, Elites, minibosses, named encounters, story bosses, Hunts, and Chapter-0 authored tutorial battles.

There is no hidden exit quota and no forced catch-up encounter before leaving an area.

## 2. Hidden encounter-pressure system

Random encounters remain random. Diyse uses a hidden **eligible-movement-distance** pressure system rather than flat independent per-step RNG.

- standing still creates no pressure;
- menus, cutscenes, dialogue, and authored pauses suspend pressure;
- sprinting must not reduce encounter frequency per unit of distance;
- victory resets pressure and begins a grace period;
- long droughts become increasingly unlikely;
- immediate back-to-back encounters are suppressed;
- exploration and backtracking naturally create more battles.

Using normalized spacing variable **S**, no encounter can trigger before approximately **0.35S**. Checks then occur around each additional 0.10S:

| Effective spacing | Trigger chance |
|---:|---:|
| <0.35S | 0% |
| 0.35S | 3% |
| 0.45S | 4% |
| 0.55S | 6% |
| 0.65S | 8% |
| 0.75S | 10% |
| 0.85S | 13% |
| 0.95S | 17% |
| 1.05S | 22% |
| 1.15S | 28% |
| 1.25S | 36% |
| 1.35S | 46% |
| 1.45S | 58% |
| 1.55S | 70% |
| 1.65S+ | 80% |

Target mean spacing is approximately **1.00S** with no hard forced encounter.

Successful flee does not fully reset pressure: grant about 0.20S grace, then resume near an effective ~0.65S pressure state; block the exact same formation once when alternatives exist. Failed flee does not reset pressure.

Same-ecology transitions preserve pressure. Safe rooms may reset. Authored battle mode and random battle pressure must not stack.

## 3. Random formation selection

Encounter selection flow is:

**pressure trigger → current area → Light / Standard / Heavy roll → weighted local formation pool**

The same exact formation should not repeat consecutively when alternatives exist. Formation lists are weighted local pools, not deterministic fight IDs.

## 4. Maximum active enemies

Maximum simultaneously active enemies: **8**.

- true summons/adds count toward 8;
- purely visual/VFX entities do not;
- reinforcements may enter after space opens;
- total participants over the whole battle may exceed 8, but active enemies at one time may not.

With four active party members, the normal primary runtime ceiling is 12 combatants.

Working formation-size grammar:

| Chapter | Typical formation | Maximum |
|---:|---|---:|
| Ch1 | 2–3 | 4 |
| Ch2 | 3–4 | 4 |
| Ch3 | 3–4 | 5 |
| Ch4 | 4–5 | 6 |
| Ch5 | 5–6 | 7 |
| Ch6 | 5–7 | 8 |
| Ch7 | 6–7 | 8 |
| Ch8 | 6–8 | 8 |
| Ch9 | 6–8 | 8 |
| Ch10 | 6–8 | 8 |
| Ch11 | 6–8 | 8 |
| Ch12 | 5–8 | 8 |

Late-game difficulty escalates through role synergy, reactions, protection, control, reinforcements, states, and target priority rather than >8 bodies.

## 5. Revised character EXP curve

Levels 1–17 retain the original quadratic cumulative curve:

**Cumulative EXP(L) = 100 × (L − 1)^2**

Beginning with the Level-17→18 level-up, cost accelerates gradually.

For level-up **L→L+1** where **L≥17**:

1. base quadratic increment = **100 × (2L − 1)**;
2. multiplier = **1 + 0.35 × (L − 17) / 42**;
3. round the final level-up cost to the nearest 100 EXP.

The multiplier therefore rises from **1.00× at L17** to **1.35× at L59**.

Key cumulative milestones:

| Level | Cumulative EXP |
|---:|---:|
| 17 | 25,600 |
| 22 | 44,400 |
| 23 | 48,900 |
| 27 | 69,300 |
| 32 | 100,600 |
| 37 | 138,800 |
| 42 | 184,300 |
| 47 | 237,600 |
| 50 | 273,500 |
| 53 | 312,400 |
| 54 | 326,000 |
| 55 | 340,000 |
| 56 | 354,400 |
| 57 | 369,100 |
| 58 | 384,200 |
| 59 | 399,600 |
| 60 | 415,400 |

The Level-60 cap remains absolute. EXP at Level 60 creates no Level 61+, prestige, or overflow-level system.

## 6. Campaign-only progression and chapter EXP budgets

Campaign-only means mandatory story content plus normal campaign-route random encounters, with no Hunts, Hunt-route combat, or other optional/backtracking combat.

| Chapter | Campaign-only completion | Chapter EXP budget |
|---:|---:|---:|
| Ch1 | ~5 | 1,600 |
| Ch2 | ~9 | 4,800 |
| Ch3 | ~13 | 8,000 |
| Ch4 | ~17 | 11,200 |
| Ch5 | ~22 | 18,800 |
| Ch6 | ~27 | 24,900 |
| Ch7 | ~32 | 31,300 |
| Ch8 | ~37 | 38,200 |
| Ch9 | ~42 | 45,500 |
| Ch10 | **~47** | **53,300** |
| Ch11 | **~53** | **74,800** |
| Ch12 | **~55** | **34,800** |

Cumulative campaign targets:
- end Ch10 = **237,600 EXP / ~Level 47**;
- end Ch11 / Chapter-12 launch = **312,400 EXP / Level 53 threshold**;
- expected end Ch12 = **~347,200 EXP**, approximately mid-Level 55.

Mandatory story content is balanced to remain completable on this campaign-only curve.

## 7. Campaign ordinary-formation EXP bands

Formation rewards are whole-formation payouts, not fixed per-enemy values. Individual authored formations may vary around these anchors as long as the weighted chapter/area expectation stays on budget.

| Ch. | Light | Standard | Heavy | Chapter weights L/S/H | Expected ordinary EXP pool |
|---:|---:|---:|---:|---:|---:|
| 1 | 45 | 55 | 70 | 25/55/20 | 1,000 |
| 2 | 130 | 165 | 200 | 25/55/20 | 3,100 |
| 3 | 215 | 280 | 315 | 22/55/23 | 5,200 |
| 4 | 315 | 375 | 460 | 20/55/25 | 7,300 |
| 5 | 460 | 610 | 710 | 18/55/27 | 12,200 |
| 6 | 650 | 850 | 995 | 18/55/27 | 16,200 |
| 7 | 830 | 1,050 | 1,250 | 17/55/28 | 20,300 |
| 8 | 1,070 | 1,360 | 1,600 | 17/55/28 | 24,800 |
| 9 | 1,480 | 1,825 | 2,265 | 22/55/23 | 29,600 |
| 10 | 1,835 | 2,300 | 2,640 | 19/55/26 | 39,100 |
| 11 | 2,075 | 2,600 | 3,100 | 22/55/23 | 46,800 |
| 12 | 2,080 | 2,600 | 3,120 | 22.5/55/22.5 | 20,800 |

Current named/story pools are the remainder of each chapter budget. Chapters 5–12 use:
- Ch5 6,600;
- Ch6 8,700;
- Ch7 11,000;
- Ch8 13,400;
- Ch9 15,900;
- Ch10 14,200;
- Ch11 28,000;
- Ch12 14,000.

Audit97's old ordinary-formation bands and dependent chapter ordinary pools are superseded.

## 8. Recommended/optional levels are descriptive

Recommended levels are readiness references, not hard access gates, exact delivery obligations, or mandatory-story balance requirements.

Late-game descriptive spine:

| Progress point | Campaign-only | Most optional | 100% behavior |
|---|---:|---:|---:|
| End Ch10 | ~47 | **~50–51** | above that depending on completion |
| End Ch11 / Ch12 launch | ~53 | **~56–57** | **may be 60** |
| End Ch12 | ~55 | **~59–60** | 60 |

A 100% player is explicitly allowed to reach **Level 60 before Chapter 12**.

## 9. Hunt access versus natural clear

A Hunt becoming available does not imply that a campaign-only player is expected to clear it immediately. Hunts retain fixed authored strength and recommended readiness levels. Returning later can naturally make them easier because there is no dynamic level scaling.

Representative natural campaign-only tendencies:

### Regional Hunts
- Cistern Devourer — Ch2-ish.
- Transfer Executioner — Ch3-ish.
- Archive Judgment Engine — Ch4-ish.
- Crown Prototype — Ch5-ish.
- Whitehorn Ravager — Ch6-ish.
- Winterglass Titan — Ch7 / early Ch8.
- Rift Gate Colossus — late Ch8 / early Ch9.
- Rift Siege Beast — late Ch9 / early Ch10.
- Mercyfallen Behemoth — Ch11-ish.
- Authority Remnant — late Ch11 / cleanup.
- Throne of Emperor Vaelkor — late Ch11 / cleanup.

### Major Hunts
- Ashen Whitehorn — Ch5-ish.
- Crownless Siege Marshal → Crownless War Engine — Ch6-ish.
- Concordance Guardian — Ch7 / Ch8.
- Worldscar Leviathan — Ch10-ish.
- Final Archive Arbiter — late Ch11 / cleanup.
- The Unfinished World → Worldheart — final cleanup / completionist.

These are descriptive tendencies only and do not change locked access gates.

## 10. Normalized Regional-Hunt EXP packages

Package totals include the Hunt boss plus expected ordinary combat unique to its optional route.

| # | Regional Hunt | Recommended Lv. | EXP package |
|---:|---|---:|---:|
| 1 | Cistern Devourer | 7 | **1,000** |
| 2 | Transfer Executioner | 11 | **1,500** |
| 3 | Archive Judgment Engine | 15 | **1,900** |
| 4 | Crown Prototype | 20 | **2,200** |
| 5 | Whitehorn Ravager | 26 | **2,700** |
| 6 | Winterglass Titan | 32 | **3,400** |
| 7 | Rift Gate Colossus | 38 | **4,500** |
| 8 | Rift Siege Beast | 44 | **6,000** |
| 9 | Mercyfallen Behemoth | 50 | **6,800** |
| 10 | Authority Remnant | 57 | **7,900** |
| 11 | Throne of Emperor Vaelkor | 60 | **8,800** |
| **Total** |  |  | **46,700** |

Working route expectation for package planning:
- Regional #1–#3: about **2** route encounters;
- Regional #4–#11: generally **1–2**, planning mean about **1.5**;
- actual fights remain random and geometry-driven, never quota-driven.

## 11. Normalized Major-Hunt EXP packages

| # | Major Hunt | Recommended Lv. | EXP package |
|---:|---|---:|---:|
| 1 | Ashen Whitehorn | 21 | **4,200** |
| 2 | Crownless Siege Marshal → Crownless War Engine | 27 | **5,000** |
| 3 | Concordance Guardian | 34 | **5,900** |
| 4 | Worldscar Leviathan | 46 | **12,300** |
| 5 | Final Archive Arbiter | 58 | **13,000** |
| **Total before Worldframe** |  |  | **40,400** |

Working Major route centers are approximately 3 / 3 / 3 / 4 / 3 encounters for #1–#5 respectively.

Major Hunt #6 — **The Unfinished World → Worldheart** — remains a Level-60 challenge and is excluded from the EXP needed to prove Level-60 reachability.

## 12. Other optional/backtracking combat

Retain **20,000 EXP across approximately 18 optional ordinary battles**. Exact identities/routes must attach to real optional spaces rather than being invented solely to satisfy arithmetic.

## 13. Total pre-Ch12 optional leveling pool

- Regional Hunts = **46,700**;
- Major Hunts #1–#5 = **40,400**;
- other optional/backtracking combat = **20,000**;
- total = **107,100 EXP**.

Worldframe is excluded.

This is a planning/economy budget, not a guarantee that every player receives it before the final operation. Actual acquisition varies with optional choices, Hunt readiness, route RNG, backtracking, and Level-60 cap waste.

## 14. Validation

100,000-run stochastic validation supports:

### Campaign-only
- end Ch10 ~47;
- Chapter-12 launch ~53;
- end Ch12 ~55;
- expected campaign ordinary count mean ~210 with SD ~4.8;
- final level distribution strongly centered on Level 55.

### Most optional
At roughly four-fifths optional completion:
- end Ch10 ~50–51;
- Chapter-12 launch ~56–57;
- end Ch12 ~59–60.

### 100% completionist
- many runs reach Level 60 during late Chapter 11 / cleanup;
- roughly seven in ten tested runs were already Level 60 before Chapter 12;
- remaining runs were generally Level 59 and reached Level 60 naturally during Chapter 12;
- Worldframe was not required.

These validation results support the descriptive, not prescriptive, interpretation of recommended levels.

## 15. Mandatory encounter-strength interpretation

Fixed authored tuning remains the rule; there is no dynamic level scaling.

Mandatory combat uses the revised campaign-only progression as its reference. Preserve the relative grammar:
- ordinary enemy ≈ +1 equivalent;
- strong ordinary / formation anchor ≈ +2;
- named miniboss ≈ +2 to +3;
- Elite ≈ +3;
- mandatory story boss ≈ +4 to +5.

Any Audit97 mandatory-strength table that specifically assumes campaign-only Chapter-12 entry at Level 52 is superseded; exact fixed late-game strength numbers should be authored against the revised ~53 launch reference.

Optional challenge rules remain compatible:
- Regional Hunt ≈ recommended level +4;
- Major Hunt ≈ +5 early / +6 late;
- Worldframe ≈ ~67-equivalent against a Level-60 party.

## 16. Explicit supersessions

Audit98 supersedes:
- Audit97's **165** expected campaign ordinary-battle baseline and 165±8 interpretation;
- Audit97's unchanged quadratic character EXP curve above Level 17;
- Audit97's campaign-only Chapter-12 entry at **Level 52**;
- Audit97's old campaign chapter EXP allocations where they conflict with Section 6;
- Audit97's old ordinary formation EXP bands where they conflict with Section 7;
- Audit97's Regional Hunt pool **42,000** and package table;
- Audit97's Major Hunt #1–#5 pool **43,000** and package table;
- Audit97's pre-Ch12 optional total **105,000**;
- any interpretation that recommended levels are exact arithmetic requirements;
- any provisional formation concept requiring more than 8 simultaneously active enemies.

Audit98 replaces those with:
- ~210 expected campaign ordinary encounters;
- the distance-based encounter-pressure architecture;
- an 8-active-enemy hard maximum;
- Chapter-5-onward gradual EXP acceleration;
- campaign-only Chapter-12 launch around Level 53;
- Regional Hunt pool **46,700**;
- Major Hunt #1–#5 pool **40,400**;
- pre-Ch12 optional pool **107,100**;
- descriptive optional-level bands;
- explicit completionist pre-Ch12 Level-60 allowance.

## 17. Inherited authority preserved

Audit98 preserves all compatible authority for:
- exactly 11 Regional Hunts;
- exactly 6 Major Hunts;
- exactly 17 Hunt-class optional encounters;
- Audit95 Major Hunt identities, unlocks, locations, forms, and Prime rewards;
- Audit92 Mercyfallen Behemoth / Larkspire route;
- Audit89 Throne of Emperor Vaelkor role and cleanup availability;
- Chapter 12 having no Regional Hunt;
- Worldframe's dual gate;
- fixed authored encounter strength and no dynamic scaling;
- Level-60 cap;
- maximum four active permanent party members;
- random encounters remaining random.

**END AUDIT98**
