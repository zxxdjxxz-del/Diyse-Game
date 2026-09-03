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

This keeps the stock UAL body but adds abstract Ilyra cues:

- pale ivory / pale-blue Warden palette
- silver guard/joint read
- blonde long-hair masses
- brown utility belt and pouches
- pale-blue segmented cape
- subtle procedural hair/cape follow-through

## 3. Ilyra anime-body / UAL proof

Generate the reshaped body from the stock female mannequin:

`python tools/animation/generate_ilyra_anime_body_proxy.py`

This writes:

`asset_sources/animation/ual/Ilyra_AnimeBody_UAL.glb`

Then run:

`game/characters/presentation/rig_preview/ilyra_anime_body_ual.tscn`

The generator preserves the original UAL skeleton, joints, skin weights, and inverse bind matrices while making conservative surface-only proportion changes: modest anime head enlargement, a more natural waist, subtle athletic torso/hips, and less blocky limbs.

The scene adds a visible one-handed Wardrod proxy to `hand_r` and a shield proxy to `hand_l`. Its preferred sequence is:

Idle → Walk → Jog → Shield Idle → Shield Action → Shield Dash → Wardrod strike motion donor → Warden Spell → Hit Reaction.

`Sword_Attack` is used only as a temporary animation donor for hand/body motion while the visible weapon remains a Wardrod. It does **not** redefine Ilyra as a sword user.

## 4. Ilyra modular character blockout

Run:

`game/characters/presentation/rig_preview/ilyra_modular_blockout.tscn`

This layers a more character-specific construction read onto the reshaped UAL-skinned body while preserving the same animation foundation:

- anime face/head blockout with visible jade-eye read
- extra long blonde face-framing hair locks
- fitted ivory Warden vest rather than heavy plate armor
- pale-blue center panel and high collar
- deliberately restrained antique-gold trim
- cape clasp and pale-blue shoulder mantle
- asymmetrical practical utility pouches
- layered front/side tabards
- silver bracers and greaves with brown leather straps
- fingerless-glove and practical boot blockouts
- canonical Wardrod in the right hand
- canonical shield in the left hand

Controls:

- `SPACE` next animation
- `P` pause/resume
- `V` toggle the new B00-guided detail layer for comparison
- `Q / E` rotate the character in 15-degree steps
- `R` restart the animation sequence
- `ESC` quit

See `ILYRA_MODULAR_BLOCKOUT_MANIFEST.md` for the exact prototype/production boundary.

## Authority boundary

None of these proxy meshes are Ilyra appearance canon. The exact approved B00 image remains authoritative for her face, vivid jade eyes, windswept blonde hair, slightly athletic natural-waist proportions, fitted white/pale-blue Warden clothing, restrained decoration, brown utility gear, silver arm/leg guards, pale-blue cape, colors, silhouette, and final visible equipment design. These scenes exist only to validate the UAL rig, deformation quality, animation language, layered-character construction, and secondary-motion direction before a production 3D mesh is authored.

The UAL female mannequin and both animation libraries share the same skeleton, so animation tracks transfer directly without humanoid retargeting.
