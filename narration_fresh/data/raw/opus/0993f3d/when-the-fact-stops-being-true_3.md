Here's the revised script. I changed the narration in three lines (8, 9 and 13) and nothing else.

**What changed:**
- **Scene 4 (lines 8–9):** The old lines said two similar odd fractions in a row ("70 of 72… 10 of 72"). Now only the transcript's 10 of 72 is spoken, because that's the result the hook sets up. Explicit state becomes "almost every time," and the 70/72 bar still shows the exact figure. "Three models" moved to line 8 so it isn't in the same sentence as 10 of 72.
- **Scene 6 (line 13):** The voice no longer says "7.5x" and "1.4x" together. It says only 1.4x, the bill figure that makes the point. The 7.5x stays on the tile.

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
| 4 Finding | BarCompare | Across three models, explicit state applied the fix almost every time. | En tres modelos, con estado explícito la aplicó casi siempre. | Teal bar: 70/72 | "Re-measured per episode on the real trajectory, across three models… explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | With the full transcript, only 10 of 72. | Con el historial completo, solo en 10 de 72. | Grey bar: 10/72 | "…and the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, the token saving shrank to 1.4x on the bill. | Con caché, el ahorro de tokens se quedó en 1,4x en la factura. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 128 words, about 49 s (within 30–60 s, a bit over the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 1.4x → "one point four times" (ES: "una coma cuatro veces")
- 10 of 72 → spoken in full
```

Things to check before approving:

1. **I left out the retracted numbers.** I didn't change this point. The article's correction note withdraws 3/44 vs 44/44 and "93 of 93", but they still appear in the LinkedIn summary, the opening paragraphs, the figure captions and the takeaways. The script only uses the re-measured 70/72 vs 10/72 (three models). Until the article body is updated, its numbers won't match the video.
2. **The 1.4x figure only holds for the short procedure.** With the realistic 5,243-token procedure, the gap is 2.51x in money. If you want that hedge, line 13 could become "In my short-procedure runs, the token saving shrank to 1.4x on the bill." That's too long for two caption rows, so it would need to be split across two lines.
3. **Line 12 may overstate the result.** "Fewer tokens isn't a smaller bill" follows the article's own sentence ("the bill savings are not"). Read literally, though, 1.4x is still a smaller bill. You could soften it to "But fewer tokens isn't a much smaller bill," which would also make the article's wording more accurate.
4. **The Spanish uses a decimal comma (1,4x).** It now appears in one ES caption and on the tiles. If the Spanish article writes it with a point, both need to match it.
5. **Scene 2 is marked bespoke.** None of the library components shows a prompt stack shrinking into a state chip. If you'd rather not build a custom animation, the fallback is a two-lane `FlowDiagram`.
6. **Caption speed is estimated, not checked.** At about 2.6 words per second, the new line 8 is the closest to the 17 characters-per-second limit (about 16.5), followed by lines 6 and 10 (about 15–16). If lint flags line 8, cut "Across three models" from the voice and keep it as an on-screen label. `npm run lint` will confirm once the timings exist.
