# Diyse — Current Balance Risks / Watchlist
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## 1. Enemy/boss action-kit and difficulty rebuild — ACTIVE
Current encounter identities/architecture remain useful, but enemy abilities, direct-damage Powers, and difficulty certification are reopened. Old static/PASS results must not be treated as final tuning.

## 2. EXP / CEXP completion timing — ACTIVE DOWNSTREAM
The former v91/v92 reward model is provisional. **Lv55–60** remains the target completion window, but final Player EXP/CEXP placement and character completion centers must be rerun after encounter/reward validation.

## 3. Proof Prime implementation — ACTIVE
Current runtime tests still exercise stale bearer lock/duration assumptions.
Could hide production Prime bugs until rewritten.

## 4. Save schema / economy persistence — ACTIVE
Proof `gold` / **G** persistence and incomplete production progression persistence can create economy/progression mismatch while the economy/progression rebuilds are still open.

## 5. Closed raw stats without full-game playtest — WATCH
Audits certify values mathematically/architecturally.
Whole-game human playtesting is still required to catch:
- resource attrition;
- build outliers;
- sequence-specific difficulty spikes;
- underused mechanics.

## 6. Optional overleveling — WATCH
Authored optional EXP is intentionally generous.
Weak-enemy diminishing returns helps, but mandatory bosses do not dynamically scale.
Test whether completionists trivialize too much mandatory content before cap.

Do not solve this by adding dynamic scaling unless explicitly approved.

## 7. Prime burst / spacing — WATCH
Primes are powerful but per-identity limited: invocation and Prime commands cost **0 MP**, spent state persists until valid restoration, and fresh forms do **not** refresh availability.
Test burst compression around saved Ready identities, three-full-round post-dismissal spacing, and multi-form transitions.

## 8. Economy rebuild — OPEN
G payouts, prices, liquidity totals, fees, and derived campaign-cash targets remain provisional until the dedicated economy rebuild/recalibration closes them.

## 9. Final UI/audio/performance — OPEN
Production UX/audio can change perceived difficulty/readability even when numbers are correct.
