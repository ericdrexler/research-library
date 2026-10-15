# §23 AI development systems can support effective human guidance

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 23 of 40. Source label: `human-guidance`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Advanced, interactive AI development resources could greatly facilitate the use of human guidance in developing safe, high-level AI services.

**Cites sections:** §15 *Development-oriented models align with deeply-structured AI systems*; §16 *Aggregated experience and centralized learning support AI-agent applications*; §20 *Collusion among superintelligent oracles can readily be avoided*; §22 *Machine learning can develop predictive models of human approval*; §35 *Predictable aspects of future knowledge can inform AI safety strategies*

**Cited by sections:** §II, §1, §3, §5, §11, §14, §28, §32

---
## Summary

Prospects for sharply accelerated development of AI technologies raise questions regarding the effectiveness of human guidance. Basic research requires only loosely coupled human guidance; in AI *application* development, by contrast, human guidance is typically essential to the value and safety of products. When exploring challenging, advanced-AI development scenarios, we should consider potential AI-enabled resources and mechanisms that could help us align AI applications with human goals. A non-exhaustive list includes:

- Strong natural language understanding

- Broad models of human approval and disapproval

- Interactive development of task objectives

- Learning from humans through observation

- Large-scale aggregation of experience and supervision

- Routine but cost-sensitive recourse to human advice

- Adversarial, AI-enabled criticism and monitoring

Prospects for AI-supported human guidance suggest that applications of high-level AI could potentially reduce, rather than increase, the challenges of aligning AI applications with human goals.

## Facilitating human guidance is part of the AI-application development task

Facilitating human guidance a key AI service that can improve tradeoffs between AI development speed and human satisfaction. Models of human guidance in which a person confronts “an AGI” *ab initio* appear neither workable nor realistic; more realistic models can instead consider prospects for diverse AI systems that emerge from structured, AI-enabled development processes in which goal-alignment is part of the development task.

## Development tasks include task selection, system design, training, testing, deployment, in-use feedback, and upgrades

Realistic models of AI application development must consider the pervasive, path-dependent structure of actual system development. Systems are composed of components, and development tasks for both systems and components include function definition and system design, then testing, implementation deployment, in-use feedback, and upgrades (typically performed in iterative, looped, overlapping stages). Prospects for successfully applying AI-enabled capabilities to AI system development are best understood in the context of [structured, task-oriented products and development processes](→§15).

## We should assume effective use of natural-language understanding

In considering advanced AI capabilities, should assume that a range of current objectives have been achieved, particularly where we see strong progress today. In particular, *natural-language understanding* (Johnson et al. 2016) can support powerful mechanisms for defining AI tasks and providing feedback on AI-system behaviors. Even imperfect language understanding can be powerful because both large text corpora and interactive communication (potentially drawing on the knowledge and expressive capabilities of many individuals) can help to disambiguate meaning.

## Generic models of human (dis)approval can provide useful priors

In some applications, avoiding undesirable AI behaviors will require a broad understanding of human preferences. Explicit rules and direct human instruction seem inadequate, but (along lines suggested by Stuart Russell (Wolchover 2015)) advanced machine learning could develop [broad, predictive models of human approval and disapproval](→§22) by drawing on large corpora of, for example, news, history, science fiction, law, and philosophy, as well as the cumulative results of imaginative, crowd-sourced challenges. Generic models of human (dis)approval can provide useful priors in defining task-specific objectives, as well as constraints on actions and side-effects.

Note that predicting human approval conditioned on events is distinct from predicting the events themselves. Accordingly, in judging an agent’s potential actions, predictive models of approval may fail to reflect unpredictable, unintended consequences, yet be effective in assessing predicted, intended consequences (of, *e.g.*, misguided or perverse plans).

## Bounded task objectives can be described and circumscribed

Describing objectives is an initial step in systems development, and conventional objectives are bounded in terms of purpose, scope of action, allocated resources, and permissible side-effects. Today, software developed for self-driving cars drives particular cars, usually on particular streets; in the future, systems developed to study cancer biology will perform experiments in particular laboratories, systems developed to write up experimental results will produce descriptive text, AI-architecting systems will propose candidate architectures, and so on. Priors based on [models of human approval](→§22) can help AI development systems suggest task-related functionality, while models of human disapproval can can help development systems suggest (or implement) hard and soft constraints; along lines suggested by Armstrong (2013), these can include minimizing unintended effects that people might regard as important.

## Observation can help systems learn to perform human tasks

For task that humans can perform, human behavior can be instructive, not only with respect to means (understanding actions and their effects), but with respect to ends (understanding task-related human objectives). Technical studies of cooperative inverse reinforcement learning (Hadfield-Menell et al. 2016) address problems of learning through task-oriented observation, demonstration, and teaching, while Paul Christiano’s work (Christiano 2015b) on scalable control explores (for example) how observation and human supervision could potentially be extended to challenging AI tasks while economizing on human effort. Generic predictive models of human approval can complement these approaches by providing strong priors on human objectives in performing tasks while avoiding harms.

## Deployment at scale enables aggregated experience and centralized learning

Important AI services will often entail [large-scale deployments that enable accelerating learning](→§16) from instances of success, failure, and human responses (potentially including criticism and advice). In addition to accelerating improvement across large deployments, aggregated experience and learning can increase the benefit-to-cost ratio of using and teaching systems by multiplying the system-wide value of users’ correcting and advising individual system-instances while diluting the per-user burdens of encountering correctable errors.

## Recourse to human advice will often be economical and effective

Imperfect models of human approval can be supplemented and improved by recourse to human advice. Imperfect models of approval should contain more reliable models of human concern; an expectation of concern together with uncertainty regarding approval could prompt recourse (without overuse) of human advice. Using advice in [learning from aggregated experience](→§16) would further economize the use of human attention.

## AI-enabled criticism and monitoring can strengthen oversight

Concerns regarding perverse planning by advanced AI agents could potentially be addressed by applying comparable AI capabilities to AI development and supervision. In AI development, the aim would be to understand and avoiding the kinds of goals and mechanisms that could lead to such plans; in AI applications, the aim would be to monitor plans and actions and recognize and warn of potential problems (or to intervene and forestall them). This kind of AI-enabled adversarial analysis, testing, monitoring, and correction [need not be thwarted by collusion among AI systems](→§20), even if these systems operate at superintelligent levels of competence.

## AI-enabled AI development could both accelerate application development and facilitate human guidance

Fast AI technology improvement will increase the scope for bad choices and potentially severe risks. Established practice in system development, however, will favor a measure of intelligent caution, informed by [contemporaneous experience and safety-oriented theory and practice](→§35). We can expect the temptation to move quickly by accepting risks to be offset to some extent by improved support for goal-aligned function definition, system design, testing, deployment, feedback, and upgrade.

It is very nearly a tautology to observe that the balanced use of powerful AI development capabilities can reduce the cost of producing safe and reliable AI products. Further, the underlying principles appear to scale to AI development technologies that enable the safe implementation of a full spectrum of AI services with superhuman-level performance. This potential, of course, by no means assures the desired outcome.

## Further Reading

- §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

- §21 *Broad world knowledge can support safe task performance*

- §22 *Machine learning can develop predictive models of human approval*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

- §28 *Automating biomedical R&D does not require defining human welfare*

- §35 *Predictable aspects of future knowledge can inform AI safety strategies*

- §36 *Desiderata and directions for interim AI safety guidelines*

