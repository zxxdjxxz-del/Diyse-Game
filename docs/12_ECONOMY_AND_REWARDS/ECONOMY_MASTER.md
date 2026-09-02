# Diyse — Economy Master

**Status:** CURRENT ECONOMY STRUCTURE / PAYOUT RECALIBRATION ACTIVE

**Domain rule:** `12_ECONOMY_AND_REWARDS` owns G denomination, purchase/replacement prices, sell rules, stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.

## Currency
The ordinary currency is:
> **G**

The former currency name **Auren** is retired.

Current display scale:
> **1 economy unit = 200 G**

Starting wallet:
> **2,500 G**

Current completionist direct-cash target:
> **roughly 650,000 G**

The older ~49.5k direct-cash calibration is retired and must not be restored as current authority.

## Design objective
The economy should support:
- routine field maintenance without punishment;
- meaningful but selective ordinary-equipment purchases;
- exploration and authored rewards retaining real value;
- optional content feeling economically useful without becoming mandatory money farming;
- subclass experimentation without forcing the player to preserve every starting item forever.

The intended checkpoint pressure remains:
> **one meaningful ordinary equipment purchase + routine consumable restock should usually be affordable without exhausting all funds.**

Buying every available upgrade immediately is not the baseline expectation.

## Current payout-recalibration requirements
The next numeric pass must preserve all of these user-directed corrections:
1. all current-facing currency values use **G**;
2. the displayed economy keeps the extra digit / tenfold presentation scale;
3. protected and nonlethal resolved encounters receive G rather than defaulting to zero;
4. Hunts give a strong G payout regardless of their separate Prime, Forge Component, item, or other reward;
5. broad completionist direct cash should land around **650,000 G**;
6. baseline story solvency must remain independent of optional content or repetitive grinding.

Existing older payout tables remain useful structural references but are not final numeric authority where they conflict with these requirements.

## Consumables
Normal-stock Consumables remain unlimited after their normal unlock.

Premium Consumables:
- **Emergency Kit — 8,000 G**;
- **Reservoir Tonic — 12,000 G**;
- **Emergency Rally — 15,000 G**.

Every Consumable-selling shop carries exactly:
- 1 Emergency Kit;
- 1 Reservoir Tonic;
- 1 Emergency Rally;

from that shop's first accessible state, with no automatic restock.

Guaranteed authored premium pickups remain separate and do not consume shop stock.

## Commerce structure
Exactly:
> **9 Regional Markets**

Cresthaven Quartermaster is a separate long-term requisition/backfill endpoint.
Vhalmarch is a separate forward-supply/requisition endpoint.

## Economy layers
### Normal commerce
- normal-stock Consumables;
- ordinary equipment purchase / replacement / requisition;
- G.

### Limited premium commerce
- Emergency Kit;
- Reservoir Tonic;
- Emergency Rally;
- 1 of each per Consumable-selling shop;
- no automatic restock.

### Authored reward layer
- guaranteed ordinary equipment;
- Relics;
- Legacy precursors/components;
- Cards / Primes;
- guaranteed premium Consumables;
- Forge Components;
- quest/story objects.

Relics, Legacies, Forge Components, Cards, and Primes do not become ordinary shop stock merely because they have economic value.

## Encounter-income rules
- ordinary formation G is formation-level;
- support/summoned/generated bodies add no second payout unless explicitly authored;
- ordinary enemies have **no random Consumable/equipment/material/junk drop table**;
- fresh boss forms do not automatically generate a second payout;
- protected/nonlethal resolution does **not** mean zero G;
- story context may present G as requisition credit, secured funds, bounty, operational reserve, or another appropriate economic handoff rather than literal coins.

## No junk-economy requirement
Do not create a large vendor-trash layer merely to feed money back to the player.

Do not add by default:
- generic monster parts;
- sell-only junk;
- low-percentage equipment farming;
- low-percentage Consumable farming.

## Mandatory/optional separation
Baseline story affordability must never require:
- Side Quests;
- optional Elites;
- Regional Hunts;
- Major Hunts;
- Character Quests;
- resale;
- repetitive grinding.

Optional content should make the player richer and widen build flexibility, not repair an underfunded mandatory route.

## Current work state
Structural economy rules are current, but the exact campaign payout tables are reopened for synchronization to:
- G terminology;
- the tenfold display scale;
- protected/nonlethal payouts;
- stronger Hunt cash rewards;
- the ~650,000 G completionist target.

## Ownership
- `08` owns item identity/stats/effects/source identity.
- `09` owns enemies/formations.
- `10` owns Player EXP/CEXP.
- `11` owns quest/hunt access and completion state.
- `12` owns G, prices, stock and non-EXP reward economy.
