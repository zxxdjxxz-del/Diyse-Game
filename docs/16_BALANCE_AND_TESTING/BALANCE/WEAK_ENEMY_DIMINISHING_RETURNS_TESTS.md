# Diyse — Weak-Enemy EXP Diminishing-Returns Tests
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


Applies only to repeatable ordinary enemy-kill **Player EXP**.

Reference:
> highest current Level among permanent party.

Let:
`D = Party Reference Level - Enemy Level`

| D | Multiplier |
|---:|---:|
| ≤0 | 100% |
| 1–2 | 90% |
| 3–4 | 65% |
| 5–6 | 40% |
| 7–9 | 20% |
| 10–14 | 10% |
| 15+ | 5% |

Round nearest whole EXP, minimum1.

## Regression cases
Base100 EXP:
- D0 → 100
- D1 → 90
- D3 → 65
- D5 → 40
- D7 → 20
- D10 → 10
- D15 → 5

Base7 EXP / D15:
- 7×5%=0.35
- nearest whole would 0
- minimum:
> **1**

## Must remain exempt
- mandatory named/story awards
- Side Quest completion
- Character Quest completion
- Regional Hunt packages
- Major Hunt packages.

## CEXP
No CEXP diminishing returns.
