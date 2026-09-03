# Diyse — Cyanis Dialogue Portrait Benchmark V1

**Status:** BENCHMARK SPEC READY — IMAGE CANDIDATE NOT YET APPROVED  
**Character ID:** `cyanis`  
**Expression ID:** `neutral`  
**Derivative lane:** dialogue portrait / bust  
**Pipeline:** `PORTRAIT_DERIVATIVE_PIPELINE.md`

## Source authority

Exact source master:
`asset_sources/characters/current/cyanis.jpg`

Source fingerprint:
SHA-256 `c622ed107cd7b735dec44b36dce0ee6e078b687abef639d5b9f9780e086b854f`

Source dimensions:
`1022 × 1536`

Matching visual lock:
`CYANIS_CURRENT_VISUAL_LOCK.md`

The source master controls exact facial identity, age read, hair, eye color, costume construction, visible equipment placement, palette, silhouette and incidental design minutiae. This benchmark is not permission to reinterpret or redesign Cyanis.

## Benchmark purpose

Create the first production dialogue-portrait derivative and use it to validate:
- identity preservation from a B00/current master;
- portrait crop/framing language;
- neutral acting intensity;
- line/value/material readability at dialogue scale;
- left/right presentation behavior;
- export quality and runtime display size;
- whether the successful treatment can become the repeatable portrait template for the rest of the cast.

This benchmark should be solved before generating broad expression packs.

## V1 acting target — `neutral`

Cyanis should read as:
- attentive;
- capable;
- calm but alert;
- serious without looking angry;
- mature and confident without becoming severe or over-aged.

This is the default conversational state, not a combat pose and not a promotional hero pose.

Do not add a grin, scowl, shouting mouth, melodramatic concern, or exaggerated anime reaction to the neutral benchmark.

## Identity locks visible in the portrait

Preserve from the exact current master:
- short tousled dark-brown / near-black hair;
- hazel eyes;
- current mature anime/seinen facial identity;
- light facial hair/stubble as shown by the master;
- dark royal-blue high-collar / long-coat clothing language;
- black fitted underlayers/leather;
- polished layered silver chest/shoulder armor;
- restrained silver hardware and trim;
- no shield in the neutral master presentation;
- no chest/back crest clutter;
- no full-heavy-plate redesign.

The portrait may omit lower-body elements naturally because of framing, but it may not invent replacement upper-body design details.

## Composition benchmark

Preferred starting composition:
- three-quarter or near-front conversational view consistent with the source face;
- head, shoulders and upper torso clearly visible;
- enough chest/shoulder armor and royal-blue clothing visible to make Cyanis instantly identifiable even when the face is partially dimmed by dialogue UI;
- hair silhouette fully inside safe crop;
- no weapon intruding into the portrait unless the source composition naturally requires it;
- no decorative background environment;
- transparent background preferred for the approved production export.

### Working display target

The V1 benchmark should be authored at high resolution but evaluated at a **324 px visible portrait-height test**, corresponding to 30% of the current 1080 px reference viewport.

Current dialogue portrait range is **approximately 25–35% of screen height**, with 30% as the normal starting target.

Reference visible heights at 1080p:
- 25% → **270 px**;
- 30% → **324 px**;
- 35% → **378 px**.

The source asset should remain high resolution; this smaller on-screen range is a presentation rule, not a request to reduce source-image quality.

Recommended working export container for the first test:
`1024 × 1024 PNG` or larger, with transparent background and adequate padding around hair/shoulders.

If the source framing requires a taller container to avoid damaging the silhouette, use a taller lossless PNG rather than forcing a square crop.

## Orientation

First approval target:
`left-facing-slot neutral` / natural source orientation.

Do not destructively mirror the source master simply to create the opposite dialogue side. After the first benchmark is approved, test whether runtime mirroring preserves all asymmetric visible details. If not, create an authored right-slot derivative.

## Rendering treatment

Preserve the current Diyse character-side style:
- mature anime/seinen-inspired construction;
- chaotic/variable line weight rather than uniform digital outlining;
- graphic cel-informed value grouping;
- selective soft integration where already appropriate to the established character style;
- polished silver reading as metal rather than grey plastic;
- royal-blue cloth reading separately from black leather/underlayers;
- controlled detail with no random dots, patch seams, accidental symbols or over-rendered gacha gloss.

This is a derivative of the current master, not a new art-style experiment.

## Prohibited benchmark drift

Reject the candidate if it:
- changes Cyanis's face shape or recognizable identity;
- changes hazel eyes to blue or another color;
- lightens hair into the retired older brown presentation or changes the haircut materially;
- adds a shield;
- adds crest insignia to chest/back;
- increases armor into bulky full plate;
- changes the royal-blue / black / silver hierarchy;
- turns the neutral expression into anger, sadness, smirking or a glamour pose;
- introduces painterly softness or glossy mobile-gacha rendering;
- mirrors asymmetric design details without review;
- contains generation artifacts, stray dots, broken armor anatomy, duplicated straps or impossible shoulder construction.

## Runtime review checklist

Review the candidate in all of these states:
1. full-resolution source review;
2. **324 px** visible-height dialogue presentation (30% baseline);
3. approximately **270 px** visible height (25% minimum target);
4. approximately **378 px** visible height (35% maximum target);
5. active portrait at full intended brightness;
6. inactive/dimmed portrait treatment once that UI value is defined;
7. left slot;
8. right slot only after orientation handling is validated.

Pass requires immediate recognition as the exact current Cyanis master at every tested dialogue scale without overwhelming the environment or dialogue box.

## Intended production output

Provisional filename after approval:
`cyanis_neutral.png`

Provisional derivative source lane:
`asset_sources/characters/derivatives/dialogue/`

Do not place a candidate in the approved production lane or point the runtime registry at it until the user approves the image benchmark.

## Approval consequence

Once the Cyanis `neutral` benchmark passes:
- record exact output dimensions and fingerprint in `PORTRAIT_PRODUCTION_MANIFEST.md`;
- freeze the successful crop/render/export treatment as the first portrait-production template;
- use that template as technique guidance for the next character while always returning to that character's own exact current master for identity;
- then add additional expression IDs only when authored scene demand requires them.
