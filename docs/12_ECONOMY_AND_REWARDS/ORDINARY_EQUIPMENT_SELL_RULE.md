# Diyse — Ordinary Equipment Sell Rule

**Status:** RESALE STRUCTURE CURRENT / G DISPLAY TABLE DERIVED FROM CURRENT PRICE UNITS

Ordinary equipment sells for:
> **50% of its registered purchase/replacement value in economy units, rounded down, then denominated in G.**

Current display conversion:
> **1 economy unit = 200 G**

Equivalent implementation:
> `SellG = floor(EconomyUnits / 2) × 200`

This preserves the established unit-level rounding rule.

Examples:
- 23 units / 4,600 G buy → 11 units → **2,200 G sell**
- 17 units / 3,400 G buy → 8 units → **1,600 G sell**
- 84 units / 16,800 G buy → 42 units → **8,400 G sell**

Do **not** instead half the displayed G first for odd-unit prices, because that would silently change the established unit-level rounding convention.

## Rules
- no depreciation by chapter;
- no vendor-specific sell values;
- no buy-low/sell-high arbitrage;
- repurchase uses the full registered G value derived from the item's economy units.

The current 38-item unit table lives in `ORDINARY_EQUIPMENT_PRICING.md`.

This rule applies to ordinary equipment only.
It does not automatically establish Consumable, Relic, Legacy, material, Card, Prime, or Key Item resale.
