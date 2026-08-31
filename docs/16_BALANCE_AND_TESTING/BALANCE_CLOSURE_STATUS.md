# Diyse — Balance Closure Status
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


| Layer | Current status | Canonical home |
|---|---|---|
| Physical/Magical/Hybrid damage formulas | **CLOSED** | `05_BATTLE_SYSTEM` |
| Hit/Evasion | **CLOSED** | `05_BATTLE_SYSTEM` |
| Crit | **CLOSED** | `05_BATTLE_SYSTEM` |
| Elements/status rules | **CLOSED** | `05_BATTLE_SYSTEM` |
| Class Ability base MP | **CLOSED** | `06_CLASSES_AND_ABILITIES` |
| Class Ability roster | **CLOSED** | `06_CLASSES_AND_ABILITIES` |
| Mastery-point currency | **REMOVED** | `06` / `10` |
| Mastery unlock schedule | **CLOSED — automatic by CL** | `06` / `10` |
| CL1–13 cumulative curve | **CLOSED: 6,000 CEXP** | `10` |
| Chapter CEXP allocation / full-class completion timing | **CLOSED v92 — mandatory full Base + Subclass completion ~Lv56–60 within Lv55–60 target** | `10` + this domain |
| Player EXP curve / Lv70 cap | **CLOSED** | `10` |
| Mandatory Player EXP | **CLOSED** | `10` |
| Optional Player EXP | **CLOSED** | `10` |
| Ordinary encounter planning center | **CLOSED AS PACING CENTER: 225** | `10` |
| Mandatory named raw stats Ch1–13 | **CLOSED** | `09` |
| Optional Elite raw stats | **CLOSED** | `09` |
| Regional Hunt raw stats | **CLOSED** | `09` |
| Major Hunt raw stats | **CLOSED** | `09` |
| Whole-roster mandatory-vs-completionist validation | **PAPER PASS COMPLETE Ch0–13 / v89; representative true-battle follow-up ACTIVE** | `16` + owning `09` files |
| Representative true-battle suite | **ACTIVE — Hollow Watch PASS v93; Archive Leviathan PASS v97; Regulation Crucible → Seventh Reaction PASS v99; Revision Arbiter next** | `16/TRUE_BATTLES` + owning `09` files |
| Ordinary equipment/item definitions | **CLOSED where catalog says closed** | `08` |
| Economy exact unresolved payouts | **OPEN where `12` says open** | `12` |
| Final production UI/audio balance | **OPEN production validation** | `13` / `15` |

## v99 Regulation Crucible certification
Regulation Crucible → The Seventh Reaction is now **TRUE-BATTLE CERTIFIED / PASS / RETAIN**.

Strict mandatory Lv15 prepared benchmark:
- no Prime core-rush: **100% wins / median 18 / mean 17.78 / P90 19** over 5,000 runs;
- one Recovered Last Sentinel use in Form II: **100% wins / median 14 / mean 14.18 / P90 16**;
- chamber-control no-Prime line: **100% wins / median 18 / mean 18.34 / P90 20**, with harmful-status load reduced from ~2.54 to ~0.33.

Completionist Lv17 reference:
- median **13** with Last Sentinel;
- median **16** without Prime.

Retain:
- Form-I HP2,400;
- Form-II HP2,900;
- all current raw stats and Powers;
- chamber architecture;
- current rule that a genuine fresh form does **not** restore a spent Prime identity.

The old paper-only universal ~13–15 mandatory-round expectation is superseded by this current route/preparation-specific result.

## Meaning of CLOSED
`CLOSED` means:
- do not casually reprice/redesign during implementation;
- use the current number as the test oracle.

It does **not** mean:
- skip QA;
- ignore a reproducible broken result;
- prohibit explicit later rebalancing after evidence/user approval.
