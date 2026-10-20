The narration now speaks only the figures that carry the point: "19/20" and "14/20" stay, and the others move to the visual. The other scenes are unchanged.

# Script: "They knew it wasn't the model. They patched it anyway."

**Target:** about 49 s. **EN:** about 125 caption words, about 133 spoken. **ES:** included, line by line.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | They knew it wasn't the model. | Sabían que no era el modelo. | Title card. The line types in. | "They knew it wasn't the model. They patched it anyway." (title) |
| 1 Hook | Intro card | They patched it anyway. | Y lo parchearon igualmente. | A second line lands under the first, in amber. | "And then, having exonerated the box, they patch it anyway." |
| 2 Setup | FlowDiagram (builds) | I swapped the language model for a frozen random forest. | Cambié el modelo de lenguaje por un random forest fijo. | A head box marked "language model" flips into "random forest". | "In the other it's a random forest — trained by distilling the model's own labels, frozen into a pickle, and given the identical interface" |
| 2 Setup | FlowDiagram | Same pipeline, same fault, planted upstream of the head. | Mismo pipeline y mismo fallo, antes de la cabeza. | corpus → **retrieval (planted fault, amber)** → context → the pipeline forks into two heads. | "The fault sits in retrieval, upstream of the head, so it is the same fault in both arms" |
| 3 Experiment | FlowDiagram | Re-running gave the same output, every time. | Volver a ejecutarlo dio siempre la misma salida. | A "260/260 ✓" badge appears on both heads at the same time. | "re-running the classification over the same context reproduced the output in 260 of 260 cases — the real number, identical in both arms" |
| 3 Experiment | FlowDiagram | Twenty agents per arm, no access to the code. | Veinte agentes por brazo, sin acceso al código. | 20 small agent dots line up next to each head. | "Forty agents saw the table without the code, twenty per arm." |
| 4 Finding | BarCompare | Nineteen of twenty patched the symptom. | 19/20 parchearon el síntoma. | Two bars, model (teal) and forest (amber), both grow to 19/20. | "Patches the symptom: 19/20, 19/20" |
| 4 Finding | BarCompare | With the model, and without it. | Con el modelo, y sin él. | Both bars pulse at the same height. | "Nineteen of twenty patch the symptom on each side, with the model and without it." (description) |
| 4 Finding | BarCompare | A second round of forty agents matched it. | Una segunda ronda de cuarenta agentes dio lo mismo. | A second pair of bars (labelled "sample 2") lands at the same height, showing 19/20 on each side. | "Patching comes out 19 and 19 both times." |
| 4 Finding | BarCompare | The difference was what they blamed it for. | La diferencia fue de qué lo acusaban. | The bars reset. New label: "calls it random by nature". | "not *how much* they blame the head, but **what they blame it for**." |
| 4 Finding | BarCompare | Fourteen of twenty called the model random by nature. | 14/20 llamaron al modelo aleatorio por naturaleza. | The teal bar grows to 14/20. | "Fourteen of twenty against four of twenty." / chart label "calls it random by nature" |
| 4 Finding | BarCompare | Far fewer said it about the forest. | Bastante menos lo dijeron del forest. | The amber bar stops at 4 of 20. Small "p = 0.0018" tag on screen only, not narrated. | "Accuses it of randomness of its own: 14/20, 4/20, 0.0018" |
| 4 Finding | KeyQuote | The forest gets accused of what the system does to it. | Al forest se le acusa de lo que el sistema le hace. | Quote card, first half. | "The forest gets accused of what the system does to it. The model, of what it is." |
| 4 Finding | KeyQuote | The model, of what it is. | Al modelo, de lo que es. | Second half fades in, in teal. | (same) |
| 5 So what | FlowDiagram (callback) | On these runs, patching didn't need a language model. | Aquí, parchear no necesitó un modelo de lenguaje. | The fork diagram comes back. The model head dims and the patch stays on. | "Whatever drives an engineer to smooth an output rather than trace it, **a language model is not a prerequisite.**" |
| 5 So what | FlowDiagram | A closed component was enough. | Bastó con un componente cerrado. | Both heads turn into padlocked black boxes. | "**A closed component is.**" / "One fault, one corpus, two heads." |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card with the URL. | — |

## Notes

- **What changed for the voice:**
  - "260 of 260" is no longer spoken. "Re-running gave the same output, every time" says the same thing, and the badge carries the number.
  - "19 and 19 again" is replaced by "A second round of forty agents matched it." The second pair of bars still shows 19/20.
  - "Only 4/20" is replaced by "Far fewer said it about the forest." The amber bar shows 4 of 20.
  - "19/20" and "14/20" stay spoken, since they carry the finding.
- **Spoken forms for the TTS** (the captions stay as written above):
  - "19/20" is said as "nineteen of twenty".
  - "14/20" is said as "fourteen of twenty".
  - "javieraguilar.ai" is said as "javier aguilar dot A I".
- **Hedges kept:** "On these runs" and "was enough" (past tense) keep the claim from going wider than the article's "one fault, one corpus, two heads". The p-value is only on screen, so the narration doesn't sound stronger than the article.
- **Reading speed:**
  - I estimated every line at 17 characters per second or less. The two closest to the limit are "I swapped the language model…" and "On these runs, patching…", both about 15.5.
  - **Not linted:** I couldn't run `npm run lint` here, so please run it once these lines are in the scene files.
  - **ES lines:** "14/20 llamaron…" is the longest ES line, near 50 characters. Check it first. The "Ambos briefs" line is gone.
- **Length:** the spoken count is about the same as before, since the removed figures were replaced with short phrases. The replication point is kept, so no line needs cutting to reach about 45 s.
- **Left out on purpose:** the "0 of 280 asked for missing data" result. It's a strong result, but it's a second story and wouldn't fit in 45 s.
- **Not saved:** I couldn't write `script.md` in this session, so the table is here for you to approve. Nothing is built yet.
