# 13_UI_AND_IMPLEMENTATION
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit corrections already preserved in the reorganized domains.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

Canonical home for:
- production-facing UI requirements;
- current runtime-architecture status;
- input/control contracts;
- Android/landscape presentation constraints;
- menu/data-display requirements;
- save-data contract and migration boundaries;
- implementation divergences between current canon and the existing proof runtime;
- validation/test gates;
- open UI/engineering decisions.

## Status distinction

Three labels are used throughout this folder:

**CANON REQUIREMENT**
- the UI/runtime must represent the current system this way.

**IMPLEMENTED FOUNDATION**
- current Godot code proves the architecture or behavior exists.

**OPEN PRODUCTION UX**
- exact final layout, interaction styling, menu transition, animation, copy/original badge treatment, or other presentation behavior has not been approved and must not be invented as canon.

A value already fixed by another owning domain does **not** become open merely because the final UI is unfinished. Example: Kessara's Relic-copy fee is already **6,000 G per successful copy**; the production service menu and fee-debit implementation remain unfinished.

## Current implementation warning
The existing Godot repository still contains historical proof data and stale technical identifiers in several places.

Notable examples:
- old `first_champion` proof Prime / bearer-lock assumptions;
- proof `gold` key instead of current player-facing **G**;
- proof Potion/equipment names;
- older Mastery-Point behavior/tests/documentation;
- proof character/portrait placeholders;
- a proof queued-round battle UI rather than final production combat UI.

Those are implementation debt, not current-facing canon.

## Key routing files

- `CURRENT_RUNTIME_IMPLEMENTATION_STATUS.md` — what the present runtime actually proves.
- `IMPLEMENTATION_AUTHORITY_PRECEDENCE.md` — conflict resolution for implementation work.
- `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md` — known proof-vs-current gaps.
- `IMPLEMENTATION_NOTES/IMPLEMENTATION_FRONTIER.md` — current engineering frontier/order.
- `IMPLEMENTATION_NOTES/RUNTIME_ID_MIGRATION_MAP.md` — save/content-safe mapping for legacy technical IDs and retired terminology.

Before renaming a legacy runtime ID, determine whether it is serialized or referenced by Resources/tests. Prefer explicit migration over cosmetic source-tree cleanup.
