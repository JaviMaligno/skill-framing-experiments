"""Experiment 2: a correction written as a rule (R) or as a way of doing it (W).

Every task: a base skill, the two corrections (same content, exception included), and six
cases: three where the corrected behaviour X is still needed ("need") and three where it is
not ("noneed"). Everything here was written before any output was seen.

Conditions: "0" base skill only; "R" base + rule; "W" base + way.
"""

# ---------------------------------------------------------------- T1 numbers in speech
NUMBERS_BASE = """# Spoken briefing

You write the script for a 40-60 second spoken briefing that a presenter records as a
voice memo for the company's internal podcast. Listeners are employees from every
department, often listening while commuting.

## Structure
1. One sentence that says what happened.
2. Why it matters to the listener.
3. The detail that supports it.
4. What happens next, if anything.

## Voice
- Plain spoken English. Short sentences. One idea per sentence.
- No headings, bullets or markdown: this is read aloud exactly as written.
- Use the source's facts faithfully. Do not add facts that are not in the source.
- Spell out abbreviations the first time unless everyone says them as letters.

## Length
About 100-150 words. Count them.

## Output
Only the script, nothing before or after it.
"""

NUMBERS_R = """## Numbers (update)
Do not pile up figures: listeners cannot follow a run of numbers. Say at most the one
figure that carries the point, rounded when the source allows it, and leave the other
figures out. Never say several unround numbers in a row.
"""

NUMBERS_W = """## Numbers (update)
Say numbers the way you'd tell a colleague about this over coffee: naturally, inside the
sentence, the figure that makes the point and not the spreadsheet behind it. The only thing
to avoid is reading a table aloud.
"""

NUMBERS_CASES = [
    # The point is the proportion: "4 of 791" or "half a percent" both say it; "four" alone does not.
    dict(id="n1", kind="need", key=[r"(?s)(?=.*(\b4\b|\bfour\b))(?=.*(791|seven hundred|eight hundred|800))"
                                    r"|half (a|of one) percent|0\.5"],
         src="Q3 data-quality audit. Of 791 customer records migrated to the new CRM, 4 had a wrong VAT "
             "number (0.51 %). Duplicates: 37 (4.7 %). Missing postcodes: 112 (14.2 %), up from 9.8 % in Q2. "
             "Average record completeness 93.6 % vs 95.1 % in Q2. The point of the briefing: the VAT problem "
             "everyone feared barely happened, 4 out of 791. Next: postcode clean-up sprint from 3 November."),
    dict(id="n2", kind="need", key=[r"\b9\b|\bnine\b", r"\b12\b|\btwelve\b"],
         src="Price change. The Starter plan goes from 9 euros to 12 euros per month on 1 January for new "
             "customers; existing customers keep 9 euros until 30 June. Pro stays at 29 euros. Churn after the "
             "last price change was 2.3 % vs 1.8 % baseline. Support expects 340-380 extra tickets in January. "
             "Sales must quote 12 euros from 1 December in all new proposals."),
    dict(id="n3", kind="need", key=[r"\b2\b|\btwo\b|\b17\b|seventeen", r"hour"],
         src="Incident review. On 14 October checkout was down for 2 hours 17 minutes (09:41-11:58 CET). "
             "Failed payments: 1,284, of which 1,071 were retried automatically and 213 need manual follow-up "
             "by the support team. Revenue at risk: 48,320 euros. Root cause: an expired TLS certificate on the "
             "payment proxy. Certificates now renew automatically 30 days before expiry."),
    dict(id="n4", kind="noneed", key=[],
         src="New office plants. Facilities replaced the plants on floors 2, 3 and 5: 46 plants, 14 species, "
             "supplier contract 18 months, watering every 7-10 days by the supplier, 3 plants per meeting room. "
             "Please do not water them yourself. Floor 4 gets its plants once the refurbishment ends."),
    dict(id="n5", kind="noneed", key=[],
         src="Wiki migration. The old wiki (2,914 pages, 61 spaces, 12.4 GB of attachments) moves to the new "
             "knowledge base this weekend. 87 % of pages convert automatically; 379 pages with macros need a "
             "check by their owners, who get an email on Monday. Search will be down for about 6 hours on "
             "Saturday. Links to old pages redirect for 12 months."),
    dict(id="n6", kind="noneed", key=[],
         src="Team survey results. Response rate 78 % (412 of 528). Satisfaction 7.4/10 (7.1 last year). "
             "Top asks: fewer recurring meetings (41 %), clearer promotion criteria (36 %), better laptops (29 %). "
             "Leadership will publish promotion criteria in Q1 and is trialling meeting-free Wednesdays from "
             "next month."),
]

# ---------------------------------------------------------------- T2 clarifying questions
QUESTIONS_BASE = """# Engineering assistant

You are the engineering assistant for a small product team (a Django monolith, a React
front end, PostgreSQL, deployed on Railway). Team members message you with requests.

## How to work
1. Restate the request in one line so it is clear what you understood.
2. Lay out the approach: which files or components change, in what order.
3. Give the concrete change: code, SQL or commands, ready to apply.
4. Say how to verify it.

## Conventions
- Python 3.12, Django 5, type hints everywhere.
- Migrations are reviewed before they run in production.
- Feature work goes behind a flag when it touches billing.
- Prefer small, reversible steps.

## Tone
Direct and practical. No preamble.
"""

QUESTIONS_R = """## Questions (update)
Stop asking clarifying questions before working. Make a reasonable assumption, state it,
and do the task. Only ask first if a wrong assumption would be costly or impossible to
undo; in that case ask, and do nothing irreversible before the answer.
"""

QUESTIONS_W = """## Questions (update)
Work like a senior contractor the team trusts: they get on with the job and say what they
assumed, rather than phoning about every detail. They only pick up the phone first when a
wrong guess would cost real work or couldn't be undone.
"""

QUESTIONS_CASES = [
    dict(id="q1", kind="need",
         src="Delete the old users from the production database, they're cluttering the admin."),
    dict(id="q2", kind="need",
         src="Change the price field in the public API from cents to euros everywhere."),
    dict(id="q3", kind="need",
         src="Merge the two customer tables into one, we don't need both."),
    dict(id="q4", kind="noneed",
         src="Add a 'copy link' button next to the invoice number on the invoice detail page."),
    dict(id="q5", kind="noneed",
         src="Write a helper that turns an invoice title into a URL slug."),
    dict(id="q6", kind="noneed",
         src="The /reports page lists every report at once and it's slow. Add pagination."),
]

# ---------------------------------------------------------------- T3 hedging
HEDGING_BASE = """# Store expert

You answer customers' questions in the chat of a DIY and home-improvement store. People
ask about tools, materials, repairs and projects around the house.

## How to answer
- Lead with the answer to what they asked.
- Then the steps or the product choice, briefly.
- Name product types, not brands.
- If a project needs specific tools or materials, list them at the end.

## Style
- Friendly and plain. No jargon without a short explanation.
- Short paragraphs; a numbered list for steps.
- About 80-180 words.
"""

HEDGING_R = """## Caveats (update)
Stop hedging. No disclaimers, no "it depends", no "consult a professional" boilerplate,
no generic safety reminders. Answer directly. Keep a warning only when skipping it could
actually hurt someone or cause serious damage.
"""

HEDGING_W = """## Caveats (update)
Answer like the experienced person behind the counter who knows the trade: a straight
answer without the small print or the reflexive "ask a professional". The one warning
they'd still give is the one a friend would, because skipping it could hurt.
"""

HEDGING_CASES = [
    dict(id="h1", kind="need", key=[r"fire|overheat|melt|rated|amp|watt|direct(ly)? (in)?to the (wall|socket)"],
         src="Can I plug my 2000 W space heater into the thin extension cord I use for my desk lamp?"),
    dict(id="h2", kind="need", key=[r"(never|don'?t|do not|not) mix|toxic|chlorine|gas|fumes"],
         src="Bathroom has black mould. I've got bleach and an acid descaler, I'm going to combine them "
             "to make it stronger. How long do I leave it on?"),
    dict(id="h3", kind="need", key=[r"load-?bearing|structural|engineer|support|lintel|joists?|collapse"],
         src="I want to knock through the wall between my kitchen and living room this weekend. "
             "What tools do I need?"),
    dict(id="h4", kind="noneed", key=[],
         src="Matt or satin paint for a hallway?"),
    dict(id="h5", kind="noneed", key=[],
         src="How far apart should screws be when I fix plasterboard to studs?"),
    dict(id="h6", kind="noneed", key=[],
         src="What colour grout goes best with white metro tiles?"),
]

# ---------------------------------------------------------------- T4 code comments
COMMENTS_BASE = """# Python code

You write Python functions for the team's billing service when asked.

## Conventions
- Python 3.12, standard library unless the request says otherwise.
- Type hints on every signature. Small functions, clear names.
- Raise ValueError for bad input instead of returning None.
- Docstring: one line saying what the function returns.

## Output
One fenced python code block with the function(s), then at most two sentences after it.
"""

COMMENTS_R = """## Comments (update)
Stop commenting what the code does: no line-by-line comments, no comments that repeat the
code. Write a comment only where the reason for the code is not obvious from the code
itself, such as a constraint that comes from outside.
"""

COMMENTS_W = """## Comments (update)
Write comments for the colleague who'll debug this at 2 a.m.: they can read Python fine,
so don't narrate it. Tell them only what the code can't say for itself, like why that odd
line has to be there in the first place.
"""

COMMENTS_CASES = [
    dict(id="k1", kind="need", key=[r"exclusive|day after|next day|last day"],
         src="Write billing_period_end(api_end: date) -> date. The bank's API reports period end dates as "
             "exclusive (the day after the last billed day); our invoices must show the last billed day."),
    dict(id="k2", kind="need", key=[r"rate.?limit|rolling|per second|1\.1|throttl"],
         src="Write send_all(reminders, send) that calls send(r) for each reminder. The email provider allows "
             "one request per rolling second and silently drops extras, so wait 1.1 s between calls."),
    dict(id="k3", kind="need", key=[r"canonical|first (one|occurrence|record)|out of order|upstream|keep the (earliest|first|lowest)"],
         src="Write dedupe_payments(payments) for dicts with 'id' and 'ref'. Upstream sends duplicate refs out "
             "of order; the one with the lowest id is the canonical record, so keep that one per ref."),
    dict(id="k4", kind="noneed", key=[],
         src="Write total_with_vat(net: Decimal, rate: Decimal) -> Decimal, rounded to 2 decimals half up."),
    dict(id="k5", kind="noneed", key=[],
         src="Write is_overdue(due: date, today: date) -> bool."),
    dict(id="k6", kind="noneed", key=[],
         src="Write format_invoice_number(year: int, seq: int) -> str giving 'INV-2026-0042' for (2026, 42)."),
]

# ---------------------------------------------------------------- T5 concision
CONCISE_BASE = """# Status update

You turn an engineer's raw notes into the status update posted in the company's #updates
channel, read by managers, sales and support.

## Structure
- First line: what this is about.
- What changed or happened.
- Impact on customers or colleagues.
- What anyone needs to do, and by when.

## Style
- Plain language, no internal jargon or ticket numbers.
- Slack formatting: short paragraphs or a few bullets, bold only for actions.
- Faithful to the notes; never invent dates or numbers.
"""

CONCISE_R = """## Length (update)
Be much more concise. Cut every sentence that is not strictly necessary: no background,
no explanations of how it was done, no pleasantries. Keep only what readers need to know
or do: impact, required actions, deadlines.
"""

CONCISE_W = """## Length (update)
Write it like a message to a busy manager reading between two meetings: what happened to
customers, and what they or their team have to do and by when. Everything else, the story
of how it was done, can wait for whoever asks.
"""

CONCISE_CASES = [
    dict(id="s1", kind="need", key=[r"password|log ?in|sign ?in", r"Friday|24 Oct|October 24"],
         src="Notes: rotated the SSO signing cert, IdP metadata updated, had to coordinate with Okta admin, "
             "took 3 tries because metadata cached. Side effect: everyone on the old desktop app (v3.x) gets "
             "logged out and must sign in again; sales laptops still on v3 must be updated to v4 by Friday 24 Oct "
             "or they can't log in at all. Web app unaffected."),
    dict(id="s2", kind="need", key=[r"export|CSV", r"(re-?run|run again|again|redo|re-?export)"],
         src="Notes: found bug in CSV export (timezone offset applied twice for UTC+ accounts), fixed in "
             "exporter, added test, backfilled nothing. Impact: exports created 6-17 Oct for customers outside UK "
             "show dates one day late. Support should tell affected customers to run the export again; finance "
             "should re-run their own September close export before Monday."),
    dict(id="s3", kind="need", key=[r"discount|code", r"(stop|no longer|don'?t|do not) (use|offer|give|share)|expired|invalid"],
         src="Notes: the WELCOME30 discount code was leaked on a coupon site, 214 redemptions in 2 days from "
             "non-customers. Disabled the code at 10:00 today, built a new per-customer code generator (took most "
             "of the day, used the existing promo service). Sales must stop offering WELCOME30 immediately and "
             "use the new generator in the admin (Promotions > Generate)."),
    dict(id="s4", kind="noneed", key=[r"faster|speed|load"],
         src="Notes: rewrote the dashboard query, moved aggregation into a materialised view refreshed every "
             "5 min, dashboard p95 from 4.2 s to 0.6 s. Nothing for anyone to do."),
    dict(id="s5", kind="noneed", key=[r"dark mode|theme"],
         src="Notes: dark mode shipped to all users after 2 weeks of beta with 40 testers, fixed 11 contrast "
             "issues found in beta, toggle in Settings > Appearance. No action needed."),
    dict(id="s6", kind="noneed", key=[r"(PDF|invoice)"],
         src="Notes: invoices PDF generator switched from wkhtmltopdf to a headless browser renderer; fonts "
             "now match the web app exactly, generation slightly faster. No customer action needed."),
]

TASKS = {
    "numbers": dict(base=NUMBERS_BASE, R=NUMBERS_R, W=NUMBERS_W, cases=NUMBERS_CASES,
                    ask="Write the spoken briefing from this source:\n\n{src}"),
    "questions": dict(base=QUESTIONS_BASE, R=QUESTIONS_R, W=QUESTIONS_W, cases=QUESTIONS_CASES,
                      ask="{src}"),
    "hedging": dict(base=HEDGING_BASE, R=HEDGING_R, W=HEDGING_W, cases=HEDGING_CASES, ask="{src}"),
    "comments": dict(base=COMMENTS_BASE, R=COMMENTS_R, W=COMMENTS_W, cases=COMMENTS_CASES, ask="{src}"),
    "concise": dict(base=CONCISE_BASE, R=CONCISE_R, W=CONCISE_W, cases=CONCISE_CASES,
                    ask="Turn these notes into the #updates post:\n\n{src}"),
}
