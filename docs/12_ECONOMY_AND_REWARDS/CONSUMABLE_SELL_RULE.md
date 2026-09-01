# Diyse — Consumable Sell Rule

**Status:** EXACT CONSUMABLE RESALE AUTHORITY

This rule applies only to normal-stock Consumables. It does not change ordinary-equipment resale, Relics, Legacies, Forge Components, Key Items, Cards, or Primes.

## Core rule
Normal-stock Consumables sell for approximately **25% of their purchase price**:

> `SellAuren = max(5, floor((BuyAuren × 0.25) / 5) × 5)`

This rounds down to the nearest 5 Auren while preserving a minimum 5-Auren resale value for a sellable normal-stock Consumable.

Purpose:
- using Consumables should normally be better value than liquidating them;
- found/quest-issued normal supplies may still be converted to modest cash if the player prefers;
- resale should not become a major alternate income engine;
- no buy/sell arbitrage is possible.

## Exact sell table
| ID | Consumable | Buy Auren | Sell Auren |
|---|---|---:|---:|
| C01 | **Field Salve** | 20 | **5** |
| C02 | **Restorative Salve** | 50 | **10** |
| C03 | **Vital Salve** | 120 | **30** |
| C04 | **Grand Salve** | 240 | **60** |
| C05 | **Company Salve** | 200 | **50** |
| C06 | **Flow Tonic** | 80 | **20** |
| C07 | **Deepflow Tonic** | 200 | **50** |
| C08 | **Highflow Tonic** | 360 | **90** |
| C10 | **Rousing Salts** | 60 | **15** |
| C11 | **Greater Rousing Salts** | 160 | **40** |
| C12 | **Trauma Remedy** | 15 | **5** |
| C13 | **Stability Remedy** | 15 | **5** |
| C14 | **General Remedy** | 50 | **10** |
| C15 | **Full Remedy** | 140 | **35** |
| C16 | **Blinding Mist** | 10 | **5** |
| C17 | **Null Seal** | 70 | **15** |
| C18 | **Balance Seal** | 60 | **15** |

## Reward-only Consumables
The following finite reward-only items are **not sellable**:
- C09 **Reservoir Tonic**;
- C19 **Emergency Kit**;
- C20 **Emergency Rally**.

Their listed Auren-equivalent values are reward-balancing references, not vendor purchase prices and not resale values.

## No vendor variance
- all eligible vendors use the same sell values;
- no chapter depreciation/appreciation;
- no faction bonus;
- no hidden merchant skill modifier;
- no random resale-price fluctuation.

## Quest-reward implication
Normal-stock Consumables received from Side Quests or Character Quests use this same resale table. Their full shop price remains the correct reward-equivalence value; their sell value is intentionally much lower.
