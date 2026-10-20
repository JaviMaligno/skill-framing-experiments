I changed only the number-heavy lines. The new Voice section says to keep the headline figure spoken and move the rest to the screen when figures pile up. Nothing else in the table changed.

**What changed:**
- **Scene 4, second line.** "70 of 72" followed straight away by "10 of 72" repeated "of 72" in back-to-back lines. The narration now says "just 10", and the grey bar still shows the full 10/72. "Across three models" stays because it limits the claim.
- **Scene 6, second line.** "7.5x … became 1.4x" put two decimal figures in one sentence. The point is the bill, so the narration keeps 1.4x and leaves 7.5x on the tile that dims.
- **Kept on purpose:** the hook's "Most of the time" stays. Saying the count there would repeat the finding three seconds before Scene 4. "Ten steps later" is a single round figure and is fine to say.

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
| 4 Finding | BarCompare | Across three models, the full transcript: just 10. | En tres modelos, el historial completo: solo 10. | Grey bar: 10/72 (full figure on screen) | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, the bill saving is just 1.4x. | Con caché, el ahorro en la factura es solo 1,4x. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 124 words, about 47 s (within 30–60 s, slightly over the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 1.4x → "one point four times" (ES: "una coma cuatro veces"); 7.5x is on screen only, not spoken
- 70 of 72 / 10 → spoken in full
```

**Still to check before approving:**

1. **The retracted numbers are left out.** The correction note withdraws 3/44 vs 44/44 and "93 of 93", but they still appear in the LinkedIn summary, the opening paragraphs, the figure captions and the takeaways. The script uses only the re-measured 70/72 vs 10/72 across three models. The video won't match the article body until the article is updated.
2. **The 1.4x figure only holds for the short procedure.** With the realistic 5,243-token procedure, the money gap is 2.51x. If you want that limit said, the Scene 6 line could become "In my short-procedure runs, the bill saving was 1.4x." Since the line got shorter, that version now fits in two caption rows and wouldn't need to be split.
3. **The Spanish uses a decimal comma (1,4x).** I assumed that's how the Spanish article writes it. If it uses a point, the Spanish caption needs to match.
4. **Scene 2 is still marked bespoke.** If you'd rather not build a custom animation, the fallback is a two-lane `FlowDiagram`.
5. **Caption speed is estimated, not checked.** The lines closest to the 17 characters-per-second limit are still the "Ten steps later" line and the "State has one place" line, at about 15–16. Both rewritten lines are shorter than before. `npm run lint` will confirm once the timings exist.
