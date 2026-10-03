# Diyse — Combat UI

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Permanent commands
Exactly:
> **Attack / Ability / Card / Item / Defend**

## Turn-entry command requirement
Diyse remains round-based, but normal party actions are not selected as a whole-party batch.

During a normal round:
1. Speed/tie rules establish the normal turn order at round start;
2. when a player-controlled character's turn arrives, the UI opens that character's legal command selection;
3. the player chooses the action and target/content for that character using the current battle state;
4. the action resolves before the next normal combatant's turn begins.

There is no universal whole-party action queue and no production **Confirm Round** step.

The UI must make it clear which character is currently acting and which command/target is being confirmed for that turn.

## Order
Resolution rules live in `05_BATTLE_SYSTEM`:
- normal turn order is highest current effective Speed to lowest as established at round start;
- **Item** and **Defend** resolve on the actor's normal turn and have no separate universal priority phase;
- party wins exact Speed ties against enemies;
- party-party ties use the established player-selected tie order;
- enemy-enemy ties use deterministic order;
- once beginning-of-round setup locks initiative, mid-round Speed changes do **not** reshuffle that round; if still active, they affect the next round's Speed-derived order.

Do not create:
- ATB bar;
- free extra actions from Speed;
- initiative resource;
- Break turn bonus.

## Party display
Must support up to:
> **4 active permanent party members**

Reserve characters are not in the normal battle frame.

Display must be able to communicate:
- HP;
- MP;
- current harmful statuses;
- current temporary buffs/debuffs where relevant;
- conscious/KO state;
- Defend/Guard state where relevant;
- current acting character clearly enough for turn-entry command selection.

## Enemy display
Must support:
- multiple enemies up to current simultaneous cap **8**;
- targetability;
- KO/dead removal state;
- named boss/form identity;
- one vs fresh multi-form HP behavior;
- support targets when authored.

## Targeting
Player selects a legal target when the acting character chooses the command.

Because later party characters do not pre-queue targets, an enemy defeated earlier in the round is simply unavailable to those later characters.

If an already-selected hostile target becomes invalid between selection and final resolution because of an explicit interrupt/reaction or authored multi-step package, runtime uses the current automatic slot-order retarget rule without asking for a second target confirmation.

## No obsolete meters
Do not display:
- Barrier bar;
- Brace;
- Break/Stagger gauge;
- natural Accuracy gauge;
- character-specific resource gauges not currently canon.
