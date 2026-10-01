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
| Class Ability base MP | **CLOSED where current owner files say closed** | `06_CLASSES_AND_ABILITIES` |
| Class Ability roster | **CLOSED where current owner files say closed** | `06_CLASSES_AND_ABILITIES` |
| Mastery-point currency | **REMOVED** | `06` / `10` |
| Mastery unlock schedule | **CLOSED — automatic by CL** | `06` / `10` |
| CL1–13 cumulative CEXP reference | **CURRENT REFERENCE: 6,000; final campaign CEXP rebuild pending** | `10` |
| Chapter CEXP allocation / full-class completion timing | **REOPENED — Lv55–60 remains the target window, old v91/v92 proof is provisional** | `10` + this domain |
| Player Level cap | **CLOSED: Lv70** | `10` |
| Player EXP curve / mandatory / optional placement | **PROVISIONAL — rebuild pending** | `10` |
| Ordinary encounter planning center | **PROVISIONAL historical pacing reference: 225** | `10` |
| Mandatory named raw stats Ch1–13 | **CURRENT REFERENCE; may reopen where difficulty/ability rebuild requires** | `09` |
| Optional Elite raw stats | **CURRENT REFERENCE; may reopen where difficulty/ability rebuild requires** | `09` |
| Regional Hunt raw stats | **CURRENT REFERENCE; timing/ability recertification open** | `09` |
| Major Hunt raw stats | **CURRENT REFERENCE; #3–#5 timing recertification open** | `09` |
| Enemy direct-damage Powers / action kits | **REOPENED / REDESIGN PENDING** | `09` + this domain |
| Whole-roster mandatory-vs-completionist validation | **HISTORICAL PAPER PASS ONLY; recertification required after ability/progression rebuild** | `16` + owning `09` files |
| Representative true-battle suite | **HISTORICAL/PROVISIONAL measurements retained; final certification paused pending rebuilt inputs** | `16/TRUE_BATTLES` + owning `09` files |
| Ordinary equipment/item definitions | **CLOSED where catalog says closed** | `08` |
| Economy numeric calibration | **REBUILD / RECALIBRATION PENDING** | `12` |
| Final production UI/audio balance | **OPEN production validation** | `13` / `15` |

> **Historical-certification boundary:** v99–v102 sections below preserve the exact test packages and mechanical findings they measured. Their old difficulty PASS/RETAIN conclusions are **provisional**, and any statement retaining enemy Powers/action kits is superseded by the current enemy-ability redesign/revalidation work. Prime-persistence and form-architecture findings remain usable where they match current system authority.

## v99 Regulation Crucible historical measurement
Regulation Crucible → The Seventh Reaction recorded a **v99 TRUE-BATTLE PASS under the then-current package**; final difficulty certification is reopened.

Strict mandatory Lv15 prepared benchmark:
- no Prime core-rush: **100% wins / median 18 / mean 17.78 / P90 19** over 5,000 runs;
- one Recovered Last Sentinel use in Form II: **100% wins / median 14 / mean 14.18 / P90 16**;
- chamber-control no-Prime line: **100% wins / median 18 / mean 18.34 / P90 20**, with harmful-status load reduced from ~2.54 to ~0.33.

Completionist Lv17 reference:
- median **13** with Last Sentinel;
- median **16** without Prime.

Historical v99 package: Form-I HP2,400 / Form-II HP2,900 with the then-current raw stats/Powers and chamber architecture. The no-fresh-form-Prime-restoration finding remains current; Powers/action-kit tuning is reopened.

## v100 Revision Arbiter historical measurement
Warden of the Nameless / Revision Arbiter recorded a **v100 TRUE-BATTLE PASS under the then-current package**; final difficulty certification is reopened.

Strict mandatory Lv30 prepared benchmark:
- no Prime: **100% wins / median 11 / mean 10.76 / P90 12** over 20,000 runs;
- any-KO incidence: **0.005% (1 / 20,000)** with **0 defeats**;
- one Awakened Last Sentinel: **100% wins / median 9 / mean 9.43 / P90 11** over 10,000 runs.

Completionist Lv34 reference:
- no Prime: **median 8 / mean 8.01 / P90 9**;
- with Last Sentinel: **median 8 / mean 7.86 / P90 9**.

Historical v100 package: HP7,600 with the then-current raw stats/Powers/status chances, Assertion Layers, Revision Claim, Open Revision Layers, and repetition locks. Treat those combat-tuning values as historical inputs pending the ability/difficulty rewrite.

Detailed certification:
`TRUE_BATTLES/REVISION_ARBITER_TRUE_BATTLE_v100.md`

## v101 Rhazek → Bastion Devourer historical measurement
Commander Rhazek — Reforged Commander → Bastion Devourer recorded a **v101 TRUE-BATTLE PASS under the then-current package**; final difficulty certification is reopened.

Strict prepared mandatory Lv40, no Prime:
- **100% wins / median 14 / mean 14.48 / P90 17** over 20,000 runs;
- any-KO **0.08%**;
- mean ending HP **75.06%**;
- mean ending MP **12.18%**;
- mean consumables **3.45**.

Prime persistence stress:
- timed Last Sentinel — **100% wins / median 15 / mean 15.34 / P90 17**;
- fresh-body crossing during manifestation **99.04%** with no spent-Prime restoration;
- legal Sentinel → 2 full normal rounds → Convergence — **100% wins / median 15 / mean 15.17 / P90 17**;
- chained-Primes ending MP **43.77%**, mean items **0.98**.

Completionist Lv48–49 no-Prime references both center at **median 12**.

Historical v101 package: both HP bodies with the then-current raw stats/Powers/status chances/repetition locks, Demolition Breaker, and 18% Exposed Rhazek. Current Prime-persistence findings remain valid; enemy combat tuning is reopened.

Detailed certification:
`TRUE_BATTLES/RHAZEK_BASTION_DEVOURER_TRUE_BATTLE_v101.md`

## v102 Vaelkor → Sovereign Panoply historical measurement
Emperor Vaelkor Draeven → Sovereign Panoply Unbound recorded a **v102 TRUE-BATTLE PASS under the then-current package**; final difficulty certification is reopened.

Prepared mandatory Lv56, no Prime:
- **100% wins / median 21 / mean 22.46 / P90 29** over 5,000 runs;
- any-KO **1.98%**;
- defeat incidence **0%**;
- mean ending HP **69.20%**;
- mean ending MP **8.80%**;
- mean consumables **4.82**.

One timed Awakened Last Sentinel:
- **100% wins / median 20 / mean 20.70 / P90 25** over 5,000 runs;
- any-KO **0.14%**;
- same manifestation crossed Form I → fresh Sovereign Panoply in **95.90%** of timed runs;
- spent Last Sentinel remained spent and manifestation continued normally.

Legal two-Prime spacing stress:
- Last Sentinel → **2 full normal party rounds** → Last Convergence;
- **100% wins / median 19 / mean 19.14 / P90 23** over 5,000 runs;
- **0% any-KO**;
- mean ending MP **17.21%**;
- mean consumables **0.51**;
- Sentinel fresh-body crossing **96.38%**.

Sovereign Overrun no-Prime stress:
- Preparation appeared in **70.32%** of runs;
- Resolution fired in **63.32%**;
- no unavoidable wipe signature appeared.

Completionist Lv66 native-Legacy reference:
- **100% wins / median 15 / mean 14.68 / P90 17** over 5,000 runs;
- **0% any-KO**.

Historical v102 tested package:
- Form-I HP **16,800** and raw line;
- Form-II HP **20,200** and raw line;
- then-current Powers/status chances/repetition locks;
- Sovereign Overrun's 55% threshold, protected one-round Preparation, **390 Power** resolution, 20% Staggered, and 3-round lock;
- Final Sovereignty's 25% same-bar state;
- the genuine fresh-body and persistent-spend Prime rules.

Only the form/Prime-system findings are carried forward automatically; enemy action-kit/Power tuning remains reopened.

Current true-battle pacing refines the historical generic paper estimate to approximately **19–21 total rounds depending on Prime commitment**, while completionist Lv66 remains at the intended **~13–15** center.

Detailed certification:
`TRUE_BATTLES/VAELKOR_SOVEREIGN_PANOPLY_TRUE_BATTLE_v102.md`

The next representative anchor is:
> **Reconstituted Entity → The Last Command — final mandatory Chapter-13 two-body test**

## Meaning of CLOSED
`CLOSED` means:
- do not casually reprice/redesign during implementation;
- use the current number as the test oracle.

It does **not** mean:
- skip QA;
- ignore a reproducible broken result;
- prohibit explicit later rebalancing after evidence/user approval.
