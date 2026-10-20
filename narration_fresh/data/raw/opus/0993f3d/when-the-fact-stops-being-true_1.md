Here is the revised script. Only the narration changed. Each spoken number now stands alone, and the other figures appear only in the visuals.

```markdown
# Script: When the Fact Stops Being True

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | My agent had the correction in context. | Mi agente tenía la corrección en contexto. | Title card "When the Fact Stops Being True"; a crossed-out shelf record flickers under the title | "The full transcript, which physically contains the correction…" |
| 1 Hook | intro card | Most of the time, it acted on the old fact. | La mayoría de las veces, usó el dato viejo. | Same card; the stale record stays lit | "…explicit state applies the correction in 70 of 72 episodes and the full transcript in 10 of 72" (correction box) |
| 2 Setup | bespoke | I was replicating SKILL.state, an EMNLP paper. | Estaba replicando SKILL.state, un paper de EMNLP. | **Bespoke:** a prompt stack (procedure / transcript / observation) where the tall grey transcript block shrinks into a small amber "state" chip | "A replication of SKILL.state, an EMNLP paper…" |
| 2 Setup | bespoke | It swaps the agent's transcript for a small state object. | Cambia el historial del agente por un pequeño estado. | Chip settles between procedure and observation | "…replaces an agent's conversation history with an explicit mutable state." |
| 3 Experiment | FlowDiagram | The agent files a pallet on a shelf. | El agente guarda un palé en una balda. | Node "step t: pallet filed on shelf" | "the agent files a pallet at step `t`" |
| 3 Experiment | FlowDiagram | Later, a correction: that shelf is empty. | Después, una corrección: la balda está vacía. | Node "t+10: correction, shelf empty" | "at `t+10` a correction says that put-away never completed and the shelf is empty" |
| 3 Experiment | FlowDiagram | Every decision after that depends on the fix. | Cada decisión posterior depende de esa corrección. | Arrow fans out to later decisions | "every subsequent decision depends on having applied the correction" |
| 4 Finding | BarCompare | With explicit state, it applied the fix almost every time. | Con estado explícito, aplicó la corrección casi siempre. | Teal bar: 70/72 (label on screen) | "explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | Across three models, the full transcript managed 10 of 72. | En tres modelos, el historial completo logró 10 de 72. | Grey bar: 10/72 | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, the money saved was just 1.4x. | Con caché, el ahorro en dinero fue de solo 1,4x. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 127 words, about 49 s (within 30–60 s, a bit over the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 1.4x → "one point four times" (ES: "una coma cuatro veces")
- 10 of 72 → spoken in full
```

**What changed:**
- **Scene 4:** The narration used to say "70 of 72" and then "10 of 72" back to back. Now it says only 10 of 72, the number that backs up the hook. Explicit state's result is spoken as "almost every time", and the 70/72 stays on the teal bar.
- **Scene 6:** The narration used to say both figures in one line ("a 7.5x token saving became 1.4x"). Now it speaks only 1.4x, the number that makes the point. The 7.5x stays on the tile.
- **Scene 3:** "Ten steps later" is now just "Later". The gap still shows on screen as "t+10".
- **Spoken forms:** I removed the entries for 7.5x and 70 of 72, since neither is spoken any more.

**Updates to the approval checks:**
- **Check 2:** The hedged version of the cost line would now be "In my short-procedure runs, the money saved was just 1.4x." That is still too long for two caption rows, so it would still need splitting.
- **Check 3:** The decimal comma now appears only in the Spanish caption 1,4x and on the Spanish 7,5x / 1,4x tiles.
- **Check 5:** The two new scene 4 lines are about 58 characters each, which works out to roughly 15 characters per second. They're now closest to the 17 characters-per-second limit, along with lines 6 and 10. `npm run lint` will confirm once the timings exist.
