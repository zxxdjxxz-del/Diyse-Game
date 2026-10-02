# Diyse — Screen, Layout & Android Rules

**Status:** ACTIVE UI / IMPLEMENTATION SPEC
**Authority:** current repository UI/implementation domain; cross-domain gameplay/content rules defer to their current numbered owner domains.

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## CANON / PRESENTATION REQUIREMENT
Reference composition:
> **1920×1080 / 16:9**

Wider Android screens:
- reveal additional horizontal scenery where appropriate;
- do not stretch critical gameplay/UI composition.

## HD-2D presentation anchors
- permanent-party field and battle characters use the current rigged-3D runtime pipeline;
- character readability is validated at the actual target display resolution and actual field/battle cameras rather than fixed sprite-height targets;
- large high-resolution dialogue portraits;
- party battle framing left;
- enemies right;
- open center lane protected for actions/VFX.

The former ~80 px field / ~200–220 px battle character targets are retired as production requirements.

## Dialogue
General final target:
- portraits generally **~25–35% of screen height**, with **~30%** as the normal starting target under `DIALOGUE_UI.md`;
- dialogue UI generally in the lower **20–25%** while preserving environment/portrait readability.

The current proof dialogue panel is substantially taller and is **not final layout authority**.

## Touch readability
Production touch UI must:
- keep primary actions clearly separated;
- avoid tiny text-only targets;
- preserve legibility over bright/dark HD-2D backgrounds;
- not overlap critical dialogue portraits or battle targeting information;
- permit one-handed/comfortable landscape use where practical.

Exact button dimensions, margins, safe-area padding and phone-notch strategy:
> **OPEN PRODUCTION UX**

## Performance scaling
Device-quality scaling may reduce:
- decorative particles;
- reflections;
- weather density;
- secondary background motion;
- distortion;
- noncritical dynamic lights.

It may not reduce:
- command readability;
- target clarity;
- battle timing;
- critical story VFX;
- exact character identity;
- required status/UI information.
