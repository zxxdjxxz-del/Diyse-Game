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

## Current Prime proof mismatch

The executable combat proof still contains `first_champion` assumptions, including bearer locking and manifestation behavior that do not match current Prime authority.

The integrated smoke test currently checks only:
- combat scene loadability;
- four-member active-party surface;
- at least one enemy;
- the five current global commands.

It does **not** certify Prime ownership, timing, cooldown, restoration, Card costs, or the current actor-by-actor round contract.

Prime-specific CI therefore remains incomplete.

## Current interpretation

Preserve useful foundations for:
- deterministic combat behavior;
- targeting/retarget;
- encounter handoff;
- dialogue continuity/runtime wiring;
- save/load;
- Kessara copy service;
- HD-2D presentation.

Do not treat placeholder content fixtures or proof-only UI/content assumptions as production balance truth.

## Execution boundary

Repository inspection alone does not prove the full Godot test suite is currently green. A release gate requires an actual current runtime/CI execution against the production branch.
