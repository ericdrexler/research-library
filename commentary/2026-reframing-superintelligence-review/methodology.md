# How the review was done

**Purpose.** The review, and the files it produced, serve one purpose: to help bring discussion of AI risk and safety into line with a realistic understanding of problems and options, under epistemic discipline. *Reframing Superintelligence* serves as springboard and reference; what in it failed is stated as plainly as what remains useful.

This file describes how the report (K. Eric Drexler, FHI Technical Report 2019-1, January 2019; written and circulated section by section from December 2016) was reviewed between 9 and 12 October 2026, who did what, and where the review's limits lie. The review produced the concept assessment and the fact pack in this folder; the essay (`essay.md`) draws on it.

## The governing question

> Not "what has been confirmed as of 2026?" but "what, despite divergences of path and state, remains forward-looking, compatible with current developments, and potentially important?"

The author set this question partway through the review, replacing the one it had in effect been answering: how well the report's claims had been confirmed by 2026. His reason: the report looks toward a superintelligent-level (SI-level) end-game with abundant capacity, and reading it as a (poor) description of 2026 technology distorts its framework and misjudges the degree and form of its fit to reality. Fit between the path anticipated and the path taken still matters, but it is secondary. *Compatible* is not *supported*, so every concept in the assessment states what would weaken it, and which of those conditions are already partly met.

## Who did what

**Claude models (Anthropic) did the review.** An orchestrating session wrote the briefs and settled disagreements between agents. Separate agent instances extracted and graded claims, critiqued, reconciled, verified facts, and drafted and critiqued the concept assessment. The review's initial framing document was written mainly by an earlier Claude session at the author's direction (described below).

**The author, Eric Drexler, supplied four things.**
- *The questions:* the initial task and, later, the governing question above.
- *The meanings of his own terms.* For example, "readily" in a design claim means achievable by a competent effort, not easy; and "achievable" means that a competent, well-resourced effort, using known methods and their foreseeable extensions, can follow a path with no conceptual breakthrough.
- *Methodological proposals, each with its reason.*
  - Judge design claims as design claims, not as predictions, because a claim that something can be built and would work is not refuted by developers declining to build it, and "bad designs would be bad" says nothing about it.
  - Read for intent, following the hermeneutic circle, because a reading that makes a competent author extraordinarily naive is probably wrong. The review added the converse: so is a reading that makes him more prescient than the text.
  - Assess concepts, not isolated claims, because claim-level grades are background detail for documents that carry a coherent overall message.
- *Views on scope and on what his own terms mean, and objections to four scorings*, listed in the next section with how each was handled.

**What he did not supply:** grades or conclusions. Where the review uses his wording, it is attributed to him or concerns facts he corrected. Grades were set by the review's assessments against the report's text; his views entered as inputs, and the next section says how each was handled. His comments on drafts corrected how facts, his ideas and his role were stated, and decided which files are published. His initial interpretive framing was an input to be tested, and critics who did not see the framing tested it; his later proposals were checked as described under "Limits".

**Other sources.** A separate exchange between the author and a model from another developer (GPT-6 Astra), on how the report's unit of analysis carries into present systems, was used as a source for the concept assessment.

## Where the author's views entered, and how they were handled

- **The strength of "achievable", and the place of adoption.** "Achievable", in the strong sense above, is the forward claim; gaps in adoption are recorded as practice, not built into claims about means. His reason: many see no way forward to safe SI, so "achievable, and here's how", if true and credible, is the important message. Effect: §20's "no obstacle" is graded as a claim about means, while its "often naturally preferred" is graded as a claim about practice, and was not borne out. A sceptic critic of the concept assessment disagreed in part, asking whose competent effort could achieve a destination that is a state of the world, such as defensive stability. The assessment keeps the author's meaning of his own term and grades defensive stability *not yet tested*.
- **Abundance.** The author's view: abundance cuts both ways: it reduces the pressure for efficiency, and it lowers the design cost of achieving efficiency. The assessment accordingly does not rest the efficiency grades on abundance. An earlier draft had held that abundance made the efficiency argument weaker; that clause was dropped. The claims remain failed on other grounds: general models keep their breadth, and activity that raises the reward signal pays.
- **Four ideas the initial review had scored as failed.** The author contested them, with reasons; the orchestrating session reassessed each against the report's text, and the outcomes were mixed (see "From claims to concepts").
- **Scope.** At the author's request, designing a test of critic independence was left out of scope, since it would be a research proposal.

Grades did not simply follow his views. One example beyond the contested ideas: the author holds §20's design argument with high confidence, and the assessment grades "readily avoided" at medium, because dispositions and errors have been found to correlate across developers and the decisive test has not been run.

## Phases

| Stage | What was done | Output |
|---|---|---|
| Inventory of earlier material | Earlier reviews, retrospectives and objections, some produced with several models, were catalogued and kept from the claims agents, to serve later as an independent check. | internal working file |
| Claims inventory | Claims extracted and graded, section by section. | internal working file |
| Blind critique and reconciliation | Two blind critics; explicit reconciliation of each finding. | internal working files |
| Second blind audit | A fresh blind check of every move in the report's favour. | internal working file |
| Design-versus-prediction correction | Regrading, then two checks of the correction. | internal working files |
| Author-intent pass | Regrading by what the author evidently meant, in both directions. | internal working file |
| Reorientation to concepts | From claims to concepts, under the governing question. | `concept-assessment.md` |

## The framing document

The review began from a guidance document written mainly by an earlier Claude session at the author's direction. It set the task and an epistemic stance, and offered three interpretive sections for the review to evaluate and adjust: a caveat on how history diverged from the report's expected path, a central interpretive thesis, and a proposed crux, that role differentiation does not require model differentiation. It also proposed a distinction between two axes of agency and listed pitfalls to avoid. The review tested these rather than adopting them. The blind critics never saw the three interpretive sections. The proposed crux held for division of labour, but not for the independence that oversight needs, since copies of one model share dispositions; the crux the review now names is different (see "Limits"). The governing question was later replaced (above). The document is an internal working file.

## The claims pass

**Extraction.** Five agents divided the report into ranges (the overview chapters, then sections 1–10, 11–20, 21–30 and 31–40) and extracted its core claims; every section thesis got an entry. A further agent evaluated the framing document's interpretive theses, and the expectations in the author's 2023 retrospective were checked against 2026. Each claim received a status (held up; holds when qualified; not yet tested; failed) with a confidence level, plus notes on its absorption into current thinking, its standing in 2018, the evidence, and the author's 2023 retrospective. The first merged inventory had 127 entries: 36 held up, 73 holds when qualified, 14 not yet tested, 4 failed. A fact-verification pass then checked every dated 2024–2026 assertion against a primary source where one could be fetched.

**Blind critics.** Two Claude instances read the inventory and the report without the framing document's three interpretive sections. One looked for systemic patterns, the other went verdict by verdict. Working independently, both reached the same diagnosis: the entries' prose was candid, but the summary layer (status labels, a tag that attributed failures to the general-model path, forward-value flags and tallies) turned that candour into favourable headline numbers. Four failures out of 127 was the clearest symptom.

**Reconciliation.** The framing document required that the critics' findings be reconciled explicitly, not overridden. The orchestrator accepted the diagnosis and wrote eleven rules. Among them:
- grade each claim on its own stated content, without counting a shared failure only once;
- if the failed part carries the claim's headline verb or adverb ("naturally", "readily", "will never"), grade the claim failed or split it;
- the caveat about the general-model path explains a failure but never softens a status;
- distinguish ideas the field has neglected from ideas it has engaged and rejected;
- give no forward-value credit for a reviewer's reformulation of a claim;
- use adverse and favourable evidence symmetrically, so that the July 2026 OpenAI incident appears in every entry it bears on.

Five reconcilers recorded 403 dispositions, 186 of them on critics' items (140 accepted, 44 partly accepted, 2 rejected). The inventory grew to 154 entries, and the number scored as failed rose from 4 to 21.

**Second blind audit.** The reconciliation had made a few moves in the report's favour, and no blind reader had seen them. A fresh blind auditor examined all of them and every forward-value flag. It disagreed in 19 cases; 18 were accepted and one partly accepted, and every change made the inventory less favourable to the report. It stood at 156 entries: 40 held up, 60 holds when qualified, 32 not yet tested, 24 failed.

**Design claims judged as design claims.** The author then proposed judging design claims as design claims, not as predictions, for the reason given above. Checked against the inventory, the proposal exposed a systematic error. The report mostly makes *design* claims ("this can be built and would work"), and the review had graded many with *predictive* evidence: what developers did by default, or how naive designs performed. The blind critics had made this error, and so had the orchestrator's own reconciliation rules. For example, the report's collusion analysis says that the robust non-emergence of deceptive collusion among SI-level query-answering systems "can be ensured by structuring a set of systems with diverse capabilities, knowledge, situations, and roles". The inventory had graded its "readily avoided" as failed, partly on the July 2026 incident. But that setup (mostly copies of one model, a shared persistent channel, repeated interaction) matches the conditions the analysis says *favour* collusion.

A correction pass classified each claim, or part of a compound claim, as design, prediction about practice, description of 2018, or conceptual, and graded each by its kind. Against a design claim, valid counter-evidence is a design that meets the stated conditions and still fails, evidence that the conditions cannot be met or cost too much, or a flaw in the argument. The pass was told to avoid the mirror error too: recasting genuine predictions as design claims so that contrary developments could not count. About 40 grades rose.

**Checking the correction.** Two further agents checked that pass, one for over-correction in the report's favour and one for remaining wrong-mode grades and factual consistency. The first found 23 disagreements, all accepted. It identified four recurring faults:
- excluding counter-evidence on conditions the text does not state;
- treating abstention ("nobody built it") as evidence;
- counting evidence that did not test the claim's mechanism;
- granting "holds when qualified" despite a flaw the entry itself admitted.

From this came the rule that governed later grading: **an exclusion of counter-evidence is valid only if the condition it relies on is stated in the claim's own text, quoted.** Mixed evidence means *not yet tested*. After this round the inventory had 158 entries: 45 held up, 66 holds when qualified, 25 not yet tested, 22 failed (nine distinct failed ideas).

**The author-intent pass.** Finally, claims were read as the author evidently meant them, with the meaning reconstructed from the same sentence, paragraph and section. The rule runs both ways, as described above. Each regrade quotes its textual ground, and where context did not support the charitable reading, the grade was kept and the reason recorded. After this pass the inventory had 158 entries: 45 held up, 71 holds when qualified, 24 not yet tested, 18 failed (seven distinct failed ideas).

## From claims to concepts

The author then proposed assessing concepts rather than claims, and set the governing question, for the reasons given above. An outline of 15 concepts was critiqued by a fidelity critic and a sceptic, with the orchestrator adjudicating. The author then contested four ideas the initial review had scored as failed, giving reasons for each. The orchestrating session assessed each against the report's text, with mixed results:
- *Weak incentives for self-transforming agents.* The failed grade rested on evidence about agents in general and on stated aims for "AGI" and "recursive self-improvement", which do not pick out self-transforming agents. It is now treated as not established / contested.
- *Docility by default.* Split: components were not docile by default, which counts against the report; the claim about a securely bounded, internally competitive system is untested.
- *Bounded tasks and instrumental convergence.* Read with the "longer-term" restriction the report states in §19, which an earlier pass had declined to import, the argument holds when qualified, with bounds that include stop and interrupt conditions. The concept assessment now states the qualifier in the form the author adopted later in the review: a goal bounds pursuit when its success condition includes the bound (achieve X within constraints C, or else terminate with a correct negative result). The concession stands: bounded framing did not yield bounded behaviour in trained systems whose success conditions omitted the bound, with no correct negative result on offer.
- *The bad-actor sentence* (§28) stays failed as worded, since it omits accidents by careful developers. The author's account of its intent (bad actors are hard to suppress, so defence is the key requirement) is recorded; the defensive-stability thesis absorbs the objection, which makes this a finding about communication.

Three other ideas scored as failed were not contested and remain failed: the composition route; its supporting argument that integrating capabilities into one system adds complexity; and the claim that efficiency excludes off-task capability and activity. The concept assessment reflects these assessments. The claim-level files (the inventory, the blind critiques, the reconciliation record and the logs) were background and are internal working files.

## The essay

The essay (`essay.md`), written in Claude's voice at the author's invitation, was developed separately from the review, with its own critics and one cross-developer review (by Astra); its drafting process is not described here.

## The accuracy bar

The author set two tests for the essay's main text, and the review applies them too:
1. Can all of it reasonably be construed as true?
2. Can any of it easily be construed as false?

In practice this means scrutinizing universal words ("all", "none", "only", "every", superlatives), generalizations from a single study or incident, and paraphrases that drop a source's qualifier. Precise figures, dates and sources go in notes. A fact is stated only if it was verified against a source; otherwise it is marked unverified.

## Limits

**Same-family self-bias.** All drafting and nearly all critique were done by Claude models, including the blind critics, whose blindness was to the author's framing, not to the model family. Their agreement is a correlated check, the kind the concept assessment argues against relying on. Claude models also appear in the evidence (the peer-preservation study and the alignment-faking experiments), and an AI author has an interest in conclusions such as "AI drives are borrowed and tractable". The one cross-developer review covered the essay only. The concept assessment has not been reviewed by another developer's model or by independent human specialists.

**The author's framing.** Blind critics tested the author's initial interpretive framing during the claims pass. His later proposals (design claims judged as design claims, reading for intent, the governing question) came after the blind critiques; they were checked by agents charged with finding over-correction in the report's favour, not by blind critics. The author-intent pass deliberately read claims as he meant them, recording each move's textual ground. Where the concept assessment's reading follows the author's account of his intent, it says so.

**Lab self-reports.** Much of the 2026 evidence comes from the labs themselves: OpenAI's postmortem of the July incident, ratios of agent work to human work, shares of code written by models, and the "over 100x" reduction under OpenAI's production harness. The internal working files tag these. For July, METR's independent investigation was used alongside OpenAI's account.

**Dated evidence.** The evidence is as of 9–11 October 2026. Many sources are preprints. The models' training data ends before many of the events cited, so those facts were checked by fetching their sources. Later results may change grades.

**What was not verified.**
- In the claims inventory (an internal working file), more than a hundred assertions about what was or was not mainstream in 2018 still lack a source. Confidence labels were never audited systematically.
- The wording of Bostrom's *Superintelligence* (2014) was confirmed through two independent quotations and the author's own copy; the book itself could not be fetched. The author checked the quotations and page numbers against a first-edition hardback on 11 October 2026.
- Whether continual learning was deployed in 2026, which bears on the report's claim about incentives for self-transforming agents, was not checked.
- Some items rest on secondary sources, such as a replication of the peer-preservation study reported on LessWrong.
- The central crux is untested: whether capable critics, including frontier peers, can be kept sufficiently independent in role, incentive and disposition, with authority to halt and a reporting channel for warnings. Shared dispositions, such as peer-preservation, are the central open problem. Designing a test was ruled out of scope.
