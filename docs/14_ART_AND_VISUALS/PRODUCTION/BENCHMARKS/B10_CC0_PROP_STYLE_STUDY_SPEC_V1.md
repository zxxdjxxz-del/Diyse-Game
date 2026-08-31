# Diyse — B10 CC0 Prop Style Study Specification v1

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** SHARED-MATERIAL STYLE STUDY LOCKED / REAL OUTPUT PENDING  
**Execution authority:** `B10_CC0_PROP_CLUSTER_EXECUTION_V1.md`  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`

## 1. Purpose

B10 establishes how verified-CC0 3D props are integrated into Diyse's painterly seinen HD-2D language without relying on a universal toon-outline effect.

Representative objects:
- Barrel;
- Chair_1;
- Lantern_Wall;
- Workbench.

The actual glTF dependency graph proves these four objects share only two BaseColor style targets:
- `T_Trim_Furniture_BaseColor.png`;
- `T_Trim_Metal_BaseColor.png`.

Therefore B10 is a **shared-material style pilot**, not four unrelated prop generations.

## 2. Required transformation

A valid B10 result must visibly move the existing CC0 material presentation toward Diyse through:
- broad painterly value grouping;
- authored edge wear/contact shadow;
- selective chaotic variable-line influence at joints, recesses, damage, and focal silhouette turns;
- controlled metal highlights;
- reduced high-frequency noise;
- one coherent furniture/wood family across Barrel, Chair_1, and Workbench;
- one coherent metal family across all metal-using props;
- compatibility with HD-2D scene lighting.

Source geometry may remain where useful. Pointless remodelling is not required.

## 3. Shared Furniture BaseColor target

The Furniture trim must use:
- broad grain direction following form;
- grouped warm/cool brown values rather than flat brown;
- selective dark joints/contact seams;
- restrained edge wear;
- occasional broken ink-like grain accents;
- no photographic pore/noise field;
- no uniform dark line around every UV island.

Because one trim serves multiple objects, the paint must remain general enough to work across barrel staves, chair parts, and workbench surfaces while still carrying clear Diyse identity.

## 4. Shared Metal BaseColor target

The Metal trim must use:
- clear plane-value separation;
- stronger highlights than wood;
- dark overlap/contact accents;
- restrained scratches/dings;
- painterly, non-photoreal reflection language;
- selective sharp highlights;
- no universal black contour shell;
- enough flexibility to work on hoops, fasteners, brackets, and lantern structure.

## 5. Normal / ORM isolation rule

For the first real B10 pilot:
- keep the original Furniture and Metal Normal maps;
- keep the original Furniture and Metal ORM maps;
- alter only the two BaseColor trims;
- render the actual four glTF models with the new BaseColor sheets;
- judge whether source Normal/ORM response still fits the new painterly appearance.

Do not rebuild Normal/ORM maps unless the real rendered result proves they are a problem.

## 6. Edge/line treatment gate

### Too clean
- generic imported-game material;
- no authored dark rhythm;
- sterile/plastic read.

### Diyse target
- selective thick-to-thin accents at meaningful joints/overlaps;
- broken/tapered surface marks;
- painterly material planes dominate;
- silhouette stays readable without a total outline.

### Too heavy
- constant-width black outline;
- every mesh edge emphasized;
- comic/toon shell dominates material;
- clutter at gameplay scale.

Only the middle treatment passes.

## 7. Prop-specific validation

### Barrel
- round silhouette remains immediate;
- staves group into broad masses;
- hoops remain readable without turning into black bands;
- wear concentrates at rim/base/handling zones.

### Chair_1
- back/seat/leg silhouette reads immediately;
- material plane changes provide structure;
- tiny trim may simplify at gameplay scale.

### Lantern_Wall
- bracket + light-source silhouette remains immediate;
- bright core stays mostly free of dark linework;
- metal carries selective joint/edge accents;
- warm spill and bloom remain restrained.

### Workbench
- broad work surface reads first;
- supports/storage read second;
- small clutter remains subordinate;
- handling wear concentrates on work-contact zones.

## 8. Required real-output evidence

A valid B10 result must be assembled from actual generated/material-applied outputs, not an AI-authored infographic.

Required evidence:
1. styled Furniture BaseColor trim;
2. styled Metal BaseColor trim;
3. neutral Barrel render;
4. neutral Chair_1 render;
5. neutral Lantern_Wall render;
6. neutral Workbench render;
7. four-prop neutral lineup;
8. warm-light cluster;
9. cool/night cluster;
10. lantern emissive close-up;
11. gameplay-scale workshop/interior cluster;
12. deterministic Asset Forge review sheet showing exact files/status/QA;
13. reuse proof showing that only the two shared BaseColor trims were changed.

## 9. Automatic rejection conditions

Reject if:
- props still look generic with only a hue shift;
- universal black outlines surround the models;
- texture noise is photoreal/high-frequency;
- material color is flat/plastic;
- lantern bloom hides fixture geometry;
- wood and metal are hard to distinguish;
- prop detail overwhelms the player/route;
- the treatment breaks when reused across multiple geometries;
- alternate lighting destroys material identity;
- the workflow silently introduces unique per-prop textures without a justified need.

## 10. Gameplay requirement

At normal exploration scale:
- object function is immediate;
- wood/metal separation survives downscale;
- edge accents do not shimmer;
- ordinary props remain subordinate to character/route readability;
- intentionally interactable props may use controlled focal contrast.

## 11. Promotion rule

Current state:

`SOURCE ANALYSIS → SHARED-MATERIAL STUDY LOCKED → TWO-BASECOLOR REAL OUTPUT PENDING`

Do not promote B10 to STYLE-PASS until the two shared BaseColor trims have been applied to the four actual models and the resulting real renders pass this gate.