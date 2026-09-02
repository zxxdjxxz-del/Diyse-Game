# Diyse — Consumable Sell Rule

**Status:** RESALE FORMULA STRUCTURE CURRENT / EXACT G TABLE NEEDS DISPLAY-SCALE SYNCHRONIZATION

This rule applies only to normal-stock Consumables. It does not change ordinary-equipment resale, Relics, Legacies, Forge Components, Key Items, Cards, or Primes.

## Core rule
Normal-stock Consumables sell for approximately **25% of their purchase price**.

Current implementation form after G synchronization:
> `SellG = max(50, floor((BuyG × 0.25) / 50) × 50)`

This is the tenfold-display equivalent of the prior nearest-5 rule and preserves a minimum sell value equal to 25% of the cheapest ordinary Consumable scale.

Purpose:
- using Consumables should normally be better value than liquidating them;
- found/quest-issued normal supplies may still be converted to modest G if the player prefers;
- resale should not become a major alternate income engine;
- no buy/sell arbitrage is possible.

## Exact sell-table status
The former exact table used the pre-extra-digit currency values and is retired as current-facing numeric authority.

The synchronized table should use the current G purchase prices in `CONSUMABLE_PRICES.md` and the formula above.

## Premium Consumables
The following limited-premium items are **not sellable**:
- C09 **Reservoir Tonic**;
- C19 **Emergency Kit**;
- C20 **Emergency Rally**.

They are purchasable in one-copy-per-shop premium stock and also have authored guaranteed sources, but resale remains disabled.

## No vendor variance
- all eligible vendors use the same sell rule;
- no chapter depreciation/appreciation;
- no faction bonus;
- no hidden merchant skill modifier;
- no random resale-price fluctuation.

## Quest-reward implication
Normal-stock Consumables received from Side Quests or Character Quests use this same resale rule. Their full shop price remains the correct reward-equivalence value; their sell value is intentionally much lower.
