# UAL Rig Preview

This is the first Diyse proof-of-concept using the project's actual Universal Animation Library rig rather than the abandoned 2D shader-deformation approach.

## Required binary assets

Copy these three files from the supplied UAL Standard packs into:

`asset_sources/animation/ual/`

- `Mannequin_F.glb` — UAL2 `Female Mannequin/Unreal-Godot/`
- `UAL1_Standard.glb` — UAL1 `Unreal-Godot/`
- `UAL2_Standard.glb` — UAL2 `Unreal-Godot/`

The preview deliberately uses the non-root-motion libraries so locomotion remains centered for inspection.

## Base rig scene

Run:

`game/characters/presentation/rig_preview/ual_rig_preview.tscn`

Automatic sequence:

Idle → Walk → Jog → Sword Idle → Sword Regular Combo → Sword Block → Hit Chest → Simple Spell → repeat.

Controls: Space = next clip, P = pause, R = restart.

## Ilyra motion proxy

Run:

`game/characters/presentation/rig_preview/ilyra_ual_proxy.tscn`

This scene inherits the real UAL rig preview and adds only abstract Ilyra cues so we can judge the animation language with a more representative Diyse silhouette:

- pale ivory / pale-blue Warden palette
- silver guard/joint read
- blonde long-hair masses
- brown utility belt and pouches
- pale-blue segmented cape
- subtle procedural hair/cape follow-through

This is **not** Ilyra's final 3D model and must not become an appearance reference. Her locked B00 image remains the exact visual-design authority. A production Ilyra requires a purpose-built 3D mesh matching that B00 design and skinned to the same UAL skeleton.

The UAL female mannequin and both animation libraries share the same skeleton, so the preview transfers their animation tracks directly without humanoid retargeting.
