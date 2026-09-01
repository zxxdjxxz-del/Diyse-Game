# Diyse — B00 Rigged Character Runtime Validation v1

**Status:** **ACTIVE B00 RUNTIME GATE**  
**Parent benchmark:** `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Character readability authority:** `../CHARACTER_SCALE_AND_SILHOUETTE.md`

## 1. Runtime decision

Diyse's permanent party should use **rigged 3D character models as the primary field and battle representation** when a production-usable rigged model is available.

The previously planned dedicated ~200–220 px battle redraws and ~80 px field sprites are **not a required B00 production gate** under this runtime direction.

The six approved high-resolution B00 character masters remain essential. They are the exact visual authorities that the rigged runtime characters must reproduce.

2D character art remains appropriate for:
- dialogue portraits / busts;
- menus and status presentation;
- Cards / Primes;
- illustrated cut-ins;
- promotional/key art;
- any deliberately 2D special presentation approved later.

## 2. One character model, multiple runtime contexts

Field and battle should normally use the **same character identity, skeleton, rig and master model family**, with context-specific presentation rather than separate character art pipelines.

Differences may include:
- camera distance and framing;
- animation state set;
- weapon visibility / equipped prop state;
- mesh LOD;
- hair / cloth / foliage secondary-motion budget;
- material detail level;
- outline strength;
- shadow quality;
- VFX attachment points;
- battle-only stance or pose language.

Do not create a second visual identity for battle and field.

## 3. Exact B00 source authority

Every runtime character model must be checked against the current fingerprinted B00 master:
- `../CHARACTERS/CYANIS_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/TORREN_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/NIMERA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/VAELIRA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/SEYRIK_CURRENT_VISUAL_LOCK.md`

The approved image controls face, hair, body proportion, costume construction, palette, material separation, weapon/prop identity and silhouette unless explicitly revised later.

A runtime model is not approved merely because it is rigged and functional.

## 4. Model-match requirements

### Anatomy / proportion
- reproduce each character's approved body proportions rather than forcing all six onto one generic body;
- preserve age read and head/body ratio;
- preserve major height/build differences;
- do not allow rig retargeting to distort shoulders, hands, limbs or posture.

### Face / hair
- face must remain recognizably the approved character at neutral camera distance and close dialogue/cutscene distance;
- preserve locked eye color and facial structure;
- hair must reproduce the large approved silhouette masses before strand detail;
- hair cards/meshes must not become noisy at gameplay distance.

### Clothing / armor
- reproduce real garment layering and approved construction;
- avoid fused coat/skirt/armor geometry where the master establishes separate layers;
- preserve major coat/cape/ghillie silhouettes;
- armor plates must articulate without obvious clipping or implausible deformation;
- cloth and armor may use simulation/secondary motion only when stable and readable.

### Weapons / props
- preserve approved weapon family, scale and silhouette;
- weapon grip points must support the actual combat usage;
- two-handed weapons must be rigged and animated as two-handed weapons even if a neutral pose uses one hand;
- Cards/books/staves/bows/quivers/shields/foci must use explicit attachment points instead of floating or hand-authored per-animation offsets wherever possible.

## 5. Diyse runtime material treatment

The runtime model must translate B00's graphic seinen/anime rendering into real-time materials rather than attempting photoreal PBR.

### Base treatment
- graphic cel-informed value grouping;
- approximately 2–4 dominant light/value bands where appropriate;
- rich but controlled color;
- simplified material response;
- selective crisp metal highlights;
- cloth and leather clearly less reflective than metal;
- no glossy mobile-gacha plastic look;
- no photoreal texture noise;
- no random grunge/speckle used as detail.

### Outline / ink treatment
The runtime line solution should reproduce the **rhythm** of chaotic variable line weight rather than literally drawing every master-art stroke.

Preferred behavior:
- strongest outer silhouette;
- heavier marks at major overlaps and deep occlusion;
- thinner/selective interior line accents;
- width influenced by camera distance, facing angle, object/material masks or authored weight maps;
- optional authored texture/decal ink accents for signature armor/fabric/hair features;
- do not uniformly outline every polygon edge.

A hybrid approach is allowed: geometry/post-process silhouette line plus authored interior ink accents.

## 6. Field presentation validation

Field validation is performed at the **actual exploration camera and target display resolution**, not by creating an 80 px sprite.

A field model passes when:
- the character is identifiable immediately by silhouette and palette;
- head/hair mass still reads;
- major coat/cape/ghillie/skirt shapes survive;
- signature weapon/prop remains readable when normally shown;
- line treatment does not shimmer or collapse into noise;
- small accessories do not become distracting flicker;
- animation remains readable while moving through representative environments.

LOD/material simplification is preferred over creating a separate sprite identity.

## 7. Battle presentation validation

Battle validation is performed at the **actual battle camera and target display resolution**, not by creating a 200–220 px battle redraw.

A battle model passes when:
- stance and weapon silhouette are immediately readable;
- face/hair identity survives at intended camera distance;
- major material divisions remain clear;
- attack anticipation, impact, hit reaction and recovery remain readable;
- armor/cloth/hair secondary motion does not obscure action;
- VFX overlap does not erase silhouette or status readability;
- outline/material treatment remains stable during animation.

## 8. Animation / rig validation

The current rigged character solution must pass:
- neutral idle;
- walk / run;
- turn / direction change;
- battle ready / idle;
- basic attack appropriate to the equipped weapon;
- hit reaction;
- defend/guard presentation where applicable;
- ability casting/action pose;
- KO/downed state;
- transition between exploration and combat presentation if the same rig is reused directly.

Available verified-CC0 animation libraries may be used as retargeting/prototyping sources, but retargeted motion is not automatically final. Each clip must be checked for Diyse character weight, weapon logic, foot contact, hand placement and silhouette.

## 9. Character-specific runtime stress tests

### Cyanis
Test silver-armor vs royal-blue/black separation, bilateral shoulders, longcoat motion and clean knight silhouette.

### Ilyra
Test pale-value readability, long blonde hair/cape motion and Wardrod/Shield/Focus attachment logic without sword drift.

### Torren
Test bow/quiver placement, ghillie-cape silhouette, foliage secondary motion and avoidance of alpha-card noise.

### Nimera
Test dense braided hair, waist-tied constellation garment, Card/book attachments and utility hardware without clipping or noisy motion.

### Vaelira
Test long crimson hair, emerald coat/skirt, black bodysuit, silver accents, tall boots and Arcane Staff handling. No archer/ranger cues.

### Seyrik
Test broad muscular proportions, red-dominant coat, Black Host skeletal/biomechanical plate articulation and oversized two-handed greatsword handling.

## 10. B00 model-validation sequence

1. preserve the six fingerprinted B00 masters as visual authority;
2. identify the current rigged humanoid model/skeleton used for the pilot;
3. validate skeleton/retarget compatibility and animation import in Godot;
4. create one B00-faithful character model/material pilot;
5. validate neutral studio render against the approved master;
6. validate the same model at field camera distance;
7. validate the same model at battle camera distance;
8. test idle/walk/run/basic battle animation;
9. test representative B01 stone, B03 foliage and B10 prop environment context;
10. test representative B06 VFX overlap;
11. correct shader/outline/LOD/rig issues;
12. propagate the proven model/material/rig grammar across all six characters;
13. compare all six together for silhouette and palette separation;
14. close B00 only after the runtime models belong visibly to the same game as the approved masters and benchmark environments.

## 11. First pilot

Use the **current production-usable rigged humanoid base** as the technical pilot.

If its proportions and rig are compatible, **Cyanis** remains the preferred first character-style target because his blue/black cloth plus silver armor gives a clean material and outline baseline. If the available rig is materially better suited to another approved party member, use that character for the technical pilot without changing canon priority.

## 12. Asset Forge / Godot boundary

Existing `tools/asset_forge/model_render_engine.py` is useful for deterministic glTF/material validation, but it explicitly remains a **validation renderer rather than the final Godot renderer**.

Existing animation tooling may support source/sequence validation, but final character motion, skeleton retargeting, skin deformation, shader behavior and runtime camera tests must be validated in Godot.

Do not mistake a successful offline Asset Forge render for final runtime approval.

## 13. Gate

Current B00 gate:

`6/6 HIGH-RES MASTERS LOCKED → RIGGED MODEL RUNTIME SPEC LOCKED → MODEL / SHADER / RIG PILOT NEXT → FIELD + BATTLE CAMERA VALIDATION → B01/B03/B10/B06 CROSS-CHECK → B00 PASS`
