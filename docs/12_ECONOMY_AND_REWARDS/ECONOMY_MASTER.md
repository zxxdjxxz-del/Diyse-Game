# Diyse — Economy Master

**Status:** **ECONOMY REBUILD / RECALIBRATION PENDING — LEGACY NUMERIC MODEL RETAINED FOR REFERENCE**

**Domain rule:** `12_ECONOMY_AND_REWARDS` owns the economy domain and remains the home for the future rebuild. **G** remains current player-facing currency terminology. The numeric calibration below is retained as historical/provisional planning material and is **not** a hard current lock while the rebuild is pending. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.

## Currency terminology
The ordinary currency is:
> **G**

The former currency name **Auren** is retired.

Legacy/provisional planning references:
- prior display/calibration scale: **1 economy unit = 200 G**;
- prior starting-wallet figure: **2,500 G**.

These values remain reference material only until the economy rebuild explicitly relocks them.

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

## Provisional legacy mandatory-route calibration
Legacy/provisional direct-G reference:
> **approximately 316,300 G**

Composition:
- starting wallet: **2,500 G**;
- ordinary Chapter 1–13 formations: **~135,600 G**;
- mandatory story bosses / named encounters: **92,100 G**;
- fixed authored combat/event payouts: **5,300 G**;
- mandatory non-battle reward map: **80,800 G**.

Ordinary formations therefore contribute approximately:
> **42.9%**

of the calibrated mandatory-route direct G, preserving the intended **40–50%** ordinary-encounter share.

Retained structural intent: protected/nonlethal resolution does **not** automatically imply zero G; exact payouts remain rebuild-pending.

The legacy mandatory-route aggregate is not a complete current ledger because Chapter 3's mandatory **Memory Construct** payout has not yet been assigned. Do not treat the ~316,300-G figure as a closed current total.

## Historical/provisional chapter-liquidity model

Chapter 1's current per-formation G remap remains open, so the liquidity result below is a **provisional stress-test pass** rather than a final exact Chapter-1 certification.
The whole-game total is also validated at chapter scale in:
> `CHAPTER_G_LIQUIDITY_VALIDATION.md`

Stress-test model using **mandatory-route income only**:
- meaningful ordinary-equipment purchase allowance through Chapter 12: **115,600 G** total;
- substantial routine HP/MP/revive/status Consumable restocking: **171,400 G** total;
- combined modeled spending: **287,000 G**.

Historical model result:
> **PASS under the former calibration**

This is not current final economy certification.

Tightest late-game checkpoint:
> **Chapter 10 — approximately 6,600 G remains after modeled equipment + routine restock**

Modeled end-of-Chapter-13 wallet:
> **approximately 29,270 G**

The former stress-test model suggested mandatory-route solvency under that calibration; it is retained as historical evidence only.

Premium Consumables are deliberately excluded from baseline solvency. Buying Emergency Kit / Reservoir Tonic / Emergency Rally is optional emergency/luxury spending, not routine healing maintenance.

## Provisional legacy optional direct-G layer
Legacy/provisional optional direct-G reference if all authored activities are cleared:
- 5 ordinary Side Quests: **18,000 G**;
- 6 Character Quests: **22,200 G**;
- 8 active Regional Hunts: **106,000 G**;
- 6 Major Hunts: **134,000 G**.

Legacy/provisional optional direct-G subtotal after retiring the former-Elite bounty layer:
> **280,200 G**

## Provisional legacy completionist direct-cash reference
Legacy mandatory reference + legacy optional direct-G reference:
> **approximately 596,500 G**

This is **below the prior ~650,000-G broad completionist target** because the historical standalone Elite-bounty layer has been retired.

Do not restore separate strong-enemy bounties simply to recover an older completionist total. Any future completionist-cash target belongs to the dedicated economy rebuild.

This completionist reference excludes:
- equipment/Consumable resale;
- deliberate extra ordinary encounters/backtracking;
- non-cash reward-equivalent value.

## Legacy/provisional major sinks / purchase references
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

## Hunt reward intent — retained; exact G values pending rebuild
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
- Regional Hunts → `REGIONAL_HUNT_REWARD_BOUNDARY.md`
- Major Hunts → `MAJOR_HUNT_REWARD_BOUNDARY.md`
- Side Quests → `SIDE_QUEST_REWARD_BOUNDARY.md`
- Character Quests → `CHARACTER_QUEST_REWARD_BOUNDARY.md`
- ordinary equipment prices/resale → `ORDINARY_EQUIPMENT_PRICING.md`, `ORDINARY_EQUIPMENT_SELL_RULE.md`
- Consumable prices/resale → `CONSUMABLE_PRICES.md`, `CONSUMABLE_SELL_RULE.md`
- Kessara → `KESSARA_RELIC_COPY_ECONOMY.md`

## Rebuild rule
Detailed economy values are already **open for rebuild/recalibration**. Do not spend cleanup/consolidation work polishing or propagating legacy numeric totals. Relock prices/payouts/liquidity only through the dedicated future economy pass.

## Ownership
- `08` owns item identity/stats/effects/source identity.
- `09` owns enemies/formations.
- `10` owns Player EXP/CEXP.
- `11` owns quest/hunt access and completion state.
- `12` owns G, prices, stock and non-EXP reward economy.
