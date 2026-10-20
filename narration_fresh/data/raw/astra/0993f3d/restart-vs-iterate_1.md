# Explainer script: "Let the Loop Iterate"

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | Restarting a stuck coding agent sounds smart. | Reiniciar a un agente atascado parece buena idea. | Title card, a "↻ restart" icon | "when a coding agent's attempt is going badly… throw the attempt away and let it start fresh. It has intuitive appeal." |
| 1 Hook | intro card | On my benchmark, it lost. | En mi benchmark, perdió. | The ↻ icon gets crossed out | "The literal *let-the-loop-restart* — restart as blind resampling — **loses** on this benchmark." |
| 2 Setup | KeyQuote | Karpathy's advice: let the loop restart. | Karpathy propone: deja que el bucle reinicie. | The quote "let the loop restart" | "crystallized by Andrej Karpathy as *'let the loop restart'*" |
| 2 Setup | KeyQuote | I tested it on coding tasks across real repos. | Lo probé con tareas en repositorios reales. | Subline under the quote: 29 tasks · 5 repos | "29 single-feature tasks across 5 real repositories" |
| 3 Experiment | FlowDiagram | It sees its test results, for up to four rounds. | El agente ve sus tests, durante hasta cuatro rondas. | Agent → code → tests → results → back to agent, round counter 1–4 | "the harness runs the feature's test suite and shows the agent the results… up to **K = 4 rounds**" |
| 3 Experiment | FlowDiagram | Each round, it either patches its work, or starts clean. | En cada ronda, corrige su trabajo o empieza de cero. | The loop splits: "patch" keeps the tree, "restart" wipes it to a blank checkout | "ITERATE — code and context accumulate… RESTART-FRESH — each round starts from a clean checkout with a fresh context." |
| 3 Experiment | FlowDiagram | Third option: a scoped restart button. | Tercera opción: un botón de reinicio con alcance. | A third branch, a button labelled file / directory / all | "an explicit **restart tool with scope** — `restart(file \| directory \| all-my-work)`" |
| 4 Finding | BarCompare | With the stronger model, iterating solved 86%. | Con el modelo fuerte, iterar resolvió el 86%. | Bars for gpt-5.4: iterate at 86% | "iterate (patch with feedback) … 86% [79–90]" (gpt-5.4 column) |
| 4 Finding | BarCompare | Clean restarts solved fewer. | Reiniciar de cero resolvió menos. | Restart-fresh bar at 69% | "restart-fresh (clean best-of-K) … 69% [69–69]" |
| 4 Finding | BarCompare | The button had a small edge, not significant. | El botón tuvo una ventaja pequeña, no significativa. | Agent-decides bar at 91%, tagged "n.s. vs iterate" | "Agent-decides tops both tiers (91% for gpt-5.4…)… Against pure iterate the edge is not significant (8–4, p=0.39)" |
| 5 Mechanism | StatGrid | The strong model restarted rarely, mostly one file at a time. | El fuerte reiniciaba poco, casi siempre un archivo. | Left half: 7 restarts · 5 file-scoped | "the strong model restarted **rarely and surgically** (7 restarts, 5 file-scoped…)" |
| 5 Mechanism | StatGrid | It rescued features that iterating lost. | Rescató funcionalidades que iterando perdía. | 3/4 with restart vs 0/4 with iterate | "Those same 4 features solve **0/4 under iterate**; the scoped restart turned three of them into wins." |
| 5 Mechanism | StatGrid | The weak model wiped it all, on features already lost. | El débil lo borraba todo, en funcionalidades ya perdidas. | Right half: 34 restarts · 23 scope=all · 2/14 under iterate | "the weak model restarted **often and destructively** (34 restarts, 23 of them `scope=all`…)… the agent razed everything *because* the feature was already lost." |
| 6 So what | KeyQuote | So keep your work, and show the agent its tests. | Así que conserva el trabajo y enséñale los tests. | "Iterate with visible tests" | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | On these runs, knowing what to throw away was the skill. | En estas pruebas, la clave fue saber qué descartar. | "Knowing *what* to throw away" | "knowing *what* to throw away is the metacognition, and it's the strong tier's scoped restart that actually pays" |
| 7 Outro | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | n/a |

**Word count (EN): 123 words, so roughly 48–50 s.** ES will run about 15–20% longer, so roughly 55–60 s, which is close to the 60 s cap.

**Notes for review**
- **Caption speed (not yet checked):** I estimated characters per second but haven't run `npm run lint`. The lines most likely to fail the 17-character limit are "The strong model restarted rarely…" and "The weak model wiped it all…". If they do, cut the words "mostly" and "it all" first.
- **Left out to keep one idea per scene:**
  - The mini-tier numbers (74/63/75%).
  - Restart-informed (69/79%).
  - The p-values.
  - Iterate's 17–2 head-to-head win over clean restarts is also left out. It is the strongest statistic in the article, so it would be the first thing to add back as a subline on the bar chart.
- **Hedges kept from the article:**
  - The 91% result is still described as a small edge, "not significant" against iterating; the percentage stays on screen.
  - The weak model's broad restarts are framed as a sign the task was already lost, not as the cause of failure.
  - The rescue is described without calling it significant; the plain 3/4 count stays on screen (the article puts it at p≈0.25).
- **Spoken forms:** 86% is spoken as “eighty-six percent” (ES: “ochenta y seis por ciento”). It is the only percentage narrated. The task and repo counts, the other percentages, and the rescue count stay on screen rather than being read aloud.
- **Visuals:** every scene maps to a library component, so nothing is bespoke. The FlowDiagram with the patch, clean-restart and scoped-restart branches is the scene that shows how the experiment works. The StatGrid could become a bespoke "scalpel vs wrecking ball" animation if you want a stronger image there.
- **File:** this session can't write files, so `script.md` isn't saved yet. Paste the table in, or tell me to adjust lines first.