# Diyse — Character Scale & Silhouette

**Status:** ACTIVE RUNTIME CHARACTER READABILITY AUTHORITY  
**Parent style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**B00 benchmark:** `BENCHMARKS/B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Runtime model gate:** `BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

The six permanent party members must remain visually separable at actual exploration and battle camera distances. Exact approved B00 masters control identity; this file controls what must survive runtime presentation.

## Runtime representation

Primary field and battle presentation uses **rigged 3D character models** when the production rig/model solution passes B00 validation.

The former fixed sprite targets of approximately 200–220 px for battle and ~80 px for field are retired as required production targets. They may still be useful as rough historical screen-space references, but they no longer require dedicated sprite redraws.

Runtime readability must instead be tested at:
- actual target display resolution;
- actual field camera distance/framing;
- actual battle camera distance/framing;
- representative motion, lighting, environment and VFX conditions.

Use mesh/material LOD, outline tuning and authored simplification to preserve readability rather than creating separate character identities.

## Primary reads

### Cyanis
**Royal blue + silver mobile knight.**

Preserve:
- dark royal-blue longcoat/tabard mass;
- bilateral silver shoulder read;
- angular silver torso/forearm/lower-leg armor;
- dark articulation layers;
- clean youthful dark-hair silhouette.

Do not let him become a generic silver plate knight.

### Ilyra
**White/pale-blue Warden with long blonde hair and cape.**

Preserve:
- long blonde hair;
- pale-blue cape mass;
- white/pale-blue clothing block;
- **bold saturated green eyes** where camera distance permits;
- restrained silver lower-arm/lower-leg accents.

Her contextual runtime equipment may include Wardrod, Shield or Focus. Do not introduce a sword identity.

### Torren
**Army-green tactical medium armor + golden-bronze protection + irregular ghillie cape.**

Preserve:
- older rugged veteran facial/hair read while retaining canonical age 42;
- **amber eyes** where camera distance permits;
- longbow/quiver;
- dominant army-green / olive tactical cloth block;
- golden-bronze medium armor on torso/shoulder/arms/knees/lower legs;
- brown leather belts, harness, pouches and boots;
- full irregular grass/branch ghillie-cape silhouette;
- three-canister field-gear rhythm where screen distance permits.

At distance the ghillie cape must resolve into several designed organic masses, not hundreds of shimmering foliage cards. Torren must read as a veteran military scout/archer, not a druid, court ranger or heavy knight.

### Nimera
**White foundation + dark-purple braided/updo silhouette + constellation waist mass.**

Preserve:
- dark skin;
- large dark-purple gathered/braided hair silhouette;
- white shirt/pants body block;
- dark-purple coat/drape tied around waist;
- black boot/utility masses;
- one strong green Cardweaver prop cue where visible.

Do not force every braid, chain, charm, vial or constellation mark to remain equally visible at distance. Group or fade secondary detail through LOD/material logic.

### Vaelira
**Emerald Arcanist + black foundation + silver accents + Arcane Staff.**

Preserve:
- crimson/burgundy hair mass;
- **electric blue eyes** where camera distance permits;
- emerald coat/skirt/boot blocks;
- black bodysuit foundation;
- silver trim/metal highlights;
- tall Arcane Staff silhouette and restrained emerald focus.

**Vaelira is not an archer.** Do not introduce bow/quiver/ranger language in any runtime model or animation set.

### Seyrik
**Massive black/crimson biomechanical heavy-plate silhouette + oversized greatsword.**

Preserve:
- broad muscular proportion;
- blond swept top / short sides;
- scarred severe face and blue-eye read where camera distance permits;
- red-dominant long coat mass;
- polished black skeletal/rib-cage armor over crimson understructure;
- asymmetric sharp Black Host plate rhythm;
- unmistakably oversized two-handed greatsword.

At distance, the rib-shell should resolve into a few strong black/crimson structural bands rather than dense specular noise.

## Avoid clone drift

Do not allow:
- Cyanis and Ilyra to converge into the same white/silver knight mass;
- Torren and Vaelira to become interchangeable green characters;
- Nimera and Vaelira to share the same caster silhouette;
- Cyanis and Seyrik to share the same armored body proportion;
- Ilyra and Vaelira to collapse into the same long-haired light-caster silhouette;
- Torren's ghillie irregularity to disappear into an ordinary cape;
- Torren's tactical medium-armor construction to drift back into robe-like ranger clothing;
- Seyrik's greatsword and heavy Black Host plate to shrink into conventional knight proportions.

Color supports recognition. **Silhouette, weapon, hair mass, outer garment shape and body proportion must still work in grayscale.**

## Screen-space simplification hierarchy

When the runtime model becomes visually dense at distance, preserve in this order:
1. overall body/outer-garment silhouette;
2. weapon or signature prop silhouette;
3. hair mass and head shape;
4. dominant palette blocks;
5. major armor/material separations;
6. one or two signature secondary accents;
7. only then small ornament.

If a small detail competes with silhouette, shimmers, aliases, clips or becomes unreadable at runtime, reduce it through LOD/material/outline treatment rather than preserving it literally.

## Camera validation rule

A character model is not approved from a close neutral render alone.

For each party member validate:
- neutral studio/model-review camera;
- field exploration camera while idle and moving;
- battle camera while idle and attacking;
- representative bright and dark lighting;
- representative environment contrast;
- VFX overlap;
- grayscale silhouette comparison with the other five party members.

B00 runtime approval requires all six to remain distinct under these real presentation conditions.
