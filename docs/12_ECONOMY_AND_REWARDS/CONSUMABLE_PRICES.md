# Diyse — Consumable Prices
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.

Current consumable count:
> **20**

| ID | Consumable | Current function | Commerce class | Auren |
|---|---|---|---|---:|
| C01 | **Field Salve** | Restore 250 HP to one ally | normal stock | **20** |
| C02 | **Restorative Salve** | Restore 750 HP to one ally | normal stock | **50** |
| C03 | **Vital Salve** | Restore 1,500 HP to one ally | normal stock | **120** |
| C04 | **Grand Salve** | Restore 2,250 HP to one ally | normal stock | **240** |
| C05 | **Company Salve** | Restore 30% Max HP to all conscious active-party members | normal stock | **200** |
| C06 | **Flow Tonic** | Restore 50 MP to one ally | normal stock | **80** |
| C07 | **Deepflow Tonic** | Restore 80 MP to one ally | normal stock | **200** |
| C08 | **Highflow Tonic** | Restore 120 MP to one ally | normal stock | **360** |
| C09 | **Reservoir Tonic** | Restore 75% Max MP to one ally | reward-only | **640 equivalent** |
| C10 | **Rousing Salts** | Revive one KO ally at 25% Max HP | normal stock | **60** |
| C11 | **Greater Rousing Salts** | Revive one KO ally at 50% Max HP + restore 25% Max MP | normal stock | **160** |
| C12 | **Trauma Remedy** | Remove Burn / Bleed | normal stock | **15** |
| C13 | **Stability Remedy** | Remove Freeze / Stun / Staggered | normal stock | **15** |
| C14 | **General Remedy** | Remove one eligible ordinary harmful status | normal stock | **50** |
| C15 | **Full Remedy** | Remove all eligible ordinary harmful statuses | normal stock | **140** |
| C16 | **Blinding Mist** | Guaranteed escape from eligible ordinary random encounter | normal stock | **10** |
| C17 | **Null Seal** | Remove one eligible removable positive effect from an enemy | normal stock | **70** |
| C18 | **Balance Seal** | Restore eligible ordinary negative stat changes toward normal | normal stock | **60** |
| C19 | **Emergency Kit** | 75% Max HP + 60% Max MP + eligible cleanse/stat restoration; no revive | reward-only | **300 equivalent** |
| C20 | **Emergency Rally** | Revive all KO active-party members at 60% Max HP + 35% Max MP | reward-only | **500 equivalent** |

## Price-family read
Cheap maintenance:
- Blinding Mist — 10
- Trauma Remedy — 15
- Stability Remedy — 15
- Field Salve — 20

Core recovery/utility:
- Restorative Salve — 50
- General Remedy — 50
- Rousing Salts — 60
- Balance Seal — 60
- Null Seal — 70
- Flow Tonic — 80

Advanced:
- Vital Salve — 120
- Full Remedy — 140
- Greater Rousing Salts — 160
- Company Salve — 200
- Deepflow Tonic — 200
- Grand Salve — 240

Late MP recovery:
- Highflow Tonic — 360

## Reward-only values
- Emergency Kit — 300 Auren equivalent
- Emergency Rally — 500 Auren equivalent
- Reservoir Tonic — **640 Auren equivalent**

The older Reservoir Tonic value of 480 equivalent is retired.

## Sell rule
Consumable resale is now authored in:
> `CONSUMABLE_SELL_RULE.md`

Normal-stock Consumables use the dedicated low-resale rule there rather than the ordinary-equipment 50% rule.

Reward-only:
- Reservoir Tonic;
- Emergency Kit;
- Emergency Rally

are **not sellable**. Their Auren-equivalent numbers are balancing references only.
