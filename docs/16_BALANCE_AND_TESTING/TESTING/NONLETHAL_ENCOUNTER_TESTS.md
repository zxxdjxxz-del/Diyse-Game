# Diyse — Nonlethal / Protected Encounter Tests

**Status:** ACTIVE NONLETHAL / PROTECTED-OUTCOME QA  
**Story/enemy authority:** current `02_STORY` and `09_ENEMIES_AND_ENCOUNTERS` owners

Some authored encounters resolve without generic lethal defeat.

Current examples requiring protected/nonlethal handling include:
- **Elder Thornhide** in Chapter 4;
- Reaction Conduit stabilization;
- lawful-authority confrontations where current story authority specifies nonlethal resolution;
- prisoner/victim/coerced-human encounters;
- animal retreat contexts where explicitly authored.

Regression firewall:
- Chapter 1 **Thornhide** is the current normal lethal final boss and must **not** inherit retired Briarhide/Stalker nonlethal treatment.

## Presentation
Nonlethal resolution should suppress generic:
- death dissolve;
- corpse assumption;
- inappropriate victory pose;
- loot framing when not authored.

## Mechanics
Protected/nonlethal state must not:
- leave the target farmable;
- pay rewards repeatedly;
- corrupt later story state;
- create a universal Capture/Subdual/Mercy command.

Objective scripting controls the authored outcome.
