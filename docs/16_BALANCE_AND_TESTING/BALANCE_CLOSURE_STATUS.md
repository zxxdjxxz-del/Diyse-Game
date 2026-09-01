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
| Representative true-battle suite | **ACTIVE — Hollow Watch PASS v93; Archive Leviathan PASS v97; Regulation Crucible → Seventh Reaction PASS v99; Revision Arbiter PASS v100; Rhazek → Bastion Devourer PASS v101; Vaelkor → Sovereign Panoply PASS v102; Reconstituted Entity → Last Command next** | `16/TRUE_BATTLES` + owning `09` files |
| Ordinary equipment/item definitions | **CLOSED where catalog says closed** | `08` |
| Economy exact unresolved payouts | **OPEN where `12` says open** | `12` |
| Final production UI/audio balance | **OPEN production validation** | `13` / `15` |

## v99 Regulation Crucible certification
Regulation Crucible → The Seventh Reaction is **TRUE-BATTLE CERTIFIED / PASS / RETAIN**.

Strict mandatory Lv15 prepared benchmark:
- no Prime core-rush: **100% wins / median 18 / mean 17.78 / P90 19** over 5,000 runs;
- one Recovered Last Sentinel use in Form II: **100% wins / median 14 / mean 14.18 / P90 16**;
- chamber-control no-Prime line: **100% wins / median 18 / mean 18.34 / P90 20**, with harmful-status load reduced from ~2.54 to ~0.33.

Completionist Lv17 reference:
- median **13** with Last Sentinel;
- median **16** without Prime.

Retain Form-I HP2,400 / Form-II HP2,900, current raw stats/Powers, chamber architecture, and no fresh-form Prime restoration.

## v100 Revision Arbiter certification
Warden of the Nameless / Revision Arbiter is **TRUE-BATTLE CERTIFIED / PASS / RETAIN**.

Strict mandatory Lv30 prepared benchmark:
- no Prime: **100% wins / median 11 / mean 10.76 / P90 12** over 20,000 runs;
- any-KO incidence: **0.005% (1 / 20,000)** with **0 defeats**;
- one Awakened Last Sentinel: **100% wins / median 9 / mean 9.43 / P90 11** over 10,000 runs.

Completionist Lv34 reference:
- no Prime: **median 8 / mean 8.01 / P90 9**;
- with Last Sentinel: **median 8 / mean 7.86 / P90 9**.

Retain HP7,600, all raw stats/Powers/status chances, 3 Closed Record Assertion Layers, Revision Claim, 2 Open Revision Layers, and repetition locks.

Detailed certification:
`TRUE_BATTLES/REVISION_ARBITER_TRUE_BATTLE_v100.md`

## v101 Rhazek → Bastion Devourer certification
Commander Rhazek — Reforged Commander → Bastion Devourer is **TRUE-BATTLE CERTIFIED / PASS / RETAIN**.

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

Retain both HP bodies, raw stats/Powers/status chances/repetition locks, Demolition Breaker, 18% Exposed Rhazek, and current Prime rules.

Detailed certification:
`TRUE_BATTLES/RHAZEK_BASTION_DEVOURER_TRUE_BATTLE_v101.md`

## v102 Vaelkor → Sovereign Panoply certification
Emperor Vaelkor Draeven → Sovereign Panoply Unbound is **TRUE-BATTLE CERTIFIED / PASS / RETAIN**.

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

Retain unchanged:
- Form-I HP **16,800** and raw line;
- Form-II HP **20,200** and raw line;
- all Powers/status chances/repetition locks;
- Sovereign Overrun's 55% threshold, protected one-round Preparation, **390 Power** resolution, 20% Staggered, and 3-round lock;
- Final Sovereignty's 25% same-bar state;
- the genuine fresh-body and persistent-spend Prime rules.

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
