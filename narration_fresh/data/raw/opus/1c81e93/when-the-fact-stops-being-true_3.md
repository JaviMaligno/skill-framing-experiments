I changed three narration lines. In each one the figures were unround and came several in a row, so the voice now says what they mean in words. The exact figures still appear on screen in the bars and tiles, and every other line and column is unchanged.

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
| 4 Finding | BarCompare | Explicit state applied the fix almost every time. | Con estado explícito, la aplicó casi siempre. | Teal bar: 70/72 | "explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | The full transcript, across three models: about one in seven. | El historial completo, en tres modelos: casi una de cada siete. | Grey bar: 10/72 | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, the big token saving shrank on the bill. | Con caché, el gran ahorro en tokens se encogió en la factura. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 126 words, about 46 s (within 30–60 s, close to the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
```

**What changed and why:**
- **Scene 4, line 1:** "70 of 72 episodes" became "almost every time." The bar still shows 70/72.
- **Scene 4, line 2:** "10 of 72" became "about one in seven," which is 10/72 ≈ 14 %. In Spanish, "casi una de cada siete" is also accurate, since 13.9 % is just under 14.3 %. I kept "three models" because it's easy to hear and matters. The bar still shows 10/72.
- **Scene 6, line 2:** "7.5x … 1.4x" became "the big token saving shrank on the bill." The tiles still show both figures.
- **Kept:** "Ten steps later" and "three models" are easy to hear and add something, so they stay spoken.
- **Spoken forms:** I dropped the entries for 7.5x / 1.4x and 70 of 72, because the narration no longer says them.

**Things to check before approving (updated):**

1. **I left out the retracted numbers.** The article's correction note withdraws 3/44 vs 44/44 and "93 of 93", but they still appear in the LinkedIn summary, the opening paragraphs, the figure captions and the takeaways. The video only shows the re-measured 70/72 vs 10/72, now on screen rather than spoken. If someone compares the video with the article body, the numbers won't match until the article is updated.
2. **The 7.5x → 1.4x figure only holds for the short procedure.** With the realistic 5,243-token procedure, the gap is 2.51x in money. If you want that limit in the narration, the second scene 6 line could become "In my short-procedure runs, the big token saving shrank on the bill." That's still too long for two caption rows, so it would have to be split across two lines.
3. **Decimal commas (7,5x / 1,4x) now only matter on the Spanish tiles.** The Spanish captions no longer contain these figures. The tiles should match how the Spanish article writes them.
4. **Scene 2 is marked bespoke.** None of the library components shows a prompt stack shrinking into a state chip. If you'd rather not build a custom animation, the fallback is a two-lane `FlowDiagram`.
5. **Caption speed is estimated, not checked.** The lines closest to the 17 characters-per-second limit are still line 6 and line 10. The second scene 4 line is now the longest caption (about 61 characters), so it needs at least about 3.6 s on screen. `npm run lint` will confirm once the timings exist.
