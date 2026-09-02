# Diyse — Consumable Sell Rule

**Status:** EXACT CONSUMABLE G RESALE AUTHORITY

This rule applies to sellable normal-stock Consumables. It does not change ordinary-equipment resale, Relics, Legacies, Forge Components, Key Items, Cards, or Primes.

## Core rule
Normal-stock Consumables sell for approximately **25% of their purchase price**:

> `SellG = max(50, floor((BuyG × 0.25) / 50) × 50)`

This rounds down to the nearest 50 G while preserving a minimum 50 G resale value for a sellable normal-stock Consumable.

Purpose:
- using Consumables should normally be better value than liquidating them;
- found/quest-issued normal supplies may still be converted to modest G if the player prefers;
- resale should not become a major alternate income engine;
- no buy/sell arbitrage is possible.

## Exact sell table
| ID | Consumable | Buy | Sell |
|---|---|---:|---:|
| C01 | **Field Salve** | 200 G | **50 G** |
| C02 | **Restorative Salve** | 500 G | **100 G** |
| C03 | **Vital Salve** | 1,200 G | **300 G** |
| C04 | **Grand Salve** | 2,400 G | **600 G** |
| C05 | **Company Salve** | 2,000 G | **500 G** |
| C06 | **Flow Tonic** | 800 G | **200 G** |
| C07 | **Deepflow Tonic** | 2,000 G | **500 G** |
| C08 | **Highflow Tonic** | 3,600 G | **900 G** |
| C10 | **Rousing Salts** | 600 G | **150 G** |
| C11 | **Greater Rousing Salts** | 1,600 G | **400 G** |
| C12 | **Trauma Remedy** | 150 G | **50 G** |
| C13 | **Stability Remedy** | 150 G | **50 G** |
| C14 | **General Remedy** | 500 G | **100 G** |
| C15 | **Full Remedy** | 1,400 G | **350 G** |
| C16 | **Blinding Mist** | 100 G | **50 G** |
| C17 | **Null Seal** | 700 G | **150 G** |
| C18 | **Balance Seal** | 600 G | **150 G** |

## Premium Consumables
The following limited-premium items are **not sellable**:
- C09 **Reservoir Tonic**;
- C19 **Emergency Kit**;
- C20 **Emergency Rally**.

They are purchasable in one-copy-per-shop premium stock and also have authored guaranteed sources, but resale remains disabled.

## No vendor variance
- all eligible vendors use the same sell values;
- no chapter depreciation/appreciation;
- no faction bonus;
- no hidden merchant skill modifier;
- no random resale-price fluctuation.

## Quest-reward implication
Normal-stock Consumables received from Side Quests or Character Quests use this same resale table. Their full shop price remains the correct reward-equivalence value; their sell value is intentionally much lower.
