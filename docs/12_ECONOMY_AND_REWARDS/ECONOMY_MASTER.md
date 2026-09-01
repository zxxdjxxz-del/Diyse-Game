# Diyse — Economy Master

**Status:** CORE ECONOMY DESIGN / CALIBRATION CLOSED

**Domain rule:** `12_ECONOMY_AND_REWARDS` owns Auren denomination, purchase/replacement prices, sell rules, normal-stock progression, commerce endpoint roles, reward-value/scarcity rules, and non-EXP reward handoffs. Item definitions remain in `08`; enemy bodies remain in `09`; EXP/CEXP remain in `10`; quest structure remains in `11`.

## Design objective
The economy should support:
- routine field maintenance without punishment;
- meaningful but selective ordinary-equipment purchases;
- exploration and authored rewards retaining real value;
- optional content feeling economically useful without becoming mandatory money farming;
- subclass experimentation without forcing the player to preserve every starting item forever.

The intended checkpoint pressure is:
> **one meaningful ordinary equipment purchase + routine consumable restock should usually be affordable without exhausting all funds.**

Buying every available upgrade immediately is not the baseline expectation.

## Current numeric calibration
### Mandatory route
Current expected direct Auren:
> **approximately 30,127 Auren**

Composition:
- ordinary formations: **~13,560 Auren**;
- mandatory story bosses / resolved boss encounters: **8,490 Auren**;
- mandatory non-battle reward map: **8,080 Auren**.

Ordinary formations therefore contribute approximately:
> **45%**

of the current mandatory-route direct-currency center.

The acceptable mandatory-route corridor remains approximately:
> **27,100–33,900 Auren**

before optional-content income, selling, or deliberate extra combat.

### Optional direct-cash layer
Current optional direct Auren if all authored activities are cleared:
- 12 numbered-chapter optional Elites: **3,890**;
- 5 ordinary Side Quests: **1,800**;
- 6 Character Quests: **2,220**;
- 11 Regional Hunts: **5,280**;
- 6 Major Hunts: **6,200**.

Total optional direct cash:
> **19,390 Auren**

### Completionist direct-cash reference
Mandatory center + all current optional direct cash:
> **approximately 49,517 Auren**

This excludes:
- equipment/Consumable resale;
- any deliberate extra ordinary encounters/backtracking;
- non-cash reward-equivalent value.

## Current major sinks / purchase references
### Ordinary equipment
There are exactly:
> **38 ordinary equipment identities**

Their complete registered purchase/replacement values total:
> **25,100 Auren**

This is a conservative catalog-value ceiling, **not expected campaign spending**, because many first copies are starting/join gear, guaranteed finds, protected caches, or authored rewards rather than purchases.

### Kessara Relic-copy service
Service fee:
> **600 Auren per successful Relic copy**

There are currently 18 Relic-copy-specific Forge Component source slots.
If all 18 copy opportunities are used, total service spending is:
> **10,800 Auren**

This is an intentional completionist sink; the copy-specific Forge Component remains the primary scarcity gate.

### Consumables
- normal-stock Consumables remain unlimited after their appropriate unlock;
- normal-stock resale is deliberately low, approximately 25% of purchase price;
- reward-only Reservoir Tonic / Emergency Kit / Emergency Rally are finite and non-sellable.

Exact finite reward-only supply:
- **Reservoir Tonic ×3**;
- **Emergency Kit ×4**;
- **Emergency Rally ×2**.

Total reward-equivalent value of those nine finite items:
> **4,120 Auren equivalent**

They are non-sellable, so this value does not increase spendable-Auren calibration.

## Commerce structure
Exactly:
> **9 Regional Markets**

Cresthaven Quartermaster is a separate long-term requisition/backfill endpoint.
Vhalmarch is a separate forward-supply/requisition endpoint.

Relics, Legacies, Forge Components, Cards, Primes, and reward-only Consumables do not become ordinary shop stock merely because they have economic value.

## Economy layers
### Normal commerce
- normal-stock Consumables;
- ordinary equipment purchase / replacement / requisition;
- Auren.

### Authored reward layer
- guaranteed ordinary equipment;
- Relics;
- Legacy precursors/components;
- Cards / Primes;
- exceptional reward-only Consumables;
- Forge Components;
- quest/story objects.

Exceptional equipment is not converted into a normal shop ladder merely because it has economic value.

## Encounter-income rules
- ordinary formation Auren is exact and formation-level;
- support/summoned/generated bodies add no second payout;
- ordinary enemies have **no random Consumable/equipment/material/junk drop table**;
- optional Elites, Regional Hunts, Major Hunts, and story bosses use their authored first-clear/event payouts;
- fresh boss forms do not generate a second Auren payout;
- story-placement-dependent special encounters remain reward-deferred until their exact role is finalized.

## Mandatory non-battle reward map
The exact **8,080-Auren** chapter/location/delivery map lives in:
> `MANDATORY_NONBATTLE_AUREN_BUDGET.md`

Economic placement is closed.
Exact prop art, NPC handoff line, UI toast, and scene scripting hook remain presentation/implementation details only.

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

## Independent economy-design status
> **No independent numeric economy/reward gaps remain open.**

Remaining dependencies belong to other workstreams:
- special authored encounter Auren where exact scene role remains unresolved → story/dialogue/enemy integration;
- vendor NPC identity/dialogue/presentation → story/world/dialogue production;
- Auren glyph/icon → visual/UI;
- runtime shop IDs, stock schema, save persistence and price UI → implementation;
- Kessara copy-menu timing / original-vs-copy labeling → implementation/UI.

These do not reopen the closed economy values by themselves.

## Reopen rule
Reopen a closed economy value only when:
- a current playtest demonstrates a specific affordability/exploit failure;
- an owner-domain reward/source changes materially;
- or the user explicitly revises the economy design.

## Ownership
- `08` owns item identity/stats/effects/source identity.
- `09` owns enemies/formations.
- `10` owns Player EXP/CEXP.
- `11` owns quest/hunt access and completion state.
- `12` owns Auren, prices, stock and non-EXP reward economy.
