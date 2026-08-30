# Diyse — Enemy Action Selection Default

**Status:** ACTIVE FALLBACK AUTHORITY — v90

This rule closes the reorganization-era ambiguity where an enemy's current action sheet is complete but historical per-action selection weights were not migrated into the owning file.

## Default
If an enemy, Elite, boss, Hunt, support actor, or authored encounter has **no explicit current selection weights** for its eligible selected actions:

1. Resolve forced actions, phase rules, preparations/resolutions, scripted threshold behavior, cooldowns/repetition locks, and action-specific eligibility first.
2. Build the set of selected actions that are currently legal.
3. If exactly one action is legal, use it.
4. If two or more actions are legal and no current explicit weights apply, select **uniformly at random** among the legal actions.

## Override rule
Any explicit per-action, per-phase, per-state, or conditional weights in an owning current file override this fallback. A later recovered exact approved weight table may replace this fallback for that identity without reopening its Power audit.

## Boundaries
- This does not add actions.
- This does not erase eligibility conditions or repetition locks.
- This does not turn automatic/threshold effects into selected actions.
- This does not grant extra turns.
- This does not change Power, Base Hit, statuses, stats, targeting, or phase architecture.
- It exists only so every current enemy sheet has deterministic production behavior even when old percentage weights were not migrated.
