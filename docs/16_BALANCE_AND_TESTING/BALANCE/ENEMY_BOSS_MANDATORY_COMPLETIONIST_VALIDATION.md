# Diyse — Mandatory vs Completionist Validation Framework

**Status:** ACTIVE VALIDATION FRAMEWORK  
**Balance/QA authority:** `../README.md`

This file owns the comparison method and acceptance record format. It does **not** own chapter story structure, enemy rosters/formations, progression totals, equipment catalogs, rewards, or Prime mechanics.

## Current-source rule

For every validation point, read current inputs from their owners:
- story/party/recruitment state — `02_STORY`;
- enemy identity, placement, formations, stats, and action kits — `09_ENEMIES_AND_ENCOUNTERS`;
- Player EXP/CEXP and level/class snapshots — `10_PROGRESSION_AND_EXP`;
- equipment/items — `08_ITEMS_AND_EQUIPMENT`;
- Cards/Primes — `07_CARDS`;
- economy/rewards — `12_ECONOMY_AND_REWARDS`.

Never reconstruct a current chapter from an old balance snapshot.

## Route baselines

### Mandatory / critical-path
Use only guaranteed progression and resources available before the encounter.

### Completionist / high-side
Use plausible optional content available before the same encounter without assuming arbitrary grind beyond authored content.

## Core comparison rule

Where practical, hold constant:
- ordinary equipment tier/loadout;
- normal-stock consumable preparation;
- active four;
- competent tactical policy.

Let real route differences come from:
- Player Level;
- CEXP / learned abilities;
- optional Cards/Primes when separately tested;
- other legitimately earned progression.

Prime-specific burst/access stress may be measured separately so it does not hide the underlying progression signal.

## Required record per encounter

Record:
- exact current encounter identity;
- current party availability and active-four choice;
- mandatory and completionist Player Level/CEXP state;
- equipment/consumable assumptions;
- Cards/Primes used;
- temporary-KO incidence;
- wipe incidence;
- ending HP/MP;
- item/recovery pressure;
- mechanic-response pressure;
- duration/round count;
- any implementation or data discrepancy found.

## Acceptance principles

- mandatory route must remain beatable without optional grinding;
- mandatory route should still create meaningful pressure appropriate to the encounter;
- optional progression should provide an earned safety/power advantage;
- fixed encounters do not dynamically scale to erase completionist advantage;
- duration alone is not sufficient proof of difficulty;
- a failed validation may reopen an owning value, but this framework never silently edits another domain.

## Current frontier

Enemy action-kit/difficulty tuning is reopened. Exact EXP/CEXP and G placement are also rebuild-pending.

Therefore current chapter-by-chapter historical validation snapshots are not certification. Re-run this framework only after the relevant current inputs are stable enough to test.
