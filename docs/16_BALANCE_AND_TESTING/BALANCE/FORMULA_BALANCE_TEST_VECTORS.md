# Diyse — Formula Regression Test Vectors

**Status:** ACTIVE DETERMINISTIC FORMULA REGRESSION VECTORS  
**Battle-math authority:** `../../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`

These vectors test correctness rather than establish new balance targets.

Use variance multiplier **1.00** for deterministic checks.

## Direct physical

Formula:

`Damage = Potency × Strength × (K / (K + Defense))`

With Potency 1.00, Strength 100, Defense 100, K 300:

> **75**

## Magical

With Potency 1.00, Magic 80, Spirit 80, K 300:

> **63.157894...** before final rounding.

## Card output source

A scalable Standard Card uses Intelligence as its source stat. Damage type still determines the target defensive stat.

Example: Potency 1.00, Intelligence 120, physical output vs Defense 60, K 300:

> **100**

## Element

Apply current affinity after the defense curve.

Weak ×1.5:
- 75 base becomes **112.5** before later modifiers/rounding.

Resist ×0.5:
- 75 base becomes **37.5**.

Null:
- **0**.

## Defend / Ward

On 100 direct damage:
- Ward only: **75**
- Defend only: **60**
- Ward + Defend: **45**

## Crit

Eligible critical:
- base chance **5%**
- damage multiplier **×1.5**

Crit does not bypass Defense/Spirit.

## Hit boundary

A legal valid action hits by default.

Explicit authored Miss/Evade effects are tested only through their owning effect.

## Status application

`final chance = base chance × target susceptibility`

Examples:
- base 40%, Normal ×1.0 → **40%**
- base 40%, Resistant ×0.5 → **20%**
- base 40%, Vulnerable ×1.5 → **60%**
- Immune ×0 → **0%**

Final chance caps at 100%.
