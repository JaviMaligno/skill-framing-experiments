I've revised the script to follow the updated rule on spoken numbers. In the old version, scenes 4 and 6 strung together seven unround decimals (0.36, 0.90, 0.078, 0.071, 0.033, 0.00, 0.15). Now the narration keeps only the figures that make the point: the 10 % mix winning back about 73 % of the loss, and full fine-tuning collapsing to zero on unseen commands. The other figures are still on screen in the `Counter` and `BarCompare` visuals, which were already showing them. I changed six lines; scenes, components, visuals, sources and the Spanish cut are otherwise the same.

I still can't write files in this session, so here is the full script to paste into `script.md`.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in 0 to 50% general text. | Cada lote mezclaba de 0 a 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, it learned the task well. | Sin mezcla, aprendió bien la tarea. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped across the board. | Pero la precisión general cayó en todas las pruebas. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning got worse. | En seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA improved. | LoRA mejoró. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning collapsed to zero. | Con comandos nuevos, el fine-tuning completo cayó a cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still got some right. | LoRA aún acertó algunos. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 125 words in English, about 45–47 s at a normal speaking pace. That's down from about 48 s, mostly because long decimals like "zero point zero seven eight" are gone. It's now close to the 45 s target, so cutting "at no cost to the new task." is optional rather than needed.

## Spoken forms (the captions stay as written)
- "0.5B" → "zero point five B"
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.
   
   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** Most of the changed lines are shorter than before. The longest captions are now "Then I tried LoRA…" and "On unseen commands, full fine-tuning collapsed to zero." The second one is one word longer than the line it replaced. Spanish lines run longer, so run `npm run lint` on both cuts before anything is built; these reading speeds are estimates, not lint results.
3. **Number style in Spanish:** the only decimal left in the narration is "0.5B". I kept the decimal point to match the English. If the Spanish article uses decimal commas, change the on-screen labels (−0,078 and so on) to match it.
4. **Numbers on screen only:** 0.36 → 0.90, −0.078, −0.071, +0.033 and 0.15 now appear only in the visuals and are no longer in the captions. Make sure each of those scenes holds the number long enough to read.
5. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: left out as before. The absolute −0.071 from the article's table stays on screen only.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
