# 12_ECONOMY_AND_REWARDS

**Status:** CORE ECONOMY / REWARD DESIGN CLOSED

This folder is the single editable home for Diyse's purchase/replacement economy, Auren distribution, commerce structure, resale rules, and non-EXP reward balancing.

## Domain ownership
`12_ECONOMY_AND_REWARDS` owns:
- Auren denomination and direct-currency tuning;
- ordinary equipment purchase/replacement values;
- Consumable prices and resale;
- normal-stock progression;
- commerce endpoint roles;
- reward-value/scarcity rules;
- non-EXP quest/Hunt/Elite/boss reward handoffs.

Other owners:
- item identity/stats/effects/source identity → `08_ITEMS_AND_EQUIPMENT`;
- enemy bodies/formations → `09_ENEMIES_AND_ENCOUNTERS`;
- Player EXP/CEXP → `10_PROGRESSION_AND_EXP`;
- quest structure/access → `11_QUESTS`.

## Current economy anchors
- ordinary currency: **Auren**;
- no second ordinary shop currency;
- **1 economy unit = 20 Auren** as the retained conversion/reference scale;
- Field Salve = **20 Auren**;
- ordinary equipment identities = **38**;
- Consumables = **20**;
- Regional Markets = **exactly 9**.

## Mandatory-route calibration
Expected direct Auren:
> **~30,127 Auren**

Composition:
- ordinary formations: **~13.56k**;
- mandatory story bosses: **8,490**;
- mandatory non-battle reward map: **8,080**.

Ordinary formations are approximately **45%** of the calibrated mandatory-route direct cash.

## Optional direct-cash calibration
Current total if all authored optional activities are cleared:
> **19,390 Auren**

Full direct-cash completionist reference before resale/extra encounters:
> **~49,517 Auren**

## Current commerce structure
Regional Markets:
1. Brackenwall
2. Dunmere
3. Caelora
4. Ivorybridge
5. Stonewake
6. Frostmere
7. Westguard
8. Larkspire
9. Cerythvale

Separate endpoints:
- **Cresthaven Quartermaster** — long-term consolidation / full registered ordinary-equipment requisition authority;
- **Vhalmarch Forward Supply / Requisition** — field logistics after capture/stabilization, not a full catalog superstore.

## Reward-only Consumable supply
Exact whole-game finite supply:
- **Reservoir Tonic ×3**;
- **Emergency Kit ×4**;
- **Emergency Rally ×2**.

All are non-sellable and never enter normal stock.

## Closed system rules
- exact ordinary-formation Auren ledger exists;
- exact boss/Elite/Hunt/quest economic packages exist;
- Consumable resale is exact;
- Kessara Relic-copy fee = **600 Auren per successful copy**;
- ordinary enemies have **no random Consumable/equipment/material/junk drop table**;
- mandatory non-battle Auren has an exact chapter/location/delivery map;
- optional content is not required for mandatory-route solvency;
- no vendor-trash economy.

## Remaining dependencies are not independent economy-design gaps
Still dependent on other domains / implementation:
- exact Auren for special authored encounters whose story role is not yet placed;
- vendor NPC identity/dialogue/presentation;
- Auren icon/glyph;
- runtime shop IDs, stock schema, save persistence and UI formatting;
- Kessara menu timing / original-vs-copy presentation.

These dependencies do not reopen the closed numeric economy unless a later test demonstrates a specific balance/exploit failure or the user explicitly revises the design.
