# Diyse — Balance Change Control
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## Test first
When a balance concern appears:
1. reproduce it under current canon;
2. record party level/build/equipment/Cards/Primes;
3. record encounter/form/state;
4. record exact inputs and result;
5. determine whether the problem is:
   - implementation bug;
   - stale data;
   - UX misunderstanding;
   - encounter scripting error;
   - actual numeric balance issue.

Do not reprice a stat because one uncontrolled playthrough "felt off."

## Closed numeric changes
A proposed change to a closed layer must identify:
- current authority;
- current value;
- observed failure;
- affected content;
- why implementation-only correction is insufficient;
- proposed replacement;
- regression consequences.

Then require explicit change approval.

## Open balance
Open/reopened work may be iterated without pretending the old values are final.

Current major reopened numeric layer:
> **CEXP chapter allocation / class-completion timing**

Target:
> full Base + Subclass completion around Player **Lv55–60** after enemy/boss mandatory-vs-completionist validation.

The old Lv53–57 model is baseline/reference only; the temporary Lv62 target is retired.

## No hidden compensation
Do not compensate for one bad number by silently changing:
- shop prices;
- encounter rate;
- enemy damage;
- EXP;
- MP;
- status rates

in another domain.
