# Implementation Notes — Android Performance & Accessibility
**Historical migration provenance:** v85-era consolidated tracker.
**Authority treatment:** this repository file is current UI/implementation-domain authority within its stated scope; Audit/v85 references remain provenance only.
**Runtime source checkpoint inspected:** `Diyse-Game` commit `3fd07e92eda04f31ba613a654b3b1b28071f44e6`.  
**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.


## Android first-class target
Performance tiers may reduce decorative rendering, but not gameplay clarity.

UI should avoid:
- excessive full-screen blur;
- expensive continuously animated masks;
- dense particle overlays behind text;
- tiny hover-only information;
- mouse-only interaction assumptions.

## Touch
Important information must not depend on:
- hover;
- right click;
- keyboard tooltip only.

## Text
Production must preserve:
- readable font scale;
- contrast over bright/dark field art;
- clear selected/disabled states.

Exact accessibility settings are still OPEN.

High-value future candidates include:
- text-size scaling;
- subtitle/dialogue speed control;
- reduced motion;
- high-contrast UI mode;
- color + icon redundancy for statuses/elements;
- controller remapping.

These are candidates, not canonized feature promises in this migration.
