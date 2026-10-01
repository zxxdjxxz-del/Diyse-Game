# 09_ENEMIES_AND_ENCOUNTERS
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Historical enemy-production provenance:** Audit90/Audit93 plus later tracker-era roster/action cleanups.
**Historical raw-stat provenance:** Audit129–Audit135.
**Authority treatment:** this repository file is current enemy-domain authority; Audit/v85 references remain historical provenance only.
**Migration rule:** current repository names, chapter placement, system firewalls, and Prime-restoration rules supersede conflicting historical enemy text.


Canonical home for:
- chapter enemy rosters;
- ordinary-enemy ecology and reuse;
- authored/nonlethal enemy roles;
- support objects;
- strong normal-pool enemy identities;
- mandatory named encounters and bosses;
- Regional Hunts;
- Major Hunts;
- boss form architecture;
- enemy raw-stat records;
- encounter-composition references.

Global battle math remains in `05_BATTLE_SYSTEM`.
Player/formation EXP and CEXP budgets remain in `10_PROGRESSION_AND_EXP`.
Quest unlock/reward presentation belongs in `11_QUESTS`.

## Current difficulty hierarchy

> **baseline ordinary enemy < strong normal-pool enemy < mandatory story boss < Regional Hunt < Major Hunt**

This is a design hierarchy, not a rule that every later encounter must have more HP than every earlier one.

**Optional-combat rule:** Hunts are the only standalone optional enemy encounters. Quest-owned combat remains governed by its owning quest. Stronger normal identities belong to the ordinary enemy pool; there is no separate Elite encounter category.

## Current raw-stat fields

Enemy raw bodies use:
- Level
- HP
- Attack
- Magic
- Defense
- Spirit
- Speed
- Evasion
- Status Resistance

There is no natural Accuracy stat.

## Current roster organization

Chapter 0 through Chapter 13 are stored under `CHAPTER_ENEMIES/`.

Important current reindex:
- Chapter 10 = **The Last Blank**
- Chapter 11 = **Crown Engine / Calder / Custodian**
- Chapter 12 = **The Reforged March / Black Host Territory**
- Chapter 13 = **The Last Command / final domain**

Do not use pre-insertion chapter numbers to relocate those rosters.
