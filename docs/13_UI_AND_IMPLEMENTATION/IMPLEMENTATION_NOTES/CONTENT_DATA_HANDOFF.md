# Implementation Notes — Content/Data Handoff
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Principle
UI reads current canonical data.
UI does not become a second balance database.

### Classes
Read:
`06_CLASSES_AND_ABILITIES`

### Cards/Primes
Read:
`07_CARDS`

### Items/equipment
Read:
`08_ITEMS_AND_EQUIPMENT`

### Enemies
Read:
`09_ENEMIES_AND_ENCOUNTERS`

### Progression
Read:
`10_PROGRESSION_AND_EXP`

### Quests
Read:
`11_QUESTS`

### Economy
Read:
`12_ECONOMY_AND_REWARDS`

## Examples of what not to hardcode in UI scripts
- item prices;
- equipment stats;
- Card MP costs;
- Prime state/cost;
- Ability MP;
- enemy HP;
- quest EXP;
- current region names;
- Story Prime names;
- class unlock levels.

These belong in data/domain sources.

## Descriptions
Final player-facing descriptions should be data-driven and replaceable without rewriting generic menu code.

## Runtime fallback
Proof fixtures may use placeholder content only when:
- clearly marked proof;
- isolated from production IDs;
- unable to masquerade as canon.
