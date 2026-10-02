# 09_ENEMIES_AND_ENCOUNTERS

**Status:** ACTIVE ENEMY / ENCOUNTER DOMAIN ROUTER  
**Authority:** current enemy/encounter owner plus later explicit approved corrections.  
**Provenance policy:** active authority files state current ownership/status directly. Historical Audit/v## tracker labels belong in Git history and should not be repeated as live authority metadata.  
**Balance-validation policy:** historical chapter PASS/v## snapshots are not current certification. Current difficulty certification must use `../16_BALANCE_AND_TESTING/BALANCE/ENEMY_BOSS_MANDATORY_COMPLETIONIST_VALIDATION.md` with current enemy, formation, party, and progression inputs.  


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
