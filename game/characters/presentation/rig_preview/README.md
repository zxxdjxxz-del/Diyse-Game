# Ilyra Current UAL Rig Preview

This folder contains the current Ilyra replacement-mesh deformation preview for the shared Universal Animation Library humanoid rig.

## Required binaries

Place the current non-root-motion UAL assets in:

`asset_sources/animation/ual/`

- `UAL1_Standard.glb`
- `UAL2_Standard.glb`

The current Ilyra replacement-mesh preview additionally expects:

- `Ilyra_ProductionMesh_v07_UAL_SpringReady.glb`

Binary UAL/character working assets are not committed through the text-oriented repository connector.

## Current preview

Run:

`ilyra_production_v07_preview.tscn`

Current implementation chain:

`ilyra_production_v07_preview.gd`
→ `ilyra_production_preview_base.gd`
→ `ual_rig_preview.gd`

The current preview proves:

- the original **65-bone UAL core** remains first and unchanged;
- **35 auxiliary hair/cape spring bones** are appended after the core;
- **100 skin joints total**;
- UAL1 + UAL2 animation-library merging;
- replacement-mesh deformation under the current stress sequence;
- multi-bone flexible connectors at forearm/hand and calf/foot transitions;
- Godot `SpringBoneSimulator3D` architecture for hair/cape secondary motion;
- collision proxies, spring toggling, mild wind, turntable controls, and debug markers.

Current stress sequence:

T-pose → Walk → Jog → Sprint → Crouch → Jump Start → Jump Land → Roll → Shield Dash → Warden Cast → Knockback.

Controls:

- `SPACE` next animation
- `P` pause/resume
- `M` springs on/off
- `F` mild wind on/off
- `N` spring-bone markers
- `Q / E` rotate manually
- `T` automatic turntable
- `R` restart sequence
- `ESC` quit

Current technical details and open defects:
`ILYRA_PRODUCTION_V07_LIVE_MANIFEST.md`

## Direction from here

Do not recreate superseded proxy/blockout/deformation-stage scenes. The current UAL core, replacement-mesh deformation path, and spring architecture are already proven.

Future passes should respond to concrete failures on the current model:
- exact current-master face likeness;
- replacement of the proof long-hair geometry with Ilyra's current neatly tied-back shorter hair silhouette;
- boot/glove/guard modeling;
- shoulder/elbow/hip weighting;
- tabard/hard-gear intersections in extreme poses;
- spring tuning;
- UVs and final materials.

## Authority boundary

This 3D candidate is implementation infrastructure, not Ilyra visual canon.

Exact appearance is owned by:
- `asset_sources/characters/current/ilyra.jpg`
- `docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md`

The current 2D master overrides the rig-preview model wherever they differ.
