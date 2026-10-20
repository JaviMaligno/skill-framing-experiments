I've revised the narration to match the updated Voice rule on spoken numbers. The figures that had been chained or hard to say now stay on screen, and the voice says one number per point. Scenes, components, visuals and structure are unchanged. I still have no file-writing tool here, so the full script is below to paste into `script.md`.

# script.md: The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a small Qwen as a tiny world model: | Entrené un Qwen pequeño como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in a share of general text. | Cada lote mezclaba una parte de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, it learned the task: accuracy jumped. | Sin mezcla, aprendió la tarea: la precisión se disparó. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped across the board. | Pero la precisión general cayó en todos los frentes. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | A little general text won back about 73% of that, | Un poco de texto general recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On following instructions, full fine-tuning got worse. | En seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA actually got better. | LoRA incluso mejoró. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On commands it never saw, full fine-tuning scored zero. | Con comandos nuevos, el fine-tuning completo sacó cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**"; "full fine-tuning collapses to zero" |
| 6 Hidden costs | `BarCompare` | LoRA still got some right. | LoRA aún acertó algunos. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 136 words in English, including the outro. That's about 48–50 s, roughly the same as before: the line count is up a little, but the voice no longer reads out long decimals. The fastest way to get to 45 s is still to cut "at no cost to the new task."

## What changed (narration only)
- **Scene 2:** the voice no longer says "0.5B". The size stays on the diagram.
- **Scene 3:** the voice no longer says "0 to 50%". The bespoke bar shows the four replay levels.
- **Scene 4:** the voice no longer says "~0.36 → ~0.90" or "0.078". The voice keeps one figure, **"about 73%"**, worded as the article words it. The 10% replay level is on the counter label.
- **Scene 6:** the voice no longer reads out four decimals in a row (−0.071, +0.033, 0.00, 0.15). It now says got worse / got better / **zero** / some right, and the bars show the exact values. "Zero" is the article's own wording.

## Spoken forms (the captions stay as written)
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6
- The "0.5B" and "~0.36 to ~0.90" entries are gone because those numbers are no longer spoken.

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works, and it now also carries the replay levels.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the longest captions are now lines 3, 8 and 14. The Spanish lines run longer, so the Spanish versions of lines 3, 6, 7, 12 and 14 need `npm run lint` before anything is built.
3. **Number style in Spanish:** decimals now only appear in the on-screen labels. If the Spanish article uses decimal commas ("0,078"), change those labels in the Spanish cut to match.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: the bar shows the absolute −0.071 from the article's table instead.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".
5. **Two other new rules I didn't apply, since you asked me to change only the numbers:**
   - **Clarity beats brevity:** the setup might need one more line explaining what "general text" is before scene 3.
   - **Key points loud and clear:** the closing could say the verdict even more plainly.

   Say if you want me to work on either.

If you approve, the next step is filling in the scene settings.
