I couldn't diff against the earlier skill text, so I checked the script against the current Voice section. The table's narration lines already read naturally, so I left them unchanged. What needed revising was the spoken-forms section. It still had a few literal readings ("zero point five B", "about 0.36 to about 0.90"), had no Spanish forms, and didn't cover every number. Captions stay as the article writes them.

# script.md: The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in 0 to 50% general text. | Cada lote mezclaba de 0 a 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy went from ~0.36 to ~0.90. | Sin mezcla, la precisión en la tarea pasó de ~0.36 a ~0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped 0.078 on average. | Pero la precisión general cayó 0.078 de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning fell 0.071. | En seguir instrucciones, el fine-tuning completo cayó 0.071. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA rose 0.033. | LoRA subió 0.033. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored 0.00. | Con comandos nuevos, el fine-tuning completo sacó 0.00. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still got 0.15. | LoRA aún sacó 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 126 words in English, about 48 s at a normal speaking pace. That's inside the 30–60 s range but a little over the 45 s target. If you want to hit 45 s, the easiest cut is the "at no cost to the new task." line.

## Spoken forms (captions stay as written)

Each form is what the voice says. The caption shows the number as the article writes it.

| Caption | Spoken EN | Spoken ES |
|---|---|---|
| 0.5B (scene 2, line 1) | a half-billion-parameter Qwen | un Qwen de 500 millones de parámetros |
| 0 to 50% (scene 3) | zero to fifty percent | de cero a cincuenta por ciento |
| ~0.36 to ~0.90 (scene 4, line 1) | about zero point three six to about zero point nine | unos cero coma treinta y seis a unos cero coma nueve |
| 0.078 (scene 4, line 2) | zero point oh seven eight | cero coma cero setenta y ocho |
| 10% and 73% (scene 4, line 3) | ten percent, about seventy-three percent | un diez por ciento, cerca del setenta y tres por ciento |
| 0.071 (scene 6, line 1) | zero point oh seven one | cero coma cero setenta y uno |
| 0.033 (scene 6, line 2) | zero point oh three three | cero coma cero treinta y tres |
| 0.00 (scene 6, line 3) | zero | cero |
| 0.15 (scene 6, line 4) | zero point fifteen | cero coma quince |

The "−" and "+" signs appear only in visuals, never in narration. Narration says "fell" and "rose".

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the longest captions are lines 10, 12 and 15, and line 15 is the riskiest at roughly 16–17 characters per second. Spanish lines run longer, so the Spanish versions of lines 4, 6, 12, 13 and 15 need `npm run lint` before anything is built.
3. **Number style in Spanish:** I kept decimal points ("0.078") in the captions so both cuts match the English article. The spoken Spanish uses decimal commas, as above. If the Spanish article uses decimal commas in its captions too, change them to match.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: I used the absolute −0.071 from the article's table instead.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

I only have the current skill text here, and the narration skill it references isn't loaded in this session. If that skill sets conventions for spoken forms that differ from the ones above, tell me and I'll adjust.
