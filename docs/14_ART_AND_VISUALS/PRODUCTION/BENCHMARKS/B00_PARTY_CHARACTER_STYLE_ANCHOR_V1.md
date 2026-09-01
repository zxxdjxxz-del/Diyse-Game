# Diyse — B00 Party Character Style Anchor v1

**Benchmark:** B00 — Permanent Party / Character Style Anchor  
**Status:** **HIGH-RES PARTY MASTER SET COMPLETE — 6 OF 6 LOCKED / RIGGED MODEL RUNTIME VALIDATION ACTIVE**  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Active runtime spec:** `B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`  
**Superseded sprite spec:** `B00_RUNTIME_DERIVATIVE_SPEC_V1.md`

## 1. Scope

B00 establishes the permanent-party rendering language for Diyse's locked visual direction:

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**

The permanent party is Cyanis, Ilyra, Torren, Nimera, Vaelira, and Seyrik.

All six high-resolution character masters are explicitly approved and fingerprinted. B00 as a full production benchmark is **not yet closed**: the approved designs must now be proven as rigged runtime characters under Godot field/battle cameras, animation, materials, environments and VFX.

## 2. Current progress

| Character | State |
|---|---|
| Cyanis | **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED** |
| Ilyra | **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED** |
| Torren | **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED** |
| Nimera | **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED** |
| Vaelira | **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED** |
| Seyrik | **HIGH-RES NEW-STYLE MASTER APPROVED / LOCKED** |

Current production-lock authorities:
- `../CHARACTERS/CYANIS_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/TORREN_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/NIMERA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/VAELIRA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/SEYRIK_CURRENT_VISUAL_LOCK.md`

## 3. Approved-anchor significance

The complete six-character master set establishes the party-wide B00 grammar:
- mature seinen/anime proportions;
- graphic cel-informed values rather than soft-brushed rendering;
- strong clean silhouettes;
- coherent garment/armor construction;
- clear cloth/leather/metal/foliage/crystal/biomechanical material separation as applicable;
- restrained, deliberate ornament rather than generic fantasy clutter;
- controlled metallic highlight planes;
- deliberate variable line hierarchy;
- no random speckle/grunge dependency;
- no painterly direction;
- single clean full-body master presentation as the preferred high-resolution review format.

Character-specific contributions:
- **Cyanis:** mobile royal battle-knight structure, clean silver armor over dark royal blue / black layers.
- **Ilyra:** light defensive / warding language with pale fabric, long blonde hair/cape read and restrained metal structure.
- **Torren:** dense natural camouflage and rugged equipment, with ghillie foliage readable as intentional masses rather than noise.
- **Nimera:** busy braided/updo hair, Cardweaver props, constellation motifs, layered utility hardware and strong white/purple/black separation without artifact-dot dependency.
- **Vaelira:** Green Arcanist silhouette, black cloth foundation, emerald outer garments/boots, silver metalwork, Arcane Staff and restrained crystal focus.
- **Seyrik:** Black Host-derived skeletal/alien biomechanical plate, polished black shell over crimson understructure, red-dominant long coat, imposing muscular silhouette and oversized two-handed greatsword.

## 4. High-resolution master rules

The high-resolution masters are complete. Any future revision must continue to satisfy:
- mature seinen/anime proportions and facial construction;
- approved identity without accidental age/face drift;
- visibly variable line weight with tapered/broken/selective contours;
- precise restrained facial linework;
- large readable hair masses;
- graphic cel-informed shading with roughly 2–4 dominant value groups;
- clean material separation;
- coherent clothing/armor construction;
- rich but controlled color;
- no painterly/soft-brushed rendering;
- no glossy mobile-gacha finish;
- no photoreal rendering;
- no sterile uniform digital outline;
- no generic AI-smooth, random-speckle, grunge, artifact-dot or broken-clothing treatment.

Character-specific redesigns remain valid only when explicitly approved. Gameplay equipment rules remain governed by their own canon authorities.

## 5. Runtime representation decision

Diyse's primary field and battle character representation is now **rigged 3D character models**, provided the current production rig/model solution passes B00 validation.

The earlier dedicated sprite targets of ~200–220 px battle art and ~80 px field art are **not required production deliverables** for B00. The old `B00_RUNTIME_DERIVATIVE_SPEC_V1.md` is retained only as optional 2D/screen-space simplification reference.

The active gate is `B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`.

The same character model family should normally serve field and battle, with context-specific:
- camera framing;
- animation sets;
- mesh/material LOD;
- outline strength;
- weapon/prop state;
- secondary motion;
- shadows and VFX attachment behavior.

## 6. Runtime visual requirements

The rigged characters must reproduce the approved B00 masters through:
- character-specific proportions rather than one generic body;
- faithful face/hair silhouette;
- correct garment and armor construction;
- correct weapon/prop identity and scale;
- graphic cel-informed real-time materials;
- controlled non-photoreal metal/cloth/leather response;
- variable/irregular outline rhythm at useful screen distances;
- stable animation deformation and attachment points;
- screen-space readability in both exploration and combat.

Rig functionality alone does not equal visual approval.

## 7. Production sequence

Completed:
1. approve all six clean high-resolution B00 masters;
2. fingerprint/document all six masters;
3. retire the unnecessary dedicated field/battle sprite gate;
4. lock the rigged-model runtime validation grammar.

Next:
5. identify and import the current production-usable rigged humanoid model/skeleton into the Godot character pipeline;
6. validate rig/retarget compatibility with representative locomotion and battle clips;
7. build one B00-faithful model/material/shader pilot;
8. validate it against the exact approved master in neutral presentation;
9. validate the same model at field camera distance;
10. validate the same model at battle camera distance;
11. test representative B01 stone, B03 foliage and B10 prop environments;
12. test representative B06 VFX overlap;
13. propagate the proven model/material/rig grammar across all six characters;
14. compare all six together for silhouette, palette, scale and animation coherence;
15. only then declare B00 fully passed.

## 8. Asset Forge / Godot boundary

Asset Forge's glTF renderer is useful for deterministic model/material review but is not the final runtime renderer. The final B00 model gate must be exercised in Godot because it depends on:
- skeleton/skin deformation;
- retargeted animation;
- shader behavior;
- outlines;
- camera distance;
- lighting;
- shadows;
- secondary motion;
- VFX overlap.

## 9. Cross-category validation

Once the runtime-model gate passes, recheck B01 stone, B03 foliage, B10 props, B06 VFX, and future enemy/NPC art against the actual six-character party rendering grammar.

Earlier material-family work is not automatically invalidated, but it must conform to the revised non-painterly visual authority before final acceptance.

## 10. Promotion state

Current state:

`VISUAL STYLE LOCKED → 6/6 HIGH-RES PARTY MASTERS LOCKED → RIGGED MODEL RUNTIME SPEC LOCKED → MODEL/SHADER/RIG PILOT NEXT`
