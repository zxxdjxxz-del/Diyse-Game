# Diyse — Hunt Quest/Presentation Boundary
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted tracker-level quest reductions/corrections and the already-migrated current story/world/progression domains.  
**Quest architecture provenance:** compatible Audit103, superseded where later current working authority changes quest counts, boss distribution, geography, terminology, rewards, or final access timing.  
**Domain rule:** this folder owns optional-activity identity, unlocks, objectives, route/area flow, quest-state outcomes, combat/no-combat classification, completion conditions, and world-state payoff. Exact enemy kits/stats live in `09_ENEMIES_AND_ENCOUNTERS`; exact EXP/CEXP in `10_PROGRESSION_AND_EXP`; item/equipment mechanics in `08_ITEMS_AND_EQUIPMENT`; exact dialogue in `03_DIALOGUE`.


Hunts are optional combat activities with quest-like:
- discovery;
- access;
- world-map markers;
- return loops;
- first-clear reward presentation.

But mechanically/content-structurally they remain:
- **Regional Hunts**
- **Major Hunts**

not ordinary Side Quests.

## Ownership
`11_QUESTS`:
- unlock/access context;
- optional-content presentation;
- returnability;
- first-clear quest-state handoff.

`09_ENEMIES_AND_ENCOUNTERS`:
- enemy body/forms;
- HP/stats;
- AI/actions;
- support objects;
- status conversion;
- fixed tuning.

`07_CARDS`:
- Major-Hunt Prime reward.

`10_PROGRESSION_AND_EXP`:
- Hunt Player EXP/CEXP.

## Tuning
Current Hunts use:
> **fixed authored tuning**

No dynamic player-level scaling.
