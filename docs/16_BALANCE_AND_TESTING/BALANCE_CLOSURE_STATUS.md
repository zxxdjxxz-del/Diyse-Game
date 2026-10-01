# Diyse — Balance Closure Status

**Status:** ACTIVE BALANCE-STATE REGISTER  
**Domain authority:** `README.md`

| Layer | Current status | Canonical home |
|---|---|---|
| Physical/Magical/Hybrid damage formulas | **CLOSED** | `05_BATTLE_SYSTEM` |
| Hit/Evasion | **CLOSED** | `05_BATTLE_SYSTEM` |
| Crit | **CLOSED** | `05_BATTLE_SYSTEM` |
| Elements/status rules | **CLOSED** | `05_BATTLE_SYSTEM` |
| Class Ability base MP / roster | **CLOSED where current owner files say closed** | `06_CLASSES_AND_ABILITIES` |
| Mastery-point currency | **REMOVED** | `06` / `10` |
| Mastery unlock schedule | **CLOSED — automatic by CL** | `06` / `10` |
| Chapter CEXP allocation / class-completion timing | **REOPENED — Lv55–60 target retained** | `10` + this domain |
| Player Level cap | **CLOSED: Lv70** | `10` |
| Player EXP placement | **PROVISIONAL — rebuild pending** | `10` |
| Enemy raw stats | **CURRENT REFERENCE; may reopen where redesign requires** | `09` |
| Enemy direct-damage Powers / action kits | **REOPENED / REDESIGN PENDING** | `09` + this domain |
| Mandatory-vs-completionist validation | **REVALIDATION REQUIRED** | `16` + current owners |
| Representative true-battle suite | **HISTORICAL / PROVISIONAL** | `TRUE_BATTLES/` |
| Ordinary equipment/item definitions | **CLOSED where owner catalog says closed** | `08` |
| Economy numeric calibration | **REBUILD / RECALIBRATION PENDING** | `12` |
| Production UI/audio balance | **OPEN production validation** | `13` / `15` |

## Historical-certification boundary

The retained versioned true-battle reports document exact historical snapshots. Their old difficulty PASS/RETAIN conclusions are not current certification while enemy action kits, progression, and reward inputs are being rebuilt.

Mechanical findings remain usable only where they still match current owner-domain rules. Current combat, Prime, boss-form, status, progression, encounter, and reward owners always win over an old test report.

## Meaning of CLOSED

`CLOSED` means:
- use the current owning-domain value/rule as the test oracle;
- do not casually redesign it during implementation.

It does not mean:
- skip QA;
- ignore a reproducible broken result;
- prohibit explicit later rebalancing after evidence and approval.
