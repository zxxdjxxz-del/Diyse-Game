# Implementation Notes — Current Frontier
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## Completed bounded frontier — G wallet / Kessara transaction
Implemented:
- persistent `wallet_g` state;
- current **2,500 G** starting baseline;
- version-safe persistence/migration;
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

## Completed bounded frontier — production permanent roster / active party
Implemented in schema **v3**:
- stable permanent character IDs: `cyanis`, `ilyra`, `torren`, `nimera`, `vaelira`, `seyrik`;
- six persistent roster records independent of the old four-character proof battle fixture;
- first-name-only display identities normalized from stable IDs;
- recruitment state separate from active-party membership;
- active-party cap **4**;
- duplicate, unknown and unrecruited active-party entries rejected;
- current new-game production baseline: Cyanis recruited and active, later permanent characters present but unrecruited;
- reserved per-character `persistent_state` envelope without inventing final progression/stat values;
- v2 → v3 migration that deliberately does **not** infer recruitment from the old four-character proof `party` array;
- dedicated roster/formation regression coverage plus save round-trip/migration coverage.

The legacy `party` fixture remains temporarily for existing proof battle/exploration compatibility. It is no longer the permanent-roster authority.

## Immediate active frontier — class / Face / loadout state
The next structural layer is per-character class/loadout state on top of the stable roster.

Current class identities:
- Cyanis — Crest Knight / Crest Arcanist;
- Ilyra — Blue Warden / Vowblade;
- Torren — War Archer / Routeweaver;
- Nimera — Cardweaver / Proofhunter;
- Vaelira — Green Arcanist / Axiomblade;
- Seyrik — Ruin Vanguard / Ruin Warden.

Required foundation:
- stable class IDs separated from display names;
- Base/Subclass ownership tied to stable character ID;
- selected class state without allowing Subclass use before Sixfold Volition;
- Class Level/CEXP-compatible state shape without inventing deferred final numeric progression;
- automatic Mastery derivation path with **no Mastery Point currency**;
- Standard Card loadout capacity **3 per character**;
- Prime loadout capacity represented separately from Standard Cards;
- Prime slot count capable of 1 from Chapter-4 loadout access and 2 after Sixfold Volition;
- versioned save migration from schema v3.

Current class terminology is routed through:
`../../00_MASTER_CONTROL/CLASS_TERMINOLOGY_CURRENT.md`

This stage is state architecture, not final class menu UX and not a balance pass.

## Before final UI production
High-impact structural divergences still to resolve include:
1. class/Face/loadout state without Mastery Points;
2. Prime collection/access/spend/restoration/spacing state;
3. turn-entry combat core replacing whole-round queue/Confirm Round;
4. production character/equipment/item data replacing proof fixtures;
5. expanded production quest/world/settings save state.

## Recommended implementation sequence
This is an engineering order, not new canon:
1. class/Face/loadout state;
2. Prime collection/persistence;
3. turn-entry combat core;
4. Recovered/Awakened Prime sequencing;
5. production UI shells;
6. quest/map/shop/service UI;
7. accessibility/polish;
8. broad Android validation.

Do not build elaborate final menus on top of stale proof state.
