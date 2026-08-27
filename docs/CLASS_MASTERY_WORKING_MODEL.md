# Diyse — CL13 Mastery / Relic / Legacy Working Model

**Status:** ACTIVE WORKING DESIGN — AUDIT117-ALIGNED  
**Current whole-project authority:** **v2.02 / Audit117**  
**Parent trackers:** `docs/CLASS_REWORK_MASTER_TRACKER.md`, `docs/CLASS_CEXP_WORKING_MODEL.md`

## 1. Purpose

This file reconciles the Mastery architecture against the current Base CL13 / Subclass CL13 class structure after Audit117.

The active Mastery architecture is now:

- **4 Core Mastery nodes**
- **4 Subclass Mastery nodes**
- **no Synthesis node**

Each purchased Mastery node costs 1 Mastery Point unless separately revised.

Mastery remains separate from ordinary Class Level rewards. Reaching the required Class Level makes a Mastery node eligible; the node is not acquired until the player spends the required Mastery Point.

---

## 2. Mastery Point economy — now requires reconciliation

The inherited grant schedule previously supplied exactly 9 Mastery Points because the old architecture contained:

- 4 Core nodes
- 4 Subclass nodes
- 1 Synthesis node

Audit117 removes Synthesis, leaving only **8 active Mastery nodes**.

Therefore the old 9-point grant schedule is **not automatically final current canon**.

Do not silently preserve a ninth mandatory point solely because the retired Synthesis architecture used one.

The dedicated progression pass must decide whether to:

- remove one inherited Mastery Point grant;
- keep one optional/unspent surplus point;
- or repurpose the point through a separately approved system.

Until that decision is made, the exact total Mastery Point economy remains **OPEN**.

---

## 3. Core Mastery gate schedule

The current working Core gates remain:

| Core node | Base-Class eligibility gate | Intent |
|---:|---:|---|
| Core 1 | **Base CL3** | first meaningful Base specialization |
| Core 2 | **Base CL5** | mid-Base refinement |
| Core 3 | **Base CL7** | mature Base technique refinement |
| Core 4 | **Base CL9** | late Base mastery |

Each costs 1 Mastery Point.

A character's own native Legacy project ultimately requires all four Core Masteries under Audit117.

---

## 4. Subclass Mastery gate schedule — Audit117

| Subclass node | Eligibility gate | Current function |
|---:|---:|---|
| Subclass 1 | **Subclass CL3** | first donor-derived refinement; donor Armor access is online at this tier |
| Subclass 2 | **Subclass CL5** | second refinement; donor Secondary access is online where applicable |
| Subclass 3 | **Subclass CL7** | **Equipment Mastery — donor Relic access** |
| Subclass 4 | **Subclass CL11** | **Legacy Mastery — donor Legacy access** |

Each costs 1 Mastery Point.

### Subclass Mastery 3 — Equipment Mastery

At Subclass CL7, Node 3 becomes eligible.

Purchasing it grants permission to equip the linked donor character's **already-obtained Relic equipment**.

It does not:
- create another Relic;
- grant a Relic automatically;
- change the Relic's slot architecture.

### Subclass Mastery 4 — Legacy Mastery

At Subclass CL11, Node 4 becomes eligible.

Purchasing it grants permission to equip the linked donor character's **already-obtained native Legacy equipment**.

It does not:
- complete the donor's Legacy project;
- create another Legacy item;
- alter the donor's slot architecture;
- gate the native owner's use of their own Legacy equipment.

This replaces the retired Synthesis gate.

---

## 5. Current Subclass progression rhythm

The controlling late progression is:

- CL1 — Ability 1 + Trait I + donor Primary access
- CL3 — Subclass Mastery 1 eligibility + donor Armor access
- CL4 — Ability 2
- CL5 — Subclass Mastery 2 eligibility + donor Secondary access
- CL6 — Trait II
- CL7 — Ability 3 + Subclass Mastery 3 / Equipment Mastery eligibility
- CL9 — Ability 4
- CL10 — **Ability 5**
- CL11 — **Subclass Mastery 4 / Legacy Mastery eligibility**
- CL12 — Trait III
- CL13 — Subclass Ultimate + cap

Important supersessions:

- Equipment Mastery is no longer CL10.
- Donor Relic access is no longer late-CL10 progression.
- Ability 5 is CL10 rather than CL11.
- Subclass Mastery 4 is CL11 rather than CL10.
- Donor Legacy access is handled directly by Subclass Mastery 4 at CL11.
- **Synthesis is removed.**

---

## 6. Donor / receiver map

Reciprocal pair structure:

- Cyanis ⇄ Vaelira
- Ilyra ⇄ Seyrik
- Torren ⇄ Nimera

Directional linked-equipment access:

- Cyanis ← Vaelira
- Ilyra ← Seyrik
- Torren ← Nimera
- Nimera ← Torren
- Vaelira ← Cyanis
- Seyrik ← Ilyra

The linked receiver accesses the donor's existing obtained item. No separate shared Relic or shared Legacy artifact is created.

---

## 7. Native Legacy completion is separate from Subclass Mastery

A character's own native Legacy completion is controlled by Audit117.

It requires:
- Base CL13;
- all 4 Core Masteries;
- Character Quest / resolution;
- unique Character Quest Legacy Component;
- unique Legacy precursor;
- Legacy Gate A material;
- Legacy Gate B material;
- Kessara project availability.

It does **not** require:
- Subclass CL13;
- all 4 Subclass Masteries;
- Equipment Mastery;
- Legacy Mastery;
- Synthesis.

Subclass Masteries 3 and 4 control only cross-character donor equipment permission.

---

## 8. Current unresolved items

The following remain open:

1. exact post-insertion CEXP timing for CL7 / CL11 / CL13;
2. exact Mastery Point grant schedule now that only 8 nodes exist;
3. whether any inherited Level-based MP grant should be removed or become optional surplus;
4. final implementation UI labels for Subclass Mastery 3 / 4 if `Equipment Mastery` / `Legacy Mastery` are not final display names;
5. synchronization of older repository files that still describe Synthesis as active.

---

## 9. Current hard decisions

- Base cap = **CL13**.
- Subclass cap = **CL13**.
- Active Mastery count = **8**: 4 Core + 4 Subclass.
- **No Synthesis node exists.**
- Subclass Mastery 3 eligibility = **CL7** and grants donor Relic access when purchased.
- Subclass Ability 5 = **CL10**.
- Subclass Mastery 4 eligibility = **CL11** and grants donor Legacy access when purchased.
- Native Legacy completion does not require Subclass progression.
- Linked donor access grants permission to equip an already-obtained item, not a duplicate artifact.

Where this file conflicts with Audit117, Audit117 controls.
