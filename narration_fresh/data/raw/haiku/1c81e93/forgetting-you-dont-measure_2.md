I rewrote the narration where numbers were hard to hear. The figures stay on screen in the visuals, and the Spanish cut follows the same changes.

- **Scene 2:** "0.5B" is now "half-billion-parameter" in the narration. The FlowDiagram still shows "0.5B".
- **Scene 3:** the batch mix is now "from none to half" instead of listing 0, 10, 25 and 50%.
- **Scene 4:** "about a third to nine in ten", "dropped across the board", "nearly three-quarters".
- **Scene 6:** "lost ground", "gained a little", "scored zero", "about one in seven". The BarCompare bars still show −0.071, +0.033, 0.00 and 0.15.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a half-billion-parameter Qwen as a tiny world model: | Entrené un Qwen de quinientos millones de parámetros como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Batches mixed in from none to half general text. | Cada lote mezclaba desde nada hasta la mitad de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy went from about a third to nine in ten. | Sin mezcla, la precisión pasó de algo más de un tercio a nueve de cada diez. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped across the board, on average. | Pero la precisión general bajó en todas partes, de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just ten percent won back nearly three-quarters of that, | Mezclar solo un 10% recuperó casi las tres cuartas partes de eso, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning lost ground. | En seguir instrucciones, el fine-tuning completo perdió terreno. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA gained a little. | LoRA ganó un poco. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored zero. | Con comandos nuevos, el fine-tuning completo sacó cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still scored about one in seven. | LoRA aún sacó alrededor de uno de cada siete. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad, | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 139 words in English, about 53 s at the pace I used for the earlier estimate. That's inside the 30–60 s range but over the 45 s target. Reaching 45 s would take about 20 fewer words, and I haven't cut any content to get there.

## Spoken forms (captions stay as written)
- Numbers in the narration are now spoken in words. The figures stay on the Counter, BarCompare and FlowDiagram visuals.
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out.
- "IFEval" isn't spoken; it only appears as the chart label in scene 6.

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** I couldn't run `npm run lint` in this session, so the 17 characters-per-second check hasn't been run on the new wording. The Spanish lines run longer than the English, so check all of them, especially the Spanish versions of lines 4, 6, 8, 12 and 15.
3. **Number style in Spanish:** I kept decimal points ("0.078") so both cuts match the English article. If the Spanish article uses decimal commas ("0,078"), change the Spanish captions to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: I used the absolute −0.071 from the article's table instead.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
