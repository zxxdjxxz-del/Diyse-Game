# UAL Rig Preview

This is the first Diyse proof-of-concept using the project's actual Universal Animation Library rig rather than the abandoned 2D shader-deformation approach.

## Required binary assets

Copy these three files from the supplied UAL Standard packs into:

`asset_sources/animation/ual/`

- `Mannequin_F.glb` — UAL2 `Female Mannequin/Unreal-Godot/`
- `UAL1_Standard.glb` — UAL1 `Unreal-Godot/`
- `UAL2_Standard.glb` — UAL2 `Unreal-Godot/`

The preview deliberately uses the non-root-motion libraries so locomotion remains centered for inspection.

## Scene

Open and run:

`game/characters/presentation/rig_preview/ual_rig_preview.tscn`

Automatic sequence:

Idle → Walk → Jog → Sword Idle → Sword Regular Combo → Sword Block → Hit Chest → Simple Spell → repeat.

Controls: Space = next clip, P = pause, R = restart.

The UAL female mannequin and both animation libraries share the same skeleton, so the preview transfers their animation tracks directly. The mannequin is only a temporary visual stand-in for Ilyra. A final Ilyra character requires a 3D mesh skinned to this same skeleton; the B00 image remains her visual-design authority rather than a skinned 3D mesh itself.
