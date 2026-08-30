# Diyse — Quest / Optional Content UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


Current optional authored inventory:
- 6 Character Quests
- 5 ordinary Side Quests
- 11 Regional Hunts
- 6 Major Hunts

## Required state representation
The UI must be capable of showing:
- locked/unavailable;
- available;
- active/in progress;
- completed;
- relevant location;
- current objective where authored;
- Hunt recommended level where current authority supplies one.

## Category firewall
Do not restore:
- a `Regional Quest` category;
- retired ten-side-quest count;
- retired removed Side Quests.

Hunts remain Hunts.

## Final cutoff
The quest UI must not mark all optional content expired merely because Chapter 13 begins.

True final cutoff:
> **Last Shelter → Reactor Galleries**

Any still-eligible content can remain returnable before that threshold.

## No morality branches
Do not show:
- alternate moral resolution paths;
- romance route flags;
- affinity outcome bars;
- dialogue-choice consequences.

## OPEN PRODUCTION UX
Exact:
- tracking/pinning;
- number of pinned objectives;
- map integration;
- completion timestamps;
- quest sorting/filtering.
