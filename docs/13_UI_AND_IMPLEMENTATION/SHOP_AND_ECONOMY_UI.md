# Diyse — Shop / Economy UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Currency
Current ordinary currency:
> **Auren**

Do not expose `Gold` as the final player-facing currency.

## Ordinary purchase/sell
Economy values are owned by `12_ECONOMY_AND_REWARDS`.

Shop UI must support:
- price in Auren;
- owned quantity;
- legal equipment recipient/slot where useful;
- buy;
- sell where allowed;
- unavailable/stock state;
- non-sellable protection.

## Ordinary equipment repurchase
Cresthaven Quartermaster is the full registered ordinary-equipment backfill authority.

The UI must be able to distinguish:
- item discovered/registered;
- currently owned;
- repurchasable.

## Vhalmarch
Vhalmarch is a forward military supply endpoint:
- essential field services;
- not a duplicate full ordinary-equipment superstore.

## Exceptional items
Do not make:
- Relics;
- Legacies;
- Forge Components;
- unique Legacy Components

look like ordinary infinitely purchasable shop stock unless their own domain explicitly allows it.

## OPEN
Exact:
- buy/sell tab design;
- quantity picker;
- stock badges;
- merchant compare pane;
- resale confirmation;
- Side Quest/Hunt Auren reward panel.
