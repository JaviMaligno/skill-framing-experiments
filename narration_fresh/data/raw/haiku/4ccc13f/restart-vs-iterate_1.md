Here is the revised script. The main change is in Scene 4. It had three percentages in three consecutive lines, so only the headline 86% is now spoken. The 69% and 91% stay on the bars, and the lines around them state the verdict in words.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | Restarting a stuck coding agent sounds smart. | Reiniciar a un agente atascado parece buena idea. | Title card, a "↻ restart" icon | "when a coding agent's attempt is going badly… throw the attempt away and let it start fresh. It has intuitive appeal." |
| 1 Hook | intro card | On my benchmark, it lost. | En mi benchmark, perdió. | The ↻ icon gets crossed out | "The literal *let-the-loop-restart* — restart as blind resampling — **loses** on this benchmark." |
| 2 Setup | KeyQuote | Karpathy's advice: let the loop restart. | Karpathy propone: deja que el bucle reinicie. | The quote "let the loop restart" | "crystallized by Andrej Karpathy as *'let the loop restart'*" |
| 2 Setup | KeyQuote | I tested it on 29 coding tasks from five real repos. | Lo probé con 29 tareas de cinco repositorios reales. | Subline under the quote: 29 tasks · 5 repos | "29 single-feature tasks across 5 real repositories" |
| 3 Experiment | FlowDiagram | It sees its test results, for up to four rounds. | El agente ve sus tests, durante hasta cuatro rondas. | Agent → code → tests → results → back to agent, round counter 1–4 | "the harness runs the feature's test suite and shows the agent the results… up to **K = 4 rounds**" |
| 3 Experiment | FlowDiagram | Each round, it either patches its work, or starts clean. | En cada ronda, corrige su trabajo o empieza de cero. | The loop splits: "patch" keeps the tree, "restart" wipes it to a blank checkout | "ITERATE — code and context accumulate… RESTART-FRESH — each round starts from a clean checkout with a fresh context." |
| 3 Experiment | FlowDiagram | Third option: a scoped restart button. | Tercera opción: un botón de reinicio con alcance. | A third branch, a button labelled file / directory / all | "an explicit **restart tool with scope** — `restart(file \| directory \| all-my-work)`" |
| 4 Finding | BarCompare | With the stronger model, iterating solved 86%. | Con el modelo fuerte, iterar resolvió el 86%. | Bars for gpt-5.4: iterate at 86% | "iterate (patch with feedback) … 86% [79–90]" (gpt-5.4 column) |
| 4 Finding | BarCompare | Clean restarts trailed. | Reiniciar de cero quedó por detrás. | Restart-fresh bar at 69% | "restart-fresh (clean best-of-K) … 69% [69–69]" |
| 4 Finding | BarCompare | The scoped button edged ahead. A small gap, not significant. | El botón con alcance quedó algo por encima. Una ventaja pequeña, no significativa. | Agent-decides bar at 91%, tagged "n.s. vs iterate" | "Agent-decides tops both tiers (91% for gpt-5.4…)… Against pure iterate the edge is not significant (8–4, p=0.39)" |
| 5 Mechanism | StatGrid | The strong model restarted rarely, mostly one file at a time. | El fuerte reiniciaba poco, casi siempre un archivo. | Left half: 7 restarts · 5 file-scoped | "the strong model restarted **rarely and surgically** (7 restarts, 5 file-scoped…)" |
| 5 Mechanism | StatGrid | It rescued 3 of 4 features that iterating lost. | Rescató 3 de 4 funcionalidades que iterando perdía. | 3/4 with restart vs 0/4 with iterate | "Those same 4 features solve **0/4 under iterate**; the scoped restart turned three of them into wins." |
| 5 Mechanism | StatGrid | The weak model wiped it all, on features already lost. | El débil lo borraba todo, en funcionalidades ya perdidas. | Right half: 34 restarts · 23 scope=all · 2/14 under iterate | "the weak model restarted **often and destructively** (34 restarts, 23 of them `scope=all`…)… the agent razed everything *because* the feature was already lost." |
| 6 So what | KeyQuote | So keep your work, and show the agent its tests. | Así que conserva el trabajo y enséñale los tests. | "Iterate with visible tests" | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | On these runs, knowing what to throw away was the skill. | En estas pruebas, la clave fue saber qué descartar. | "Knowing *what* to throw away" | "knowing *what* to throw away is the metacognition, and it's the strong tier's scoped restart that actually pays" |
| 7 Outro | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | n/a |

**Word count (EN): about 128 words, so roughly 48–50 s.** ES will run about 15–20% longer, so roughly 55–60 s.

**What changed**
- **Scene 2, line 2:** "5 real repos" became "five real repos." Two figures in one line was the only other pile-up. "29" stays as the figure that carries the point, and the subline still shows "5 repos."
- **Scene 4, lines 2 and 3:** the 69% and 91% are no longer spoken. The bars show them, and the lines now say the verdict: "trailed," and "a small gap, not significant." The 86% stays as the one spoken figure.
- **Everything else is unchanged.** Scenes 5 and 6 already had no pile-up. Their figures (3 of 4, 7, 34, 23, 2/14) are all on screen, and the spoken lines carry only the 3 of 4 count.

**Still open**
- **Caption speed:** I can't run `npm run lint` from this session, so the 17-characters-per-second check is still unverified. The lines to watch are the Scene 5 ones, as noted before.
- **Closing verdict:** the skill asks the close to state the result plainly. The Scene 6 lines do that ("keep your work, and show the agent its tests"). If you want the restart verdict stated as a sentence too, I can add one, though it would add a line.
