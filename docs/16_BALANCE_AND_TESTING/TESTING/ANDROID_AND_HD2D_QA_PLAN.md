# Diyse — Android / HD-2D QA Plan
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current written whole-project authority:** **v2.20 / Audit135**, plus newer explicit user corrections preserved by the reorganization.  
**Primary balance chain:** Audits 121–135 where compatible, especially 123–128 progression and 129–135 raw-stat certification.  
**Runtime test checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Balance ownership rule:** this domain owns cross-system balance acceptance criteria, verification plans, playtest targets, certification status and regression gates. Exact formulas/stats/rewards remain canonically housed in their dedicated system domains.


## Devices
Test multiple Android classes:
- lower-spec supported target;
- midrange;
- higher-end;
- at least one wider-than-16:9 display.

Exact supported-device floor remains a production decision.

## Validate
- stable frame pacing;
- battle input latency;
- touch target readability;
- dialogue readability;
- no critical UI under notches/cutouts;
- wider displays reveal scenery rather than stretch critical composition;
- field sprite readability ~80 px;
- battle sprite readability ~200–220 px;
- portrait scale;
- VFX clarity;
- load times;
- memory pressure;
- scene-transition stability.

## Quality scaling
Allowed to reduce:
- decorative particles;
- reflections;
- weather density;
- secondary motion;
- distortion;
- noncritical dynamic lights.

Never reduce:
- target clarity;
- gameplay timing;
- command legibility;
- exact character identity;
- critical story VFX;
- status readability.

## Manual screenshot review
Capture:
- bright scene;
- dark scene;
- snow;
- wet/water scene;
- Black Host dark environment;
- four-enemy and eight-enemy battle;
- Prime manifestation;
- boss fresh-form transition;
- dialogue with two portraits;
- map/shop/menu when production screens exist.
