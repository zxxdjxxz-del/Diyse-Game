# 12_ECONOMY_AND_REWARDS

**Status:** CORE G ECONOMY / REWARD DESIGN CLOSED

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

## Mandatory-route calibration
Expected direct G:
> **~316,900 G**

Composition:
- starting wallet: **2,500 G**;
- ordinary formations: **~135,600 G**;
- mandatory story bosses/named encounters: **92,700 G**;
- fixed authored combat/event payouts: **5,300 G**;
- mandatory non-battle reward map: **80,800 G**.

Ordinary formations are approximately **42.8%** of mandatory direct G, preserving the intended **40–50%** share.

## Optional direct-G calibration
Current total if all authored optional activities are cleared:
> **329,600 G**

Breakdown:
- Elites: **38,900 G**;
- ordinary Side Quests: **18,000 G**;
- Character Quests: **22,200 G**;
- Regional Hunts: **116,500 G**;
- Major Hunts: **134,000 G**.

## Completionist direct-cash reference
Mandatory center + all authored optional direct G:
> **~646,500 G**

This intentionally lands very close to the broad **~650,000 G** target.
It excludes resale, deliberate extra encounters/backtracking, and non-cash reward-equivalent value.

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

Premium Consumables remain non-sellable.

## Major sinks
- complete registered ordinary-equipment catalog value: **251,000 G**;
- Kessara Relic-copy fee: **6,000 G per successful copy**;
- all 18 current Relic-copy opportunities: **108,000 G** maximum service spending.

## Closed structural rules
- protected/nonlethal resolution does **not** default to zero G;
- Hunts give strong G regardless of separate permanent/item rewards;
- ordinary enemies have **no random Consumable/equipment/material/junk drop table**;
- optional content is not required for mandatory-route solvency;
- no vendor-trash economy;
- G is the only current-facing ordinary currency term.

## Remaining dependencies
Implementation/presentation still owns:
- vendor NPC identity/dialogue/presentation;
- runtime shop IDs, stock schema, save persistence and UI formatting;
- Kessara menu timing / original-vs-copy presentation.

These do not reopen the closed numeric economy by themselves.
