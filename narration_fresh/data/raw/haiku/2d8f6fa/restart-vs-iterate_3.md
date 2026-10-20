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
| 4 Finding | BarCompare | Starting clean, it reached 69%. | Empezando de cero, llegó al 69%. | Restart-fresh bar at 69% | "restart-fresh (clean best-of-K) … 69% [69–69]" |
| 4 Finding | BarCompare | The scoped button reached 91%. | El botón llegó al 91%. | Agent-decides bar at 91% | "Agent-decides tops both tiers (91% for gpt-5.4…)" |
| 4 Finding | BarCompare | That edge over iterating isn't significant. | Esa ventaja sobre iterar no es significativa. | Tag on the bar: "n.s. vs iterate" | "Against pure iterate the edge is not significant (8–4, p=0.39)" |
| 5 Mechanism | StatGrid | The strong model restarted 7 times, mostly one file. | El fuerte reinició 7 veces, casi siempre un archivo. | Left half: 7 restarts · 5 file-scoped | "the strong model restarted **rarely and surgically** (7 restarts, 5 file-scoped…)" |
| 5 Mechanism | StatGrid | It rescued 3 of 4 features that iterating lost. | Rescató 3 de 4 funcionalidades que iterando perdía. | 3/4 with restart vs 0/4 with iterate | "Those same 4 features solve **0/4 under iterate**; the scoped restart turned three of them into wins." |
| 5 Mechanism | StatGrid | The weak model restarted 34 times. | El débil reinició 34 veces. | Right half: 34 restarts · 23 scope=all · 2/14 under iterate | "the weak model restarted **often and destructively** (34 restarts, 23 of them `scope=all`…)" |
| 5 Mechanism | StatGrid | Most of them wiped everything, on features already lost. | La mayoría borró todo, en funcionalidades ya perdidas. | Same right half | "the agent razed everything *because* the feature was already lost." |
| 6 So what | KeyQuote | So keep your work, and show the agent its tests. | Así que conserva el trabajo y enséñale los tests. | "Iterate with visible tests" | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | On these runs, knowing what to throw away was the skill. | En estas pruebas, la clave fue saber qué descartar. | "Knowing *what* to throw away" | "knowing *what* to throw away is the metacognition, and it's the strong tier's scoped restart that actually pays" |
| 7 Outro | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | n/a |

**Word count (EN): about 140 words, roughly 50–53 s.** The ES cut will run about 15–20% longer, so it may pass the 60 s cap. If it does, the first candidates to trim are the scene 2 subline and the scene 3 "Each round" line.

**What changed (narration only, all other content kept)**
- Scene 4: the bar labels "Clean restarts: 69%" and "The button: 91%" were fragments that read like table cells. They are now full sentences with the number inside them. The hedge on the 91% is split into its own line, so the "not significant" point gets its own spoken sentence and on-screen tag.
- Scene 5: the three lines that carried the numbers only on screen now say them aloud as part of the sentence ("7 times", "34 times"). The 23 `scope=all` restarts are described as "most of them wiped everything", which matches the article's count without reciting it.

**Still to do**
- **Caption speed:** `npm run lint` has not been run. The longest lines are now the scene 5 and scene 4 "That edge over iterating…" lines, so check those first.
- **File:** I haven't saved `script.md`. Paste the table in, or ask me to write it out.
