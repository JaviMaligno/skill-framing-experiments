# Explainer script: "Let the Loop Iterate"

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | Restarting a stuck coding agent sounds smart. | Reiniciar a un agente atascado parece buena idea. | Title card, a "↻ restart" icon | "when a coding agent's attempt is going badly… throw the attempt away and let it start fresh. It has intuitive appeal." |
| 1 Hook | intro card | On my benchmark, it lost. | En mi benchmark, perdió. | The ↻ icon gets crossed out | "The literal *let-the-loop-restart* — restart as blind resampling — **loses** on this benchmark." |
| 2 Setup | KeyQuote | Karpathy's advice: let the loop restart. | Karpathy propone: deja que el bucle reinicie. | The quote "let the loop restart" | "crystallized by Andrej Karpathy as *'let the loop restart'*" |
| 2 Setup | KeyQuote | I tested it on 29 coding tasks from real repos. | Lo probé con 29 tareas de repositorios reales. | Subline under the quote: 29 tasks · 5 repos | "29 single-feature tasks across 5 real repositories" |
| 3 Experiment | FlowDiagram | The agent sees its test results, for up to four rounds. | El agente ve sus tests, durante hasta cuatro rondas. | Agent → code → tests → results → back to agent, round counter 1–4 | "the harness runs the feature's test suite and shows the agent the results… up to **K = 4 rounds**" |
| 3 Experiment | FlowDiagram | Each round, it either patches its work, or starts clean. | En cada ronda, corrige su trabajo o empieza de cero. | The loop splits: "patch" keeps the tree, "restart" wipes it to a blank checkout | "ITERATE — code and context accumulate… RESTART-FRESH — each round starts from a clean checkout with a fresh context." |
| 3 Experiment | FlowDiagram | Third option: a restart button for a file, a folder, or all. | Tercera vía: un botón para reiniciar archivo, carpeta o todo. | A third branch, a button labelled file / directory / all | "an explicit **restart tool with scope** — `restart(file \| directory \| all-my-work)`" |
| 4 Finding | BarCompare | With the stronger model, iterating solved 86% of the tasks. | Con el modelo fuerte, iterar resolvió el 86% de las tareas. | Bars for gpt-5.4: iterate at 86% | "iterate (patch with feedback) … 86% [79–90]" (gpt-5.4 column) |
| 4 Finding | BarCompare | Clean restarts did worse. | Reiniciar de cero salió peor. | Restart-fresh bar at 69% | "restart-fresh (clean best-of-K) … 69% [69–69]"; "restart as blind resampling — **loses** on this benchmark" |
| 4 Finding | BarCompare | The button did slightly better, but not significantly. | El botón, algo mejor, pero no de forma significativa. | Agent-decides bar at 91%, tagged "n.s. vs iterate" | "Agent-decides tops both tiers (91% for gpt-5.4…)… Against pure iterate the edge is not significant (8–4, p=0.39)" |
| 5 Mechanism | StatGrid | The strong model restarted rarely, mostly one file at a time. | El fuerte reiniciaba poco, casi siempre un archivo. | Left half: 7 restarts · 5 file-scoped | "the strong model restarted **rarely and surgically** (7 restarts, 5 file-scoped…)" |
| 5 Mechanism | StatGrid | It rescued 3 of 4 features that iterating lost. | Rescató 3 de 4 funcionalidades que iterando perdía. | 3/4 with restart vs 0/4 with iterate | "Those same 4 features solve **0/4 under iterate**; the scoped restart turned three of them into wins." |
| 5 Mechanism | StatGrid | The weak model wiped it all, on features already lost. | El débil lo borraba todo, en funcionalidades ya perdidas. | Right half: 34 restarts · 23 scope=all · 2/14 under iterate | "the weak model restarted **often and destructively** (34 restarts, 23 of them `scope=all`…)… the agent razed everything *because* the feature was already lost." |
| 6 So what | KeyQuote | So don't restart by default. | Así que no reinicies por defecto. | "Don't restart by default" stamped big | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | Keep your work, and show the agent its tests. | Conserva el trabajo y enséñale los tests. | "Iterate with visible tests" | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | On these runs, knowing what to throw away was the skill. | En estas pruebas, la clave fue saber qué descartar. | "Knowing *what* to throw away" | "knowing *what* to throw away is the metacognition, and it's the strong tier's scoped restart that actually pays" |
| 7 Outro | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | n/a |

**Word count (EN): about 138 words, so roughly 55–57 s.** ES will run about 15–20% longer, so roughly 63–67 s. That's over the 60 s cap. The skill allows going past 60 s when it makes things clearer, but if you want the ES cut under 60 s, the first line I'd trim is "So don't restart by default."

**What changed and why (Voice section)**
- **Finding (scene 4):** the narration used to say three percentages in a row (86%, 69%, 91%), which is hard to follow by ear. Now it says only the 86%, which is easy to hear and gives the baseline. The other two lines say what their numbers mean ("did worse", "slightly better, but not significantly"). All three figures stay on screen in the bars.
- **Setup:** "29 tasks across 5 repos" put two numbers back to back. The narration now says only 29, and "5 repos" stays in the subline.
- **Kept as spoken numbers:** "four rounds" and "3 of 4" are easy to hear and add something.
- **Clarity:** "It sees its test results" now says "The agent", so it's clear who "it" is. "A scoped restart button" now says what the scope means (a file, a folder, or all), since "scoped" wasn't explained anywhere.
- **Plain verdict:** the close now opens with its own sentence and stamp, "So don't restart by default", taken from the article's conclusion. Because of that, scene 6 has three rows instead of two.

**Notes for review**
- **Caption speed (not yet checked):** I haven't run `npm run lint`. The lines most likely to break the 17-characters-per-second limit are "The strong model restarted rarely…", "The weak model wiped it all…" and the new "Third option…" line. If they fail, cut "mostly" and "it all" first, then "for" in the "Third option" line ("a file, a folder, or all").
- **Left out to keep one idea per scene:**
  - The mini-tier numbers (74/63/75%).
  - Restart-informed (69/79%).
  - The p-values.
  - Iterate's 17–2 head-to-head win over clean restarts is also left out. It's the strongest statistic in the article, so it would be the first thing to add back as a subline on the bar chart, where it would also back up "did worse".
- **Hedges kept from the article:**
  - The button's edge is still described as "not significant" compared with iterating.
  - The weak model's wipe-everything restarts are presented as a sign the feature was already lost, not as the cause of the failure.
  - The 3/4 rescue is stated as a plain count, without calling it significant (the article puts it at p≈0.25).
- **Spoken forms:** none needed. "86%", "29" and "3 of 4" are written the way the article writes them and read naturally.
- **Visuals:** unchanged, apart from the stamp on the new "don't restart by default" line. Every scene still uses a library component, so nothing is bespoke.
- **File:** `script.md` isn't saved yet. Paste the table in, or tell me which lines to change first.
