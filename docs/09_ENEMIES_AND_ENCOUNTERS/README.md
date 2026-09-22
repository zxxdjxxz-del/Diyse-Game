# 09_ENEMIES_AND_ENCOUNTERS
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary enemy-production authority:** compatible **Audit90 / Audit93** plus accepted later tracker roster/action cleanups.  
**Primary raw-stat authority:** **Audit129 + Audit130 / Audit131 / Audit132 / Audit133 / Audit134 / Audit135**.  
**Current whole-project written authority:** **v2.20 / Audit135**.  
**Migration rule:** later current names, chapter reindexing, four-element rules, removed-system firewalls, and fresh-body Prime-refresh rules supersede stale earlier enemy text.


Canonical home for:
- chapter enemy rosters;
- ordinary-enemy ecology and reuse;
- authored/nonlethal enemy roles;
- support objects;
- strong normal-pool Elite identities;
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

> **Ordinary < strong normal-pool Elite < mandatory story boss < Regional Hunt < Major Hunt**

This is a design hierarchy, not a rule that every later encounter must have more HP than every earlier one.

**Optional-combat rule:** Hunts are the only standalone optional enemy/Elite encounters. Quest-owned combat remains governed by its owning quest. Elite-strength identities belong to normal encounter pools; there is no separate optional-Elite combat category.

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
