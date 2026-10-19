# Release notes

Rules for writing Ledgerly's release notes:

1. The audience is customers (freelancers who invoice with Ledgerly), never engineers.
2. Include a change ONLY if a user can notice it. DO NOT include refactors, tests, CI,
   dependency upgrades, logging or monitoring, unless they change something users see.
3. Describe each change as what the user can now do or will notice. For fixes, describe
   the symptom the user saw. DO NOT explain the cause.
4. NEVER use engineering vocabulary. NEVER include ticket ids, PR numbers, class names,
   file names, or framework and library names.
5. EXCEPTION to rule 4: ALWAYS keep the exact name of anything the user sees in the
   product or must use: buttons, settings, "API key", file formats.
6. If the user must take an action, put it FIRST: state what they must do and the deadline.
7. Format: one heading line, then bullets. Group small fixes into a single bullet.
   Keep it short.
