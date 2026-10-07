# 08_ITEMS_AND_EQUIPMENT

**Status:** ACTIVE ITEMS / EQUIPMENT DOMAIN ROUTER  
**Authority:** current items/equipment-domain owner plus later explicit approved corrections.  

Canonical home for:
- ordinary equipment;
- Relics;
- native Legacies;
- equipment slot rules;
- donor equipment access references;
- consumable identities/functions;
- Legacy precursors and Character Quest Legacy Components;
- Forge Components;
- Kessara Relic-copy mechanics.

Economy values such as purchase price, sell value, shop stock, and reward-budget economics belong in `../12_ECONOMY_AND_REWARDS`.

Global combat behavior belongs in `../05_BATTLE_SYSTEM/BATTLE_SYSTEM_MASTER.md`.

## Battle-redesign boundary

Equipment raises the character's **visible combat stats directly** and may grant explicit passives. There is no hidden Weapon Power layer in the current damage formula.

The exact item catalog remains owned here, but combat-facing magnitudes/effects that depend on the redesigned formulas, statuses, timing, targeting, or stat set must be certified against the battle master before implementation. Consumable-specific exceptional behavior may override the battle master's default Item timing only when explicitly authored.

## Current active equipment count

| Layer | Count |
|---|---:|
| Ordinary equipment | **38** |
| Relics | **36** |
| Native Legacies | **17** |
| **Total equipment** | **91** |

Consumables and project/material items are tracked separately and are not counted in the 91-piece equipment total.

## Current supporting item counts

- Consumables: **20**
- Forge Components: **30**
- Character Quest Legacy Components: **6**
- Native Legacy precursors: **6**

## Major hierarchy

> **Ordinary < Relic < Legacy**

A Relic may retain a narrow specialist advantage. A Legacy is stronger overall as the late-game capstone layer.

Balance reference:
- `STARTING_LOADOUTS.md` records guaranteed starting/join equipment used to construct mandatory-route player bodies.
