# Diyse — B10 CC0 Prop Cluster Benchmark Execution v1

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** SOURCE ANALYSIS COMPLETE / SHARED-MATERIAL PILOT READY  
**Style authority:** `../../DIYSE_VISUAL_STYLE_CANON.md`  
**Benchmark authority:** `../STYLE_BENCHMARK_SET_V1.md`  
**Conversion pipeline:** `../ASSET_STYLE_CONVERSION_PIPELINE.md`

## 1. Source record

**Source pack:** Quaternius Fantasy Props MegaKit [Standard]  
**Provenance lane:** Lane A — verified CC0 / redistributable source.  
**Representative benchmark props:**
- `Barrel`
- `Chair_1`
- `Lantern_Wall`
- `Workbench`

The pack provides these assets in FBX, glTF, and OBJ export forms.

## 2. Verified shared-material architecture

The actual glTF files show that the benchmark is materially cheaper and more scalable than a four-prop independent-generation workflow.

Per-model BaseColor dependencies:
- `Barrel` → `T_Trim_Furniture_BaseColor.png` + `T_Trim_Metal_BaseColor.png`;
- `Chair_1` → `T_Trim_Furniture_BaseColor.png` + `T_Trim_Metal_BaseColor.png`;
- `Lantern_Wall` → `T_Trim_Metal_BaseColor.png`;
- `Workbench` → `T_Trim_Furniture_BaseColor.png` + `T_Trim_Metal_BaseColor.png`.

Therefore the four-prop benchmark has only **two unique BaseColor style targets**:
1. `T_Trim_Furniture_BaseColor.png`;
2. `T_Trim_Metal_BaseColor.png`.

The associated Normal and ORM maps remain structurally reusable during the first style pilot:
- `T_Trim_Furniture_Normal.png`;
- `T_Trim_Furniture_ORM.png`;
- `T_Trim_Metal_Normal.png`;
- `T_Trim_Metal_ORM.png`.

This changes the preferred B10 workflow from:

`4 props → 4 independent image generations`

to:

`2 shared BaseColor trims → apply to 4 actual models → validate all four together`.

The same shared-material strategy can potentially update a substantial portion of the larger 94-prop CC0 library at once.

## 3. B10 goal

B10 must prove that clean-provenance 3D geometry can sit beside Diyse's painterly HD-2D environment language without reading as an imported generic low-poly pack.

The benchmark must prove:
- useful geometry can be retained;
- shared trim textures can be repainted into the Diyse material grammar;
- variable line-weight influence can live in material paint and selective edge accents without a universal toon outline;
- wood and metal remain immediately readable;
- lighting and emissive behavior remain functional;
- one shared material treatment can scale across multiple prop geometries.

## 4. Geometry policy

Because the source is verified CC0, direct geometry modification is allowed.

Preferred order:
1. preserve useful silhouettes and proportions;
2. simplify geometry only where tiny features create gameplay-scale noise;
3. exaggerate high-value silhouette features only when readability needs it;
4. add Diyse-specific geometry when it changes identity or function;
5. do not remodel acceptable CC0 props from zero merely to claim originality.

### Representative geometry pressure

**Barrel**
- preserve cylinder/barrel read;
- keep hoops and rim visible;
- avoid excessive stave segmentation.

**Chair_1**
- preserve back/seat/leg silhouette;
- simplify tiny trim where necessary;
- rely on silhouette and material rhythm rather than micro-carving.

**Lantern_Wall**
- preserve bracket + lamp silhouette;
- keep emissive focal area obvious;
- prevent metal line noise from surrounding the bright core.

**Workbench**
- preserve broad horizontal work plane and support/storage read;
- control clutter density;
- make the work surface read before small attached detail.

## 5. Diyse shared Furniture trim target

`T_Trim_Furniture_BaseColor.png` becomes the first scalable wood/furniture style target.

Target grammar:
- painterly broad wood planes;
- 3–4 value families;
- grain follows functional direction rather than forming random noise;
- darker irregular accents at joints/recesses;
- restrained handling/wear highlights;
- occasional broken ink-like grain accents;
- no dense realistic pore field;
- no uniform black edge baking.

The Barrel, Chair, and Workbench should share this material family while still reading as different objects because geometry, UV placement, lighting, and local accent distribution differ.

## 6. Diyse shared Metal trim target

`T_Trim_Metal_BaseColor.png` becomes the scalable metal style target.

Target grammar:
- clear plane changes;
- stronger contrast than wood;
- selective sharp highlights;
- dark overlap/joint accents;
- restrained scratches/dings;
- painterly rather than photoreal reflection;
- no universal toon outline baked into every UV island.

This single trim must work on barrel hoops, chair fasteners, lantern structure, and workbench hardware.

## 7. Normal / ORM handling for first pilot

For B10 pilot v1:
- preserve source Normal maps;
- preserve source ORM maps;
- replace only the two BaseColor trims first;
- validate whether the existing geometry response and material roughness remain compatible with the new painterly BaseColor language.

Only after that test should we decide whether Diyse needs:
- softened/simplified normals;
- adjusted roughness/metallic ranges;
- custom shared Normal/ORM replacements.

This isolates visual-style changes from physically-based material changes and prevents unnecessary work.

## 8. Chaotic variable line influence on 3D props

The line identity should come mainly from painted material accents, decals, selected recess darkening, and authored edge treatment.

Strongest accents:
- deep construction joints;
- underside overlaps;
- metal/wood contact;
- damage;
- selected silhouette turns;
- recessed panels.

Light/broken accents:
- shallow grain;
- minor wear;
- light-facing trim;
- non-focal articulation.

Reject:
- every polygon edge outlined;
- constant-width black post-process outline;
- every UV seam darkened;
- ink overpowering the material colors.

## 9. Lantern emissive rule

`Lantern_Wall` remains the emissive validation object.

Requirements:
- bright core mostly free of dark linework;
- surrounding metal may carry stronger silhouette/joint accents;
- warm spill integrates with scene lighting;
- bloom remains restrained;
- lamp still reads in brighter scenes where emissive contrast is reduced.

## 10. Asset Forge implementation

Shared material analysis is implemented at:

`tools/asset_forge/shared_material_engine.py`

It can:
- inspect actual glTF dependencies in a source ZIP;
- identify unique BaseColor trim sheets;
- report which models reuse each trim;
- extract only the shared BaseColor targets needed for a bounded pilot.

For the representative B10 cluster, the expected style-generation count is **2 BaseColor image edits**, not 4 independent prop edits.

## 11. Required B10 pilot outputs

Before B10 can become STYLE-PASS, produce:

1. Diyse-styled `T_Trim_Furniture_BaseColor`;
2. Diyse-styled `T_Trim_Metal_BaseColor`;
3. Barrel rendered with both new shared trims;
4. Chair_1 rendered with both new shared trims;
5. Lantern_Wall rendered with new metal trim and emissive validation;
6. Workbench rendered with both new shared trims;
7. neutral-light four-prop lineup;
8. warm-light and cool/night scene checks;
9. gameplay-scale prop cluster;
10. deterministic review sheet from the actual outputs.

No AI-generated infographic is accepted as B10 evidence.

## 12. Gameplay readability gate

At normal exploration scale:
- Barrel reads as barrel;
- Chair reads as chair;
- Lantern reads as a light source;
- Workbench reads as a work station;
- props do not become black silhouettes;
- trim detail does not shimmer;
- prop contrast does not compete with the player unless intentionally interactable;
- wood/metal identity survives scene lighting.

## 13. Direct-use policy

These verified CC0 props may become direct Diyse production assets after modification and review.

Possible outcomes:
- geometry retained + shared Diyse material repaint;
- geometry modified + shared material repaint;
- optional prop-specific decal/overlay additions;
- replacement only when source geometry is insufficient.

The objective is efficient authorship, not unnecessary replacement.

## 14. Acceptance checklist

B10 passes only when:

- [ ] the two shared BaseColor trims are clearly Diyse-native;
- [ ] all four props feel native to the same scene;
- [ ] wood is painterly, readable, and non-photoreal;
- [ ] metal is crisp without glossy realism;
- [ ] chaotic line influence is visible but selective;
- [ ] no uniform toon outline dominates;
- [ ] existing Normal/ORM behavior remains compatible or a justified adjustment is documented;
- [ ] Lantern_Wall emissive behavior works in bright and dark scenes;
- [ ] gameplay-scale silhouettes remain clear;
- [ ] shared material strategy demonstrably scales beyond the four benchmark props;
- [ ] provenance remains verified CC0.

## 15. Production decision

**B10 shared-material source analysis is complete.**

The preferred next action is a bounded **two-BaseColor real-output style pilot**, followed by rendering the four actual glTF models with those shared trims.