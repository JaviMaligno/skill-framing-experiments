# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

The script runs about 50 s with about 109 caption words. Every line fits in two caption rows of about 32 characters (64 maximum). Reading speeds are estimates at about 2.5 spoken words per second, and `npm run lint` will check them against the real audio.

```markdown
| Scene | Component | EN line | ES line | Visual | Source sentence |
|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini-3-Flash, | Lo repetí con el modelo del paper, Gemini-3-Flash, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku 4.5. | y con Claude Haiku 4.5. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed in 75 episodes of up to 200 steps. | En Gemini no falló nunca en 75 episodios de hasta 200 pasos. | Counter runs 0 → 75 episodes, with a steady "0 failures" label under it. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off about 25 failures. | En un caso, esa copia errónea desató unos 25 fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in 17 of 24 runs. | Haiku escribió algún parche erróneo en 17 de 24 ejecuciones. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, keeping the transcript absorbed it, scoring 0.999. | En Haiku, guardar la transcripción lo absorbió, con 0,999. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** about 109 caption words, unchanged by my recount. **Estimated length:** about 50 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "75" is said as "seventy-five" (ES: "setenta y cinco").
- "200" is said as "two hundred" (ES: "doscientos").
- "25" is said as "twenty-five" (ES: "veinticinco").
- "17 of 24" is said as "seventeen of twenty-four" (ES: "diecisiete de veinticuatro").
- "0.999" is said as "zero point nine nine nine" (ES: "cero coma nueve nueve nueve").
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## What changed
- **Scene 3:** "75 episodes, up to 200 steps" was a bare list after a colon. It is now a sentence that uses the article's wording: "never failed in 75 episodes of up to 200 steps." The ES line follows the same pattern.
- **Scene 6:** "…absorbed it: 0.999." was a number dropped after a colon. It is now "…absorbed it, scoring 0.999." The ES line follows the same pattern. I also dropped "too", which the article does not support.
- **Scenes 4 and 5:** No change. Their numbers already sit inside a sentence.
- **Narration never reads the visual's values.** The ReAct and SKILL.state scores in scene 6 and the Gemini tile in scene 5 stay on screen only.

## Open item
The Voice section asks the closing to say plainly what the result means (good, bad, or "only sometimes"). Scene 7 states the lesson but not the verdict. The article's result supports something like "On Haiku it misremembered; on Gemini it never did." I left it out because you asked me to change only what the skill requires for numbers. Tell me if you want it added as a line before the scene 7 closing, and I will adjust the length.
