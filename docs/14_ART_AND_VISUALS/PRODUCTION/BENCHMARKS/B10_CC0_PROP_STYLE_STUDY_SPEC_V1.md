# Diyse — B10 CC0 Prop Style Study Specification v1

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** STYLE STUDY SPEC LOCKED / VISUAL PASS PENDING  
**Execution authority:** `B10_CC0_PROP_CLUSTER_EXECUTION_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## 1. Purpose

B10 establishes how clean-provenance 3D props are integrated into Diyse's painterly seinen HD-2D visual language without relying on a universal toon-outline effect.

The four representative objects are:
- Barrel;
- Chair_1;
- Lantern_Wall;
- Workbench.

These objects deliberately test repeated wood/metal materials, furniture silhouettes, clutter density, and an emissive light source.

## 2. Required visual transformation

A valid B10 result must show a visible move away from generic imported low-poly presentation through:
- broad hand-painted material value grouping;
- more authored edge wear and contact shadow;
- selective chaotic variable-line influence at construction joints, deep recesses, damage, and focal silhouette turns;
- controlled highlights on metal;
- simplified texture noise;
- consistent shared wood/metal family across all four props;
- lighting integration appropriate to HD-2D scenes.

The result may retain source geometry where it already works. Style transformation does not require pointless remodelling.

## 3. Wood target

Wood must use:
- broad grain direction following form;
- grouped warm/cool brown values rather than flat brown;
- selective dark joints and contact seams;
- restrained edge wear;
- occasional irregular ink-like grain accents;
- enough variation to separate barrel, chair, and workbench while preserving one shared material family.

Reject:
- photographic wood noise;
- uniform black grain lines;
- over-carved microdetail;
- every edge receiving the same dark stroke.

## 4. Metal target

Metal must use:
- distinct plane changes;
- stronger highlight geometry than wood;
- dark recess/contact accents;
- restrained scratches/dings;
- controlled roughness;
- selected sharp highlights;
- no mirror-real rendering;
- no uniform contour shell.

## 5. Edge/line treatment test

The visual board must explicitly compare:

### Too clean
- smooth imported-game material;
- little/no authored dark edge rhythm;
- sterile digital look.

### Diyse target
- selective thick-to-thin dark accents at meaningful joints/overlaps;
- broken/tapered surface marks;
- painterly planes dominate;
- silhouette remains readable without total outline.

### Too heavy
- constant-width black outline;
- every mesh edge emphasized;
- comic/toon shell dominates material;
- clutter at gameplay scale.

The accepted direction is the middle treatment.

## 6. Prop-specific target read

### Barrel
- strong round silhouette;
- staves group into broad masses rather than many equal stripes;
- metal hoops remain visible but do not become black bands;
- wear concentrated at rim, base, handling zones.

### Chair_1
- back/seat/leg silhouette reads immediately;
- wood-plane changes provide structure;
- small trim is simplified if it vanishes at gameplay scale.

### Lantern_Wall
- bracket + light-source silhouette reads immediately;
- bright emissive core stays mostly free of dark linework;
- surrounding metal carries selective ink/joint accents;
- warm spill/bloom is restrained.

### Workbench
- broad horizontal work surface reads first;
- supports/storage read second;
- small clutter/details are subordinate;
- material wear concentrates on work/handling zones.

## 7. Required B10 visual board

A valid B10 board/result must contain:

1. `B10 — CC0 PROP CLUSTER` title.
2. Four-prop neutral-light lineup.
3. Source-like/generic vs Diyse target treatment.
4. Wood material close-up.
5. Metal material close-up.
6. Too clean / target / too heavy edge treatment comparison.
7. Gameplay-scale interior or workshop cluster containing all four props where practical.
8. Neutral/warm/cool lighting test.
9. Lantern emissive close-up.
10. Shared-material reuse diagram showing one Diyse wood/metal family serving multiple props.
11. Note that the source is verified CC0 and direct final-use modification is allowed.

## 8. Automatic rejection conditions

Reject the visual candidate if:
- props still look like generic imported low-poly assets with only a color tweak;
- a universal black toon outline surrounds every object;
- texture noise is high-frequency or photoreal;
- material color becomes flat and plastic;
- lantern bloom hides the fixture shape;
- wood and metal are hard to distinguish;
- prop detail overwhelms the player or route at field scale;
- every prop requires a unique material workflow, defeating scalable reuse;
- the treatment no longer works under alternate lighting.

## 9. Gameplay-scale requirement

At normal exploration scale, object function must remain immediately recognizable and material detail must simplify gracefully.

The player/readable route remains the priority. Interactive props may receive focal contrast intentionally; ordinary decoration must remain subordinate.

## 10. Promotion rule

Current state:

`SOURCE ANALYSIS → STYLE STUDY SPEC LOCKED → VISUAL STYLE-PASS PENDING`

Do not promote B10 until a valid prop-only visual candidate passes this specification.