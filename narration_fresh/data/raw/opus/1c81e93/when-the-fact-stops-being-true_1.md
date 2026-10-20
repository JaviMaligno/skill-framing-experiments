I changed three lines and the spoken-forms list. The rest of the script is the same as before.

**What changed:**
- **Lines 8 and 9 (the finding):** "70 of 72" and "10 of 72" are two unround figures in a row, which is hard to follow by ear. The narration now says what they mean ("almost every time", "rarely"). The exact numbers stay on screen on the `BarCompare` bars.
- **Line 13 (the cost twist):** "7.5x" and "1.4x" are two decimals in a row. The line now says what happened ("most of that saving never reached the bill"), and the `StatGrid` tiles keep the figures.
- **Spoken forms:** the 7.5x/1.4x and 70/72 entries are gone, because those numbers are no longer spoken. "Ten steps later" and "three models" stay as spoken numbers because they're easy to hear and add something.

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
| 4 Finding | BarCompare | Explicit state applied the fix almost every time. | Con estado explícito, la aplicó casi siempre. | Teal bar, labelled large: 70/72 | "explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | With the full transcript, across three models, it rarely did. | Con el historial completo, en tres modelos, rara vez. | Grey bar, labelled large: 10/72 | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, most of that saving never reached the bill. | Con caché, casi todo ese ahorro no llegó a la factura. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 126 words, about 48 s at 2.6 words per second (within 30–60 s, a bit over the 45 s target). The spoken audio may come out slightly shorter, since the long spoken numbers are gone.

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
```

**Things to check before approving:**

1. **I left out the retracted numbers.** This hasn't changed. The article's correction note withdraws 3/44 vs 44/44 and "93 of 93", but they still appear in the LinkedIn summary, the opening paragraphs, the figure captions and the takeaways. The script only uses the re-measured 70/72 vs 10/72 (three models), and those now appear only on screen. If someone compares the video with the article body, the numbers won't match until the article is updated.
2. **The 7.5x → 1.4x figure only holds for the short procedure.** With the realistic 5,243-token procedure the gap is 2.51x in money. If you want that limit stated, line 13 could become "In my short-procedure runs, most of that saving never reached the bill." That needs splitting across two lines to fit the caption limit.
3. **The Spanish decimal commas now only matter in the visuals.** No Spanish caption contains 7.5x or 1.4x any more. The Spanish cut's `StatGrid` tiles should still write the figures the way the Spanish article does (7,5x / 1,4x if it uses commas).
4. **Scene 2 is marked bespoke.** This hasn't changed. None of the library components shows a prompt stack shrinking into a state chip. If you'd rather not build a custom animation, the fallback is a two-lane `FlowDiagram`.
5. **Caption speed is still an estimate.** Lines 6, 9 and 10 are the closest to the 17 characters-per-second limit, at about 15–16. Line 9 is now one of them, because it is the longest new line. `npm run lint` will confirm once the timings exist.
6. **Line 12 overstates the cost result a little.** "Fewer tokens isn't a smaller bill" goes further than the numbers, since 1.4x is still a cheaper bill. It matches the article's phrasing ("the bill savings are not [real]"), so I left it. A version that stays closer to the numbers would be "But fewer tokens isn't the same as a smaller bill."
