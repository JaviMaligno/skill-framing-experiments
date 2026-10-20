I've revised the narration to follow the skill's updated Voice section: numbers are spoken naturally inside sentences instead of being read off like a table. The rest of the script is unchanged: scenes, components, visuals, structure and hedges.

I still have no file-writing tool here, so `script.md` isn't saved. The full script is below, ready to paste once you approve it.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a 0.5B Qwen as a tiny world model: | Entrené un Qwen de 0.5B como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Into each batch, I mixed between 0 and 50% general text. | En cada lote mezclé entre un 0 y un 50% de texto general. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy jumped from ~0.36 to ~0.90. | Sin mezcla, la precisión en la tarea saltó de ~0.36 a ~0.90. | Counter ticks 0.36 → 0.90 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | But general accuracy slipped, by 0.078 on average. | Pero la precisión general bajó, 0.078 de media. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about 73% of that, | Mezclar solo un 10% recuperó cerca del 73%, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On following instructions, full fine-tuning slipped by 0.071, | Al seguir instrucciones, el fine-tuning completo bajó 0.071, | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | while LoRA actually improved, by 0.033. | mientras que LoRA incluso mejoró, 0.033. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On commands it had never seen, full fine-tuning scored 0.00. | Con comandos nunca vistos, el fine-tuning completo sacó 0.00. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**" |
| 6 Hidden costs | `BarCompare` | LoRA still managed 0.15. | LoRA aún logró 0.15. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 140 English words in the narration, or 143 counting the outro line. That's about 55–58 s at a normal speaking pace: inside the 30–60 s range and at the top of the 75–140 word range, but over the 45 s target. The extra words come from the connecting phrases that make the numbers sound natural. The skill says clarity beats brevity, so I kept them. If you want to get closer to 45 s, the easiest cut is still "at no cost to the new task." But it states a key point, so I'd rather keep it.

## What changed in the narration
- **Scene 6 no longer sounds like a table being read aloud.** The four separate "X fell 0.071. Y rose 0.033." lines are now two contrasts, each spoken as one sentence: "full fine-tuning slipped by 0.071, while LoRA actually improved, by 0.033" and "on commands it had never seen, full fine-tuning scored 0.00. LoRA still managed 0.15."
- **Scenes 3 and 4:** the numbers now sit inside full sentences ("Into each batch, I mixed between 0 and 50%…", "task accuracy jumped from…", "slipped, by 0.078 on average").
- **Captions keep the article's numbers exactly:** ~0.36, ~0.90, 0.078, 73%, 0.071, 0.033, 0.00, 0.15. Only the words around the numbers changed.

## Spoken forms (the captions stay as written)
- "0.5B" → "zero point five B"
- "~0.36 to ~0.90" → "about 0.36 to about 0.90" (ES: "alrededor de 0.36 a alrededor de 0.90")
- "0.00" → "zero" (ES: "cero")
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** all captions now fit in two rows of about 32 characters. The longest are lines 5, 6, 12 and 14, at 57–62 characters. In Spanish, lines 5, 6, 12 and 14 are the longest. Run `npm run lint` on both cuts before anything is built.
3. **Number style in Spanish:** I kept decimal points ("0.078") so both cuts match the English article. If the Spanish article uses decimal commas ("0,078"), change the Spanish captions to match it. Also check that the Spanish voice reads "0.078" naturally, and add a spoken form if it doesn't.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: I used the absolute −0.071 from the article's table instead.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
