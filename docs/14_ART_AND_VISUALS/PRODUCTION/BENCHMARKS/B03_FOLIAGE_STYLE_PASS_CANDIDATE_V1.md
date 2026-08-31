# Diyse — B03 Foliage Style-Pass v1

**Benchmark:** B03 — Tree / Foliage Silhouette  
**Status:** STYLE-PASS APPROVED / GAMEPLAY TEST READY  
**Approved:** 2026-08-31  
**Execution authority:** `B03_FOLIAGE_EXECUTION_V1.md`  
**Style-study authority:** `B03_FOLIAGE_STYLE_STUDY_SPEC_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## Authority note

The foliage-only benchmark board generated during the 2026-08-31 working session is accepted as the visual-direction reference for B03. Any dates, percentages, checkboxes, or status labels embedded in generated imagery are presentation text only; repository text controls actual production state.

The accepted direction establishes a Diyse-original foliage language rather than permission to reproduce or repaint Map084 directly.

## Approved foliage grammar

The B03 direction is approved with the following permanent rules:

- the full tree reads as one authored silhouette before internal detail;
- standard field trees use approximately 3–6 major canopy masses;
- asymmetry is intentional and concentrated rather than random;
- negative-space holes are designed as large readable shapes, not peppered alpha noise;
- painterly foliage masses establish the material before linework is added;
- strongest chaotic line weight is reserved for deep canopy overlaps, branch forks, damage, contact shadow, and selected silhouette turns;
- medium line weight marks selected mass overlaps and trunk plane changes;
- fine, broken, tapered marks appear on light-facing edges and minor bark/branch accents;
- linework may disappear completely in bright/open areas;
- ordinary field foliage never receives a uniform black contour;
- standard gameplay foliage is not rendered leaf-by-leaf;
- alpha edges must remain clean and stable under scaling and movement;
- foreground trees may carry the strongest line rhythm, midground trees simplify, and background trees simplify further through mass/value reduction rather than blur alone;
- nearby player-character silhouettes remain more visually dominant than ordinary tree interior detail;
- icon/map trees are dedicated compact interpretations, not blind downscales of field trees.

## Accepted visual hierarchy

### Foreground / focal foliage
- strongest silhouette accents;
- full four-value canopy structure;
- selective visible interior ink rhythm;
- controlled bark and edge detail;
- largest intentional negative spaces retained.

### Midground / normal exploration foliage
- three to four broad values;
- fewer internal lines;
- fewer alpha holes;
- strong silhouette and canopy masses dominate.

### Background foliage
- two to three value masses;
- minimal or no interior linework;
- simplified contour;
- atmospheric color/value shift;
- no tiny silhouette chatter.

## Alpha-edge lock

Final foliage assets must reject:
- dark matte fringe;
- pale halo;
- one-pixel spikes that shimmer;
- many tiny transparency holes;
- edge breakup that changes character under normal camera scaling.

Organic edge complexity must be clustered into deliberate readable groups.

## Icon-tree lock

The compact icon/map canopy uses:
- a strong simplified canopy silhouette;
- roughly 4–7 large lobes;
- three major value masses;
- one deep central/recess cluster;
- one restrained highlight cluster;
- little or no internal linework;
- selected irregular contour accents only where needed.

It should feel related to field foliage through palette, mass rhythm, and edge language, not geometry duplication.

## B03 promotion decision

The foliage visual direction has passed user review and is promoted to the provisional Diyse foliage baseline.

Current state:

`SOURCE ANALYSIS → STYLE STUDY → STYLE-PASS APPROVED → GAMEPLAY TEST READY`

B03 is **not yet final ACCEPTED**. It still requires a representative Diyse-original foliage family and gameplay/integration proof covering alpha stability, character hierarchy, route visibility, depth simplification, and lighting response.

Next production actions:
1. build the Diyse-original foliage-family kit specification;
2. define the compact gameplay test scene;
3. validate neutral/warm/cool lighting;
4. validate foreground/midground/background density tiers;
5. validate field and icon scales;
6. promote to `ACCEPTED` only if runtime proof holds.