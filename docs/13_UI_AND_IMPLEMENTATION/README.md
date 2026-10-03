# 13_UI_AND_IMPLEMENTATION

**Status:** ACTIVE UI / IMPLEMENTATION DOMAIN ROUTER  
**Authority rule:** current numbered owner domains define gameplay/content truth; proof runtime is engineering evidence only.

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
The existing Godot repository still contains historical proof data and compatibility-era implementation residue in several places.

Notable examples:
- old `first_champion` proof Prime / bearer-lock assumptions;
- proof reward amounts and detailed numeric economy values remain rebuild-pending; current runtime/save storage uses `rewards.g`, with legacy `rewards.gold` load compatibility;
- proof Potion/equipment names;
- a proof battle UI rather than final production combat UI.

Those are implementation debt, not current-facing canon.


## Routing note
Current project priority is not owned by this README. Use `../90_WORKING/ACTIVE_WORK_QUEUE.md` for active sequencing and `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md` for verified runtime gaps.
