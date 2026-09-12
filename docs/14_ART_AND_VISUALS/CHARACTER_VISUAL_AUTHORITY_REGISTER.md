# Diyse — Character Visual Authority Register

**Status:** ACTIVE NAVIGATION REGISTER  
**Primary current-character authority:** [`PRODUCTION/CHARACTERS/README.md`](PRODUCTION/CHARACTERS/README.md)  
**Current master-image folder:** [`asset_sources/characters/current/`](../../asset_sources/characters/current/)

This register is a navigation layer. It does **not** override current repository master images or their matching visual-lock documents.

## Authority order for current repository-master characters

1. current repository master image in `asset_sources/characters/current/`;
2. matching `PRODUCTION/CHARACTERS/*_CURRENT_VISUAL_LOCK.md`;
3. current Diyse B00 / HD-2D visual-style rules;
4. older migration prose, archived renders, historical fingerprints, generated filenames, or superseded concept notes.

Do not infer or restore surnames for the current master characters from retired filenames or old migration documents.

## Current repository-master characters

| Character | Status | Exact master | Current lock |
| --- | --- | --- | --- |
| Cyanis | **LOCKED** | `asset_sources/characters/current/cyanis.jpg` | `PRODUCTION/CHARACTERS/CYANIS_CURRENT_VISUAL_LOCK.md` |
| Ilyra | **LOCKED** | `asset_sources/characters/current/ilyra.jpg` | `PRODUCTION/CHARACTERS/ILYRA_CURRENT_VISUAL_LOCK.md` |
| Torren | **LOCKED** | `asset_sources/characters/current/torren.jpg` | `PRODUCTION/CHARACTERS/TORREN_CURRENT_VISUAL_LOCK.md` |
| Nimera | **LOCKED** | `asset_sources/characters/current/nimera.jpg` | `PRODUCTION/CHARACTERS/NIMERA_CURRENT_VISUAL_LOCK.md` |
| Vaelira | **LOCKED — 2026-09-12 B00** | `asset_sources/characters/current/vaelira.png` | `PRODUCTION/CHARACTERS/VAELIRA_CURRENT_VISUAL_LOCK.md` |
| Seyrik | **LOCKED** | `asset_sources/characters/current/seyrik.jpg` | `PRODUCTION/CHARACTERS/SEYRIK_CURRENT_VISUAL_LOCK.md` |
| Maevra | **LOCKED** | `asset_sources/characters/current/maevra.jpg` | `PRODUCTION/CHARACTERS/MAEVRA_CURRENT_VISUAL_LOCK.md` |
| Kessara | **LOCKED** | `asset_sources/characters/current/kessara.png` | `PRODUCTION/CHARACTERS/KESSARA_CURRENT_VISUAL_LOCK.md` |

The first six are the permanent playable party. Maevra and Kessara are supporting-character visual masters.

## Other registered visual authorities

The following entries remain registered from the wider art documentation. They are **not** part of the eight-file repository-master set above, and this register does not attempt to reconstruct their exact image minutiae:

- Queen Lysara Ceryth — locked supporting-character visual authority;
- Crown Princess Mirena Ceryth — locked portrait/turnaround authority;
- Prince Alaric Ceryth — locked visual authority;
- Princess Nalia Ceryth — locked visual authority;
- Commander Rhazek — locked multi-form visual authority;
- Matron Zevraya — locked visual master set;
- Marshal Varkesh — locked visual authority;
- Emperor Vaelkor Draeven — locked antagonist visual authority;
- Chancellor Othmar Calder — locked visual set;
- Reconstituted Entity / Last Command — locked final-boss visual set.

Where an exact approved image exists for one of these characters, preserve that image as source authority rather than inventing missing details from memory. If one of these characters receives a current repository master later, add it to `asset_sources/characters/current/` and create/update its production visual-lock document before promoting it into the current-master section above.

## Retired migration contamination

Older art documents may contain obsolete surnames, older generated-image hashes, superseded costume descriptions, or retired character proportions. Those records are historical only when they conflict with the current authority system.

In particular, older visual files for the permanent six and for Maevra/Kessara have been replaced by surname-free navigation files under `CHARACTERS/PLAYABLE/` and `CHARACTERS/SUPPORTING/` that point to the current production locks.
