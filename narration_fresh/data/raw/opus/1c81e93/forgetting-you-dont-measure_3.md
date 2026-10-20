I've revised the narration for the new number rule. Visuals, components and source quotes are unchanged. Each figure I took out of the spoken line is still on screen in that scene's visual. The length line, the spoken-forms list and the notes changed only where the new narration affects them. I still can't write files in this session, so the full script is below for you to paste into `script.md`.

**Narration changes:**

| Line | Before | After | Why |
|---|---|---|---|
| 3 | "a 0.5B Qwen" | "it" | "Zero point five B" adds little when heard, and the hook already says "small model". 0.5B stays in the diagram box. |
| 5 | "0 to 50%" | (unchanged) | "Zero to fifty percent" is easy to hear and gives the range. |
| 6 | "~0.36 to ~0.90" | "more than doubled" | Two unround decimals in a row are hard to follow. The Counter still shows 0.36 → 0.90. |
| 7 | "0.078" | "across the board" | This is the article's own wording. The Counter still shows −0.078. |
| 8 | "10%" and "73%" | "10%" and "almost three quarters" | "Ten percent" is easy to hear, but two percentages in a row are not. The Counter still shows 73%. |
| 12–13 | "−0.071" and "+0.033" | "got worse" and "got slightly better" | The bars show the figures. "Slightly" keeps the gain as small as it really is. |
| 14 | "scored 0.00" | "collapsed to zero" | "Zero" is the striking number, so it stays spoken. "Collapses to zero" is the article's wording. |
| 15 | "0.15" | "still got some right" | The bar shows 0.15. |
| 16 | "three costs" | (unchanged) | "Three" is easy to hear. |

---

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained it as a tiny world model: | Lo entrené como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in 0 to 50% general text. | Cada lote mezclaba de 0 a 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy more than doubled. | Sin mezcla, la precisión en la tarea subió a más del doble. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped across the board. | Pero la precisión general cayó en todos los frentes. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back almost three quarters of that, | Mezclar solo un 10% recuperó casi tres cuartas partes, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning got worse. | En seguir instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA got slightly better. | LoRA mejoró un poco. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning collapsed to zero. | Con comandos nuevos, el fine-tuning completo cayó a cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still got some right. | LoRA aún acertó algunos. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** about 132 words in English, roughly 51 s at the pace of the previous estimate (126 words for 48 s). That's inside the 30–60 s range but over the 45 s target. If you want to hit 45 s, the easiest cut is still the "at no cost to the new task." line.

## Spoken forms (the captions stay as written)
- "0 to 50%" → "zero to fifty percent"
- "10%" → "ten percent"
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the longest captions are now lines 8, 10 and 14. The short lines (13 and 15) should no longer be at risk. Spanish lines run longer, so the Spanish versions of lines 6, 8, 12 and 14 need `npm run lint` before anything is built.
3. **Number style in Spanish:** decimals now appear only in the visuals (Counters and bars), not in the captions. I kept decimal points ("0.078") so they match the English article. If the Spanish article uses decimal commas ("0,078"), change the Spanish visuals to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: the bar shows the absolute −0.071 from the article's table instead, and the narration says "got worse".
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
