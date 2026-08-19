# Diyse — HD-2D Presentation Rules

**Status:** ACTIVE / REQUIRED  
**Authority:** v1.73 / Audit88, inheriting v1.72 / Audit87  
**Effective:** August 19, 2026

## Target

Diyse is an **HD-2D JRPG** targeting Android/APK.

Older active `2.5D` and `3D` presentation language is superseded. Historical proof files, stable IDs, filenames, comments and archives may retain those terms, but they do not restore those directions.

## Master composition

- Reference composition: **1920×1080 / 16:9**.
- Wider Android displays reveal additional horizontal scenery rather than stretching critical gameplay/UI composition.
- Field characters target approximately **80 px**.
- Battle characters target approximately **200 px**.
- Dialogue uses large high-resolution portraits, generally around 35–45% of screen height where practical.
- Dialogue UI generally occupies the lower 20–25% while preserving portrait/environment readability.

## Field grammar

HD-2D depth is authored rather than brute-forced.

Use:

- background / midground / playable / foreground / atmosphere layers;
- restrained parallax;
- selective depth geometry only where traversal, collision or occlusion needs it;
- bounded authored cameras with damped follow;
- temporary pans/pushes/reframes for authored beats;
- automatic or authored foreground fade/reorder when navigation would be obscured;
- layered environment art and prepared state changes for scale and persistence.

Do not use a free camera as the normal field grammar.

Normal exploration generally displays the controlled field character. Full story groups appear through authored staging rather than permanent follower trains.

## Portrait philosophy

Portraits are a primary performance layer, not decoration. They carry hesitation, irritation, amusement, fear, embarrassment, silent reactions, micro-smiles, eye-direction/attention changes and other facial acting that would be wasteful to reproduce as bespoke ~80 px body animation.

Exact visual masters control portrait identity.

## Battle grammar

Standard battle framing is permanent across the game:

- active party staggered on the **left**;
- enemies on the **right**;
- open center action/VFX lane;
- reserve characters absent from the normal battle frame.

Undersized early parties occupy legal positions inside the same four-slot grammar rather than being recentered.

Battle backgrounds derive from the field sub-area and should reuse small composition families. Boss/Hunt arenas may add depth layers, foregrounds, lighting, motion and state changes while remaining visibly related to the location.

Bosses and Primes may exceed the ordinary ~200 px scale through layered art and temporary camera treatment.

## Random encounters

Random encounters remain Diyse's ordinary hostile-exploration layer where fiction supports them.

- Chapter 0 is the explicit exception: seven authored tutorial encounters, no normal random encounter table.
- Chapter 1 onward uses the campaign-standard fast random-battle transition in approved hostile areas.
- Safe/story pockets suppress encounter triggering locally.
- HD-2D conversion does not replace random encounters with visible roaming enemies.
- The field-to-battle transition never implies a free enemy action.

## Production tiers

Use the official Audit87/Audit88 vocabulary:

- **C0 — Conversational**
- **C1 — Staged**
- **C2 — Dramatic**
- **C3 — Spectacle**
- **V1 — Common**
- **V2 — Face/class identity**
- **V3 — Named signature**
- **V4 — Prime/boss spectacle**

Most scenes are C0–C1. C2 is selective. C3 is rare. V4 is reserved for true top-tier events. In Chapters 0–4, the first Last Sentinel manifestation in S022 is the first approved V4 event.

## Reuse and cost discipline

Prefer:

- reusable regional environment families;
- camera-specific authored art;
- reusable character poses/action families;
- portraits;
- prop-state and environment-state swaps;
- small battle-background families;
- layered crowd/NPC loops;
- audio for offscreen population/machinery/scale;
- lightweight particles;
- baked/precomposed lighting where useful;
- selective dynamic lights;
- modular Face, Card, Prime and elemental VFX systems.

Avoid by default:

- fully physically modeled cities;
- seamless giant dungeons merely to imply scale;
- free-camera exploration;
- general destruction physics;
- fluid simulation;
- crowd simulation;
- chain, cloth or hair simulation;
- one unique battle arena per formation;
- one bespoke body animation per named Ability;
- six complete independent environment/body pipelines merely because six elements exist.

## Exact visual authority

Exact approved visual masters remain controlling over derivative field sprites, battle sprites, portraits, cut-ins, boss layers and Prime presentation. Simplify only what the target scale requires; do not redesign silhouette, face, apparent age, body proportions, weapon identity, palette or approved costume/armor language.

The exact approved Yahtrea world-map image remains the spatial master and is not to be reinterpreted by HD-2D conversion.

## Android performance

Quality scaling may reduce decorative particle density, reflections, distortion, secondary background animation, weather density, decorative parallax layers and noncritical dynamic lights.

Do not reduce:

- playable-space readability;
- critical target readability;
- exact character identity;
- critical story effects;
- battle action timing;
- command/UI clarity.

## Technical-proof interpretation

Step 7B.5 remains accepted evidence for reusable exploration/dialogue/combat/Card/Prime/persistence architecture and Android feasibility. Any historical proof statement that specifically requires the retired 2.5D/real-3D presentation layer is superseded as art-direction authority and must be reinterpreted through Audit87/Audit88 HD-2D grammar.

Detailed completed-chapter conversion authority: `docs/production/HD2D_CHAPTERS_00_04_CONVERSION_AUDIT_PASS_1.md`.