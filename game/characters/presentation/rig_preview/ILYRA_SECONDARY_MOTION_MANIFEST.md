# Ilyra Stage 8 — Secondary Motion / UAL Proof

## Purpose

Stage 8 keeps the Stage 7 production-topology body and adds dedicated inertial motion for Ilyra's two largest secondary-silhouette systems: her long blonde hair and pale-blue cape.

This remains a rig/deformation prototype. Ilyra's approved cleaned B00 image is still the exact appearance authority.

## Skeleton rule

The imported UAL skeleton is preserved exactly as the first **65 bones**. Stage 8 appends auxiliary bones after that core; it does not rename, reorder, reparent, resize, or replace any UAL bone.

Runtime Stage 8 skeleton:

- 65 imported UAL core bones
- 20 hair spring bones: 5 chains × 4 bones
- 15 cape spring bones: 3 chains × 5 bones
- **100 runtime bones total**

UAL animation tracks continue to target only the original 65 bones.

## Spring system

Stage 8 uses Godot `SpringBoneSimulator3D`, which is intended for inertial oscillation of hair and cloth after skeletal animation.

Hair chains:

- `IlyraHairSpring_OuterL_00..03`
- `IlyraHairSpring_InnerL_00..03`
- `IlyraHairSpring_Center_00..03`
- `IlyraHairSpring_InnerR_00..03`
- `IlyraHairSpring_OuterR_00..03`

Hair starter tuning:

- stiffness 0.68
- drag 0.20
- gravity 0.16
- radius 0.018

Cape chains:

- `IlyraCapeSpring_L_00..04`
- `IlyraCapeSpring_C_00..04`
- `IlyraCapeSpring_R_00..04`

Cape starter tuning:

- stiffness 0.44
- drag 0.30
- gravity 0.32
- radius 0.026

## Collision proxies

Spring collision is intentionally lightweight for this proof:

- head sphere attached to `Head`
- upper-torso capsule attached to `spine_03`
- hip sphere attached to `pelvis`

These are spring-solver collision proxies only, not gameplay collision shapes.

## Geometry replacement

When Stage 8 spring mode is ON:

- Stage 7 `ProductionBackHairMass` is hidden
- Stage 7 `ProductionPaleBlueCape` is hidden
- five spring-skinned hair ribbons are shown
- one spring-skinned cape grid is shown
- Stage 7 face-framing hair remains body-weighted near the face
- Stage 7 torso, sleeves, hip drape, tabard, Wardrod, shield, bracers, greaves, and hard/detail geometry stay unchanged

Secondary proof geometry adds about **85 vertices / 94 triangles** above Stage 7. This is intentionally a rig test, not final hair/cape topology.

## Controls

- `SPACE` — next Stage 8 stress animation
- `P` — pause/resume
- `V` — character / underlying UAL body
- `L` — Stage 7 / Stage 6
- `K` — Stage 6 weighted / Stage 5 rigid
- `M` — Stage 8 spring hair+cape / Stage 7 ordinary weighted hair+cape
- `F` — toggle a mild external wind force
- `N` — toggle the 35 auxiliary spring-bone markers
- `B` — toggle Stage 7 core transition-bone markers
- `Q / E` — rotate
- `T` — turntable
- `R` — restart sequence

## Stress loop

T-pose → Walk → Jog → Sprint → Jump Start → Jump Land → Roll → Shield Dash → Warden Cast → Knockback.

## Production boundary

Stage 8 proves the architecture for secondary motion, not final simulation tuning. Before production lock, Ilyra still needs:

- final authored hair/cape topology matching B00 exactly
- final chain locations placed against that topology
- tuned per-joint stiffness/drag rather than one value per chain
- self/body collision refinement
- teleport/reset handling in real gameplay scenes
- animation-state-specific damping as needed
- performance checks with the full party and combat VFX

Do not treat Stage 8's hair shapes, cape cut, spring values, collision radii, or auxiliary-bone count as final canon.
