# Diyse — Mandatory Chapter Spine
**Migration baseline:** `Diyse_CURRENT_WORKING_TRACKER_CONSOLIDATED_2026-08-27_v85.md`  
**Current whole-project written authority:** **v2.20 / Audit135**, read through all later explicit user corrections and current domain migrations.  
**Primary story authorities:** current chapter index; current chapter files and later explicit corrections; current Prime/character/world corrections.  
**Domain rule:** this folder owns mandatory story structure, chapter purpose, scene order, reveal order, recruitment/Prime milestones, interchapter causality, and story-state outcomes. Exact spoken dialogue belongs in `03_DIALOGUE`; battle numbers in `09_ENEMIES_AND_ENCOUNTERS`; progression numbers in `10_PROGRESSION_AND_EXP`.

## Global chapter-end cleanup / transition rule — LOCKED
For **every chapter that has a following chapter (Chapter 0 through Chapter 12)**:

1. The chapter's mandatory climax / final required story beat resolves **before** the chapter boundary.
2. The game then enters a **chapter-end cleanup period while still inside the current chapter**.
3. During cleanup, the player retains control and may use whatever content is legitimately available at that story state, including as applicable:
   - Hunts / return Hunts;
   - ordinary side quests;
   - Character-Life scenes;
   - permitted backtracking / exploration;
   - shopping, equipment, party formation, records, healing, saving, and preparation;
   - other optional cleanup content already unlocked and not barred by story geography or a point of no return.
4. Cleanup does **not** automatically open the entire world. Existing travel restrictions, story-state restrictions, location access, temporary closures, and point-of-no-return rules still apply.
5. Completing the final mandatory scene, resting, leaving a boss arena, or reaching the cleanup hub must **not automatically start the next chapter**.
6. The next chapter begins only when the player makes a **deliberate explicit advance-story choice** such as `Begin Chapter N`, `Depart`, `Start Operation`, or an equivalent clearly marked interaction appropriate to the chapter.
7. That choice is the actual chapter boundary. Any opening surprise, attack, travel sequence, overnight transition, or mandatory first event of the next chapter occurs **only after** the player chooses to advance.
8. If advancing will change or close currently available content, the transition should communicate that clearly enough for the player to understand they are leaving the cleanup period.

This rule supersedes older chapter scripts, line-complete staging, or summaries that automatically roll directly from one chapter's last mandatory scene into the next chapter.

**Chapter 13 exception:** Chapter 13 is the final chapter and has no following chapter. Diyse has no post-game, so this rule does not create a post-ending cleanup state after the final ending.

## Chapter spine

| Ch | Current identity / title | Core function |
|---:|---|---|
| 0 | **The Broken Convoy** | Cyanis convoy disaster; Ilyra joins through independent Blue Warden duty; sealed Card gives an incomplete green/gold protective response but remains unidentified; no Player Levels; Field Triage Camp cleanup with C01/C02 before the player deliberately departs for Brackenwall / begins Chapter 1. |
| 1 | **Brackenwall and the Wayfinder** | Torren joins; Hollow Watch / Briar Passage / Wayfinder cartographic mystery begins; Wayfinder-area cleanup before player chooses to continue toward Dunmere and confirms **Start Chapter 2**. |
| 2 | **The Drowned Oath** | Chapter opens on the path immediately outside Dunmere; missing-traveler crisis; covert Red Transfer Bastion infiltration through old waterworks into the Sunken Archive; complete western-half Diysean map reveals the broader route network and lines continuing beyond its edges; Archive Leviathan; old secret passage leads directly into the Prisoner Galleries; prisoners reveal the Bastion is a holding/transit site and identify Commander Rhazek; Bastion command ascent; Rhazek and masked Seyrik foreshadowing; Rhazek is defeated locally and withdraws; party returns to free the prisoners, then the story cuts directly back to Dunmere where the elder confirms the rescued people are safe and direct Greenhollow–Dunmere travel is reopened; Dunmere cleanup before the player explicitly starts Chapter 3. |
| 3 | **The Old City and Last Sentinel** | Queen-seal mystery; Nimera joins; First Command Warden; ancient seal-working chamber; Prime / Might / Last Sentinel identified but Last Sentinel not yet Recovered; Cresthaven established as headquarters; after the handoff Maevra returns to Caelora with Mirena and the resident/traveling permanent group becomes Cyanis + Ilyra + Torren + Nimera; **H01 + H03** / Archive Judgment Engine / other eligible cleanup before player chooses Chapter 4. |
| 4 | **The Seventh Reaction** | Last Sentinel first manifests / becomes Recovered in S022 after the player starts Chapter 4; Vaelira joins; four-element Reaction Annex crisis; Seventh Reaction defeated; cleanup before Chapter 5. |
| 5 | **The Mountain Engine — inherited current identity** | Stonewake→Emberforge→Deepforge; Last Sentinel awakening; Last Cartographer acquisition; Seyrik/Rhazek pre-reveal continuity; cleanup before Chapter 6. |
| 6 | **current Frostmere / Weather Crown / Crimson Work chapter** | Last Convergence acquired; Zevraya climax; Seyrik breaks from Black Host and joins by chapter end; cleanup before Chapter 7. |
| 7 | **The Prison of Names** | first full-six chapter; Prison identity crisis; Last Scribe recovered; Sixfold Volition at end; cleanup before Chapter 8. |
| 8 | **current Horizon Vault / Westguard / Varkesh chapter** | Last Cartographer awakens; Last Erasure recovered; western counteroffensive; Varkesh escapes after defeat; cleanup before Chapter 9. |
| 9 | **Larkspire / Crownfall / Rhazek** | Equal Mercy + Last Sanctuary; Crownfall invasion; Rhazek climax; chapter ends at Crownfall; cleanup before Chapter 10. |
| 10 | **The Last Blank** | Mirena lead → Cerythvale → Eastern Wayfinder discovery → map mystery completion → Calder provenance → Registry Warden / Buried Registry → Mirena verification; cleanup before Chapter 11. |
| 11 | **Crown Engine / Calder / Custodian / Truth** | Calder / Living Anchor conflict; Custodian; ancient truth; Last Scribe awakening; strategic handoff into final Black Host campaign; cleanup before Chapter 12. |
| 12 | **The Reforged March** | Black Host Territory invasion; Varkesh captured alive; Vhalmarch secured; Vaelkor defeated; Last Erasure awakening; mandatory cleanup / preparation period before the player chooses Chapter 13. |
| 13 | **The Last Command** | Deepest City; survival truth; Last Weapon Archon; Last Shelter; Reconstituted Entity → Last Command; Final Severance; ending. No post-game. |

## Title-status rule
Where the current repository index does not certify a formal chapter title, this migration preserves the current chapter **identity** rather than inventing one.

In particular, do not force a new formal title for Chapters 6, 8, 9 or 11 merely to make the index look symmetrical.