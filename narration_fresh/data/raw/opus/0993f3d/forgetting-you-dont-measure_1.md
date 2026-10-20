Here is the revised script. Each number that was chained or unround in the narration has been moved onto the screen. The voice now says at most one figure per point, and the visuals still show every exact value. Components, visuals and scene structure haven't changed. Where a line changed, I updated its source quote to match.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained Qwen as a tiny world model: | Entrené a Qwen como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in a share of general text. | Cada lote mezclaba una parte de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy more than doubled. | Sin mezcla, la precisión en la tarea más que se duplicó. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But its general skills dropped across the board. | Pero su nivel general cayó en todos los frentes. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back most of that, | Mezclar solo un 10% recuperó la mayor parte, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On following instructions, full fine-tuning got worse. | En seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA got better. | LoRA mejoró. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored zero. | Con comandos nuevos, el fine-tuning completo sacó cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 6 Hidden costs | `BarCompare` | LoRA still got some right. | LoRA aún acertó algunos. | LoRA bar 0.15 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 7 So what | `KeyQuote` | Full fine-tuning paid three costs. | El fine-tuning completo pagó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold them. | En estas pruebas, un solo benchmark los subestimó. | Quote stays on screen | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 134 words in English, about 52 s at the same pace as before. That's inside the 30–60 s range but about 7 s over the 45 s target. To get closer, the easiest cuts are "at no cost to the new task." and "LoRA got better."

## Spoken forms (the captions stay as written)
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6
- No other spoken forms are needed. The "0.5B" and "~0.36 to ~0.90" entries are gone because those numbers are no longer spoken.

## What changed in the narration
- **Spoken numbers:** the voice used to say nine figures (0.5B, 0–50%, 0.36, 0.90, 0.078, 73%, 0.071, 0.033, 0.15). Now it says only "10%" and "zero", plus "three costs". The other values stay on screen in the visuals.
- **Wording I chose that you should check against the article:**
  - "More than doubled" is my own reading of 0.36 → 0.90 (about 2.5×). The article doesn't say it.
  - "Most of that" is a softer way to say "about 73%". The exact figure is on the counter.
  - "Some right" stands in for 0.15.
- **Closing verdict:** I split the first so-what line in two so that the verdict gets its own sentence ("Full fine-tuning paid three costs."), as the updated Voice section asks. The hedge "on these runs … undersold" is kept as before.

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the lines are shorter now. The longest are lines 6, 7, 12 and 14. In Spanish, run `npm run lint` on lines 6, 12 and 14 before anything is built.
3. **Number style in Spanish:** the narration no longer contains decimals, so this only affects the on-screen labels (−0.078, 0.15, …). If the Spanish article uses decimal commas, change those labels to match it.
4. **What's still left out:**
   - The 82% worst-case recovery.
   - The base-vs-instruct and size comparisons, which the article calls nuances.
   - IFEval's "37% relative" drop.

If you approve, the next step is filling in the scene settings.
