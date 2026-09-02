# Combat Tests

The combat test folder currently contains a mixture of proof-runtime regression coverage and behavior that will need replacement during the production battle migration.

## `validate_round_combat.gd`

**Classification:** LEGACY PROOF REGRESSION — NOT CURRENT BATTLE AUTHORITY.

It intentionally verifies the existing proof architecture, including behavior now superseded by current canon:
- whole-party action selection before resolution;
- enemy actions locked before future player choices;
- universal Confirm Round;
- Item/Defend priority tiers;
- bearer-locked `first_champion`;
- old two-round Recovered Prime direct-control behavior.

Do not cite those assertions as production requirements.

When the production battle/Prime core is migrated, replace these stale assertions with tests for `docs/05_BATTLE_SYSTEM/TURN_AND_ROUND_RULES.md`, `docs/05_BATTLE_SYSTEM/PRIME_ROUND_SEQUENCING.md`, and `docs/07_CARDS/PRIME_CARDS/PRIME_SYSTEM_RULES.md` in the same coordinated change.

## `validate_generated_encounter_battle_state.gd`

This test also inherits the base proof battle state. Formation handoff/enemy-cap/reward-contract checks may remain useful, but any assertion that depends on the old queued-round/Prime proof must be reassessed when the base battle state changes.

## Migration plan

Follow:
`docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/PRODUCTION_RUNTIME_MIGRATION_SEQUENCE.md`

Tests must move with runtime behavior. Do not make a stale test pass by weakening current domain rules, and do not delete regression coverage without a current-authority replacement.
