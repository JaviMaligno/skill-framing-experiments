I changed three narration lines. Everything else in the script is as it was.

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
| 4 Finding | BarCompare | Explicit state applied the fix in almost every episode. | Con estado explícito, la aplicó en casi todos los episodios. | Teal bar: 70/72 | "explicit state applies the correction in 70 of 72 episodes" |
| 4 Finding | BarCompare | Across three models, the full transcript rarely did. | En tres modelos, el historial completo rara vez lo hizo. | Grey bar: 10/72 | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching, a big token saving became a small cost saving. | Con caché, un gran ahorro en tokens fue uno pequeño en dinero. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 125 words, about 47 s (within 30–60 s, a little over the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
```

**What changed in the narration**

- **Scene 4 (70 of 72, then 10 of 72):** These are two unround figures in a row, which are hard to follow by ear. The narration now gives what they mean, "almost every episode" and "rarely did", and the bars keep showing 70/72 and 10/72 exactly. "Rarely" for the transcript is also consistent with the hook's "most of the time, it acted on the old fact".
- **Scene 6 (7.5x to 1.4x):** Two decimal multipliers back to back are just as hard to hear. The line now says "a big token saving became a small cost saving", and the two tiles still show 7.5x and 1.4x.
- **"Ten steps" and "three models"** stay spoken, because they're easy to hear and add something.
- The spoken forms for those numbers are gone, since the narration no longer says them.

**Things to check before approving**

1. **Retracted numbers.** I left these out, as before. The script uses only the re-measured 70/72 vs 10/72. The withdrawn 3/44 vs 44/44 and "93 of 93" still appear in the rest of the article, so the video won't match it until the article is updated.
2. **The 7.5x to 1.4x result only holds for the short procedure.** With the realistic 5,243-token procedure, the money gap is 2.51x. If you want that limit in the video, two lines would do it: "In my short-procedure runs," / "a big token saving became a small cost saving."
3. **Decimal commas in Spanish.** The Spanish captions no longer contain 7,5x or 1,4x. The question now only affects the Spanish tile labels, which should be written the way the Spanish article writes them.
4. **Scene 2 is still bespoke.** If you'd rather not build a custom animation, the fallback is still a two-lane `FlowDiagram`.
5. **Caption speed is estimated, not checked.** Line 13 now has the longest captions: 60 characters in English and about 62 in Spanish, which should still fit in two rows. `npm run lint` will confirm the 17 characters-per-second limit once the timings exist.
