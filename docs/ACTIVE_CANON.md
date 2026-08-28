# Diyse — Active Engineering Canon Guardrails

This file is the implementation-facing authority index and compact guardrail summary. It does **not** replace the canon audits. Compatible older locks remain active where not superseded. If this file conflicts with a later explicit approved correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.12 / Audit127 — Chapters 5–8 Named/Story EXP+CEXP Placement Lock**  
**Date:** August 27, 2026

Newest authority chain:
- **v2.12 / Audit127** — exact mandatory named/story player-EXP + CEXP placement for Chapters 5–8.
- **v2.11 / Audit126** — exact mandatory named/story player-EXP + CEXP placement for Chapters 1–4.
- **v2.10 / Audit125** — mandatory ordinary-vs-authored player-EXP allocation, Ch9–13 formation EXP anchors, formation CEXP bands, chapter named/story CEXP envelopes, Ch12 formation rebase.
- **v2.09 / Audit124** — fixed authored optional-player-EXP packages, 195,000 pre-Last-Shelter cap-proof pool, Level-70 completionist proof, and diminishing-return firewall.
- **v2.08 / Audit123** — class Ability MP, 6,000-CEXP CL13 curve, chapter CEXP envelopes, exact 8-point Mastery schedule, restored player-level spine, late mandatory EXP budgets and enemy bands.
- **v2.07 / Audit122** — Base Hit/Evasion and current Bleed lifecycle.
- **v2.06 / Audit121** — system removals, current classes/Faces, final Legacy set, Relic cleanup, 20-consumable economy/placement, Chapter-4 four-element rework, terminology, Prime numeric sync.
- **v2.05 / Audit120** — compatible direct-damage and Critical rules.
- **v2.04 / Audit119** — compatible Card/Prime MP, named resistance, Prime status/scaling, and non-superseded progression architecture.
- **v2.03 / Audit118** — exact 38/38 ordinary-equipment source/numeric catalog and compatible Relic/Forge data.
- **v2.02 / Audit117** — compatible equipment/Legacy/class-access structure and Synthesis removal.
- **v2.01 / Audit116** — compatible Standard-Card and Prime command definitions.
- **v2.00 / Audit115** — compatible status/element/Ruin/class-Ability definitions.
- **v1.98 / Audit113** — current 13-chapter reindex.

Primary current domain files:
- `docs/canon/AUDIT127_CHAPTERS_5_8_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT126_CHAPTERS_1_4_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT125_MANDATORY_FORMATION_EXP_CEXP_ALLOCATION_LOCK.md`
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md`
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md`
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md`
- `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`
- `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`

Historical cumulative trackers are provenance/design history, not implementation authority by themselves.

---

# Universal combat firewall

Physical direct damage:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical direct damage:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Hybrid actions resolve authored components independently. Same-axis penetration caps at 75%. **Spirit** is the canonical magical-defense stat.

## Base Hit / Evasion
There is no natural Accuracy stat.

> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

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
Bleed damages each round and again when the affected character acts. It clears only on full-HP restoration, an eligible harmful-status clear, or an eligible item.

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

Base/Subclass cap = CL13. No Subclass before the Sixfold Volition boundary.

Class Ability MP is closed under Audit123 with no base-cost changes. General bands: routine 10–24; premium non-Ultimate 26–40; Ultimate 52–64; Standard Cards 18–48; Prime Invocation 50 / 80 / 90 MP.

---

# CEXP / Mastery / player progression

CL13 cumulative CEXP = **6,000**. Base and Subclass CEXP are separate; selected class receives 100%, unselected class receives 0; CEXP sent to a capped class is lost.

Pre-Volition Ch1–7 campaign CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch8–12 total 8,500
- Ch13 catch-up/overflow 1,500

Full Base + Subclass **Class-Level** completion occurs during Ch12, with Seyrik around end Ch12.

Synthesis is removed. Exactly 4 Core + 4 Subclass Masteries = 8 nodes.

Automatic Mastery Points:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

No ninth point and no Lv70 surplus point.

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

Desired progression layering:
1. Class Levels finish around Ch12 / roughly Lv53–57.
2. Final Mastery point arrives around Last Shelter / Lv60.
3. Normal campaign ends around Lv62.
4. Lv62–70 is optional/completionist headroom.

---

# Optional player EXP — Audit124

Fixed authored pre-Last-Shelter optional EXP:
- 5 ordinary Side Quests — **20,000**
- 6 Character Quests — **55,000**
- 11 Regional Hunts — **70,000**
- Major Hunts #1–5 — **50,000**
- **Total — 195,000 EXP**

Major Hunt #6 / The Unfinished World = **24,000 EXP**, excluded from Level-70 reachability proof.

At Last Shelter:
- normal route = 415,400 EXP / Lv60
- Lv70 threshold = 594,100
- completionist proof = 610,400
- buffer = **16,300 EXP**

Lower-level enemy EXP diminishing returns apply to repeatable/ordinary enemy-kill EXP only. Fixed authored completion/first-clear packages are exempt.

> **WEAK ENEMIES DIMINISH — AUTHORED CONTENT DOES NOT**

---

# Mandatory formation EXP/CEXP — Audit125

Expected ordinary encounter center = **225 total**, with Chapter 4 fixed at 19. Counts are stochastic planning centers, not quotas.

Mandatory player-EXP allocation:

| Ch | Ordinary | Named/story | Total |
|---:|---:|---:|---:|
| 1 | 855 | 745 | 1,600 |
| 2 | 2,288 | 2,512 | 4,800 |
| 3 | 3,480 | 4,520 | 8,000 |
| 4 | 5,262 | 5,938 | 11,200 |
| 5 | 8,978 | 9,822 | 18,800 |
| 6 | 10,600 | 14,300 | 24,900 |
| 7 | 14,120 | 17,180 | 31,300 |
| 8 | 18,962 | 19,238 | 38,200 |
| 9 | 25,000 | 20,500 | 45,500 |
| 10 | 31,800 | 21,500 | 53,300 |
| 11 | ~45,300 | ~16,200 | 61,500 |
| 12 | ~47,100 | ~22,900 | 70,000 |
| 13 | ~29,800 | ~49,200 | 79,000 |

Normal mandatory total remains **448,100 EXP / ~Lv62**.

Late Light / Standard / Heavy player-EXP anchors:
- Ch9 — **1,245 / 1,540 / 1,920**
- Ch10 — **1,700 / 2,100 / 2,500**
- Ch11 — **2,100 / 2,650 / 3,100**
- Ch12 — **2,100 / 2,600 / 3,150**
- Ch13 — **3,000 / 3,700 / 4,500**

Chapter 4 retains its protected 6/6/7 phase center, 202.4→256.2→358.6 formation averages, 5,262 ordinary EXP, and 11,200 total EXP.

Formation CEXP bands by chapter:
- Ch1 8 / 10 / 12
- Ch2 10 / 12 / 15
- Ch3 12 / 15 / 18
- Ch4 14 / 18 / 22
- Ch5 17 / 21 / 26
- Ch6 20 / 25 / 31
- Ch7 23 / 29 / 36
- Ch8 26 / 33 / 41
- Ch9 30 / 38 / 47
- Ch10 32 / 40 / 50
- Ch11 36 / 45 / 56
- Ch12 42 / 53 / 66
- Ch13 46 / 58 / 72

Current named/story CEXP remainders:
- Ch1 ~172
- Ch2 ~220
- Ch3 ~264
- Ch4 ~304
- Ch5 ~367
- Ch6 ~461
- Ch7 ~631
- Ch8 ~687
- Ch9 ~837
- Ch10 ~586
- Ch11 ~1,015
- Ch12 **~1,786**
- Ch13 ~1,032

No CEXP diminishing-return system is added.

---

# Exact mandatory named/story reward placement — Audits126–127

## Chapters 1–4 — Audit126

### Ch1 — 745 EXP / 172 CEXP
- Hollow Watch Castellan — 300 / 65
- Briarhide Stalker nonlethal stabilization — 120 / 28
- Greenhollow civilians secured + Torren permanent recruitment — 75 / 19
- Wayfinder Junction documented / chapter clear — 250 / 60

### Ch2 — 2,512 EXP / 220 CEXP
- Archive Leviathan — 700 / 55
- Prisoner Galleries safe-room state — 250 / 20
- Commander Rhazek — Bastion Master first clear/withdrawal — 900 / 75
- Hold the Junction — 350 / 30
- extraction / chapter clear — 312 / 40

### Ch3 — 4,520 EXP / 264 CEXP
- lawful-authority confrontation I — 400 / 24
- lawful-authority confrontation II — 500 / 30
- Suppressed Archives / Nimera permanent recruitment — 500 / 30
- First Command Warden — 1,800 / 90
- Last Sentinel confirmed — 600 / 40
- Cresthaven established / chapter clear — 720 / 50

### Ch4 — 5,938 EXP / 304 CEXP
- Elder Briarhide nonlethal resolution — 500 / 28
- Vaelira permanent recruitment / Annex expedition milestone — 450 / 30
- Reaction Conduit stabilization — 850 / 42
- Regulation Crucible → Seventh Reaction full clear — 2,800 / 120
- Annex crisis resolved / chapter clear — 1,338 / 84

## Chapters 5–8 — Audit127

### Ch5 — 9,822 EXP / 367 CEXP
- Furnace Tyrant — 2,100 / 70
- Repair Galleries / maintenance route stabilized — 1,000 / 40
- Deepforge Colossus full two-form clear — 4,500 / 150
- First Sovereign response — 1,300 / 50
- Deepforge handoff / chapter clear — 922 / 57

### Ch6 — 14,300 EXP / 461 CEXP
- Crownstorm Roc — 2,800 / 80
- Weather Crown stabilized / First Element — 1,300 / 45
- Matron Zevraya full transformed encounter — 4,500 / 130
- Masked Ruin Vanguard / Seyrik nonlethal clear — 3,000 / 100
- Seyrik permanent recruitment / chapter clear — 2,700 / 106

### Ch7 — 17,180 EXP / 631 CEXP
- Chainworks Behemoth — 3,200 / 100
- Ashford/Chainworks control dismantled — 1,200 / 45
- Veycross transit controls secured — 2,000 / 70
- Prison records / Seyrik provenance secured — 2,200 / 80
- Warden of the Nameless / Revision Arbiter — 5,500 / 190
- First Change / Prison resolution / Sixfold Volition chapter-clear handoff — 3,080 / 146

### Ch8 — 19,238 EXP / 687 CEXP
- Horizon Vault severance/intelligence breakthrough — 1,500 / 50
- Western Rift Engine — 5,000 / 165
- Western line / Westreach operational control — 2,200 / 70
- Marshal Varkesh — Rift Conqueror full two-form clear — 7,000 / 230
- coalition consolidation / chapter clear — 3,538 / 172

Reward architecture rules:
- optional Elites/Hunts do not consume mandatory chapter pools;
- same-bar transitions do not pay twice;
- fresh-HP transformations pay one combined package after final-form clear;
- nonlethal authored clears receive full progression where specified.

Still open: exact named/story reward placement **Chapters 9–13**, then progression-dependent named/boss raw-stat recertification.

---

# Equipment / items

Current equipment catalog:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- **91 total equipment pieces**

Current consumables = **20**. Currency = **Auren**. `1 economy unit = 20 Auren`.

Ordinary equipment architecture, 17/17 Legacy mechanics, Relic stale-mechanic cleanup, consumable architecture, current normal-stock pricing and reward placement remain closed.

---

# Standard Cards / Primes

Exactly 24 Standard Cards; maximum 3 equipped per character. Current Acuity quartet = Faultline Sight / Measured Response / Predicted Impact / Decisive Interval.

Predicted Impact = one enemy, Magical/Colorless, P180, BH110, 28 MP, 30% Stun.

Exactly 12 Primes; progression = Recovered → Awakened only. Invocation MP = 50 / 80 / 90. Prismatic Deluge = 90×4 = 360 total listed Power. Regulator Fang = 250 Power / 25% Spirit penetration.

---

# Chapter 4 firewall

Chapter 4 uses exactly Fire / Ice / Lightning / Earth. Wind and Water are removed from the research/regulation framework. Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers with exactly two active/targetable at once.

The live S022–S026 Markdown scripts and matching dialogue `.tres` resources are synchronized to the four-element rework.

---

# Implementation rule

When a live implementation file conflicts with Audit127/Audit126/Audit125/Audit124/Audit123/Audit122/Audit121 in their respective domains, update the implementation file. Do not revive stale Synthesis, Barrier, Brace, six-element Chapter-4, retired class names, old Resource-face, old Bleed-clearing, Lv62-at-end-Ch12, pre-cut optional-EXP, obsolete formation-budget assumptions, or duplicate transition rewards from historical trackers.
