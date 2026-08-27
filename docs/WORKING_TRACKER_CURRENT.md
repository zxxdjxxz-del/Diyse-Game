# Diyse — Current Working Tracker (Consolidated)

**Date:** August 26, 2026  
**Working revision:** **v1**  
**Status:** **ACTIVE WORKING TRACKER — NOT MASTER CANON**

This file replaces the cumulative 165,000-line item/equipment tracker as the active working tracker.

The cumulative v603 tracker is frozen historical design evidence. Do not append new work to it. Master canon always outranks this file.

---

# 1. Current written authority

Current whole-project authority:

> **v2.04 / Audit119**

Newest relevant chain:
- Audit119 — combat/resource/Prime/progression reconciliation
- Audit118 — exact ordinary/Relic/Legacy-Trait/Forge numerical catalog
- Audit117 — equipment/Legacy/class-access structure and Synthesis removal
- Audit116 — compatible Standard-Card/Prime command definitions
- Audit115 — compatible status/element/Ruin/class-Ability definitions
- Audit113 — current 13-chapter reindex

Use `docs/ACTIVE_CANON.md` for the compact implementation-facing authority index.

---

# 2. Current project baselines

- HD-2D presentation target.
- Player level cap = 70.
- Base/Subclass class cap = CL13.
- Active battle party = 4.
- Maximum active enemies = 8.
- Permanent commands = Attack / Ability / Card / Item / Defend.
- Chapter 0 grants no character levels.
- Current late spine: Ch10 The Last Blank → Ch11 Crown Engine → Ch12 The Reforged March → Ch13 The Last Command.
- True irreversible threshold = Last Shelter → Reactor Galleries.

Current six:
- Cyanis — Crest Knight / Crest Magus
- Ilyra — Blue Warden / Vowblade
- Torren — War Archer / Routeweaver
- Nimera — Cardweaver / Sixfold Knight
- Vaelira — Prism Archer / Green Arcanist
- Seyrik — Ruin Vanguard / Ruin Healer

---

# 3. Class / Mastery state

Current Subclass equipment progression:
- CL1 donor Primary
- CL3 donor Armor + Mastery 1 eligible
- CL5 donor Secondary + Mastery 2 eligible
- CL7 Mastery 3 / Equipment Mastery eligible; purchasing it grants donor Relic access
- CL11 Mastery 4 / Legacy Mastery eligible; purchasing it grants donor Legacy access

Synthesis is removed completely.

Only eight active Mastery nodes remain. The inherited nine-point Mastery Point schedule therefore needs reconciliation.

Exact current Base/Subclass Ability MP costs remain open after the latest class-kit/name changes. Preserve the higher-MP direction and modest Subclass premium; do not treat retired-name working tables as final.

---

# 4. Universal direct-damage formula

> **Component Damage = Weight × (Power / 100) × Offense × 1.50 × [150 / (150 + Effective Defensive Stat)]**

- Physical = Attack vs Defense.
- Magical = Magic vs Spirit.
- Ruin character Ability = 75% Attack / 25% Magic.
- same-axis penetration adds and caps at 75%.
- no cross-axis penetration transfer.
- Basic Attack = 100 Power / Physical / Neutral unless equipment says otherwise.
- no universal AoE penalty.
- no universal random damage variance.

Open:
- Accuracy vs Evasion formula
- universal Critical payout/order

---

# 5. Standard Cards / Primes

Exactly 24 Standard Cards; max 3 equipped per character.

Current Card MP costs are 18–48 and are controlled by Audit119. Audit116's old 12–36 costs are superseded.

Open Standard-Card acquisition homes:
- Restoration
- Cinder Judgment
- Iron Testament
- Sunder the Gate

Prime progression:

> **Recovered → Awakened**

Current Invocation costs:
- Recovered Story = 50 MP
- Awakened Story = 80 MP
- Awakened Major Hunt = 90 MP
- manifested commands = 0 additional MP

Awakened Prime duration = 3 Prime rounds. Shared cooldown = 3 full normal-party rounds. No Prime XP/levels/duplicate progression.

Default Prime harmful-status susceptibility = 80%. Freeze/Stun together may deny at most one selected Prime command per manifestation.

Prime Reference Level = highest current level among the four active party members at Invocation, clamp 1–70. Full Prime baseline/state/identity multipliers are in Audit119.

Retained late-Hunt anchors:
- Final Archive Arbiter — 43,100 HP / 229 ATK / 244 MAG / 194 DEF / 198 Spirit / 50 SPD
- The Unfinished World — 78,000 HP / 304 ATK / 318 MAG / 226 DEF / 232 Spirit / 61 SPD

Open: exact Prismatic Deluge Power if not closed by a later dedicated Prime pass.

---

# 6. Consumables

Current Consumable count = 21.

MP ladder:
- Flow Tonic — 50 MP
- Deepflow Tonic — 80 MP
- Highflow Tonic — 120 MP
- Reservoir Tonic — 75% Max MP
- Emergency Kit — 60% Max MP as its MP component

Open:
- exact HP-restorative values
- Emergency Rally final revive/heal values
- exact shop timing/prices
- final integer currency denomination

---

# 7. Equipment / Relic / Legacy state

Current catalog:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- **91 total**

Exact ordinary stats/source map, Relic stats/Traits/placements, settled Legacy Traits, Cresthaven relative-value rules, and exact 30-slot Forge source matrix are closed under Audit118.

Slot firewalls:
- Ilyra Wardrod Primary; Shield or Focus Secondary
- Torren Great Bow = Weapon + Secondary
- Vaelira Arcane Staff = one-slot Primary; Focus legal
- Seyrik 2H Sword = Weapon + Secondary
- Nimera ordinary/surviving Relic Conduits = one-slot
- Nimera native Legacy Conduit = Weapon + Secondary

All 12 Subclass Relics are removed. Six separate shared-Legacy artifacts are removed.

Native Legacy completion requires:
1. Base CL13
2. all 4 Core Masteries
3. Character Quest / resolution
4. unique Character Quest Legacy Component
5. unique Legacy precursor
6. Gate A material
7. Gate B material
8. Kessara project availability

Gate A → weapon. Gate B → remaining package pieces.

Forge Components:
- 30 total
- 12 Legacy-gate-specific
- 18 Relic-copy-specific
- categories non-interchangeable

Relic copy:
- original must already be obtained
- one matching-Face copy material
- one forged duplicate maximum
- max quantity 2
- Legacies remain unique

---

# 8. Legacy current frontier

Tier hierarchy:

> **Ordinary < Relic < Legacy**

Approved Legacy capstone-stat axes:
- Max HP
- Max MP
- Accuracy
- Evasion

## Pending approval — exact v600 package

- Cyanis Sword — +74 ATK / +55 MAG / Accuracy +8
- Cyanis Shield — +30 DEF / +28 Spirit / Max HP +8%
- Cyanis Heavy Armor — +50 DEF / +42 Spirit / Max HP +12%
- Ilyra Wardrod — +58 ATK / +63 MAG / Max MP +8%
- Ilyra Shield — +28 DEF / +30 Spirit / Max HP +8%
- Ilyra Focus — +22 MAG / +28 Spirit / Max MP +12%
- Ilyra Warding Armor — +34 DEF / +44 Spirit / Max HP +10%
- Torren Great Bow — +95 ATK / Accuracy +10
- Torren Medium Armor — +42 DEF / +33 Spirit / +3 SPD / Evasion +10
- Nimera 2H Conduit — +60 ATK / +82 MAG / Max MP +10%
- Nimera Focus — +22 MAG / +22 Spirit / +8 SPD / Max MP +12%
- Nimera Light Ritual Armor — +32 DEF / +42 Spirit / Evasion +10
- Vaelira Arcane Staff — +12 ATK / +83 MAG / Accuracy +8
- Vaelira Focus — +24 MAG / +24 Spirit / +5 SPD / Max MP +12%
- Vaelira Light Caster Armor — +29 DEF / +50 Spirit / +4 SPD / Evasion +8
- Seyrik 2H Sword — +105 ATK / +7 MAG / Accuracy +8
- Seyrik Battle Heavy Armor — +56 DEF / +34 Spirit / Max HP +15%

These exact values are **not master canon yet**.

## Open Legacy identity question

An earlier explicit working requirement said Relics and Legacies should include elemental/harmful-status perks and that Legacies should combine stats + perks + passive(s).

Relics have now been fully reconciled. For Legacies, explicitly decide whether:
- every Legacy piece still requires elemental/status interaction;
- only selected Legacy pieces receive it where character identity supports it;
- the newer HP/MP/Accuracy/Evasion capstone-stat layer partly replaces the earlier universal expectation.

Do not silently treat this requirement as closed.

---

# 9. Legacy precursors / project presentation

Current precursor timing:
- Cyanis — Major Hunt #2
- Nimera — Major Hunt #3
- Vaelira — Ch8 story
- Ilyra — Ch9 story
- Torren — Ch11 Crown Engine
- Seyrik — Ch12 Black Host campaign

Timing is closed. Exact pickup/reward presentation remains open where not explicitly authored.

Kessara Relic-copy service fee/UI and some exact Forge pickup presentation also remain open.

---

# 10. Progression high-level locks

- Chapters 1–7 deliberately somewhat lower than a near-linear progression curve.
- faster progression after Chapter 7.
- expected Chapter-12 campaign-only clear target = Lv60.
- distribute added late EXP backward through Chapter 9 onward.
- enemy strength and kill EXP rise from chapter start to chapter end.
- old/weak enemies award much less kill EXP to overlevelled parties.
- fixed authored quest/Hunt first-clear reward packages are not automatically reduced by overlevel.

Exact Ch1–13 player bands, enemy bands, encounter counts, per-formation EXP, and diminishing-return percentages remain deferred to the dedicated EXP rebalance.

Do not restore the old v494–v503 exact tables as current canon.

---

# 11. Current ordinary Side Quests

The old v480–v493 reduction branch is stale.

Current retained quests include:
- Edda Harth — The Marks We Leave — Ch1 after Torren joins / Greenhollow / low-zero required combat
- Edda Harth — When the Roads Open — post-Vaelkor cleanup / current Ch12
- Talia Rell — The Third Caravan — after Ch8 / Greenhollow → Ashford
- Talia Rell — The Living List — after Ch10 / Ashford anchor

Dialogue and exact final rewards remain deferred.

---

# 12. Current open / pending / deferred queue

## Pending approval
1. exact v600 17-Legacy raw stats + capstone perks

## Open — system/numerical
2. Legacy elemental/status/perk/passive requirement vs newer capstone-stat identity
3. exact current Base/Subclass Ability MP table
4. Accuracy vs Evasion formula
5. universal Crit payout/order
6. Mastery Point schedule for 8 active nodes
7. Prismatic Deluge exact Power if still unresolved
8. HP consumables / Emergency Rally
9. detailed Ch1–13 EXP/enemy/encounter/diminishing-return rebalance
10. progression-dependent named-enemy raw-stat re-certification

## Open — content/economy/implementation
11. four Standard-Card acquisition homes
12. Consumable stock timing/prices/final currency
13. Kessara Relic-copy service fee/UI
14. exact presentation for some Forge Component pickups
15. exact presentation for some Legacy precursors

## Deferred
16. final Relic names
17. final Legacy names
18. final Character Quest Legacy Component names
19. final Forge-variant names
20. ordinary Side-Quest dialogue
21. exact Side-Quest final rewards
22. new Caelora Civic Ward proper name

---

# 13. Stale / retired branch quarantine

Do not reactivate by accident:
- Synthesis architecture / ninth node
- six separate shared-Legacy artifacts
- 12 Subclass Relics
- old 118-piece equipment catalog
- Resource / Regulator terminology
- temporary Reactive Prime state
- Audit116 12–36 Card MP costs
- Audit116 60/75/75 Prime costs
- old v494–v503 chapter progression tables
- stale v480–v493 Side-Quest reduction branch
- pre-insertion Ch10/11/12 numbering
- old low-MP class Ability tables as final values
- old class names that conflict with the current six
- rejected personal-equipment naming attempts

---

# 14. Next recommended workflow

1. resolve the Legacy elemental/status/perk/passive structure;
2. approve/revise the v600 exact 17-Legacy stat/perk table;
3. promote approved final Legacy numbers to master canon;
4. reconcile the 8-node Mastery Point schedule;
5. then proceed to Accuracy/Evasion + Crit, current class Ability MP, the dedicated EXP/enemy rebalance, or remaining Consumable/economy work.
