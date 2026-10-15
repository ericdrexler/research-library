# §6 A system of AI services is not equivalent to a utility maximizing agent

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 6 of 40. Source label: `not-maximizers`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** The conditions for von Neumann–Morgenstern rationality do not imply that *systems composed of AI services* will act as utility-maximizing agents, hence the design space for manageable superintelligent-level systems is broader than often supposed.

**Cites sections:** §2 *Standard definitions of “superintelligence” conflate learning with competence*; §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*; §14 *The AI-services model brings ample risks*; §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*; §19 *The orthogonality thesis undercuts the generality of instrumental convergence*; §20 *Collusion among superintelligent oracles can readily be avoided*; §21 *Broad world knowledge can support safe task performance*; §22 *Machine learning can develop predictive models of human approval*; §32 *Unaligned superintelligent agents need not threaten world stability*; §35 *Predictable aspects of future knowledge can inform AI safety strategies*

**Cited by sections:** §II, §4

---
## Summary

Although a common story suggests that any system composed of rational, high-level AI agents should (or must?) be regarded as a single, potentially powerful agent, the case for this idea is extraordinarily weak. AI service providers can readily satisfy the conditions for VNM rationality while employing knowledge and reasoning capacity of any level or scope. Bostrom’s Orthogonality Thesis implies that even VNM-rational, SI-level agents need not maximize broad utility functions, and as is well known, *systems composed of rational agents* need not maximize any utility function at all. In particular, systems composed of competing AI service providers cannot usefully be regarded as unitary agents, much less as a unitary, forward-planning, utility-maximizing AGI agent. If, as seems likely, much of the potential solution-space for AI safety requires affordances like those in the AI-services model, then we must reconsider long-standing assumptions regarding the dominance of utility-maximizing AI agents.

## Systems of SI-level agents have been assumed to act as a single agent

In informal discussions of AI safety, it been widely assumed that, when considering a system comprising rational, utility-maximizing AI agents, one can (or should, or even *must*) model them as a single, emergent agent. This assumption is mistaken, and worse, impedes discussion of a range of potentially crucial AI safety strategies. To understand how we could employ and manage systems of rational agents, we can (without loss of generality) start by considering individual systems (“service providers”) that act as rational agents.

## Individual service providers can be modeled as individual agents

The von Neumann-Morgenstern expected-utility theorem shows that, if an agent meets a set of reasonable conditions defining rational behavior, the agent must choose actions that maximize the expected value of some function that assigns numerical values (utilities) to potential outcomes. If we consider a system that provides a service to be “an agent”, then it is at least reasonable to regard VNM rationality as a condition for optimality.

## Trivial agents can readily satisfy the conditions for VNM rationality

To *manifestly violate* the conditions for VNM rationality, an agent must make choices that are incompatible with any possible utility function. Accordingly, VNM rationality can be a trivial constraint: It is compatible, for example, with a null agent (that takes no actions), with an indifferent agent (that values all outcomes equally), and with any agent that acts only once (and hence cannot exhibit inconsistent preferences). Even among non-trivial agents, VNM rationality need not have deep or complex implications for world-oriented behaviors. [Unlike humans](→§5), [fn: §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*.] computational systems do not necessarily (or even by default) [act in an open world](→§20), or [value the “receipt” of “rewards”](→§18), or [accumulate state changes over time](→§2), or [pursue outcomes beyond the completion of an immediate, atomic task](→§19).

## Trivially-rational agents can employ reasoning capacity of any scope

Predictive models are services that can provide building blocks for active AI services. Potential predictions include:

|                |     |                                                   |
|---------------:|:---:|:--------------------------------------------------|
| Text, language |  →  | [Predicted human translation](→§21)  |
|  Present state |  →  | Predicted state                                   |
|   Agent, State |  →  | Predicted action                                  |
|  Action, State |  →  | Predicted outcome                                 |
|        Outcome |  →  | [Predicted human approval](→§22) |

The archetypical predictive model acts as a fixed function (*e.g.*, a translator of type T :: string → string). In each instance above, greater knowledge and reasoning capacity can improve performance; and in each instance, “actions” (function applications) may be judged by their external instrumental value, but cannot themselves violate the conditions for VNM rationality. As suggested by the examples above, fixed predictive models can encapsulate intelligence for active applications: For example, a system might drive a car to a user-selected destination while employing SI-level resources that inform steering decisions by predicting human (dis)approval of predicted outcomes.

## High intelligence does not imply optimization of broad utility functions

Bostrom’s (2014, 107) Orthogonality Thesis states that “more or less any level of intelligence can be combined with more or less any final goal”, and it follows that high-level intelligence can be applied tasks of bounded scope and duration that [do not engender convergent instrumental goals](→§19). Note that service-*providers* need not seek to expand their capabilities: This is a task for service *developers,* while the service-developers are themselves *providers* of service-development services (the implied regress is loopy, not infinite).

## Systems composed of rational agents need not maximize a utility function

There is no canonical way to aggregate utilities over agents, and game theory shows that interacting sets of rational agents need not achieve even Pareto optimality. Agents can compete to perform a task, or can perform [adversarial tasks such as proposing and criticizing actions](→§20); from an external client’s perspective, these uncooperative interactions are features, not bugs (consider the growing utility of [generative adversarial networks](https://scholar.google.co.uk/scholar?as_ylo=2017&q=generative+adversarial+networks&hl=en&as_sdt=0,5) [fn: <https://scholar.google.co.uk/scholar?as_ylo=2017&q=generative+adversarial+networks&hl=en&as_sdt=0,5>]). Further, *adaptive* collusion can be cleanly avoided: Fixed functions, for example, cannot negotiate or adapt their behavior to align with another agent’s purpose.

In light of these considerations, it would seem strange to think that sets of AI services (even SI-level services) would necessarily or naturally collapse into utility-maximizing AI agents.

## Multi-agent systems are *structurally* inequivalent to single agents

There is, of course, an even more fundamental objection to drawing a boundary around a set of agents and treating them as a single entity: In interacting with a set of agents, one can choose to communicate with one or another (*e.g.*, with an agent or its competitor); if we assume that the agents are in effect a single entity, we are assuming a constraint on communication that does not exist in the multi-agent model. The models are fundamentally, structurally inequivalent.

## Problematic AI services need not be problematic AGI agents

Because AI services can in principle be fully general, combinations of services could of course be used to implement complex agent behaviors up to and including those of unitary AGI systems. Further, because evolutionary pressures can engender the emergence of powerful agents from lesser cognitive systems (*e.g.*, our evolutionary ancestors), the [unintended emergence of problematic agent behaviors in AI systems must be a real concern](→§14).

Unintended, perverse interactions among some sets of service-providers will likely be a routine occurrence, [familiar to contemporaneous researchers as a result of ongoing experience and AI safety studies](→§35). Along this development path, the implied threat model is quite unlike that of a naïve humanity abruptly confronting a powerful, world-transforming AGI agent.

## The AI-services model expands the solution-space for addressing AI risks

The AI-services and AGI-agent models of superintelligence are far from equivalent, and the AI-services model offers a wider range of affordances for structuring AI systems. Distinct, stable [predictive models of human approval](→§22), together with natural applications of [competing and adversarial AI services](→§20), can provide powerful tools for addressing traditional AI safety concerns. If, as seems likely, much of [the potential solution-space for addressing AI x-risk](→§32) requires affordances within the AI-services model, then we must reconsider long-standing assumptions regarding the dominant role of utility-maximizing agents, and expand the AI-safety research portfolio to embrace new lines of inquiry.

## Further Reading

- §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

- §11 *Potential AGI-enabling technologies also enable comprehensive AI services*

- §14 *The AI-services model brings ample risks*

- §20 *Collusion among superintelligent oracles can readily be avoided*

- §19 *The orthogonality thesis undercuts the generality of instrumental convergence*

- §21 *Broad world knowledge can support safe task performance*

- §32 *Unaligned superintelligent agents need not threaten world stability*

