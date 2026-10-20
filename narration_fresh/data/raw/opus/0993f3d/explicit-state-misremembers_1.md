# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 47 s with 104 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second. `npm run lint` will check them against the real audio.

```markdown
| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini, | Lo repetí con el modelo del paper, Gemini, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku. | y con Claude Haiku. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed once in 75 episodes. | En Gemini no falló ni una vez en 75 episodios. | Counter runs 0 → 75 episodes, with a steady "0 failures" label under it and a small "up to 200 steps" tag. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off about 25 failures. | En un caso, esa copia errónea desató unos 25 fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in most of its runs. | En la mayoría de ejecuciones, Haiku escribió algún parche mal. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed the errors. | En Haiku, guardar también la transcripción absorbió los errores. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 104 caption words, about 110 when spoken. **Estimated length:** about 47 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## What changed for the number rule
Only the narration changed. Now each spoken line carries at most one figure, and every figure is round.
- **Scene 2:** I took the version numbers out of the voice ("Gemini-3-Flash" became "Gemini", "Haiku 4.5" became "Haiku"). The chips still show the full model names on screen.
- **Scene 3:** Only "75 episodes" is spoken now. "Up to 200 steps" moved into a small tag on the Counter. That tag is the only change to a visual.
- **Scene 5:** "17 of 24" became "most of its runs" (17/24 is 71 %, and the line keeps the "at least one" hedge). The exact 17/24 is still on the tile. This is a judgment call: if you'd rather the finding's number be spoken, put "in 17 of 24 runs" back.
- **Scene 6:** I dropped "0.999" from the voice. The bars show it, and the line now ends with "absorbed the errors". That still holds to the article's "keeping the transcript absorbs it" and stays limited to Haiku.
- The only figures still spoken are "75" (scene 3) and "about 25" (scene 4).

## Notes for review
- **The hook line reads fast.** It is 47 characters, and the long words push it close to 17 characters per second. A short beat between the two sentences should keep it under the limit. If lint still flags it, shorten the text instead of speeding up the voice.
- **The ES decimals are a guess.** No decimals are spoken anymore, but the scene 6 bar labels in the ES cut need the Spanish article's format. I assumed it uses a decimal comma (0,999). If it writes 0.999, match it.
- **What I left out to stay near 45 s:** the 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost and the "repeat every cell" point. I also cut a Gemini line ("never made that error in 75") because it repeats scene 3, so that number now appears only on the scene 5 tiles. If you want any of these back, the retraction result fits best as a `BarCompare` scene after scene 5, adding about 5 s. Put its numbers on screen and keep the voice qualitative.
- **Hedges I kept:** "in one case" for the seed-2 cascade, "on Haiku" for the transcript result, and "at least one" for the wrong patches.
- **The visual that shows the mechanism** is the `FlowDiagram` in scene 4, which follows the article's step-132 figure.

I couldn't write files here, so `script.md` isn't saved yet. The table is ready to paste, and nothing gets built until you approve the script.
