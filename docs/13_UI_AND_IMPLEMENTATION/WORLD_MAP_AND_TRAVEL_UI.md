# Diyse — World Map & Travel UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Current map terminology
Use:
- Yahtrenhold
- The Westways
- The Greyspires
- Black Host Territory
- The Blackspine
- Westguard
- Vhalmarch
- Vorathen
- The Veiled Citadel

Do not display retired labels as current destinations.

## Spatial authority
The current final world map's location placement is fixed by `04_WORLD_AND_LORE`.

UI markers must not relocate canonical places for convenience.

## Travel
World-map/fast-travel UI must respect story access.

Important late rule:
after Vhalmarch is secured:
> **Cresthaven ↔ Vhalmarch**

permanent two-way travel is available through the compatible cleanup/returnable period.

## Chapter 13
Starting Chapter 13:
- does not disable world return automatically.

Final return point:
> Last Shelter

Irreversible threshold:
> **Last Shelter → Reactor Galleries**

The travel UI must communicate the final lock clearly before the player crosses it.

## OPEN PRODUCTION UX
- exact atlas/map visual treatment;
- marker iconography;
- cursor behavior;
- route-line presentation;
- area completion indicators;
- quest/Hunt marker layering.
