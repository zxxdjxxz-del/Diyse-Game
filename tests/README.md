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
