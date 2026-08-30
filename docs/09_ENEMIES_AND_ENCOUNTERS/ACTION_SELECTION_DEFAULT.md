# Diyse — Enemy Action Selection Default

**Status:** ACTIVE FALLBACK AUTHORITY — v90 plus newer turn-entry battle-flow correction

This rule closes the reorganization-era ambiguity where an enemy's current action sheet is complete but historical per-action selection weights were not migrated into the owning file.

## When selection occurs
Under the current turn-entry round model, ordinary enemy action selection occurs when that enemy/entity's **normal Speed-ordered turn arrives**.

The AI evaluates the legitimate battle state that exists at that turn. It does not lock an ordinary action at beginning-of-round and may not inspect future player choices that have not yet been made.

Explicit forced actions, Preparation follow-ups, threshold scripts, or other authored delayed-action rules may constrain what is legal on that turn without restoring the retired universal enemy-action queue.

## Default
If an enemy, Elite, boss, Hunt, support actor, or authored encounter has **no explicit current selection weights** for its eligible selected actions:

1. Resolve forced actions, phase rules, preparations/resolutions, scripted threshold behavior, cooldowns/repetition locks, and action-specific eligibility first.
2. Build the set of selected actions that are currently legal.
3. If exactly one action is legal, use it.
4. If two or more actions are legal and no current explicit weights apply, select **uniformly at random** among the legal actions.

## Prepared follow-ups
If an owning current action says a Preparation locks a named follow-up as the actor's next selected action:
- that Preparation spends its own turn when used;
- the follow-up remains pending between turns;
- on the actor's next eligible normal turn, the locked follow-up is the required selected action if its owning conditions still permit it;
- this is an authored delayed-action mechanic, not the retired beginning-of-round action lock.

Interrupt eligibility is never inferred solely from Preparation. A pending action must be explicitly marked **Interruptible** by its owning current rule before an interrupt mechanic may affect it.

## Override rule
Any explicit per-action, per-phase, per-state, or conditional weights in an owning current file override this fallback. A later recovered exact approved weight table may replace this fallback for that identity without reopening its Power audit.

## Boundaries
- This does not add actions.
- This does not erase eligibility conditions or repetition locks.
- This does not turn automatic/threshold effects into selected actions.
- This does not grant extra turns.
- This does not change Power, Base Hit, statuses, stats, targeting, or phase architecture.
- It exists only so every current enemy sheet has deterministic production behavior even when old percentage weights were not migrated.
