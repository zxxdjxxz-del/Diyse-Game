# Diyse — Combat UI
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Permanent commands
Exactly:
> **Attack / Ability / Card / Item / Defend**

## Round-selection requirement
During a normal party round:
1. player selects one action for each conscious active party member;
2. selections remain queued until confirmation;
3. the round resolves only after all required actions are selected and confirmed.

The UI must make it clear that selecting a command:
> queues an action

rather than immediately resolving it.

## Priority / order
Resolution rules live in `05_BATTLE_SYSTEM`:
- Item priority first by Speed;
- Defend second by Speed;
- remaining actions by Speed;
- party wins exact Speed tie against enemies;
- party-party ties use player selection order;
- enemy-enemy ties use deterministic order.

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
- Defend/Guard state where relevant.

## Enemy display
Must support:
- multiple enemies up to current simultaneous cap **8**;
- targetability;
- KO/dead removal state;
- named boss/form identity;
- one vs fresh multi-form HP behavior;
- support targets when authored.

## Targeting
Player selects a legal target at command entry.

If a queued hostile target dies before the action:
- runtime retargets by current automatic slot-order rule;
- action/cost/priority/actor remain unchanged.

The UI should not ask for a second target confirmation during resolution.

## No obsolete meters
Do not display:
- Barrier bar;
- Brace;
- Break/Stagger gauge;
- natural Accuracy gauge;
- character-specific resource gauges not currently canon.
