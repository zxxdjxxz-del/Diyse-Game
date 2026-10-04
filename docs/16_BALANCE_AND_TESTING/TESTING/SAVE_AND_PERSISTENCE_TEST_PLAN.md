# Diyse — Save / Persistence Test Plan

**Status:** ACTIVE SAVE / PERSISTENCE QA PLAN  
**Current schema authority:** implementation/save owners plus current numbered system domains

Existing proof coverage is useful, but production schema must expand beyond proof fixtures.

## Existing tests should continue to verify
- missing save safe failure;
- invalid JSON safe failure;
- unsupported future schema rejection;
- state round-trip;
- intentionally supported prior-schema normalization;
- transient random-encounter state excluded;
- transient state cleared on load.

## Production-state coverage must add/verify
- Player EXP/Level;
- Base/Subclass CL/CEXP;
- selected class;
- automatic Mastery unlock derivation/state;
- player-facing **G** currency semantics;
- equipment/loadouts;
- Relic copies;
- Legacy project state;
- Standard Cards/Primes/loadouts;
- persistent Prime spent/Ready state where current authority requires it;
- quests/Hunts;
- world/travel flags;
- story state;
- settings.

## Serialization boundary

Production saves must represent current systems directly:
- Masteries derive from Class Level; there is no separate Mastery-resource field;
- ordinary currency persists as **G**;
- supported schema-v1 `rewards.gold` may normalize on load but is not a separate current currency system;
- unconfirmed UI cursor state is not persistent canon;
- live scene-node references are not serialized.

## Exploit regression

Test save/load around:
- reward collection;
- Hunt first clear;
- Kessara Relic copy;
- shop transactions;
- Legacy completion;
- quest completion;
- Prime restoration/spent-state changes

for duplication or rollback exploits.
