"""Release-notes cases. Written before any output was seen.

Each change is one merged item as an engineer would title it.
kind: "visible" (a user notices it) or "internal" (should be left out).
anchors: regexes; any hit means the change is mentioned in the notes.
required: terms the user needs verbatim (S5); each entry is a regex of accepted variants.
leak: literal internal tokens from the input that must not reach the notes (S4).
action: for cases where the user must do something (S6): what + date regexes.

Split: c01-c06 dev (patches are derived from these), c07-c12 test (held out).
"""

C = lambda text, kind, anchors, required=(), leak=(): dict(
    text=text, kind=kind, anchors=list(anchors), required=list(required), leak=list(leak))

CASES = [
    dict(id="c01", split="dev", changes=[
        C("FAC-1182: API keys now expire after 90 days; existing keys without expiry are revoked on 2026-11-15 (#4410)",
          "visible", [r"API key"], [r"API key"], ["FAC-1182", "#4410"]),
        C("Refactor InvoiceRenderer to use pdfkit 0.15", "internal", [r"pdfkit", r"InvoiceRenderer", r"renderer"],
          leak=["InvoiceRenderer", "pdfkit"]),
        C("Fix: N+1 query on client list made the Clients page take 8s to load for accounts with >500 clients",
          "visible", [r"client(s)? (list|page)", r"Clients page"], leak=["N+1"]),
        C("Bump eslint to 9.12", "internal", [r"eslint", r"\blint"], leak=["eslint"]),
        C("Fix: tooltip on Due date column overlapped the Status filter", "visible", [r"tooltip", r"due date"]),
        C("Add Sentry breadcrumbs to checkout flow", "internal", [r"Sentry", r"breadcrumb", r"checkout"], leak=["Sentry"]),
    ], action=dict(what=[r"regenerat", r"create a new", r"new API key", r"generate"],
                   when=[r"November 15", r"15 November", r"Nov\.? 15", r"2026-11-15", r"15/11", r"11/15"])),

    dict(id="c02", split="dev", changes=[
        C("Two-factor authentication (TOTP) available under Settings -> Security", "visible",
          [r"two-factor", r"2FA", r"authenticator"], [r"two-factor authentication|2FA"]),
        C("Migrate sessions table to Postgres 16", "internal", [r"Postgres", r"sessions table", r"database"],
          leak=["Postgres"]),
        C("Fix: race condition in autosave lost edits when two tabs were open", "visible",
          [r"two tabs", r"another tab", r"multiple tabs", r"more than one tab", r"lost (your )?(edits|changes)", r"autosave"]),
        C("CSV export now includes the Paid on column", "visible", [r"CSV", r"export"], [r"CSV"]),
        C("Increase unit test coverage of tax module to 85%", "internal", [r"test coverage", r"unit test", r"85 ?%"]),
        C("Fix typo in Spanish invoice footer ('Fatura' -> 'Factura')", "visible",
          [r"typo", r"Spanish", r"footer", r"Factura"]),
    ], action=None),

    dict(id="c03", split="dev", changes=[
        C("Webhooks: new invoice.paid event (LED-77)", "visible",
          [r"webhook", r"invoice\.paid", r"paid event"], [r"webhook"], ["LED-77"]),
        C("Replace moment.js with date-fns", "internal", [r"moment", r"date-fns"], leak=["moment.js", "date-fns"]),
        C("Fix: PDF invoices showed totals rounded to whole euros when locale was de-DE", "visible",
          [r"round", r"whole euro", r"cents", r"totals?"], [r"PDF"], ["de-DE", "locale"]),
        C("Dark mode for the dashboard (Settings -> Appearance)", "visible", [r"dark mode", r"Appearance"]),
        C("Upgrade CI runners to ubuntu-24.04", "internal", [r"ubuntu", r"\bCI\b", r"runner"], leak=["ubuntu"]),
        C("Log retry attempts for failed Stripe webhook deliveries", "internal", [r"retry attempt", r"\blog(s|ged|ging)?\b"]),
    ], action=None),

    dict(id="c04", split="dev", changes=[
        C("Deprecate legacy XLS export; XLS export is removed on 2026-12-01, use XLSX or CSV instead", "visible",
          [r"\bXLS\b", r"XLSX"], [r"XLSX"]),
        C("Fix: clicking 'Send reminder' twice sent two emails (debounce missing)", "visible",
          [r"reminder", r"twice", r"two emails", r"duplicate"], [r"Send reminder"], ["debounce"]),
        C("Extract EmailService into its own module", "internal", [r"EmailService", r"\bmodule"], leak=["EmailService"]),
        C("Add OpenTelemetry tracing to API gateway", "internal", [r"OpenTelemetry", r"tracing", r"gateway"],
          leak=["OpenTelemetry"]),
        C("Recurring invoices: option to bill on the last day of the month", "visible",
          [r"recurring", r"last day of (the )?month"]),
        C("Fix: logo upload failed for SVG files over 1MB", "visible", [r"logo", r"SVG"], [r"SVG"]),
    ], action=dict(what=[r"XLSX", r"switch", r"CSV"],
                   when=[r"December 1\b", r"1 December", r"Dec\.? 1\b", r"2026-12-01", r"1/12", r"12/1\b"])),

    dict(id="c05", split="dev", changes=[
        C("SEPA Direct Debit payments via GoCardless (Settings -> Payments)", "visible",
          [r"SEPA", r"direct debit"], [r"SEPA"]),
        C("Fix: null pointer when client had no email crashed the Send button", "visible",
          [r"no email", r"without an? email", r"email address", r"missing email"], leak=["null pointer"]),
        C("Rename DB column amount_cents -> amount_minor", "internal", [r"amount_cents", r"amount_minor", r"column"],
          leak=["amount_cents", "amount_minor"]),
        C("Cache exchange rates for 1h instead of 24h, so converted totals are fresher", "visible",
          [r"exchange rate", r"currenc", r"convert"]),
        C("Storybook stories for Button component", "internal", [r"Storybook", r"stories"], leak=["Storybook"]),
        C("Fix: date picker started weeks on Sunday for UK users", "visible",
          [r"date picker", r"calendar", r"Monday", r"Sunday"]),
    ], action=None),

    dict(id="c06", split="dev", changes=[
        C("Single sign-on (SSO) with Google Workspace for team accounts (beta)", "visible",
          [r"single sign-on", r"\bSSO\b"], [r"single sign-on|\bSSO\b"]),
        C("Fix flaky deploy pipeline on staging", "internal", [r"staging", r"pipeline", r"flaky"]),
        C("Fix: VAT number validation rejected valid Irish numbers (IE1234567FA format)", "visible",
          [r"VAT", r"Irish", r"Ireland"], [r"VAT"]),
        C("Upgrade React 18 -> 19", "internal", [r"React"], leak=["React"]),
        C("Fix: dashboard chart showed last month's revenue as current after midnight UTC (timezone bug)", "visible",
          [r"chart", r"revenue", r"midnight"]),
        C("Add rate limiting to public invoice links (LED-91)", "internal", [r"rate limit", r"LED-91"], leak=["LED-91"]),
    ], action=None),

    dict(id="c07", split="test", changes=[
        C("Bank feed provider moves from Plaid to TrueLayer; users must reconnect their bank in Settings -> Bank feeds by 2026-11-30",
          "visible", [r"bank feed", r"reconnect", r"TrueLayer"], [r"Bank feeds?"]),
        C("Refactor PaymentMatcher heuristics", "internal", [r"PaymentMatcher", r"heuristic"], leak=["PaymentMatcher"]),
        C("Fix: matched payments appeared twice in the Transactions list after a reconnect", "visible",
          [r"twice", r"duplicate", r"Transactions"]),
        C("Bump Node to 22.11", "internal", [r"\bNode\b"], leak=["Node 22"]),
        C("IBAN shown in the invoice PDF footer", "visible", [r"IBAN"], [r"IBAN"]),
        C("Add Datadog dashboards for queue depth", "internal", [r"Datadog", r"queue"], leak=["Datadog"]),
    ], action=dict(what=[r"reconnect", r"connect (your bank )?again", r"re-?link"],
                   when=[r"November 30", r"30 November", r"Nov\.? 30", r"2026-11-30", r"30/11", r"11/30"])),

    dict(id="c08", split="test", changes=[
        C("Zapier integration: new trigger 'Invoice overdue'", "visible", [r"Zapier", r"overdue"], [r"Zapier"]),
        C("Fix: memory leak in PDF worker made generation time out for large invoices (100+ lines)", "visible",
          [r"large invoices?", r"100", r"time(d)? out", r"long invoices?", r"many lines"], leak=["memory leak", "worker"]),
        C("Convert remaining class components to hooks", "internal", [r"class component", r"\bhooks\b"],
          leak=["class components"]),
        C("Payment QR code on invoices (EPC QR / Girocode)", "visible", [r"QR"], [r"QR code"]),
        C("Add e2e tests for onboarding with Playwright", "internal", [r"Playwright", r"e2e", r"end-to-end"],
          leak=["Playwright"]),
        C("Fix: 'Duplicate invoice' button copied the old due date", "visible",
          [r"Duplicate invoice", r"due date"], [r"Duplicate invoice"]),
    ], action=None),

    dict(id="c09", split="test", changes=[
        C("Public API: rate limit raised from 60 to 300 requests/min (LED-120)", "visible",
          [r"300", r"rate limit", r"requests"], [r"\bAPI\b"], ["LED-120"]),
        C("Move image storage from S3 to R2", "internal", [r"\bS3\b", r"\bR2\b", r"storage"], leak=["S3", "R2"]),
        C("Fix: expense receipts in HEIC format (iPhone photos) could not be uploaded", "visible",
          [r"HEIC", r"iPhone", r"receipt"], [r"HEIC|iPhone"]),
        C("Reports: profit & loss can be filtered by client", "visible", [r"profit", r"P&L", r"filter"]),
        C("Fix: off-by-one in pagination hid the 51st invoice", "visible",
          [r"51", r"missing invoice", r"hid", r"(didn't|did not|wasn't|was not) show", r"invoice list"],
          leak=["off-by-one", "pagination"]),
        C("Clean up feature flags for the old onboarding", "internal", [r"feature flag", r"onboarding"]),
    ], action=None),

    dict(id="c10", split="test", changes=[
        C("E-invoicing: send invoices over the Peppol network to public-sector clients", "visible",
          [r"Peppol", r"e-invoic"], [r"Peppol"]),
        C("Fix: credit notes didn't subtract from the client's outstanding balance", "visible",
          [r"credit note", r"balance"], [r"credit note"]),
        C("Rewrite tax engine in Rust (no behaviour change)", "internal", [r"Rust", r"tax engine", r"rewr"],
          leak=["Rust"]),
        C("Update Terraform modules", "internal", [r"Terraform"], leak=["Terraform"]),
        C("Fix: 'Mark as paid' button disabled on mobile Safari", "visible",
          [r"Mark as paid", r"Safari", r"mobile", r"iPhone"], [r"Mark as paid"]),
        C("Add structured logging to invoice sender", "internal", [r"structured", r"\blog(s|ged|ging)?\b"]),
    ], action=None),

    dict(id="c11", split="test", changes=[
        C("Password policy: minimum 12 characters; users with shorter passwords must change it at next login after 2026-11-20",
          "visible", [r"password"], [r"password"]),
        C("Hash passwords with argon2id instead of bcrypt", "internal", [r"argon", r"bcrypt", r"hash"],
          leak=["argon2id", "bcrypt"]),
        C("Sign in with Microsoft accounts (OAuth)", "visible", [r"Microsoft"], [r"Microsoft"], ["OAuth"]),
        C("Fix: session expired silently and lost unsaved invoice drafts", "visible",
          [r"draft", r"signed out", r"logged out", r"unsaved"]),
        C("Bump TypeScript to 5.7", "internal", [r"TypeScript"], leak=["TypeScript"]),
        C("Fix: German translation missing on the Settings page", "visible", [r"German", r"translation"]),
    ], action=dict(what=[r"change (your|their) password", r"update (your|their) password", r"new password",
                         r"asked to change", r"12 characters"],
                   when=[r"November 20", r"20 November", r"Nov\.? 20", r"2026-11-20", r"20/11", r"11/20"])),

    dict(id="c12", split="test", changes=[
        C("Multi-currency: invoice in one currency and get paid in another, with the conversion shown on the PDF",
          "visible", [r"currenc"], [r"currenc"]),
        C("Fix: CSV import failed on files with semicolon delimiters (common in Spain/Germany)", "visible",
          [r"CSV", r"import", r"semicolon"], [r"CSV"], ["delimiter"]),
        C("Batch GraphQL client resolver with DataLoader", "internal", [r"GraphQL", r"DataLoader", r"resolver"],
          leak=["GraphQL", "DataLoader"]),
        C("Archive clients instead of deleting them; archived clients are hidden from lists", "visible", [r"archiv"]),
        C("Remove unused CSS (-40KB)", "internal", [r"\bCSS\b", r"unused"], leak=["CSS"]),
        C("Fix: email preview showed a raw {{client_name}} placeholder", "visible",
          [r"preview", r"placeholder", r"client'?s? name"], leak=["{{client_name}}"]),
    ], action=None),
]
