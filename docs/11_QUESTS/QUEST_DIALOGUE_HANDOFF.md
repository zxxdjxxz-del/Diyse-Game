# Diyse — Quest → Dialogue Handoff
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted tracker-level quest reductions/corrections and the already-migrated current story/world/progression domains.  
**Quest architecture provenance:** compatible Audit103, superseded where later current working authority changes quest counts, boss distribution, geography, terminology, rewards, or final access timing.  
**Domain rule:** this folder owns optional-activity identity, unlocks, objectives, route/area flow, quest-state outcomes, combat/no-combat classification, completion conditions, and world-state payoff. Exact enemy kits/stats live in `09_ENEMIES_AND_ENCOUNTERS`; exact EXP/CEXP in `10_PROGRESSION_AND_EXP`; item/equipment mechanics in `08_ITEMS_AND_EQUIPMENT`; exact dialogue in `03_DIALOGUE`.


`11_QUESTS` owns:
- premise;
- objective flow;
- quest giver;
- route;
- interaction function;
- combat classification;
- completion condition;
- world-state result.

`03_DIALOGUE` owns:
- exact spoken lines;
- speaker order;
- final banter;
- delivery;
- final scene prose.

Current Side Quest gameplay structures remain usable even though their final dialogue is deferred.

Character Quest thematic endpoints are authoritative, but this migration does not manufacture line-complete scripts.
