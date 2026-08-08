# Diyse-Game

Clean Godot production repository for **Diyse**, a 2.5D, party-based, command-driven turn-based JRPG targeting Android.

This repository begins from a fresh implementation baseline. The older `zxxdjxxz-del/Diyse` repository is historical prototype reference only and is not a code source for this project unless an explicit task authorizes a specific port.

## Current phase

**Step 7B.5 — Technical Feasibility & Vertical Slice Proof**

The immediate goal is to prove that the intended Diyse architecture can run as a coherent Android game loop before full Step 7C dialogue production begins.

## Baseline rules

- Engine line: Godot 4.7.x stable; current proof target Godot 4.7.1.
- Language: GDScript.
- Platform target: Android, landscape.
- Presentation: 2.5D — 3D environments/depth/lighting/traversal with stylized 2D/2.5D character presentation and illustrated dialogue portraits where appropriate.
- Dialogue: fully authored; no player dialogue choices.
- Combat: discrete round-based command combat.
- Maximum active permanent party: four.
- Permanent commands: Attack / Ability / Card / Item / Defend.
- MP is the universal ordinary Ability resource; no character-specific combat gauges.
- Content architecture should be data-driven wherever practical.
- Do not invent mechanics or silently change canon to make implementation easier.

See `AGENTS.md` and the documents under `docs/` before implementing gameplay.
