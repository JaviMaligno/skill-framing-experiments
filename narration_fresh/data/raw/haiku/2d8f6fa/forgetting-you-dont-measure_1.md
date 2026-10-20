# script.md: The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in between 0 and 50% general text. | Cada lote mezclaba entre 0 y 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy went from about 0.36 to about 0.90. | Sin mezcla, la precisión en la tarea pasó de unos 0.36 a unos 0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped 0.078 on average. | Pero la precisión general cayó 0.078 de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning fell 0.071, | En seguir instrucciones, el fine-tuning completo cayó 0.071, | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | while LoRA rose 0.033. | mientras LoRA subió 0.033. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored 0.00, | Con comandos nuevos, el fine-tuning completo sacó 0.00, | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | while LoRA still got 0.15. | mientras LoRA aún sacó 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 135 words in English, about 51 s at the pace implied by the earlier estimate (about 158 wpm). The previous draft's 126-word count was wrong; the actual count for that version was 132. This is inside the 30–60 s range but above the 45 s target. Cutting "at no cost to the new task." (7 words) brings it to about 48 s, and I'd still want to hear it read aloud before settling on a cut.

## What changed
- **Number-bearing lines now sit inside full sentences** instead of standing alone. The scene 6 pairs are one comparison each ("…fell 0.071, while LoRA rose 0.033"), not two isolated figures.
- **Approximations are spoken as words** ("about 0.36 to about 0.90" instead of "~0.36 to ~0.90"), so the caption and the voice match.
- **Ranges are spoken as ranges** ("between 0 and 50%").
- **Components, visuals, source sentences, and scene structure are unchanged.** The Spanish cut follows the same changes line by line.

## Spoken forms (captions stay as written)
- "0.5B" → "zero point five B"
- "0.00" → "zero" (scene 6, unseen commands)
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Still to check
1. **Reading speed:** I can't run `npm run lint` from this session. Run it on the EN and ES captions before building. Lines 15 and 17 are the riskiest in Spanish.
2. **Decimal style in Spanish:** I kept decimal points ("0.078") to match the English article. If the Spanish article uses decimal commas, change the Spanish captions to match.
3. **Two bespoke scenes** (scene 3 batch bar, scene 5 redrawn chart) can fall back to `FlowDiagram` or `BarCompare` if you'd rather skip new animation work.

I don't have a file-writing tool here either, so paste the table above into `script.md` once you approve it.
