# Diyse — B10 CC0 Prop Cluster Benchmark Execution v1

**Benchmark:** B10 — Verified CC0 Prop Cluster  
**Status:** SOURCE ANALYSIS COMPLETE / STYLE STUDY READY  
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

### Verified archive paths

`Barrel`
- `Exports/FBX/Barrel.fbx`
- `Exports/glTF/Barrel.gltf`
- `Exports/glTF/Barrel.bin`
- `Exports/OBJ/Barrel.obj`
- `Exports/OBJ/Barrel.mtl`

`Chair_1`
- `Exports/FBX/Chair_1.fbx`
- `Exports/glTF/Chair_1.gltf`
- `Exports/glTF/Chair_1.bin`
- `Exports/OBJ/Chair_1.obj`
- `Exports/OBJ/Chair_1.mtl`

`Lantern_Wall`
- `Exports/FBX/Lantern_Wall.fbx`
- `Exports/glTF/Lantern_Wall.gltf`
- `Exports/glTF/Lantern_Wall.bin`
- `Exports/OBJ/Lantern_Wall.obj`
- `Exports/OBJ/Lantern_Wall.mtl`

`Workbench`
- `Exports/FBX/Workbench.fbx`
- `Exports/glTF/Workbench.gltf`
- `Exports/glTF/Workbench.bin`
- `Exports/OBJ/Workbench.obj`
- `Exports/OBJ/Workbench.mtl`

## 2. Verified technical observations

Approximate triangle counts from the glTF indexed primitives:
- `Barrel`: **824 triangles**;
- `Chair_1`: **496 triangles**;
- `Lantern_Wall`: **2,822 triangles**;
- `Workbench`: **1,368 triangles**.

Material usage:
- `Barrel`: furniture + metal trim materials;
- `Chair_1`: furniture + metal trim materials;
- `Lantern_Wall`: metal trim material;
- `Workbench`: furniture + metal trim materials.

Shared texture families visible in the glTF exports include:
- `T_Trim_Furniture_BaseColor.png`;
- `T_Trim_Furniture_Normal.png`;
- `T_Trim_Furniture_ORM.png`;
- `T_Trim_Metal_BaseColor.png`;
- `T_Trim_Metal_Normal.png`;
- `T_Trim_Metal_ORM.png`.

Verified shared texture dimensions:
- all six listed furniture/metal texture maps: **2048×2048 RGB**.

The pack therefore uses shared trim/material atlases rather than unique bespoke texture sets for every prop. This is efficient for production, but it also creates the main B10 challenge: Diyse must impose a stronger unified painterly/ink identity without destroying the useful shared-material workflow.

## 3. What B10 must prove

B10 is not primarily a polygon-count benchmark. It tests whether a clean-provenance 3D asset can sit beside Diyse's painterly 2D/HD-2D environment art without reading as an imported low-poly prop pack.

The benchmark must prove:
- geometry can be retained where useful;
- shared trim textures can be repainted/rebuilt into the Diyse material grammar;
- variable line-weight influence can be introduced selectively without putting a uniform black outline around the whole model;
- wood and metal remain instantly readable;
- scene lighting still behaves correctly;
- the result stays economical enough to reuse across many props.

## 4. Geometry policy

Because this source is verified CC0, direct geometry modification is allowed.

Preferred order:
1. preserve good silhouettes and useful proportions;
2. remove or simplify geometry that creates noisy tiny features at gameplay distance;
3. exaggerate only high-value silhouette features needed for readability;
4. add Diyse-specific geometry only where it meaningfully changes identity or function;
5. avoid remodelling every acceptable prop from zero merely to claim originality.

### Prop-specific geometry pressure

**Barrel**
- preserve strong cylinder/barrel read;
- ensure hoops and rim remain visible at field scale;
- avoid excessive stave segmentation.

**Chair_1**
- preserve readable back/seat/leg silhouette;
- simplify small trim if it disappears at gameplay scale;
- use silhouette and wood-plane rhythm rather than micro-carving.

**Lantern_Wall**
- preserve bracket + lamp silhouette;
- ensure emissive focal area is obvious;
- avoid overly intricate metal line noise around the light source.

**Workbench**
- preserve broad work surface, supports, storage/tool function;
- control clutter density;
- make the main horizontal work plane read before small attached detail.

## 5. Diyse 3D prop rendering grammar — draft lock

### Silhouette
- clean, strong readable outer shape;
- selected asymmetry/wear where appropriate;
- no universal toon-outline shell around every model.

### Painterly surface
- broad hand-painted material planes;
- controlled value grouping;
- restrained texture noise;
- wear concentrated at handling/contact/damage zones;
- no photo-real material breakup.

### Chaotic variable line influence
For 3D props, the line language may come from a combination of texture paint, decals, selective shader treatment, and authored edge accents.

Use strongest dark accents at:
- deep construction joints;
- underside overlaps;
- metal/wood contact points;
- damaged edges;
- selected silhouette turns;
- recessed panel lines.

Use lighter/broken marks at:
- shallow grain;
- minor wear;
- light-facing trim;
- non-focal surface articulation.

Do not:
- outline every polygon edge;
- use a constant-width black post-process outline on all props;
- darken every UV seam;
- let edge ink overpower material color.

## 6. Wood grammar for B10

Wood should use:
- broad grain direction following form;
- 3–4 large value families;
- selective darker grooves at construction joints;
- restrained worn highlights on handled edges;
- occasional irregular ink-like grain accents;
- no dense realistic pore/noise field.

The barrel, chair, and workbench must visibly share the same wood family without becoming identical brown objects.

## 7. Metal grammar for B10

Metal should use:
- clear plane changes;
- stronger value contrast than wood;
- selective sharp highlights;
- dark joint/overlap accents;
- restrained scratches/dings;
- no mirror-realistic reflections;
- no uniform black outline.

Metal hoops, brackets, fasteners, and lantern structure should read immediately against wood or background materials.

## 8. Lantern emissive rule

`Lantern_Wall` adds an emissive test to B10.

Requirements:
- bright core remains mostly free of dark linework;
- surrounding metal may carry stronger silhouette/joint ink;
- warm light spill must feel integrated with the HD-2D scene;
- bloom remains restrained;
- the lamp must still read when the scene is bright enough that emissive intensity is reduced.

## 9. Shared trim-texture strategy

The existing shared furniture and metal atlas approach is worth preserving conceptually.

B10 should test a **Diyse shared material atlas** rather than forcing unique 2K textures for every prop.

Potential production structure:
- shared `Diyse_Furniture_BaseColor`;
- shared `Diyse_Furniture_Normal` or simplified normal treatment where useful;
- shared `Diyse_Furniture_ORM`;
- shared `Diyse_Metal_BaseColor`;
- shared `Diyse_Metal_Normal`;
- shared `Diyse_Metal_ORM`;
- optional small prop-specific overlay/decal atlas for wear, symbols, faction treatment, or unique paint.

This keeps prop reuse scalable while allowing a strongly authored visual identity.

## 10. Required B10 style-study outputs

Before B10 can become STYLE-PASS, produce:

1. **Four-prop neutral-light lineup** — Barrel, Chair_1, Lantern_Wall, Workbench.
2. **Source-like vs Diyse target comparison** — prove the imported-pack look has been removed.
3. **Wood material study** — broad painterly grain + line accents.
4. **Metal material study** — selective highlights + dark joint accents.
5. **Outline comparison** — no outline / selective Diyse edge treatment / uniform toon outline (reject).
6. **Gameplay-scale prop cluster** — props integrated into a small interior/exterior scene.
7. **Lighting comparison** — neutral day/interior + warm lantern/torch + cool/night.
8. **Lantern emissive close-up** — verify clean bright core and restrained bloom.
9. **Reuse proof** — same Diyse shared wood/metal material family applied coherently across all four assets.

## 11. Gameplay readability gate

At normal exploration scale:
- Barrel reads as barrel;
- Chair reads as chair;
- Wall lantern reads as a light source;
- Workbench reads as a work surface/station;
- props do not become black silhouettes;
- texture marks do not shimmer;
- prop contrast does not compete with the player unless intentionally interactable;
- material identity survives scene lighting.

## 12. Originalization and direct-use policy

Unlike Lane B extracted reference assets, these verified CC0 props **may become direct final Diyse production assets after modification and review**.

Possible outcomes:
- geometry retained + full Diyse material repaint;
- geometry modified + Diyse material repaint;
- prop-specific Diyse additions;
- replacement only when source geometry is insufficient for the required role.

The objective is efficient authorship, not unnecessary asset replacement.

## 13. B10 acceptance checklist

B10 passes only when:

- [ ] all four props feel native to the same Diyse scene;
- [ ] wood family is painterly, readable, and non-photoreal;
- [ ] metal family is crisp without glossy realism;
- [ ] chaotic line influence is visible but selective;
- [ ] no uniform toon outline dominates;
- [ ] shared material approach remains viable;
- [ ] Lantern_Wall emissive behavior works in bright and dark scenes;
- [ ] gameplay-scale silhouettes remain clear;
- [ ] prop detail stays subordinate to player/readability needs;
- [ ] provenance remains recorded as verified CC0;
- [ ] pipeline can scale to the larger 94-prop verified CC0 library.

## 14. Production decision

**B10 source analysis is complete and the benchmark is ready for visual style-study generation.**