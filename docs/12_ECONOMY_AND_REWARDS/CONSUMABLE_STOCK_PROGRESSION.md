# Diyse — Consumable Stock Progression

**Status:** CURRENT STOCK AUTHORITY

## Stock classes
### Normal stock
Normal purchasable Consumables use:
> **UNLIMITED NORMAL STOCK ONCE UNLOCKED**

unless a specific authored story state temporarily restricts access.

### Limited premium stock
Reservoir Tonic, Emergency Kit, and Emergency Rally use a separate permanent rule:
> **1 copy of each premium Consumable in every Consumable-selling shop from that shop's first accessible state; no restock.**

They are purchasable from the beginning of the normal shop economy, but intentionally scarce and expensive.

This means:
- Chapter 0 still has no normal shop loop;
- the first actual premium-shop opportunity begins with the first normal Consumable shop access in Chapter 1;
- every later Consumable-selling commerce endpoint receives its own one-copy stock when that endpoint first becomes accessible.

## Chapter 0 authored field issue
Chapter 0 begins with:
- the provisional starting-wallet amount owned by `CHAPTER_00_FIELD_ISSUE.md`;
- **3 Field Salves** issued to Cyanis.

Reliable normal purchasing still begins in Chapter 1.

## Premium price boundary

Exact numeric premium prices live in `CONSUMABLE_PRICES.md` and remain provisional pending the economy rebuild.

The structural stock rule here does not relock those values; early scarcity remains a function of limited one-copy-per-shop availability plus whatever prices are ultimately recertified.
## Premium per-shop rule
Every commerce endpoint that actually sells Consumables carries:
- **1 Emergency Kit**
- **1 Reservoir Tonic**
- **1 Emergency Rally**

from that shop's first accessible state.

Rules:
- quantities are tracked separately for each shop and each premium identity;
- no automatic replenishment;
- purchasing the copy permanently reduces that shop's stored quantity to zero;
- authored guaranteed pickups do not consume any shop's stock;
- there is no shared global premium-stock cap;
- a location that is not a Consumable-selling shop does not receive premium stock merely because it is a settlement or service point.

## Reliable normal-stock progression spine
### Chapter 1 / early core
Reliable unlimited core includes:
- Field Salve
- Rousing Salts
- Blinding Mist
- Trauma Remedy early enough for Bleed pressure

Premium stock is already present at applicable shops under the one-copy rule above.

### By late Chapter 2
Add reliable unlimited access to:
- Restorative Salve
- Flow Tonic

### By Chapter 3
- Stability Remedy is available before first Chapter-3 Stun pressure and remains reliably available for Chapter-4 Freeze.
- General Remedy enters core/regional stock.

### Chapter 4–5
Add unlimited normal stock for:
- Null Seal
- Balance Seal
- Vital Salve by Chapter 5

### Chapter 6
Add unlimited normal stock for:
- Deepflow Tonic
- Greater Rousing Salts

### Chapter 7–8
Add unlimited normal stock for:
- Full Remedy

### Chapter 8
Add reliable unlimited normal-stock access to:
- Company Salve

Guaranteed authored Reservoir Tonic / Emergency Kit pickups remain separate free rewards.

### Chapter 9
Larkspire Regional Market introduces unlimited normal stock for:
- Grand Salve
- Highflow Tonic

Their numeric prices are owned by `CONSUMABLE_PRICES.md` and remain provisional.

### Chapter 10+
No new unlimited normal-stock Consumable tier is required.
Premium items have already been present throughout the shop economy under the one-copy-per-shop rule.

## Cresthaven / Vhalmarch / later endpoints
When Cresthaven Quartermaster first becomes a Consumable-selling requisition endpoint, it receives:
> **1 Emergency Kit + 1 Reservoir Tonic + 1 Emergency Rally**

When Vhalmarch Forward Supply first becomes a Consumable-selling endpoint, it receives:
> **1 Emergency Kit + 1 Reservoir Tonic + 1 Emergency Rally**

The same rule applies to any other authored Consumable shop when it first becomes accessible.

## Carry-forward
Once unlocked, normal-stock Consumables carry forward to later full-service endpoints and Cresthaven consolidation.

Premium items do **not** become unlimited stock. Their one-copy-per-shop cap is permanent unless explicitly revised.
