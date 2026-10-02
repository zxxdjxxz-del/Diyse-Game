# Diyse — Formation Rules
**Status:** CURRENT FORMATION-DOMAIN RULES  
**Authority:** current formation rules plus later explicit approved corrections. Historical tracker/Audit provenance remains in Git history.


- maximum simultaneously active enemies: **8**
- no fixed random-battle quota;
- Light/Standard/Heavy are encounter/reward planning tiers, not separate lore species;
- compositions should reflect local ecology and role synergy;
- carryovers keep their identity rather than being renamed for a later chapter;
- ordinary encounter counts remain stochastic planning centers;
- do not add enemies merely to make formation arithmetic hit a chapter quota.

## Optional-combat boundary — 2026-09-22
**Hunts are the only standalone optional enemy encounters. Quest-owned combat remains governed by its owning quest.**

Do not create or preserve a separate Elite / side-room enemy category.

Former Elite-design identities that remain current are folded into their chapter/area's normal encounter pool as strong normal-pool enemies:
- repeatable identities may appear through ordinary formation selection;
- unique/named identities use a one-time normal-pool entry rather than being duplicated;
- they do not require a side room, optional branch, or separate optional-combat flag;

Whole-formation EXP/CEXP economy is owned by `10_PROGRESSION_AND_EXP`. Converting former optional fights into normal-pool entries requires progression/reward revalidation where their prior optional rewards affected chapter budgets.

## Enemy action-selection fallback
Where a current owning enemy file lacks explicit action weights, use `../ACTION_SELECTION_DEFAULT.md`. Explicit current weights always override the fallback.
