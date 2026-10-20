# Script: "The Scaffolding You Pay For"

The hook is the planning skill that wrote a plan instead of the code. The thesis comes from the article's own description: once the agent has tools, the benefit disappears and only the bill stays. I haven't saved this as `script.md` because I had no way to write files in this session.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | I gave my agent a planning skill. | Le di a mi agente una skill de planificación. | Title card. A cursor opens a code file. | "Four of the twelve `writing-plans` runs didn't deliver." |
| 1 Hook | Intro card | It wrote the plan, not the code. | Escribió el plan, no el código. | The code file closes and a neat plan document lands in its place. | "The agent leaves a nicely written document under `docs/plans/` and never touches the source." |
| 2 Setup | KeyQuote | Skills are process documents riding along in the context. | Las skills son documentos de proceso que viajan en el contexto. | Quote card with the three example rules fading in below it ("Never fix without investigating…"). | "a few thousand characters of prescribed process that ride along in the context" |
| 2 Setup | KeyQuote | My hunch: a frontier model does better without them. | Mi intuición: un modelo puntero va mejor sin ellas. | The quote is struck through and the word "hunch" is highlighted. | "with a good enough model the scaffolding is dead weight, and you do better stripping it out." |
| 2 Setup | Counter | So I measured it across 147 agent runs on two models. | Así que lo medí en 147 ejecuciones de agente con dos modelos. | Counter climbs to 147, with "Opus · Sonnet" underneath. | "Axes 3 and 4 are Claude Code with a tool loop, a scratch repository, and 147 runs across two models." |
| 3 Experiment | FlowDiagram | Same task, with and without a real skill, in a repo with tools. | Misma tarea, con y sin skill real, en un repo con herramientas. | Task splits into two branches (free / + skill text), both feed an agent with tools in a repo (8 modules, 19 tests, README rules), and the result is scored on tests, turns, tokens and cost. | "Free: the task alone. Constrained: the same task plus the full text of a real skill" / "eight modules, nineteen green tests, three domain rules written down in the README" |
| 4 Finding | Counter | With tools, 48 out of 48 runs kept every domain rule. | Con herramientas, 48 de 48 ejecuciones respetaron todas las reglas. | Counter reaches 48/48, with a green check per condition. | "Nobody broke a domain rule. 48 out of 48." |
| 4 Finding | FlowDiagram | The agent just went and read the README. | El agente simplemente fue y leyó el README. | The ticket says "stack with promotions" and the README says "only one stacks". An arrow runs from agent to README and the README wins. | "Given tools, the model goes and reads the README. Every time, in every condition, free included." |
| 4 Finding | BarCompare | But the planning skill cost 133% more output tokens. | Pero la skill de planificación gastó un 133% más de tokens de salida. | Two bars: free 9,686 vs `writing-plans` 22,530 output tokens, with "+133%" on the second. | "`writing-plans` … **22,530** (p<0.001)" / "32%, 35% and 133% more output tokens" |
| 4 Finding | **Bespoke** | Only 8/12 of its runs delivered code; without it, all 12/12 did. | Solo 8/12 de sus ejecuciones entregaron código; sin ella, 12/12. | Twelve run tiles; four flip from code files into plan documents. A free row of 12 sits beside them, all code. | "`writing-plans` … **8/12**" vs "free … 12/12" / "cost a third of that condition's runs" |
| 5 So what | KeyQuote | Once the agent has tools, the benefit goes and the bill stays. | Con herramientas, el beneficio se va y la factura se queda. | Quote card. A "benefit" tag fades out and a receipt stays on screen. | "once the agent has tools, the benefit disappears and only the bill stays." |
| 5 So what | KeyQuote | A skill on every task should have a benefit you can name. | Una skill en cada tarea debe aportar algo que puedas nombrar. | Same card, new line. | "a skill riding along on every task should have a benefit you can name, and most of mine couldn't." |
| 5 So what | KeyQuote | Most of mine couldn't. | La mayoría de las mías, no. | The last two words get the emphasis. | (same) |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card. | — |

**Spoken forms.** These change only what the voice says; the caption stays as written:
- "Only 8/12 of its runs … all 12/12 did" is spoken as "Only eight of its twelve runs … all twelve did" (ES: "Solo ocho de sus doce ejecuciones … sin ella, las doce").
- "133%" is spoken as "a hundred and thirty-three percent" (ES: "ciento treinta y tres por ciento").
- "147" in Spanish is spoken as "ciento cuarenta y siete".
- "javieraguilar.ai" is spoken as "javier aguilar dot A I" (ES: "javier aguilar punto A I").

**What changed for the updated Voice section.** Every number is now spoken as part of a sentence, and none is tacked on after a colon like a table cell:
- "147 agent runs, two models" became "across 147 agent runs on two models".
- "no run broke a domain rule: 48 out of 48" became "48 out of 48 runs kept every domain rule".
- "a third … delivered no code: 8/12 against 12/12" became "Only 8/12 of its runs delivered code; without it, all 12/12 did". The article's figures are unchanged.

**Choices to confirm:**
- **The two Opus numbers:** the 133% tokens and the 8/12 delivered are both from Opus. The article says the planning skill's cost holds on both models (+203% on Sonnet), so "the bill stays" isn't stronger than the article. If you want the model named on screen, put "Opus" on the visuals.
- **Hook:** it simplifies "4 of 12 runs". The 8/12 line in scene 4 gives the exact figure later in the same video.
- **Left out:** the Sonnet comparison (7/12 vs 2/12) and the text-only result (8/20 → 15/20). Both would push the video past 60 s and muddy the one message.

**Word count (EN):** 125 words, about 50 s. That's inside 30–60 s but over the 45 s target. To get closer to 45 s, cut the "The agent just went and read the README" line (−8 words, ~47 s).

**Caption speed:** at a normal speaking pace every line should come in under 17 characters per second. The longest captions (~64 characters) are on the 12-word lines, which are spoken slowly enough, but `npm run lint` will confirm it once the voice track exists. The Spanish lines are each kept under two rows of about 32 characters.

Approve this, or tell me what to change, before any scene is built.
