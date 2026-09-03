# Diyse — Portrait Production Manifest

**Status:** ACTIVE PRODUCTION TRACKER  
**Pipeline:** `PORTRAIT_DERIVATIVE_PIPELINE.md`

This manifest tracks downstream portrait production without changing B00/current-master authority.

## Current source readiness

| Character ID | Current master | Source fingerprint | Dialogue derivative status | UI derivative status |
| --- | --- | --- | --- | --- |
| `cyanis` | `asset_sources/characters/current/cyanis.jpg` | SHA-256 `c622ed107cd7b735dec44b36dce0ee6e078b687abef639d5b9f9780e086b854f` | `neutral` benchmark spec ready in `CYANIS_DIALOGUE_PORTRAIT_BENCHMARK_V1.md`; image candidate not yet approved | Source ready; no production derivative approved yet |
| `ilyra` | `asset_sources/characters/current/ilyra.jpg` | SHA-256 `46dbfd2783d9aa3da04209b0938122517cb0bd2077b6da809fe3da50aa7dd358` | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |
| `torren` | `asset_sources/characters/current/torren.jpg` | SHA-256 `5ea50d69d667cd53460e27b757dbaf2a8190f2291614cda29ca0197e9035ae98` | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |
| `nimera` | `asset_sources/characters/current/nimera.jpg` | SHA-256 `c24f819b287baf2cf087e12f14f2aee0be1c94dd1ea56ca4cc6747b89ced0330` | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |
| `vaelira` | `asset_sources/characters/current/vaelira.jpg` | SHA-256 `0a593588e59f644bb83efe6ee4d33caf9173495035ef007e1daa307c9385cd6e` | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |
| `seyrik` | `asset_sources/characters/current/seyrik.jpg` | SHA-256 `51aca401cfd41b9d6f042c57f9850b70eb9ddcde2a43510e7bee6d44b7f57f23` | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |
| `maevra` | `asset_sources/characters/current/maevra.jpg` | SHA-256 `9e2b3affd3c208f7dd9e9568ed46da8faf194a98c0a6936e8d6b412f0d452c94` | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |
| `kessara` | `asset_sources/characters/current/kessara.png` | Git blob `c773505a1b031788849588a38e677dcc09727108`; SHA-256 pending verification | Source ready; no production derivative approved yet | Source ready; no production derivative approved yet |

## First benchmark target — Cyanis `neutral`

Controlling benchmark spec:
`CYANIS_DIALOGUE_PORTRAIT_BENCHMARK_V1.md`

Current benchmark state:
- exact authoritative source master identified;
- exact source fingerprint recorded;
- neutral acting target defined;
- identity/prohibited-drift checklist defined;
- preferred conversational bust composition defined;
- 432 px visible-height runtime test defined, with 378 px and 486 px boundary checks;
- provisional approved-output filename reserved as `cyanis_neutral.png`;
- **no image candidate is approved yet**.

The benchmark must be produced from the actual current `cyanis.jpg` master rather than reconstructed from an older visual document, benchmark sheet, filename, or prose-only description.

## Runtime/proof findings

The current portrait registry architecture is ready for stable semantic character/expression lookup.

Current proof-only registry coverage:
- Cyanis — `neutral`, `amused`;
- Torren — `neutral`, `dry`.

Those four SVGs under `game/characters/placeholders/portraits/` are proof fixtures only. They do not count as completed production portraits.

Current Chapter 0 authored Resources inspected during this setup primarily use in-world/cinematic staging with empty portrait slots, so this manifest does **not** infer a speculative Chapter-0 expression list from prose/staging cues.

## Expression-production rule

Do not generate a fixed universal expression pack for every character by assumption.

Portrait expressions enter this manifest when one of these is true:
- an authored scene explicitly calls for the portrait presentation and expression;
- a UI production requirement needs a defined neutral/status variant;
- the user explicitly approves a reusable expression set.

When approved, add one row per derivative containing:
- character ID;
- expression/variant ID;
- derivative lane;
- source fingerprint;
- output path;
- pixel dimensions;
- framing/orientation;
- transparency/background treatment;
- approval status.

## Next production action

Produce the Cyanis `neutral` image candidate from the exact current repository master, review it at the benchmark dialogue sizes, and obtain explicit approval before promoting it to the derivative lane or runtime registry.

After approval, use the successful crop/render/export treatment as technique guidance for later portraits while always returning to each character's own current master for identity.

Do not create an empty production-image registry that points directly at full B00 masters as a shortcut.
