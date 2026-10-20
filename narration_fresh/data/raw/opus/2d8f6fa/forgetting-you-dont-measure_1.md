Here's the revised script. Only the narration lines, word count and spoken forms changed. Components, visuals and source sentences are the same, apart from the new verdict line.

**What changed and why**
- **Scene 6 sounded like a table read aloud.** It was four short lines in a row: "full FT fell 0.071. LoRA rose 0.033. Full FT scored 0.00. LoRA got 0.15." Each pair is now one sentence that compares the two methods. The captions still show the numbers as the article writes them.
- **Scene 3 was unclear.** "0 to 50% general text" didn't say what the mixing was for. It now says the mixing is meant to fight forgetting and names the four levels the article tested.
- **The ending gives a clear verdict.** Full fine-tuning paid three costs that one benchmark undersold, and LoRA learned the task just as well and barely forgot. Both are the article's own words.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | To fight forgetting, I mixed general text into each batch: | Para frenar el olvido, mezclé texto general en cada lote: | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia)"; "Ten percent replay recovers about 73% of the average forgetting" |
| 3 Experiment | **bespoke** | zero, 10%, 25% or 50%. | cero, 10%, 25% o 50%. | Bar steps through each level | "Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy jumped from ~0.36 to ~0.90. | Sin mezcla, la precisión en la tarea saltó de ~0.36 a ~0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped 0.078 on average. | Pero la precisión general cayó 0.078 de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning fell 0.071, | En seguir instrucciones, el fine-tuning completo cayó 0.071, | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | while LoRA actually rose 0.033. | mientras que LoRA incluso subió 0.033. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On commands it never saw, full fine-tuning scored 0.00, | Con comandos que nunca vio, el fine-tuning completo sacó 0.00, | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | but LoRA still got 0.15. | pero LoRA aún sacó 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, full fine-tuning paid three costs | En estas pruebas, el fine-tuning completo pagó tres costes | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | that one benchmark undersold. | que un solo benchmark subestimó. | Quote stays on screen | Same sentence |
| 7 So what | `KeyQuote` | LoRA learned the task just as well and barely forgot. | LoRA aprendió la tarea igual de bien y apenas olvidó. | **New:** verdict line large: "LoRA: same skill, barely forgot" | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 157 words in English, about 60 s at a normal speaking pace. That's over the 140-word guide and the 45 s target. The skill now allows it ("clarity beats brevity", and every key point gets its own line). If you need it shorter, the easiest cuts are "at no cost to the new task." and "Check more than one capability, / and pick your training method on purpose.", which together bring it down to about 54 s. The verdict line should stay.

## Spoken forms (the captions stay as written)
- "0.5B" → "zero point five B"
- "~0.36 to ~0.90" → "about 0.36 to about 0.9" (ES: "cerca de 0.36 a cerca de 0.9")
- "0.00" → "zero" (ES: "cero")
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3, which now covers two lines. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the longest English captions are now the first line of scene 3 (58 characters) and the two longer lines of scene 6 (54–55 characters). By my estimate they run at about 14–15 characters per second. In Spanish, the third line of scene 6 ("Con comandos que nunca vio…", 62 characters) and the first verdict line are the riskiest. Run `npm run lint` on both cuts before anything is built.
3. **Number style in Spanish:** I kept decimal points ("0.078") so both cuts match the English article. If the Spanish article uses decimal commas ("0,078"), change the Spanish captions to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: I used the absolute −0.071 from the article's table instead.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
