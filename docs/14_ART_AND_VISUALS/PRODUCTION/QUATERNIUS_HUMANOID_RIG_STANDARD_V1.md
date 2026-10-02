# Diyse — Quaternius-Compatible Humanoid Rig Standard v1

**Status:** **ACTIVE PROTOTYPE RIG STANDARD — GODOT UAL FOUNDATION PROVEN**  
**B00 runtime gate:** `BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

## 1. Decision

Diyse uses the **Quaternius Universal Animation Library humanoid Armature as the official prototype skeleton/rig foundation** for permanent-party runtime character work.

The purpose is technical compatibility and animation reuse. It does **not** make a stock Quaternius mannequin the final visual identity of any Diyse party member.

Final visible characters must be Diyse-original models built to the approved B00 masters while preserving compatibility with this skeleton wherever practical.

## 2. V5 source verification

The rig is already contained inside the two verified-CC0 Quaternius animation archives represented by **Asset Library Master v5**. A separate `Universal Base Characters` archive is **not required for the prototype rig**.

The user re-uploaded both v5 archives in the active project conversation and their archive SHA-256 values exactly match `ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`:

- `Universal Animation Library[Standard].zip`  
  SHA-256 `cc73fc4e495b82958207316596317a3f40b9fa38065bde1027937452da537724`
- `Universal Animation Library 2[Standard].zip`  
  SHA-256 `4008ea208a604773a2b2177d965f0f5d3195498b5bf838c3f5785d68e95f2a68`

### Embedded Godot/glTF rig payloads

`Universal Animation Library[Standard].zip` contains:
- `Unreal-Godot/UAL1_Standard.glb`
  - 1 mesh: `Mannequin`
  - 1 skin: `Armature`
  - 43 animations
  - SHA-256 `69591853d817488edaa8fd9bf8fc1d821eaeaf789f8627b3cd23b41c4ed67997`
- `Unreal-Godot/UAL1_Standard_RM.glb`
  - same rigged mannequin family
  - 43 root-motion animations
  - SHA-256 `be684571ed655a1b892c2c07e6e2aeca053b606c442d34004adaf1d944090d01`

`Universal Animation Library 2[Standard].zip` contains:
- `Unreal-Godot/UAL2_Standard.glb`
  - 1 mesh: `Mannequin`
  - 1 skin: `Armature`
  - 43 animations
  - SHA-256 `8cee20ab1bc55130092447e810e26df22dd2803eccc54f52137a7d54d7ab88a8`
- `Unreal-Godot/UAL2_Standard_RM.glb`
  - same rigged mannequin family
  - 43 root-motion animations
  - SHA-256 `814eee878f82934992d3ea746c539df25e981487109c591f5efbb8dd03286f99`
- `Female Mannequin/Unreal-Godot/Mannequin_F.glb`
  - 1 mesh: `Mannequin`
  - 1 skin: `Armature`
  - 0 embedded animations; designed to share/retarget the library animations
  - SHA-256 `2ee6cc3fe888d9b144afa8cc4b2ab7bfc5d13a0d5b7548df777f61f64ad65fa6`

The included female-mannequin README explicitly states that the female mannequin shares the same rig and very similar proportions, and the animations can be retargeted from the library files.

## 3. Current prototype rig path

The active Godot preview path now:
- uses the **non-root-motion** UAL standard assets as the current deformation/animation proof source;
- merges UAL1 + UAL2 into the live preview animation library;
- uses the compatible female/shared-skeleton path as the permanent-party technical foundation;
- preserves the first **65 UAL bones unchanged** in the Ilyra production-mesh proof;
- appends **35 auxiliary spring bones** for current hair/cape secondary-motion testing.

The root-motion variants remain available for an explicit production comparison/policy decision; the current Ilyra v0.7 proof does not itself close that decision.

This rig choice is technical infrastructure and may evolve while preserving a compatible shared humanoid contract.

## 4. Skeleton compatibility requirements

All prototype/final party rigs should preserve a stable humanoid contract:
- consistent bone naming;
- consistent hierarchy;
- consistent rest pose;
- consistent model scale;
- consistent forward-axis convention after Godot import normalization;
- explicit root/root-motion policy;
- stable left/right hand attachment transforms;
- stable back/hip attachment points where needed;
- retarget-safe shoulder, elbow, wrist, hip, knee and ankle chains.

Do not allow each character to develop an incompatible ad-hoc skeleton unless a character-specific requirement genuinely cannot be expressed on the shared rig.

## 5. Runtime attachment standard

The shared rig should expose or support stable attachment points for at least:
- right-hand weapon;
- left-hand weapon / secondary;
- two-handed weapon secondary grip;
- shield / Focus;
- staff / Wardrod;
- bow;
- quiver / back equipment;
- hip book / grimoire;
- Card/hand prop origin;
- belt/hip utility prop;
- VFX hand origins;
- torso/center VFX origin;
- head/face VFX origin;
- feet for contact and ground effects.

Character-specific equipment may use a subset of these sockets.

## 6. Animation source status

The two v5 archives provide **86 verified-CC0 humanoid animation clips total** across UAL1 + UAL2.

They are valid prototype/retarget sources subject to the source checksums in `ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`.

Retargeted clips are **not automatically final Diyse animation**. Every motion must be reviewed for:
- character weight and personality;
- weapon logic;
- hand placement;
- foot contact;
- root motion;
- silhouette/readability;
- timing appropriate to Diyse combat;
- clipping with character-specific coats, capes, ghillie material, armor, hair and equipment.

## 7. Diyse-original visible model rule

The prototype rig/mannequin may come from the Quaternius ecosystem, but final visible party models must match the exact B00 masters:
- original heads/faces;
- original hair;
- original body proportions;
- original clothing/armor;
- original weapons/props;
- original textures/material identity;
- Diyse B00 shader/outline treatment.

The shared `Armature` is infrastructure, not character art authority.

## 8. Godot validation state

Completed in the staged repository preview:
1. import the non-root-motion UAL assets into Godot;
2. verify the shared humanoid skeleton path;
3. merge UAL1 + UAL2 into the preview animation library;
4. exercise the compatible female/shared-rig path;
5. retain the original 65-bone UAL core at the front of the Ilyra production skin;
6. prove multi-bone torso/cloth/hair/cape deformation;
7. append and simulate 35 auxiliary spring bones for hair/cape secondary motion;
8. run the current Ilyra v0.7 replacement shell through the UAL stress loop;
9. reduce the major v0.6 wrist/ankle seam failures with flexible underlayers in v0.7.

Still open before production propagation:
- explicit root-motion comparison and project policy;
- exact current-master character likeness, including replacement of visually superseded proof geometry;
- final attachment/grip verification across all needed equipment families;
- final shoulder/elbow/hip and hard-gear intersection cleanup;
- final spring tuning;
- production UVs/materials;
- B00 cel/outline treatment;
- actual field-camera and battle-camera validation;
- representative environment/VFX overlap;
- six-character shared-rig propagation and cohesion review.

Current detailed proof status:
> `game/characters/presentation/rig_preview/README.md`

## 9. Gate

`UAL SOURCE VERIFIED → GODOT UAL FOUNDATION PROVEN → ILYRA v0.7 DEFORMATION TEST ACTIVE → ROOT-MOTION POLICY / CURRENT-MASTER VISUAL CORRECTION → B00 PRODUCTION MODEL PILOT`
