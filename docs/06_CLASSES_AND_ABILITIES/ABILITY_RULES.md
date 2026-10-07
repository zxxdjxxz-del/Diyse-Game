# Diyse — Ability Rules

**Status:** ACTIVE CLASS / ABILITY STRUCTURAL AUTHORITY  
**Authority:** current class-domain owner plus `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.  

## Lived-world identity

Character Abilities are natural forms of magic/technique expressed through the person using them. In-world characters do not experience ordinary trained Ability use as game commands or artifact powers.

## Universal native-Ability rules

- **MP** is the ordinary native-Ability resource.
- There is no separate class-specific combat gauge by default.
- Native Abilities generally cost less MP than comparable Standard Cards.
- Global timing, targeting, damage/healing, crit, elements, statuses, Delay/Interrupt, and cancellation rules are owned by the battle master.
- Native damage normally scales from Strength for physical output or Magic for magical output unless the Ability explicitly defines another current rule.
- Native scalable healing uses **Spirit**.
- Equipment does not secretly choose an Ability's source stat or output type.

## Required authored data

Every native Ability must explicitly define:

- MP Cost
- Execution category
- Return category
- Targeting
- Potency or fixed magnitude
- Physical / Magical / Other type where relevant
- Element if any
- crit eligibility
- queued-action interaction class: Interruptible / Delay-only / Uninterruptible
- status application chance if any
- timeline effect such as Delay/Interrupt if any
- explicit conditions/special rules

No Ability should rely on hidden timing assumptions.

A legal direct-damage Ability hits by default under the current battle system unless an explicit miss/evade mechanic applies. Do not assign legacy Base Hit values as a universal requirement.

Scalable direct-damage Abilities use **Potency**, not the former Power-100 scale. See `../05_BATTLE_SYSTEM/ACTION_POWER_REQUIREMENT.md`.

## Kit architecture

Current system targets:

- Base class: **6–8 active Abilities**
- Subclass: **4–6 active Abilities**
- fully developed native toolkit: roughly **10–14 active Abilities**
- Base class: **4 passives**
- Subclass: **3 passives**
- fully developed total: **7 passives**

Starting characters begin with **3 base active Abilities + 1 base passive**.

When subclass access is gained, it immediately grants **2 subclass active Abilities + 1 subclass passive**.

Base and subclass Abilities share one top-level **Abilities** command with visible origin tags; no extra Base/Subclass submenu is required.

## Content rebuild boundary

Existing Ability/passive sheets are source material, not constraints under the redesigned battle system. Individual actions/passives may be kept, reworked, renamed, merged, moved between active/passive or base/subclass space, or replaced.

Exact character-kit rebuilding and exact CL unlock thresholds are intentionally parked for the dedicated class-content pass.
