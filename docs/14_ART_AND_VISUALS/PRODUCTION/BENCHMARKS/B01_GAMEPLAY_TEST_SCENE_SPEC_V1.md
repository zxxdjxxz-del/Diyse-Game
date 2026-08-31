# Diyse — B01 Stone Gameplay Test Scene Specification v1

**Benchmark:** B01 — Stone / Fortified Exterior  
**Status:** ACTIVE GAMEPLAY TEST SPEC  
**Stone kit:** `B01_DIYSE_ORIGINAL_STONE_KIT_SPEC_V1.md`  
**Style pass:** `B01_STONE_STYLE_PASS_CANDIDATE_V1.md`

## 1. Purpose

This scene is the final validation gate between an approved art-direction study and an accepted production material.

It must prove that the B01 stone grammar works at real exploration scale, under real HD-2D depth/lighting pressure, without losing navigation readability or becoming visually noisy.

## 2. Scene footprint

Use one compact fortified ruin/courtyard test area with approximately three visual depth bands:

- foreground obstruction/ledge;
- playable middle-ground route;
- background wall/ruin mass.

The scene is not intended to be a canon location. It is a neutral production proving ground.

## 3. Required geometry/modules

The proof scene must visibly use:

- 2 straight wall variants;
- 1 damaged wall variant;
- 1 inner corner;
- 1 outer corner;
- 1 broken wall end;
- 1 floor/paving family;
- 1 ledge/cap family;
- 1 short stair/elevation change;
- 1 arch or door surround;
- 1 pillar/abutment;
- 2 rubble clusters with different silhouettes;
- 1 moss/ground transition;
- 1 foreground stone element;
- 1 background stone mass.

## 4. Required composition

The playable route must be readable within one glance.

Include:
- a clear entrance/read direction;
- one turn in the route;
- one elevation change;
- one intact architectural zone;
- one visibly damaged/ruined zone;
- one quiet low-detail area to prevent uniform visual density;
- one focal stone structure, preferably the arch/pillar area.

## 5. Character-scale reference

Place one representative field-scale character or neutral proxy on the route.

The character must remain more visually important than ordinary wall microdetail.

If stone cracks, moss, or mortar compete with the character silhouette at normal field scale, B01 fails the readability gate.

## 6. Lighting tests

### Test A — Neutral daylight

Purpose: judge material and linework without dramatic lighting masking problems.

Requirements:
- readable midtones;
- visible but subordinate chaotic line weight;
- clear wall/floor separation;
- no crushed recesses;
- moss remains secondary.

### Test B — Warm torch / fire

Purpose: test strong local warm light against cool-neutral masonry.

Requirements:
- warm focal area without orange-washing the entire scene;
- deep joints gain weight naturally;
- painterly planes remain visible;
- linework does not double up with lighting shadow into black mush.

### Test C — Cool night / moon

Purpose: test dark-scene navigation.

Requirements:
- path edges remain legible;
- wall silhouette remains strong;
- foreground/background depth survives;
- stone does not collapse into one dark mass;
- selective highlights remain controlled.

## 7. Camera/readability tests

Review at:

1. normal gameplay camera;
2. 75% of normal displayed size;
3. 50% of normal displayed size;
4. close-up inspection.

The scene must still preserve:
- route read;
- wall/floor distinction;
- elevation read;
- intact-vs-damaged distinction;
- main focal structure;
- character silhouette.

Microdetail is allowed to disappear as scale decreases.

## 8. Line-density zones

The scene must deliberately include three line-density bands.

### Quiet zone
- light-facing intact masonry;
- minimal fractures;
- mostly painterly planes.

### Normal zone
- standard joints;
- selected broken interior strokes;
- moderate hand-drawn irregularity.

### High-energy zone
- rubble/damage focal area;
- deeper black clusters;
- more fracture convergence;
- heavier silhouette breakup.

The high-energy zone must remain localized. If every area reads like the damage focal zone, B01 fails.

## 9. Repetition test

No two adjacent repeated modules should reveal an obvious stamped pattern.

Break repetition through:
- module alternates;
- damage inserts;
- offset joins;
- moss variation;
- rubble placement;
- lighting;
- occasional silhouette changes.

Do not solve repetition with high-frequency noise.

## 10. HD-2D depth test

Use at least:
- foreground occlusion;
- midground playable layer;
- background stone mass;
- mild atmospheric depth separation;
- selective depth-of-field or focus falloff if consistent with current runtime presentation.

Stone silhouette and navigation must remain readable after these effects are applied.

## 11. Pass/fail checklist

B01 gameplay proof passes only if all are true:

- [ ] route reads before surface detail;
- [ ] player/proxy remains visually dominant over ordinary masonry;
- [ ] walls, floors, stairs, and ledges separate instantly;
- [ ] damaged masonry is distinct without dominating the entire scene;
- [ ] chaotic variable line weight survives normal scale;
- [ ] linework remains subordinate to structural form;
- [ ] quiet/normal/high-energy line-density zones are visibly different;
- [ ] repeated modules do not look stamped;
- [ ] moss is integrated and secondary;
- [ ] neutral daylight works;
- [ ] warm torch light works;
- [ ] cool night light works;
- [ ] dark areas remain navigable;
- [ ] foreground/background depth remains readable;
- [ ] no photo-noise dependence appears after compositing;
- [ ] scene reads as Diyse-native rather than Map086-derived.

## 12. Acceptance outcome

If all checks pass:

`B01 → ACCEPTED`

Then extract the tested rules into **Diyse Visual Material Grammar v1 — Stone** and begin B03 foliage.

If any major test fails, revise the stone kit or line-density implementation before promotion. Do not weaken the overall style canon merely to rescue one failed stone implementation.
