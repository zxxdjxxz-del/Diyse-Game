# Diyse — Test Strategy Master

**Status:** ACTIVE TEST-STRATEGY AUTHORITY  
**Balance/QA domain:** `../README.md`

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
