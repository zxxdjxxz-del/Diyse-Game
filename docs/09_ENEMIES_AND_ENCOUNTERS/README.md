# 09_ENEMIES_AND_ENCOUNTERS

**Status:** ACTIVE ENEMY / ENCOUNTER DOMAIN ROUTER  
**Authority:** current enemy/encounter owner plus later explicit approved corrections.  

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
- enemy stat records;
- encounter-composition references.

Global battle timing, formulas, targeting, statuses, elements, Delay/Interrupt, crit/hit rules, and battle-state resolution are owned by `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.
Player/formation EXP and CEXP budgets remain in `../10_PROGRESSION_AND_EXP`.
Quest unlock/reward presentation belongs in `../11_QUESTS`.

## Current difficulty hierarchy

> **baseline ordinary enemy < strong normal-pool enemy < mandatory story boss < Regional Hunt < Major Hunt**

This is a design hierarchy, not a rule that every later encounter must have more HP than every earlier one.

**Optional-combat rule:** Hunts are the default standalone optional enemy category. Quest-owned combat remains governed by its owning quest. A non-Hunt standalone optional encounter requires an explicit current story/encounter owner; Chapter 4's placement-reopened **Annex Duelist** is the current named exception pending that chapter's enemy rework. Stronger normal identities belong to the ordinary enemy pool; there is no separate Elite encounter category.

## Battle-redesign boundary

Enemy identities, encounter placement, ecology, authored roles, and form architecture remain valid where not otherwise changed.

Exact enemy combat stats, action kits, status riders, action timing, Potencies, and numerical difficulty tuning are **open for the enemy/balance rebuild**. Existing leaf sheets may be used as source material, but they cannot override the current battle-system master where they still carry incompatible combat fields or mechanics.

Current enemy data must not treat the following as universal core stats/mechanics:

- Accuracy;
- Evasion;
- Status Resistance;
- legacy action Power/Base Hit fields;
- discrete-round timing.

Future enemy stat/action records must resolve through the battle master's HP/offense/Defense/Spirit/Speed, Potency/fixed-effect, status-susceptibility, and TURN / EXECUTION rules as applicable.

## Current roster organization

Chapter 0 through Chapter 13 are stored under `CHAPTER_ENEMIES/`.

Important current reindex:
- Chapter 10 = **The Last Blank**
- Chapter 11 = **Crown Engine / Calder / Custodian**
- Chapter 12 = **The Reforged March / Black Host Territory**
- Chapter 13 = **The Last Command / final domain**
