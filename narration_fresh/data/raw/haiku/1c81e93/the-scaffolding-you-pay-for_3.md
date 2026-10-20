I revised the three narration lines that were awkward to hear. Everything else is unchanged. I couldn't save `script.md` because this session has no file-writing tool, so the full script is below.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | I gave my agent a planning skill. | Le di a mi agente una skill de planificación. | Title card. A cursor opens a code file. | "Four of the twelve `writing-plans` runs didn't deliver." |
| 1 Hook | Intro card | It wrote the plan, not the code. | Escribió el plan, no el código. | The code file closes and a neat plan document lands in its place. | "The agent leaves a nicely written document under `docs/plans/` and never touches the source." |
| 2 Setup | KeyQuote | Skills are process documents riding along in the context. | Las skills son documentos de proceso que viajan en el contexto. | Quote card with the three example rules fading in below it ("Never fix without investigating…"). | "a few thousand characters of prescribed process that ride along in the context" |
| 2 Setup | KeyQuote | My hunch: a frontier model does better without them. | Mi intuición: un modelo puntero va mejor sin ellas. | The quote is struck through and the word "hunch" is highlighted. | "with a good enough model the scaffolding is dead weight, and you do better stripping it out." |
| 2 Setup | Counter | So I measured it: 147 agent runs, two models. | Así que lo medí: 147 ejecuciones de agente, dos modelos. | Counter climbs to 147, with "Opus · Sonnet" underneath. | "Axes 3 and 4 are Claude Code with a tool loop, a scratch repository, and 147 runs across two models." |
| 3 Experiment | FlowDiagram | Same task, with and without a real skill, in a repo with tools. | Misma tarea, con y sin skill real, en un repo con herramientas. | Task splits into two branches (free / + skill text), both feed an agent with tools in a repo (8 modules, 19 tests, README rules), and the result is scored on tests, turns, tokens and cost. | "Free: the task alone. Constrained: the same task plus the full text of a real skill" / "eight modules, nineteen green tests, three domain rules written down in the README" |
| 4 Finding | Counter | With tools, no run broke a domain rule: 48 out of 48. | Con herramientas, ninguna ejecución rompió una regla: 48 de 48. | Counter reaches 48/48, with a green check per condition. | "Nobody broke a domain rule. 48 out of 48." |
| 4 Finding | FlowDiagram | The agent just went and read the README. | El agente simplemente fue y leyó el README. | The ticket says "stack with promotions" and the README says "only one stacks". An arrow runs from agent to README and the README wins. | "Given tools, the model goes and reads the README. Every time, in every condition, free included." |
| 4 Finding | BarCompare | But the planning skill used more than twice the output tokens. | Pero esa skill gastó más del doble de tokens de salida. | Two bars: free 9,686 vs `writing-plans` 22,530 output tokens, with "+133%" on the second. | "`writing-plans` … **22,530** (p<0.001)" / "32%, 35% and 133% more output tokens" |
| 4 Finding | **Bespoke** | And a third of its runs delivered no code. Free ones did. | Y un tercio no entregó código. Las libres siempre sí. | Twelve run tiles; four flip from code files into plan documents. A free row of 12 sits beside them, all code. Shows "8/12" and "12/12". | "`writing-plans` … **8/12**" vs "free … 12/12" / "cost a third of that condition's runs" |
| 5 So what | KeyQuote | Once the agent has tools, the benefit goes and the bill stays. | Con herramientas, el beneficio se va y la factura se queda. | Quote card. A "benefit" tag fades out and a receipt stays on screen. | "once the agent has tools, the benefit disappears and only the bill stays." |
| 5 So what | KeyQuote | A skill riding along on every task should have a benefit you can name. | Una skill en cada tarea debe aportar algo que puedas nombrar. | Same card, new line. | "a skill riding along on every task should have a benefit you can name, and most of mine couldn't." |
| 5 So what | KeyQuote | Most of mine couldn't. | La mayoría de las mías, no. | The last two words get the emphasis. | (same) |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card. | — |

**Changes from the previous version**
- **133% → "more than twice":** 133% more is 2.33 times, so "more than twice" is accurate and easier to hear. The "+133%" stays on the BarCompare visual, and the source sentence still gives the exact figure.
- **"8/12 against 12/12" → "a third … The free ones did":** "a third" is 4 of 12, which matches the article. The exact counts stay on screen. The new second sentence makes the contrast with the free condition audible.
- **"48 out of 48" kept:** it is short and easy to hear, and it carries the emphasis of the finding.

**Spoken forms (voice only; captions stay as written)**
- "147" is spoken as "one forty-seven" (ES: "ciento cuarenta y siete").
- "javieraguilar.ai" is spoken as "javier aguilar dot A I" (ES: "javier aguilar punto A I").
- The earlier spoken forms for "8/12 against 12/12" and "133%" are retired, because those lines now say the meaning in words.

**Length and captions**
- EN is about 130 words, roughly 52 s. That is within 30–60 s but above the 45 s target. Cutting "The agent just went and read the README." (−8 words) brings it to about 49 s.
- The new caption lines are kept under two rows of about 32 characters. The longest EN caption is 62 characters, and `npm run lint` will check the 17-characters-per-second limit once the voice track exists.

Approve this, or tell me what to change, and I'll write `script.md` once I have a way to save files.
