# Diyse — Android / HD-2D QA Plan

**Status:** ACTIVE DEVICE / PRESENTATION QA PLAN  
**Visual authority:** `../../14_ART_AND_VISUALS/`

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
- current rigged 3D party models remain readable at actual field-camera distance;
- current rigged 3D party models remain readable at actual battle-camera distance;
- silhouette, face/hair mass, palette, weapons/props, and status/VFX readability survive target device resolution;
- portrait scale/readability;
- VFX clarity;
- load times;
- memory pressure;
- scene-transition stability.

Readability gates must be derived from the current rigged-3D presentation and actual target-device captures.

## Quality scaling

Allowed to reduce:
- decorative particles;
- reflections;
- weather density;
- secondary motion;
- distortion;
- noncritical dynamic lights;
- noncritical LOD/material complexity.

Never reduce:
- target clarity;
- gameplay timing;
- command legibility;
- exact character identity;
- critical story VFX;
- status readability.

## Manual screenshot/video review

Capture representative:
- bright scene;
- dark scene;
- snow;
- wet/water scene;
- Black Host environment;
- four-enemy and eight-enemy battle;
- Prime manifestation;
- boss fresh-form transition;
- dialogue with two portraits;
- map/shop/menu when production screens exist.
