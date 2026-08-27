# Diyse — Current Implementation Status

**Written authority checkpoint:** **v2.07 / Audit122**  
**Presentation target:** HD-2D  
**Active repository:** `zxxdjxxz-del/Diyse-Game`

## Current closure / implementation state

- Chapters **0–4** remain COMPLETE/CLOSED at story/dialogue authority level.
- Chapters 0–4 HD-2D Conversion Audit Pass 1: COMPLETE / APPROVED.
- Shared HD-2D runtime foundation: IMPLEMENTED.
- Detailed later-chapter scene/runtime implementation remains pending where not separately completed.
- **Audit122** supplies the exact Base Hit/Evasion resolver and current Bleed runtime.
- **Audit121** supplies current system removals, class/Face names, final 17/17 Legacy mechanics, Relic cleanup deltas, 20-consumable economy/placement, Chapter-4 four-element reconciliation, commerce/location corrections, Prime numeric sync, and the Lv62 class-completion target.
- **Audit120** supplies compatible Physical/Magical/Hybrid direct-damage and Critical rules.
- **Audit118** remains the implementation source for the closed 38/38 ordinary-equipment catalog and compatible Relic/Forge data.
- The **class Ability MP check/certification remains OPEN**.
- The **CEXP / Mastery / player-level progression redo remains OPEN**.

---

# Combat implementation guardrails

## Direct damage

> **BasePhysicalDamage = [Attack² / (Attack + EffectiveDefense)] × (Power / 100)**

> **EffectiveDefense = CurrentDefense × (1 - EffectiveDefensePenetration)**

> **BaseMagicalDamage = [Magic² / (Magic + EffectiveSpirit)] × (Power / 100)**

> **EffectiveSpirit = CurrentSpirit × (1 - EffectiveSpiritPenetration)**

- Physical = Attack vs Defense.
- Magical = Magic vs Spirit.
- Spirit is the magical-defense stat.
- same-axis penetration cap = 75%.
- no universal random damage variance.

## Base Hit / Evasion — CLOSED

> **AdjustedBaseHit = round(ActionBaseHit × BaseHitPercentModifiers) + FlatBaseHitModifiers**

> **EffectiveEvasion = round(BaseEvasion × EvasionPercentModifiers) + FlatEvasionModifiers**

> **FinalHitChance = clamp(AdjustedBaseHit - EffectiveEvasion, 5, 100)**

Do not implement a natural Accuracy stat.

Normal authoring bands:
- standard ~100 Base Hit
- heavy 90–95
- precision 105–115
- exceptional precision up to ~120

## Critical
- base chance 5%
- flat percentage-point bonuses
- ordinary random cap 50%
- eligible multiplier 1.5×
- hit/evasion resolves first
- no Critical roll on a miss
- Crit does not bypass Defense/Spirit or automatically improve status application.

## Removed systems
- Barrier does not exist.
- Brace does not exist.
- no global Break/Stagger meter.
- Staggered is an ordinary harmful status only.
- Guard remains valid.

## Bleed
- damages each round and again when the affected character acts;
- old one-proc-per-round restriction is retired;
- clears only on full-HP restoration, eligible harmful-status clear, or eligible item;
- partial healing/Regen does not clear it unless full HP is reached or an explicit valid status clear is included.

---

# Standard Cards / Primes

Standard Cards:
- exactly 24
- maximum 3 equipped
- reusable and MP-consuming
- current MP range 18–48
- Acuity quartet = Faultline Sight / Measured Response / Predicted Impact / Decisive Interval
- Predicted Impact = Magical/Colorless, P180, BH110, 28 MP, 30% Stun.

Prime Invocation:
- Recovered Story — 50 MP
- Awakened Story — 80 MP
- Awakened Major Hunt — 90 MP
- manifested commands — 0 additional MP

Prime progression = **Recovered → Awakened**.

Current numeric sync:
- Prismatic Deluge = 90 × 4 = 360 listed Power per target
- Regulator Fang = 250 Power / 25% Spirit penetration

---

# Current class / Mastery implementation state

| Character | Base | Subclass | Face |
|---|---|---|---|
| Cyanis | Crest Knight | Crest Arcanist | Might |
| Ilyra | Blue Warden | Vowblade | Grace |
| Torren | War Archer | Routeweaver | Acuity |
| Nimera | Cardweaver | Proofhunter | Change |
| Vaelira | Green Arcanist | Axiomblade | Elements |
| Seyrik | Ruin Vanguard | Ruin Warden | Ruin |

Base/Subclass cap = **CL13**.

No permanent Subclass use before Sixfold Volition at end-Ch7.

Synthesis is removed.

Exactly 8 active Masteries:
- 4 Core
- 4 Subclass

Eligibility:
- Core — Base CL3 / CL6 / CL9 / CL12
- Subclass — CL3 / CL5 / CL7 / CL11
- Subclass Mastery 3 purchase → donor Relic access
- Subclass Mastery 4 / Legacy Mastery purchase → donor Legacy access

Donor pairs:
- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

Donor access equips the existing obtained item. No duplicate shared artifact.

Exact 8-point Mastery grant timing is OPEN and must close with the CEXP redo.

---

# Equipment implementation state

Current catalog:
- 38 ordinary
- 36 Relics
- 17 native Legacies
- **91 total**

The 38/38 ordinary source/stat/shop architecture is closed.

All **17/17 Legacy raw stats/perks/Traits are final under Audit121**.

Current equipment must not depend on Barrier, Brace, or a global Break/Stagger meter.

Hierarchy:

> **Ordinary < Relic < Legacy**

Remaining item/equipment work is implementation/naming polish unless explicitly reopened.

---

# Consumable / economy implementation state

Current count = **20**.

Currency = **Auren**; 1 economy unit = 20 Auren.

Fixed Salves:
- Field 250 HP / 20 Auren
- Restorative 750 HP / 50 Auren
- Vital 1,500 HP / 120 Auren
- Grand 2,250 HP / 240 Auren

Company Salve = 30% Max HP to all conscious active-party members / 200 Auren.

MP:
- Flow 50 / 80 Auren
- Deepflow 80 / 200 Auren
- Highflow 120 / 360 Auren
- Reservoir 75% Max MP / reward-only / 640 Auren equivalent

Revive:
- Rousing Salts = 25% Max HP / 60 Auren
- Greater Rousing Salts = 50% Max HP + 25% Max MP / 160 Auren

Emergency Kit and Emergency Rally are reward-only with their Audit121 values and placements.

---

# Chapter 4 implementation state

Exactly four standard elements are used in the Chapter-4 regulation/research system:
- Fire
- Ice
- Lightning
- Earth

Wind and Water are removed and their old functions are not reassigned.

The Seventh Reaction is emergent four-element behavior, not a seventh element or player combat system.

Reaction Conduit replaces Elemental Hexarch.

Regulation Crucible uses the Audit121 four-chamber/two-active architecture.

---

# Current progression / enemy numerical status

Current hard direction:
- player level cap 70
- Chapter 0 grants no character levels
- slower player progression through Ch1–7
- faster growth after Ch7
- normal full class completion target ≈ **player Lv62**
- Lv62–70 should provide meaningful full-build play.

Still OPEN:
1. class Ability MP check/certification;
2. full CEXP/class-progression redo;
3. exact 8-point Mastery schedule;
4. Ch1–13 player/enemy level bands;
5. encounter counts / formation EXP / diminishing returns;
6. progression-dependent named-enemy/boss recertification.

Do not implement old exact progression tables or the simulation-only Lv5/10/15/20/Volition/40/50/60 Mastery schedule as final.

---

# Current late-game chapter structure

- Chapter 10 — The Last Blank
- Chapter 11 — Crown Engine
- Chapter 12 — The Reforged March
- Chapter 13 — The Last Command

Historical mapping:
- old Ch10 → current Ch11
- old Ch11 → current Ch12
- old Ch12 → current Ch13

Do not wire runtime content against the old numbering.
