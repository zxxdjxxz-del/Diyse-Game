# Diyse — Runtime State Boundaries
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Persistent
State that changes the long-term playthrough should generally live in persistent game state/data:
- story progression;
- recruitment;
- levels/EXP;
- class/CEXP;
- item ownership;
- equipment;
- Cards/Primes;
- quest/Hunt completion;
- map/travel unlocks;
- world-state flags;
- Relic copy/component state.

## Transient
Scene-to-scene technical handoff that should not survive disk reload belongs in transient state.

Current proven example:
- generated random encounter payload;
- encounter return result.

These are intentionally excluded from save data.

## Derived
Where possible, do not serialize redundant currency/state if it can be safely derived from authoritative persistent values.

Current Mastery unlocks are a useful example:
- automatic Class-Level unlocks can be derived from current CL;
- there is no Mastery Point balance to save.

## UI-only
Selection cursor, open tab, temporary highlighted target, or unconfirmed queued menu navigation should not become durable gameplay state unless explicitly required.

## Scene nodes
Do not persist live scene-node references.
Persist semantic data/IDs and reconstruct presentation.
