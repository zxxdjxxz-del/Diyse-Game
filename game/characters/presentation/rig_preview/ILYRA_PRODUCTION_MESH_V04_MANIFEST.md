# Ilyra Production Mesh v0.4 — first skinned visual-shell candidate

Purpose: first deliberate visual-model replacement after the Stage 8 literal render exposed the quality gap between the proven UAL rig foundation and the mannequin/proxy character shell.

The visual shell was first authored as a static candidate around the UAL rest proportions, then skinned onto the existing UAL core without changing the imported animation skeleton.

## B00-directed targets

The approved cleaned Ilyra B00 remains exact visual authority. This candidate is trying to move the real geometry toward that authority:

- mature/confident anime face direction
- vivid jade eyes
- long windswept blonde hair
- slightly athletic build with a natural waist
- fitted ivory / pale-blue Warden clothing rather than heavy armor
- restrained decoration
- brown utility belt/pouches
- fingerless gloves
- light silver bracers/greaves
- pale-blue cape
- Wardrod primary / shield secondary equipment language

## v0.4 visible changes from Stage 8

- denser jaw/cheek/head surface instead of the crude Stage 5 face proxy
- narrower mature eye forms, jade irises, restrained brows
- asymmetric bangs
- five longer tapered volumetric hair locks instead of flat slabs/capsules
- continuous fitted torso shell with a more natural waist/hip transition
- shaped front bodice surface outside the mannequin chest/abdomen so base anatomy no longer defines the clothing front
- fitted ivory lower-body Warden fabric with restrained pale-blue accents
- shaped pointed tabards rather than rectangular panels
- cleaner broad pale-blue cape cut with a tapered hem
- smaller one-handed Wardrod proportions
- smaller secondary shield so it no longer dominates Ilyra's silhouette

## UAL skinning pass

`Ilyra_ProductionMesh_v04_UAL_Skinned.glb` uses the same imported skin as the existing Ilyra anime-body proof:

- original UAL core: **65 joints, unchanged and in the same order**
- original two body primitives retained as the anatomy understructure
- **56 new replacement-shell primitives** appended to the same skinned mesh node
- every new primitive carries `POSITION`, `NORMAL`, `JOINTS_0`, `WEIGHTS_0`, and indices
- new joint values remain within the original 0–64 UAL joint-slot range
- all generated vertex weight sets normalize to 1.0
- no humanoid retarget layer introduced

Weighting intent:

- face / cap / bangs: Head
- longer hair: Head → neck → upper spine starter weighting until Stage 8 springs are reconnected
- fitted torso/bodice: clavicles / spine chain / pelvis / upper thighs
- sleeves: clavicle → upper arm → lower arm
- tabards: pelvis → thighs
- fitted legwear: thigh → calf
- cape: shoulder girdle / spine chain / pelvis starter weighting
- Wardrod and shield: rigid 1.0 hand weights
- bracers, gloves, greaves and boots: rigid corresponding limb-bone weights

Structural validation passed with 65 UAL joints, 58 total skinned primitives (2 original + 56 replacement), no weight-normalization errors, and a successful GLB parser smoke test.

## What is deliberately retained

- proven UAL 65-bone animation foundation
- Stage 8 appended character-specific hair/cape secondary-chain architecture
- hard-equipment behavior for Wardrod, shield, bracers and greaves

## What is not complete

- production retopology and manual deformation cleanup
- final face sculpt / exact B00 likeness
- final hand-authored hair topology
- final UVs/textures/materials
- reconnecting the Stage 8 auxiliary spring chains to this exact new hair/cape mesh
- visual deformation review under the full UAL motion stress set

The downloadable v0.4 bundle contains the literal static GLB, literal front/3/4/side technical render, the UAL-skinned GLB, manifest, visual-shell generator, and skinning generator.

## Next step

Reconnect the already-tested Stage 8 secondary-motion chains to the v0.4 skinned long-hair/cape geometry, then run deformation cleanup against walk, jog, sprint, crouch, roll, shield dash, cast and knockback. Do not add another rig-architecture experiment unless that test exposes a specific need.

## Authority boundary

This generated mesh is **not Ilyra visual canon**. The approved cleaned B00 remains exact authority and overrides this candidate anywhere they differ.
