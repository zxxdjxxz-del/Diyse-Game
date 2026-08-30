# Diyse — Screen, Layout & Android Rules
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit v85 working overrides already preserved in the reorganized domains.  
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## CANON / PRESENTATION REQUIREMENT
Reference composition:
> **1920×1080 / 16:9**

Wider Android screens:
- reveal additional horizontal scenery where appropriate;
- do not stretch critical gameplay/UI composition.

## HD-2D presentation anchors
- field characters ~80 px target;
- battle characters ~200–220 px target;
- large high-resolution dialogue portraits;
- party battle framing left;
- enemies right;
- open center lane protected for actions/VFX.

## Dialogue
General final target:
- portraits around **35–45% screen height** where practical;
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
