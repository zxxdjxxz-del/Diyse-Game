# Diyse — Save / Persistence Test Plan
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Existing proof coverage is useful but production schema must expand.

## Existing tests should continue to verify
- missing save safe failure;
- invalid JSON safe failure;
- unsupported future schema rejection;
- state round-trip;
- old schema compatibility where intentionally supported;
- transient random-encounter state excluded;
- transient state cleared on load.

## Production-state coverage must add
- Player EXP/Level;
- Base/Subclass CL/CEXP;
- selected class;
- automatic Mastery unlock derivation/state;
- Auren;
- equipment/loadouts;
- Relic copies;
- Legacy project state;
- Cards/Primes/loadouts;
- quests/Hunts;
- world/travel flags;
- story state;
- settings.

## Must not serialize
- Mastery Point currency;
- stale proof Gold as current semantic currency;
- unconfirmed UI cursor state;
- live scene-node references.

## Exploit regression
Test save/load around:
- reward collection;
- Hunt first clear;
- Kessara Relic copy;
- shop transactions;
- Legacy completion;
- quest completion

for duplication or rollback exploits.
