# Diyse — B03 Foliage Gameplay Test Scene Specification v1

**Benchmark:** B03 — Tree / Foliage Silhouette  
**Status:** GAMEPLAY TEST SPEC READY  
**Style-pass authority:** `B03_FOLIAGE_STYLE_PASS_CANDIDATE_V1.md`  
**Original kit spec:** `B03_DIYSE_ORIGINAL_FOLIAGE_KIT_SPEC_V1.md`

## 1. Purpose

This compact proof scene determines whether the approved B03 foliage grammar survives actual HD-2D gameplay presentation. A concept board alone is not enough to mark B03 `ACCEPTED`.

## 2. Required scene composition

Build one small exploration scene containing:
- one player-character field-scale stand-in;
- one foreground/focal tree partially framing the scene;
- two midground standard trees near but not covering the route;
- one background canopy/tree cluster;
- one sapling or low foliage element;
- a clearly readable walkable route;
- a simple neutral ground material;
- enough open sky/background to expose alpha edges.

Do not use a dense forest scene for the first proof. The purpose is to isolate readability failures.

## 3. Required camera tests

Test:
- normal exploration framing;
- slight camera movement/pan;
- representative zoom or resolution scaling used by the project;
- foreground occlusion crossing the player if the runtime presentation supports it.

The test must reveal whether alpha edges shimmer or whether line detail collapses during motion.

## 4. Player-vs-tree hierarchy

At normal field scale:
- the player silhouette must remain immediately findable;
- ordinary midground foliage must not contain stronger local contrast or line density than the player;
- the foreground tree may be visually stronger at the outer silhouette, but its interior detail must not pull focus away from the playable character;
- foliage behind the character must not create a dark halo that destroys character readability.

## 5. Route-readability gate

The route must remain obvious through:
- clean ground/foliage value separation;
- controlled lower-canopy height;
- no excessive root/grass clutter at route edges;
- foreground occlusion used intentionally rather than constantly;
- background foliage not merging into walkable ground.

If the viewer has to inspect leaves to understand where to walk, B03 fails.

## 6. Alpha stability gate

During camera movement and scaling, reject any asset showing:
- dark fringe;
- pale fringe;
- one-pixel glitter;
- unstable tiny canopy holes;
- crawling outline noise;
- edge artifacts caused by inconsistent premultiplication/import settings.

Fix source art/import behavior before acceptance.

## 7. Depth-tier gate

The same foliage grammar must visibly simplify with distance.

Foreground:
- full selective line rhythm;
- strongest silhouette turns;
- four broad values.

Midground:
- fewer lines;
- reduced alpha holes;
- three to four broad values.

Background:
- little/no interior linework;
- two to three broad values;
- atmospheric color shift;
- simplified silhouette.

Do not satisfy depth differentiation with blur alone.

## 8. Lighting tests

Run at least three states on the same scene:

### Neutral day
Tests base material and alpha readability.

### Warm directional light
Tests whether light-facing canopy planes remain painterly without becoming neon yellow or losing ink hierarchy.

### Cool/night light
Tests whether foliage stays legible without becoming a single black mass.

Optional fourth state:
- local magical light or torch spill.

## 9. Icon-scale companion test

Alongside the scene, test the dedicated icon/map canopy at its intended compact size.

Pass if:
- it reads immediately as a tree/canopy;
- 3-value grouping remains visible;
- it feels visually related to the field foliage;
- no microdetail is required for recognition.

## 10. Acceptance checklist

B03 may become `ACCEPTED` only when all are true:

- [ ] player remains instantly readable;
- [ ] route remains instantly readable;
- [ ] alpha edges remain clean during movement;
- [ ] no shimmering tiny silhouette detail;
- [ ] foreground/midground/background tiers are visibly distinct;
- [ ] trees retain authored silhouettes at normal camera distance;
- [ ] linework is recognizably Diyse but subordinate to gameplay readability;
- [ ] neutral/warm/cool lighting all preserve form;
- [ ] icon-tree family match succeeds;
- [ ] original tree silhouettes do not reproduce Map084 source shapes.

## 11. Promotion rule

Current state:

`STYLE-PASS APPROVED → GAMEPLAY TEST READY`

Only successful runtime/representative integration proof advances B03 to `ACCEPTED`.