# Diyse — Save / Load UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## IMPLEMENTED FOUNDATION
The current field proof exposes simple:
- SAVE
- LOAD

buttons and validates persistence behavior.

That is proof UI only.

## CANON REQUIREMENT
Save/load presentation must:
- never corrupt current state on a failed load;
- clearly report missing/invalid/unsupported saves;
- restore the correct saved area/position/state;
- not resurrect transient encounter handoff state;
- respect irreversible story locks once saved past them.

## Production save availability
Exact save-point/manual-save rules are not fully closed in this UI migration.

Do not invent:
- a fixed number of slots;
- autosave cadence;
- quicksave;
- cloud save;
- chapter-select;
- load-anywhere rules.

## Last Shelter
Last Shelter is explicitly:
- a final save/checkpoint;
- a final preparation point.

The UI must clearly warn that proceeding to Reactor Galleries crosses the irreversible threshold.

## OPEN PRODUCTION UX
- save slot count;
- thumbnail;
- playtime display;
- chapter/location label;
- overwrite confirmation;
- autosave indicator;
- backup/recovery slot behavior.
