Here is the revised script. The only narration changes are the numbers. Scene 3 and scene 6 now state their figures inside natural sentences, and scene 6 gets a second line so the 0.999 score has its own sentence.

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
| 6 So what | `BarCompare` | On Haiku, keeping the transcript too absorbed it. | En Haiku, guardar también la transcripción lo absorbió. | Haiku at T=200: ReAct 0.974, Stateful 0.999 (highlighted), SKILL.state 0.958. | Table: "Claude Haiku 4.5 \| 0.974 \| 0.999 \| 0.958"; "Keeping the transcript absorbs it" |
| 6 So what | `BarCompare` | Stateful scored 0.999. | Stateful obtuvo 0,999. | Stateful bar fills to 0.999 and holds its highlight. | Table: Claude Haiku 4.5 row, Stateful column, 0.999 |
| 7 So what | `KeyQuote` | A schema checks the patch's shape. Nothing checks its value. | Un esquema valida la forma del parche. Nada mira su valor. | Quote card. "shape" in teal, "value" in amber. | "A schema can validate the shape of a patch; nothing in the runtime checks that the value matches what the action did." |
| 7 So what | `KeyQuote` | If you build on explicit state, that check is what to add. | Si construyes sobre estado explícito, añade esa comprobación. | Second line of the quote fades in. | "If you build on explicit state, that check is the part to add." |
| 8 Close | Outro card | More at javieraguilar.ai | Más en javieraguilar.ai | Outro card | — |

**EN word count:** 111 caption words by my count (the previous version is 107 by my count, though it was stated as 109). **Estimated length:** about 51 s.

## Spoken forms (the captions stay as written)
- "SKILL.state" is said as "skill dot state".
- "Gemini-3-Flash" is said as "Gemini three Flash".
- "Haiku 4.5" is said as "Haiku four point five" (ES: "cuatro punto cinco").
- "0.999" is said as "zero point nine nine nine" (ES: "cero coma nueve nueve nueve").
- "javieraguilar.ai" is said as "javier aguilar dot A I".

## Notes for review
- **Number changes:** "75 episodes, up to 200 steps" is now a sentence ("in 75 episodes of up to 200 steps"). The bare "0.999" after a colon is now its own sentence ("Stateful scored 0.999."), so the figure reads as a result rather than a label. The Spanish follows the same pattern.
- **Closing verdict:** The skill asks the closing to say plainly what the result means (good, bad, or only sometimes). Scene 7 doesn't do that yet. The article's verdict is closer to "only sometimes": the state approach held on Gemini and broke on Haiku. A possible extra line is "On Gemini it held. On Haiku, it sometimes broke." I haven't added it, since you asked me to keep everything else as it was.
- **Hook line:** It is still close to 17 characters per second. Lint may flag it against the real audio. If so, shorten the text rather than speeding up the voice.
- **ES decimal:** "0,999" assumes the Spanish article uses a decimal comma. If it writes 0.999, match it.
- **Cut material:** The 70/72 vs 10/72 retraction result, the 5.2x prompt-order cost, the "repeat every cell" point, and the Gemini 0/75 line are still out. The 0/75 figure still appears in the scene 5 tiles.
- **Hedges kept:** "in one case" for the seed-2 cascade, and "On Haiku" for the transcript result.

Nothing is built until you approve the script. I still can't write `script.md` from here, so the table above is ready to paste.
