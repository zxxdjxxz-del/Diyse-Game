# Ilyra Production Mesh v0.6 — live UAL + spring preview

Purpose: first Diyse rig-preview scene that uses the actual replacement Ilyra visual shell instead of the older mannequin/proxy character construction.

## Required binary asset

Copy the generated file to:

`asset_sources/animation/ual/Ilyra_ProductionMesh_v06_UAL_SpringReady.glb`

The UAL1 and UAL2 Standard GLBs remain required in the same folder.

## Runtime architecture

- first 65 skin joints are the unchanged UAL core, in the original order
- 35 auxiliary character-specific bones are appended after the UAL core
- five 4-bone hair chains drive the actual `LongHair_0..4` v0.4 replacement geometry
- three 5-bone cape chains drive the actual `PaleBlueCape` replacement geometry
- no duplicate proxy hair/cape is generated for this scene
- all non-secondary geometry continues to reference only UAL joint slots 0–64
- the spring-ready GLB has 100 skin joints total

## Understructure cleanup

The full mannequin-derived body was causing visible skin breakthrough during crouch, roll and other extreme animation poses. v0.6 prunes covered understructure triangles and retains only the head/neck and distal hand/finger regions that the replacement shell still needs.

This is a modeling/deformation correction, not a new rig architecture.

## Spring configuration

Starter values are intentionally inherited from the Stage 8 proof:

- hair: stiffness 0.68, drag 0.20, gravity 0.16, radius 0.018
- cape: stiffness 0.44, drag 0.30, gravity 0.32, radius 0.026
- head sphere collision
- upper-torso capsule collision
- pelvis sphere collision
- optional mild external wind

## Stress sequence

T-pose → Walk → Jog → Sprint → Crouch → Jump Start → Jump Land → Roll → Shield Dash → Warden Cast → Knockback.

## Controls

- `SPACE` next animation
- `P` pause/resume
- `M` spring simulation on/off
- `F` wind on/off
- `N` auxiliary spring-bone debug markers
- `Q / E` rotate manually
- `T` automatic turntable
- `R` restart stress sequence
- `ESC` quit

## Literal deformation validation

A software deformation pass applied real UAL animation tracks directly to the v0.6 GLB for Walk, Crouch, Roll, Shield Dash, Warden Cast and Knockback. This caught the mannequin-understructure breakthrough and drove the v0.6 pruning pass.

That offline renderer does not simulate `SpringBoneSimulator3D`; spring inertia remains a Godot runtime validation item.

## Known remaining visual problems

- face is still a generated modeling-base approximation, not the exact B00 likeness
- hair volumes are still simple authored/generated forms
- boot/ankle and some joint transitions need production cleanup
- extreme roll/crouch poses expose hard-gear intersections
- Wardrod and shield are still simplified production-base shapes
- UVs/textures/final materials are not authored

Do not add another abstract rig stage unless a specific deformation failure requires it. The next passes should improve the visible replacement mesh and weights revealed by this stress test.

## Authority boundary

This mesh is not Ilyra visual canon. The approved cleaned B00 remains exact visual authority and overrides the v0.6 candidate wherever they differ.
