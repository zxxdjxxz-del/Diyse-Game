# Diyse — Active Engineering Canon Guardrails

This file is the implementation-facing authority index. It does not replace the canon audits. Compatible older locks remain active where not superseded; later explicit approved corrections win.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.13 / Audit128 — Chapters 9–13 Named/Story EXP+CEXP Placement Lock**  
**Date:** August 27, 2026

Newest authority chain:
- **v2.13 / Audit128** — exact mandatory named/story player-EXP + CEXP placement for Chapters 9–13; completes all 13 chapters; Ch13 5/3 pre/post Last-Shelter encounter planning split.
- **v2.12 / Audit127** — exact mandatory named/story player-EXP + CEXP placement for Chapters 5–8.
- **v2.11 / Audit126** — exact mandatory named/story player-EXP + CEXP placement for Chapters 1–4.
- **v2.10 / Audit125** — mandatory ordinary-vs-authored EXP allocation, late formation EXP anchors, formation CEXP bands, chapter named/story envelopes.
- **v2.09 / Audit124** — 195,000 authored optional-EXP cap-proof pool and diminishing-return firewall.
- **v2.08 / Audit123** — class Ability MP certification, 6,000-CEXP CL13 curve, exact 8-point Mastery schedule, player-level spine.
- **v2.07 / Audit122** — Base Hit/Evasion and current Bleed lifecycle.
- **v2.06 / Audit121** — current classes/Faces, removed systems, final Legacy set, Relic cleanup, 20-consumable economy, Chapter-4 four-element rework.
- compatible Audit120–Audit113 remain active where not superseded.

Primary current domain files:
- `docs/canon/AUDIT128_CHAPTERS_9_13_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT127_CHAPTERS_5_8_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT126_CHAPTERS_1_4_NAMED_STORY_EXP_CEXP_PLACEMENT_LOCK.md`
- `docs/canon/AUDIT125_MANDATORY_FORMATION_EXP_CEXP_ALLOCATION_LOCK.md`
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md`
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md`
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md`
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

Historical trackers/audits are provenance, not current authority by themselves.

---

# Universal combat firewall

Physical direct damage:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical direct damage:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

Hybrid components resolve independently. Same-axis penetration cap = 75%. **Spirit** is magical defense.

Base Hit / Evasion:
> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

There is no natural Accuracy stat.

Critical:
- base 5%;
- flat percentage-point bonuses;
- ordinary random cap 50%;
- eligible multiplier 1.5×;
- Crit does not bypass Defense/Spirit.

Removed systems:
- **Barrier does not exist.**
- **Brace does not exist.**
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

Bleed damages each round and again when the affected character acts. It clears only on full-HP restoration, eligible harmful-status clear, or eligible item.

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

Base/Subclass cap = CL13. No Subclass before end-Ch7 Sixfold Volition. Synthesis is removed.

Class Ability MP is closed: routine roughly 10–24; premium non-Ultimate 26–40; Ultimates 52–64; Standard Cards 18–48; Prime Invocation 50 / 80 / 90 MP.

---

# CEXP / Mastery / player progression

CL13 cumulative CEXP = **6,000**. Base and Subclass CEXP are separate. Selected class receives 100%; unselected class receives 0; CEXP sent to a capped selected class is lost.

Pre-Volition Ch1–7 CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch8–12 total 8,500
- Ch13 catch-up/overflow 1,500

Class Levels complete during Ch12; Seyrik is the limiting normal-route case around end Ch12.

Exact Mastery Points:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

Player level cap = 70. Chapter 0 grants no levels.

Mandatory-route anchors:
- End Ch1 Lv5
- End Ch2 Lv9
- End Ch3 Lv13
- End Ch4 Lv17
- End Ch5 Lv22
- End Ch6 Lv27
- End Ch7 Lv32
- End Ch8 Lv37
- End Ch9 Lv42
- End Ch10 Lv47
- End Ch11 Lv52
- End Ch12 Lv57
- **Last Shelter Lv60**
- **End Ch13 Lv62**

Layering: Class Levels finish first (~Lv53–57), final Mastery point around Last Shelter/Lv60, normal campaign ends ~Lv62, Lv62–70 is optional/completionist headroom.

---

# Optional player EXP — Audit124

Fixed authored pre-Last-Shelter pool:
- 5 Side Quests — 20,000
- 6 Character Quests — 55,000
- 11 Regional Hunts — 70,000
- Major Hunts #1–5 — 50,000
- **total 195,000 EXP**

Major Hunt #6 = 24,000, excluded from the cap proof.

At Last Shelter: normal 415,400 / Lv60; Lv70 threshold 594,100; broad completionist proof 610,400; buffer 16,300.

> **WEAK ENEMIES DIMINISH — AUTHORED CONTENT DOES NOT**

---

# Mandatory formation EXP/CEXP — Audit125

Expected ordinary encounters = **225 total**, planning centers not quotas. Chapter 4 remains 19 expected random encounters, 5,262 ordinary EXP, 11,200 total EXP.

Late Light / Standard / Heavy EXP anchors:
- Ch9 1,245 / 1,540 / 1,920
- Ch10 1,700 / 2,100 / 2,500
- Ch11 2,100 / 2,650 / 3,100
- Ch12 2,100 / 2,600 / 3,150
- Ch13 3,000 / 3,700 / 4,500

Formation CEXP tiers remain those locked in Audit125. No separate CEXP diminishing-return system exists.

---

# Exact mandatory named/story rewards — Audits126–128

All 13 chapters are now placed exactly. Optional Elites/Hunts/quests never consume mandatory pools. Same-bar transitions pay once; fresh-HP multi-form bosses pay one combined package after final-form clear.

## Ch9
20,500 EXP / 837 CEXP total:
- Equal Mercy stabilization 1,500/60
- Equal Mercy Arbiter 4,500/170
- Last Sanctuary resolution 1,500/60
- Crownfall defense/infiltration milestone 2,500/100
- Rhazek → Bastion Devourer full encounter 7,500/300
- Crownfall preserved/chapter clear 3,000/147

## Ch10 — The Last Blank
21,500 / 586:
- eastern survey secured 2,000/50
- Calder secured / Lower Archive 3,000/75
- Buried Registry access 3,500/85
- Registry Warden 8,000/200
- Sixfold Unsealing / Last Blank resolved 3,500/110
- Crown Engine handoff 1,500/66

## Ch11 — Crown Engine
16,200 / 1,015:
- Living Anchor/Crown Engine confrontation 4,000/230
- Custodian domain/contact 2,500/140
- Truth Beneath the Empire 4,000/240
- First Reckoning/Sixfold Reconciliation 4,000/250
- chapter clear 1,700/155

Do not retrofit Varkesh/Vhalmarch/Vaelkor into Chapter 11.

## Ch12 — The Reforged March
22,900 / 1,786:
- Blackspine/Draevensreach breakthrough 3,000/200
- Varkesh defeat/live capture 6,000/450
- Vhalmarch Forward Hub secured 2,500/200
- Vorathen/Veiled Citadel breach 3,000/250
- Vaelkor two-form full clear 7,000/550
- post-Vaelkor cleanup state/chapter clear 1,400/136

Use **Westguard**, not Westreach/Yahtrens Stand. Vhalmarch becomes Forward Hub only after Varkesh capture. Vaelkor's defeat opens cleanup and does not automatically launch Ch13.

## Ch13 — The Last Command
Current hard order:
**Deepest City → Last Weapon Archive → Last Weapon Archon → Last Shelter → Reactor Galleries → Reactor–Crest Interface → Reconstituted Entity → Crest Integration / The Last Command → Final Severance → aftermath.**

True PONR = **Last Shelter → Reactor Galleries**.

Eight ordinary-encounter planning center splits **5 before Last Shelter / 3 after**, not quotas.

Pre-Shelter:
- expected ordinary EXP 18,600
- fixed named/story EXP 27,700
- total 46,300 → ~Lv60
- named/story CEXP 600

Fixed pre-Shelter packages:
- Deepest City / Archive reached 4,000/90
- Archive fragment-survival truth 5,000/110
- Last Weapon Archon 12,000/280
- Last Shelter reached 6,700/120

Post-PONR:
- expected ordinary EXP 11,200
- fixed named/story EXP 21,500
- total 32,700 → normal ending ~Lv62
- named/story CEXP 432

Fixed post-PONR packages:
- Reactor Galleries realization 3,500/70
- Reactor–Crest Interface reached 2,500/50
- Reconstituted Entity → The Last Command complete two-form final boss 13,500/270
- aftermath/surface return/ending 2,000/42

Final boss = exactly two genuine full-health forms, no third form. Crest Integration pays 0 at transition.

For exact Ch1–8 packages, use Audit126 and Audit127.

---

# Equipment / items / Cards / Primes

Equipment catalog remains 38 ordinary + 36 Relics + 17 Legacies = **91**. Consumables = **20**. Currency = Auren.

Exactly 24 Standard Cards, max 3 equipped. Exactly 12 Primes, Recovered → Awakened only. Prismatic Deluge = 90×4 = 360 total; Regulator Fang = 250 Power / 25% Spirit penetration.

---

# Chapter 4 firewall

Exactly Fire / Ice / Lightning / Earth. Wind and Water are not research/regulation elements. Reaction Conduit replaces Elemental Hexarch. Regulation Crucible uses four chambers with exactly two active/targetable. Live S022–S026 Markdown and matching dialogue Resources are synchronized.

---

# Active frontier

## Progression-dependent named-enemy / boss raw-stat recertification

Recover current HP / ATK / MAG / DEF / Spirit / SPD / Evasion / Status Resistance for mandatory named enemies and bosses and compare them against the now-final chapter player-level bands.

Preserve encounter mechanics, HP-bar/form architecture, fresh-form rules, current formulas, statuses and elements. Do not add Barrier, Brace, global Break/Stagger, natural Accuracy, Synthesis, or other retired systems.
