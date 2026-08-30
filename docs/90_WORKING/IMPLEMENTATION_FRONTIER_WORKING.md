# Working — Implementation Frontier

**Owner:** `13_UI_AND_IMPLEMENTATION`

## High-impact reconciliation
1. remove Mastery Point assumptions from production state/UI
2. replace stale bearer-locked `first_champion` Prime proof
3. implement current Prime slots/states/cooldown/fresh-form refresh
4. migrate proof `gold` semantics to Auren
5. replace proof item/equipment fixtures with current data
6. expand/version production save schema
7. build production menu/combat/loadout UI

## Test debt
Update stale automated Prime expectations before treating the suite as a current green gate.

## Rule
Do not build final UI around proof-state structures known to be obsolete.
