# Diyse — B00 Rigged Character Runtime Validation v1

**Status:** **ACTIVE B00 RUNTIME GATE — CURRENT CHARACTER MASTERS LOCKED / UAL GODOT FOUNDATION PROVEN / ILYRA v0.7 DEFORMATION TEST ACTIVE**  
**Parent benchmark:** `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Character identity authority:** `../CHARACTERS/README.md`  
**Character readability authority:** `../CHARACTER_SCALE_AND_SILHOUETTE.md`  
**Prototype rig standard:** `../QUATERNIUS_HUMANOID_RIG_STANDARD_V1.md`

## 1. Runtime decision

Diyse's permanent party uses **rigged 3D character models as the primary field and battle representation** once the production rig/model solution passes B00 validation.

The previously planned dedicated ~200–220 px battle redraws and ~80 px field sprites are **not required B00 production deliverables**.

The six current repository image masters remain the exact visual authorities that the runtime characters must reproduce. 2D character art remains appropriate for dialogue portraits/busts, menus, Cards/Primes, illustrated cut-ins, promotional art, and other explicitly approved 2D presentation.

## 2. Character source authority

Before modeling or reviewing any party member, follow `../CHARACTERS/README.md`:

1. current repository master image in `asset_sources/characters/current/`;
2. matching current visual-lock document;
3. current B00 / Diyse style rules;
4. older prose, archived renders, historical fingerprints, generated filenames, or superseded concept notes.

Permanent-party master images:
- `asset_sources/characters/current/cyanis.jpg`
- `asset_sources/characters/current/ilyra.jpg`
- `asset_sources/characters/current/torren.jpg`
- `asset_sources/characters/current/nimera.jpg`
- `asset_sources/characters/current/vaelira.jpg`
- `asset_sources/characters/current/seyrik.jpg`

A runtime model is not approved merely because it is rigged and functional. It must visibly reproduce the current master.

## 3. Prototype rig foundation

The official prototype foundation is the **Quaternius Universal Animation Library humanoid `Armature`**, defined in `../QUATERNIUS_HUMANOID_RIG_STANDARD_V1.md`.

The verified pilot payload represented by Asset Library Master v5 includes the standard and root-motion UAL1/UAL2 rigged mannequin GLBs plus a compatible female mannequin on the same Armature contract. This source is for **technical rig/animation validation**, not character identity.

Repository implementation has progressed beyond source-only verification. The staged preview under `game/characters/presentation/rig_preview/` proves UAL1 + UAL2 animation-library merging in Godot, the shared 65-bone UAL core, multi-bone deformation, 35 appended auxiliary spring bones, and the current Ilyra v0.7 replacement-shell deformation path. Those proofs validate architecture only; they do not override the current exact character masters.

Never allow mannequin proportions, face, costume, or generic body construction to replace the proportions and identity of a Diyse repository master.

## 4. One character model, multiple runtime contexts

Field and battle should normally use the **same character identity, skeleton, rig, and master model family**, with context-specific presentation rather than separate character-art identities.

Differences may include:
- camera distance and framing;
- animation state set;
- weapon/prop visibility;
- mesh and material LOD;
- hair/cloth/foliage secondary-motion budget;
- outline strength;
- shadow quality;
- VFX attachment points;
- battle-only stance or pose language.

Do not create a second visual identity for battle and field.

## 5. Model-match requirements

### Anatomy / proportion
- reproduce each character's current approved body proportions rather than forcing all six onto one generic body;
- preserve age read and head/body ratio;
- preserve major height/build differences established by the masters;
- do not allow rig retargeting to distort shoulders, hands, limbs, waist, or posture.

### Face / hair
- face must remain recognizably the current approved character at neutral and appropriate close presentation distances;
- preserve the master-controlled facial structure and eye treatment;
- preserve large hair silhouette masses before strand detail;
- hair cards/meshes must not become noisy at gameplay distance.

### Clothing / armor
- reproduce the real garment layering and construction shown by the master;
- do not fuse coat/skirt/cape/armor layers when the master shows them separately;
- preserve major coat/cape/ghillie silhouettes;
- armor plates must articulate without implausible deformation or severe clipping;
- cloth and armor secondary motion must remain stable and readable.

### Weapons / props
- preserve the approved weapon family, scale, silhouette, and left/right carry layout;
- weapon grip points must support actual combat usage;
- two-handed weapons must be rigged and animated as two-handed weapons;
- Cards/books/staves/bows/quivers/shields/foci should use stable attachment points;
- gameplay-equipment variation must not rewrite a character's locked neutral identity.

## 6. Diyse runtime material treatment

Translate B00's graphic seinen/anime rendering into real-time materials rather than photoreal PBR.

Required behavior:
- graphic cel-informed value grouping;
- roughly 2–4 dominant light/value bands where useful;
- rich but controlled color;
- simplified material response;
- selective crisp metal highlights;
- cloth/leather less reflective than metal;
- no glossy mobile-gacha plastic look;
- no photoreal texture noise;
- no random grunge/speckle used as detail.

### Outline / ink treatment

The runtime line solution should reproduce the **rhythm** of chaotic variable line weight rather than literally drawing every master-art stroke.

Prefer:
- strongest outer silhouette;
- heavier marks at major overlaps and deep occlusion;
- thinner/selective interior accents;
- camera-aware line width;
- authored masks/weight maps where useful;
- optional authored texture/decal ink accents for signature features;
- no uniform outline around every polygon edge.

A hybrid silhouette-line plus authored-interior-ink solution is allowed.

## 7. Field presentation validation

Validate at the actual exploration camera and target display resolution.

A field model passes when:
- identity is immediate from silhouette and palette;
- head/hair mass remains readable;
- major coat/cape/ghillie/skirt shapes survive;
- signature weapon/prop remains readable when normally shown;
- line treatment does not shimmer or collapse into noise;
- small accessories do not become distracting flicker;
- animation remains readable in representative environments.

Use LOD/material simplification rather than a separate sprite identity.

## 8. Battle presentation validation

Validate at the actual battle camera and target display resolution.

A battle model passes when:
- stance and weapon silhouette are immediately readable;
- face/hair identity survives at intended distance;
- major material divisions remain clear;
- attack anticipation, impact, hit reaction, and recovery remain readable;
- armor/cloth/hair secondary motion does not obscure action;
- VFX overlap does not erase silhouette or status readability;
- outline/material treatment remains stable during animation.

## 9. Animation / rig validation

The prototype rig solution must pass:
- clean Godot import and skeleton/rest-pose inspection;
- animation visibility/import checks;
- non-root-motion vs root-motion comparison;
- idle, walk, run, turn, and direction-change behavior;
- battle-ready/idle;
- basic attack appropriate to equipped weapon;
- hit reaction;
- defend/guard where applicable;
- ability/casting action;
- KO/downed state;
- compatible female-proportion retarget test;
- extension-library animation test;
- exploration/combat transition behavior where the same rig is reused.

Retargeted motion is not automatically final. Check each clip for Diyse character weight, weapon logic, foot contact, hand placement, and silhouette.

## 10. Character-specific runtime stress tests

### Cyanis
Test royal-blue/black cloth vs layered silver armor separation, long split outer-garment motion, and mobile battle-knight readability.

### Ilyra
Test pale-value readability, the current neatly tied-back shorter blonde-hair silhouette, pale-blue cape motion, natural slightly athletic proportions, and Wardrod/Shield/Focus attachment logic without sword drift. The v0.7 proof mesh's older long-hair volumes are deformation infrastructure, not current visual authority.

### Torren
Test back-mounted bow, exact right-hip arrow draw/quiver layout, mixed-foliage ghillie silhouette, field gear, and foliage secondary motion without alpha-card noise.

### Nimera
Test short purple locs/twists, white sleeveless clothing/trousers, black harness/belt/glove/boot utility masses, the darker purple waist drape, and the hip book/Cardweaver prop without clipping or noisy motion. Do not restore the retired braided/updo or constellation-drape silhouette.

### Vaelira
Test shoulder-length crimson/burgundy hair, emerald/black/silver garment separation, the staff-free default silhouette from the exact current master, and vivid caster readability. Separately test Arcane Staff attachment/handling when the gameplay loadout displays an equipped staff. **No archer/ranger cues or bow animations.**

### Seyrik
Test broad muscular proportions, black/deep-charcoal entity-inspired gothic plate, deep-red coat/collar accents, the locked reduced-shine material treatment, and oversized two-handed greatsword handling. Do not restore older glossy rib-shell armor or a bright chest-light treatment.

## 11. B00 model-validation sequence

Completed:
1. lock the six current repository masters as character identity authority;
2. align the six visual-lock documents and character authority index;
3. verify the Quaternius-compatible UAL humanoid source;
4. import the non-root-motion UAL path into Godot and merge UAL1 + UAL2 animation libraries;
5. prove the compatible female/shared-skeleton path;
6. prove the unchanged 65-bone UAL core plus 35 appended auxiliary spring bones;
7. prove staged multi-bone deformation and the Ilyra v0.7 seam-repaired replacement-shell path.

Next:
8. bring the Ilyra proof shell toward the **current exact master** rather than its older proof appearance: exact face likeness, neatly tied-back shorter hair, final gear shapes, UVs and materials;
9. resolve remaining hard-gear/tabard intersections, weighting issues and final spring tuning;
10. complete the explicit root-motion comparison/policy decision where production movement needs it;
11. validate a B00-faithful production model/material treatment at the actual field camera;
12. validate the same model at the actual battle camera;
13. test representative exploration/battle animation plus B01 stone, B03 foliage, B10 props and B06 VFX overlap;
14. correct shader/outline/LOD/rig issues;
15. propagate only the proven model/material/rig grammar across all six;
16. compare all six together for silhouette, palette, canonical height, scale and animation separation;
17. close B00 only when the runtime models visibly reproduce their current masters and belong to the same game.

## 12. Technical and visual pilots

The shared UAL technical-rig foundation is already proven in Godot, and Ilyra v0.7 is the current deformation-focused replacement-shell pilot.

For full B00 **style/material fidelity**, **Cyanis** remains the preferred first character target because his blue/black cloth plus silver armor provides a clean material/outline baseline. His actual model must be built from `asset_sources/characters/current/cyanis.jpg`, not from the mannequin or an older Cyanis render.

Ilyra's current v0.7 proof should continue as the deformation/secondary-motion track while its visible model is corrected toward the exact current Ilyra master.

## 13. Asset Forge / Godot boundary

Asset Forge's glTF/material renderer can support deterministic source and material review, but it is not the final Godot renderer. Final character motion, retargeting, skin deformation, shader behavior, outlines, camera distance, lighting, shadows, secondary motion, and VFX overlap must be validated in Godot.

Do not mistake a successful offline render for final runtime approval.

## 14. Gate

Current B00 gate:

`6/6 CURRENT REPOSITORY MASTERS LOCKED → UAL GODOT FOUNDATION PROVEN → ILYRA v0.7 DEFORMATION TEST ACTIVE → CURRENT-MASTER VISUAL CORRECTION → ROOT-MOTION POLICY + FINAL DEFORMATION TUNING → B00 MODEL/SHADER PILOT → FIELD + BATTLE CAMERA VALIDATION → B01/B03/B10/B06 CROSS-CHECK → SIX-CHARACTER RUNTIME COHESION → B00 PASS`
