# Diyse — 2.5D Presentation Rules

## Target

Diyse is a 2.5D JRPG.

The intended visual language combines:

- real 3D environments and traversal space;
- 3D depth, elevation, lighting, scale, architecture, environmental effects, battle spaces, bosses, Black Host spaces, and Prime spectacle;
- stylized 2D/2.5D characters in-world;
- illustrated dialogue portraits for expressive acting where appropriate.

## Step 7B.5 validation status

The foundational presentation architecture is **PROVEN / PASS on Android**.

Step 7B.5 demonstrated that:

- a world-space 2D/2.5D character can occupy a real 3D environment coherently;
- floor contact, camera, collision, boundaries and depth presentation work together on Android;
- touch exploration can share the same movement architecture used for desktop development;
- proximity interaction and portrait dialogue can transition into and out of exploration without state loss;
- combat and Prime presentation can coexist with the same overall 2.5D application architecture;
- placeholder art can be replaced without redefining core gameplay systems.

This PASS validates the architecture, **not** the final camera language, character rendering technique, art quality or temporary proof assets.

## Production presentation requirements

Future production work should preserve and improve:

- world-space placement of 2D/2.5D characters;
- convincing floor contact;
- camera readability;
- depth sorting/occlusion;
- foreground obstruction handling;
- scale/depth behavior;
- transitions between exploration, dialogue and battle;
- Android readability and performance;
- replaceability of temporary assets.

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

The accepted dialogue architecture supports reaction beats without forcing every emotional change into spoken text.

## Do not over-freeze proof fixtures

The 7B.5 placeholder sprite/billboard, temporary camera values, graybox field and proof dialogue layout are not final art direction merely because they passed technically.

Any production method must remain compatible with:

- final authored character visual identities;
- multiple character poses/expressions;
- battle presentation;
- mobile performance;
- replacement of placeholder art without rewriting core gameplay systems.

## Historical-prototype exclusion

The old libGDX pre-rendered/fixed-camera field approach is not the default architecture for this repository. It may be studied only if explicitly requested as a comparison. The accepted `Diyse-Game` Godot line is the active implementation baseline.