# Diyse — Random Encounter Presentation Lock

**Status:** CURRENT EXPLICIT USER DIRECTION  
**Domain:** dialogue / scene scripting / gameplay presentation

## Hard rule

> **Ordinary enemies are random encounters. Dialogue and scene scripts must not silently convert them into authored on-map fights, mandatory combat set pieces, fixed ambushes, room-clear gates, or scripted enemy activations.**

This applies to ordinary Black Host troops, wildlife, constructs, and other non-boss enemy groups unless a separate explicit authority identifies a specific encounter as a scripted exception.

## Scene-authoring consequences

- Hostile areas may state that random encounters are active and identify the encounter pool or escalation band.
- Story progression must not require the player to have triggered a particular ordinary random encounter unless that requirement is explicitly authorized elsewhere.
- Dialogue may not assume an exact ordinary enemy composition, exact count, or exact battle result.
- Do not write `Combat begins` for ordinary enemies.
- Do not build mandatory `after this fight` story stops around ordinary enemies.
- Optional post-random-encounter dialogue may exist only **after combat has fully ended** and must not be required for story progression.
- No spoken dialogue occurs during an active random encounter.
- Bosses remain authored encounters. A chapter boss or other explicitly designated boss is not converted into a random encounter by this rule.

## HD-2D interaction

Random encounters support the reductive production target: ordinary enemy pressure belongs to the encounter system rather than requiring extra on-map enemy staging, bespoke approach animation, or unique combat rooms.

## Chapter 1 correction

For the current Chapter 1 rehearsal-first rebuild, Hollow Watch, its excavation, and its inner ruin use random encounters for ordinary Black Host troops and Diysean defenses. The Hollow Watch Castellan remains an authored boss encounter. Any earlier Beat 1–8 wording that implies mandatory ordinary combat, fixed Sentry activation, or a required room-clear fight must be rewritten as random-encounter gameplay or removed.
