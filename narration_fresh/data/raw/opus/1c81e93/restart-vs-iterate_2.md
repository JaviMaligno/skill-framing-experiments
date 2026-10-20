I revised the narration so numbers are spoken only where they're easy to hear. Where a figure is awkward to say aloud, the line now says what it means and the exact value stays on screen. I also made a few clarity fixes that come from the same Voice section. Components, visuals and source sentences are unchanged.

# Explainer script: "Let the Loop Iterate"

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | Restarting a stuck coding agent sounds smart. | Reiniciar a un agente atascado parece buena idea. | Title card, a "↻ restart" icon | "when a coding agent's attempt is going badly… throw the attempt away and let it start fresh. It has intuitive appeal." |
| 1 Hook | intro card | On my benchmark, it lost. | En mi benchmark, perdió. | The ↻ icon gets crossed out | "The literal *let-the-loop-restart* — restart as blind resampling — **loses** on this benchmark." |
| 2 Setup | KeyQuote | Karpathy's advice: let the loop restart. | Karpathy propone: deja que el bucle reinicie. | The quote "let the loop restart" | "crystallized by Andrej Karpathy as *'let the loop restart'*" |
| 2 Setup | KeyQuote | I tested it on coding tasks from 5 real repos. | Lo probé con tareas de código de 5 repositorios reales. | Subline under the quote: 29 tasks · 5 repos | "29 single-feature tasks across 5 real repositories" |
| 3 Experiment | FlowDiagram | The agent sees its test results, for up to four rounds. | El agente ve sus tests, durante hasta cuatro rondas. | Agent → code → tests → results → back to agent, round counter 1–4 | "the harness runs the feature's test suite and shows the agent the results… up to **K = 4 rounds**" |
| 3 Experiment | FlowDiagram | Each round, it either patches its work, or starts clean. | En cada ronda, corrige su trabajo o empieza de cero. | The loop splits: "patch" keeps the tree, "restart" wipes it to a blank checkout | "ITERATE — code and context accumulate… RESTART-FRESH — each round starts from a clean checkout with a fresh context." |
| 3 Experiment | FlowDiagram | Third option: a scoped restart button. | Tercera opción: un botón de reinicio con alcance. | A third branch, a button labelled file / directory / all | "an explicit **restart tool with scope** — `restart(file \| directory \| all-my-work)`" |
| 4 Finding | BarCompare | With the stronger model, patching solved most tasks. | Con el modelo fuerte, corregir resolvió la mayoría. | Bars for gpt-5.4: iterate at 86% | "iterate (patch with feedback) … 86% [79–90]" (gpt-5.4 column) |
| 4 Finding | BarCompare | Clean restarts solved clearly fewer. | Reiniciar de cero resolvió claramente menos. | Restart-fresh bar at 69% | "restart-fresh (clean best-of-K) … 69% [69–69]" |
| 4 Finding | BarCompare | The button did a bit better than patching, but not significantly. | El botón superó un poco a corregir, pero no de forma significativa. | Agent-decides bar at 91%, tagged "n.s. vs iterate" | "Agent-decides tops both tiers (91% for gpt-5.4…)… Against pure iterate the edge is not significant (8–4, p=0.39)" |
| 5 Mechanism | StatGrid | The strong model restarted rarely, mostly one file at a time. | El fuerte reiniciaba poco, casi siempre un archivo. | Left half: 7 restarts · 5 file-scoped | "the strong model restarted **rarely and surgically** (7 restarts, 5 file-scoped…)" |
| 5 Mechanism | StatGrid | It rescued 3 of 4 features that patching lost. | Rescató 3 de 4 funcionalidades que corrigiendo perdía. | 3/4 with restart vs 0/4 with iterate | "Those same 4 features solve **0/4 under iterate**; the scoped restart turned three of them into wins." |
| 5 Mechanism | StatGrid | The weak model wiped it all, on features already lost. | El débil lo borraba todo, en funcionalidades ya perdidas. | Right half: 34 restarts · 23 scope=all · 2/14 under iterate | "the weak model restarted **often and destructively** (34 restarts, 23 of them `scope=all`…)… the agent razed everything *because* the feature was already lost." |
| 6 So what | KeyQuote | So don't restart by default. Keep your work, and show the agent its tests. | Así que no reinicies por defecto. Conserva el trabajo y enséñale los tests. | "Iterate with visible tests" | "Default to **iterate with visible tests** — don't restart-by-default, and don't hide the feedback." |
| 6 So what | KeyQuote | On these runs, knowing what to throw away was the skill. | En estas pruebas, la clave fue saber qué descartar. | "Knowing *what* to throw away" | "knowing *what* to throw away is the metacognition, and it's the strong tier's scoped restart that actually pays" |
| 7 Outro | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | n/a |

**Word count (EN): about 135 words, so roughly 52–55 s.** The Spanish version will run about 15–20% longer, so roughly 60–65 s. That may go slightly over the 60 s cap, which the skill now allows when it's needed for clarity.

**What changed in the narration**
- **Spoken numbers:**
  - **Finding (scene 4):** the three percentages (86 / 69 / 91) are no longer read out. They're unround and come one after another, which is hard to follow by ear. Each line now says what the number means: "most tasks", "clearly fewer", "a bit better… but not significantly". The exact figures stay on the bars.
  - **Setup (scene 2):** I dropped "29" from the narration and kept "29 tasks · 5 repos" in the subline. "5 real repos" stays because it's easy to hear.
  - **Unchanged:** "four rounds" and "3 of 4" are easy to say and hear, so I kept them.
- **Clarity:**
  - "It sees its test results" is now "The agent sees its test results". The "it" came right after Karpathy's quote and could have meant the loop.
  - In scene 5, "features that iterating lost" is now "that patching lost", so the term matches what the viewer heard in scene 3.
- **Plain verdict:** the closing now opens with "So don't restart by default". That says the result in words, as the article concludes it, instead of leaving it implied.

**Notes for review**
- **Caption speed (not yet checked):** I haven't run `npm run lint`. The lines most at risk of going over 17 characters per second are:
  - "The button did a bit better than patching, but not significantly." If it fails, cut it to "The button: a bit better, not significantly."
  - "The strong model restarted rarely…" If it fails, cut "mostly".
  - "The weak model wiped it all…" If it fails, cut "it all".
  - The longer scene-6 line. If it fails, split it into two caption beats at "by default."
- **Left out to keep one idea per scene:**
  - The mini-tier numbers (74/63/75%).
  - Restart-informed (69/79%).
  - The p-values.
  - Iterate's 17–2 head-to-head win over clean restarts. It's still the first thing to add back, as a subline on the bar chart.
- **Hedges kept from the article:**
  - The button's edge is still called "not significant" against patching.
  - The weak model's broad restarts are still framed as a sign the task was already lost, not as the cause of failure.
  - The 3/4 rescue is still a plain count, without calling it significant (the article puts it at p≈0.25).
  - "On these runs" is still in the closing.
- **Spoken forms:** none needed. The digits still in captions ("5", "3 of 4") read naturally as written.
- **Visuals:** unchanged. Every scene maps to a library component, and the FlowDiagram is still the scene that shows how the experiment works. The skill now asks for a clear on-screen moment for each key point. A "lost" stamp on the restart-fresh bar in scene 4 would give the verdict one, but I haven't added it because you asked me to keep the visuals as they are.
- **File:** `script.md` isn't saved yet. Paste the table in, or tell me which lines to adjust first.
