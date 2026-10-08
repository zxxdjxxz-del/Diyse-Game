# 13_UI_AND_IMPLEMENTATION

**Status:** ACTIVE UI / IMPLEMENTATION DOMAIN ROUTER  
**Authority rule:** current numbered owner domains define gameplay/content truth; proof runtime is engineering evidence only.

Canonical home for:

- production-facing UI requirements;
- current runtime-architecture status;
- input/control contracts;
- Android/landscape presentation constraints;
- menu/data-display requirements;
- save-data contract and compatibility boundaries;
- implementation divergences between current authority and proof runtime;
- validation/test gates;
- open UI/engineering decisions.

## Status distinction

**CANON REQUIREMENT**
- the UI/runtime must represent the current system this way.

**IMPLEMENTED FOUNDATION**
- current Godot code proves the architecture or behavior exists.

**OPEN PRODUCTION UX**
- final layout, interaction styling, animation, transitions, and other presentation details remain open unless an owning UI file closes them.

## Proof-runtime boundary

The proof runtime is not gameplay authority. Any proof field, fixture, UI surface, or save-compatibility path that differs from current owner-domain rules is implementation debt and must be migrated rather than used to redefine canon.

Verified gaps are tracked in:

> `IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

## Routing note

Current project sequencing is owned by:

> `../90_WORKING/ACTIVE_WORK_QUEUE.md`
