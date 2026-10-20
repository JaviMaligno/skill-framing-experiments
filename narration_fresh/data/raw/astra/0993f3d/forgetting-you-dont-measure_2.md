# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a small Qwen as a tiny world model: | Entrené un Qwen pequeño como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | I varied how much general text I mixed in. | Varié cuánto texto general añadía a la mezcla. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy rose sharply. | Sin mezcla, la precisión en la tarea subió mucho. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped on average. | Pero la precisión general cayó de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | A little mixing recovered about 73% of that, | Una pequeña mezcla recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning did worse. | Al seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA improved. | LoRA mejoró. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning failed completely. | Con comandos nuevos, el fine-tuning completo falló del todo. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still had some success. | LoRA aún tuvo algunos aciertos. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 126 words in English, about 48 s at a normal speaking pace. That's inside the 30–60 s range but a little over the 45 s target. If you want to hit 45 s, the easiest cut is the "at no cost to the new task." line.

## Spoken forms (the captions stay as written)
- "73%" → "seventy-three percent" in EN; "setenta y tres por ciento" in ES.
- The other experimental figures stay on screen, rather than being read aloud.
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.
   
   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** check the revised captions against their scene durations with `npm run lint` before anything is built. Both cuts need to stay within 17 characters per second and two rows of about 32 characters.
3. **Number style in Spanish:** I kept decimal points ("0.078") in the visuals so both cuts match the English article. If the Spanish article uses decimal commas ("0,078"), change the Spanish visuals to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: the visual uses the absolute −0.071 from the article's table instead.
   - The narration now speaks the central recovery figure and leaves the other experimental numbers on screen.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.