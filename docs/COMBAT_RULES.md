# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline aligned with **Clean Active Master v1.36** and **Active Technical Annex v1.36**. It does not replace the full combat authority.

**Step 7B.5 combat, Standard Card, retarget and Prime gates are COMPLETE / PASS on Android.** The rules below are accepted regression behavior rather than provisional proof targets. Chapter 0 Step 7C production dialogue was merged without changing these combat rules and passed the complete combat regression stack.

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

If a queued player hostile action targets an enemy that is defeated before that action resolves in the same round, the action is not wasted.

- Retarget to the next living enemy in encounter-slot order after the original target.
- If no later slot is living, wrap to the first living enemy.
- If no enemies remain living, there is no legal target and the battle should already resolve victory as appropriate.
- This rule applies to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly establishes different targeting behavior.
- Retargeting changes only the target; it does not change the action, cost, priority tier, Speed, or actor.
- The presentation/combat log should expose the retarget so the player can understand what happened.

This rule was explicitly accepted during 7B.5E and remains current combat authority.

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, or personal-resource commands.

## Active party

Maximum four permanent characters can be active in battle. Reserve members do not participate mid-battle and cannot be swapped in through a universal command.

## Ability economy

- MP is the universal ordinary Ability resource.
- Do not create character-specific combat gauges/resources.
- Content records must remain separable from actor engine code wherever practical.

## Standard Card guardrails

Current collection architecture is 24 Standard Cards + 12 Prime Cards.

- Standard Cards are unlimited-use and have no per-battle charges, Essence, ranks, refresh counters, or use counters.
- Standard Cards never summon or create independent entities.
- Card content must remain data-driven.
- Standard Cards integrate into the ordinary resolver rather than using a separate timing game.

`Proof Strike` was used only to validate the architecture and is not a canonical Standard Card identity.

## Prime Card / Prime Manifestation framework

Current Prime authority controls Prime behavior.

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
- Prime defeat/Banishment is not a normal return and uses current Resonance Backlash rules.
- Prime Manifestations and ordinary summons are separate systems. Never infer ordinary-summon AI or recovery rules from Prime direct control.

### Accepted 7B.5F validation

Recovered First Champion was the representative Prime because it is the current Might story Prime borne by Cyanis. The proof validated bearer locking, activation timing, pending state, party suspension, direct control, Prime-only commands, hostile targeting of the Prime, finite duration, normal return and same-battle use consumption.

Temporary flat damage values used in that proof are not canon. Production Power/Defense/Spirit and authored command effects remain controlled by the active technical authority.

## Determinism and testing

Pure round resolution must remain testable without relying on animation timing.

The accepted regression baseline covers Item priority; Defend priority; Speed ordering/ties; enemy action locking; one ordinary selected action per legal unit; automatic hostile retargeting including wraparound; unlimited Standard Card reuse; Prime bearer locking/use timing; activation-round completion; Prime snapshot/command/duration/return behavior; and frozen party state during replacement.

Presentation and animation should consume resolver/state results rather than define combat legality. Future production changes must keep these tests green unless a newer approved authority deliberately changes the rule under test.