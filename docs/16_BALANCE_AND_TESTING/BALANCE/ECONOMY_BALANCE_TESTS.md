# Diyse — Economy Balance Tests
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Economy authority:
`12_ECONOMY_AND_REWARDS`

## Current currency
> **Auren**

## Test goals
- normal-route income can support ordinary consumable/equipment use without trivializing purchases;
- ordinary equipment registration/repurchase works;
- selling cannot create infinite profit loops;
- protected project materials cannot be sold;
- reward-only exceptional consumables remain scarce;
- Vhalmarch is not a duplicate full superstore;
- Cresthaven Quartermaster backfill works as authored.

## Unresolved payouts
Do not "test to an invented target" for still-open exact:
- Side Quest cash packages;
- Character Quest cash add-ons;
- Hunt Auren payouts where open;
- Kessara service fee.

Those need design closure first.

## Exploit tests
Check:
- buy → sell loop;
- forged Relic duplication → sell or copy exploit;
- project-material resale;
- repeated first-clear reward;
- save/load duplication around service/reward commits.
