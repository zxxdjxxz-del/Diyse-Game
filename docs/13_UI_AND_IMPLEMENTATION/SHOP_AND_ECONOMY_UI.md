# Diyse — Shop / Economy UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Currency
Current ordinary currency:
> **G**

Do not expose `Gold` or retired `Auren` as the final player-facing currency.

## Ordinary purchase/sell
Economy values are owned by `12_ECONOMY_AND_REWARDS`.

Shop UI must support:
- price in G;
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
- Side Quest/Hunt G reward panel.
