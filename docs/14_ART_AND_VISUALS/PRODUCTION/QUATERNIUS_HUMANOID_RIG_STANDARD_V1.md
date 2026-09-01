# Diyse — Quaternius-Compatible Humanoid Rig Standard v1

**Status:** **ACTIVE PROTOTYPE RIG STANDARD**  
**B00 runtime gate:** `BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

## 1. Decision

Diyse uses a **Quaternius-compatible humanoid skeleton/rig as the official prototype foundation** for permanent-party runtime character work.

The purpose is technical compatibility and animation reuse. It does **not** make a stock Quaternius visible character model the final visual identity of any Diyse party member.

Final visible characters must be original Diyse models built to the approved B00 masters while preserving compatibility with the chosen humanoid skeleton wherever practical.

## 2. Prototype foundation

The selected prototype direction is based on the Quaternius Universal Base Character / Universal humanoid ecosystem:
- CC0 foundation;
- rigged humanoid base suitable for Godot prototyping;
- FBX / glTF-family interchange support in the source ecosystem;
- roughly low-to-mid five-figure triangle character-base scale suitable for a prototype foundation;
- intended compatibility with the Quaternius Universal Animation Library packages.

The exact final mesh budget for Diyse party characters is **not** locked by the stock base. Final budgets must be established through runtime performance and visual validation.

## 3. Skeleton compatibility requirements

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

## 4. Runtime attachment standard

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

## 5. Animation source status

The current authoritative source manifest already represents two verified-CC0 animation archives:
- `Universal Animation Library[Standard].zip`
- `Universal Animation Library 2[Standard].zip`

They are valid prototype/retarget candidates subject to the source checksums in `ASSET_LIBRARY/SOURCE_ARCHIVE_MANIFEST.md`.

Retargeted clips are **not automatically final Diyse animation**. Every motion must be reviewed for:
- character weight and personality;
- weapon logic;
- hand placement;
- foot contact;
- root motion;
- silhouette/readability;
- timing appropriate to Diyse combat;
- clipping with character-specific coats, capes, ghillie material, armor, hair and equipment.

## 6. Current source-preservation gap

The current `SOURCE_ARCHIVE_MANIFEST.md` and active `asset_sources/third_party_cc0/` representation include the two Universal Animation Library archives but do **not** currently list/preserve a `Universal Base Characters` source archive.

Therefore:
- the Quaternius-compatible skeleton decision is active;
- the base-character source should not be claimed as durably preserved in the current repo records;
- before a reproducible clean-room Godot import test, the exact CC0 base-character source used for the rig pilot should be supplied/recovered, hashed, inventoried and added to the asset-source ledger or another approved durable binary location;
- if a compatible rigged model already exists locally outside the repo, record its exact file identity/checksum before treating it as production authority.

Do not silently substitute a different humanoid base because the original source package is missing from the current archive manifest.

## 7. Diyse-original visible model rule

The prototype rig may come from the Quaternius ecosystem, but final visible party models must match the exact B00 masters:
- original heads/faces;
- original hair;
- original body proportions;
- original clothing/armor;
- original weapons/props;
- original textures/material identity;
- Diyse B00 shader/outline treatment.

The shared rig is infrastructure, not character art authority.

## 8. Godot import validation

Before character-specific modeling is scaled across the party, validate one rig through:
1. clean model import;
2. skeleton hierarchy inspection;
3. rest-pose verification;
4. animation-library retarget/import;
5. idle/walk/run playback;
6. root-motion decision;
7. hand/weapon attachments;
8. two-handed grip test;
9. skin deformation at shoulders/hips/knees;
10. one coat/cape secondary-motion test;
11. one field camera test;
12. one battle camera test;
13. one B00 cel/outline material pilot;
14. representative environment/VFX overlap.

## 9. Gate

`QUATERNIUS-COMPATIBLE RIG STANDARD LOCKED → EXACT BASE RIG SOURCE/PILOT FILE IDENTIFIED + HASHED → GODOT IMPORT/RETARGET TEST → B00 CHARACTER MODEL PILOT`
