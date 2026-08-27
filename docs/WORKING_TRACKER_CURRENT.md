# Diyse — Current Working Tracker (Consolidated)

**Date:** August 26, 2026  
**Working revision:** **v4**  
**Status:** **ACTIVE WORKING TRACKER — NOT MASTER CANON**

This file replaces the cumulative 165,000-line item/equipment tracker as the active working tracker.

The cumulative v603 tracker is frozen historical design evidence. Do not append new work to it. Master canon always outranks this file.

---

# 1. Current written authority

Current whole-project authority:

> **v2.05 / Audit120**

Newest relevant chain:
- Audit120 — Critical Hit + controlling direct-damage formula
- Audit119 — compatible Card/Prime MP, resistance, Prime scaling/control, progression
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

# 4. Direct damage / Critical Hits — Audit120

Physical:

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

Magical:

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

Same-axis penetration adds and caps at **75%**.

Hybrid direct hits resolve their authored Physical and Magical weighted components independently, then combine them. Character Ability Ruin remains 75% Attack / 25% Magic where Audit115 applies.

Critical rules:
- base Critical Chance = **5%**
- modifiers add flat percentage points
- ordinary random Crit cap = **50%**
- eligible Critical damage = **1.5×**
- Base Hit/Evasion check occurs before Crit
- miss = no Crit roll
- multihit actions roll Crit independently per authored direct hit by default
- one authored Hybrid hit uses one Crit roll on its combined eligible direct-damage result
- eligible Magical direct hits use the same 1.5× multiplier
- Critical does not bypass Defense/Spirit
- Critical does not automatically improve status application
- Burn/Bleed and other explicitly excluded indirect damage cannot Crit

No hidden universal AoE penalty. No universal random damage variance. Round at the normal final-damage step.

Use **Base Hit**, not `Accuracy`, as the canonical hit-stat term.

Open:
- global **Base Hit vs Evasion** formula

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

Approved capstone-stat axes:
- Max HP
- Max MP
- **Base Hit**
- Evasion

`Accuracy` is retired wording for this stat axis.

Legacies do **not** require a universal elemental identity. Do not force elemental damage/resistance/riders merely because an item is a Legacy. Status interaction may remain where an individual Trait naturally uses it.

## Pending approval — exact v600 package, terminology corrected

- Cyanis Sword — +74 ATK / +55 MAG / Base Hit +8
- Cyanis Shield — +30 DEF / +28 Spirit / Max HP +8%
- Cyanis Heavy Armor — +50 DEF / +42 Spirit / Max HP +12%
- Ilyra Wardrod — +58 ATK / +63 MAG / Max MP +8%
- Ilyra Shield — +28 DEF / +30 Spirit / Max HP +8%
- Ilyra Focus — +22 MAG / +28 Spirit / Max MP +12%
- Ilyra Warding Armor — +34 DEF / +44 Spirit / Max HP +10%
- Torren Great Bow — +95 ATK / Base Hit +10
- Torren Medium Armor — +42 DEF / +33 Spirit / +3 SPD / Evasion +10
- Nimera 2H Conduit — +60 ATK / +82 MAG / Max MP +10%
- Nimera Focus — +22 MAG / +22 Spirit / +8 SPD / Max MP +12%
- Nimera Light Ritual Armor — +32 DEF / +42 Spirit / Evasion +10
- Vaelira Arcane Staff — +12 ATK / +83 MAG / Base Hit +8
- Vaelira Focus — +24 MAG / +24 Spirit / +5 SPD / Max MP +12%
- Vaelira Light Caster Armor — +29 DEF / +50 Spirit / +4 SPD / Evasion +8
- Seyrik 2H Sword — +105 ATK / +7 MAG / Base Hit +8
- Seyrik Battle Heavy Armor — +56 DEF / +34 Spirit / Max HP +15%

These exact values are **not master canon yet**.

Legacy Trait wording has been normalized in the local consolidated tracker to use Base Hit, Defense, Spirit, Status Resistance, explicit duration, and percentage-point terminology without intentionally redesigning the underlying Trait identities.

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
2. exact current Base/Subclass Ability MP table
3. Base Hit vs Evasion formula
4. Mastery Point schedule for 8 active nodes
5. Prismatic Deluge exact Power if still unresolved
6. HP consumables / Emergency Rally
7. detailed Ch1–13 EXP/enemy/encounter/diminishing-return rebalance
8. progression-dependent named-enemy raw-stat re-certification

## Open — content/economy/implementation
9. four Standard-Card acquisition homes
10. Consumable stock timing/prices/final currency
11. Kessara Relic-copy service fee/UI
12. exact presentation for some Forge Component pickups
13. exact presentation for some Legacy precursors

## Deferred
14. final Relic names
15. final Legacy names
16. final Character Quest Legacy Component names
17. final Forge-variant names
18. ordinary Side-Quest dialogue
19. exact Side-Quest final rewards
20. new Caelora Civic Ward proper name

---

# 13. Stale / retired branch quarantine

Do not reactivate by accident:
- Audit119 `Offense × 1.50 × 150/(150+Defense)` direct-damage resolver
- unresolved/alternative Critical multipliers
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
- `Accuracy` as the active hit-stat term; use **Base Hit**

---

# 14. Next recommended workflow

1. approve/revise the v600 exact 17-Legacy stat/perk table under the current Base-Hit terminology and non-elemental Legacy direction;
2. promote approved final Legacy numbers to master canon;
3. reconcile the 8-node Mastery Point schedule;
4. then proceed to Base Hit/Evasion, current class Ability MP, the dedicated EXP/enemy rebalance, or remaining Consumable/economy work.
