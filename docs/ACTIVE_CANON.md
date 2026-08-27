# Diyse — Active Engineering Canon Guardrails

This file is the implementation-facing authority index and compact guardrail summary. It does **not** replace the canon audits. Compatible older locks remain active where not superseded. If this file conflicts with a later explicit approved correction, the later authority wins.

## Current whole-project authority

**Diyse: HD-2D JRPG Clean Active Complete Master Canon v2.06 / Audit121 — Current Systems, Item/Equipment, and Progression Reconciliation Lock**  
**Date:** August 27, 2026

Current newest authority chain:

- **v2.06 / Audit121** — current system removals, classes/Faces, final Legacy set, Relic stale-mechanic cleanup, 20-consumable economy/placement, commerce/location terminology, Chapter-4 four-element rework, Prime numeric sync, Lv62 class-completion direction, and current OPEN progression/Ability-MP work.
- **v2.05 / Audit120** — compatible Physical/Magical/Hybrid direct-damage formula and Critical Hit system.
- **v2.04 / Audit119** — compatible Card/Prime MP, named resistance, Prime status/scaling, and progression architecture not changed by Audit121.
- **v2.03 / Audit118** — exact 38/38 ordinary-equipment source/numeric catalog and compatible Relic/Forge data not superseded by Audit121.
- **v2.02 / Audit117** — compatible equipment/Legacy/class-access structure and Synthesis removal.
- **v2.01 / Audit116** — compatible Standard-Card and Prime command definitions.
- **v2.00 / Audit115** — compatible global status/element/Ruin/class-Ability definitions.
- **v1.98 / Audit113** — current 13-chapter reindex.
- compatible older audits remain active where not superseded.

Current domain pointers:
- `docs/canon/AUDIT121_CURRENT_SYSTEMS_ITEM_EQUIPMENT_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT120_CRITICAL_HIT_AND_DIRECT_DAMAGE_FORMULA_LOCK.md`
- `docs/canon/AUDIT119_POST_AUDIT116_COMBAT_RESOURCE_PRIME_AND_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT118_COMPLETE_EQUIPMENT_TRACKER_DELTA_PROMOTION_AND_NUMERICAL_CATALOG_LOCK.md`
- `docs/canon/AUDIT117_ITEM_EQUIPMENT_LEGACY_AND_CLASS_PROGRESSION_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT116_STANDARD_CARD_PRIME_RESOURCE_AND_COMMAND_RECONCILIATION_LOCK.md`
- `docs/canon/AUDIT115_COMBAT_RUIN_STATUS_AND_FULL_CLASS_ABILITY_NORMALIZATION_LOCK.md`
- `docs/canon/AUDIT113_POST_INSERTION_CHAPTER_REINDEX_AND_LATE_GAME_OPERATIONAL_FILE_RECONCILIATION_LOCK.md`

---

# Conflict order for current work

1. **Audit121** controls the domains it explicitly changes.
2. **Audit120** controls compatible direct-damage and Critical rules.
3. **Audit119** controls compatible Card/Prime resource/scaling/resistance/progression rules.
4. **Audit118** controls the compatible exact 38/38 ordinary-equipment catalog and Forge/source data.
5. **Audit117** controls compatible equipment/Legacy/class-access structure.
6. **Audit116** controls compatible Card/Prime command identities/effects.
7. **Audit115** controls compatible status/element/Ruin/class-Ability definitions.
8. **Audit113** controls current chapter labels.
9. Compatible older domain locks remain active.

Historical cumulative trackers are design history, not authority by themselves.

---

# Universal combat firewall

## Direct damage

Physical:

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

Magical:

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

Hybrid hits resolve authored Physical and Magical components independently, then combine them.

- Physical = Attack vs Defense.
- Magical = Magic vs Spirit.
- Spirit is the canonical magical-defense stat.
- same-axis penetration cap = **75%**.
- Basic Attack = 100 Power / Physical / Neutral unless equipment explicitly changes affinity.
- no universal random damage variance.

## Critical Hits

- base Critical Chance = **5%**;
- bonuses are flat percentage-point additions;
- ordinary random Critical Chance cap = **50%**;
- eligible Critical multiplier = **1.5×**;
- resolve Base Hit/Evasion before Critical Chance;
- eligible multihit direct hits roll independently by default;
- eligible Magical direct hits use the same 1.5× multiplier;
- Crit does not bypass Defense/Spirit;
- Burn, Bleed, explicitly no-Crit copied/echo damage, indirect Max-HP damage unless explicitly authored otherwise, and healing cannot Crit.

Use **Base Hit**, never `Accuracy`, as the canonical hit-stat term.

## Removed systems

- **Barrier does not exist.** Remove it from combat/damage-order/equipment/Ability/enemy/Card/Prime wording.
- **Brace does not exist.**
- There is **no global Break/Stagger meter**.
- **Staggered** is an ordinary harmful status only where explicitly authored.
- **Guard** remains valid.

---

# Elements / harmful statuses

Standard elements:
- Fire
- Ice
- Lightning
- Earth

Universal harmful statuses:
- Burn
- Freeze
- Stun
- Staggered
- Bleed

Ruin is a special affinity/school, not a fifth standard element.

Named-combat elemental multipliers remain:
- Weak 125%
- Neutral 100%
- Resistant 80%
- Strongly Resistant 60%
- Immune 0%

Named-combat harmful-status susceptibility remains:
- Normal 100%
- Resistant 80%
- Strongly Resistant 60%
- Immune 0%

---

# Current permanent classes / Faces

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | **Crest Arcanist** | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | **Acuity** |
| Nimera | Cardweaver | **Proofhunter** | Change |
| Vaelira | **Green Arcanist** | **Axiomblade** | Elements |
| Seyrik | Ruin Vanguard | **Ruin Warden** | Ruin |

Base and Subclass caps remain **CL13**.

No permanent character uses a Subclass before **Sixfold Volition at the end of Chapter 7**.

---

# Mastery / donor-access firewall

**Synthesis is removed.** Never implement a Synthesis node, cost, passive, Base+Subclass cap gate, or duplicate shared artifact.

Exactly:
- 4 Core Masteries
- 4 Subclass Masteries
- **8 active nodes total**

Core eligibility: Base CL3 / 6 / 9 / 12.

Subclass eligibility: CL3 / 5 / 7 / 11.

- purchase Subclass Mastery 3 at CL7 → linked donor Relic access;
- purchase Subclass Mastery 4 / Legacy Mastery at CL11 → linked donor Legacy access.

Donor pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

Linked access uses the donor's actual obtained item. Trait travels with the item. No duplicate artifact and no universal off-owner nerf.

A character's own native Legacy does **not** require Synthesis or donor Legacy Mastery.

Exact 8-point MP grant timing remains **OPEN** and must be finalized with the CEXP redo.

---

# Progression firewall

- Player level cap = **70**.
- Chapter 0 grants **no character levels**.
- Chapters 1–7 stay somewhat below a near-linear player-level curve.
- Faster level growth begins after Chapter 7.
- Current class-completion pacing target: **about player Lv62** for normal full class completion.
- Lv62–70 should provide meaningful full-build play.

Still OPEN:
- full CEXP/class-progression redo;
- exact 8-point Mastery Point schedule;
- final class Ability MP check/certification;
- detailed Ch1–13 EXP/enemy/encounter calibration;
- progression-dependent named-enemy/boss raw-stat recertification.

The simulation-only MP candidate Lv5/10/15/20/Volition/40/50/60 is **not final implementation canon**.

---

# Standard Cards

Exactly **24 Standard Cards**, maximum **3 equipped** per character.

Cards are reusable and MP-consuming. No draw/deck/discard/charge/duplicate/rank system.

Current exact MP costs remain the Audit119 table except where later explicitly revised.

Current Acuity quartet:
- Faultline Sight — 18 MP
- Measured Response — 24 MP
- Predicted Impact — 28 MP
- Decisive Interval — 36 MP

### Predicted Impact
- one enemy
- Magical / Colorless
- Power 180
- Base Hit 110
- 30% Stun on successful damaging hit
- no Break/Stagger-meter contribution

Previously open early acquisition homes are closed:
- Iron Testament — Ch1 Hollow Watch / Ancient-route protected cache
- Restoration — Ch2 Sunken Archive protected recovery/triage cache
- Sunder the Gate — Ch2 Red Transfer Bastion protected siege/access-control cache
- Cinder Judgment — Ch4 Reaction Annex/regulation-system protected cache

---

# Primes

Exactly **12 Primes**: 6 Story + 6 Major Hunt.

Progression:

> **Recovered → Awakened**

Current Invocation MP:
- Recovered Story — 50 MP
- Awakened Story — 80 MP
- Awakened Major Hunt — 90 MP
- manifested commands — 0 additional MP

Awakened Primes:
- suspend/replace the ordinary party;
- last exactly 3 Prime rounds;
- trigger a shared 3-full-normal-round cooldown after dismissal;
- once per identity per battle unless a genuine fresh-HP boss form refreshes availability.

No Prime XP, Prime levels, duplicates, or upgrade-material progression.

### Prismatic Deluge
All enemies; Magical elemental sequence:
- Fire 90
- Ice 90
- Lightning 90
- Earth 90
- **360 total listed Power per target**
- 15% linked status check per wave; maximum 1 new harmful status per target.

### Regulator Fang
- one enemy
- Magical
- choose Fire/Ice/Lightning/Earth
- **Power 250**
- **25% Spirit penetration**
- no harmful-status rider.

---

# Equipment / Relic / Legacy firewall

Current active equipment:
- **38 ordinary**
- **36 Relics**
- **17 native Legacies**
- **91 total**

Hierarchy:

> **Ordinary < Relic < Legacy**

Audit118 remains controlling for the current 38/38 ordinary-equipment catalog and compatible Relic/Forge data. Audit121 controls the finalized 17 Legacy stats/perks/Traits and the listed Relic stale-mechanic corrections.

Slot rules remain:
- Ilyra — Wardrod Primary; Shield or Focus Secondary.
- Torren Great Bow — Weapon + Secondary.
- Vaelira Arcane Staff — one-slot Primary; Focus legal.
- Seyrik 2H Sword — Weapon + Secondary.
- Nimera ordinary/surviving Relic Conduits — one-slot.
- Nimera native Legacy Conduit — Weapon + Secondary.

Native Legacy completion retains its established Base-class/Character Quest/component/precursor/gate requirements. Native Legacy does not require Synthesis.

All 17 native Legacies are mechanically final under Audit121. All current Legacies are unique; linked donor use shares the original item.

No current equipment Trait may depend on Barrier, Brace, or a global Break/Stagger meter.

---

# Consumables / economy — Audit121

Current Consumable count = **20**.

Currency = **Auren**.

> **1 economy unit = 20 Auren**

Fixed Salves:
- Field Salve — 250 HP — 20 Auren
- Restorative Salve — 750 HP — 50 Auren
- Vital Salve — 1,500 HP — 120 Auren
- Grand Salve — 2,250 HP — 240 Auren

Party HP:
- Company Salve — 30% Max HP to all conscious active-party members — 200 Auren

MP:
- Flow Tonic — 50 MP — 80 Auren
- Deepflow Tonic — 80 MP — 200 Auren
- Highflow Tonic — 120 MP — 360 Auren
- Reservoir Tonic — 75% Max MP — reward-only, 640 Auren equivalent

Revival:
- Rousing Salts — revive at 25% Max HP — 60 Auren
- Greater Rousing Salts — revive at 50% Max HP + 25% Max MP — 160 Auren

Remedies/tactical:
- Trauma Remedy — Burn/Bleed — 15 Auren
- Stability Remedy — Freeze/Stun/Staggered — 15 Auren
- General Remedy — one eligible ordinary harmful status — 50 Auren
- Full Remedy — all eligible ordinary harmful statuses — 140 Auren
- Blinding Mist — guaranteed escape from eligible ordinary random encounter — 10 Auren
- Null Seal — remove one eligible enemy positive effect — 70 Auren
- Balance Seal — restore eligible ordinary negative stat changes toward normal — 60 Auren

Reward-only emergency:
- Emergency Kit — 75% Max HP + 60% Max MP + established eligible cleanse/stat restoration; no revive — 300 Auren equivalent
- Emergency Rally — revive all unconscious active-party members at 60% Max HP + 35% Max MP; no cleanse/stat restoration — 500 Auren equivalent

Reward-only first guaranteed placements are locked in Audit121.

---

# Commerce / current place names

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

**Westguard** replaces Westreach and the intermediate Yahtrens Stand label.

Greenhollow, Ashford, Veycross, Deepforge, and Emberforge are not Regional Markets.

Cresthaven Quartermaster = full normal-stock consolidation/requisition endpoint.

Vhalmarch = forward supply/requisition after capture/stabilization, not a civilian Regional Market. Cresthaven remains the full ordinary-equipment catalog endpoint.

---

# Chapter 4 elemental firewall

Chapter 4 uses exactly:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed from the Chapter-4 research/regulation framework and their old functions are not reassigned.

The **Seventh Reaction** is emergent four-element system behavior, not a seventh element, Omni, Prismatic, Colorless, Wind/Water, or a reusable player system.

No global Composite Reaction table. No Imprint system.

**Reaction Conduit** replaces Elemental Hexarch and has four elemental expressions only.

Regulation Crucible:
- Fire/Ice/Lightning/Earth chambers;
- exactly 2 active/targetable at once;
- core always targetable;
- dormant chambers untargetable;
- destroyed chambers stay destroyed;
- rotation Fire/Ice → Lightning/Earth → Fire/Lightning → Ice/Earth;
- former Wind speed inheritance removed;
- former Water Barrier/restoration/stabilization inheritance removed;
- Form II is a fresh-HP/MP body and refreshes Prime availability under the global fresh-form rule.

Cinder Judgment's Chapter-4 source is the Reaction Annex/regulation-system protected cache.

---

# Post-insertion chapter-number firewall

The game has Chapter 0 plus Chapters **1–13**.

Current late-game numbering:
- Chapter 10 — The Last Blank
- Chapter 11 — Crown Engine
- Chapter 12 — The Reforged March
- Chapter 13 — The Last Command

Historical translation:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

---

# Current work frontier

Mechanically/content-architecture complete at current canon level:
- 20/20 consumables
- 38/38 ordinary equipment
- 36/36 Relics
- 17/17 Legacies

Next substantive balance passes:
1. **Class Ability MP check/certification**
2. **CEXP + Mastery + player-level progression redo**, targeting full class completion around Lv62

Do not reopen completed item/equipment architecture unless a later explicit decision does so.
