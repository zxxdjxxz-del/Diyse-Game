# Diyse — Combat Engineering Rules

This is the implementation-facing combat baseline aligned with **v1.40 Chapter 0 Rebuild Change Control**, inheriting the compatible v1.39 combat authority. It does not replace the full combat specification.

**Step 7B.5 combat, Standard Card, retarget and Prime gates are COMPLETE / PASS on Android.** These rules are accepted regression behavior. The pre-v1.40 Chapter 0 content merge proved the architecture but its S001-S006 content is superseded; the rebuilt Chapter 0 must be integrated without changing this resolver contract.

## Core round structure

Diyse uses traditional discrete rounds.

At the start of a round:

1. Resolve beginning-of-round effects and immediate battle-state checks.
2. Each conscious enemy locks **one legal action** from the legitimate beginning-of-round state without inspecting any unconfirmed player command.
3. The player selects **one action for every conscious active party member** before the party round is confirmed.
4. Resolve Item actions first, ordered within the Item tier by current effective Speed.
5. Resolve Defend actions second, ordered within the Defend tier by current effective Speed.
6. Resolve all remaining already-locked party and enemy actions from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members use player-selected order.
9. Tied enemies/entities use stable deterministic order.
10. Complete the legal effects/state changes belonging to each selected action, then perform end-of-round processing.

**Speed determines order only. Speed never grants an extra ordinary action.**

## No real-time reaction layer

Diyse does **not** have a universal real-time reaction system.

Do not implement:

- overwatch;
- interrupt commands;
- reaction prompts;
- free intercepts;
- mid-resolution manual repositioning;
- an enemy changing its locked target because it saw the player's unconfirmed command;
- an HP-threshold transformation that grants a bonus attack/turn;
- a reinforcement that appears and immediately receives an ordinary action outside normal round timing.

Animation, dialogue barks, whistles, blocks, wards, movement and cinematic staging may illustrate a legal selected/resolved action, but presentation never creates combat legality by itself.

### Visible intent

When an encounter exposes enemy intent, it exposes information about an **already-locked beginning-of-round action**. The player may use that information while selecting the party's full round.

Visible intent is not a reaction window and the enemy may not inspect the player's commands and switch after confirmation.

### Reinforcement timing

If a reinforcement enters because a round/end-of-round condition is met, it participates in normal enemy action locking at the next beginning of round.

If a legal selected action calls a reinforcement during resolution, the arriving unit may appear as part of that action but receives no ordinary selected action until the following round unless a separately approved universal rule explicitly states otherwise.

## Automatic hostile retargeting

If a queued **player hostile action** targets an enemy that is defeated before that action resolves in the same round, the action is not wasted.

- Retarget to the next living enemy in encounter-slot order after the original target.
- If no later slot is living, wrap to the first living enemy.
- If no enemies remain living, there is no legal target and battle victory should resolve as appropriate.
- This rule applies to Attack, hostile/damaging Abilities, hostile Standard Cards, and equivalent directly controlled Prime hostile commands unless an authored effect explicitly establishes different targeting behavior.
- Retargeting changes only the target; it does not change action identity, cost, priority tier, Speed, or actor.
- The presentation/combat log should expose the retarget so the player can understand what happened.

This accepted player-retarget rule does **not** authorize enemy AI to read player commands or dynamically change its already-locked target.

## Permanent command list

Exactly:

- Attack
- Ability
- Card
- Item
- Defend

Do not add universal Swap, Reserve, Assist, Row, Move, Wait, Timeline, Overwatch, Interrupt, Counter, or personal-resource commands.

## Active party

Maximum four characters can be active in battle under the controlling party-state authority. Reserve members do not participate mid-battle and cannot be swapped in through a universal command.

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
- Prime activation resolves in the ordinary non-Item/non-Defend action tier according to current effective Speed unless a later controlling Prime authority explicitly changes that placement.
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

## Chapter 0 v1.40 encounter-specific locks

The rebuilt Chapter 0 must teach and obey this same resolver:

1. Raider — basic round selection/resolution.
2. Raider + Crossbowman — no free pre-battle Crossbowman shot.
3. Shieldbearer + Raider — no spontaneous guard/intercept reaction unless an already-authorized passive independently provides it.
4. Rift Hound + Raider — high Speed changes order only.
5. Handler + Hound — support synergy consumes separate legal actions; Handler cannot grant an extra Hound action.
6. Ruin Vanguard Pursuer — visible intent is already locked; objective pressure consumes its one action.
7. Riftmaw + two Handlers — Handler support consumes Handler actions; Riftmaw uses one continuous HP bar; Restrained -> Unbound is processed between completed rounds with no refill or bonus action; Cornered changes future action weighting only.

If Riftmaw reaches zero HP before a later locked Riftmaw action resolves, that action is lost under normal defeat rules. There is no last-gasp bonus attack. Surviving Handlers use a legal scripted withdrawal/neutralization encounter exit and receive no revenge action.

## Determinism and testing

Pure round resolution must remain testable without relying on animation timing.

The accepted regression baseline covers Item priority; Defend priority; Speed ordering/ties; enemy action locking; one ordinary selected action per legal unit; automatic hostile player retargeting including wraparound; unlimited Standard Card reuse; Prime bearer locking/use timing; activation-round completion; Prime snapshot/command/duration/return behavior; and frozen party state during replacement.

The v1.40 Chapter 0 replacement must add regression coverage for visible locked intent, reinforcement no-arrival-action timing, Handler support not granting extra actions, and Riftmaw transition/Cornered timing without changing the universal resolver.

Presentation and animation must consume resolver/state results rather than define combat legality. Future production changes must keep these tests green unless a newer approved authority deliberately changes the rule under test.