# Diyse — Runtime Test-Suite Status

**Status:** ACTIVE TEST-SOURCE STATUS / NOT A GREEN RELEASE CERTIFICATE  
**Balance/QA authority:** `../README.md`

## Current source inventory

Current repository inspection finds **36 GDScript validation/test files** under `tests/`.

Coverage includes:
- combat;
- dialogue/authoring/runtime context;
- encounters/field encounter flow;
- equipment service;
- exploration/graybox;
- presentation/HD-2D;
- save/load;
- smoke/integration;
- visual capture/proof utilities.

The source inventory is useful foundation coverage, but not all tests represent current production canon.

## Known legacy proof debt

The current smoke/combat proof still contains legacy First Champion / `first_champion` assumptions, including:
- Cyanis-only bearer access;
- non-bearer rejection;
- old manifestation/duration behavior.

The legacy combat regression explicitly labels itself as proof-only, but the smoke test still asserts these stale Prime expectations.

These tests must be updated before Prime-related CI can be treated as a current-canon gate.

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
