# Content spec — release notes for users

Both framings must carry every point below, and nothing else. Written before any output
was seen.

- S1 Audience: the product's customers (freelancers using Ledgerly, an invoicing app), not engineers.
- S2 Include only changes a user can notice. Skip internal work (refactors, tests, CI,
  dependency upgrades, logging, monitoring) unless it changes something they see.
- S3 Describe each change by what the user can now do or will notice. For a fix, the
  symptom they experienced, not its cause.
- S4 No engineering vocabulary and no internal references (ticket ids, PR numbers,
  class or file names, framework or library names).
- S5 Exception to S4: keep the exact name of anything the user sees in the product or has
  to use (a button, a setting, "API key", a file format).
- S6 If the user has to do something, say it first: what, and by when.
- S7 Short: one heading line and bullets; small fixes grouped together.
