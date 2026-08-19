# Diyse HD-2D Presentation Runtime

This directory contains reusable runtime presentation contracts introduced under **v1.73 / Audit88**.

These systems are presentation/runtime infrastructure only. They must not decide or lock story dialogue, final ordinary-enemy rosters, Elite placement, Hunt placement, final balance, or final visual assets.

The runtime layer exists so Chapters 0–4 can be implemented against the approved HD-2D grammar now while final sprites/backgrounds/VFX remain replaceable.

Core targets:

- field character target scale: approximately 80 px;
- battle character target scale: approximately 200 px;
- large high-resolution dialogue portraits;
- party-left / enemy-right / open-center battle composition;
- authored environment layers and state swaps;
- bounded cameras and restrained parallax;
- reusable nonlethal resolution and Prime presentation hooks;
- Android quality scaling for decorative effects only.

Do not add chapter-specific Elite placement or dialogue ownership here. Elite placement remains a separate later encounter-design decision unless an individual Elite is explicitly canon-locked elsewhere.