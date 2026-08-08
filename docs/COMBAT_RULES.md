# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline for Step 7B.5. It does not replace the full combat authority.

## Core round structure

Diyse uses traditional discrete rounds.

At the start of a round:

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

If a queued party hostile action targets an enemy that is defeated before that action resolves in the same round, the action is not wasted.

- Retarget to the next living enemy in encounter-slot order after the original target.
- If no later slot is living, wrap to the first living enemy.
- If no enemies remain living, there is no legal target and the battle should already resolve victory as appropriate.
- This rule applies to Attack, damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly establishes different targeting behavior.
- Retargeting changes only the target; it does not change the action, cost, priority tier, Speed, or actor.
- The presentation/combat log should expose the retarget so the player can understand what happened.

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands.

## Active party

Maximum four permanent characters can be active in battle.

Reserve members do not participate mid-battle and cannot be swapped in through a universal command.

## Ability economy

- MP is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- The proof may use temporary Ability records, but the engine must not hard-code them into character scripts.

## Standard Card guardrails

Current collection architecture is 24 Standard Cards + 12 Prime Cards.

- Standard Cards are unlimited-use and have no per-battle charges, Essence, ranks, refresh counters, or use counters.
- Standard Cards never summon or create independent entities.
- Card content must remain data-driven.

## Prime Card / Prime Manifestation framework

Current Section 88 authority controls Prime behavior.

- Every collectible Prime Card summons one directly controlled Prime Manifestation.
- A Prime is not a one-shot attack, heal, buff, cinematic-only effect, or ordinary summon.
- Prime activation consumes the holder's ordinary selected Card action and no MP unless an individual rule explicitly says otherwise.
- Prime activation resolves in Tier 3 by effective Speed.
- A successful activation spends that Prime's one use for the ordinary battle or genuine new boss form and establishes Manifestation Pending.
- The already-locked ordinary round finishes before replacement occurs.
- At end of the activation round, the active party and eligible allied temporary entities become Suspended and the Prime enters.
- Only one Prime activation may be selected by the party in a round.
- During each Prime round the player selects exactly one command printed on that Prime's action sheet.
- The Prime receives no substitute universal Attack, Ability, Card, Item, Defend, Escape, counter, or reaction menu.
- Prime Speed orders its one selected command against hostile actions and never grants an extra action.
- Recovered duration is 2 Prime action rounds; Awakened and Concordant duration is 3 unless an approved final command ends the manifestation earlier.
- Suspended permanent characters retain frozen HP, MP, statuses, buffs, debuffs, cooldowns, equipment state, and once-per-battle state. They cannot be targeted and receive no beginning/end-of-round ticks while suspended.
- Allied temporary entities are archived and frozen during Prime replacement and return after normal exit if still legal.
- On normal duration expiry or an approved final command, the Prime exits at end of round and the archived party returns before the next beginning-of-round effects.
- Prime defeat/Banishment is not a normal return and uses the current Resonance Backlash rules.
- Prime Manifestations and ordinary summons are separate systems. Never infer ordinary-summon AI or recovery rules from Prime direct control.

### 7B.5F proof scope

Recovered First Champion is the proof Prime because it is the current Might story Prime borne by Cyanis. The proof exposes its first three current commands: Champion Edge, Shieldbreak Arc, and Stand Between. Current production Power formulas are not yet implemented in the slice, so temporary flat proof damage may stand in for output while command identity, targeting, activation timing, suspension, duration, control and return semantics remain exact.

## Determinism and testing

Pure round resolution should be testable without relying on animation timing.

At minimum, tests should cover:

- Item priority over faster ordinary actions;
- Defend priority after Items;
- Speed ordering within a priority tier;
- exact party-versus-enemy Speed tie;
- tied party player-selected order;
- stable tied-enemy order;
- enemy action locking before player confirmation;
- one ordinary selected action maximum per legal unit per round unless a separately legal effect explicitly changes that outcome;
- queued hostile party actions automatically retargeting from a defeated enemy to the next living enemy, including wraparound;
- Prime bearer locking and one-use spend timing;
- activation-round completion before suspension;
- Prime HP/Speed snapshot at entry;
- one directly selected Prime command per Prime round;
- frozen party state during replacement;
- correct duration and normal return.

Presentation and animation should consume resolver/state results rather than define combat legality.
