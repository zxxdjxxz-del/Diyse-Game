# Implementation Notes — Current Frontier
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## Immediate active frontier
Current repository status identifies the Kessara Relic-copy path as a useful bounded implementation frontier.

Already implemented:
- original Relic ownership requirement;
- matching-Face copy-component requirement;
- one forged duplicate maximum per individual Relic;
- quantity cap 2;
- three forged Relics maximum per Face;
- Legacy rejection;
- same Relic identity retained for the forged copy;
- current Face canonicalization for **Might / Elements / Grace / Perception / Memory / Ruin**;
- compatibility aliases that migrate retired Resource/Acuity/Change Face labels into Perception/Memory rather than re-exposing them as current names.

Current authority already fixes the service fee at:
> **6,000 G per successful Relic copy**

The fee amount is **not open** and must not be described as Auren.

Still unresolved/unfinished at the implementation layer:
- exact service/menu unlock timing where not separately fixed by its owning content authority;
- production service-menu presentation;
- atomic deduction of the 6,000 G fee once the production currency/wallet state is reconciled;
- original-vs-forged-copy UI presentation.

## Before final UI production
Resolve the high-impact code/canon divergences first:
1. Mastery Point removal;
2. Prime loadout/access/duration/spend/restoration/spacing update;
3. production **G** wallet/state migration from proof `gold` semantics;
4. production character/equipment/item data replacing proof fixtures;
5. expanded production save schema.

## Recommended implementation sequence
This is an engineering order, not new canon:
1. data/state reconciliation;
2. save schema versioning/migration;
3. production party/status/menu skeleton;
4. equipment + Cards/Primes;
5. combat HUD;
6. quest/map/shop/service UIs;
7. accessibility/polish;
8. broad Android validation.

Do not build elaborate final menus on top of stale proof state.
