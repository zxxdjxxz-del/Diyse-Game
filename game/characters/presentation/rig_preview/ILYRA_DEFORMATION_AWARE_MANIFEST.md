# Ilyra UAL Stage 6 — Deformation-Aware Character Proof

Stage 6 keeps the exact UAL 65-bone skeleton and animation libraries, but moves the character pieces that should flex across joints from rigid `BoneAttachment3D` behavior to real multi-bone vertex weighting.

## Newly weighted geometry

- **Fitted Warden vest:** `spine_03 → spine_02 → spine_01 → pelvis`
- **Blue torso center panel:** same torso weighting as the vest
- **Long blonde hair locks:** `Head → neck_01 → spine_03 → spine_02`
- **Pale-blue cape:** `spine_03 → spine_02 → spine_01 → pelvis`
- **Front tabard:** `pelvis → thigh_l + thigh_r`
- **Side tabards:** `pelvis → matching thigh`

The face/head shell, hair cap, collar/clasp, bracers, greaves, Wardrod and shield remain rigid to their appropriate existing bones intentionally.

## Skeleton rule

Stage 6 adds **zero new core animation bones**. It creates a Godot `Skin` from the existing UAL rest transforms and supplies four bone indices/weights per custom `ArrayMesh` vertex. The UAL animation contract stays unchanged.

## Comparison controls

- **V** — authored character vs underlying UAL-skinned body
- **K** — Stage 6 multi-bone deformation vs Stage 5 rigid deformable pieces
- **Q / E** — manual rotation
- **T** — automatic turntable
- **Space** — next deformation-test animation
- **P** — pause
- **R** — restart sequence
- **Esc** — quit

The stress sequence includes walking, jogging, crouching, rolling, shield movement, casting and a hit reaction.

## Authority boundary

This remains a rig/deformation proof rather than Ilyra's final production mesh. The approved cleaned B00 remains exact authority for her face identity, vivid jade eyes, blonde hair design, body proportions, clothing cuts, pale-blue cape, restrained decoration, and equipment appearance.
