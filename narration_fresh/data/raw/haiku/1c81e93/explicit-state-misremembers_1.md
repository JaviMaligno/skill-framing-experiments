# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 50 s with 109 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second, and `npm run lint` will check them against the real audio.

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
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed it: 0.999. | En Haiku, guardar también la transcripción lo absorbió: 0,999. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 109 caption words (about 126 spoken). **Estimated length:** about 50 s.

## Spoken forms

Captions stay as written. These are the narration forms the TTS should use.

**Numbers, case by case:**
- Scene 3 (EN): "seventy-five episodes, up to two hundred steps"
  (ES): "setenta y cinco episodios, hasta doscientos pasos"
- Scene 4 (EN): "about twenty-five failures"
  (ES): "unos veinticinco fallos"
- Scene 5 (EN): "seventeen of twenty-four runs"
  (ES): "diecisiete de veinticuatro ejecuciones"
- Scene 6 (EN): "On Haiku, keeping the transcript too absorbed it: a near-perfect score."
  (ES): "En Haiku, guardar también la transcripción lo absorbió: una puntuación casi perfecta."
  The figure 0.999 (0,999) stays in the caption and on the Stateful tile. It is unround and hard to hear, so the narration gives its meaning in words.

**Names and identifiers:**
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## Notes for review
- **Scene 6 wording:** "a near-perfect score" describes 0.999 without adding a claim. If you prefer the article's own terms, I can swap in its phrasing.
- **The hook line reads fast.** It is 47 characters, and the long words push it close to 17 characters per second. A short beat between the two sentences should keep it under the limit. If lint still flags it, shorten the text rather than speed up the voice.
- **The ES decimal is a guess.** I used "0,999" on the assumption that the Spanish article uses a decimal comma. If it writes 0.999, match that in the caption.
- **Left out to keep near 45 s:** the 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost, and the "repeat every cell" point. The retraction result fits best as a `BarCompare` scene after scene 5, at about +5 s.
- **Hedges kept:** "in one case" for the seed-2 cascade, and "on Haiku" for the transcript result.
- **Mechanism visual:** the `FlowDiagram` in scene 4 follows the article's step-132 figure.

Nothing is saved to a file yet. The table is ready to paste into `script.md`, and nothing gets built until you approve the script.
