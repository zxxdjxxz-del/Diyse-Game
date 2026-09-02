# Diyse — Kessara Relic-Copy UI

**Implementation rule:** current domain canon beats older proof code/docs. Proof implementations are evidence of architecture, not permission to restore stale mechanics, names, currencies, progression, or UI concepts.

## IMPLEMENTED FOUNDATION
Current service logic validates:
1. original Relic obtained;
2. Relic not already copied;
3. Face has remaining copy opportunity;
4. matching-Face Relic-copy component exists;
5. party can afford the exact **6,000 G** fee;
6. successful commit consumes that component;
7. successful commit deducts exactly **6,000 G**;
8. same Relic identity becomes quantity 2.

The component/item/wallet mutation is committed through one GameState transaction after all eligibility checks pass.

Per Face:
> exactly **3** Relic-copy components / copy opportunities.

Per individual Relic:
> at most **1 forged duplicate**, quantity max **2**.

Legacies cannot use this service.

## Exact service fee
Owner authority:
`../12_ECONOMY_AND_REWARDS/KESSARA_RELIC_COPY_ECONOMY.md`

Current fee:
> **6,000 G per successful Relic-copy forge**

Fee behavior:
- invalid attempt = **0 G** charged;
- cancellation = **0 G** charged;
- already-copied Relic = **0 G** charged;
- insufficient G = no component/item mutation;
- successful forge = exactly **6,000 G** deducted.

This fee is closed and must not be presented as optional, variable, chapter-scaled, Face-scaled, or Auren-denominated.

## Required service UI information
A future service menu must be able to show:
- Relic identity;
- Face;
- original obtained / not obtained;
- current quantity;
- copied already / copy available;
- matching component available;
- Face copy opportunities used/remaining or equivalent clear eligibility feedback;
- service fee: **6,000 G**;
- current party G balance or otherwise clear affordability feedback;
- explicit insufficient-G failure state;
- final result quantity 2 and updated G balance after success.

## Failure reasons represented by service code
- invalid state;
- original not obtained;
- already copied;
- Face copy limit reached;
- no matching component;
- insufficient G;
- commit failed.

Player-facing wording can be polished without changing the rule.

## Still OPEN
- exact service unlock/menu timing;
- exact original-vs-copy visual badge/label;
- confirmation flow;
- service animation/presentation.

Those presentation questions do not reopen the exact 6,000-G fee.
