# Diyse — Ordinary Equipment Sell Rule
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted v85 tracker-level economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


Ordinary equipment sells for:
> **50% of its registered purchase/replacement value in economy units, rounded down, then denominated in Auren.**

Equivalent implementation:
> `SellAuren = floor(EconomyUnits / 2) × 20`

This preserves the established pre-denomination rounding rule.

Examples:
- 23 units / 460 Auren → 11 units → **220 Auren**
- 17 units / 340 Auren → 8 units → **160 Auren**
- 84 units / 1,680 Auren → 42 units → **840 Auren**

Do **not** instead half the displayed Auren first for odd-unit prices, because that would silently change the established unit-level rounding convention.

## Complete current sell table
| Equipment | Units | Buy/replace Auren | Sell Auren |
|---|---:|---:|---:|
| Dunmere Steel | 23 | 460 | **220** |
| Blue Wardrod | 22 | 440 | **220** |
| Tower Shield | 11 | 220 | **100** |
| Caeloran Plate | 23 | 460 | **220** |
| Warden Fieldmail | 21 | 420 | **200** |
| Swift Focus | 18 | 360 | **180** |
| Warding Shield | 21 | 420 | **200** |
| Battle Focus | 22 | 440 | **220** |
| Deepforge Blade | 52 | 1,040 | **520** |
| Arcanist Weave | 31 | 620 | **300** |
| Crestguard Plate | 42 | 840 | **420** |
| Weaver Coat | 38 | 760 | **380** |
| Campaign Mail | 46 | 920 | **460** |
| Veycross Battlestaff | 70 | 1,400 | **700** |
| Crestblade | 18 | 360 | **180** |
| Wardrod | 17 | 340 | **160** |
| Yahtrean War Bow | 20 | 400 | **200** |
| Command War Bow | 32 | 640 | **320** |
| Twin Token | 29 | 580 | **280** |
| Crucible Wardrod | 42 | 840 | **420** |
| Arcanist Staff | 36 | 720 | **360** |
| Index Tablet | 46 | 920 | **460** |
| Ruin Vanguard Sword | 58 | 1,160 | **580** |
| Storm War Bow | 64 | 1,280 | **640** |
| Clearing Bell | 68 | 1,360 | **680** |
| Fieldbreaker | 84 | 1,680 | **840** |
| Crest Plate | 15 | 300 | **140** |
| Blue Warden Mail | 15 | 300 | **140** |
| War Archer Gear | 17 | 340 | **160** |
| Cardweaver Garb | 25 | 500 | **240** |
| Green Arcanist Garb | 27 | 540 | **260** |
| Annex Guard Mail | 27 | 540 | **260** |
| High Warden Mail | 34 | 680 | **340** |
| Ruin Vanguard Plate | 35 | 700 | **340** |
| Breach Plate | 47 | 940 | **460** |
| Yahtrean Shield | 9 | 180 | **80** |
| War Shield | 34 | 680 | **340** |
| Warding Focus | 16 | 320 | **160** |

Rules:
- no depreciation by chapter;
- no vendor-specific sell values;
- no buy-low/sell-high arbitrage;
- repurchase uses full registered value.

This rule applies to ordinary equipment only.
It does not automatically establish consumable, Relic, Legacy, material or Key Item resale.
