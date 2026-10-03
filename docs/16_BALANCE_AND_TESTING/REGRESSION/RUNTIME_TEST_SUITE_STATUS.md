# Diyse — Runtime Test-Suite Status

**Status:** ACTIVE TEST-SOURCE STATUS / NOT A GREEN RELEASE CERTIFICATE  
**Balance/QA authority:** `../README.md`

## Current source inventory

Current repository inspection finds **36 executable validation/test files** under `tests/`:
- **33 GDScript** validations/capture utilities;
- **3 Python** Dialogue Engine contract/compiler tests.

Coverage includes:
- combat;
- dialogue/authoring/runtime context, including Python authority/Person-Agent contracts;
- encounters/field encounter flow;
- equipment service;
- exploration/graybox;
- presentation/HD-2D;
- save/load;
- smoke/integration;
- visual capture/proof utilities.

The source inventory is useful foundation coverage, but not all tests represent current production canon.

## Known legacy proof debt

The executable combat proof still contains legacy First Champion / `first_champion` assumptions, including bearer-locked and outdated manifestation behavior.

The obsolete mechanics regression that hard-locked those assumptions has been removed from the live tree. The current integrated smoke test deliberately checks only:
- combat scene loadability;
- four-member active-party surface;
- at least one enemy;
- the five current global commands.

It does **not** certify Prime ownership, timing, cooldown, restoration, Card costs, or the retired whole-round queue.

Prime-specific CI therefore remains incomplete, but the current smoke test is no longer itself asserting the stale Prime mechanics.

## Current interpretation

Preserve useful foundations for:
- deterministic combat behavior;
- targeting/retarget;
- encounter handoff;
- dialogue continuity/runtime wiring;
- save/load;
- Kessara copy service;
- HD-2D presentation.

Do not treat:
- placeholder content fixtures;
- retired Prime identifiers;
- proof-only UI/content assumptions;
- old migration-era assertions

as production balance truth.

## Execution boundary

Repository inspection alone does not prove the full Godot test suite is currently green. A release gate requires an actual current runtime/CI execution against the production branch.
