# 13_UI_AND_IMPLEMENTATION
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current UI/implementation-domain authority; Audit/v85 references remain provenance only. Cross-domain gameplay rules defer to their current owning repository domains.
**Runtime source checkpoint inspected:** `Diyse-Game` main commit `2127e6a7d80ce5c4070193a9a47b47868d79087a`.  
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
- exact final layout, interaction styling, slot count, menu transition, animation, copy/original badge, and other production presentation details remain open; numeric service-fee values belong to the rebuild-pending economy owner and must not be invented here.

## Current implementation warning
The existing Godot repository still contains historical proof data and stale documentation in several places.

Notable examples:
- old `first_champion` proof Prime / bearer-lock assumptions;
- proof `gold` technical key versus current player-facing **G** terminology; detailed numeric economy values remain rebuild-pending;
- proof Potion/equipment names;
- older Mastery-Point documentation;
- a proof battle UI rather than final production combat UI.

Those are implementation debt, not current-facing canon.


## Routing note
Current project priority is not owned by this README. Use `../90_WORKING/ACTIVE_WORK_QUEUE.md` for active sequencing and `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md` for verified runtime gaps.
