# Diyse — 2.5D Presentation Rules

## Target

Diyse is a 2.5D JRPG.

The intended visual language combines:

- real 3D environments and traversal space;
- 3D depth, elevation, lighting, scale, architecture, environmental effects, battle spaces, bosses, Black Host spaces, and Prime spectacle;
- stylized 2D/2.5D characters in-world;
- illustrated dialogue portraits for expressive acting where appropriate.

## Technical-proof priorities

The proof must specifically test:

- world-space placement of 2D/2.5D characters;
- floor contact;
- camera readability;
- depth sorting/occlusion;
- foreground obstruction handling;
- scale/depth behavior;
- transitions between exploration, dialogue, and battle;
- Android readability and performance.

## Portrait philosophy

Portraits are not decorative duplicates of dialogue text. They carry performance information such as:

- hesitation;
- amusement;
- irritation;
- embarrassment;
- fear;
- micro-smiles;
- eye-direction or attention changes where supported;
- silent reactions.

The dialogue system must support reaction beats without forcing every emotional change into spoken text.

## Do not lock too early

Step 7B.5 is allowed to compare implementation techniques for 2.5D character rendering, occlusion, camera behavior, and portrait staging.

Do not treat a placeholder technical method as final art direction merely because it works once.

Any chosen production method must remain compatible with:

- final authored character identities;
- multiple character poses/expressions;
- battle presentation;
- mobile performance;
- replacement of placeholder art without rewriting core gameplay systems.

## Historical-prototype exclusion

The old libGDX pre-rendered/fixed-camera field approach is not the default architecture for this repository. It may be studied only if explicitly requested as a comparison.
