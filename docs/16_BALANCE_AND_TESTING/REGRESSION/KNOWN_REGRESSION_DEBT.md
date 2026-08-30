# Diyse — Known Regression/Test Debt
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## HIGH — Prime proof tests
Current smoke/combat proof still expects:
- `first_champion`;
- Cyanis bearer lock;
- non-bearers unable to use it;
- older proof manifestation behavior.

These expectations conflict with current Prime authority.

Production test update required.

## HIGH — Mastery Point regression
Older repository documentation references 8 automatic Mastery Points.

Current:
> Mastery Point currency removed.

Add regression that no runtime/save/UI field reintroduces it.

## HIGH — Auren
Proof state uses `gold`.

Current currency:
> **Auren**

Production schema/UI tests must verify migration/semantic correctness.

## HIGH — content fixtures
Proof:
- Potion
- Proof Sword / armor
- four-character proof party
- placeholder Card/Prime

must not become production balance tests.

## MEDIUM — Chapter ID range
Older schema docs may stop at chapter_12/S062.

Current:
- chapter_13
- S073.

## MEDIUM — no full production CEXP test
Current formal CEXP projection is the old Lv53–57 baseline. The queued recalibration target is Lv55–60.

Do not write a regression that locks the pre-rebalance Lv53–57 timing.

## MEDIUM — audio/UI final QA absent
No production audio bank/final UI yet, so release tests cannot be complete.
