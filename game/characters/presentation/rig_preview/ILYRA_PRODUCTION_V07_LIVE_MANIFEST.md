# Ilyra Production Mesh v0.7 — current live deformation candidate

**Status:** CURRENT ILYRA REPLACEMENT-MESH DEFORMATION TEST

## Binary asset

Current working binary:

`Ilyra_ProductionMesh_v07_UAL_SpringReady.glb`

Expected local path:

`asset_sources/animation/ual/`

Current preview:

`game/characters/presentation/rig_preview/ilyra_production_v07_preview.tscn`

## Current architecture

- first **65** skin joints are the unchanged UAL humanoid core;
- **35** auxiliary hair/cape spring bones are appended after the core;
- **100** skin joints total;
- UAL1 + UAL2 animation libraries use the shared core skeleton contract;
- the pale-blue cape is spring-weighted across three chains;
- five proof hair volumes are spring-weighted for secondary-motion architecture testing;
- covered mannequin-derived torso/limb understructure is pruned;
- flexible underlayers bridge each `lowerarm → hand` and `calf → foot` deformation span;
- rigid bracers, gloves, greaves, and boots remain attached to their intended hard-gear bones.

Current connector-to-hard-gear gaps measured across Walk/Crouch/Roll are approximately **0.01–0.025 m**.

## Current stress sequence

T-pose → Walk → Jog → Sprint → Crouch → Jump Start → Jump Land → Roll → Shield Dash → Warden Cast → Knockback.

The shared implementation is owned by:
`ilyra_production_preview_base.gd`

## Known remaining issues

- face is still a generated approximation, not exact current-master likeness;
- proof long-hair geometry does not match Ilyra's current neatly tied-back shorter hair and must be replaced during visual-fidelity work;
- boots/gloves/bracers/greaves remain primitive production-base shapes;
- extreme roll/crouch poses still produce hard-gear and tabard intersections;
- spring inertia still requires final visual tuning;
- final UVs, textures, materials, and exact hair topology remain open.

## Direction

Continue correcting concrete visual/deformation failures on the current model. Do not recreate earlier proxy/blockout/topology stages unless a current, specific technical requirement cannot be tested on this candidate.

## Authority boundary

Exact Ilyra appearance is owned by `asset_sources/characters/current/ilyra.jpg` and `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md`. Those current sources override this generated candidate wherever they differ.
