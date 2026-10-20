Here's the revised script. The narration now carries one number per line or none. The on-screen visuals (Counter, BarCompare) keep the exact figures, so the viewer still sees them. The Spanish cut follows the same changes.

# script.md: The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in zero to half general text. | Cada lote mezclaba de cero a la mitad de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy jumped to about 0.90. | Sin mezcla, la precisión en la tarea subió a unos 0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped, on average. | Pero la precisión general bajó, de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back most of that, | Mezclar solo un 10% recuperó la mayor parte de eso, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning fell. | En seguir instrucciones, el fine-tuning completo cayó. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA rose. | LoRA subió. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored zero. | Con comandos nuevos, el fine-tuning completo sacó cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still got 0.15. | LoRA aún sacó 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 124 spoken words in English (127 with the outro card), about 47 s at a normal pace. That's inside the 30–60 s range but still a little over the 45 s target. The cuts were short numbers, so the total barely moved. The "at no cost to the new task." line is still the easiest cut if you need 45 s.

## Spoken forms (captions stay as written, except where the narration drops a figure)
- "0.5B" → "zero point five B"
- "about 0.90" → "about zero point nine"
- "10%" → "ten percent"
- "0.15" → "zero point one five"
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6
- The figures 0.36, −0.078, 73%, −0.071, +0.033 and 0.00 are no longer spoken. They stay on screen in the Counter and BarCompare visuals.

## Things to decide or check
1. **Captions and visuals:** the caption is burned in from the narration, so it now omits 0.36, −0.078, 73%, −0.071 and +0.033. Those values must be legible on the Counter and BarCompare visuals. The caption says "zero" where the chart shows 0.00. That's a word for the same value, but say so if you'd rather the caption match the chart.
2. **Two bespoke scenes:** the batch-mixing bar in scene 3 and the redrawn chart in scene 5. Either can fall back to a `FlowDiagram` or `BarCompare` if you don't want new animation work.
3. **Reading speed:** the line lengths changed, so `npm run lint` needs to run again on both cuts before anything is built. The Spanish lines run longer, so check them first.
4. **Number style in Spanish:** I kept decimal points ("0.90", "0.15") so both cuts match the English article. If the Spanish article uses decimal commas, change the Spanish captions to match.
5. **What I cut and why** (unchanged from before): the 82% worst-case recovery, the base-vs-instruct and size comparisons, and IFEval's "37% relative" drop. The hedges stay as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
