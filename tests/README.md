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

Prioritize deterministic and authority-sensitive behavior, including:
- round resolution, priority tiers and Speed ties;
- enemy action locking and targeting legality;
- state/effect application;
- Standard Card and Prime behavior where testable;
- save/load serialization and world-state restoration;
- dialogue authority/runtime handoff;
- encounter and equipment regressions;
- current-facing naming/visual/presentation contracts.

Presentation may still require manual, screenshot or device validation where automation cannot prove the result, but core legality and simulation should not depend on animation timing.

Tests are evidence that implementation matches the current contract; they are not an independent source of game-design canon. When a stale proof expectation conflicts with current authority, update the implementation/test against the owning `docs/` source rather than preserving the stale behavior merely to keep a test green.

Add regression coverage for defects and authority-drift failures whenever practical.

## Known proof-regression suites

Some tests intentionally lock the behavior of still-unmigrated proof runtime code. They protect engineering continuity; they do **not** certify the tested behavior as current game-design authority.

Important examples:
- `tests/combat/validate_round_combat.gd` — retains the old whole-round queue / priority model and retired `first_champion` Prime proof behavior until combat runtime migration;
- `tests/combat/validate_generated_encounter_battle_state.gd` — exercises proof enemy data, legacy technical `gold` reward keys, and the mixed-authority encounter catalog;
- `tests/encounters/validate_audit98_encounters.gd` — regression-locks the Audit98 executable encounter prototype, including rows/caps that are now superseded or rework-pending in current encounter authority.

Current divergence owner:
`docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

When the corresponding runtime is migrated, migrate these proof tests in the same implementation change instead of using them to preserve retired behavior.
