# Diyse — Ability Rules

**Status:** ACTIVE CLASS / ABILITY STRUCTURAL AUTHORITY  
**Authority:** current class-domain owner plus `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.

Character Abilities are natural forms of magic/technique expressed through the person using them.

## Universal native-Ability rules

- MP is the ordinary native-Ability resource.
- There is no separate class-specific combat gauge by default.
- Native Abilities generally cost less MP than comparable Standard Cards.
- Physical native offense normally scales from **Strength**.
- Magical native offense normally scales from **Magic**.
- Native scalable healing uses **Spirit**.
- Global timing, targeting, damage/healing, crit, elements, statuses, Delay/Interrupt, cancellation, and retargeting are owned by the battle master.

## Required authored data

Every rebuilt native Ability must explicitly define:

- MP Cost
- Execution category
- Return category
- Targeting
- Potency or fixed magnitude
- output type
- element where relevant
- crit eligibility
- Interruptible / Delay-only / Uninterruptible classification
- status application chance where relevant
- explicit timeline effect where relevant
- conditions and special rules

A legal direct-damage Ability hits by default unless an explicit current effect creates a miss/evade interaction.

## Kit architecture

- Base Class: **6–8 active Abilities**
- Subclass: **4–6 active Abilities**
- combined mature toolkit: roughly **10–14 active Abilities**
- Base Class: **4 passives**
- Subclass: **3 passives**

Starting characters begin with **3 Base active Abilities + 1 Base passive**.

Subclass access grants **2 Subclass active Abilities + 1 Subclass passive** immediately.

Exact content and CL unlock thresholds remain open for the dedicated class rebuild.
