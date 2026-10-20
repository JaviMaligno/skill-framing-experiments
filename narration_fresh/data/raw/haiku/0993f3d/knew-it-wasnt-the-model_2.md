# Script: "They knew it wasn't the model. They patched it anyway."

**Target:** about 48 s. **EN:** about 131 spoken words. **ES:** included, line by line.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | They knew it wasn't the model. | Sabían que no era el modelo. | Title card. The line types in. | "They knew it wasn't the model. They patched it anyway." (title) |
| 1 Hook | Intro card | They patched it anyway. | Y lo parchearon igualmente. | A second line lands under the first, in amber. | "And then, having exonerated the box, they patch it anyway." |
| 2 Setup | FlowDiagram (builds) | I swapped the language model for a frozen random forest. | Cambié el modelo de lenguaje por un random forest fijo. | A head box marked "language model" flips into "random forest". | "In the other it's a random forest — trained by distilling the model's own labels, frozen into a pickle, and given the identical interface" |
| 2 Setup | FlowDiagram | Same pipeline, same fault, planted upstream of the head. | Mismo pipeline y mismo fallo, antes de la cabeza. | corpus → **retrieval (planted fault, amber)** → context → the pipeline forks into two heads. | "The fault sits in retrieval, upstream of the head, so it is the same fault in both arms" |
| 3 Experiment | FlowDiagram | Both briefs said re-running gave the same output, every time. | Ambos briefs: volver a ejecutar dio la misma salida, cada vez. | A "260/260 ✓" badge appears on both heads at the same time. The number lives on screen only. | "re-running the classification over the same context reproduced the output in 260 of 260 cases — the real number, identical in both arms" |
| 3 Experiment | FlowDiagram | Twenty agents per arm, no access to the code. | Veinte agentes por brazo, sin acceso al código. | 20 small agent dots line up next to each head. | "Forty agents saw the table without the code, twenty per arm." |
| 4 Finding | BarCompare | 19/20 patched the symptom. | 19/20 parchearon el síntoma. | Two bars, model (teal) and forest (amber), both grow to 19/20. | "Patches the symptom: 19/20, 19/20" |
| 4 Finding | BarCompare | With the model, and without it. | Con el modelo, y sin él. | Both bars pulse at the same height. | "Nineteen of twenty patch the symptom on each side, with the model and without it." (description) |
| 4 Finding | BarCompare | A second sample of forty agents came out the same. | Una segunda muestra de cuarenta agentes salió igual. | A second pair of bars (labelled "sample 2") lands at the same height, 19/20 on screen. | "Patching comes out 19 and 19 both times." |
| 4 Finding | BarCompare | The difference was what they blamed it for. | La diferencia fue de qué lo acusaban. | The bars reset. New label: "calls it random by nature". | "not *how much* they blame the head, but **what they blame it for**." |
| 4 Finding | BarCompare | Fourteen of twenty called the model random by nature. | 14/20 llamaron al modelo aleatorio por naturaleza. | The teal bar grows to 14/20. | "Fourteen of twenty against four of twenty." / chart label "calls it random by nature" |
| 4 Finding | BarCompare | Far fewer said that about the forest. | Bastantes menos lo dijeron del forest. | The amber bar stops at 4/20. Small "p = 0.0018" tag on screen only, not narrated. | "Accuses it of randomness of its own: 14/20, 4/20, 0.0018" |
| 4 Finding | KeyQuote | The forest gets accused of what the system does to it. | Al forest se le acusa de lo que el sistema le hace. | Quote card, first half. | "The forest gets accused of what the system does to it. The model, of what it is." |
| 4 Finding | KeyQuote | The model, of what it is. | Al modelo, de lo que es. | Second half fades in, in teal. | (same) |
| 5 So what | FlowDiagram (callback) | On these runs, patching didn't need a language model. | Aquí, parchear no necesitó un modelo de lenguaje. | The fork diagram comes back. The model head dims and the patch stays on. | "Whatever drives an engineer to smooth an output rather than trace it, **a language model is not a prerequisite.**" |
| 5 So what | FlowDiagram | A closed component was enough. | Bastó con un componente cerrado. | Both heads turn into padlocked black boxes. | "**A closed component is.**" / "One fault, one corpus, two heads." |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card with the URL. | — |

## Notes

- **What changed for the number rule:**
  - **Scene 3, line 1:** "260 of 260" is out of the narration. The badge on screen carries the figure, and "every time" says the same thing in the voice.
  - **Scene 4, line 3:** "19 and 19 again" is replaced by "came out the same". The replication point stays, with 19/20 shown on screen.
  - **Scene 4, line 5:** "14/20" is the one figure spoken in the contrast. It is said as "fourteen of twenty".
  - **Scene 4, line 6:** "Only 4/20" is replaced by "Far fewer". The 4/20 stays on the bar, so the voice never gives two figures in a row.
- **Spoken forms for the TTS:**
  - "19/20" → "nineteen of twenty"
  - "14/20" → "fourteen of twenty"
  - "javieraguilar.ai" → "javier aguilar dot A I"
  - "260 of 260" is no longer spoken, so its spoken form is dropped.
- **Hedges kept:** "On these runs" and "was enough" are unchanged. The p-value stays on screen only.
- **Not verified:** I haven't run `npm run lint`, so the 17 characters-per-second check still needs doing once these lines are in the scene files. I also haven't recounted the caption and ES lengths against the timing. The new EN line "Both briefs said re-running gave the same output, every time." is the longest line I changed, so check it first.
- **Not saved:** I couldn't write `script.md` in this session, so the table is here for approval. Nothing is built yet.
