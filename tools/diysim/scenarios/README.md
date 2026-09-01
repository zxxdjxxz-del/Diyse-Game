# Scenarios

Owns reusable simulation setups, not canonical actor definitions.

A scenario should declare:
- exact story/balance point;
- party members and selected reusable snapshots;
- enemy/boss/support definitions used;
- active party size;
- starting HP/MP and consumables;
- legal Cards/Primes/equipment/class access;
- tactical policy;
- run count/seed defaults;
- expected regression/certification ranges where known.

Suggested subfamilies as coverage grows:
- `chapters/`
- `story_bosses/`
- `elites/`
- `regional_hunts/`
- `major_hunts/`
- `regressions/`

Do not duplicate owner stats or experimental overlays in scenario files.