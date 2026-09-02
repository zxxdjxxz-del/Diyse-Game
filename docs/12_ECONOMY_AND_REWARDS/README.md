# 12_ECONOMY_AND_REWARDS

**Status:** ACTIVE ECONOMY RECALIBRATION / CURRENT CURRENCY AUTHORITY

This folder is the single editable home for Diyse's purchase/replacement economy, **G** distribution, commerce structure, resale rules, and non-EXP reward balancing.

## Domain ownership
`12_ECONOMY_AND_REWARDS` owns:
- G denomination and direct-currency tuning;
- ordinary equipment purchase/replacement values;
- Consumable prices and resale;
- normal and limited-premium stock progression;
- commerce endpoint roles;
- reward-value/scarcity rules;
- non-EXP quest/Hunt/Elite/boss reward handoffs.

Other owners:
- item identity/stats/effects/source identity → `08_ITEMS_AND_EQUIPMENT`;
- enemy bodies/formations → `09_ENEMIES_AND_ENCOUNTERS`;
- Player EXP/CEXP → `10_PROGRESSION_AND_EXP`;
- quest structure/access → `11_QUESTS`.

## Current economy anchors
- ordinary currency: **G**;
- retired currency name: **Auren**;
- no second ordinary shop currency;
- **1 economy unit = 200 G**;
- Field Salve = **200 G**;
- starting wallet = **2,500 G**;
- ordinary equipment identities = **38**;
- Consumables = **20**;
- Regional Markets = **exactly 9**.

## Current cash-flow target
The economy is being recalibrated after the display-scale and reward revisions.

Current target for a broad completionist direct-cash route:
> **roughly 650,000 G**

Do not restore the older ~49.5k completionist total as current authority.

Current revisions that must be reflected in the final payout pass:
- protected/nonlethal resolved encounters receive G rather than defaulting to zero;
- Hunts should pay a strong G reward regardless of their separate permanent/item rewards;
- payout tables must use the current tenfold display scale.

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
- **Cresthaven Quartermaster** — long-term consolidation / registered ordinary-equipment requisition authority;
- **Vhalmarch Forward Supply / Requisition** — field logistics after capture/stabilization.

## Premium Consumables
Reservoir Tonic, Emergency Kit, and Emergency Rally are **not reward-only**.

From the first accessible state of every Consumable-selling shop:
- **1 Reservoir Tonic**;
- **1 Emergency Kit**;
- **1 Emergency Rally**;
- no automatic restock.

Guaranteed authored pickups remain separate and do not consume shop stock.

Current prices:
- Emergency Kit — **8,000 G**;
- Reservoir Tonic — **12,000 G**;
- Emergency Rally — **15,000 G**.

## Closed structural rules
- ordinary enemies have **no random Consumable/equipment/material/junk drop table**;
- optional content is not required for mandatory-route solvency;
- no vendor-trash economy;
- G is the only current-facing ordinary currency term.

## Remaining economy work
The current payout/value tables still require synchronization to the latest economy revisions and display scale before the numeric economy can be called fully closed again.

Implementation/presentation still owns:
- vendor NPC identity/dialogue/presentation;
- runtime shop IDs, stock schema, save persistence and UI formatting;
- Kessara menu timing / original-vs-copy presentation.
