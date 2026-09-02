# Tests

The repository contains both **proof-runtime regressions** and tests that will become/are production-facing validation. Passing an old proof regression does not make the behavior it exercises current canon.

Current implementation authority is routed through:
- `docs/00_MASTER_CONTROL/CURRENT_CANON_STATUS.md`
- the owning numbered domain
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_AUTHORITY_PRECEDENCE.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`
- `docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/PRODUCTION_RUNTIME_MIGRATION_SEQUENCE.md`

## Legacy proof regressions

Some tests intentionally preserve architecture that is now known to be superseded so the existing proof remains reproducible until its coordinated replacement.

Important examples:
- `combat/validate_round_combat.gd` currently asserts whole-party command queue/Confirm-Round behavior, enemy action locking, Item/Defend priority, bearer-locked `first_champion`, and the old two-round Recovered Prime proof. These assertions are **proof behavior, not current production battle authority**.
- `smoke/validate_project.gd` currently checks the same proof combat surface, including bearer lock and the Confirm Round control.

Do not edit those assertions one at a time merely to make source text look current. Replace them alongside the runtime systems they exercise, with current-authority coverage in the same migration pass.

## Current regression principles

For production-facing systems:
- test deterministic legality/state transitions rather than animation timing;
- test current terminology at the UI/data boundary;
- preserve stable-ID/save migration coverage where legacy values remain readable;
- do not weaken tests simply because stale runtime behavior conflicts with canon;
- when a proof subsystem is replaced, retire/replace its stale tests rather than leaving contradictory requirements in CI.

The Kessara Relic-copy test now follows this migration pattern for Face terminology: current Perception/Memory values are written/tested, while Resource/Acuity/Change are retained only as compatibility inputs that normalize to current values.

Presentation tests may still require screenshot/device validation, but core legality and simulation should remain testable without visual timing.
