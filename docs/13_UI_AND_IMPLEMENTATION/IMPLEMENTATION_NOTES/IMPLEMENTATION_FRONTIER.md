# Implementation Notes — Current Frontier
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` main commit `2127e6a7d80ce5c4070193a9a47b47868d79087a`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Current routing role
This file is a **summary/router**, not an independent project-priority queue.

Detailed current sequencing is owned by:
- `../../90_WORKING/ACTIVE_WORK_QUEUE.md`;
- `../../90_WORKING/IMPLEMENTATION_FRONTIER_WORKING.md`;
- `CURRENT_CODE_DIVERGENCES.md` for verified runtime/canon gaps.

Do not revive an older “Kessara service first” priority from this file.

Kessara Relic-copy service logic already exists as implementation foundation. Remaining menu timing, original-vs-copy presentation, and any service-fee value belong to the current UI/equipment/economy owners. **Auren is retired; player-facing currency terminology is G, while detailed numeric economy values remain rebuild-pending.**

## Before final UI production
Resolve the still-current high-impact divergences in `CURRENT_CODE_DIVERGENCES.md`, including:
- stale Mastery Point assumptions;
- stale `first_champion` / Prime proof behavior and the current persistent-spend + three-round spacing model;
- proof `gold` technical semantics versus player-facing **G** terminology, without hard-coding rebuild-pending economy numbers;
- production character/equipment/item data replacing proof fixtures;
- expanded/versioned production save schema;
- production turn-entry combat flow and HUD replacing the proof whole-round queue / Confirm Round model.

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
