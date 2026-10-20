# Explainer script: "Let the Loop Iterate"

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | Restarting a stuck coding agent sounds smart. | Reiniciar a un agente atascado parece buena idea. | Title card, a "↻ restart" icon | "when a coding agent's attempt is going badly… throw the attempt away and let it start fresh. It has intuitive appeal." |
| 1 Hook | intro card | On my benchmark, it lost. | En mi benchmark, perdió. | The ↻ icon gets crossed out | "The literal *let-the-loop-restart* — restart as blind resampling — **loses** on this benchmark." |
| 2 Setup | KeyQuote | Karpathy's advice: let the loop restart. | Karpathy propone: deja que el bucle reinicie. | The quote "let the loop restart" | "crystallized by Andrej Karpathy as *'let the loop restart'*" |
| 2 Setup | KeyQuote | I tested it on 29 coding tasks across 5 real repos. | Lo probé con 29 tareas en 5 repositorios reales. | Subline under the quote: 29 tasks · 5 repos | "29 single-feature tasks across 5 real repositories" |
| 3 Experiment | FlowDiagram | It sees its test results, for up to four rounds. | El agente ve sus tests, durante hasta cuatro rondas. | Agent → code → tests → results → back to agent, round counter 1–4 | "the harness runs the feature's test suite and shows the agent the results… up to **K = 4 rounds**" |
| 3 Experiment | FlowDiagram | Each round, it either patches its work, or starts clean. | En cada ronda, corrige su trabajo o empieza de cero. | The loop splits: "patch" keeps the tree, "restart" wipes it to a blank checkout | "ITERATE — code and context accumulate… RESTART-FRESH — each round starts from a clean checkout with a fresh context." |
| 3 Experiment | FlowDiagram | Third option: a scoped restart button. | Tercera opción: un botón de reinicio con alcance. | A third branch, a button labelled file / directory / all | "an explicit **restart tool with scope** — `restart(file \| directory \| all-my-work)`" |
| 4 Finding | BarCompare | With the stronger model, iterating solved 86%. | Con el modelo fuerte, iterar resolvió el 86%. | Bars for gpt-5.4: iterate at 86% | "iterate (patch with feedback) … 86% [79–90]" (gpt-5.4 column) |
| 4 Finding | BarCompare | Clean restarts solved 69%. | Reiniciar de cero resolvió el 69%. | Restart-fresh bar at 69% | "restart-fresh (clean best-of-K) … 69% [69–69]" |
| 4 Finding | BarCompare | The button solved 91%, a small edge that isn't statistically significant. | El botón resolvió el 91%, una ventaja pequeña que no es estadísticamente significativa. | Agent-decides bar at 91%, tagged "n.s. vs iterate" | "Agent-decides tops both tiers (91% for gpt-5.4…)… Against pure iterate the edge is not significant (8–4, p=0.39)" |
| 5 Mechanism | StatGrid | The strong model restarted rarely, and mostly just one file. | El fuerte reiniciaba poco, y casi siempre solo un archivo. | Left half: 7 restarts · 5 file-scoped | "the strong model restarted **rarely and surgically** (7 restarts, 5 file-scoped…)" |
| 5 Mechanism | StatGrid | It rescued three of the four features that iterating lost. | Rescató tres de las cuatro funcionalidades que iterando perdía. | 3/4 with restart vs 0/4 with iterate | "Those same 4 features solve **0/4 under iterate**; the scoped restart turned three of them into wins." |
| 5 Mechanism | StatGrid | The weak model wiped everything, on features it had already lost. | El débil lo borraba todo, en funcionalidades ya perdidas. | Right half: 34 restarts · 23 scope=all · 2/14 under iterate | "the weak model restarted **often and destructively** (34 restarts, 23 of them `scope=all`…)… the agent razed everything *because* the feature was already lost." |
| 6 So what | KeyQuote | So keep your work, and show the agent its tests. | Así que conserva el trabajo y enséñale los tests. | "Iterate with visible tests" | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | On these runs, knowing what to throw away was the skill. | En estas pruebas, la clave fue saber qué descartar. | "Knowing *what* to throw away" | "knowing *what* to throw away is the metacognition, and it's the strong tier's scoped restart that actually pays" |
| 7 Outro | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | n/a |

**Word count (EN): about 135 words, roughly 50–55 s at a normal speaking pace.** My earlier estimate of 125 words was low. Spanish will run about 15–20% longer, so it will probably land at 60 s or a little over. Trim the ES lines if it does.

**What changed (Voice section, numbers spoken naturally)**
- Bare figures that read like table cells ("Clean restarts: 69%", "The button: 91%. A small edge, not significant.") are now full sentences with the number inside the verb phrase.
- "3 of 4" and "7 restarts" are spoken as "three of the four" and "rarely, and mostly just one file." The on-screen visuals still show the exact counts.
- The 91% line keeps the article's hedge: a small edge that is not statistically significant.
- Everything else is unchanged: components, visuals, source sentences and the outro.

**Notes for review**
- **Caption speed (not yet checked):** I haven't run `npm run lint`. The longest lines are "The weak model wiped everything, on features it had already lost." and "The button solved 91%, a small edge that isn't statistically significant." If either fails the 17-characters-per-second limit, cut "already" first, then shorten the hedge to "a small, non-significant edge."
- **Spoken forms:** none are needed. Caption and narration use the same wording, and the percentages are read as written. If the TTS reads "86%" or "91%" badly, add a spoken form per the `narration` skill and leave the caption alone.
- **Left out to keep one idea per scene:** the mini-tier numbers (74/63/75%), restart-informed (69/79%), the p-values, and iterate's 17–2 head-to-head win over clean restarts. The 17–2 result is the strongest statistic in the article, so it is the first thing to add back as a subline on the bar chart.
- **File:** this session can't write files, so `script.md` isn't saved. Paste the table in, or ask me to adjust lines first.
