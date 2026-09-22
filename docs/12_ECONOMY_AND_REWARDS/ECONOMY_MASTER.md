# Diyse — Economy Master

**Status:** CORE ECONOMY DESIGN / OPTIONAL-CASH CALIBRATION REOPENED AFTER FORMER-ELITE CONVERSION

**Domain rule:** `12_ECONOMY_AND_REWARDS` owns G denomination, purchase/replacement prices, sell rules, stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.

## Currency
The ordinary currency is:
> **G**

The former currency name **Auren** is retired.

Current display scale:
> **1 economy unit = 200 G**

Starting wallet:
> **2,500 G**

## Design objective
The economy should support:
- routine field maintenance without punishment;
- meaningful but selective ordinary-equipment purchases;
- exploration and authored rewards retaining real value;
- optional content feeling economically useful without becoming mandatory money farming;
- subclass experimentation without forcing the player to preserve every starting item forever.

The intended checkpoint pressure remains:
> **one meaningful ordinary equipment purchase + routine Consumable restock should usually be affordable without exhausting all funds.**

Buying every available upgrade immediately is not the baseline expectation.

## Mandatory-route calibration
Current expected direct G:
> **approximately 316,900 G**

Composition:
- starting wallet: **2,500 G**;
- ordinary Chapter 1–13 formations: **~135,600 G**;
- mandatory story bosses / named encounters: **92,700 G**;
- fixed authored combat/event payouts: **5,300 G**;
- mandatory non-battle reward map: **80,800 G**.

Ordinary formations therefore contribute approximately:
> **42.8%**

of the calibrated mandatory-route direct G, preserving the intended **40–50%** ordinary-encounter share.

Protected/nonlethal resolution is included in the current economy and does **not** default to zero G.

## Chapter liquidity certification
The whole-game total is also validated at chapter scale in:
> `CHAPTER_G_LIQUIDITY_VALIDATION.md`

Stress-test model using **mandatory-route income only**:
- meaningful ordinary-equipment purchase allowance through Chapter 12: **115,600 G** total;
- substantial routine HP/MP/revive/status Consumable restocking: **171,400 G** total;
- combined modeled spending: **287,000 G**.

Result:
> **PASS — wallet remains positive through every chapter**

Tightest late-game checkpoint:
> **Chapter 10 — approximately 7,200 G remains after modeled equipment + routine restock**

Modeled end-of-Chapter-13 wallet:
> **approximately 29,870 G**

This confirms that normal equipment progression and routine recovery supplies do not require optional content or grinding.

Premium Consumables are deliberately excluded from baseline solvency. Buying Emergency Kit / Reservoir Tonic / Emergency Rally is optional emergency/luxury spending, not routine healing maintenance.

## Optional direct-G layer
Current optional direct G if all authored activities are cleared:
- 5 ordinary Side Quests: **18,000 G**;
- 6 Character Quests: **22,200 G**;
- 11 Regional Hunts: **116,500 G**;
- 6 Major Hunts: **134,000 G**.

Current optional direct G after retiring the former-Elite bounty layer:
> **290,700 G**

## Completionist direct-cash reference
Mandatory center + current optional direct G:
> **approximately 607,600 G**

This is **below the prior ~650,000-G broad completionist target** because the historical 38,900-G standalone optional-Elite bounty layer has been retired.

Do not restore those bounties simply to recover the old total. The completionist-cash calibration is reopened and should be solved later through the current economy process if the ~650,000-G target is still desired.

This completionist reference excludes:
- equipment/Consumable resale;
- deliberate extra ordinary encounters/backtracking;
- non-cash reward-equivalent value.

## Current major sinks / purchase references
### Ordinary equipment
There are exactly:
> **38 ordinary equipment identities**

Their complete registered purchase/replacement values total:
> **251,000 G**

This is a conservative catalog-value ceiling, **not expected campaign spending**, because many first copies are starting/join gear, guaranteed finds, protected caches, or authored rewards rather than purchases.

### Kessara Relic-copy service
Service fee:
> **6,000 G per successful Relic copy**

There are currently 18 Relic-copy-specific Forge Component source slots.
If all 18 copy opportunities are used, total service spending is:
> **108,000 G**

This is an intentional completionist sink; the copy-specific Forge Component remains the primary scarcity gate.

### Consumables
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
Premium Consumables remain non-sellable.

## Commerce structure
Exactly:
> **9 Regional Markets**

Cresthaven Quartermaster is a separate long-term requisition/backfill endpoint.
Vhalmarch is a separate forward-supply/requisition endpoint.

## Hunt reward rule — LOCKED
Regional and Major Hunts should provide **strong G regardless of separate permanent/item rewards**.

Do not reduce Hunt cash merely because the Hunt also grants:
- a Prime;
- Forge Component;
- Legacy precursor/component;
- premium Consumable;
- another deterministic permanent reward.

## Encounter-income rules
- ordinary formation G is formation-level;
- support/summoned/generated bodies add no second payout unless explicitly authored;
- ordinary enemies have **no random Consumable/equipment/material/junk drop table**;
- fresh boss forms do not automatically generate a second payout;
- protected/nonlethal resolution does **not** mean zero G;
- story context may present G as requisition credit, secured funds, bounty, operational reserve, or another appropriate economic handoff rather than literal coins.

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
- Regional Hunts;
- Major Hunts;
- Character Quests;
- resale;
- repetitive grinding.

Optional content should make the player richer and widen build flexibility, not repair an underfunded mandatory route.

## Current owner files
- currency/display scale → `CURRENCY_AND_PRICE_UNIT.md`
- ordinary formations → `ENCOUNTER_G_REWARDS.md`
- story bosses/named encounters → `STORY_BOSS_G_REWARDS.md`
- fixed authored combats → `ENEMY_REWARD_HANDOFF.md`
- mandatory non-battle map → `MANDATORY_NONBATTLE_G_BUDGET.md`
- chapter liquidity validation → `CHAPTER_G_LIQUIDITY_VALIDATION.md`
- former optional-Elite reward retirement → `ELITE_G_REWARDS.md`
- Regional Hunts → `REGIONAL_HUNT_REWARD_BOUNDARY.md`
- Major Hunts → `MAJOR_HUNT_REWARD_BOUNDARY.md`
- Side Quests → `SIDE_QUEST_REWARD_BOUNDARY.md`
- Character Quests → `CHARACTER_QUEST_REWARD_BOUNDARY.md`
- ordinary equipment prices/resale → `ORDINARY_EQUIPMENT_PRICING.md`, `ORDINARY_EQUIPMENT_SELL_RULE.md`
- Consumable prices/resale → `CONSUMABLE_PRICES.md`, `CONSUMABLE_SELL_RULE.md`
- Kessara → `KESSARA_RELIC_COPY_ECONOMY.md`

## Reopen rule
Reopen a closed economy value only when:
- a current playtest demonstrates a specific affordability/exploit failure;
- actual battle-consumption simulation materially exceeds the certified restock allowance;
- an owner-domain reward/source changes materially;
- or the user explicitly revises the economy design.

## Ownership
- `08` owns item identity/stats/effects/source identity.
- `09` owns enemies/formations.
- `10` owns Player EXP/CEXP.
- `11` owns quest/hunt access and completion state.
- `12` owns G, prices, stock and non-EXP reward economy.
