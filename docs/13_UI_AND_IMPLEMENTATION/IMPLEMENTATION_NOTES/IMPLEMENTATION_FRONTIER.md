# Implementation Notes — Current Frontier
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## Recently completed bounded frontier — G wallet / Kessara transaction
Implemented:
- persistent `wallet_g` state;
- current **2,500 G** starting baseline;
- schema-v2 persistence;
- deliberate schema-v1 → v2 migration;
- no reinterpretation of legacy proof `rewards.gold` as the wallet;
- wallet affordability/credit/spend operations;
- exact Kessara fee **6,000 G per successful Relic copy**;
- insufficient-G rejection without mutation;
- successful G deduction + matching component consumption + forged-copy state committed through one GameState transaction;
- current Face canonicalization for **Might / Elements / Grace / Perception / Memory / Ruin**;
- compatibility aliases that normalize retired Resource/Acuity/Change values into Perception/Memory.

Still open for Kessara presentation only:
- exact service/menu unlock timing where not separately fixed by its owning content authority;
- production service-menu presentation;
- original-vs-forged-copy visual treatment;
- confirmation/animation polish.

The fee itself and wallet transaction behavior are no longer open implementation gaps.

## Immediate active frontier — production party / character state
The next structural state layer is to stop treating the four proof characters as the complete permanent roster.

Required foundation:
- stable character IDs for the six permanent characters;
- recruited-roster state separate from active-party state;
- active battle party capped at **4**;
- persistent per-character state container suitable for later Level/EXP, class/CEXP, equipment, Standard Card and Prime loadouts;
- current first-name-only display identities;
- migration that preserves useful proof HP/MP/state without making proof fixture stats/content authoritative;
- no premature final stat-table lock inside the state schema.

Permanent six:
- Cyanis;
- Ilyra;
- Torren;
- Nimera;
- Vaelira;
- Seyrik.

This stage is state architecture, not final party UI and not a balance pass.

## Before final UI production
High-impact structural divergences still to resolve include:
1. production party/character state;
2. class/loadout state without Mastery Points;
3. Prime loadout/access/spend/restoration/spacing state;
4. turn-entry combat core replacing whole-round queue/Confirm Round;
5. production character/equipment/item data replacing proof fixtures;
6. expanded production quest/world/settings save state.

## Recommended implementation sequence
This is an engineering order, not new canon:
1. production party/character state;
2. class/Face/loadout state;
3. Prime collection/persistence;
4. turn-entry combat core;
5. Recovered/Awakened Prime sequencing;
6. production UI shells;
7. quest/map/shop/service UI;
8. accessibility/polish;
9. broad Android validation.

Do not build elaborate final menus on top of stale proof state.
