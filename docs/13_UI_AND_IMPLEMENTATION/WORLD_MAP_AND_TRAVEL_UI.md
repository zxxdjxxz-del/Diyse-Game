# Diyse — World Map & Travel UI
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current UI/implementation-domain authority; Audit/v85 references remain provenance only. Cross-domain gameplay rules defer to their current owning repository domains.
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
