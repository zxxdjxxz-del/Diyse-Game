# Diyse — Portrait / Optional 2D Derivative Compatibility Rules

**Status:** ACTIVE COMPATIBILITY ROUTER — NOT PRIMARY FIELD/BATTLE CHARACTER AUTHORITY  
**Primary portrait pipeline:** `CHARACTERS/PORTRAIT_DERIVATIVE_PIPELINE.md`  
**Primary field/battle runtime gate:** `BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`  
**Character identity authority:** `CHARACTERS/README.md`

Diyse's permanent-party field and battle presentation now uses the rigged-3D character pipeline. The former dedicated ~80 px field and ~200–220 px battle sprite targets are retired as production requirements.

This file remains only for intentionally 2D derivatives such as portraits, cut-ins, icons, minimap representations, special illustrated states, or another explicitly approved 2D surface.

## Source hierarchy

1. newest exact approved character master;
2. matching current visual-lock document;
3. approved purpose-specific derivative pipeline/spec;
4. generated derivative.

A derivative never outranks its master.

## Screen-space simplification

For any optional small 2D derivative:
- preserve silhouette before microdetail;
- preserve hair mass and dominant palette blocks;
- preserve major clothing/armor divisions;
- preserve only the weapon/prop state actually required by that feature;
- remove detail that aliases, shimmers, or becomes unreadable at the feature's real output size.

Do not use retired fixed sprite heights as a character-identity rule.

## Portraits

Portraits carry:
- facial acting;
- eye color;
- scars/marks actually present in the current master;
- hair detail;
- age identity;
- emotional nuance.

Use `CHARACTERS/PORTRAIT_DERIVATIVE_PIPELINE.md` for current portrait production and validation. Do not use a simplified field/battle derivative as face-authority reference.

## Cut-ins and other illustrated derivatives

Named signature / Ultimate / Prime cut-ins and other illustrated derivatives must return to:
- the exact current face;
- exact current costume/body identity;
- the correct current equipment/prop state for that scene or feature.

Do not invent a separate "super form" or permanent equipment silhouette unless explicitly approved.

## Historical boundary

Git history preserves the former dedicated field/battle sprite plan. It must not be used to restore the retired ~80 px / ~200–220 px production gates or create a second character identity beside the rigged-3D runtime model.
