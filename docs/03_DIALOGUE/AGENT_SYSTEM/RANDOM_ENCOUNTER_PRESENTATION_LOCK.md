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

Current Chapter 1 placement is:

- Hollow Watch **approach / surface** uses random encounters for ordinary Black Host troops;
- after the party enters the Diysean excavation corridor, ordinary random encounters are **Construct-only**;
- the **Shield Construct** is a fixed authored stronger encounter, outside the random pool, but it is **not a miniboss** and receives no boss-style framing;
- **Watch Castellan is retired** from the current Chapter 1 structure and must not be restored;
- the removed Six-Channel / surviving-channel / protected-inner structure is not current.

Any earlier wording that implies mandatory ordinary combat, fixed ordinary-Sentry activation, a required room-clear fight, underground Black Host randoms, or a Castellan encounter must be rewritten to the current structure or removed.
