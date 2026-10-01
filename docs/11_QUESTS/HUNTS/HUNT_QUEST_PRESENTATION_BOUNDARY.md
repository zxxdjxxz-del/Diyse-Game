# Diyse — Hunt Quest/Presentation Boundary
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current quest-domain authority. Audit/v85 references remain provenance only; exact EXP/CEXP values are owned by `10_PROGRESSION_AND_EXP` and remain provisional pending the planned progression rebuild.
**Historical quest-architecture provenance:** Audit103 plus later accepted quest reductions/corrections.
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
