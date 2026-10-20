I revised the narration to follow the new Voice rule on spoken numbers. The voice now says only one figure, "17 of 24", which is the finding the video rests on. The other figures, model versions and unround decimals now appear only in the visuals. Visuals, structure and source quotes are unchanged.

# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 45 s with 104 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second, and `npm run lint` will check them against the real audio.

```markdown
| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini Flash, | Lo repetí con el modelo del paper, Gemini Flash, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku. | y con Claude Haiku. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed. Not once. | En Gemini no falló nunca. Ni una vez. | Counter runs 0 → 75 episodes, with a steady "0 failures" label under it. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off a cascade of failures. | En un caso, esa copia errónea desató una cascada de fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in 17 of 24 runs. | Haiku escribió algún parche erróneo en 17 de 24 ejecuciones. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed the errors. | En Haiku, conservar la transcripción absorbió los errores. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 104 caption words (about 110 spoken). **Estimated length:** about 45 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## Notes for review
- **What changed in the voice:**
  - **Scene 2:** the voice now says "Gemini Flash" and "Claude Haiku". The full names with version numbers stay on the chips.
  - **Scene 3:** the voice no longer says "75 episodes, up to 200 steps". It now says "never failed. Not once.", and the 75 appears on the counter.
  - **Scene 4:** "about 25 failures" is now "a cascade of failures". The ~25 stays in the counter.
  - **Scene 6:** the voice no longer says "0.999". The bars show it.
  - **Spoken forms:** the Gemini, Haiku 4.5 and 0.999 entries are gone because those lines no longer say them.
- **The ES decimal note is gone.** No line says a decimal any more, so the comma question doesn't come up.
- **The hook line reads fast.** It is 47 characters, and the long words push it close to 17 characters per second. Leaving a short beat between the two sentences should keep it under the limit. If lint still flags it, shorten the text rather than speed up the voice.
- **What I left out to keep near 45 s:** the 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost, and the "repeat every cell" point. If you want the retraction result back, it fits best as a `BarCompare` scene after scene 5. Under the new rule, its narration would leave both counts on screen.
- **Hedges I kept:** "in one case" for the seed-2 cascade, and "on Haiku" for the transcript result.
- **The visual that shows the mechanism** is the `FlowDiagram` in scene 4, which follows the article's step-132 figure.

I couldn't save `script.md` from here, so the table is ready to paste. Nothing gets built until you approve the script.
