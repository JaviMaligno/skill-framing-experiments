I changed only the narration lines that had numbers in them. The new rule is to say a number only when it's easy to hear, and otherwise say what it means in words while the figure stays on screen. Every figure the article gives is still shown in the visuals, unchanged. All other columns are as they were, except one line I had to split (scene 4, explained below) and the notes at the end, which I updated where they mentioned changed lines. I still can't write files in this session, so here's the full script to paste into `script.md`.

# script.md — The Forgetting You Don't Measure

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | intro card | I taught a small model a new skill. | Le enseñé una habilidad nueva a un modelo pequeño. | Title card: "The Forgetting You Don't Measure" | "I took `Qwen2.5-0.5B-Instruct` … teaching it to be a tiny world model." |
| 1 Hook | intro card | What it forgot wasn't where I first looked. | Lo que olvidó no estaba donde miré primero. | Card subtitle fades in: "What did it forget?" | "the losses were real, they just weren't in the first place you'd look." |
| 2 Setup | `FlowDiagram` | I trained a small Qwen as a tiny world model: | Entrené un Qwen pequeño como un mini modelo del mundo: | `ls -la` → [0.5B model] → predicted terminal output, exit code | "continually pre-trained the model to predict those outputs — teaching it to be a tiny world model." |
| 2 Setup | `FlowDiagram` | predicting real terminal output. | predecir la salida real de una terminal. | Output box fills with real shell text | "a narrow 'terminal simulator' dataset (real shell commands and their real outputs)" |
| 3 Experiment | **bespoke** | Each batch mixed in general text, from none up to half. | Cada lote mezclaba texto general, desde nada hasta la mitad. | **Bespoke:** one training-batch bar, amber terminal blocks with grey Wikipedia blocks sliding in at 0 → 10 → 25 → 50% | "what fraction of each training batch is *replay* — general text (Wikipedia) … Zero, 10%, 25%, 50%" |
| 4 Finding | `Counter` | With no mixing, task accuracy jumped | Sin mezcla, la precisión en la tarea saltó | Counter starts at 0.36 | "exact-match on held-out outputs jumps from ~0.36 to ~0.90" |
| 4 Finding | `Counter` | from about a third to nine in ten. | de cerca de un tercio a nueve de cada diez. | Counter ticks 0.36 → 0.90 | Same sentence |
| 4 Finding | `Counter` | But general accuracy slipped across the board. | Pero la precisión general cayó en todos los frentes. | Counter in red: −0.078 | "General accuracy drops across the board: on average −0.078" |
| 4 Finding | `Counter` | Mixing in just 10% won back about three quarters of that, | Mezclar solo un 10% recuperó cerca de tres cuartas partes, | Counter 0 → 73%, labelled "forgetting recovered at 10% replay" | "Ten percent replay recovers about 73% of the average forgetting" |
| 4 Finding | `Counter` | at no cost to the new task. | sin coste para la tarea nueva. | Task accuracy stays pinned at ~0.90 | "at **no cost to the new task** (task accuracy stays at ~0.90)" |
| 5 Method | `FlowDiagram` | Then I tried LoRA, which freezes the original weights. | Luego probé LoRA, que congela los pesos originales. | Base model with a padlock, plus a small adapter block that lights up | "LoRA … freezes the original model and trains only a small set of add-on 'adapter' weights." |
| 5 Method | **bespoke** | It barely forgot, even with no mixing. | Apenas olvidó, incluso sin mezcla. | **Bespoke:** redraw of the article chart. The amber full-FT line climbs toward zero while the blue LoRA line stays flat near zero | "LoRA barely forgets, even with no replay at all, while learning the terminal task just as well" |
| 6 Hidden costs | `BarCompare` | On instruction-following, full fine-tuning got worse. | Siguiendo instrucciones, el fine-tuning completo empeoró. | IFEval bars: Full FT −0.071 | "Instruction-following (IFEval) \| −0.071 \| **+0.033**" |
| 6 Hidden costs | `BarCompare` | LoRA actually got better. | LoRA incluso mejoró. | LoRA bar +0.033 appears | Same table row |
| 6 Hidden costs | `BarCompare` | On unseen commands, full fine-tuning collapsed to zero. | Con comandos nuevos, el fine-tuning completo se hundió a cero. | "Unseen commands" (`sed`, `awk`, pipes): Full FT 0.00 | "World model on unseen commands \| **0.00** \| **0.15**"; "full fine-tuning collapses to zero" |
| 6 Hidden costs | `BarCompare` | LoRA still got some right. | LoRA aún acertó algunos. | LoRA bar 0.15 | "full fine-tuning collapses to zero while LoRA still gets 0.15" |
| 7 So what | `KeyQuote` | On these runs, one benchmark undersold three costs. | En estas pruebas, un solo benchmark subestimó tres costes. | Quote: "One number can quietly stand in for several you didn't check." | "full fine-tuning pays three costs … that a single benchmark undersells" |
| 7 So what | `KeyQuote` | Check more than one capability, | Mide más de una capacidad | Quote stays on screen | "check more than one capability" |
| 7 So what | `KeyQuote` | and pick your training method on purpose. | y elige el método de entrenamiento con intención. | Quote stays on screen | "pick the training method deliberately" |
| 8 Close | outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**Length:** 142 words in English, about 55 s at the same pace as before. That's inside 30–60 s but over the 45 s target and just past the 75–140 word guide, because saying a number in words takes more words than the number. The easiest cut is still "at no cost to the new task.", which would bring it to about 52 s.

## What changed in the narration
- **Line 3:** "a 0.5B Qwen" is now "a small Qwen". The 0.5B stays in the flow box.
- **Line 5:** "0 to 50%" is now "from none up to half". The bar shows the steps 0 / 10 / 25 / 50%.
- **Line 6:** "~0.36 to ~0.90" is now "from about a third to nine in ten". I split this into two rows because the new wording didn't fit in two caption rows of about 32 characters.
- **Line 7:** "dropped 0.078 on average" is now "slipped across the board", which is the article's own phrase. The −0.078 stays on the counter.
- **Line 8:** I kept "10%" because it's easy to hear and it's the point of the line. "About 73%" is now "about three quarters", and the counter still shows 73%.
- **Lines 12 and 13:** "fell 0.071 / rose 0.033" is now "got worse / actually got better". That was two unround numbers in a row; the bars show the values.
- **Lines 14 and 15:** "scored 0.00 / got 0.15" is now "collapsed to zero / got some right". "Zero" is easy to hear and it's how the article puts it. The 0.15 moves to the bar.
- **Line 16:** I kept "one" and "three". They're easy to hear and they carry the point.

## Spoken forms (the captions stay as written)
- "LoRA" → "LoRA" (rhymes with "Laura"), not spelled out
- "IFEval" isn't spoken; it only appears as the chart label in scene 6
- The spoken forms for "0.5B" and "~0.36 to ~0.90" are gone, because those numbers are no longer in the narration.

## Things to decide or check
1. **Two bespoke scenes:**
   - The batch-mixing bar in scene 3. This is the scene that shows how the experiment works.
   - The redrawn chart in scene 5, where one line rises and the other stays flat.

   Either one could fall back to a `FlowDiagram` or a `BarCompare` if you don't want new animation work.
2. **Reading speed:** the longest captions are now lines 5, 9 and 15; line 16 is no longer a risk. The Spanish versions of lines 5, 7, 9, 13 and 15 need `npm run lint` before anything is built.
3. **Number style in Spanish:** decimals now appear only in the on-screen figures, not in the captions. If the Spanish article uses decimal commas ("0,078"), change the Spanish chart and counter labels to match it.
4. **What I cut and why:**
   - The 82% worst-case recovery: there wasn't time for it.
   - The base-vs-instruct and size comparisons: the article calls them nuances.
   - IFEval's "37% relative" drop: the chart shows the absolute −0.071 from the article's table.
   - The hedges are kept as the article writes them: "on these runs" and "undersold", not "hid".

If you approve, the next step is filling in the scene settings.
