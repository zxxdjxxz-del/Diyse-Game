# Diyse — Formation Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary enemy-production authority:** compatible **Audit90 / Audit93** plus accepted later tracker roster/action cleanups.  
**Primary raw-stat authority:** **Audit129 + Audit130 / Audit131 / Audit132 / Audit133 / Audit134 / Audit135**.  
**Current whole-project written authority:** **v2.20 / Audit135**.  
**Migration rule:** later current names, chapter reindexing, four-element rules, removed-system firewalls, and fresh-body Prime-refresh rules supersede stale earlier enemy text.


- maximum simultaneously active enemies: **8**
- no fixed random-battle quota;
- Light/Standard/Heavy are encounter/reward planning tiers, not separate lore species;
- compositions should reflect local ecology and role synergy;
- carryovers keep their identity rather than being renamed for a later chapter;
- ordinary encounter counts remain stochastic planning centers;
- do not add enemies merely to make formation arithmetic hit a chapter quota.

## Optional-combat boundary — 2026-09-22
**Hunts are the only optional enemy encounters.**

Do not create or preserve a separate "optional Elite" / side-room enemy category.

Former optional-Elite identities are folded into their chapter/area's normal encounter pool as strong normal-pool enemies:
- repeatable identities may appear through ordinary formation selection;
- unique/named identities use a one-time normal-pool entry rather than being duplicated;
- they do not require a side room, optional branch, or separate optional-combat flag;
- "Elite" may still describe enemy strength/role, but not optional-content status.

Whole-formation EXP/CEXP economy is owned by `10_PROGRESSION_AND_EXP`. Converting former optional fights into normal-pool entries requires progression/reward revalidation where their prior optional rewards affected chapter budgets.

## Enemy action-selection fallback
Where a current owning enemy file lacks explicit action weights, use `../ACTION_SELECTION_DEFAULT.md`. Explicit current weights always override the fallback.
