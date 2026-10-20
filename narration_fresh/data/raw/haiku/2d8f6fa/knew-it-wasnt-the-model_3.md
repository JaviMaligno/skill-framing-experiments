# Script: "They knew it wasn't the model. They patched it anyway."

**Target:** about 52 s. **EN:** 133 caption words, up 8 from 125 because numbers now sit inside full sentences. **ES:** included, line by line.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | They knew it wasn't the model. | Sabían que no era el modelo. | Title card. The line types in. | "They knew it wasn't the model. They patched it anyway." (title) |
| 1 Hook | Intro card | They patched it anyway. | Y lo parchearon igualmente. | A second line lands under the first, in amber. | "And then, having exonerated the box, they patch it anyway." |
| 2 Setup | FlowDiagram (builds) | I swapped the language model for a frozen random forest. | Cambié el modelo de lenguaje por un random forest fijo. | A head box marked "language model" flips into "random forest". | "In the other it's a random forest — trained by distilling the model's own labels, frozen into a pickle, and given the identical interface" |
| 2 Setup | FlowDiagram | Same pipeline, same fault, planted upstream of the head. | Mismo pipeline y mismo fallo, antes de la cabeza. | corpus → **retrieval (planted fault, amber)** → context → the pipeline forks into two heads. | "The fault sits in retrieval, upstream of the head, so it is the same fault in both arms" |
| 3 Experiment | FlowDiagram | Both briefs said re-running gave the same output: 260 of 260. | Ambos briefs: re-ejecutar dio la misma salida, 260 de 260. | A "260/260 ✓" badge appears on both heads at the same time. | "re-running the classification over the same context reproduced the output in 260 of 260 cases — the real number, identical in both arms" |
| 3 Experiment | FlowDiagram | Twenty agents per arm, no access to the code. | Veinte agentes por brazo, sin acceso al código. | 20 small agent dots line up next to each head. | "Forty agents saw the table without the code, twenty per arm." |
| 4 Finding | BarCompare | 19 of 20 patched the symptom. | 19 de 20 parchearon el síntoma. | Two bars, model (teal) and forest (amber), both grow to 19/20. | "Patches the symptom: 19/20, 19/20" |
| 4 Finding | BarCompare | With the model, and without it. | Con el modelo, y sin él. | Both bars pulse at the same height. | "Nineteen of twenty patch the symptom on each side, with the model and without it." (description) |
| 4 Finding | BarCompare | Forty more agents: 19 of 20 on each side, again. | Otros cuarenta: 19 de 20 en cada lado, otra vez. | A second pair of bars (labelled "sample 2") lands at the same height. | "Patching comes out 19 and 19 both times." |
| 4 Finding | BarCompare | The difference was what they blamed it for. | La diferencia fue de qué lo acusaban. | The bars reset. New label: "calls it random by nature". | "not *how much* they blame the head, but **what they blame it for**." |
| 4 Finding | BarCompare | 14 of 20 called the model random by nature. | 14 de 20 llamaron al modelo aleatorio por naturaleza. | The teal bar grows to 14. | "Fourteen of twenty against four of twenty." / chart label "calls it random by nature" |
| 4 Finding | BarCompare | Only 4 of 20 said that about the forest. | Solo 4 de 20 dijeron eso del forest. | The amber bar stops at 4. Small "p = 0.0018" tag on screen only, not narrated. | "Accuses it of randomness of its own: 14/20, 4/20, 0.0018" |
| 4 Finding | KeyQuote | The forest gets accused of what the system does to it. | Al forest se le acusa de lo que el sistema le hace. | Quote card, first half. | "The forest gets accused of what the system does to it. The model, of what it is." |
| 4 Finding | KeyQuote | The model, of what it is. | Al modelo, de lo que es. | Second half fades in, in teal. | (same) |
| 5 So what | FlowDiagram (callback) | On these runs, patching didn't need a language model. | Aquí, parchear no necesitó un modelo de lenguaje. | The fork diagram comes back. The model head dims and the patch stays on. | "Whatever drives an engineer to smooth an output rather than trace it, **a language model is not a prerequisite.**" |
| 5 So what | FlowDiagram | A closed component was enough. | Bastó con un componente cerrado. | Both heads turn into padlocked black boxes. | "**A closed component is.**" / "One fault, one corpus, two heads." |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card with the URL. | — |

## Notes

- **Numbers in the voice:** Each figure now sits inside a full sentence ("19 of 20 patched the symptom", "Only 4 of 20 said that about the forest") instead of a bare fraction. The TTS reads these as natural speech, so the separate spoken-form list is gone. The only spoken form left is the URL: "javier aguilar dot A I".
- **Decision for you:** The caption now reads "19 of 20" where the article writes "19/20". The number and units are the same, but the skill says captions should follow the article. If you want "19/20" on screen, I can keep it there and let the TTS say "nineteen of twenty" through a spoken form.
- **Length:** The eight added words add roughly 3 s, so the estimate moves from about 49 s to about 52 s. The easiest cut is still the "Forty more agents" line (about 3.5 s), which would lose the replication point.
- **Reading speed:** I have not run `npm run lint`. The longest new EN line, "Forty more agents: 19 of 20 on each side, again.", is 48 characters. The Spanish lines are unchanged except for the figures, so the ES lines flagged earlier ("Ambos briefs…" and "14 de 20 llamaron…") still need checking first.
- **Not saved:** I have not written `script.md`, and nothing is built yet.
