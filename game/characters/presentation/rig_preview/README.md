# UAL Rig Preview

This folder contains the staged Diyse proof-of-concepts using the actual Universal Animation Library rig rather than the abandoned 2D shader-deformation approach.

## Required UAL binary assets

Copy these three files from the supplied UAL Standard packs into:

`asset_sources/animation/ual/`

- `Mannequin_F.glb` — UAL2 `Female Mannequin/Unreal-Godot/`
- `UAL1_Standard.glb` — UAL1 `Unreal-Godot/`
- `UAL2_Standard.glb` — UAL2 `Unreal-Godot/`

The previews deliberately use the non-root-motion libraries so locomotion remains centered for inspection.

## 1. Base rig scene

Run:

`game/characters/presentation/rig_preview/ual_rig_preview.tscn`

This is the untouched female-mannequin motion proof.

## 2. Ilyra motion proxy

Run:

`game/characters/presentation/rig_preview/ilyra_ual_proxy.tscn`

This keeps the stock UAL body but adds abstract Ilyra cues: palette, hair mass, utility gear, cape, and secondary-motion direction.

## 3. Ilyra anime-body / UAL proof

Generate the reshaped body from the stock female mannequin:

`python tools/animation/generate_ilyra_anime_body_proxy.py`

This writes:

`asset_sources/animation/ual/Ilyra_AnimeBody_UAL.glb`

Then run:

`game/characters/presentation/rig_preview/ilyra_anime_body_ual.tscn`

The generator preserves the original UAL skeleton, joints, skin weights, and inverse bind matrices while making conservative surface-only proportion changes. The visible equipment is a one-handed Wardrod and shield; `Sword_Attack` is only a temporary motion donor and does not redefine Ilyra as a sword user.

## 4. Ilyra modular character blockout

Run:

`game/characters/presentation/rig_preview/ilyra_modular_blockout.tscn`

This layers B00-guided character parts over the reshaped skinned body: jade-eye face read, fitted Warden clothing, long blonde hair masses, cape, tabards, practical leather gear, light silver arm/leg guards, Wardrod, and shield.

Controls include `V` for layer comparison and `Q / E` for rotation.

## 5. Ilyra authored-geometry / UAL proof

Run:

`game/characters/presentation/rig_preview/ilyra_authored_geometry.tscn`

This replaces the most visibly primitive Stage 4 pieces with custom generated triangle meshes: an anime head surface, windswept ribbon hair, fitted Warden silhouette pieces, shaped tabards/cape, and authored Wardrod/shield forms. Stage 5 remains a rigid-attachment deformation baseline for the next stage.

Controls:

- `SPACE` next animation
- `P` pause/resume
- `V` compare authored character / skinned body
- `Q / E` rotate manually
- `T` automatic turntable
- `R` restart sequence
- `ESC` quit

See `ILYRA_AUTHORED_GEOMETRY_MANIFEST.md` for the prototype/production boundary.

## 6. Ilyra deformation-aware weighted proof

Run:

`game/characters/presentation/rig_preview/ilyra_deformation_aware.tscn`

Stage 6 keeps the exact 65-bone UAL core but changes the character parts that should flex across joints from rigid attachments to actual multi-bone vertex skinning:

- fitted Warden vest: `spine_03 → spine_02 → spine_01 → pelvis`
- blue torso center panel: same torso weighting as the vest
- long blonde hair: `Head → neck_01 → spine_03 → spine_02`
- pale-blue cape: `spine_03 → spine_02 → spine_01 → pelvis`
- front tabard: `pelvis → thigh_l + thigh_r`
- side tabards: `pelvis → matching thigh`

Hard pieces remain rigid intentionally: head shell/hair cap, collar/clasp, bracers, greaves, Wardrod, and shield.

The deformation stress loop adds crouch and roll tests alongside walk, jog, shield movement, casting, and hit reaction.

Controls:

- `SPACE` next deformation-test animation
- `P` pause/resume
- `V` authored character / underlying body comparison
- `K` Stage 6 weighted deformation / Stage 5 rigid comparison
- `Q / E` rotate manually
- `T` automatic turntable
- `R` restart sequence
- `ESC` quit

See `ILYRA_DEFORMATION_AWARE_MANIFEST.md` for the weighting plan and production boundary.

## Authority boundary

None of these proxy meshes are Ilyra appearance canon. The approved cleaned B00 image remains authoritative for her face, vivid jade eyes, windswept blonde hair, slightly athletic natural-waist proportions, fitted white/pale-blue Warden clothing, restrained decoration, brown utility gear, silver arm/leg guards, pale-blue cape, colors, silhouette, and final visible equipment design. These scenes exist to validate the UAL rig, deformation quality, animation language, character construction, and secondary-motion direction before a production 3D mesh is authored.

The UAL female mannequin and both animation libraries share the same skeleton, so animation tracks transfer directly without humanoid retargeting.
