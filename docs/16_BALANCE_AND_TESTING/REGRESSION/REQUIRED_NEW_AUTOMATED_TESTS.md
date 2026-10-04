# Diyse — Required New Automated Tests

**Status:** ACTIVE AUTOMATED-TEST BACKLOG  
**Balance/QA authority:** `../README.md`

High-value production regressions:

## Combat formulas
- physical/magical/hybrid
- penetration cap
- Base Hit/Evasion clamp
- crit cap/multiplier/order
- status resolver.

## Round logic
- max4 active party
- max8 enemies
- normal round order begins from current effective Speed and the current tie rules
- each actor selects/chooses and resolves its action on that actor's turn
- player decisions use the battle state produced by earlier turns in the same round
- enemy/entity AI chooses from the legitimate state when its turn arrives
- Item and Defend do **not** receive universal priority phases
- there is no whole-party action queue / universal Confirm Round gate
- initiative remains locked for the current round after setup; mid-round Speed changes affect the next round only if still active
- no Speed extra actions unless explicitly authored
- legal retarget behavior.

## Status

Full matrix in `../TESTING/STATUS_REGRESSION_MATRIX.md`.

## Primes

Full current matrix in `../TESTING/PRIME_REGRESSION_MATRIX.md`.

## Equipment
- three slots only
- two-slot commitments
- Ilyra Wardrod/Shield-or-Focus
- Relic copy
- Legacy no-copy.

## Progression
- Lv70 threshold
- chapter mandatory EXP totals after the progression rebuild
- weak-enemy DR
- no CEXP DR
- no Ch0 levels
- no pre-Volition Subclass.

## CEXP

After rebalance:
- explicit class-completion timing regression around the final **Lv55–60** route target.

Do not freeze the current provisional model before rebalance.

## Content counts
- 78 Ability/Ultimate entries
- 24 Standard Cards
- 12 Primes
- 91 equipment
- 20 Consumables
- 30 Forge Components
- 5 Side Quests
- 6 Character Quests
- 8 active Regional Hunts
- 6 Major Hunts.

## Current terminology

Automated current-facing data validation should enforce the owning registries directly:
- Faces exactly: **Might / Elements / Grace / Perception / Memory / Ruin**;
- current world/region names from `04_WORLD_AND_LORE`;
- ordinary player-facing currency: **G**;
- current battle commands/status/mechanics from `05_BATTLE_SYSTEM`;
- current class names from `00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`.

Tests should validate the current allowed set directly from owning registries.
