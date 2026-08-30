# Diyse — Equipment Max HP / Max MP Bonus Rules

**Current authority:** newer explicit equipment-stat correction.

## Core rule

Equipment bonuses to **Max HP** and **Max MP** are persistent **flat raw additions**, not percentage modifiers.

Production-facing equipment wording must use:
- `Max HP +N`
- `Max MP +N`

Do not author ordinary equipment as `Max HP +N%` or `Max MP +N%` unless a later explicit exception deliberately reopens percentage-based equipment HP/MP scaling.

## Construction order

For an ordinary player body:
1. calculate the neutral natural HP/MP for Player Level;
2. apply the selected-class HP/MP multiplier;
3. round the selected-class natural value to a whole number;
4. add all equipped flat Max HP / Max MP bonuses.

Equipment HP/MP bonuses therefore behave like other persistent raw equipment stats and do **not** use `05_BATTLE_SYSTEM/STAT_CHANGES.md`.

## Stacking

Legal flat equipment Max HP / Max MP bonuses stack additively across equipped items.

There is no temporary-stat ±40% cap on these persistent equipment additions.

## Current Legacy conversions

The former percentage-based Legacy capstones are retired and replaced by these flat values:

| Legacy | Retired wording | Current flat bonus |
|---|---:|---:|
| **That Didn't Do Shit.** | Max HP +12% | **Max HP +400** |
| **Try Me Instead.** | Max HP +8% | **Max HP +250** |
| **No. Stay Here.** | Max MP +12% | **Max MP +40** |
| **Get Behind Me.** | Max HP +10% | **Max HP +325** |
| **That Saves Me the Trouble.** | Max MP +12% | **Max MP +45** |
| **You Should Have Killed Me.** | Max HP +15% | **Max HP +600** |

These values preserve approximately the intended late-game strength of the retired percentages while preventing the equipment contribution from continuing to scale upward with Player Level or selected-class HP/MP multipliers.

## Boundary

This rule changes **equipment Max HP / Max MP bonuses only**.

It does not convert:
- healing based on a percentage of Max HP;
- MP restoration based on a percentage of Max MP;
- damage based on Max HP;
- selected-class HP/MP multipliers;
- temporary Attack / Magic / Defense / Spirit / Speed percentage changes;
- encounter or Prime HP formulas.
