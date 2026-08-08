# Tests

Step 7B.5 should build a regression suite alongside the prototype.

Priority areas:

- deterministic round resolution;
- priority tiers;
- Speed tie rules;
- enemy action locking;
- targeting legality;
- state/effect application;
- Standard Card proof behavior;
- Prime state entry/exit behavior where testable;
- save/load serialization and restoration;
- world-state persistence;
- dialogue trigger/state behavior.

Presentation tests may require manual or screenshot/device validation, but core legality and simulation should not depend on animation timing.

A milestone is not accepted merely because its happy path works once. Add regression coverage for bugs found during the proof whenever practical.
