Here is the revised script. The narration now carries one number per scene. The second figure in each pair moved to the on-screen visual, and the caption follows the narration.

- **Finding (scene 4):** The voice says 70 of 72 for explicit state. The full-transcript line says it "applied it far less often" and leaves 10/72 on the grey bar.
- **Cost twist (scene 6):** The voice says only 1.4x. The 7.5x stays on the tile.
- **Spoken forms:** Dropped the 7.5x entry and the 10 of 72 entry. Added 1.4x.

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
| 4 Finding | BarCompare | The full transcript applied it far less often, across three models. | El historial completo la aplicó con mucha menos frecuencia, en tres modelos. | Grey bar: 10/72 | "Re-measured per episode on the real trajectory, across three models… the full transcript in 10 of 72" |
| 5 Mechanism | KeyQuote | State has one place where the fact lives. | El estado tiene un solo sitio para cada dato. | Quote: "Having a single place where the truth lives is an advantage precisely when the truth changes." | "Explicit state has exactly one place where the fact lives" |
| 5 Mechanism | KeyQuote | The transcript holds the claim and its retraction. | El historial guarda el dato y su retractación. | Same quote, highlight "when the truth changes" | "a transcript holding a claim and its retraction" |
| 6 Cost twist | StatGrid | But fewer tokens isn't a smaller bill. | Pero menos tokens no es una factura menor. | Two tiles: "7.5x tokens", "1.4x money" | "The token savings are real and the bill savings are not" |
| 6 Cost twist | StatGrid | With caching on, the money saving was only 1.4x. | Con caché, el ahorro en dinero fue solo 1,4x. | 7.5x tile dims, 1.4x tile lights up | "7.5x becomes 1.4x once you turn caching on" |
| 7 So what | KeyQuote | Explicit state earns its place when facts change. | El estado explícito compensa cuando los datos cambian. | "Explicit state earns its place when facts get invalidated." | "Explicit state earns its place when facts get invalidated." |
| 7 So what | KeyQuote | Measure the bill, not the token count. | Mide la factura, no los tokens. | "Measure the bill, not the token count." | "Measure the bill, not the token count" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 127 spoken words plus a 3-word outro, about 49 s at 2.6 words per second (within 30–60 s, slightly over the 45 s target).

## Spoken forms (captions stay as written)
- SKILL.state → "skill dot state"
- EMNLP → "E-M-N-L-P"
- 1.4x → "one point four times" (ES: "una coma cuatro veces")
- 70 of 72 → spoken in full
```

Two things to check before approving:

1. **The hedge on 1.4x is gone from the voice.** The earlier caveat still applies: the 1.4x holds for the short procedure, and the realistic 5,243-token procedure gives 2.51x. The on-screen tile can carry that qualifier if you want it there.
2. **The 10/72 figure is only on screen now.** The voice says "far less often," so a viewer who wants the exact comparison has to read the grey bar. The retracted numbers are still excluded, as before.
