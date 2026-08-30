# Diyse — Runtime Test-Suite Status
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## Source availability
Automated GDScript test sources exist for:
- smoke;
- combat;
- encounters;
- dialogue;
- save/load;
- equipment service;
- HD-2D presentation.

## Execution status in this migration
The active artifact-building environment does not provide the project's Godot runtime binary as an executable test runner.

Therefore this migration:
- inspected test source;
- inventories coverage;
- performs static cross-domain arithmetic/consistency checks;
- does **not** falsely claim a fresh full Godot test run passed.

## Known stale assertions
At least the integrated smoke proof still asserts:
- `first_champion`;
- Cyanis bearer-lock;
- non-bearer unavailability.

Those are incompatible with current Prime canon.

A future production CI pass must update these assertions before the suite can be treated as a current-canon green gate.

## Good existing foundations
Current source includes meaningful regression coverage for:
- deterministic round resolution;
- targeting/retarget;
- random encounter handoff;
- save/load;
- dialogue source/continuity;
- Kessara copy service;
- HD-2D proof.

Preserve and update rather than discard.
