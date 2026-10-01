# Diyse — Weak-Enemy EXP Diminishing-Returns Tests

**Status:** ACTIVE PROGRESSION REGRESSION VECTORS  
**Progression authority:** `../../10_PROGRESSION_AND_EXP/`

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
