# Diyse — Retired Terminology Map

Use this file when cleaning old text, code comments, filenames or notes.

| Retired / old | Current |
|---|---|
| Southhold | Yahtrenhold |
| The Crownhold / Crownhold | Yahtrenhold |
| Heartlands | Yahtrenhold |
| Edgelands | The Westways |
| Diysereach | The Greyspires |
| Highlands as formal region | The Greyspires |
| Blackstone | Black Host Territory |
| Black Mountains | The Blackspine / Black Host Territory according to meaning |
| Hostlands as formal region | Black Host Territory |
| Westreach | Westguard |
| Yahtrens Stand | Westguard |
| Waystone Cut | Ridgecut |
| Westline Relay as formal name | Westline |
| Elemental Hexarch | Reaction Conduit |
| Sixfold Annex | Reaction Annex |
| Sixfold Node | Reaction Node |
| Sixfold Crucible | Regulation Crucible |
| Long Day | The Last Day |
| Resource Face | Perception |
| Acuity Face | Perception |
| Change Face | Memory |
| Last Measure | Last Cartographer |
| Sixfold Accord | Sixfold Volition |
| Crest Magus | Crest Arcanist |
| Sixfold Knight | Proofhunter |
| Ruin Healer | Ruin Warden |
| Auren | G |
| MDEF / Magic Defense as display term | Spirit |
| Accuracy as character stat | no natural Accuracy; use Base Hit where appropriate |
| Concordant Prime stage | removed |
| Mastery Points | removed |
| Synthesis progression | removed |
| Barrier combat system | removed |
| Brace combat mechanic | removed |
| Break/Stagger meter | removed |
| general Accessory slot | removed |

## Character-name note
Canonical surnames are **not retired terminology**.

Current full names owned by the active character files include:
- Cyanis Dovaren
- Ilyra Amarin
- Torren Harth
- Nimera Pellan
- Vaelira Serren
- Seyrik Rell
- Maevra Solmar
- Kessara Durnan

First-name-only usage remains valid in dialogue/UI according to context, but it does not replace or retire the surname.

## Currency migration note
Current ordinary currency:
> **G**

Historical/current-facing economy text should not use **Auren** except when explicitly discussing retired provenance.

Current runtime/save storage uses `rewards.g`. Legacy schema-v1 `rewards.gold` is accepted only as a compatibility input and normalizes to `rewards.g` on load; do not introduce new live `gold` storage or player-facing terminology.

## Face migration note
Historical Face migration chain:
- Resource → Acuity → **Perception**
- Change → **Memory**

Current Face set:
> **Might / Elements / Grace / Perception / Memory / Ruin**

The word `change` remains valid ordinary English where it is not the retired Card-Face name.

## Context exceptions
Ordinary words are still valid where they are not retired mechanics:
- physical water
- environmental wind
- structural brace
- physical/security barrier
- descriptive highlands
- ordinary change/change of state
- ordinary perception
- ordinary memory
- ordinary resource

Archive filenames may retain old terminology.
