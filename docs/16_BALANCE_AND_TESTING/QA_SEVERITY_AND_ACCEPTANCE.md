# Diyse — QA Severity / Acceptance

**Status:** ACTIVE QA SEVERITY / MILESTONE ACCEPTANCE RULE  
**Balance/QA authority:** `README.md`

Suggested production triage language:

## Blocker
Cannot progress / data loss / crash / save corruption / impossible mandatory battle due bug.

## Critical
Major current-canon system broken:
- wrong damage formula;
- Prime spent/Ready restoration or spacing behavior wrong;
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
