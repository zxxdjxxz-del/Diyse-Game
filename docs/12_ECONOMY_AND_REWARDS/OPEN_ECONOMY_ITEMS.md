# Diyse — Economy Closure / Deferred Dependencies

**Current economy authority:** `12_ECONOMY_AND_REWARDS`

## Core economy-design status
> **CLOSED**

The G payout recalibration is complete at owner-domain level.

## Closed current structure
- currency = **G**;
- retired currency name = **Auren**;
- **1 economy unit = 200 G**;
- starting wallet = **2,500 G**;
- exactly **9 Regional Markets**;
- Cresthaven = separate long-term requisition/backfill authority;
- Vhalmarch = separate forward-supply endpoint;
- ordinary equipment identities = **38**;
- Consumables = **20**;
- ordinary enemies have **no random Consumable/equipment/material/junk drops**;
- Kessara Relic-copy fee = **6,000 G per successful copy**;
- protected/nonlethal resolution may award G and does not default to zero;
- Hunts give strong G regardless of separate permanent rewards;
- premium Consumables use one-copy-per-Consumable-shop stock from each shop's first accessible state;
- premium Consumables do not automatically restock and remain non-sellable.

## Closed direct-G calibration
Mandatory route:
> **~316,900 G**

Optional authored direct G:
> **329,600 G**

Broad completionist direct-cash reference:
> **~646,500 G**

This is intentionally close to the user-directed **~650,000 G** target.

Mandatory composition:
- starting wallet: **2,500 G**;
- ordinary formations: **~135,600 G**;
- mandatory story bosses/named encounters: **92,700 G**;
- fixed authored combat/event payouts: **5,300 G**;
- mandatory non-battle map: **80,800 G**.

Optional composition:
- Elites: **38,900 G**;
- ordinary Side Quests: **18,000 G**;
- Character Quests: **22,200 G**;
- Regional Hunts: **116,500 G**;
- Major Hunts: **134,000 G**.

## Closed price / sink synchronization
- ordinary equipment catalog value: **251,000 G**;
- ordinary equipment resale table synchronized;
- Consumable purchase/resale tables synchronized;
- Kessara all-18-copy maximum service spending: **108,000 G**.

## Deferred cross-domain / implementation dependencies
These remain open but do not reopen the numeric economy by themselves:
- story-owned special encounter placement before exact reward assignment where scene role is unresolved;
- vendor NPC identity/dialogue/presentation;
- runtime shop IDs, stock schema, save persistence and price UI formatting;
- Kessara menu timing / original-vs-copy UI labeling;
- later whole-game economy QA/playtest certification.

## Reopen rule
Reopen a closed economy value only when:
- a current playtest demonstrates a specific affordability/exploit failure;
- an owner-domain reward/source changes materially;
- or the user explicitly revises the economy design.

Do not restore retired Auren-era values as current G merely because an older file or audit still contains them.
