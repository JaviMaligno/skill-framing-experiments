I revised the narration so that numbers sit inside full sentences with their verbs and objects, not as trailing fragments. The captions still use the article's number format. The spoken forms are listed separately, as the skill requires. Only the English lines changed, plus one Spanish note below. I still can't save `script.md`, so the full script is below.

# script.md: The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in 0 to 50% general text. | Cada lote mezclaba de 0 a 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy went from ~0.36 to ~0.90. | Sin mezcla, la precisión en la tarea pasó de ~0.36 a ~0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy dropped by 0.078 on average. | Pero la precisión general cayó 0.078 de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning fell 0.071. | En seguir instrucciones, el fine-tuning completo cayó 0.071. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA rose by 0.033. | LoRA subió 0.033. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning scored 0.00. | Con comandos nuevos, el fine-tuning completo sacó 0.00. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still got 0.15. | LoRA aún sacó 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 128 words in English, about 49 s at a normal speaking pace. That's inside the 30–60 s range but above the 45 s target. The easiest cut is "at no cost to the new task."

## Spoken forms (the captions stay as written)
- "0.5B" → "zero point five B"
- "~0.36 to ~0.90" → "about 0.36 to about 0.90"
- "0.00" → "zero"
- "10%" and "73%" → "10 percent" and "73 percent"
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## What changed
1. **Scene 4, line 2:** "dropped 0.078" became "dropped by 0.078," so the number sits inside a full clause.
2. **Scene 6, line 2:** "LoRA rose 0.033." became "LoRA rose by 0.033." The Spanish line is unchanged, since "LoRA subió 0.033" already reads as a sentence.
3. **Everything else** is as before. The captions still use the article's figures, and the spoken forms above handle how they are said.

## Things to decide or check
1. **Caption speed:** the two lines I changed are longer, so run `npm run lint` on scene 4 line 2 and scene 6 line 2 (EN and ES) before building. Line 15 ("and pick your training method on purpose.") was already the riskiest at roughly 16–17 characters per second.
2. **Number style in Spanish:** I kept decimal points ("0.078") so both cuts match the English article. If the Spanish article uses decimal commas ("0,078"), change the Spanish captions to match.
3. **Two bespoke scenes:** the batch-mixing bar in scene 3 and the redrawn chart in scene 5. Either can fall back to a `FlowDiagram` or `BarCompare` if you don't want new animation work.
4. **Cuts from the article:** the 82% worst-case recovery, the base-vs-instruct and size comparisons, and IFEval's "37% relative" drop were left out. I used the absolute −0.071 from the article's table instead. The hedges stay as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
