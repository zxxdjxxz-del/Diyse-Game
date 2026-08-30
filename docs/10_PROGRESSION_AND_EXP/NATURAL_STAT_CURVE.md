# Diyse — Natural Stat Curve

**Status:** **RECOVERED / ACTIVE FOR BALANCE VALIDATION**  
**Scope:** Player Levels 1–70 before selected-class multipliers and equipment.

This file restores the neutral natural-stat formula required to reproduce player bodies during encounter validation.

Let:
> **x = Player Level − 1**

Neutral natural stats:
- **HP = 220 + 34x + 0.28x²**
- **MP = 28 + 3.25x + 0.018x²**
- **Attack = 18 + 2.05x + 0.008x²**
- **Magic = 18 + 2.05x + 0.008x²**
- **Defense = 16 + 1.70x + 0.006x²**
- **Spirit = 16 + 1.70x + 0.006x²**
- **Speed = 22 + 0.52x**

## Resolution order
1. Calculate the neutral natural stat for the character's Player Level.
2. Apply the currently selected class stat multiplier.
3. Round the resulting selected-class natural stat to a whole number.
4. Add equipment bonuses afterward.

Prime bodies remain separate and do not use this ordinary player-body construction.

## Chapter 0 anchor
Chapter 0 is Player-Level static, so Cyanis and Ilyra use the Level-1 neutral body when they are active there:
- HP 220
- MP 28
- Attack 18
- Magic 18
- Defense 16
- Spirit 16
- Speed 22

Selected-class multipliers and equipment then produce the actual combat body.

## Balance-validation use
Mandatory-vs-completionist validation must use this natural-stat curve together with:
- `06_CLASSES_AND_ABILITIES/SELECTED_CLASS_STAT_PACKAGES.md`
- current owning equipment files;
- current Player-Level route assumptions;
- current Class-Level / Ability access.

Do not substitute an obsolete pre-Lv70 natural-stat table.
