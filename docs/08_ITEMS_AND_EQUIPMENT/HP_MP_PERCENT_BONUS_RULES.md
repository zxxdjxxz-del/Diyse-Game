# Diyse — Equipment Max HP / Max MP Bonus Rules

**Current authority:** newer explicit equipment-stat correction.

## Core rule

Equipment bonuses to **Max HP** and **Max MP** are persistent **percentage modifiers**, not flat raw additions.

Production-facing equipment wording must use:
- `Max HP +N%`
- `Max MP +N%`

Do not author ordinary equipment as flat `Max HP +N` or `Max MP +N` unless a later explicit exception deliberately reopens flat equipment HP/MP scaling.

## Construction order

For an ordinary player body:
1. calculate the neutral natural HP/MP for Player Level;
2. apply the selected-class HP/MP multiplier;
3. round the resulting selected-class natural value to a whole number;
4. sum all legal equipped Max HP percentage bonuses and Max MP percentage bonuses separately;
5. apply the equipment-derived cap of **+30% Max HP** and **+30% Max MP** separately;
6. calculate each equipment bonus from the rounded selected-class natural Max HP / Max MP;
7. round the resulting equipment bonus to a whole number, with exact .5 rounding up;
8. add that rounded equipment bonus to the rounded selected-class natural value.

Equipment Max HP / Max MP percentages therefore scale with Player Level and selected-class identity, but they do **not** multiply one another.

## Stacking

Legal equipment Max HP / Max MP percentages stack **additively**, not multiplicatively.

Examples:
- Max HP +10% and Max HP +12% = **Max HP +22%**;
- Max MP +15% and Max MP +15% = **Max MP +30%**;
- bonuses that would exceed +30% are capped at **+30%** for that resource.

The +30% Max HP cap and +30% Max MP cap are separate.

This is an **equipment-derived persistent-resource cap**, not the temporary core-stat ±40% cap in `../05_BATTLE_SYSTEM/STAT_CHANGES.md`.

## Current Legacy values

| Legacy | Current bonus |
|---|---:|
| **That Didn't Do Shit.** | **Max HP +15%** |
| **Try Me Instead.** | **Max HP +10%** |
| **No. Stay Here.** | **Max MP +15%** |
| **Get Behind Me.** | **Max HP +12%** |
| **That Saves Me the Trouble.** | **Max MP +15%** |
| **You Should Have Killed Me.** | **Max HP +18%** |

These are strengthened late-game Legacy capstones. Their percentage scaling is intentional so they remain meaningful as natural HP/MP grows toward Level 70.

## Equip / unequip current-resource behavior

Changing equipment does not heal or restore MP for free.

When Max HP or Max MP changes because equipment changes:
- preserve the current absolute HP / MP value if it is still legal under the new maximum;
- if the new maximum falls below the current value, clamp current HP / MP down to the new maximum;
- increasing the maximum does not fill the newly created capacity.

## Boundary

This rule changes **equipment Max HP / Max MP bonuses only**.

It does not convert:
- healing based on a percentage of Max HP;
- MP restoration based on a percentage of Max MP;
- damage based on Max HP;
- selected-class HP/MP multipliers;
- temporary Attack / Magic / Defense / Spirit / Speed percentage changes;
- encounter or Prime HP formulas.
