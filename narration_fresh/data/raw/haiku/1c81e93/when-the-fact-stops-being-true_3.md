I can't write files in this session, so here is the full revised script to save as `script.md`. Under the updated Voice rules, I moved three narration lines (EN and ES) from exact figures to plain words. The figures stay on screen in the visuals. Everything else is unchanged.

```markdown
# Script: When the Fact Stops Being True

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | My agent had the correction in context. | Mi agente tenía la corrección en contexto. | Title card "When the Fact Stops Being True"; a crossed-out shelf record flickers under the title | "The full transcript, which physically contains the correction…" |
| 1 Hook | intro card | Most of the time, it acted on the old fact. | La mayoría de las veces, usó el dato viejo. | Same card; the stale record stays lit | "…explicit state applies the correction in 70 of 72 episodes and the full transcript in 10 of 72" (correction box) |
| 2 Setup | bespoke | I was replicating SKILL.state, an EMNLP paper. | Estaba replicando SKILL.state, un paper de EMNLP. | **Bespoke:** a prompt stack (procedure / transcript / observation) where the tall grey transcript block shrinks into a small amber "state" chip | "A replication of SKILL.state, an EMNLP paper…" |
| 2 Setup | bespoke | It swaps the agent's transcript for a small state object. | Cambia el historial del agente por un pequeño estado. | Chip settles between procedure and observation | "…replaces an agent's conversation history with an explicit mutable state." |
| 3 Experiment | FlowDiagram | The agent files a pallet on a shelf. | El agente guarda un palé en una balda. | Node "step t: pallet filed on shelf" | "the agent files a pallet at step `t`" |
| 3 Experiment | FlowDiagram | Ten steps later, a correction: that shelf is empty. | Diez pasos después, una corrección: la balda está vacía. | Node "t+10: correction, shelf empty" | "at `t+10` a correction says that put-away never completed and the shelf is empty" |
| 3 Experiment | FlowDiagram | Every decision after that depends on the fix. | Cada decisión posterior depende de esa corrección. | Arrow fans out to later decisions | "every subsequent decision depends on having applied the correction" |
| 4 Finding | BarCompare | Explicit state applied the fix in almost every episode. | Con estado explícito, la aplicó en casi todos los episodios. | Teal bar: 70/72, label "70 of 72" stays on screen | "explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | Across three models, the full transcript applied it only about one time in seven. | En tres modelos, con el historial completo, la aplicó solo una de cada siete veces. | Grey bar: 10/72, label "10 of 72" stays on screen | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, that token saving shrank to a small money saving. | Con caché activado, ese gran ahorro en tokens se quedó en uno pequeño en dinero. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 132 words (narration only), about 51 s at 2.6 words per second. That is within 30–60 s and a little over the 45 s target. The outro card adds two words.

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 70 of 72, 10 of 72, 7.5x and 1.4x are not spoken. The narration says them in words ("almost every episode", "about one time in seven", "a small money saving"), and the figures stay on screen in the visuals. Captions use the narration text as written.
```

**What changed**

- **Scene 4, line 1:** "70 of 72 episodes" → "almost every episode" (EN and ES). Almost every is what 70 of 72 means, and the teal bar still shows 70/72.
- **Scene 4, line 2:** "10 of 72" → "about one time in seven" (EN and ES). Both halves of the pair now use words, so they don't stack up as figures. The grey bar still shows 10/72.
- **Scene 6, line 2:** "a 7.5x token saving became 1.4x in money" → "that token saving shrank to a small money saving" (EN) and the matching Spanish. Two unround figures in a row were the awkward case the skill describes. The tiles still show 7.5x and 1.4x.
- The spoken-forms section now says these figures are no longer spoken, so the Spanish decimal-comma question only applies to on-screen tiles.

**Open points**

- The "small money saving" wording still loses the hedge from my earlier note about the short procedure. The 1.4x only holds for that procedure, and at 5,243 tokens the gap is 2.51x. If you want the hedge, it needs its own line, which will need a caption split across two rows.
- I recounted the narration at 132 words. The earlier count of 127 was short by about five. The length is still within 30–60 s.
- The caption speed on the rewritten lines is estimated at about 14–16 characters per second. `npm run lint` will check it once timings exist.
