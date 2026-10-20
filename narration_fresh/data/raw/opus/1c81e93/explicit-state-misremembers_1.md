I revised the narration so numbers follow the new Voice rule. Numbers that are easy to hear are still spoken. The awkward ones (17 of 24, 0.999, and the two numbers in a row in scene 3) are now said in words, and the exact figure stays on screen. Everything else is unchanged except one visual label in scene 3, explained in the notes.

# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 46 s with 105 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second, and `npm run lint` will check them against the real audio.

```markdown
| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini-3-Flash, | Lo repetí con el modelo del paper, Gemini-3-Flash, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku 4.5. | y con Claude Haiku 4.5. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed once in 75 long episodes. | En Gemini no falló ni una vez en 75 episodios largos. | Counter runs 0 → 75 episodes, with a steady "0 failures" label and an "up to 200 steps each" label under it. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off about 25 failures. | En un caso, esa copia errónea desató unos 25 fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in most of its runs. | Haiku escribió un parche erróneo en la mayoría de ejecuciones. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, also keeping the transcript absorbed those errors. | En Haiku, guardar además la transcripción los absorbió. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 105 caption words (about 115 spoken, because some names are read out in full). **Estimated length:** about 46 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## How each number is now handled
- **Scene 3, "75 episodes, up to 200 steps":** this was two numbers in a row. The line now says only "75 long episodes", and "up to 200 steps" moves to a label on the Counter. That label is the one visual change, made so the figure stays on screen.
- **Scene 4, "about 25 failures":** still spoken. It's round and easy to hear.
- **Scene 5, "17 of 24 runs":** an awkward fraction to hear, so it's spoken as "most of its runs". The exact 17/24 is already on the tile.
- **Scene 6, "0.999":** "zero point nine nine nine" is long and one of three values on screen, so it's no longer spoken. The line now says what it means ("absorbed those errors"), and the highlighted bar shows 0.999. I also changed "it" to "those errors" so the line is clear when heard on its own.
- **Model names (Gemini-3-Flash, Haiku 4.5):** still spoken. They're names, not findings.

## Notes for review
- **The hook line reads fast.** It is 47 characters, and the long words push it close to 17 characters per second. Leaving a short beat between the two sentences should keep it under the limit. If lint still flags it, the fix is to shorten the text, not speed up the voice.
- **The ES decimal now only affects the bar labels.** 0.999 isn't spoken any more. If the ES cut gets its own labels, use whatever the Spanish article writes ("0,999" or "0.999").
- **What I left out to keep near 45 s:** the 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost, and the "repeat every cell" point. I also cut a Gemini line ("never made that error in 75") because it repeats scene 3; its number now appears only in the scene 5 tiles. If you want any of these back, the retraction result fits best as a `BarCompare` scene after scene 5, at about +5 s.
- **Hedges I kept:** "in one case" for the seed-2 cascade, and "on Haiku" for the transcript result. "Most of its runs" is no stronger than 17/24, and the tile still notes T=200.
- **The visual that shows the mechanism** is the `FlowDiagram` in scene 4, which follows the article's step-132 figure.

`script.md` still isn't saved to disk; the table above is ready to paste. Nothing gets built until you approve the script.
