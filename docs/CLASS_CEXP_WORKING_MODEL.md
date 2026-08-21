# Diyse — CL13 Class EXP Working Model

**Status:** ACTIVE WORKING DESIGN — NOT MASTER CANON  
**Parent tracker:** `docs/CLASS_REWORK_MASTER_TRACKER.md`  
**Parent whole-project authority:** v1.84 / Audit99 plus newer explicit class-rework decisions.

## 1. Purpose

This file models Class EXP pacing for the proposed **Base CL1–13 / Subclass CL1–13** architecture. It is intended to keep class progression meaningful through the campaign-only Level ~55 finish while leaving optional Level 56–60 play useful for players who split Focus or want to finish both class lines.

Class EXP remains separate from Character EXP. The currently selected class receives CEXP; the unselected class receives none. Before the Sixfold Accord only Base Focus exists.

## 2. Proposed shared CL13 threshold curve

Use the same cumulative threshold curve for Base and Subclass unless later testing demonstrates a need to separate them.

| Class Level | Cumulative CEXP | CEXP to next |
|---:|---:|---:|
| CL1 | 0 | 150 |
| CL2 | 150 | 200 |
| CL3 | 350 | 250 |
| CL4 | 600 | 350 |
| CL5 | 950 | 400 |
| CL6 | 1,350 | 450 |
| CL7 | 1,800 | 500 |
| CL8 | 2,300 | 550 |
| CL9 | 2,850 | 600 |
| CL10 | 3,450 | 700 |
| CL11 | 4,150 | 800 |
| CL12 | 4,950 | 1,050 |
| CL13 | **6,000** | — |

Design reasons:
- 6,000 is long enough to spread a fresh Subclass across the post-Accord campaign.
- Early levels are deliberately less compressed than the retired 4,800-CEXP CL12 implementation table, so donor equipment learned by CL5 does not all arrive after only a handful of fights.
- Late levels deliberately lengthen so Trait III and the Ultimate remain meaningful late-campaign goals.
- Exact encounter CEXP rewards are not yet locked and must be calibrated against Audit99's actual encounter counts.

## 3. Base learning schedule paired to the curve

| Base CL | Major class result | Cumulative CEXP |
|---:|---|---:|
| 1 | Trait I + Base Abilities 1–3 + starting equipment | 0 |
| 3 | Base Ability 4 | 350 |
| 5 | Native advanced equipment permission where one exists | 950 |
| 6 | Base Ability 5 + Trait II | 1,350 |
| 9 | Base Ability 6 | 2,850 |
| 12 | Trait III | 4,950 |
| 13 | Base Ultimate | 6,000 |

Base CL5 remains class-specific: Cyanis second Sword, Ilyra Shield, Nimera two-handed Conduits; Vaelira Focus remains the leading candidate; Torren and Seyrik must not receive fabricated equipment permissions merely for symmetry.

## 4. Subclass learning schedule paired to the curve

| Subclass CL | Major class result | Cumulative CEXP |
|---:|---|---:|
| 1 | Donor Primary + Trait I + Ability 1 | 0 |
| 3 | Donor Armor | 350 |
| 4 | Ability 2 | 600 |
| 5 | Donor advanced equipment permission / Secondary package where applicable | 950 |
| 6 | Trait II | 1,350 |
| 7 | Ability 3 | 1,800 |
| 9 | Ability 4 | 2,850 |
| 11 | Ability 5 | 4,150 |
| 12 | Trait III | 4,950 |
| 13 | Subclass Ultimate | 6,000 |

## 5. Recruitment starting Base CL values

When a character joins above CL1, begin them exactly at the threshold for their authored starting Base CL unless a later balance pass intentionally gives partial progress.

| Character | Recruitment | Starting Base CL | Starting cumulative CEXP |
|---|---|---:|---:|
| Cyanis | Chapter 0 | CL1 | 0 |
| Ilyra | Chapter 0 | CL1 | 0 |
| Torren | Chapter 1 | CL4 working | 600 |
| Nimera | Chapter 3 | CL4 working | 600 |
| Vaelira | Chapter 4 | CL7 working | 1,800 |
| Seyrik | Chapter 6 | **CL8** | **2,300** |

Seyrik CL8 is an explicit current design decision. He therefore reaches CL9 / Call Shardfang through player-controlled growth after recruitment rather than arriving with it.

## 6. Target natural progression windows

These are pacing targets, not hard character-level gates.

### Base line before/around the Accord

For Cyanis/Ilyra and other characters with substantial pre-Accord availability, target roughly:
- early Ch1: CL1;
- Ch2: CL3–4 neighborhood;
- Ch3: CL5–6 neighborhood;
- Ch4: CL7–8 neighborhood;
- Ch5: CL9–10 neighborhood;
- Ch6 / approach to Accord: CL10–12 neighborhood;
- Base CL13: normally earned during Ch7–8 if the player continues Base Focus after Subclasses unlock.

This intentionally prevents the Sixfold Accord from automatically meaning “Base class finished.”

### Fresh Subclass after the Accord

A character who selects and mostly maintains Subclass Focus should target roughly:
- Ch7: foundational CL1–5 development, including donor equipment package by CL5;
- Ch8: around CL6–7;
- Ch9: around CL7–8;
- Ch10: around CL9–10;
- Ch11: around CL10–12;
- Ch12 / campaign-only Level ~55 finish: CL13 Ultimate.

Optional/Hunt-heavy play may reach milestones earlier. Frequent Base/Subclass switching delays the selected line naturally. Levels 56–60 remain useful completion space for players finishing both class lines.

## 7. Required CEXP reward calibration

Do not copy Character EXP values into CEXP. CEXP should use compact authored rewards appropriate to class progression.

Next numerical pass must derive:
1. ordinary random-encounter CEXP bands by campaign stage;
2. Elite/miniboss CEXP multipliers;
3. story-boss CEXP values;
4. Hunt and Major Hunt CEXP values;
5. whether reserves receive the same selected-class CEXP as active members under the current full-roster progression rule;
6. simulations for a Base-focused, Subclass-focused, 50/50 split, and optional-heavy player;
7. proof that Subclass CL13 lands near the Level ~55 campaign finish for a predominantly Subclass-focused character rather than far earlier.

## 8. Mastery interaction — not yet reconciled

This CEXP model does not move Equipment Mastery onto ordinary class levels. Mastery Points and the four Core / four Subclass / one Synthesis architecture remain a separate system until explicitly revised.

The old Synthesis prerequisite of both classes at CL12 must be reconsidered for the new CL13 cap. Do not automatically convert that requirement without a dedicated mastery pass.
