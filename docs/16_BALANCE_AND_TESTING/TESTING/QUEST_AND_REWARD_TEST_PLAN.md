# Diyse — Quest / Reward Test Plan

**Status:** ACTIVE QUEST / REWARD QA PLAN  
**Quest authority:** `../../11_QUESTS/`  
**Reward-number authority:** `../../10_PROGRESSION_AND_EXP/` and `../../12_ECONOMY_AND_REWARDS/`

## Counts
Current:
- **6** Character Quests;
- **5** ordinary Side Quests;
- **8 active Regional Hunts**;
- **6** Major Hunts.

## Character Quests
Verify:
- unlock window;
- correct location;
- current boss/no-boss architecture;
- completion flag;
- unique Legacy Component granted exactly once;
- no direct finished Legacy reward unless equipment authority says so.

## Side Quests
Verify only the current five quest identities from `11_QUESTS`. Retired quests must not remain in the active quest registry or reward totals.

## Hunts
Verify:
- current unlock/access;
- recommended level is display guidance, not an access gate;
- first-clear reward exactly once;
- Major-Hunt Prime acquired Awakened;
- Major Hunt #6 dual gate;
- no dynamic player-level scaling.

## Reward boundary
Exact EXP/CEXP/G values are rebuild/recalibration inputs and must be tested against the current owner, not historical balance snapshots.

## Final cutoff
Entering Chapter 13 does not automatically close optional content.

True cutoff:
> **Last Shelter → Reactor Galleries**
