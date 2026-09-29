# Card Runtime Content Boundary

This folder currently contains **implementation/proof Card resources**, not the production Card catalog.

## Current authority

Game-design authority for Cards and Primes lives under:

- `docs/07_CARDS/`;
- current battle-system owners referenced by that domain;
- current character/story owners for acquisition, knowledge, and chronology.

A resource existing in this folder does **not** make its name, bearer rule, duration, use limit, command set, or other proof behavior current canon.

## Current files

- `standard_card_definition.gd` — runtime Resource definition/infrastructure.
- `proof_standard_card.tres` — explicitly non-canon Standard Card fixture.
- `first_champion_recovered.tres` — legacy Prime proof fixture retained for the current combat prototype.

The `first_champion_recovered.tres` resource intentionally still carries retired proof assumptions such as the `first_champion` identity, First Champion display name, bearer lock, proof duration, and direct-control command data. Those assumptions are tracked as implementation debt in:

`docs/13_UI_AND_IMPLEMENTATION/IMPLEMENTATION_NOTES/CURRENT_CODE_DIVERGENCES.md`

Do not use that fixture to override current Last Sentinel / Prime authority.

## Production-content rule

When production Card/Prime resources are introduced, synchronize them from the owning current authority rather than editing proof fixtures into apparent canon piecemeal.

Proof resources may remain until the corresponding runtime architecture is migrated, but they must stay clearly non-authoritative.
