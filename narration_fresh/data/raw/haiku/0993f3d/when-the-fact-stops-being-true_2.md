Here is the revised script. The captions and the table are unchanged. Only the spoken forms changed, following the Voice rule to say one number per line at most and to leave the rest on screen.

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
| 4 Finding | BarCompare | Explicit state applied the fix in 70 of 72 episodes. | Con estado explícito, la aplicó en 70 de 72 episodios. | Teal bar: 70/72 | "explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | Across three models, the full transcript: 10 of 72. | En tres modelos, el historial completo: 10 de 72. | Grey bar: 10/72 | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, a 7.5x token saving became 1.4x in money. | Con caché, un ahorro de 7,5x en tokens fue 1,4x en dinero. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count (spoken):** 123 words, about 47 s (within 30–60 s, near the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- Scene 4, line 1 → voiced: "Explicit state applied the fix in almost every episode." (ES: "Con estado explícito, la aplicó en casi todos los episodios.")
- Scene 4, line 2 → voiced: "Across three models, the full transcript managed ten." (ES: "En tres modelos, el historial completo logró solo diez.")
- Scene 6, line 2 → voiced: "With caching on, most of that saving never reaches the bill." (ES: "Con caché, la mayor parte de ese ahorro no llega a la factura.")
```

**What changed in the narration**

- **Scene 4:** The voice no longer says "70 of 72" and "10 of 72" in consecutive lines. It says "almost every episode" and "ten", and the captions and bars keep the exact counts. "Almost every" rounds 70 of 72, so if the article's wording doesn't support that rounding, I can voice "70 of 72" alone and drop the "ten" line's denominator.
- **Scene 6:** The voice no longer chains "7.5x" and "1.4x". It says "most of that saving never reaches the bill", and the caption and the tiles carry the figures. This also removes the spoken forms for 7.5x and 1.4x.

The earlier points still stand, including the short-procedure hedge on 7.5x → 1.4x, the decimal commas in the Spanish, and the bespoke scene 2.
