# Diyse — Test Strategy Master
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Testing layers:

## 1. Static data consistency
Checks:
- counts;
- names;
- totals;
- references;
- no retired terminology in current-facing data;
- no duplicate IDs;
- no impossible slot combinations.

## 2. Deterministic unit/regression
Best for:
- formulas;
- turn order;
- targeting;
- status duration/cadence;
- save serialization;
- service eligibility;
- reward once-only state.

## 3. Integration
Best for:
- field → dialogue → battle → field;
- random encounter handoff;
- boss form transitions;
- Prime suspension/resume;
- quest/reward state;
- save/load across systems.

## 4. Balance simulation
Best for:
- damage distributions;
- hit/status probabilities;
- progression curves;
- expected encounter EXP;
- resource consumption;
- build comparisons.

## 5. Human playtest
Required for:
- encounter readability;
- decision quality;
- difficulty feel;
- pacing;
- grind perception;
- menu friction;
- boss clarity;
- build diversity.

## 6. Device/presentation
Required for:
- Android;
- touch;
- readability;
- performance;
- HD-2D composition;
- audio mix when available.

A formula passing unit tests does not prove the encounter is fun.
A playtest feeling does not prove the formula implementation is correct.
