Here is the full revised script. Two lines had a pile-up of figures, so I changed those and left everything else as it was.

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
| 4 Finding | BarCompare | Across three models, the full transcript: just 10. | En tres modelos, el historial completo: solo 10. | Grey bar: 10/72 (denominator on screen) | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, the big token saving shrank to 1.4x in money. | Con caché, el gran ahorro en tokens se quedó en 1,4x en dinero. | 7.5x tile dims (shown, not spoken), 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 127 words, about 47 s (within 30–60 s, slightly over the 45 s target; dropping "seven point five times" from the audio shortens the spoken length a little).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 1.4x → "one point four times" (ES: "una coma cuatro veces")
- 70 of 72 / 10 → spoken in full
```

**What changed and why:**

- **Line 9 (finding):** "10 of 72" became "just 10". Together with line 8, the narration was saying four figures with "of 72" twice in a row. Both counts are still spoken because the contrast between them is the finding. The denominator stays on the bar.
- **Line 13 (cost twist):** "a 7.5x token saving became 1.4x" packed two unround figures into one sentence. The 1.4x carries the point (the bill barely moves), so it stays in the narration. The 7.5x now only appears on its tile. I updated the spoken forms to match.
- **Unchanged on purpose:** the hook still says "Most of the time" instead of a count. The exact counts come about 15 s later in scene 4, and saying them in the hook too would repeat them. If you'd rather lead with the count, the hook line could be "It applied it in just 10 of 72 episodes." Then line 9 would need different wording so the number isn't said twice.

**Earlier notes, updated:**

1. **Retracted numbers.** No change: the script still uses only the re-measured 70/72 vs 10/72, so it won't match the parts of the article that haven't been updated yet.
2. **The 1.4x only holds for the short procedure** (with the realistic procedure the gap is 2.51x). Now that 7.5x is gone from the narration, there's room for the hedge on one line: "In my short-procedure runs, the token saving shrank to 1.4x in money." That's about 50 characters, so check it against the caption limits.
3. **Spanish decimal comma.** Only 1,4x is affected now, in the line 13 caption and on the tile. Check it against the Spanish article.
4. **Scene 2 is still bespoke.** The fallback is still a two-lane `FlowDiagram`.
5. **Caption speed is still an estimate.** Line 13 is now 62 characters, a few more than before, so watch its timing when `npm run lint` runs.
