# Script: "The Scaffolding You Pay For" (revised)

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | I gave my agent a planning skill. | Le di a mi agente una skill de planificación. | Title card. A cursor opens a code file. | "Four of the twelve `writing-plans` runs didn't deliver." |
| 1 Hook | Intro card | It wrote the plan, not the code. | Escribió el plan, no el código. | The code file closes and a neat plan document lands in its place. | "The agent leaves a nicely written document under `docs/plans/` and never touches the source." |
| 2 Setup | KeyQuote | Skills are process documents riding along in the context. | Las skills son documentos de proceso que viajan en el contexto. | Quote card with the three example rules fading in below it ("Never fix without investigating…"). | "a few thousand characters of prescribed process that ride along in the context" |
| 2 Setup | KeyQuote | My hunch: a frontier model does better without them. | Mi intuición: un modelo puntero va mejor sin ellas. | The quote is struck through and the word "hunch" is highlighted. | "with a good enough model the scaffolding is dead weight, and you do better stripping it out." |
| 2 Setup | Counter | So I measured it, on two models. | Así que lo medí, en dos modelos. | Counter climbs to 147, with "Opus · Sonnet" underneath. | "Axes 3 and 4 are Claude Code with a tool loop, a scratch repository, and 147 runs across two models." |
| 3 Experiment | FlowDiagram | Same task, with and without a real skill, in a repo with tools. | Misma tarea, con y sin skill real, en un repo con herramientas. | Task splits into two branches (free / + skill text), both feed an agent with tools in a repo (8 modules, 19 tests, README rules), and the result is scored on tests, turns, tokens and cost. | "Free: the task alone. Constrained: the same task plus the full text of a real skill" / "eight modules, nineteen green tests, three domain rules written down in the README" |
| 4 Finding | Counter | With tools, no run broke a domain rule: 48 out of 48. | Con herramientas, ninguna ejecución rompió una regla: 48 de 48. | Counter reaches 48/48, with a green check per condition. | "Nobody broke a domain rule. 48 out of 48." |
| 4 Finding | FlowDiagram | The agent just went and read the README. | El agente simplemente fue y leyó el README. | The ticket says "stack with promotions" and the README says "only one stacks". An arrow runs from agent to README and the README wins. | "Given tools, the model goes and reads the README. Every time, in every condition, free included." |
| 4 Finding | BarCompare | But the planning skill cost more than double the output tokens. | Pero la skill de planificación gastó más del doble de tokens de salida. | Two bars: free 9,686 vs `writing-plans` 22,530 output tokens, with "+133%" on the second. | "`writing-plans` … **22,530** (p<0.001)" / "32%, 35% and 133% more output tokens" (22,530 / 9,686 ≈ 2.3×) |
| 4 Finding | **Bespoke** | And a third of its runs delivered no code. | Y un tercio de sus ejecuciones no entregó código. | Twelve run tiles; four flip from code files into plan documents. A free row of 12 sits beside them, all code. Label on screen: "8/12 vs 12/12". | "`writing-plans` … **8/12**" vs "free … 12/12" / "cost a third of that condition's runs" |
| 5 So what | KeyQuote | Once the agent has tools, the benefit goes and the bill stays. | Con herramientas, el beneficio se va y la factura se queda. | Quote card. A "benefit" tag fades out and a receipt stays on screen. | "once the agent has tools, the benefit disappears and only the bill stays." |
| 5 So what | KeyQuote | A skill on every task should have a benefit you can name. | Una skill en cada tarea debe aportar algo que puedas nombrar. | Same card, new line. | "a skill riding along on every task should have a benefit you can name, and most of mine couldn't." |
| 5 So what | KeyQuote | Most of mine couldn't. | La mayoría de las mías, no. | The last two words get the emphasis. | (same) |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card. | — |

**Spoken forms.** These change only what the voice says; the caption stays as written:
- "javieraguilar.ai" is spoken as "javier aguilar dot A I" (ES: "javier aguilar punto A I").

The spoken forms for "147", "133%" and "8/12 against 12/12" are no longer used, because those figures now appear only on screen. I can restore them if you want the numbers spoken.

**Word count (EN):** 129 words including the outro (126 without it), about 50 s. That is over the 45 s target. Cutting "The agent just went and read the README." (8 words) brings it to about 48 s.

**Changes made for the spoken-numbers rule:**
- Each scene now has at most one spoken figure. Scene 2 keeps no figure in the voice, and scene 4 keeps only "48 out of 48" and "a third".
- "147 runs" became "on two models". The Counter still shows 147 on screen.
- "133% more output tokens" became "more than double the output tokens". 22,530 / 9,686 ≈ 2.3, so the claim is accurate. The +133% stays on the bar chart.
- "8/12 against 12/12" became "a third of its runs delivered no code". "A third" is the article's own wording. The 8/12 vs 12/12 label stays on screen.

**Choices to confirm:**
- **"More than double" vs "133%":** I rounded to "more than double" because the rule asks for rounding and the number is already on the bar chart. If you want the exact figure in the voice, the line becomes "a hundred and thirty-three percent more" and scene 4 then has two spoken figures, which the rule discourages.
- **Opus numbers:** the 133% tokens and the 8/12 delivered are both from Opus. The article says the planning skill's cost holds on Sonnet too (+203%), so "the bill stays" isn't stronger than the article. If you want the model named on screen, put "Opus" on those visuals.
- **Hook:** it still simplifies "4 of 12 runs". Scene 4's "a third of its runs" corrects that inside the same video.
- **Left out:** the Sonnet comparison (7/12 vs 2/12) and the text-only result (8/20 → 15/20), as before. Both would push the video past 60 s and muddy the one message.

Approve this, or tell me what to change, before any scene is built.
