# Diyse — Enemy Action Selection Default

**Status:** ACTIVE CURRENT FALLBACK AUTHORITY

## When selection occurs

An enemy chooses its legal selected action when that enemy's **TURN** arrives.

The AI evaluates the legitimate battlefield state that exists at that TURN.

A queued enemy action may then EXECUTE later according to its Execution category.

## Default selection

If an enemy/boss/Hunt/support actor has no explicit current selection weights:

1. resolve forced-action, phase, setup, cooldown, repetition-lock, and eligibility rules;
2. build the currently legal selected-action set;
3. if exactly one action is legal, choose it;
4. if multiple actions are legal and no explicit weights apply, select uniformly among them.

## Queued/setup follow-ups

An authored action may establish a required later follow-up.

That follow-up must use current TURN / EXECUTION language and may be Delayed or Interrupted only according to its explicit current classification.

## Override rule

Explicit per-action, phase, state, or conditional weighting in an owning current file overrides this fallback.

This default does not add actions, grant extra TURNs, alter targeting, or change an action's Potency/status/timing package.
