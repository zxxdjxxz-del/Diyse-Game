# Diyse — Character Scale & Silhouette

**Status:** ACTIVE RUNTIME CHARACTER READABILITY AUTHORITY  
**Parent style authority:** `../DIYSE_VISUAL_STYLE_CANON.md`  
**Character identity authority:** `CHARACTERS/README.md`  
**B00 benchmark:** `BENCHMARKS/B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Runtime model gate:** `BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

The six permanent party members must remain visually separable at actual exploration and battle camera distances. **Current repository image masters control exact identity.** This file controls which large-scale reads must survive runtime simplification.

If a shorthand description here conflicts with a current repository master or its visual-lock document, follow the authority order in `CHARACTERS/README.md` rather than this shorthand.

## Runtime representation

Primary field and battle presentation uses **rigged 3D character models** when the production rig/model solution passes B00 validation.

The former fixed sprite targets of approximately 200–220 px for battle and ~80 px for field are retired as required production targets. They may still be useful only as historical screen-space references; they do not require dedicated sprite redraws and do not define character identity.

Runtime readability must instead be tested at:
- actual target display resolution;
- actual field camera distance/framing;
- actual battle camera distance/framing;
- representative motion, lighting, environment, and VFX conditions.

Use mesh/material LOD, outline tuning, and authored simplification to preserve readability rather than creating separate character identities.

## Primary reads

### Cyanis
**Royal blue + black + silver mobile battle-knight.**

Preserve:
- dark royal-blue long split coat/tabard mass;
- large layered silver shoulder read;
- layered silver torso/forearm/lower-leg armor;
- black fitted underlayers and leather articulation;
- compact dark-hair head silhouette.

Do not let him become a generic silver plate knight or lose the royal-blue/black material blocks.

### Ilyra
**White/pale-blue Warden with long blonde hair and one coherent cape.**

Preserve:
- long blonde hair;
- pale-blue cape mass;
- white/pale-blue fitted clothing block;
- **vivid jade/green eyes** where camera distance permits;
- restrained silver forearm/lower-leg protection;
- slightly athletic natural body proportions rather than an exaggerated narrow-waist silhouette.

Her contextual runtime equipment follows gameplay canon: Wardrod primary, with Shield or Focus where equipped. Do not introduce a sword identity.

### Torren
**Forest-green veteran ranger + golden-bronze medium armor + irregular mixed-foliage ghillie mantle.**

Preserve:
- rugged age-42 veteran head/face silhouette;
- forest/army-green clothing mass;
- golden-bronze rigid medium armor on the torso/shoulders and other major protected areas shown by the master;
- dark field-leather belts, harnessing, pouches, gloves, and boots;
- bow carried on the back;
- right-hip arrow draw/quiver layout exactly as established by the master;
- utility canister/pouch rhythm where screen distance permits;
- full irregular grass/moss/leaf/twig ghillie silhouette.

At distance the ghillie mantle must resolve into several designed organic masses, not hundreds of shimmering foliage cards. Torren must read as a veteran ranger/military scout, not a druid or heavy knight.

### Nimera
**White foundation + dark-purple braided/updo silhouette + purple constellation waist mass.**

Preserve:
- dark skin;
- large dark-purple gathered/braided hair silhouette;
- white fitted clothing body block;
- dark-purple constellation garment/drape around the waist;
- black boot/utility masses;
- one strong green Cardweaver book/card cue where visible.

Do not force every braid, chain, charm, vial, or constellation mark to remain equally visible at distance. Group or fade secondary detail through LOD/material logic.

### Vaelira
**Emerald Green Arcanist + black foundation + silver accents + Arcane Staff.**

Preserve:
- crimson/burgundy hair mass;
- vivid royal/electric-blue eyes where camera distance permits;
- emerald outer-garment and boot blocks;
- black fitted foundation layer;
- silver trim/metal highlights;
- tall Arcane Staff silhouette with emerald/teal crystal focus.

**Vaelira is not an archer.** Do not introduce bow, quiver, ranger, or bow-animation language in any runtime model or animation set.

### Seyrik
**Massive black/crimson Black Host heavy silhouette + oversized greatsword.**

Preserve:
- broad muscular proportion;
- short blond-hair head silhouette;
- scarred severe face where camera distance permits;
- red/black long outer-garment mass as shown by the master;
- polished black skeletal/rib-like armor over crimson understructure;
- sharp Black Host plate rhythm;
- unmistakably oversized two-handed greatsword.

At distance, the rib-shell should resolve into a few strong black/crimson structural bands rather than dense specular noise.

## Avoid clone drift

Do not allow:
- Cyanis and Ilyra to converge into the same pale/silver knight mass;
- Torren and Vaelira to become interchangeable green characters;
- Nimera and Vaelira to share the same caster silhouette;
- Cyanis and Seyrik to share the same armored body proportion;
- Ilyra and Vaelira to collapse into the same long-haired light-caster silhouette;
- Torren's ghillie irregularity to disappear into an ordinary cape;
- Torren's medium-armor ranger construction to drift into robes or heavy plate;
- Seyrik's greatsword and Black Host heavy armor to shrink into conventional knight proportions.

Color supports recognition. **Silhouette, weapon/prop, hair mass, outer-garment shape, and body proportion must still work in grayscale.**

## Screen-space simplification hierarchy

When the runtime model becomes visually dense at distance, preserve in this order:
1. overall body/outer-garment silhouette;
2. weapon or signature prop silhouette;
3. hair mass and head shape;
4. dominant palette blocks;
5. major armor/material separations;
6. one or two signature secondary accents;
7. only then small ornament.

If a small detail competes with silhouette, shimmers, aliases, clips, or becomes unreadable at runtime, reduce it through LOD/material/outline treatment rather than preserving it literally.

## Identity-reference rule

Do not build runtime character identity from this document alone. For each character:
1. open the current repository master image;
2. open the matching current visual-lock document;
3. use this file only to decide what must remain readable after runtime simplification.

Do not use another party member's master as a subject reference. Other approved characters may guide shared B00 technique only.

## Camera validation rule

A character model is not approved from a close neutral render alone.

For each party member validate:
- neutral studio/model-review camera against the exact current master;
- field exploration camera while idle and moving;
- battle camera while idle and attacking;
- representative bright and dark lighting;
- representative environment contrast;
- VFX overlap;
- grayscale silhouette comparison with the other five party members.

B00 runtime approval requires all six to remain distinct under these real presentation conditions without altering their master identities.
