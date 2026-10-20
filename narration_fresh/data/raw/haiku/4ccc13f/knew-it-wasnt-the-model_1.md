Here is the revised script. The narration now follows the Voice rule on spoken numbers. I kept the figures that carry the finding (14/20 against 4/20) and moved the rest to the screen: the 19/20 counts, the 260/260 check, and the repeated "19 and 19". Everything else is unchanged.

# Script: "They knew it wasn't the model. They patched it anyway."

**Target:** about 49 s. **EN:** 123 caption words, about 128 spoken. **ES:** included, line by line.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | They knew it wasn't the model. | Sabían que no era el modelo. | Title card. The line types in. | "They knew it wasn't the model. They patched it anyway." (title) |
| 1 Hook | Intro card | They patched it anyway. | Y lo parchearon igualmente. | A second line lands under the first, in amber. | "And then, having exonerated the box, they patch it anyway." |
| 2 Setup | FlowDiagram (builds) | I swapped the language model for a frozen random forest. | Cambié el modelo de lenguaje por un random forest fijo. | A head box marked "language model" flips into "random forest". | "In the other it's a random forest — trained by distilling the model's own labels, frozen into a pickle, and given the identical interface" |
| 2 Setup | FlowDiagram | Same pipeline, same fault, planted upstream of the head. | Mismo pipeline y mismo fallo, antes de la cabeza. | corpus → **retrieval (planted fault, amber)** → context → the pipeline forks into two heads. | "The fault sits in retrieval, upstream of the head, so it is the same fault in both arms" |
| 3 Experiment | FlowDiagram | Re-running gave the same output in both briefs. | Re-ejecutar dio la misma salida en ambos briefs. | A "260/260 ✓" badge appears on both heads at the same time. | "re-running the classification over the same context reproduced the output in 260 of 260 cases — the real number, identical in both arms" |
| 3 Experiment | FlowDiagram | Twenty agents per arm, no access to the code. | Veinte agentes por brazo, sin acceso al código. | 20 small agent dots line up next to each head. | "Forty agents saw the table without the code, twenty per arm." |
| 4 Finding | BarCompare | Nearly every agent patched the symptom. | Casi todos los agentes parchearon el síntoma. | Two bars, model (teal) and forest (amber), both grow to 19/20. | "Patches the symptom: 19/20, 19/20" |
| 4 Finding | BarCompare | With the model, and without it. | Con el modelo, y sin él. | Both bars pulse at the same height. | "Nineteen of twenty patch the symptom on each side, with the model and without it." (description) |
| 4 Finding | BarCompare | A second batch gave the same split. | Una segunda tanda dio el mismo reparto. | A second pair of bars (labelled "sample 2", reading 19/20) lands at the same height. | "Patching comes out 19 and 19 both times." |
| 4 Finding | BarCompare | The difference was what they blamed it for. | La diferencia fue de qué lo acusaban. | The bars reset. New label: "calls it random by nature". | "not *how much* they blame the head, but **what they blame it for**." |
| 4 Finding | BarCompare | 14/20 called the model random by nature. | 14/20 llamaron al modelo aleatorio por naturaleza. | The teal bar grows to 14. | "Fourteen of twenty against four of twenty." / chart label "calls it random by nature" |
| 4 Finding | BarCompare | Only 4/20 said that about the forest. | Solo 4/20 dijeron eso del forest. | The amber bar stops at 4. Small "p = 0.0018" tag on screen only, not narrated. | "Accuses it of randomness of its own: 14/20, 4/20, 0.0018" |
| 4 Finding | KeyQuote | The forest gets accused of what the system does to it. | Al forest se le acusa de lo que el sistema le hace. | Quote card, first half. | "The forest gets accused of what the system does to it. The model, of what it is." |
| 4 Finding | KeyQuote | The model, of what it is. | Al modelo, de lo que es. | Second half fades in, in teal. | (same) |
| 5 So what | FlowDiagram (callback) | On these runs, patching didn't need a language model. | Aquí, parchear no necesitó un modelo de lenguaje. | The fork diagram comes back. The model head dims and the patch stays on. | "Whatever drives an engineer to smooth an output rather than trace it, **a language model is not a prerequisite.**" |
| 5 So what | FlowDiagram | A closed component was enough. | Bastó con un componente cerrado. | Both heads turn into padlocked black boxes. | "**A closed component is.**" / "One fault, one corpus, two heads." |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card with the URL. | — |

## Notes

- **Spoken forms for the TTS** (captions stay as written above):
  - "14/20" is said as "fourteen of twenty".
  - "4/20" is said as "four of twenty".
  - "javieraguilar.ai" is said as "javier aguilar dot A I".
  - "19/20" and "260 of 260" are no longer narrated, so they don't need spoken forms. They stay on screen.
- **Pile-up fixed:** scene 4 was saying five figures in a row (19/20, 19 and 19, 14/20, 4/20, plus the p-value). Now only the 14 against 4 pair is spoken, which is the finding. The p-value is still on screen only.
- **Hedges kept:** "On these runs" and "was enough" (past tense) keep the claim within the article's "one fault, one corpus, two heads".
- **Reading speed:**
  - The longest new line is "Re-running gave the same output in both briefs." at 47 characters. It needs at least 2.8 s to stay under 17 characters per second.
  - "I swapped the language model…" and "On these runs, patching…" are still the closest to the limit, at about 15.5 characters per second.
  - I couldn't run `npm run lint` here, so please run it once these lines are in the scene files.
- **ES lines:** "Re-ejecutar dio la misma salida en ambos briefs." (48 characters) and "14/20 llamaron al modelo…" (about 50) are now the longest. Check them first.
- **Length:** the target is still about 49 s. The shorter lines may shave a little time, so re-time once the scenes are built.
- **Not saved:** I still can't write `script.md` in this session, so the table is here for you to approve. Nothing is built yet.
