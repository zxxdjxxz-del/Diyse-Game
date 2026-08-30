# Diyse — QA Severity / Acceptance
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Suggested production triage language:

## Blocker
Cannot progress / data loss / crash / save corruption / impossible mandatory battle due bug.

## Critical
Major current-canon system broken:
- wrong damage formula;
- Prime form refresh wrong;
- story state invalid;
- quest unique reward duplicates/vanishes;
- equipment eligibility corrupt;
- EXP/CEXP missing or duplicated.

## Major
Substantial gameplay/UX failure with workaround:
- status duration wrong;
- target selection confusing;
- incorrect shop registration;
- significant performance hitch;
- key menu unreadable.

## Minor
Localized presentation/copy issue not changing rules.

## Cosmetic
Visual/audio polish with no gameplay effect.

## Acceptance rule
A milestone is not accepted because one happy-path playthrough works.

For closed systems:
- deterministic regressions pass;
- known stale tests reconciled;
- no blocker/critical unresolved;
- manual playtest completed for affected content;
- device validation completed when relevant.
