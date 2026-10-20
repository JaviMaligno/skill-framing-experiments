# Script: "The Scaffolding You Pay For"

The hook is the planning skill that wrote a plan instead of the code. The thesis comes from the article's own description: once the agent has tools, the benefit disappears and only the bill stays. I haven't saved this as `script.md` because I had no way to write files in this session.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | I gave my agent a planning skill. | Le di a mi agente una skill de planificación. | Title card. A cursor opens a code file. | "Four of the twelve `writing-plans` runs didn't deliver." |
| 1 Hook | Intro card | It wrote the plan, not the code. | Escribió el plan, no el código. | The code file closes and a neat plan document lands in its place. | "The agent leaves a nicely written document under `docs/plans/` and never touches the source." |
| 2 Setup | KeyQuote | Skills are process documents riding along in the context. | Las skills son documentos de proceso que viajan en el contexto. | Quote card with the three example rules fading in below it ("Never fix without investigating…"). | "a few thousand characters of prescribed process that ride along in the context" |
| 2 Setup | KeyQuote | My hunch: a frontier model does better without them. | Mi intuición: un modelo puntero va mejor sin ellas. | The quote is struck through and the word "hunch" is highlighted. | "with a good enough model the scaffolding is dead weight, and you do better stripping it out." |
| 2 Setup | Counter | So I measured it, with two models. | Así que lo medí, con dos modelos. | Counter climbs to 147 runs, with "Opus · Sonnet" underneath. | "Axes 3 and 4 are Claude Code with a tool loop, a scratch repository, and 147 runs across two models." |
| 3 Experiment | FlowDiagram | Same task, with and without a real skill, in a repo with tools. | Misma tarea, con y sin skill real, en un repo con herramientas. | Task splits into two branches (free / + skill text), both feed an agent with tools in a repo (8 modules, 19 tests, README rules), and the result is scored on tests, turns, tokens and cost. | "Free: the task alone. Constrained: the same task plus the full text of a real skill" / "eight modules, nineteen green tests, three domain rules written down in the README" |
| 4 Finding | Counter | With tools, not one run broke a domain rule. | Con herramientas, ninguna ejecución rompió una regla. | Counter reaches 48/48, with a green check per condition. | "Nobody broke a domain rule. 48 out of 48." |
| 4 Finding | FlowDiagram | The agent just went and read the README. | El agente simplemente fue y leyó el README. | The ticket says "stack with promotions" and the README says "only one stacks". An arrow runs from agent to README and the README wins. | "Given tools, the model goes and reads the README. Every time, in every condition, free included." |
| 4 Finding | BarCompare | But the planning skill used more than twice the output tokens. | Pero la skill de planificación gastó más del doble de tokens de salida. | Two bars: free 9,686 vs `writing-plans` 22,530 output tokens, with "+133%" on the second. | "`writing-plans` … **22,530** (p<0.001)" / "32%, 35% and 133% more output tokens" |
| 4 Finding | **Bespoke** | And a third of its runs delivered no code. | Y un tercio de sus ejecuciones no entregó código. | Twelve run tiles; four flip from code files into plan documents. A free row of 12 sits beside them, all code. "8/12 vs 12/12" on screen. | "`writing-plans` … **8/12**" vs "free … 12/12" / "cost a third of that condition's runs" |
| 5 So what | KeyQuote | Once the agent has tools, the benefit goes and the bill stays. | Con herramientas, el beneficio se va y la factura se queda. | Quote card. A "benefit" tag fades out and a receipt stays on screen. | "once the agent has tools, the benefit disappears and only the bill stays." |
| 5 So what | KeyQuote | A skill on every task should have a benefit you can name. | Una skill en cada tarea debe aportar algo que puedas nombrar. | Same card, new line. | "a skill riding along on every task should have a benefit you can name, and most of mine couldn't." |
| 5 So what | KeyQuote | Most of mine couldn't. | La mayoría de las mías, no. | The last two words get the emphasis. | (same) |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card. | — |

**What changed in the narration (numbers only):**
- Scene 2: "147 agent runs, two models" chained two figures, and 147 isn't a round number. The voice now just says "with two models". The Counter still shows 147.
- Scene 4, rules: "no run broke a rule: 48 out of 48" said the same thing twice. The voice keeps the point, and 48/48 stays on screen.
- Scene 4, tokens: "133%" becomes "more than twice", which is accurate (22,530 ÷ 9,686 ≈ 2.3×). The "+133%" label stays on the bar.
- Scene 4, delivery: "8/12 against 12/12" stacked four figures. The voice keeps the article's own "a third", and the tiles show 8/12 vs 12/12.

**Spoken forms.** These change only what the voice says; the caption stays as written:
- "javieraguilar.ai" is spoken as "javier aguilar dot A I" (ES: "javier aguilar punto A I").
- The forms for "8/12 against 12/12", "133%" and the Spanish "147" are gone, since those numbers are no longer spoken.

**Choices to confirm:**
- **"More than twice":** the article says "133% more", not "more than double". The rounding is arithmetically exact, but if you'd rather the voice use only the article's wording, the alternative is to drop the figure from the voice ("But the planning skill ran up the bill") and let the bar carry it.
- **The two Opus numbers:** the token gap and the 8/12 delivered are both from Opus. The article says the planning skill's cost holds on both models (+203% on Sonnet, also "more than twice"), so "the bill stays" isn't stronger than the article. If you want the model named on screen, put "Opus" on the visuals.
- **Hook:** it simplifies "4 of 12 runs". Scene 4's "a third of its runs" corrects that inside the same video.
- **Left out:** the Sonnet comparison (7/12 vs 2/12) and the text-only result (8/20 → 15/20). Both would push the video past 60 s and muddy the one message.

**Word count (EN):** 120 words, about 48 s, down from 124 words and about 50 s. The spoken numbers are gone too, and "a hundred and thirty-three percent" and "eight of twelve against twelve of twelve" took longer to say than they took to write. That's inside 30–60 s and close to the 45 s target. To get closer still, cut the "The agent just went and read the README" line (−8 words, about 45 s).

**Caption speed:** at a normal speaking pace every line should come in under 17 characters per second. The longest caption is now the tokens line (~62 characters, 11 words), and it's spoken slowly enough. `npm run lint` will confirm it once the voice track exists. The Spanish lines are each kept under two rows of about 32 characters.

Approve this, or tell me what to change, before any scene is built.
