# Diyse Character Derivatives

This directory is for downstream production assets derived from the authoritative character masters in `../current/`.

The files under `../current/` remain the exact visual identity masters. Nothing in this derivative tree overrides them.

## Lanes

- `dialogue/` — approved dialogue portrait/bust derivatives by stable character/expression ID.
- `ui/` — approved menu/status/party UI portrait derivatives.
- later field/battle derivatives require their own explicitly approved production lane; Diyse's current B00 field/battle direction is rigged 3D rather than mandatory 2D sprite derivatives.

## Production rules

- Never overwrite or destructively edit a current master.
- Keep derivative provenance traceable to the exact current master.
- Preserve stable character IDs: `cyanis`, `ilyra`, `torren`, `nimera`, `vaelira`, `seyrik`, `maevra`, `kessara`.
- A derivative is purpose-specific and may simplify/crop/reframe, but may not redesign identity.
- Proof assets under `game/characters/placeholders/` are not production derivatives.

Controlling pipeline:
`docs/14_ART_AND_VISUALS/PRODUCTION/CHARACTERS/PORTRAIT_DERIVATIVE_PIPELINE.md`
