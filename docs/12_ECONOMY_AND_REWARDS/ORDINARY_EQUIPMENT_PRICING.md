# Diyse — Ordinary Equipment Pricing
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted v85 tracker-level economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


Current ordinary catalog:
> **38 / 38**

Breakdown:
- 16 Weapons
- 15 Armors
- 4 Shields
- 3 Foci

The item/stat/source identity remains owned by `08_ITEMS_AND_EQUIPMENT`.
This file owns the purchase/replacement values.

## Exact Auren conversion
| Equipment | Price/replacement units | Auren | Origin class |
|---|---:|---:|---|
| **Dunmere Steel** | 23 | **460** | normal shop-origin / duplicate access |
| **Blue Wardrod** | 22 | **440** | normal shop-origin / duplicate access |
| **Tower Shield** | 11 | **220** | normal shop-origin / duplicate access |
| **Caeloran Plate** | 23 | **460** | normal shop-origin / duplicate access |
| **Warden Fieldmail** | 21 | **420** | normal shop-origin / duplicate access |
| **Swift Focus** | 18 | **360** | normal shop-origin / duplicate access |
| **Warding Shield** | 21 | **420** | normal shop-origin / duplicate access |
| **Battle Focus** | 22 | **440** | normal shop-origin / duplicate access |
| **Deepforge Blade** | 52 | **1,040** | normal shop-origin / duplicate access |
| **Arcanist Weave** | 31 | **620** | normal shop-origin / duplicate access |
| **Crestguard Plate** | 42 | **840** | normal shop-origin / duplicate access |
| **Weaver Coat** | 38 | **760** | normal shop-origin / duplicate access |
| **Campaign Mail** | 46 | **920** | normal shop-origin / duplicate access |
| **Veycross Battlestaff** | 70 | **1,400** | normal shop-origin / duplicate access |
| **Crestblade** | 18 | **360** | registration/replacement value after authored first access |
| **Wardrod** | 17 | **340** | registration/replacement value after authored first access |
| **Yahtrean War Bow** | 20 | **400** | registration/replacement value after authored first access |
| **Command War Bow** | 32 | **640** | registration/replacement value after authored first access |
| **Twin Token** | 29 | **580** | registration/replacement value after authored first access |
| **Crucible Wardrod** | 42 | **840** | registration/replacement value after authored first access |
| **Arcanist Staff** | 36 | **720** | registration/replacement value after authored first access |
| **Index Tablet** | 46 | **920** | registration/replacement value after authored first access |
| **Ruin Vanguard Sword** | 58 | **1,160** | registration/replacement value after authored first access |
| **Storm War Bow** | 64 | **1,280** | registration/replacement value after authored first access |
| **Clearing Bell** | 68 | **1,360** | registration/replacement value after authored first access |
| **Fieldbreaker** | 84 | **1,680** | registration/replacement value after authored first access |
| **Crest Plate** | 15 | **300** | registration/replacement value after authored first access |
| **Blue Warden Mail** | 15 | **300** | registration/replacement value after authored first access |
| **War Archer Gear** | 17 | **340** | registration/replacement value after authored first access |
| **Cardweaver Garb** | 25 | **500** | registration/replacement value after authored first access |
| **Green Arcanist Garb** | 27 | **540** | registration/replacement value after authored first access |
| **Annex Guard Mail** | 27 | **540** | registration/replacement value after authored first access |
| **High Warden Mail** | 34 | **680** | registration/replacement value after authored first access |
| **Ruin Vanguard Plate** | 35 | **700** | registration/replacement value after authored first access |
| **Breach Plate** | 47 | **940** | registration/replacement value after authored first access |
| **Yahtrean Shield** | 9 | **180** | registration/replacement value after authored first access |
| **War Shield** | 34 | **680** | registration/replacement value after authored first access |
| **Warding Focus** | 16 | **320** | registration/replacement value after authored first access |

Count check:
- shop-origin/duplicate-access price lines: **14**
- non-shop first-acquisition replacement lines: **24**
- total: **38**

## Price philosophy
Shop gear is priced for **choice**, not automatic catalog completion.

Guaranteed/found gear still has a replacement/economy value so:
- reward weight can be compared;
- Cresthaven can price later copies;
- subclass build backfill remains possible.

## No late ordinary inflation
An older ordinary item keeps its established price after subclasses broaden equipment access.
Do not reprice a Chapter-2 item as a Chapter-8 item merely because a later build can now equip it.

## Exceptional firewall
These ordinary-equipment prices do not imply shop prices for:
- Relics
- Legacies
