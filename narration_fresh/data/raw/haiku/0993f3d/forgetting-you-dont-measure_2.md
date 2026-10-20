Captions stay as the article writes them, so nothing on screen changes. The voice-only rewrites are in the Spoken forms section. Scene 4 had three figures in a row and scene 6 had four, so I reduced each to one spoken number that carries the point. The Spanish spoken forms match the English.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in 0 to 50% general text. | Cada lote mezclaba de 0 a 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy went from ~0.36 to ~0.90. | Sin mezcla, la precisión en la tarea pasó de ~0.36 a ~0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped 0.078 on average. | Pero la precisión general cayó 0.078 de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning fell 0.071. | En seguir instrucciones, el fine-tuning completo cayó 0.071. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA rose 0.033. | LoRA subió 0.033. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored 0.00. | Con comandos nuevos, el fine-tuning completo sacó 0.00. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still got 0.15. | LoRA aún sacó 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 128 words in English, counted across every line including the intro and outro cards. The count before this revision was 133, not the 126 I gave earlier. At the same speaking pace as before, that's about 49 s. This is inside 30–60 s but over the 45 s target. Cutting "at no cost to the new task." (7 words) brings it to about 46 s.

## Spoken forms (captions stay as written)

**EN**
- Scene 2, "0.5B" → "zero point five B"
- Scene 3, "Each batch mixed in 0 to 50% general text." → "Each batch mixed in some general text, up to half."
- Scene 4, "With no mixing, task accuracy went from ~0.36 to ~0.90." → "Without mixing, task accuracy jumped."
- Scene 4, "But general accuracy dropped 0.078 on average." → "But general accuracy dropped, on average."
- Scene 4, "Mixing in just 10% won back about 73% of that," → "Just a little mixing won back about three quarters of that,"
- Scene 6, "On instruction-following, full fine-tuning fell 0.071." → "On instruction-following, full fine-tuning got worse."
- Scene 6, "LoRA rose 0.033." → "LoRA went up."
- Scene 6, "On unseen commands, full fine-tuning scored 0.00." → "On unseen commands, full fine-tuning collapsed."
- Scene 6, "LoRA still got 0.15." → spoken as written (the only number left in scene 6)
- "LoRA" → rhymes with "Laura", not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

**ES**
- Escena 2, "0.5B" → "cero punto cinco B"
- Escena 3, "Cada lote mezclaba de 0 a 50% de texto general." → "Cada lote mezclaba texto general, hasta la mitad."
- Escena 4, "Sin mezcla, la precisión en la tarea pasó de ~0.36 a ~0.90." → "Sin mezcla, la precisión en la tarea subió."
- Escena 4, "Pero la precisión general cayó 0.078 de media." → "Pero la precisión general cayó, de media."
- Escena 4, "Mezclar solo un 10% recuperó cerca del 73%," → "Mezclar solo un poco recuperó casi tres cuartos de eso,"
- Escena 6, "En seguir instrucciones, el fine-tuning completo cayó 0.071." → "En seguir instrucciones, el fine-tuning completo empeoró."
- Escena 6, "LoRA subió 0.033." → "LoRA subió."
- Escena 6, "Con comandos nuevos, el fine-tuning completo sacó 0.00." → "Con comandos nuevos, el fine-tuning completo colapsó."
- Escena 6, "LoRA aún sacó 0.15." → spoken as written

The "Things to decide or check" section is unchanged. Its item 2 still applies: lines 10, 12 and 15 are the longest captions, and line 15 is the riskiest for reading speed.
