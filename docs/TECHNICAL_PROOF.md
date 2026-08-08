# Step 7B.5 — Technical Feasibility & Vertical Slice Proof

## Purpose

Prove that the intended Diyse architecture can grow into the full game **before** full Step 7C dialogue-first scene writing begins.

This is not a content demo. Placeholder assets and temporary data are acceptable. The architecture, transitions, rules, and Android behavior are what matter.

## Gate A — 2.5D exploration proof

Build one small graybox area containing:

- real 3D ground/architecture;
- real depth and elevation;
- at least one occluder that can pass in front of the character;
- a stylized 2D/2.5D Cyanis placeholder that occupies the 3D world convincingly;
- collision;
- camera behavior suitable for the chosen 2.5D presentation;
- keyboard/gamepad-friendly desktop controls for development;
- touch movement/interaction controls for Android;
- one NPC;
- one interactable object;
- one area/room transition;
- at least one basic ambient effect.

### Gate A passes when

- movement, depth, occlusion, floor contact, camera readability, and touch control all work coherently;
- the character does not visibly float, clip, or sort incorrectly in ordinary traversal;
- the prototype demonstrates a credible path to final 2.5D presentation rather than relying on an unrelated fallback technique;
- the same area runs acceptably on an Android device.

## Gate B — authored dialogue presentation proof

Implement one disposable authored conversation with no player response choices.

It must prove:

- speaker name and dialogue text;
- illustrated portrait display;
- multiple expression states for at least two speakers;
- left/right or otherwise clearly staged speaker presentation;
- manual advance;
- configurable text speed;
- authored pauses/timing hooks;
- portrait-only reaction beats with no spoken line;
- an interruption or expression change inside the exchange;
- clean return to exploration control;
- ability to trigger from world state rather than hard-coded scene startup.

### Gate B passes when

- the system supports authored cinematic dialogue without requiring branching response architecture;
- portrait/expression timing does not require emotional information to be redundantly written into text;
- the system can be driven by data or authored scene records rather than bespoke UI code for each conversation.

## Gate C — real Diyse combat architecture proof

Use a placeholder encounter with four party members and multiple enemies.

Required commands:

- Attack
- Ability
- Card
- Item
- Defend

Required rules:

1. Beginning-of-round effects/state checks resolve.
2. Enemies lock one legal action each from the legitimate beginning-of-round state without inspecting unconfirmed player commands.
3. The player selects one action for every conscious active party member before confirmation.
4. Item actions resolve first, ordered by current effective Speed.
5. Defend actions resolve second, ordered by current effective Speed.
6. All remaining party/enemy actions resolve from highest to lowest current effective Speed.
7. Party members win exact Speed ties against enemies.
8. Tied party members use player-selected order.
9. Tied enemies/entities use stable deterministic order.
10. Speed determines order only and never grants an extra ordinary action.

Also prove:

- HP;
- MP;
- KO;
- targeting;
- at least one status effect;
- victory and defeat;
- encounter rewards;
- clean return to exploration.

### Gate C passes when

The resolver follows the actual round architecture and is not secretly implemented as a timeline/ATB system with round-like presentation.

## Standard Card proof

Implement exactly one placeholder Standard Card sufficient to prove:

- Card command/menu integration;
- legal targeting/effect execution;
- unlimited-use architecture;
- compatibility with the ordinary round resolver;
- no charge, Essence, rank, or per-battle use-counter architecture.

Do not implement all 24 Standard Cards during 7B.5.

## Prime proof

Implement one placeholder Prime manifestation sufficient to prove:

- Prime activation path;
- manifestation entry;
- direct player control of Prime actions where required by current Prime rules;
- separate Prime action presentation;
- legal exit/cleanup;
- correct return to the ordinary battle state.

Do not implement final First Champion content/art during 7B.5.

## Save/load proof

Persist and restore at least:

- current area;
- Cyanis/player position or an authored safe resume point;
- party state;
- character stats needed by the proof;
- inventory proof data;
- Card proof data;
- one equipment placeholder;
- one story/quest flag;
- one opened/changed interactable;
- one NPC state change.

Close the application completely, reload the save, and verify persistence.

## Android gate

A desktop run is not enough.

The proof must eventually produce an installable Android build and validate:

- landscape layout;
- touch controls;
- text readability;
- portrait readability;
- battle command sizing;
- menu navigation;
- exploration/dialogue/combat transitions;
- save/load;
- suspend/resume behavior where feasible;
- load time;
- frame pacing/performance on a real device.

## Explicitly out of scope for 7B.5

Do not build the whole game.

Not required yet:

- final Chapter 0 content;
- all six final playable implementations;
- finished maps;
- final art/portraits/animation;
- all 24 Standard Cards;
- all 12 Primes;
- all classes/Abilities/equipment;
- final enemy catalog;
- final UI;
- final audio;
- full script;
- final cinematics.

## Final 7B.5 acceptance flow

The technical proof is considered successful only when a user can:

1. launch the Android build;
2. load or start the proof state;
3. move Cyanis through the 2.5D area;
4. encounter ambient/world interaction;
5. enter an authored portrait conversation;
6. return to exploration;
7. enter a four-character round-based battle;
8. use an Ability;
9. use the Standard Card proof;
10. invoke the Prime proof;
11. win;
12. return to exploration;
13. change persistent world state;
14. save;
15. close the game;
16. reopen and reload;
17. verify the saved state remains correct.

Passing 7B.5 means the architecture is credible enough to resume full narrative production and expand the game deliberately.
