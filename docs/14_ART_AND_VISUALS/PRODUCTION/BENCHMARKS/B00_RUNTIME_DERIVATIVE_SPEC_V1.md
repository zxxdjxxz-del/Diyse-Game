# Diyse — B00 Runtime Character Derivative Spec v1

**Status:** **LOCKED FOR FIRST EXECUTION PASS**  
**Parent benchmark:** `B00_PARTY_CHARACTER_STYLE_ANCHOR_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Scale authority:** `../CHARACTER_SCALE_AND_SILHOUETTE.md`

## 1. Purpose

This specification defines how the six approved high-resolution B00 party masters are converted into runtime battle and field character art without losing Diyse's visual identity.

The derivative process is **not a blind resize**. Each smaller version is a controlled redraw/simplification derived from the exact approved master.

## 2. Required source authority

Every derivative must use the current fingerprinted B00 visual lock for that character. Do not regenerate from prose alone when the approved image is available.

Current lock files:
- `../CHARACTERS/CYANIS_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/TORREN_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/NIMERA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/VAELIRA_CURRENT_VISUAL_LOCK.md`
- `../CHARACTERS/SEYRIK_CURRENT_VISUAL_LOCK.md`

## 3. Battle derivative

**Target display height:** approximately **200–220 px**.

Battle art should retain enough detail to support expressive combat animation while remaining clear against HD-2D environments and VFX.

### Preserve
- exact character silhouette and body proportion;
- major hair masses and face read;
- signature weapon/prop shape;
- dominant garment blocks;
- major armor/material divisions;
- strongest palette relationships;
- a reduced but visible thick/thin ink rhythm;
- 2–4 designed value groups;
- one or two signature secondary details.

### Simplify/remove
- tiny chains, rivets, buttons and fasteners that alias;
- hair micro-strands;
- dense armor filigree;
- tiny constellation marks;
- individual ghillie leaves/grass blades;
- tiny crystalline facets;
- decorative edge stitching;
- random texture breakup.

### Line treatment
- silhouette line remains strongest and most irregular;
- weapon and major overlap lines medium-heavy;
- facial/interior marks thin and selective;
- broken/tapered contours remain visible but cannot become pixel noise;
- do not outline every armor plate or fold.

### Shading
- preserve graphic cel-informed light/shadow grouping;
- merge close values that become indistinguishable at runtime;
- keep metal highlights sharp and selective;
- cloth must remain visibly less reflective than metal;
- no soft airbrush or glossy gacha treatment.

## 4. Field derivative

**Target display height:** approximately **80 px**.

Field art is a deliberate iconographic version of the approved character, not a miniature illustration.

### Preserve
- outer silhouette;
- head/hair shape;
- dominant palette blocks;
- iconic weapon/prop when normally visible;
- major coat/cape/ghillie/skirt mass;
- major body proportion differences;
- 1–3 deliberate heavy ink accents.

### Aggressively simplify
- faces to a few controlled marks;
- armor to broad plates/value bands;
- accessories to one grouped cue;
- chains/charms/ornament to simple silhouette accents or omit them;
- hair subdivisions to large locks/masses;
- material texture to near-zero unless needed for identification.

Field derivatives must still identify all six party members in grayscale silhouette tests.

## 5. Character-specific simplification rules

### Cyanis
Battle: preserve bilateral shoulders, angular silver chest/forearm/lower-leg structure and royal-blue longcoat.  
Field: royal-blue body/coat block + silver shoulder/chest flashes + dark hair.

### Ilyra
Battle: preserve long blonde hair, pale-blue cape, white/pale-blue body and restrained silver accents. Contextual Wardrod/Shield/Focus may appear.  
Field: blonde head mass + pale cape/body + one silver/green focal cue. Never use a sword cue.

### Torren
Battle: preserve longbow/quiver, older rugged read and ghillie cape as grouped branches/grass masses.  
Field: irregular green organic back silhouette + bow arc + bronze accent. Do not render individual foliage pieces.

### Nimera
Battle: preserve dark-purple braided/updo mass, dark skin, white body block, purple waist drape and one clear Cardweaver cue.  
Field: purple hair mass + white body + purple hip/waist mass + black boots. Omit most chains/vials/charms.

### Vaelira
Battle: preserve crimson/burgundy hair, emerald coat/skirt/boots, black bodysuit, silver accents and Arcane Staff.  
Field: crimson hair + emerald outer silhouette + black core + staff line. **No bow/quiver/ranger language.**

### Seyrik
Battle: preserve broad muscular scale, red-dominant coat, black skeletal/rib armor with crimson recesses and oversized two-handed greatsword.  
Field: largest/heaviest party silhouette, red coat mass + black armor core + huge sword. Simplify biomechanical ribs to a few hard bands.

## 6. Shared pose / framing rules

For comparison sheets and first validation:
- use neutral standing/ready poses rather than action poses;
- keep camera angle and apparent scale consistent across the party;
- do not use turnarounds or multi-view character sheets as the approval target;
- use a clean transparent or plain neutral background for source review;
- do not add environmental lighting until the neutral derivative itself passes.

Once neutral derivatives pass, test scene lighting separately.

## 7. Validation sequence

For each character:
1. derive battle-scale art from the exact master;
2. review at native display size, not only zoomed in;
3. run silhouette/grayscale check;
4. correct aliasing and lost signature cues;
5. derive field-scale art from the approved battle/master read;
6. review at native display size;
7. compare beside all other party members;
8. then test against B01 stone, B03 foliage and B10 props;
9. test representative B06 VFX overlap;
10. approve or revise.

## 8. Party-wide pass criteria

B00 derivative execution passes only if:
- all six are immediately distinguishable at battle scale;
- all six remain distinguishable at field scale;
- no derivative silently changes an approved outfit, hairstyle, palette or weapon identity;
- chaotic variable line rhythm survives without becoming noisy;
- no painterly or glossy-gacha drift appears;
- materials remain readable;
- characters remain stronger visual anchors than backgrounds;
- VFX can overlap without destroying silhouette or status readability.

## 9. First execution order

Use this order for the first derivative pass:
1. **Cyanis** — clean baseline for armor/cloth simplification;
2. **Torren** — stress-test irregular foliage and bow silhouette;
3. **Nimera** — stress-test dense accessories/hair simplification;
4. **Vaelira** — stress-test caster/staff and emerald/black layering;
5. **Seyrik** — stress-test dense biomechanical plate and oversized weapon;
6. **Ilyra** — finalize pale-value/cape readability once the shared contrast range is established.

This order is for production testing only and does not imply character priority in canon.

## 10. Gate

Current gate:

`6/6 HIGH-RES MASTERS LOCKED → RUNTIME DERIVATIVE SPEC LOCKED → BATTLE DERIVATIVE EXECUTION NEXT`
