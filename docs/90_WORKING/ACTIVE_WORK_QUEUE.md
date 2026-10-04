# Diyse — Active Work Queue

**Status:** ACTIVE CROSS-DOMAIN SEQUENCING INDEX

This file tracks work order only. Detailed rules and open-item definitions belong to the numbered owner domains.

## 1 — Dialogue / story continuation

Current:
- Chapters 0–3 dialogue are current production;
- Chapter 4 exact dialogue remains open against the current redesigned beats;
- Chapters 5–13 remain development-in-progress;
- optional Side Quest / Character Quest dialogue remains open where not already authored.

Use:
- `../03_DIALOGUE/README.md`
- `../02_STORY/OPEN_STORY_ITEMS.md`

Story-owned enemy placement/timing questions remain deferred until their scenes are authored. Use only identities and placements present in the current Story and enemy-domain owners.

## 2 — Playable area / route production

**ACTIVE — inventory established; blueprint/graybox work underway**

The world map and macro route order do not replace build-ready playable geometry.

Current working owners:
- `AREA_AND_ROUTE_LAYOUT_PRODUCTION_WORKING.md`
- `PLAYABLE_AREA_INVENTORY_WORKING.md`
- `AREA_LAYOUTS/`

Current first production anchor:
> validate/play the Chapter-0 Convoy/Wreck graybox, revise scale/camera/topology from traversal evidence, then promote approved topology to L3.

## 3 — Runtime / UI implementation reconciliation

Current high-impact debt includes:
- replace legacy First Champion/bearer-lock Prime proof behavior;
- migrate combat proof flow to current turn-entry rules;
- replace proof items/equipment/party fixtures;
- expand/version save schema;
- reconcile current encounter runtime data;
- build production menu/combat/loadout/shop/Kessara UI from owner-domain values.

Use:
- `../13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`
- `../13_UI_AND_IMPLEMENTATION/OPEN_UI_IMPLEMENTATION_ITEMS.md`

## 4 — Visual production

Current immediate gate:
> **B00 rigged-model runtime validation**

Six exact party masters are locked. The shared UAL/Godot rig foundation and Ilyra v0.7 deformation path are already proven at architecture level.

Current visual-production work should now focus on:
- correcting proof character geometry toward the exact current masters;
- final deformation/spring/attachment cleanup;
- B00 material/shader/outline fidelity;
- actual field and battle camera validation;
- then safe propagation across the remaining party.

Permanent-party field/battle production now uses rigged 3D models matched to the exact current 2D masters.

Environment/material B01–B11 certification remains open before bulk environment conversion.

Use:
- `../14_ART_AND_VISUALS/PRODUCTION/OPEN_VISUAL_PRODUCTION_ITEMS.md`
- `../14_ART_AND_VISUALS/PRODUCTION/BENCHMARKS/B00_RIGGED_MODEL_RUNTIME_VALIDATION_V1.md`

## 5 — Enemy / progression / economy rebuild and recertification

Current:
- enemy abilities/action kits and direct-damage Powers require redesign/revalidation;
- mandatory/completionist difficulty must be rerun from current kits;
- Player EXP/CEXP placement is rebuild-pending;
- **Lv55–60** remains the normal full Base + Subclass completion target;
- detailed **G** economy pricing/payout/liquidity calibration remains rebuild-pending.

Use current enemy, progression, economy, and QA owners for all rebuild and certification work.

Use:
- `../09_ENEMIES_AND_ENCOUNTERS/`
- `../10_PROGRESSION_AND_EXP/`
- `../12_ECONOMY_AND_REWARDS/`
- `../16_BALANCE_AND_TESTING/OPEN_BALANCE_ITEMS.md`

## 6 — Audio / music

Final music direction, cue plan, voice scope, SFX palette, and implementation/mix targets remain open.

Use:
- `../15_AUDIO_AND_MUSIC/OPEN_AUDIO_ITEMS.md`

## 7 — Whole-game QA / release certification

After the relevant content and implementation layers stabilize, run the current campaign, optional-content, boss/Hunt, progression, save/exploit, UI, audio, and Android release gates.

Use:
- `../16_BALANCE_AND_TESTING/FINAL_RELEASE_GATES.md`
- `../16_BALANCE_AND_TESTING/TRUE_BATTLES/TRUE_BATTLE_TEST_PROTOCOL.md`

There is currently no live true-battle difficulty certification; new certifications must use current inputs.

## 8 — Intentionally open story/lore

Do not guess intentionally unresolved story/lore details into canon.

Use:
- `../02_STORY/OPEN_STORY_ITEMS.md`

## Rule

When a working item is resolved:
1. update the numbered owner domain;
2. update this queue only if sequencing changes;
3. delete resolved working notes rather than preserving parallel authority.
