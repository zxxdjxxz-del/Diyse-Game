# Diyse — Formula Regression Test Vectors

**Status:** ACTIVE DETERMINISTIC FORMULA REGRESSION VECTORS  
**Battle-math authority:** `../../05_BATTLE_SYSTEM/`

These are deterministic correctness vectors, not new balance targets.

## Direct physical
Formula:
`ATK² / (ATK + EffectiveDEF) × Power/100`

Example:
- ATK 100
- DEF 100
- Power 100
- no penetration

Expected pre-final-rounding:
> **50**

With 50% Defense penetration:
- EffectiveDEF 50
- expected:
> **66.666...**

Penetration above 75% must clamp to 75%.

## Magical
MAG 80 / Spirit 80 / Power100:
> **40**

## Hybrid
Resolve each component independently.
Do not average ATK/MAG or DEF/Spirit.

## Hit
Case A:
- Base Hit100
- no modifiers
- EVA0
→ **100%**

Case B:
- Base Hit90
- EVA30
→ **60%**

Case C:
- Base Hit120
- EVA0
→ clamp **100%**

Case D:
- Base Hit0
- EVA30
→ ordinary clamp **5%**

## Crit
- base 5%
- eligible damage ×1.5
- ordinary chance cap50%
- miss means no Crit roll
- Crit does not bypass defenses.

## Status chance
Base20 / no affinity / SR10:
> **10%**

Base10 / resist−10 / SR15:
raw −15 → ordinary clamp:
> **5%**

Explicit immunity:
> **0**, bypassing ordinary minimum.
