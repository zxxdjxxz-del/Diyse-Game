# Diyse — Active Engineering Canon Guardrails

This file is an implementation-facing summary. It does **not** replace the authoritative Diyse master canon, protected character source files, or newer explicit user approvals. If this summary conflicts with a newer controlling project authority, the newer authority wins and this file must be updated deliberately.

## Project foundation

- Diyse is a mature fantasy JRPG with an approximately 20-hour critical path.
- Permanent roster: exactly six — Cyanis Dovaren, Ilyra Amarin, Torren Harth, Nimera Pellan, Vaelira Serren, Seyrik Rell.
- Maximum active permanent battle party: four.
- Character level cap: 50.
- Each permanent character has exactly one Base Class and one Subclass.
- Combat is command-driven and turn-based using discrete rounds.
- MP is the universal ordinary Ability resource.
- There are no character-specific combat gauges/resources.
- Permanent battle commands: Attack / Ability / Card / Item / Defend.
- Current Card collection: 24 Standard Cards + 12 Prime Cards.
- Current Faces: Might, Elements, Grace, Resource, Change, Ruin.
- After-story free roam exists; no exclusive post-ending progression or hidden true ending.

## Presentation supersession

Diyse is now a **2.5D** game. This supersedes older implementation text that described the game as fully 3D.

The target combines:

- 3D environments and real world depth;
- 3D lighting, scale, traversal, architecture, battle spaces, bosses, Black Host spaces, and Prime spectacle;
- stylized 2D/2.5D character presentation;
- expressive illustrated dialogue portraits where appropriate.

The technical proof may use placeholder assets, but must test the actual 2.5D layering/occlusion/camera problem rather than quietly reverting to an all-3D or pre-rendered-field game.

## Dialogue supersession

Diyse has **no player dialogue choices**.

Cyanis is a defined authored protagonist. Do not implement response wheels, tone menus, affinity dialogue, branching player-spoken responses, persuasion trees, good/evil dialogue, or romance dialogue choices.

## Permanent character/class/story-Prime identities

- Cyanis — Crest Knight / Crest Magus — Might / First Champion
- Ilyra — Blue Warden / Vowblade — Grace / First Mercy
- Torren — War Archer / Diysean Marksman — Resource / First Sovereign
- Nimera — Cardweaver / Sixfold Knight — Change / First Change
- Vaelira — Green Arcanist / Prism Archer — Elements / First Element
- Seyrik — Ruin Vanguard / Ruin Reclaimer — Ruin / First Reckoning

Maevra is a temporary playable/recurring major ally, not a permanent progression character. Kessara is a nonplayable recurring technical ally.

## Relationship/story guardrails relevant to engineering

- No romance system, affection meter, jealousy system, triangle, triad, or route.
- Authored relationships can exist without gameplay meters.
- Cyanis and Ilyra have an authored mutual love relationship.
- Torren and Maevra have an authored adult intimate relationship.
- All six permanent characters survive the canonical ending.
- Vaelkor does not knowingly ally with the surviving fragment. The fragment covertly influences him and extends his life for nearly 300 years; the influence is subtle and does not remove his agency or responsibility.

## Historical repository rule

The older `zxxdjxxz-del/Diyse` repository is **historical prototype material only**. Its libGDX architecture, fixed/pre-rendered field experiments, old branches, temporary formulas, assets, and prototype mechanics are not implementation authority for `Diyse-Game`.
