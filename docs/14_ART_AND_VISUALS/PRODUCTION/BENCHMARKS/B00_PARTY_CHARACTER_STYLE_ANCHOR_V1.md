# Diyse — B00 Party Character Style Anchor v1

**Benchmark:** B00 — Permanent Party / Character Style Anchor  
**Status:** **6/6 CURRENT REPOSITORY MASTERS LOCKED — RUNTIME TRANSLATION GATE ACTIVE**  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Character authority index:** `../CHARACTERS/README.md`  
**Active runtime spec:** `B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`  
**Rig standard:** `../QUATERNIUS_HUMANOID_RIG_STANDARD_V1.md`

## 1. Scope

B00 establishes the permanent-party rendering language for Diyse's locked visual direction:

> **Seinen HD-2D Fantasy with Chaotic Variable Line Weight + Graphic Anime-Stylized Rendering**

The permanent party is **Cyanis, Ilyra, Torren, Nimera, Vaelira, and Seyrik**.

The six current repository master images are the exact visual authorities for their identities. This benchmark controls shared party cohesion and the requirements for translating those masters into runtime characters; it does not supersede any individual master image.

## 2. Exact character authority

Use the authority order defined in `../CHARACTERS/README.md`:

1. current repository master image in `../../../../../asset_sources/characters/current/`;
2. matching `../CHARACTERS/*_CURRENT_VISUAL_LOCK.md`;
3. current B00 / Diyse visual-style rules;
4. older prose, archived renders, historical hashes, superseded concepts, or generated filenames.

Current permanent-party masters:

| Character | Repository master | Visual lock |
| --- | --- | --- |
| Cyanis | `asset_sources/characters/current/cyanis.jpg` | `../CHARACTERS/CYANIS_CURRENT_VISUAL_LOCK.md` |
| Ilyra | `asset_sources/characters/current/ilyra.jpg` | `../CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md` |
| Torren | `asset_sources/characters/current/torren.jpg` | `../CHARACTERS/TORREN_CURRENT_VISUAL_LOCK.md` |
| Nimera | `asset_sources/characters/current/nimera.jpg` | `../CHARACTERS/NIMERA_CURRENT_VISUAL_LOCK.md` |
| Vaelira | `asset_sources/characters/current/vaelira.jpg` | `../CHARACTERS/VAELIRA_CURRENT_VISUAL_LOCK.md` |
| Seyrik | `asset_sources/characters/current/seyrik.jpg` | `../CHARACTERS/SEYRIK_CURRENT_VISUAL_LOCK.md` |

Do not infer surnames from superseded documents. The current production identities use the character names above.

## 3. Shared B00 party grammar

The six-character set must remain visibly part of the same game while preserving each person's exact identity. Shared requirements:

- mature seinen/anime proportions and facial construction;
- strong, clean, character-specific silhouettes;
- deliberate chaotic variable line hierarchy;
- graphic cel-informed value grouping;
- large readable hair and garment masses before microdetail;
- clear cloth / leather / metal / foliage / crystal / biomechanical material separation as applicable;
- controlled metallic highlights rather than photoreal or plastic response;
- rich but controlled color;
- restrained, authored detail rather than generic fantasy clutter;
- no painterly/soft-brushed target;
- no glossy mobile-gacha finish;
- no random speckle, grunge, artifact dots, broken seams, or AI-noise dependency.

## 4. Character separation anchors

These are runtime/cohesion shorthand only. The repository images control exact minutiae.

- **Cyanis:** royal-blue / black / silver mobile battle-knight silhouette, dark hair, layered silver armor, long split outer garment.
- **Ilyra:** white / pale-blue Warden silhouette, long blonde hair, coherent pale-blue cape, restrained silver protection, vivid jade/green eye identity.
- **Torren:** rugged veteran ranger silhouette, forest-green clothing, golden-bronze medium armor, back-mounted bow, right-hip arrow draw/quiver layout, field gear, mixed-foliage ghillie mantle.
- **Nimera:** dark skin, large dark-purple braided/updo hair mass, white foundation, purple constellation waist garment, black utility masses, green Cardweaver prop cue.
- **Vaelira:** crimson/burgundy hair, emerald / black / silver Green Arcanist silhouette, Arcane Staff. **No bow or quiver.**
- **Seyrik:** massive black/crimson Black Host-derived heavy silhouette, skeletal/rib-like armor architecture, red/black outer garment mass, oversized two-handed greatsword.

These shorthand reads must never be used to redraw a character from memory when the exact repository master is available.

## 5. Party cohesion rule

Cohesion review compares the **actual current repository masters side by side**. Do not substitute regenerated lineup approximations or older master renders.

Review:
- face-construction maturity;
- eye treatment without erasing character-specific identity;
- line-weight behavior;
- value grouping;
- material highlight strength;
- ornament/detail density;
- foliage/hair microdetail density;
- saturation/color richness;
- silhouette strength and separation;
- same-game rendering feel.

Cohesion is not permission to redesign the six. Exact costumes, faces, hairstyles, body identities, palettes, equipment placement, weapons, and props remain controlled by each repository master.

## 6. Runtime representation decision

Diyse's primary field and battle character presentation uses **rigged 3D character models** once the model/rig solution passes B00 validation.

Dedicated ~200–220 px battle redraws and ~80 px field sprites are **not required B00 production deliverables**. Historical sprite specifications may inform simplification principles, but they do not override the active rigged-model pipeline.

The same character model family should normally serve field and battle, with context-specific camera framing, animation sets, mesh/material LOD, outline strength, equipment visibility, secondary motion, shadows, and VFX attachment behavior.

## 7. Runtime translation requirements

The rigged characters must reproduce the current masters through:
- character-specific proportions rather than one generic body;
- faithful face and hair silhouette;
- correct garment and armor construction;
- correct weapon/prop identity, scale, and left/right placement;
- graphic cel-informed real-time materials;
- controlled non-photoreal metal/cloth/leather response;
- variable/irregular outline rhythm at useful screen distances;
- stable animation deformation and attachment points;
- clear exploration and battle readability.

Rig functionality alone does not equal visual approval.

## 8. Redraw/reference rule

When producing a new character image or model:
- use only that character's current repository master as the subject/identity authority;
- other approved characters may guide shared technique and cohesion only;
- do not borrow another character's face, body, palette, costume, armor, equipment, or props;
- when a clean redraw is requested, rebuild rather than patching an older image;
- do not revive superseded designs because an older document contains more detailed prose.

## 9. B00 runtime sequence

Completed:
1. establish and lock the current six repository image masters;
2. align the six current visual-lock documents to those masters;
3. establish the character visual authority index;
4. lock the rigged-model runtime validation grammar;
5. verify the Quaternius-compatible V5 rig source used for technical prototyping.

Next runtime work:
6. validate the prototype rig in Godot;
7. validate skeleton hierarchy, animation import, skin deformation, and root-motion behavior;
8. create one B00-faithful model/material/shader pilot;
9. compare the pilot directly against its current repository master;
10. validate at real field and battle camera distances;
11. test representative environments and VFX overlap;
12. propagate only the proven model/material/rig grammar across all six;
13. compare all six runtime characters for silhouette, palette, scale, and animation coherence;
14. close B00 runtime translation only after the models visibly belong to the same game as the current masters.

## 10. Gate

Current B00 gate:

`6/6 CURRENT REPOSITORY MASTERS LOCKED → CHARACTER AUTHORITY SYSTEM ALIGNED → V5 RIG SOURCE VERIFIED → GODOT RIG/MODEL PILOT → FIELD + BATTLE CAMERA VALIDATION → SIX-CHARACTER RUNTIME COHESION → B00 PASS`
