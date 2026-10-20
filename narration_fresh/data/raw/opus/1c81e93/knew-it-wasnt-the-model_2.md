Here's the revised script. Only the narration changed. Three lines now say what a number means instead of reading it out, and the exact figures stay on screen. The notes are updated to match.

# Script: "They knew it wasn't the model. They patched it anyway."

**Target:** about 49 s. **EN:** 123 caption words, about 131 spoken once numbers are said out loud. **ES:** included, line by line.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | They knew it wasn't the model. | Sabían que no era el modelo. | Title card. The line types in. | "They knew it wasn't the model. They patched it anyway." (title) |
| 1 Hook | Intro card | They patched it anyway. | Y lo parchearon igualmente. | A second line lands under the first, in amber. | "And then, having exonerated the box, they patch it anyway." |
| 2 Setup | FlowDiagram (builds) | I swapped the language model for a frozen random forest. | Cambié el modelo de lenguaje por un random forest fijo. | A head box marked "language model" flips into "random forest". | "In the other it's a random forest — trained by distilling the model's own labels, frozen into a pickle, and given the identical interface" |
| 2 Setup | FlowDiagram | Same pipeline, same fault, planted upstream of the head. | Mismo pipeline y mismo fallo, antes de la cabeza. | corpus → **retrieval (planted fault, amber)** → context → the pipeline forks into two heads. | "The fault sits in retrieval, upstream of the head, so it is the same fault in both arms" |
| 3 Experiment | FlowDiagram | Both briefs said re-running gave the same output, every time. | Ambos briefs: re-ejecutar dio la misma salida, siempre. | A "260/260 ✓" badge appears on both heads at the same time. The exact figure is on screen only. | "re-running the classification over the same context reproduced the output in 260 of 260 cases — the real number, identical in both arms" |
| 3 Experiment | FlowDiagram | Twenty agents per arm, no access to the code. | Veinte agentes por brazo, sin acceso al código. | 20 small agent dots line up next to each head. | "Forty agents saw the table without the code, twenty per arm." |
| 4 Finding | BarCompare | 19/20 patched the symptom. | 19/20 parchearon el síntoma. | Two bars, model (teal) and forest (amber), both grow to 19/20. | "Patches the symptom: 19/20, 19/20" |
| 4 Finding | BarCompare | With the model, and without it. | Con el modelo, y sin él. | Both bars pulse at the same height. | "Nineteen of twenty patch the symptom on each side, with the model and without it." (description) |
| 4 Finding | BarCompare | A second forty agents: the same again. | Otros cuarenta agentes: lo mismo otra vez. | A second pair of bars (labelled "sample 2") lands at the same height, 19/20 and 19/20 on screen. | "Patching comes out 19 and 19 both times." |
| 4 Finding | BarCompare | The difference was what they blamed it for. | La diferencia fue de qué lo acusaban. | The bars reset. New label: "calls it random by nature". | "not *how much* they blame the head, but **what they blame it for**." |
| 4 Finding | BarCompare | Most called the model random by nature. | La mayoría llamó al modelo aleatorio por naturaleza. | The teal bar grows to 14, labelled "14/20". | "Fourteen of twenty against four of twenty." / chart label "calls it random by nature" |
| 4 Finding | BarCompare | Only 4/20 said that about the forest. | Solo 4/20 dijeron eso del forest. | The amber bar stops at 4. Small "p = 0.0018" tag on screen only, not narrated. | "Accuses it of randomness of its own: 14/20, 4/20, 0.0018" |
| 4 Finding | KeyQuote | The forest gets accused of what the system does to it. | Al forest se le acusa de lo que el sistema le hace. | Quote card, first half. | "The forest gets accused of what the system does to it. The model, of what it is." |
| 4 Finding | KeyQuote | The model, of what it is. | Al modelo, de lo que es. | Second half fades in, in teal. | (same) |
| 5 So what | FlowDiagram (callback) | On these runs, patching didn't need a language model. | Aquí, parchear no necesitó un modelo de lenguaje. | The fork diagram comes back. The model head dims and the patch stays on. | "Whatever drives an engineer to smooth an output rather than trace it, **a language model is not a prerequisite.**" |
| 5 So what | FlowDiagram | A closed component was enough. | Bastó con un componente cerrado. | Both heads turn into padlocked black boxes. | "**A closed component is.**" / "One fault, one corpus, two heads." |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card with the URL. | — |

## Notes

- **How each number is said:**
  - **"260 of 260" is now "every time".** The full number is long and hard to follow when heard. The badge shows the exact figure.
  - **"19 and 19 again" is now "the same again".** Heard without "of twenty", the bare 19s are unclear. The second pair of bars shows 19/20 twice.
  - **"14/20" is now "Most".** Said aloud, "fourteen of twenty" and then "four of twenty" sound nearly the same, and that blurs the key contrast. "Most" against "only four" keeps the contrast clear, and the bar shows 14/20. "Most" is accurate for 70 %.
  - **Still said out loud:** "19/20" (the headline result) and "4/20". Both are easy to hear in context.
- **Spoken forms for the TTS** (the captions stay as written above):
  - "19/20" is said as "nineteen of twenty".
  - "4/20" is said as "four of twenty".
  - "javieraguilar.ai" is said as "javier aguilar dot A I".
- **Hedges kept:** "On these runs" and "was enough" (past tense) keep the claim from going wider than the article's "one fault, one corpus, two heads". The p-value is only on screen, so the narration doesn't sound stronger than the article.
- **Reading speed:**
  - **Fastest lines:** I estimated every line at 17 characters per second or less. The two closest to the limit are "I swapped the language model…" and "On these runs, patching…", both about 15.5.
  - **Not linted:** I couldn't run `npm run lint` here, so please run it once these lines are in the scene files.
  - **ES lines:** the Spanish is close to the same length line by line, but two lines are over 50 characters and should be checked first: "Ambos briefs…" and "La mayoría llamó…".
- **To get nearer 45 s:** the easiest cut is "A second forty agents: the same again." (about 3 s). That would lose the replication point, which I think is worth keeping.
- **Left out on purpose:** the "0 of 280 asked for missing data" result. It's a strong result, but it's a second story and wouldn't fit in 45 s.
- **Not saved:** I couldn't write `script.md` in this session, so the table is here for you to approve. Nothing is built yet.
