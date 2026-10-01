# Diyse — Menu Architecture
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current UI/implementation-domain authority; Audit/v85 references remain provenance only. Cross-domain gameplay rules defer to their current owning repository domains.
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## CANON REQUIREMENT
The final menu system must expose the current game state without creating obsolete systems.

Required functional access includes:
- party/formation;
- character status;
- class/CEXP/Masteries;
- Abilities;
- equipment;
- Cards;
- inventory/materials;
- quests/Hunts;
- world map/travel;
- save/load/options where legally available.

## Context-sensitive services
Separate service screens may exist for:
- ordinary shop;
- Cresthaven Quartermaster;
- Kessara Relic-copy service;
- native Legacy project;
- Vhalmarch Forward Supply.

These are service contexts, not necessarily permanent top-level menu tabs.

## Do not expose
- Mastery Points;
- Synthesis;
- Accessory equipment tab;
- deck/hand/discard;
- Prime XP;
- Prime Concordant screen;
- Bestiary mechanics not separately approved;
- crafting tree beyond current Forge/Legacy projects;
- dialogue affinity/romance values.

## OPEN PRODUCTION UX
Exact hierarchy remains open:
- tab order;
- whether Status and Formation are one screen or separate;
- whether Class and Ability are one screen or separate;
- whether Standard/Prime Cards share one screen;
- exact iconography;
- exact navigation animation.
