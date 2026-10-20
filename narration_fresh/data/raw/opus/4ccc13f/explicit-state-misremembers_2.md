I changed three narration lines and left the rest as it was. The new skill says to keep saying the number that carries the point and to put the others on screen when several come in a row. These lines had a run of figures: 75 and 200, then 25, then 17 of 24, then 0.999. Saying "25" right before "24" also made them easy to mix up.

- **Scene 3:** the narration now says only "75 episodes". "Up to 200 steps" moves to a label on screen.
- **Scene 4 (second line):** the narration says "a cascade of failures". The "~25 failures follow" counter already shows the number.
- **Scene 6:** the narration no longer says "0.999". The bar chart already shows it.
- **Scene 5 is unchanged.** "17 of 24" is the main finding, so the narration still says it.

The only visual change is the "up to 200 steps" label in scene 3, because that number still needs to appear somewhere. The 0.999 spoken form is removed, and the word count, length and ES decimal note are updated to match.

# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 47 s with 108 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second, and `npm run lint` will check them against the real audio.

```markdown
| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini-3-Flash, | Lo repetí con el modelo del paper, Gemini-3-Flash, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku 4.5. | y con Claude Haiku 4.5. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed once in 75 episodes. | En Gemini no falló ni una vez en 75 episodios. | Counter runs 0 → 75 episodes, with a steady "0 failures" label and an "up to 200 steps" label under it. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off a cascade of failures. | En un caso, esa copia errónea desató una cascada de fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in 17 of 24 runs. | Haiku escribió algún parche erróneo en 17 de 24 ejecuciones. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed the error. | En Haiku, guardar también la transcripción absorbió el error. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 108 caption words (about 118 spoken, because numbers and names are read out in full). **Estimated length:** about 47 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## Notes for review
- **The hook line reads fast.** It is 47 characters, and the long words push it close to 17 characters per second. Leaving a short beat between the two sentences should keep it under the limit. If lint still flags it, the fix is to shorten the text, not speed up the voice.
- **The ES decimal is a guess.** The narration no longer says 0.999, but the scene 6 bars still show it. In the ES version I'd write those labels with a decimal comma (0,999), assuming the Spanish article does. If that article writes 0.999, match it.
- **What I left out to keep near 45 s:** the 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost, and the "repeat every cell" point. I also cut a Gemini line ("never made that error in 75") because it repeats scene 3; its number now appears only in the scene 5 tiles. If you want any of these back, the retraction result fits best as a `BarCompare` scene after scene 5, at about +5 s.
- **Hedges I kept:** "in one case" for the seed-2 cascade, and "on Haiku" for the transcript result.
- **The visual that shows the mechanism** is the `FlowDiagram` in scene 4, which follows the article's step-132 figure.

I couldn't write files here, so `script.md` still isn't saved; the table is ready to paste. Nothing gets built until you approve the script.
