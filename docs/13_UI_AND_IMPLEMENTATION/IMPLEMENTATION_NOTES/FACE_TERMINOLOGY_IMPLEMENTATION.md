# Implementation Notes — Current Face Terminology

**Status:** ACTIVE IMPLEMENTATION TERMINOLOGY HANDOFF  
**Owning Face authority:** `../../07_CARDS/SIX_FACES.md`

Current player-facing Face names are exactly:

> **Might / Elements / Grace / Perception / Memory / Ruin**

## Current semantic mapping

**Perception**
- precision;
- criticals;
- battlefield reading;
- timing and openings;
- especially Interrupt and other eligible queued-action interaction.

**Memory**
- Quick / Slow;
- Delay / Stuck;
- duration manipulation;
- delayed/echo effects;
- controlled recall/copy.

The Face model does not create additional universal combat stats.

## Runtime compatibility boundary

Serialized/runtime compatibility code may accept earlier internal Face identifiers only where required to load existing proof/save data safely.

Compatibility inputs must be normalized immediately to the six current Face identities and must never appear in player-facing UI, authored Card/Prime lists, dialogue, tutorials, or current content authority.

Current runtime storage and display should use:

> **Might / Elements / Grace / Perception / Memory / Ruin**
