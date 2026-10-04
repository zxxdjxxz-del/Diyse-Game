# Diyse — Balance Change Control

**Status:** ACTIVE BALANCE CHANGE-CONTROL RULE  
**Balance/QA authority:** `README.md`

## Test first

When a balance concern appears:
1. reproduce it under current repository authority;
2. record party level/build/equipment/Cards/Primes;
3. record encounter/form/state;
4. record exact inputs and result;
5. determine whether the problem is an implementation bug, stale current data, UX misunderstanding, encounter scripting error, or actual numeric balance issue.

Do not change a value because one uncontrolled playthrough merely felt off.

## Closed-layer changes

A proposed change to a closed owner-domain value must identify:
- current owner;
- current value/rule;
- observed failure;
- affected content;
- why an implementation-only correction is insufficient;
- proposed replacement;
- regression consequences.

Then require explicit approved change.

## Reopened work

Current reopened/rebuild frontiers include:
- enemy action kits/Powers and difficulty certification;
- Player EXP/CEXP placement;
- economy G pricing/payout calibration;
- downstream mandatory-vs-completionist certification.

The **Lv55–60** full Base + Subclass completion window remains the target while exact reward tables are rebuilt.

## No hidden compensation

Do not compensate for one bad number by silently changing another domain's prices, encounter rate, enemy damage, EXP/CEXP, MP, status rates, equipment, or reward values.

Changes belong in the actual owner domain and require the corresponding regressions to be rerun.
