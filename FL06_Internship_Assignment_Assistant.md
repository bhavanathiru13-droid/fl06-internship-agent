# FL-06: Design Your Personal Agent

## Internship Assignment Assistant

**Owner:** Bhavana\
**Track:** General AI Fluency\
**Phase:** Build

## 1. Job to be done

The Internship Assignment Assistant helps me organize internship tasks,
understand assignment requirements, track progress, and decide what to
do next.

Its core job is to turn an assignment brief into a clear checklist,
identify missing requirements, maintain a simple progress log, and check
whether the work appears ready for submission.

The assistant focuses on internship assignments rather than trying to
manage my entire academic or personal life.

## 2. User and usage frequency

**Primary user:** Me, a B.Tech AI & Data Science student completing
technical internship assignments.

**Usage frequency:** Whenever a new assignment arrives, whenever I make
progress, and before I submit an assignment.

**Typical workflow:** 1. Provide the assignment instructions. 2. Extract
the deliverables and evaluation criteria. 3. Create a step-by-step
checklist. 4. Update each task as not started, in progress, or
completed. 5. Review the evidence and identify anything missing. 6.
Produce a final submission checklist.

## 3. Tools, data, and access plan

**Initial platform:** A Python script developed in VS Code, using local
Markdown and CSV files.

**Data sources:** - Assignment instructions supplied by me. - A local
task tracker containing assignment names, requirements, deadlines,
status, and evidence links. - Public project or notebook URLs that I
explicitly provide.

**Access plan:** The first version will use manually supplied text and
local files. It will not automatically access my email, calendar,
private internship dashboard, or GitHub account. If I provide a public
URL, the initial version may require me to open and verify it manually.

**Data storage:** Store only the information necessary to track tasks.
Do not store passwords, API keys, private tokens, or unnecessary
personal information.

**Future enhancement:** An optional AI model could summarize
instructions and explain technical concepts. Any external AI service
would require an appropriate access plan and review of its data-handling
terms.

## 4. Draft agent instructions

You are my Internship Assignment Assistant. Your purpose is to help me
complete internship assignments accurately and understand the work I
submit.

For every new assignment:

1.  Identify the assignment title, objective, deliverables, evaluation
    criteria, and deadline if provided.
2.  Break the work into small, ordered actions suitable for a beginner.
3.  Explain unfamiliar technical terms in simple English, with examples
    when helpful.
4.  Ask for missing information instead of inventing requirements or
    results.
5.  Track progress only from information or evidence I provide.
6.  Before submission, check the required files, repository path,
    execution status, public-link accessibility, and written explanation
    where relevant.
7.  Clearly distinguish verified facts from assumptions and incomplete
    checks.
8.  Never claim an assignment has been saved, uploaded, or submitted
    unless there is reliable evidence.
9.  Never submit work, change files, send messages, or modify accounts
    without my explicit approval.
10. Encourage me to explain technical decisions in my own words rather
    than blindly copying generated answers.

## 5. Evaluation plan: five test cases

### Test 1 --- New assignment

**Input:** An assignment brief listing four deliverables.\
**Expected result:** The agent extracts all four deliverables and
produces an ordered checklist without inventing additional requirements.

### Test 2 --- Missing deadline

**Input:** Assignment instructions with no deadline.\
**Expected result:** The agent marks the deadline as unknown and asks me
to provide it instead of guessing.

### Test 3 --- Partial progress

**Input:** The notebook has been executed, but the repository link has
not been verified.\
**Expected result:** The agent marks execution as completed based on my
report but keeps repository verification and submission pending.

### Test 4 --- Incorrect or inaccessible link

**Input:** A project URL that cannot be opened or does not point to the
expected file.\
**Expected result:** The agent flags the link for correction and does
not claim that the project is publicly accessible.

### Test 5 --- Submission readiness

**Input:** A task checklist with one required deliverable still
incomplete.\
**Expected result:** The agent identifies the missing deliverable and
reports that the assignment is not yet ready for submission.

**Pass criteria:** The agent must be accurate about task status,
preserve all stated requirements, avoid invented information, and
clearly identify unresolved items in all five tests.

## 6. Risks and guardrails

-   **Incorrect summaries:** Preserve the original requirements and ask
    me to verify ambiguous interpretations.
-   **False completion claims:** Require evidence or an explicit user
    report before marking work complete.
-   **Privacy exposure:** Use only necessary task information and avoid
    storing credentials or confidential data.
-   **Unapproved actions:** Keep external changes and submissions under
    my control.
-   **Over-reliance on AI:** Explain recommendations and ask me to
    review technical conclusions before using them.
-   **Stale task status:** Record when a status was last updated and
    reconfirm it when necessary.

The agent must never fabricate results, conceal uncertainty, or submit
work automatically.

## 7. Build platform and implementation plan

I will start with a scripted Python agent in VS Code because it is free
to prototype, fits my current learning level, and allows me to inspect
how the workflow operates.

**Phase 1:** Create a local task tracker and a Python script that reads
assignment details and produces a checklist.

**Phase 2:** Add progress updates, missing-information checks, and a
submission-readiness report.

**Phase 3:** Optionally integrate an AI model for summarization and
explanations, after checking the cost, privacy implications, and access
requirements.

The first version will not need paid connectors, autonomous browsing, or
automatic submission capabilities.

## Definition of done

The prototype is ready for an initial demonstration when it can process
a sample assignment, generate a complete checklist, track partial
progress, identify missing evidence, and pass all five evaluation cases.
Its limitations and manual verification requirements will be documented.

**Expected outcome:** A small, understandable assistant that helps me
manage internship assignments while keeping technical decisions,
verification, and final submissions under my control.
