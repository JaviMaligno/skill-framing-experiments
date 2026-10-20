I revised the narration to follow the updated rule on spoken numbers. The old script read eight figures aloud in scenes 4 and 6, many of them long decimals ("0.36… 0.90… 0.078… 0.071… 0.033…"). The narration now says only the figures that carry the point:

- **"10%… 73%"** is the headline.
- **"zero"** is the collapse.
- **"0.15"** is LoRA's counterweight.

The other figures still appear in each scene's visual, so the viewer sees them on screen without hearing them.

The scenes, components, visuals and hedges are unchanged. I updated the notes only where they referred to the old lines.

# script.md: The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained it as a tiny world model: | Lo entrené como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | I varied how much general text each batch mixed in. | Varié cuánto texto general se mezclaba en cada lote. | **Bespoke:** one training-batch bar. Amber terminal blocks, with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50%. Each step is labelled on screen. | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy shot up. | Sin mezcla, la precisión en la tarea se disparó. | Counter ticks 0.36 → 0.90, labelled "task accuracy" | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped across the board. | Pero la precisión general cayó en todas las pruebas. | Counter in red: −0.078, labelled "average general accuracy" | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning got worse. | En seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA actually improved. | LoRA incluso mejoró. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning collapsed to zero. | Con comandos nuevos, el fine-tuning completo cayó a cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 6 Hidden costs | `BarCompare` | LoRA still got 0.15. | LoRA aún sacó 0.15. | LoRA bar 0.15 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 129 words in English, about 48–50 s.

- The count is slightly higher than before. However, the spoken time is about the same or a little shorter, because the decimals that were removed each took several spoken words ("zero point zero seven eight").
- It's still inside the 30–60 s range but over the 45 s target. To hit 45 s, the easiest cut is still the "at no cost to the new task." line.

## Spoken forms (the captions stay as written)
- "0.15" → "zero point one five"
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "0.5B" and "IFEval" aren't spoken. They only appear on screen, in scenes 2 and 6.

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works, and it now also carries the 0/10/25/50% fractions on screen.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the longest captions are now lines 5, 10, 12 and 14, all around 51–55 characters. Line 14 is the riskiest. The Spanish versions of lines 5, 7, 12 and 14 run longer, so they need `npm run lint` before anything is built.
3. **Number style in Spanish:** only "10%", "73%" and "0.15" are spoken now. I kept the decimal point in "0.15" to match the English article. If the Spanish article uses decimal commas ("0,15"), change that caption and the on-screen labels to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: the bar shows the absolute −0.071 from the article's table instead.
   - The spoken figures 0.36, 0.90, 0.078, 0.071 and 0.033 now appear only on screen, so the narration doesn't stack figures.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
