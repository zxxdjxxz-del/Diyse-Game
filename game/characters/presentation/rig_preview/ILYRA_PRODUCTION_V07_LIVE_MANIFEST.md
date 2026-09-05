# Ilyra Production Mesh v0.7 — seam-repaired live deformation candidate

v0.7 keeps the v0.6 UAL + spring architecture unchanged and corrects the largest animated seam defects found by the literal UAL deformation contact sheet.

## Binary asset

Copy:

`Ilyra_ProductionMesh_v07_UAL_SpringReady.glb`

to:

`asset_sources/animation/ual/`

Then run:

`game/characters/presentation/rig_preview/ilyra_production_v07_preview.tscn`

## What changed from v0.6

The v0.6 mesh ended its flexible clothing at the `lowerarm_*` and `calf_*` bones while its rigid gloves/boots followed `hand_*` and `foot_*`. Under animation this created large visible gaps.

Measured v0.6 gaps across Walk/Crouch/Roll were approximately:

- bracer / glove region: 0.21–0.23 m
- greave / boot region: 0.36–0.40 m

v0.7 adds four flexible underlayers:

- `FlexibleForearmUnderlayer_l`
- `FlexibleForearmUnderlayer_r`
- `FlexibleShinUnderlayer_l`
- `FlexibleShinUnderlayer_r`

They are multi-bone skinned across:

- `lowerarm → hand`
- `calf → foot`

The rigid bracers, gloves, greaves and boots remain rigid on their original attachment bones.

After the repair, measured connector-to-hard-gear gaps across Walk/Crouch/Roll are approximately 0.01–0.025 m.

## What did not change

- first 65 skin joints are still the unchanged UAL core
- 35 auxiliary hair/cape spring bones remain appended after the core
- actual replacement long-hair meshes remain spring-weighted
- actual replacement cape remains spring-weighted
- UAL animation-library merge path is unchanged
- SpringBoneSimulator3D starter settings are unchanged
- covered mannequin-derived torso/limb understructure remains pruned

## Known remaining issues

- face is still a generated approximation, not exact B00 likeness
- boots/gloves/bracers/greaves remain primitive production-base shapes
- extreme roll/crouch poses still produce hard-gear and tabard intersections
- spring inertia has not been visually executed in this environment
- final UVs, textures, materials and exact hair topology remain open

## Direction from here

v0.7 is now the active replacement-mesh deformation test. Continue correcting concrete visual/deformation failures on this mesh; do not add another abstract rig stage unless a specific failure proves the current architecture insufficient.

## Authority boundary

The approved cleaned Ilyra B00 remains exact visual authority and overrides this generated candidate wherever they differ.
