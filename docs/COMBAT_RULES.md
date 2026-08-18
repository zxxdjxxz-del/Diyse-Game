# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline under **Diyse Clean Active Complete Master Canon v1.64 / Audit79**. Accepted Step 7B.5 combat behavior remains a technical regression baseline only where compatible with the current master. Older v1.36/technical-proof numbers, Card counts, Prime names, durations, HP rules, and boss-form refresh assumptions do not override v1.64.

## Core round structure

Diyse uses traditional discrete rounds.

Accepted compatible resolver behavior:

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. Each enemy locks one legal action from the legitimate beginning-of-round state without inspecting unconfirmed player commands.
3. The player selects one action for every conscious active party member before the round is confirmed.
4. Resolve Item actions first, ordered by current effective Speed.
5. Resolve Defend actions second, ordered by current effective Speed.
6. Resolve all remaining party and enemy actions from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members use player-selected order.
9. Tied enemies/entities use stable deterministic order.
10. Resolve complete action/reaction/state-change packages, then end-of-round processing according to the controlling combat specification.

Speed determines order only. Speed never grants extra ordinary actions.

## Automatic hostile retargeting

If a queued player hostile action targets an enemy that is defeated before that action resolves in the same round, the action is not wasted.

- Retarget to the next living enemy in encounter-slot order after the original target.
- If no later slot is living, wrap to the first living enemy.
- If no enemies remain living, there is no legal target and battle resolution proceeds as appropriate.
- This rule applies to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly establishes different targeting behavior.
- Retargeting changes only the target; it does not change the action, cost, priority tier, Speed, or actor.
- Presentation/combat logging should expose the retarget clearly enough for the player to understand it.

This behavior was accepted during Step 7B.5E and remains compatible current combat architecture.

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands without explicit later change control.

## Active party

Maximum four active permanent characters. Reserve members are inert while reserved and do not participate through a normal universal mid-battle swap command.

Temporary/guest party participation is authored separately and never expands the permanent roster beyond six.

## Ability economy

- MP is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- Content records remain separable from actor engine code wherever practical.
- Focus is selected outside battle and remains fixed for that battle.

## Standard Card guardrails

Current collection architecture is **30 Standard Cards + 12 Prime Cards = 42 total Cards**.

- Standard Cards are unlimited-use.
- They are not a deck/hand/draw/discard/charge/rank/duplicate/Essence/refresh-counter system.
- Standard Cards do not summon independent beings. Prime Cards are the collectible manifestation system.
- Each permanent character unlocks exactly four Standard Card slots at Base CL1, CL4, CL8, and CL12.
- Card content remains data-driven.
- Standard Cards integrate into the ordinary resolver rather than using a separate timing game.
- Cards are Ancient Diysean artifacts; modern bosses do not create them. A victory/access state may expose or release a pre-existing Card.

`Proof Strike` remains a non-canon technical fixture and is not part of the 30 Standard Cards.

## Prime Card / Prime Manifestation framework

Current Story Primes are:

- Might — **Last Sentinel**
- Resource — **Last Measure**
- Elements — **Last Convergence**
- Change — **Last Scribe**
- Grace — **Last Sanctuary**
- Ruin — **Last Erasure**

There are 12 Prime Cards total: six Story Primes plus six optional-major Primes.

### Slots and ownership

- Each permanent character has two dedicated Prime slots.
- Prime Slot 1 unlocks in Chapter 3 when the first usable Prime exists.
- Prime Slot 2 unlocks party-wide at the Sixfold Accord.
- Gameplay equipment is flexible among permanent characters for all 12 Prime Cards. Story associations govern narrative acquisition, characterization, and Awakening; they are not exclusive gameplay ownership locks.
- Prime progression state belongs to the Prime identity, not separately to each wearer.

### Current Prime states

**Recovered**
- One strong Prime action resolves and the Prime is dismissed in the same ordinary round.
- Old proof rules that gave Recovered a two-round manifestation are superseded.

**Awakened**
- Exactly 3 Prime action rounds.
- Manifestation HP = **40% of the combined current HP of the active party at manifestation**.

**Concordant**
- Manifestation HP = **50% of the combined current HP of the active party at manifestation**.
- No fixed timer; remains until 0 HP under the current core unless a later approved open-rule resolution defines a legal voluntary exit or final-command path.

### Current common Prime boundaries

- Prime activation uses the Card action.
- Genuine new boss forms do **not** refresh Prime use availability.
- Prime manifestations remain once-per-battle under the current core.
- **Exact once-per-battle scope is OPEN:** per Prime identity versus one party-total manifestation. Do not choose one by reviving an obsolete technical sheet.
- Concordant voluntary dismissal, Concordant Art, Return Effects, defeat backlash, and redesigned exact Prime action sheets remain OPEN/DEFERRED under v1.64.
- Old 70%/80%/90% Prime HP rules are superseded.
- Old `First Champion` naming is superseded; Cyanis's Story Prime is Last Sentinel.

### Direct-control architecture

Step 7B.5F proved the direct-control replacement/suspension architecture. Preserve the compatible architectural behavior for Prime states that occupy dedicated Prime rounds:

- successful use is bearer/equipment legal and consumes the selected Card action;
- already-locked ordinary actions are not retroactively erased by the activation;
- party state can be suspended/frozen while a multi-round Prime is directly controlled;
- the Prime uses its authored Prime action sheet rather than a substitute universal Attack/Ability/Card/Item/Defend menu;
- one selected Prime command resolves per Prime round, ordered by Prime Speed against hostile actions;
- frozen party state does not tick or become targetable while suspended;
- normal return restores the archived party state according to current authored rules.

Do **not** import the historical proof's exact First Champion commands, old two-round Recovered duration, old HP values, or boss-form refresh behavior. Recovered now follows its v1.64 single-action rule rather than the obsolete proof fixture.

### Story/knowledge boundary

S021 identifies and unlocks Last Sentinel without manifestation. The first actual later battle activation of Last Sentinel is the first verified modern Prime manifestation/sighting in story canon. Gameplay UI may teach legal mechanics after unlock without retroactively granting characters in-world empirical knowledge they have not earned.

## Prepared effects and universal Attack

- Attack comes from the currently equipped Weapon. A Conduit Attack is equipment functionality, not a class Ability.
- Abilities do not automatically inherit the equipped weapon's ordinary Attack hit pattern unless an Ability explicitly says so.
- The one-armed Prepared-effect limit across Abilities and Standard Cards remains active.
- Presentation cannot invent illegal combat actions merely because a cinematic would look dramatic.

## Determinism and testing

Pure round resolution must remain testable without relying on animation timing.

The accepted regression baseline covers Item priority; Defend priority; Speed ordering/ties; enemy action locking; one ordinary selected action per legal unit; automatic hostile retargeting including wraparound; unlimited Standard Card reuse; Prime equipment/use legality; direct-control state handling where applicable; and frozen party behavior during multi-round replacement.

Tests encoding superseded Prime/Card facts must be updated deliberately rather than treated as authority merely because they once passed.

Presentation and animation should consume resolver/state results rather than define combat legality. Future production changes must keep compatible tests green unless a newer approved authority deliberately changes the rule under test.
