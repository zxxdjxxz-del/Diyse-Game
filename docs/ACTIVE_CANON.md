# Diyse — Active Engineering Canon Guardrails

This file is the implementation-facing authority index and compact guardrail summary. It does **not** replace the canon audits. Compatible older locks remain active where not superseded. If this file conflicts with a later explicit approved correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.08 / Audit123 — Class MP, CEXP, Mastery, and Late-Game Progression Lock**  
**Date:** August 27, 2026

Current newest authority chain:
- **v2.08 / Audit123** — current class Ability MP costs, 6,000-CEXP CL13 curve, chapter CEXP envelopes, exact 8-point Mastery schedule, restored late-game player-level spine, late mandatory EXP budgets, and late enemy bands.
- **v2.07 / Audit122** — Base Hit/Evasion resolver and current Bleed lifecycle.
- **v2.06 / Audit121** — system removals, current classes/Faces, final Legacy set, Relic stale-mechanic cleanup, 20-consumable economy/placement, commerce/location terminology, Chapter-4 four-element rework, and Prime numeric sync.
- **v2.05 / Audit120** — compatible direct-damage and Critical Hit rules.
- **v2.04 / Audit119** — compatible Card/Prime MP, named resistance, Prime status/scaling, and other progression architecture not superseded later.
- **v2.03 / Audit118** — exact 38/38 ordinary-equipment source/numeric catalog and compatible Relic/Forge data.
- **v2.02 / Audit117** — compatible equipment/Legacy/class-access structure and Synthesis removal.
- **v2.01 / Audit116** — compatible Standard-Card and Prime command definitions.
- **v2.00 / Audit115** — compatible status/element/Ruin/class-Ability definitions.
- **v1.98 / Audit113** — current 13-chapter reindex.

Primary domain files:
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md`
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md`
- `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`
- `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Historical cumulative trackers are design history, not authority by themselves.

---

# Universal combat firewall

Physical direct damage:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical direct damage:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Hybrid actions resolve authored Physical and Magical components independently. Same-axis penetration caps at 75%. Spirit is the canonical magical-defense stat.

## Base Hit / Evasion
There is no natural Accuracy stat.

> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

Standard authoring: ~100 Base Hit; heavy 90–95; precision 105–115; exceptional precision may reach ~120.

## Critical Hits
- base Crit Chance 5%;
- flat percentage-point bonuses;
- ordinary random Crit cap 50%;
- eligible Crit multiplier 1.5×;
- Crit does not bypass Defense/Spirit.

## Removed systems
- **Barrier does not exist.**
- **Brace does not exist.**
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

## Bleed
Bleed damages each round and again when the affected character acts. It clears only on full-HP restoration, an eligible harmful-status clear, or an eligible item. Partial healing/Regen does not remove it unless full HP is reached or a valid status clear is included.

---

# Current classes / Faces

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Base and Subclass caps are CL13. No Subclass before Sixfold Volition at end Ch7.

## Class Ability MP
Audit123 closes the 12/12 MP certification with no new base-cost changes. Current certified tables in Audit123 are implementation authority.

General bands:
- routine class actions ~10–24 MP;
- premium non-Ultimates ~26–40 MP;
- class Ultimates 52–64 MP;
- Standard Cards 18–48 MP;
- Prime Invocation 50 / 80 / 90 MP.

---

# CEXP / Mastery / player progression — Audit123

## CEXP
Base and Subclass CEXP are separate. Selected class gets 100% of awarded CEXP; unselected class gets 0. CEXP sent to an already capped class is lost.

CL13 cumulative threshold = **6,000 CEXP**.

Pre-Volition Ch1–7 campaign CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch8–12 total 8,500
- Ch13 catch-up/overflow 1,500

Normal full Base + Subclass Class-Level completion occurs during Ch12. Seyrik remains the limiting case around end Ch12.

## Mastery
Synthesis is removed.

Exactly:
- 4 Core Masteries;
- 4 Subclass Masteries;
- 8 active nodes;
- 8 automatic Mastery Points.

Core eligibility = Base CL3 / 6 / 9 / 12.
Subclass eligibility = CL3 / 5 / 7 / 11.

Exact automatic point grants:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

No ninth point. No Lv70 surplus point.

Subclass Mastery 3 purchase grants donor Relic access; Subclass Mastery 4 purchase grants donor Legacy access. The actual donor item must already have been obtained. No duplicate artifact and no universal off-owner nerf.

## Player-level spine
Player level cap = 70. Chapter 0 grants no levels.

Mandatory-route anchors:
- End Ch1 Lv5
- End Ch2 Lv9
- End Ch3 Lv13
- End Ch4 Lv17
- End Ch5 Lv22
- End Ch6 Lv27
- End Ch7 / Volition Lv32
- End Ch8 Lv37
- End Ch9 Lv42
- End Ch10 Lv47
- End Ch11 Lv52
- End Ch12 Lv57
- **Last Shelter Lv60**
- **End Ch13 Lv62**

Desired late sequence:
1. class levels complete during Ch12 / roughly Lv53–57;
2. final Mastery-board point arrives around Last Shelter / Lv60;
3. normal campaign ends around Lv62;
4. Lv62–70 remains optional/completionist headroom.

Key cumulative player EXP:
- Lv32 100,600
- Lv37 138,800
- Lv42 184,300
- Lv47 237,600
- Lv52 299,100
- Lv57 369,100
- Lv60 415,400
- Lv62 448,100
- Lv70 594,100

Late mandatory EXP:
- Ch8 38,200
- Ch9 45,500
- Ch10 53,300
- Ch11 61,500
- Ch12 70,000
- Ch13 pre-Last-Shelter 46,300
- Ch13 post-Last-Shelter 32,700

Late ordinary enemy bands:
- Ch8 Lv32–37
- Ch9 Lv37–42
- Ch10 Lv42–47
- Ch11 Lv47–52
- Ch12 Lv52–57
- Ch13 pre-Shelter Lv57–60
- Ch13 post-Shelter Lv60–62

Expected ordinary random-encounter planning center remains 225 total; Chapter 4 remains 19. These are planning centers, not quotas.

Still open:
- optional player EXP source-by-source re-certification;
- Light/Standard/Heavy formation EXP;
- exact formation CEXP allocation;
- named/story EXP and CEXP package placement;
- progression-dependent raw-stat recertification.

---

# Equipment / items

Current active equipment catalog:
- 38 ordinary equipment
- 36 Relics
- 17 native Legacies
- **91 total equipment pieces**

Hierarchy: Ordinary < Relic < Legacy.

All 17 native Legacies are mechanically final under Audit121. Linked donor use shares the donor's actual item.

Current consumables = **20**. Currency = **Auren**. `1 economy unit = 20 Auren`.

Fixed Salves:
- Field 250 HP / 20 Auren
- Restorative 750 HP / 50 Auren
- Vital 1,500 HP / 120 Auren
- Grand 2,250 HP / 240 Auren

Company Salve = 30% Max HP party-wide.

MP restoratives:
- Flow 50 MP
- Deepflow 80 MP
- Highflow 120 MP
- Reservoir 75% Max MP, reward-only.

Emergency Kit and Emergency Rally remain reward-only under Audit121.

Regional Markets:
- Brackenwall
- Dunmere
- Caelora
- Ivorybridge
- Stonewake
- Frostmere
- Westguard
- Larkspire
- Cerythvale

Cresthaven Quartermaster remains the full normal-stock consolidation endpoint. Vhalmarch is forward supply/requisition after capture, not a civilian Regional Market.

---

# Standard Cards / Primes

Exactly 24 Standard Cards; maximum 3 equipped per character. Cards are reusable and MP-consuming.

Current Acuity quartet:
- Faultline Sight
- Measured Response
- Predicted Impact
- Decisive Interval

Predicted Impact:
- one enemy
- Magical / Colorless
- Power 180
- Base Hit 110
- 28 MP
- 30% Stun

Exactly 12 Primes: 6 Story + 6 Major Hunt.

Prime progression = **Recovered → Awakened** only.

Invocation MP:
- Recovered Story 50
- Awakened Story 80
- Awakened Major Hunt 90
- manifested commands 0 additional MP.

Prismatic Deluge = 90×4 / 360 total listed Power per target.
Regulator Fang = 250 Power / 25% Spirit penetration.

---

# Chapter 4 four-element firewall

Chapter 4 uses exactly:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed from the research/regulation framework. The Seventh Reaction is emergent four-element system behavior, not a seventh element.

Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers with exactly two active/targetable at once.

The live S022–S026 Markdown scripts and matching dialogue `.tres` resources are synchronized to the four-element rework. Historical `SIXFOLD` runtime IDs may remain only as legacy technical compatibility keys and are not player-facing canon.

---

# Implementation rule

When a live implementation file conflicts with Audit123/Audit122/Audit121 in their respective domains, update the implementation file. Do not revive stale Synthesis, Barrier, Brace, six-element Chapter-4, retired class names, old Resource-face, old Bleed-clearing, or Lv62-at-end-Ch12 assumptions from historical trackers.
