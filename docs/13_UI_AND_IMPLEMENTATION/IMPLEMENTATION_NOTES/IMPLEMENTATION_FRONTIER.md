# Implementation Notes — Current Frontier
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Immediate active frontier
Current repository status identifies:
> **Kessara Relic-copy service implementation**

Core service logic is already present and tested.

Remaining production decisions:
- service/menu unlock timing;
- Auren fee, if any;
- original-vs-copy UI presentation.

## Before final UI production
Resolve the high-impact code/canon divergences first:
1. Mastery Point removal;
2. Prime loadout/access/duration/cooldown update;
3. Auren production state;
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
