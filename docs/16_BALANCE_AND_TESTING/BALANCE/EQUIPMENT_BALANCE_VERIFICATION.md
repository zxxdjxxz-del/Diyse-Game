# Diyse — Equipment Balance Verification
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## Catalog
Current equipment count:
- 38 ordinary
- 36 Relics
- 17 Legacies
- **91 total**

Hierarchy:
> Ordinary < Relic < Legacy

## Verification
Test:
- legal slots;
- two-slot commitments;
- class/character eligibility;
- stat application;
- perk/trait activation;
- copy quantities;
- no duplicate stacking bug;
- no illegal Secondary item when Weapon consumes Secondary.

## Specific slot checks
Two-slot:
- Torren Great Bow
- Seyrik Two-Handed Sword
- Nimera native Legacy Conduit

Ilyra:
- Wardrod Weapon
- Shield or Focus Secondary
- no sword identity
- no simultaneous Shield + Focus.

## Relics
Test:
- original ownership;
- forged duplicate mechanically identical;
- max quantity 2 per identity;
- no Legacy copy;
- donor eligibility does not generate ownership/copy.

## Legacies
Balance acceptance:
- stronger than Relics overall;
- role-fitting perk;
- meaningful Legacy Trait;
- no invented unsupported combat subsystem.

Exact stats/traits remain in `08`.
