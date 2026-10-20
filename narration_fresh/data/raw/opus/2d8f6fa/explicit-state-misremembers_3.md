I changed one line. The skill now says to speak numbers naturally as part of a sentence, and to avoid reading a table aloud. Scene 6 was the only line that broke that: it ended on a bare "0.999" after a colon, with no comparison. I split it into two lines. The second line says the number as a before-and-after: Haiku went from 0.958 with state alone to 0.999 with the transcript kept. Every other row and note is unchanged except where the extra line affects the count, the length and the spoken forms.

# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 54 s with 118 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second, and `npm run lint` will check them against the real audio.

```markdown
| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini-3-Flash, | Lo repetí con el modelo del paper, Gemini-3-Flash, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku 4.5. | y con Claude Haiku 4.5. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed: 75 episodes, up to 200 steps. | En Gemini no falló nunca: 75 episodios, hasta 200 pasos. | Counter runs 0 → 75 episodes, with a steady "0 failures" label under it. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off about 25 failures. | En un caso, esa copia errónea desató unos 25 fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in 17 of 24 runs. | Haiku escribió algún parche erróneo en 17 de 24 ejecuciones. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed it. | En Haiku, guardar también la transcripción lo absorbió. | Haiku at T=200: bars build for ReAct 0.974, Stateful 0.999, SKILL.state 0.958. | "Keeping the transcript absorbs it" |
| 6 So what | `BarCompare` (cont.) | It took Haiku from 0.958 with state alone to 0.999. | Llevó a Haiku de 0,958 solo con estado a 0,999. | An arrow runs from the SKILL.state bar (0.958) to the Stateful bar (0.999), which is highlighted. ReAct stays dimmed. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 118 caption words (about 140 spoken, because numbers and names are read out in full). **Estimated length:** about 54 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "0.958" is said as "zero point nine five eight" (ES: "cero coma nueve cinco ocho").
- "0.999" is said as "zero point nine nine nine" (ES: "cero coma nueve nueve nueve").
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## Notes for review
- **What changed in scene 6:** the old line "…absorbed it: 0.999." read a single table value aloud. The finding now has its own line, which says the number as the change from state alone to state plus transcript. That adds about 4 s, which the skill allows ("clarity beats brevity"). The new line is 50 characters and has about 18 spoken words, so it stays well under 17 characters per second. The line says "took Haiku from… to…" rather than naming the metric, because the script doesn't say what the table's numbers measure. If the article names it (for example "success rate"), it's worth adding.
- **The hook line reads fast.** It is 47 characters, and the long words push it close to 17 characters per second. Leaving a short beat between the two sentences should keep it under the limit. If lint still flags it, the fix is to shorten the text, not speed up the voice.
- **The ES decimals are a guess.** I used "0,958" and "0,999" on the assumption that the Spanish article uses a decimal comma. If that article writes 0.958 and 0.999, match it.
- **What I left out to keep near 45 s:** the 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost, and the "repeat every cell" point. I also cut a Gemini line ("never made that error in 75") because it repeats scene 3; its number now appears only in the scene 5 tiles. If you want any of these back, the retraction result fits best as a `BarCompare` scene after scene 5, at about +5 s.
- **Hedges I kept:** "in one case" for the seed-2 cascade, and "on Haiku" for the transcript result.
- **The visual that shows the mechanism** is the `FlowDiagram` in scene 4, which follows the article's step-132 figure.

I couldn't write files here, so `script.md` isn't saved yet; the table is ready to paste. Nothing gets built until you approve the script.
