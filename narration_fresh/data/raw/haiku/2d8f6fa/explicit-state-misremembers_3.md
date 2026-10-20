Here is the revised script. The captions are unchanged. Numbers that sat alone or read like table cells are now spoken inside full sentences, and the spoken forms are updated to match.

# Explainer script: "Explicit State Doesn't Forget. It Misremembers."

```markdown
| Scene | Component | EN caption | EN spoken | ES line | Visual | Source sentence |
|---|---|---|---|---|---|---|
| 1 Hook | Intro card | Explicit state doesn't forget. It misremembers. | Explicit state doesn't forget. It misremembers. | El estado explícito no olvida. Recuerda mal. | Title card. "Misremembers" lands on the second beat. | Title: "Explicit State Doesn't Forget. It Misremembers." |
| 2 Setup | `FlowDiagram` | SKILL.state agents keep a state block, not the transcript. | Skill dot state agents keep a state block, not the transcript. | SKILL.state guarda un bloque de estado, no la transcripción. | Two lanes. Steps flow into a growing transcript scroll (ReAct) and into one compact state block (SKILL.state). | "ReAct (full transcript)… SKILL.state (state block only)" |
| 2 Setup | `FlowDiagram` | I reran it on the paper's own model, Gemini-3-Flash, | I reran it on the paper's own model, Gemini three Flash, | Lo repetí con el modelo del paper, Gemini-3-Flash, | Model chip "Gemini-3-Flash" drops onto the diagram. | "So this half runs on theirs — gemini-3-flash-preview through Vertex" |
| 2 Setup | `FlowDiagram` | and on Claude Haiku 4.5. | and on Claude Haiku four point five. | y con Claude Haiku 4.5. | Second chip "Claude Haiku 4.5" appears beside it. | "plus Claude Haiku 4.5 under the same environment and output cap" |
| 3 Finding A | `Counter` | On Gemini, it never failed: 75 episodes, up to 200 steps. | On Gemini, it never failed once. Across seventy-five episodes, with runs up to two hundred steps long. | En Gemini no falló nunca: 75 episodios, hasta 200 pasos. | Counter runs 0 → 75 episodes, with a steady "0 failures" label under it. | "SKILL.state does not fail once in 75 episodes of up to 200 steps" |
| 4 Mechanism | `FlowDiagram` (broken link) | On Haiku, it broke differently: right action, wrong state patch. | On Haiku, it broke differently: right action, wrong state patch. | En Haiku falló distinto: acción bien, estado mal escrito. | "Move 7 → 3 ✓" flows to a state patch "shelf 3: SKU-J" ✗ (copied from shelf 6, while reality is SKU-K). That link turns amber. | "a Move executed correctly with a state patch written wrong" |
| 4 Mechanism | `FlowDiagram` (cont.) | In one case, that wrong copy set off about 25 failures. | In one case, that wrong copy set off about twenty-five failures. | En un caso, esa copia errónea desató unos 25 fallos. | Continues: "Ship shelf 3 ✗", then "ACTION REJECTED", then a "~25 failures follow" counter ticks up. | "in 6 of the 8 runs of seed 2 the corruption happens at exactly that step, and from there the agent cascades through about 25 failures" |
| 5 Finding B | `StatGrid` | Haiku wrote at least one wrong patch in 17 of 24 runs. | Haiku wrote at least one wrong patch in seventeen of twenty-four runs. | Haiku escribió algún parche erróneo en 17 de 24 ejecuciones. | Two tiles: "Haiku 4.5: 17/24 runs with a wrong patch (T=200)" and "Gemini: 0/75". | "Gemini never made this error in 75 episodes; Haiku wrote at least one wrong patch in 17 of 24 at T=200." |
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed it: 0.999. | On Haiku, keeping the transcript too absorbed the error, scoring zero point nine nine nine. | En Haiku, guardar también la transcripción lo absorbió: 0,999. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | More at javier aguilar dot A I | Más en javieraguilar.ai | Outro card | — |
```

**EN word count:** 109 caption words. The spoken EN is about 135 words, which at about 2.5 words per second is about 54 s, under the 60 s limit. **Estimated length:** about 54 s.

## Spoken forms

- Numbers are spoken as words inside the sentence: "seventy-five episodes", "two hundred steps", "twenty-five failures", "seventeen of twenty-four runs".
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "0.999" is said as "zero point nine nine nine" inside a sentence (ES: "cero coma nueve nueve nueve").
- "javieraguilar.ai" is said as "javier aguilar dot A I".
- ES numbers spoken as words: 75 → "setenta y cinco", 200 → "doscientos", 25 → "veinticinco", 17 de 24 → "diecisiete de veinticuatro".

## Notes for review

- **Closing verdict (not changed):** The updated skill says the closing must state plainly what the result means: good, bad, or "only sometimes." Scene 7 gives the "so what" but never says the verdict in plain terms, such as "on Haiku, explicit state can misremember, so check the values." I left it alone because you asked me to keep everything else. If you approve, I can add that sentence and it will add about 4 s.
- **The hook still reads fast.** The reading-speed fix is still to leave a short beat between the two sentences, not to speed up the voice.
- **The ES decimal is a guess.** I kept "0,999" on the assumption that the Spanish article uses a decimal comma. If it writes 0.999, match it.
- **Cuts from the last version are unchanged.** The retraction result, the 5.2x prompt-order cost, and the "repeat every cell" point are still out. The retraction result fits best as a `BarCompare` scene after scene 5 if you want it back.
- **Nothing is saved to a file.** This is the full script in the table for you to paste. Nothing gets built until you approve it.
