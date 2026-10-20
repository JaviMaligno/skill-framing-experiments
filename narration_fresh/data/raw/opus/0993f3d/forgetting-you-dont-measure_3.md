# script.md: The Forgetting You Don't Measure

I rewrote the narration so it follows the new rule on spoken numbers. The voice now says one number per point and the other figures stay on screen. Scenes, components, visuals and the closing card haven't changed. I've marked each changed line with ✎.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | ✎ I trained it as a tiny world model: | ✎ Lo entrené como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | ✎ Each training batch mixed in some general text. | ✎ Cada lote de entrenamiento mezclaba algo de texto general. | **Bespoke:** one training-batch bar. Grey Wikipedia blocks slide in among the amber terminal blocks at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | ✎ With no mixing, it learned the task well. | ✎ Sin mezcla, aprendió bien la tarea. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | ✎ But it got worse at general tasks across the board. | ✎ Pero empeoró en todas las tareas generales. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | ✎ A little general text in each batch won back about 73% of that, | ✎ Un poco de texto general en cada lote recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | ✎ On following instructions, full fine-tuning got worse. | ✎ Al seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | ✎ LoRA got slightly better. | ✎ LoRA mejoró un poco. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | ✎ On commands it never saw, full fine-tuning scored zero. | ✎ Con comandos nunca vistos, el fine-tuning completo sacó cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 6 Hidden costs | `BarCompare` | ✎ LoRA still got some right. | ✎ LoRA aún acertó algunos. | LoRA bar 0.15 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 138 words in English, outro included, so about 52 s at the same pace as before. That's inside the 30–60 s range but above the 45 s target. Most of the added words are plain wording that replaces the figures. If you want to get closer to 45 s, the easiest cut is still "at no cost to the new task."

## What the numbers rule changed
- **Scene 4:** the main spoken number is now "about 73%", kept as the article writes it. The values 0.36 → 0.90, −0.078 and 10% are still on the counters and labels, but the voice doesn't say them.
- **Scene 6:** the voice no longer says four decimals in a row. It says which way each method moved, plus one number, "zero", which is the article's own word ("collapses to zero"). The exact values stay on the bars.
- **Scenes 2 and 3:** "0.5B" and "0 to 50%" are now on screen only, in the model box and the batch bar.

## Spoken forms (the captions stay as written)
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6
- The "0.5B" and "~0.36 to ~0.90" spoken forms are no longer needed because neither is in the narration now.

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works, and it now carries the 0 → 50% range on its own.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the riskiest captions are now "On following instructions, full fine-tuning got worse." and "On commands it never saw, full fine-tuning scored zero.", because they are long lines with few words. The Spanish versions of these two lines, and the 73% line in Spanish, need `npm run lint` before anything is built.
3. **Number style in Spanish:** the narration no longer has decimals, so this only affects the on-screen labels (−0.078, 0.36 → 0.90, and the scene 6 bars). If the Spanish article uses decimal commas, change those labels to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: the bar shows the absolute −0.071 from the article's table instead, and the voice only says "got worse".
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
