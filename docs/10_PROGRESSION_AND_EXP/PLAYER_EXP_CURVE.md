# Diyse — Player EXP Curve
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Primary master-canon progression chain:** **Audit123 / Audit124 / Audit125 / Audit126 / Audit127 / Audit128**, plus compatible later raw-stat audits.  
**Current whole-project written authority:** **v2.20 / Audit135**.  
**Current working override:** v85 Sections 220–225 remove the **Mastery Point** currency and make Masteries automatic Class-Level unlocks. This newer working lock is preserved as current working authority pending formal promotion.


## Levels 1–17
`CumulativeEXP(L) = 100 × (L - 1)^2`

## Level 17 onward
For the level-up from Level `L` to `L+1`, `L >= 17`:

`BaseCost = 100 × (2L - 1)`

`Multiplier = 1 + 0.35 × (L - 17) / 42`

`LevelUpCost = round_to_nearest_100(BaseCost × Multiplier)`

## Full table
| Level | Cumulative EXP |
|---:|---:|
| 1 | 0 |
| 2 | 100 |
| 3 | 400 |
| 4 | 900 |
| 5 | 1,600 |
| 6 | 2,500 |
| 7 | 3,600 |
| 8 | 4,900 |
| 9 | 6,400 |
| 10 | 8,100 |
| 11 | 10,000 |
| 12 | 12,100 |
| 13 | 14,400 |
| 14 | 16,900 |
| 15 | 19,600 |
| 16 | 22,500 |
| 17 | 25,600 |
| 18 | 28,900 |
| 19 | 32,400 |
| 20 | 36,200 |
| 21 | 40,200 |
| 22 | 44,400 |
| 23 | 48,900 |
| 24 | 53,600 |
| 25 | 58,600 |
| 26 | 63,800 |
| 27 | 69,300 |
| 28 | 75,000 |
| 29 | 81,000 |
| 30 | 87,300 |
| 31 | 93,800 |
| 32 | 100,600 |
| 33 | 107,700 |
| 34 | 115,100 |
| 35 | 122,700 |
| 36 | 130,600 |
| 37 | 138,800 |
| 38 | 147,300 |
| 39 | 156,100 |
| 40 | 165,200 |
| 41 | 174,600 |
| 42 | 184,300 |
| 43 | 194,300 |
| 44 | 204,600 |
| 45 | 215,300 |
| 46 | 226,300 |
| 47 | 237,600 |
| 48 | 249,200 |
| 49 | 261,200 |
| 50 | 273,500 |
| 51 | 286,100 |
| 52 | 299,100 |
| 53 | 312,400 |
| 54 | 326,000 |
| 55 | 340,000 |
| 56 | 354,400 |
| 57 | 369,100 |
| 58 | 384,200 |
| 59 | 399,600 |
| 60 | 415,400 |
| 61 | 431,600 |
| 62 | 448,100 |
| 63 | 465,000 |
| 64 | 482,300 |
| 65 | 500,000 |
| 66 | 518,100 |
| 67 | 536,500 |
| 68 | 555,300 |
| 69 | 574,500 |
| 70 | 594,100 |

At **Lv70 / 594,100 EXP**:
- no Level 71;
- no prestige levels;
- no overflow-level system.
