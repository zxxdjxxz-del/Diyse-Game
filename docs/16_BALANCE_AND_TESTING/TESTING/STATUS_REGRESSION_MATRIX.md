# Diyse — Status Regression Matrix

**Status:** ACTIVE STATUS QA OWNER  
**Authority:** `../../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`

## Shared duration/reapplication

Verify:
- timed duration counts the affected unit's own TURNs;
- hidden reserve TURNs count;
- same-status reapplication refreshes full duration rather than stacking;
- same-TURN duration protection prevents immediate loss of a newly applied/refreshed duration;
- KO clears ordinary temporary statuses/buffs/debuffs under current KO rules.

## Quick

- personal TURN spacing ×0.75;
- 4 affected TURNs;
- no Execution change;
- does not move an already queued EXECUTION;
- mutually exclusive with Slow;
- opposite effect cancels to neutral.

## Slow

- personal TURN spacing ×1.25;
- 4 affected TURNs;
- no Execution change;
- mutually exclusive with Quick.

## Stuck

- 4 affected TURNs;
- commands remain available;
- at queued EXECUTION, 40% trigger chance;
- trigger pushes EXECUTION by 25% of normal personal spacing;
- does not cancel the action;
- Immediate actions are unaffected;
- at most one Stuck push per queued action;
- no Stuck check if the status expired before EXECUTION.

## Asleep

- 3 affected TURNs;
- denies command on affected TURN;
- queued action remains pending if sleep is applied after selection;
- if still Asleep at that EXECUTION, the action fails;
- direct damage wakes after damage;
- passive DoT and healing do not wake by default;
- legal cleanse/wake removes it.

## Poison

- 6% Max HP at each afflicted TURN;
- 5 affected TURNs;
- exact indirect damage;
- ignores Defense/Spirit;
- Ward does not reduce it;
- cannot Crit;
- can KO;
- hidden reserve TURNs process it.

## Wounded

- 4% Max HP when afflicted unit successfully resolves an action;
- canceled action creates no proc;
- +10% physical damage taken;
- self-damage ignores Defense/Spirit/Ward and cannot Crit;
- can KO;
- persists until its healing threshold is reached or another legal clear occurs;
- reapplication does not stack and updates threshold only under the current Wounded rule.

## Sealed

- 3 affected TURNs;
- blocks future selection of native Abilities;
- does not block Attack, Cards, Item, Defend, Swap, or Prime access;
- does not cancel an already queued Ability.

## Ward

- incoming direct physical/magical damage ×0.75;
- 3 affected TURNs;
- refreshes rather than stacks.

## Regen

- 6% Max HP at each affected TURN;
- 5 affected TURNs;
- exact healing;
- hidden reserve TURNs process it;
- contributes toward Wounded healing threshold.

## Doomed

- visible 5-TURN countdown;
- decrements on afflicted TURN;
- reaching 0 KOs;
- Quick/Slow indirectly change real-time frequency by changing TURN spacing.

## Stat Up / Down

For Strength / Magic / Intelligence / Defense / Spirit:
- Up +25%;
- Down −25%;
- 4 affected TURNs;
- same state refreshes;
- opposite cancels to neutral;
- no generic Speed Up/Down.

## Application

`final chance = base chance × susceptibility`

- Vulnerable ×1.5
- Normal ×1.0
- Resistant ×0.5
- Immune ×0
- cap 100%
