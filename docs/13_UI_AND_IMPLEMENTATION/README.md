# 13_UI_AND_IMPLEMENTATION
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
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
- exact final layout, interaction styling, slot count, menu transition, animation, copy/original badge, service fee, etc. has not been approved and must not be invented as canon.

## Current implementation warning
The existing Godot repository still contains historical proof data and stale documentation in several places.

Notable examples:
- old `first_champion` proof Prime / bearer-lock assumptions;
- proof `gold` key instead of current **Auren**;
- proof Potion/equipment names;
- older Mastery-Point documentation;
- a proof battle UI rather than final production combat UI.

Those are implementation debt, not current-facing canon.
