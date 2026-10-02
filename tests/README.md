# Tests

This directory contains the repository's automated and regression validation.

Current test areas include:
- `combat/`;
- `dialogue/`;
- `encounters/`;
- `equipment/`;
- `exploration/`;
- `presentation/`;
- `save/`;
- `smoke/`;
- `visual/`.

## Validation principles

Prioritize deterministic, authority-sensitive behavior that the current runtime can actually prove, including:
- executable combat/encounter handoff and current-safe combat surfaces;
- encounter selector, pressure-state and profile-schema legality;
- save/load serialization and world-state restoration;
- dialogue authority/runtime handoff;
- equipment-service regressions;
- current-facing naming, visual and presentation contracts.

Presentation may still require manual, screenshot or device validation where automation cannot prove the result, but core legality and simulation should not depend on animation timing.

Tests are evidence that implementation matches the current contract; they are not an independent source of game-design canon. When a stale proof expectation conflicts with current authority, update the implementation/test against the owning `docs/` source rather than preserving stale behavior merely to keep a test green.

Add regression coverage for defects and authority-drift failures whenever practical.

## Proof-runtime boundary

Some current tests intentionally exercise still-unmigrated proof runtime code. They protect engineering continuity; they do **not** certify that proof data or behavior as current game-design authority.

Important examples:
- `tests/combat/validate_generated_encounter_battle_state.gd` proves that the executable encounter catalog can instantiate and resolve through the generated-battle path. It may touch proof enemy data and legacy technical reward keys; it does not certify current chapter formations, final rewards, production turn flow, Prime behavior or Card costs.
- `tests/encounters/validate_encounter_runtime_contract.gd` checks content-neutral encounter-runtime invariants such as profile schema, weighted-pool integrity, pressure-state behavior and selector legality. It deliberately does not freeze superseded encounter counts, formations or progression totals.
- `tests/smoke/validate_project.gd` checks integrated project loadability and current-safe surface contracts; it is not a certification of unresolved combat internals.

The obsolete `validate_round_combat.gd` mechanics regression and `validate_audit98_encounters.gd` audit-era encounter regression were retired from the live tree. Git history preserves them as implementation provenance.

Current divergence owner:
`docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`
