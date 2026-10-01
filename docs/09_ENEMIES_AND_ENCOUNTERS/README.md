# 09_ENEMIES_AND_ENCOUNTERS

**Status:** ACTIVE ENEMY / ENCOUNTER DOMAIN ROUTER  
**Authority:** current enemy/encounter-domain owner plus later explicit approved corrections.  


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


## Balance / numeric authority boundary

This domain's **current identity, placement, encounter architecture, status/mechanic intent, and owner routing** are live authority.

Exact raw stats, action Powers/kits, recommended levels, and mandatory-vs-completionist difficulty claims remain subject to the active enemy/progression recertification frontier unless a newer explicit owner locks them after that rebuild.

Old v80–v106 `PASS`, `FORMALLY VALIDATED`, `POWER COMPLETE`, and true-battle certification labels are historical evidence only and must not be treated as current release certification.

Use:
- current enemy/boss/Hunt owner files for working implementation inputs;
- `../16_BALANCE_AND_TESTING/BALANCE/ENEMY_BOSS_MANDATORY_COMPLETIONIST_VALIDATION.md` for the current comparison method;
- `../16_BALANCE_AND_TESTING/OPEN_BALANCE_ITEMS.md` for the active rebuild frontier.
