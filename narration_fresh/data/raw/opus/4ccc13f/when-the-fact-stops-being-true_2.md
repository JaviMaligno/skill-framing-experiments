I changed two narration lines: one repeated the same count, and the other said two odd decimals back to back. Everything else is unchanged.

**What changed and why**
- **Line 9 (finding):** "70 of 72" and then "10 of 72" made the ear hear "of 72" twice in a row. Both headline counts are still spoken. The "of 72" for the transcript now shows on the bar label instead.
- **Line 13 (cost twist):** "7.5x … 1.4x" put two decimals together. The line now says only 1.4x, which is the point. The 7.5x stays on screen: it's on the tile and line 12 already sets it up.
- **Left as they were on purpose:** the hook ("Most of the time"), "Ten steps later", "three models" and "70 of 72". None of them pile up, and the skill says not to turn numbers into words by reflex. The exact count comes in scene 4.

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
| 4 Finding | BarCompare | Across three models, the full transcript: just 10. | En tres modelos, el historial completo: solo 10. | Grey bar grows beside the teal one, labelled "10/72" | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, that saving shrank to 1.4x in money. | Con caché, ese ahorro se quedó en 1,4x en dinero. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** about 125 words, about 47 s (within 30–60 s, a little over the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 1.4x → "one point four times" (ES: "una coma cuatro veces")
- 70 of 72 → spoken in full; "just 10" / "solo 10" → spoken as written
```

**Things to check before approving** (the same five as before, with notes 2 and 5 updated):

1. **I left out the retracted numbers.** The article's correction note withdraws 3/44 vs 44/44 and "93 of 93". They still appear in the LinkedIn summary, the opening paragraphs, the figure captions and the takeaways. The script only uses the re-measured 70/72 vs 10/72 (three models). Until the article body is updated, the video and the article won't match.
2. **The 1.4x figure only holds for the short procedure.** With the realistic 5,243-token procedure, the gap is 2.51x in money. If you want that caveat in the narration, line 13 could become "In my short-procedure runs, that saving shrank to 1.4x." That's shorter than the old hedge, but it's still close to two full caption rows, so lint should confirm it.
3. **The Spanish uses decimal commas (1,4x, and 7,5x on the tile).** I assumed that's how the Spanish article writes them. If it uses points, the Spanish captions need to match it.
4. **Scene 2 is marked bespoke.** None of the library components shows a prompt stack shrinking into a state chip. If you'd rather not build a custom animation, the fallback is a two-lane `FlowDiagram`.
5. **Caption speed is estimated, not checked.** The lines closest to the 17 characters-per-second limit are still lines 6 and 10. Lines 9 and 13 are shorter now and further under the limit. `npm run lint` will confirm once the timings exist.
