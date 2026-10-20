I changed five narration lines and kept everything else as it was. The current skill no longer says every number aloud. It keeps a number when it's easy to hear and adds something. When a value is awkward to hear or comes in a run of numbers, the narration says what it means and the figure stays on screen. I also updated the notes those changes affect.

**What changed:**
- **"260 of 260" → "every re-run".** Said aloud as "two hundred and sixty of two hundred and sixty", it was the hardest number to listen to. The narration now says what it means, and the 260/260 badge stays on screen.
- **"19/20" is still spoken.** It's the headline finding and easy to hear as "nineteen of twenty".
- **"19 and 19 again" → "the same again".** It was the second of four numbers in a row. The figures stay on the bars.
- **"14/20" and "4/20" → "Most" and "only a few".** They came straight after the 19s. The contrast now comes through in words, and the bars show 14/20 and 4/20.
- **Visuals:** the visual text for the 260/260 badge and three bars (sample 2, 14 and 4) now says the figure shows, so each number left out of the narration stays readable on screen.

# Script: "They knew it wasn't the model. They patched it anyway."

**Target:** about 46 s. **EN:** 123 caption words, about 125 spoken. **ES:** included, line by line.

| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | They knew it wasn't the model. | Sabían que no era el modelo. | Title card. The line types in. | "They knew it wasn't the model. They patched it anyway." (title) |
| 1 Hook | Intro card | They patched it anyway. | Y lo parchearon igualmente. | A second line lands under the first, in amber. | "And then, having exonerated the box, they patch it anyway." |
| 2 Setup | FlowDiagram (builds) | I swapped the language model for a frozen random forest. | Cambié el modelo de lenguaje por un random forest fijo. | A head box marked "language model" flips into "random forest". | "In the other it's a random forest — trained by distilling the model's own labels, frozen into a pickle, and given the identical interface" |
| 2 Setup | FlowDiagram | Same pipeline, same fault, planted upstream of the head. | Mismo pipeline y mismo fallo, antes de la cabeza. | corpus → **retrieval (planted fault, amber)** → context → the pipeline forks into two heads. | "The fault sits in retrieval, upstream of the head, so it is the same fault in both arms" |
| 3 Experiment | FlowDiagram | Both briefs: every re-run gave the same output. | Ambos briefs: cada re-ejecución dio la misma salida. | A "260/260 ✓" badge appears on both heads at the same time and stays readable for the whole line. | "re-running the classification over the same context reproduced the output in 260 of 260 cases — the real number, identical in both arms" |
| 3 Experiment | FlowDiagram | Twenty agents per arm, no access to the code. | Veinte agentes por brazo, sin acceso al código. | 20 small agent dots line up next to each head. | "Forty agents saw the table without the code, twenty per arm." |
| 4 Finding | BarCompare | 19/20 patched the symptom. | 19/20 parchearon el síntoma. | Two bars, model (teal) and forest (amber), both grow to 19/20. | "Patches the symptom: 19/20, 19/20" |
| 4 Finding | BarCompare | With the model, and without it. | Con el modelo, y sin él. | Both bars pulse at the same height. | "Nineteen of twenty patch the symptom on each side, with the model and without it." (description) |
| 4 Finding | BarCompare | A second forty agents: the same again. | Otros cuarenta agentes: lo mismo otra vez. | A second pair of bars (labelled "sample 2") lands at the same height, each showing "19/20". | "Patching comes out 19 and 19 both times." |
| 4 Finding | BarCompare | The difference was what they blamed it for. | La diferencia fue de qué lo acusaban. | The bars reset. New label: "calls it random by nature". | "not *how much* they blame the head, but **what they blame it for**." |
| 4 Finding | BarCompare | Most of them called the model random by nature. | La mayoría llamó al modelo aleatorio por naturaleza. | The teal bar grows to 14, with a "14/20" figure on it. | "Fourteen of twenty against four of twenty." / chart label "calls it random by nature" |
| 4 Finding | BarCompare | For the forest, only a few did. | Del forest, solo unos pocos. | The amber bar stops at 4, with a "4/20" figure on it. Small "p = 0.0018" tag on screen only, not narrated. | "Accuses it of randomness of its own: 14/20, 4/20, 0.0018" |
| 4 Finding | KeyQuote | The forest gets accused of what the system does to it. | Al forest se le acusa de lo que el sistema le hace. | Quote card, first half. | "The forest gets accused of what the system does to it. The model, of what it is." |
| 4 Finding | KeyQuote | The model, of what it is. | Al modelo, de lo que es. | Second half fades in, in teal. | (same) |
| 5 So what | FlowDiagram (callback) | On these runs, patching didn't need a language model. | Aquí, parchear no necesitó un modelo de lenguaje. | The fork diagram comes back. The model head dims and the patch stays on. | "Whatever drives an engineer to smooth an output rather than trace it, **a language model is not a prerequisite.**" |
| 5 So what | FlowDiagram | A closed component was enough. | Bastó con un componente cerrado. | Both heads turn into padlocked black boxes. | "**A closed component is.**" / "One fault, one corpus, two heads." |
| 6 Outro | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card with the URL. | — |

## Notes

- **Spoken forms for the TTS** (the captions stay as written above):
  - "19/20" is said as "nineteen of twenty" (ES: "diecinueve de veinte").
  - "javieraguilar.ai" is said as "javier aguilar dot A I".
- **Numbers on screen only:** the narration describes these in words instead of reading them out: 260/260 ("every re-run"), the second pair of 19/20 ("the same again"), 14/20 ("Most") and 4/20 ("only a few"). The visuals show each figure as the article writes it.
- **Hedges kept:** "On these runs" and "was enough" (past tense) keep the claim from going wider than the article's "one fault, one corpus, two heads". "Most" and "only a few" say no more than 14/20 and 4/20 do. The p-value is only on screen, so the narration doesn't sound stronger than the article.
- **Reading speed:**
  - **Fastest lines:** I estimated every line at 17 characters per second or less. Now that "Both briefs…" isn't stretched out by a long spoken number, it's about 16. "I swapped the language model…" and "On these runs, patching…" are both about 15.5.
  - **Not linted:** I couldn't run `npm run lint` here, so please run it once these lines are in the scene files. Check "Both briefs…" first.
  - **ES lines:** the Spanish is close to the same length line by line. The one to check first is "La mayoría llamó…" (about 52 characters).
- **To get nearer 45 s:** the script is now about 46 s, so no cut is needed. If you still want one, the easiest is "A second forty agents: the same again." (about 2.5 s). That would lose the replication point, which I think is worth keeping.
- **Left out on purpose:** the "0 of 280 asked for missing data" result. It's a strong result, but it's a second story and wouldn't fit in 45 s.
- **Not saved:** I couldn't write `script.md` in this session, so the table is here for you to approve. Nothing is built yet.
