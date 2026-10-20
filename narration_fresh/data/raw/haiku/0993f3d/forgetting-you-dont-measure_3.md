I revised the narration so each line voices at most one figure, and the rest stay on screen. The changes:

- **Scene 3:** "0 to 50%" became "up to half," with the 0, 10, 25 and 50% steps shown in the bar.
- **Scene 4:** "from ~0.36 to ~0.90" became "jumped to about 0.90," with the climb on the counter. "0.078" is now on screen only. "10%" moved into the counter label, and the voice keeps "about 73%."
- **Scene 6:** the four figures in a row (−0.071, +0.033, 0.00, 0.15) are now words, with the bars carrying the numbers.

## script.md

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in up to half general text. | Cada lote mezclaba hasta la mitad de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy jumped to about 0.90. | Sin mezcla, la precisión en la tarea subió a cerca de 0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped, on average. | Pero la precisión general bajó, de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Replaying just a little general text won back about 73% of that, | Repasar solo un poco de texto general recuperó cerca del 73% de ese olvido, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning lost ground. | En seguir instrucciones, el fine-tuning completo perdió terreno. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA went the other way. | LoRA fue en sentido contrario. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning collapsed to zero. | Con comandos nuevos, el fine-tuning completo se hundió a cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still held up. | LoRA aguantó. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 133 words in English before the outro card, about 50 s at a normal pace. That's inside the 30–60 s range and above the 45 s target. My recount of the previous version came to about 132 words, not the 126 I reported, so the earlier figure was low. To reach 45 s, the cut I'd still make first is "at no cost to the new task."

## Spoken forms (the captions stay as written)
- "0.5B" → "zero point five B"
- "about 0.90" → "about zero point nine"
- "73%" → "seventy-three percent"
- "0.078", "0.071", "0.033" and "0.15" are not spoken. They stay on screen.
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Still to check
- The reading-speed numbers from my last message no longer apply, because the lines were renumbered and some got shorter. Run `npm run lint` on both cuts before building.
- The two bespoke scenes (the batch-mixing bar in scene 3 and the redrawn chart in scene 5) still stand, with the same fallbacks as before.
- Decimal points are kept in the Spanish cut. Change them to decimal commas if the Spanish article uses them.
