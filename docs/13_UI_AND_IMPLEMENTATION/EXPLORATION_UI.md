# Diyse — Exploration UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## CANON REQUIREMENT
Exploration UI should remain restrained so the HD-2D field remains readable.

It must be capable of presenting, when relevant:
- interaction prompt;
- current location/area transition;
- quest/objective update;
- travel availability;
- optional Hunt access;
- save/return warnings;
- field party/menu access.

## Random encounters
Random encounters remain normal hostile-exploration grammar in approved areas.

The field UI must not show a mandatory visible random-encounter meter unless separately approved.

Current runtime internally tracks encounter pressure, but that does **not** establish a player-facing gauge.

## Interaction
A contextual interaction prompt may cover:
- Talk;
- Examine;
- Open;
- Use;
- service access.

The exact player-facing wording may be authored per interaction.

## Chapter 0
Chapter 0 is authored/tutorial content, not normal random-encounter UI.

## OPEN PRODUCTION UX
- minimap vs no minimap;
- compass;
- permanent objective tracker;
- interaction icon language;
- encounter-transition overlay;
- exact field HUD density.
