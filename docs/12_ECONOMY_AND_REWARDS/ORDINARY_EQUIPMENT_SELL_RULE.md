# Diyse — Ordinary Equipment Sell Rule

**Status:** EXACT ORDINARY-EQUIPMENT G RESALE AUTHORITY

Ordinary equipment sells for:
> **50% of its registered purchase/replacement value in economy units, rounded down, then denominated in G.**

Current display conversion:
> **1 economy unit = 200 G**

Equivalent implementation:
> `SellG = floor(EconomyUnits / 2) × 200`

This preserves the established unit-level rounding rule.

Do **not** instead half the displayed G first for odd-unit prices, because that would silently change the established unit-level rounding convention.

## Complete current sell table
| Equipment | Units | Buy / replace | Sell |
|---|---:|---:|---:|
| **Dunmere Steel** | 23 | **4,600 G** | **2,200 G** |
| **Blue Wardrod** | 22 | **4,400 G** | **2,200 G** |
| **Tower Shield** | 11 | **2,200 G** | **1,000 G** |
| **Caeloran Plate** | 23 | **4,600 G** | **2,200 G** |
| **Warden Fieldmail** | 21 | **4,200 G** | **2,000 G** |
| **Swift Focus** | 18 | **3,600 G** | **1,800 G** |
| **Warding Shield** | 21 | **4,200 G** | **2,000 G** |
| **Battle Focus** | 22 | **4,400 G** | **2,200 G** |
| **Deepforge Blade** | 52 | **10,400 G** | **5,200 G** |
| **Arcanist Weave** | 31 | **6,200 G** | **3,000 G** |
| **Crestguard Plate** | 42 | **8,400 G** | **4,200 G** |
| **Weaver Coat** | 38 | **7,600 G** | **3,800 G** |
| **Campaign Mail** | 46 | **9,200 G** | **4,600 G** |
| **Veycross Battlestaff** | 70 | **14,000 G** | **7,000 G** |
| **Crestblade** | 18 | **3,600 G** | **1,800 G** |
| **Wardrod** | 17 | **3,400 G** | **1,600 G** |
| **Yahtrean War Bow** | 20 | **4,000 G** | **2,000 G** |
| **Command War Bow** | 32 | **6,400 G** | **3,200 G** |
| **Twin Token** | 29 | **5,800 G** | **2,800 G** |
| **Crucible Wardrod** | 42 | **8,400 G** | **4,200 G** |
| **Arcanist Staff** | 36 | **7,200 G** | **3,600 G** |
| **Index Tablet** | 46 | **9,200 G** | **4,600 G** |
| **Ruin Vanguard Sword** | 58 | **11,600 G** | **5,800 G** |
| **Storm War Bow** | 64 | **12,800 G** | **6,400 G** |
| **Clearing Bell** | 68 | **13,600 G** | **6,800 G** |
| **Fieldbreaker** | 84 | **16,800 G** | **8,400 G** |
| **Crest Plate** | 15 | **3,000 G** | **1,400 G** |
| **Blue Warden Mail** | 15 | **3,000 G** | **1,400 G** |
| **War Archer Gear** | 17 | **3,400 G** | **1,600 G** |
| **Cardweaver Garb** | 25 | **5,000 G** | **2,400 G** |
| **Green Arcanist Garb** | 27 | **5,400 G** | **2,600 G** |
| **Annex Guard Mail** | 27 | **5,400 G** | **2,600 G** |
| **High Warden Mail** | 34 | **6,800 G** | **3,400 G** |
| **Ruin Vanguard Plate** | 35 | **7,000 G** | **3,400 G** |
| **Breach Plate** | 47 | **9,400 G** | **4,600 G** |
| **Yahtrean Shield** | 9 | **1,800 G** | **800 G** |
| **War Shield** | 34 | **6,800 G** | **3,400 G** |
| **Warding Focus** | 16 | **3,200 G** | **1,600 G** |

## Rules
- no depreciation by chapter;
- no vendor-specific sell values;
- no buy-low/sell-high arbitrage;
- repurchase uses full registered value.

This rule applies to ordinary equipment only.
It does not automatically establish Consumable, Relic, Legacy, material, Card, Prime, or Key Item resale.
