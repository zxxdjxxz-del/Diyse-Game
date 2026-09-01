# Diyse — B00 Runtime Character Derivative Spec v1

**Status:** **SUPERSEDED FOR PRIMARY RUNTIME — RETAINED AS OPTIONAL 2D FALLBACK REFERENCE**  
**Superseded by:** `B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

## Decision

The earlier B00 plan assumed dedicated character art derivatives at approximately **200–220 px battle height** and **~80 px field height**.

That is no longer the primary runtime plan because Diyse is proceeding with **rigged 3D character models** for field and battle presentation when a production-usable rig is available.

The six fingerprinted B00 high-resolution masters remain the visual authority. Runtime characters should now be validated by matching those masters in the rigged model, materials, shader/outline treatment, animation, field camera and battle camera.

Do **not** create the previously planned six battle redraws and six field sprites merely to satisfy B00.

## What remains useful from this spec

The old simplification principles remain useful as **screen-space readability guidance**:
- preserve silhouette before microdetail;
- preserve signature weapon/prop shape;
- preserve hair mass and dominant palette blocks;
- preserve major armor/clothing/material divisions;
- remove or simplify details that shimmer, alias or disappear at distance;
- keep the character stronger than environment noise;
- maintain clear VFX overlap readability.

Those goals should now be achieved through:
- mesh LOD;
- material/detail LOD;
- outline tuning;
- selective secondary-motion budgets;
- camera-aware presentation;
- authored runtime simplification;

rather than separate sprite identities.

## Optional future use

This file may still guide intentionally 2D assets such as:
- special cut-ins;
- icons or minimap representations;
- deliberately sprite-based effects;
- an explicitly approved alternate presentation mode.

It is **not** the active B00 gate.

## Active gate

See:
`B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

Current production state:

`6/6 HIGH-RES MASTERS LOCKED → RIGGED MODEL RUNTIME VALIDATION ACTIVE`
