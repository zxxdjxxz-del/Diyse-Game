# AGENTS.md — Diyse Engineering Contract

This file governs AI-assisted engineering work in this repository.

## Read first

Before changing gameplay code or production content, read:

1. `docs/ACTIVE_CANON.md`
2. `docs/IMPLEMENTATION_STATUS.md`
3. `docs/chapters/README.md`
4. the relevant current chapter file under `docs/chapters/`
5. the latest controlling canon audit for the subject
6. `docs/PRESENTATION_RULES.md`
7. the relevant subsystem document
8. `docs/DIALOGUE_AUTHORING_SCHEMA.md` and `docs/STEP_7C_AUTHORING_TEMPLATE.md` before dialogue Resource work
9. `docs/TECHNICAL_PROOF.md` only as compatible historical engineering evidence

If a task conflicts with these files or a newer explicit user instruction, stop and surface the conflict. Do not silently reinterpret canon.

Historical audit filenames and cumulative trackers remain provenance, not automatic current authority.

---

# Current authority state

Whole-project written authority:

> **Diyse v2.09 / Audit124**

Current authority chain:
- `docs/canon/AUDIT124_OPTIONAL_EXP_AND_LEVEL_70_COMPLETIONIST_CAP_LOCK.md` — optional player EXP / Level-70 completionist proof.
- `docs/canon/AUDIT123_CLASS_MP_CEXP_MASTERY_AND_LATE_GAME_PROGRESSION_LOCK.md` — class Ability MP, CEXP, Mastery, player-level spine, late mandatory EXP, enemy bands.
- `docs/canon/AUDIT122_BASE_HIT_EVASION_AND_BLEED_RUNTIME_LOCK.md` — Base Hit/Evasion and Bleed.
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md` — current classes/Faces, removed systems, 17/17 Legacies, Relic cleanup, 20-consumable economy, Chapter-4 four-element conversion, current terminology, Prime numeric sync.
- `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md` — compatible direct-damage and Critical rules.
- `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md` — compatible Card/Prime MP, resistance and Prime rules not superseded later.
- `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md` — closed 38/38 ordinary-equipment catalog and compatible Relic/Forge data.
- `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md` — compatible equipment/Legacy/class-access structure.
- `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md` — compatible Standard Card and Prime commands.
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md` — compatible status/element/Ruin/class Ability definitions.
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md` — current 13-chapter numbering.

Current world-map/region authority remains the compatible Audit111 chain plus later explicit place-name corrections.

Chapters 0–4 remain COMPLETE/CLOSED at story/dialogue authority level. Chapter 4's current four-element script/runtime state is controlling.

HD-2D is the sole active presentation target.

---

# Current combat firewall

## Direct damage

Physical:
> `BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)`

Magical:
> `BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)`

- Physical = Attack vs Defense.
- Magical = Magic vs Spirit.
- Hybrid components resolve independently on their authored axes.
- Character-Ability Ruin remains 75% Attack / 25% Magic where current Ruin rules apply.
- Same-axis penetration adds in percentage points and caps at **75%**.
- No cross-axis penetration transfer.
- No hidden universal AoE penalty.
- No universal random damage variance.
- Basic Attack = 100 Power / Physical / Neutral unless equipment explicitly changes affinity.

## Critical Hits
- base Critical Chance = **5%**;
- bonuses are flat percentage-point additions;
- ordinary random Critical Chance cap = **50%**;
- eligible Critical multiplier = **1.5×**;
- Base Hit/Evasion resolves before Critical Chance;
- a miss receives no Critical roll;
- Critical does not bypass Defense/Spirit;
- Critical does not automatically improve harmful-status application;
- Burn, Bleed, healing, and explicitly no-Crit indirect/copied effects do not Crit unless separately authored otherwise.

## Base Hit / Evasion
There is no natural Accuracy stat.

> `AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers`

> `EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers`

> `FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)`

Normal authoring centers:
- standard ~100 Base Hit
- heavy 90–95
- precision 105–115
- exceptional precision may reach ~120

Hit/Evasion, Critical, and harmful-status application are separate rolls/systems.

## Removed systems
- **Barrier does not exist.**
- **Brace does not exist.**
- no global Break/Stagger meter.
- **Staggered** is only an ordinary harmful status where authored.
- **Guard** remains valid.

Do not recreate removed mechanics under renamed equivalents.

## Bleed
Bleed:
- damages each round;
- damages again when the affected character acts;
- clears only on full-HP restoration, an eligible harmful-status clear, or an eligible item.

Partial healing/Regen does not clear Bleed unless full HP is reached or the action includes a valid status clear.

---

# Standard Cards / Primes

## Standard Cards
- exactly **24**;
- maximum **3 equipped per character**;
- reusable and MP-consuming;
- no charge/deck/draw/discard/duplicate/rank subsystem;
- current Card MP band = **18–48 MP**.

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
- no Break/Stagger-meter rider.

## Primes
Progression:
> **Recovered → Awakened**

Invocation MP:
- Recovered Story — 50
- Awakened Story — 80
- Awakened Major Hunt — 90
- manifested Prime commands — 0 additional MP

Awakened Primes replace/suspend the ordinary party for exactly 3 Prime rounds, then trigger the shared 3-full-normal-round cooldown. Prime use remains once per identity per battle unless a genuine fresh-HP form refresh applies.

No Prime XP, levels, duplicates, or upgrade-material progression.

Current numeric sync:
- Prismatic Deluge = **4 × 90 = 360 total listed Power per target**.
- Regulator Fang = **250 Power / 25% Spirit penetration**, choose Fire/Ice/Lightning/Earth, no harmful-status rider.

---

# Current class / Mastery architecture

Permanent six:
- Cyanis — **Crest Knight / Crest Arcanist** — Might
- Ilyra — **Blue Warden / Vowblade** — Grace
- Torren — **War Archer / Routeweaver** — Acuity
- Nimera — **Cardweaver / Proofhunter** — Change
- Vaelira — **Green Arcanist / Axiomblade** — Elements
- Seyrik — **Ruin Vanguard / Ruin Warden** — Ruin

Base and Subclass caps are **CL13**.

No permanent character uses a Subclass before Sixfold Volition at the end of Chapter 7.

## Class Ability MP — CLOSED
Audit123's exact Base/Subclass MP tables are implementation authority.

General bands:
- routine class actions ~10–24 MP
- premium non-Ultimates ~26–40 MP
- Ultimates 52–64 MP

Do not reopen the MP tables without an actual later authority or demonstrated system failure.

## Mastery
**Synthesis is removed.** Never implement Synthesis Mastery, Synthesis cost/passive, a ninth Mastery point, or a duplicate shared Legacy artifact.

Exactly:
- 4 Core Masteries
- 4 Subclass Masteries
- 8 active nodes
- 8 automatic Mastery Points

Eligibility:
- Core — Base CL3 / 6 / 9 / 12
- Subclass — CL3 / 5 / 7 / 11

Automatic points:
1. Lv5
2. Lv10
3. Lv15
4. Lv20
5. Sixfold Volition
6. Lv40
7. Lv50
8. Lv60

No Lv70 surplus point.

Subclass Mastery 3 purchase → donor Relic access.  
Subclass Mastery 4 purchase → donor Legacy access.

The donor's actual obtained item is equipped. No duplicate artifact. Trait travels with the item. No universal off-owner nerf.

Donor pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

A character's native Legacy does not require Synthesis or donor Legacy Mastery.

---

# CEXP / player progression firewall

## CEXP
CL13 cumulative threshold = **6,000 CEXP**.

Base and Subclass CEXP remain separate. The selected class receives 100% of awarded CEXP. The unselected class receives 0. CEXP sent to a capped class is lost and does not spill over.

Pre-Volition Ch1–7 normal CEXP = **4,950**.

Post-Volition normal CEXP:
- Ch8 1,300
- Ch9 1,450
- Ch10 1,200
- Ch11 1,800
- Ch12 2,750
- Ch8–12 total **8,500**
- Ch13 catch-up/overflow **1,500**

Normal full Base + Subclass Class-Level completion occurs during Chapter 12:
- Torren early
- Vaelira early/mid
- Cyanis/Ilyra mid
- Nimera mid/late
- Seyrik around end Ch12

Class Levels intentionally finish before the final Mastery-board point.

## Player levels
Player cap = **70**. Chapter 0 grants no character levels.

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

Do not restore the rejected Lv62-at-end-Ch12 model.

Desired progression sequence:
1. Class Levels complete around Ch12 / roughly Lv53–57.
2. Final Mastery point arrives around Last Shelter / Lv60.
3. Normal campaign ends around Lv62.
4. Lv62–70 is optional/completionist headroom.

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

Expected ordinary random-encounter planning center = **225 total**. Chapter 4 remains **19**. These are planning centers, not quotas.

---

# Optional EXP / Level-70 firewall — Audit124

Fixed authored pre-Last-Shelter optional EXP:
- 5 ordinary Side Quests — **20,000**
- 6 Character Quests — **55,000**
- 11 Regional Hunts — **70,000**
- Major Hunts #1–5 — **50,000**
- total — **195,000 EXP**

Major Hunt #6 / The Unfinished World:
- **24,000 EXP**
- excluded from Level-70 reachability proof.

At Last Shelter:
- normal route = 415,400 EXP / Lv60
- Lv70 threshold = 594,100
- required gap = 178,700
- completionist proof = 610,400
- buffer = **16,300 EXP**

A broad completionist route can therefore reach Level 70 before Last Shelter without MH6 or repetitive grinding.

Lower-level enemy diminishing returns apply to ordinary/repeatable enemy-kill EXP only.

Fixed authored Side Quest, Character Quest, Hunt activity, and one-time story completion packages are exempt.

> **WEAK ENEMIES DIMINISH — AUTHORED CONTENT DOES NOT**

For Regional Hunts, the package may be split among route enemy EXP, boss EXP, and deterministic first-clear remainder. Do not make route RNG or diminishing returns lower the authored total; restore any shortfall in the first-clear remainder.

---

# Equipment / Relic / Legacy firewall

Current active equipment catalog:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- **91 total**

Hierarchy:
> **Ordinary < Relic < Legacy**

Exact 38/38 ordinary-equipment source/numeric architecture remains closed under Audit118.

Audit121 locks all **17/17 native Legacy** raw stats, perks, and Traits and the current Relic cleanup deltas.

Key slot rules:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik Two-Handed Sword — Weapon + Secondary.
- Nimera ordinary/surviving Relic Conduits — one-slot where currently authored.
- Nimera native Legacy Conduit — Weapon + Secondary.

Native Legacy completion retains the compatible Base/Character Quest/component/precursor/Gate-A/Gate-B/Kessara requirements. Native Legacy does not require Synthesis.

Relic copies remain limited to the current authored copy rule after the original is obtained. Legacies remain unique.

No equipment may depend on Barrier, Brace, or a global Break/Stagger meter.

---

# Consumables / economy firewall

Current consumables = **20**.

Currency = **Auren**; **1 economy unit = 20 Auren**.

HP:
- Field Salve — 250 HP / 20 Auren
- Restorative Salve — 750 HP / 50 Auren
- Vital Salve — 1,500 HP / 120 Auren
- Grand Salve — 2,250 HP / 240 Auren
- Company Salve — 30% Max HP to all conscious active party / 200 Auren

MP:
- Flow Tonic — 50 MP / 80 Auren
- Deepflow Tonic — 80 MP / 200 Auren
- Highflow Tonic — 120 MP / 360 Auren
- Reservoir Tonic — 75% Max MP / reward-only

Revival:
- Rousing Salts — revive at 25% Max HP
- Greater Rousing Salts — revive at 50% Max HP + 25% Max MP

Current normal-stock cure/tactical items:
- Trauma Remedy — Burn/Bleed
- Stability Remedy — Freeze/Stun/Staggered
- General Remedy — one eligible ordinary harmful status
- Full Remedy — all eligible ordinary harmful statuses
- Blinding Mist — eligible ordinary random-encounter escape
- Null Seal — remove one eligible enemy positive effect
- Balance Seal — ordinary negative stat changes toward normal

Reward-only:
- Emergency Kit — 75% Max HP + 60% Max MP + current eligible cleanse/stat restoration; no revive
- Emergency Rally — revive all unconscious active-party members at 60% Max HP + 35% Max MP; no cleanse/stat restoration

Do not restore the old 21-consumable count or Barrier-dependent consumables.

---

# Commerce / place-name firewall

Regional Markets:
- Brackenwall
- Dunmere
- Caelora
- Ivorybridge
- Stonewake
- Frostmere
- **Westguard**
- Larkspire
- Cerythvale

Westguard replaces Westreach and Yahtrens Stand.

Greenhollow, Ashford, Veycross, Deepforge, and Emberforge are not Regional Markets.

Cresthaven Quartermaster remains the full normal-stock consolidation/requisition endpoint.

Vhalmarch is forward supply/requisition after capture, not a civilian Regional Market.

---

# Chapter 4 elemental firewall

Chapter 4 uses exactly:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed from the Chapter-4 regulation/research framework and their old functions are not reassigned.

The Seventh Reaction is emergent four-element behavior, not a seventh element or reusable player system.

Reaction Conduit replaces Elemental Hexarch.

Regulation Crucible uses four chambers with two active/targetable at once and the current rotation:
- Fire/Ice
- Lightning/Earth
- Fire/Lightning
- Ice/Earth

Former Wind speed inheritance and Water Barrier/restoration/stabilization inheritance are removed.

The live S022–S026 Markdown scripts and matching dialogue `.tres` resources are synchronized. Historical `SIXFOLD` strings may remain only as technical compatibility IDs and are not display/lore/mechanical authority.

Cinder Judgment comes from the Reaction Annex/regulation-system protected cache.

---

# Post-insertion chapter-number firewall

The game has Chapter 0 plus Chapters 1–13.

Current late-game numbering:
- Chapter 10 — **The Last Blank**
- Chapter 11 — **Crown Engine**
- Chapter 12 — **The Reforged March**
- Chapter 13 — **The Last Command**

Historical translation:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Never implement the pre-insertion late-game numbering.

---

# Current open progression implementation work

The following remain open after Audit124:
1. Light / Standard / Heavy formation EXP tables;
2. exact formation CEXP values;
3. chapter-by-chapter ordinary EXP/CEXP shares;
4. named/story EXP and CEXP remainder placement;
5. progression-dependent named-enemy/boss raw-stat recertification.

Do **not** reopen class Ability MP, the 6,000-CEXP curve, the eight-point Mastery schedule, Ch12 class-level completion, Last Shelter Lv60, ending Lv62, or the 195,000 pre-Last-Shelter optional EXP pool merely because formation allocation is still pending.
