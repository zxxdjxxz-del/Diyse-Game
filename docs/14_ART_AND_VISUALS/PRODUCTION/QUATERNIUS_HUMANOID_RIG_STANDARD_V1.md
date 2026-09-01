# Diyse — Quaternius-Compatible Humanoid Rig Standard v1

**Status:** **ACTIVE PROTOTYPE RIG STANDARD — V5 RIG SOURCE VERIFIED**  
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

## 3. Prototype rig choice

For the first Godot technical pilot:
- use `UAL1_Standard.glb` as the default **non-root-motion mannequin + Armature + animation** source;
- retain `UAL1_Standard_RM.glb` as the root-motion comparison source;
- use `Mannequin_F.glb` to verify that the same skeleton contract supports a female body proportion without requiring a second incompatible rig;
- use UAL2 clips to extend the available motion set once import/retarget behavior is proven.

This choice is technical and may be revised if Godot import testing reveals a better member file while preserving the same compatible skeleton contract.

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

## 8. Godot import validation

Before character-specific modeling is scaled across the party, validate the v5 rig through:
1. import `UAL1_Standard.glb` into Godot;
2. inspect skeleton hierarchy/rest pose;
3. confirm the embedded 43 animations import correctly;
4. compare non-root-motion vs `_RM` behavior;
5. test idle/walk/run playback;
6. decide the project root-motion policy;
7. create stable weapon/prop attachment points;
8. test a two-handed grip;
9. inspect skin deformation at shoulders/hips/knees;
10. import/retarget `Mannequin_F.glb` against the same animation set;
11. test one coat/cape secondary-motion setup;
12. run one field camera test;
13. run one battle camera test;
14. apply one B00 cel/outline material pilot;
15. test representative environment/VFX overlap.

## 9. Gate

`V5 QUATERNIUS RIG SOURCE VERIFIED → GODOT IMPORT/ROOT-MOTION/RETARGET TEST → B00 CHARACTER MODEL PILOT`
