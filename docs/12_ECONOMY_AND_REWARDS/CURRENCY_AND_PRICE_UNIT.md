# Diyse — Currency & Price Unit
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, plus later explicitly accepted v85 tracker-level economy closures.  
**Frozen provenance source:** `Diyse_Item_Equipment_Catalog_Economy_Audit_ARCHIVE_FULL_v603.md` only where later authority does not supersede it.  
**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.


## Currency
The ordinary currency is:
> **AUREN**

Valid display examples:
- 1 Auren
- 20 Auren
- 1,200 Auren

There is no second ordinary shop currency.

No dedicated currency symbol/glyph is currently authored. Do not invent one in implementation docs.

## Denomination
Tracker-level final:
> **1.0 economy unit = 20 Auren**

Anchor:
> **Field Salve = 1.0 unit = 20 Auren**

The denomination converts the already-balanced relative economy into readable integer prices. It does not rebalance the ratios.

## Conversion
For an economy-unit value `U`:
> `Auren = U × 20`

Current consumable prices use clean integer or half/quarter-unit values where already established.

## Reward-equivalence values
A reward-only item may have an Auren-equivalent value for:
- reward density;
- treasure comparison;
- optional-content budgeting.

An equivalence value is **not** a shop price and does not imply the item can be sold or bought.
