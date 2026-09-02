# Diyse — Ordinary Equipment Pricing

**Status:** CATALOG / RELATIVE PRICE STRUCTURE CURRENT / EXACT G DISPLAY VALUES NEED SYNCHRONIZATION

Current ordinary catalog:
> **38 / 38**

Breakdown:
- 16 Weapons
- 15 Armors
- 4 Shields
- 3 Foci

The item/stat/source identity remains owned by `08_ITEMS_AND_EQUIPMENT`.
This file owns the purchase/replacement values.

## Currency
All current-facing prices use:
> **G**

The former currency name **Auren** is retired.

## Price-unit structure
The existing economy-unit values remain the relative-price authority for the 38-item catalog.

Current display conversion is:
> **1 economy unit = 200 G**

Therefore the old pre-extra-digit displayed table must not be treated as current G prices.

The synchronized G price for an item is:
> `PriceG = EconomyUnits × 200`

Examples:
- 23 units → **4,600 G**
- 17 units → **3,400 G**
- 84 units → **16,800 G**

## Catalog economy units
| Equipment | Price/replacement units | Origin class |
|---|---:|---|
| **Dunmere Steel** | 23 | normal shop-origin / duplicate access |
| **Blue Wardrod** | 22 | normal shop-origin / duplicate access |
| **Tower Shield** | 11 | normal shop-origin / duplicate access |
| **Caeloran Plate** | 23 | normal shop-origin / duplicate access |
| **Warden Fieldmail** | 21 | normal shop-origin / duplicate access |
| **Swift Focus** | 18 | normal shop-origin / duplicate access |
| **Warding Shield** | 21 | normal shop-origin / duplicate access |
| **Battle Focus** | 22 | normal shop-origin / duplicate access |
| **Deepforge Blade** | 52 | normal shop-origin / duplicate access |
| **Arcanist Weave** | 31 | normal shop-origin / duplicate access |
| **Crestguard Plate** | 42 | normal shop-origin / duplicate access |
| **Weaver Coat** | 38 | normal shop-origin / duplicate access |
| **Campaign Mail** | 46 | normal shop-origin / duplicate access |
| **Veycross Battlestaff** | 70 | normal shop-origin / duplicate access |
| **Crestblade** | 18 | registration/replacement value after authored first access |
| **Wardrod** | 17 | registration/replacement value after authored first access |
| **Yahtrean War Bow** | 20 | registration/replacement value after authored first access |
| **Command War Bow** | 32 | registration/replacement value after authored first access |
| **Twin Token** | 29 | registration/replacement value after authored first access |
| **Crucible Wardrod** | 42 | registration/replacement value after authored first access |
| **Arcanist Staff** | 36 | registration/replacement value after authored first access |
| **Index Tablet** | 46 | registration/replacement value after authored first access |
| **Ruin Vanguard Sword** | 58 | registration/replacement value after authored first access |
| **Storm War Bow** | 64 | registration/replacement value after authored first access |
| **Clearing Bell** | 68 | registration/replacement value after authored first access |
| **Fieldbreaker** | 84 | registration/replacement value after authored first access |
| **Crest Plate** | 15 | registration/replacement value after authored first access |
| **Blue Warden Mail** | 15 | registration/replacement value after authored first access |
| **War Archer Gear** | 17 | registration/replacement value after authored first access |
| **Cardweaver Garb** | 25 | registration/replacement value after authored first access |
| **Green Arcanist Garb** | 27 | registration/replacement value after authored first access |
| **Annex Guard Mail** | 27 | registration/replacement value after authored first access |
| **High Warden Mail** | 34 | registration/replacement value after authored first access |
| **Ruin Vanguard Plate** | 35 | registration/replacement value after authored first access |
| **Breach Plate** | 47 | registration/replacement value after authored first access |
| **Yahtrean Shield** | 9 | registration/replacement value after authored first access |
| **War Shield** | 34 | registration/replacement value after authored first access |
| **Warding Focus** | 16 | registration/replacement value after authored first access |

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
An older ordinary item keeps its established economy-unit price after subclasses broaden equipment access.
Do not reprice a Chapter-2 item as a Chapter-8 item merely because a later build can now equip it.

## Exceptional firewall
These ordinary-equipment prices do not imply shop prices for Relics or Legacies.
