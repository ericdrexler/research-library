# §19 The orthogonality thesis undercuts the generality of instrumental convergence

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 19 of 40. Source label: `orthogonality-undercuts`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** If any level of intelligence can be applied to any goal, then superintelligent-level systems can pursue goals for which the pursuit of the classic instrumentally-convergent subgoals would offer no value.

**Cites sections:** §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

**Cited by sections:** §II, §6, §7, §30

---
## Summary

Bostrom (2014) presents carefully qualified arguments regarding the “orthogonality thesis” and “instrumental convergence”, but the scope of their implications has sometimes been misconstrued. The orthogonality thesis proposes that any level of intelligence can be applied to any goal (more or less), and the principle of instrumental convergence holds that a wide range of goals can be served by the pursuit of subgoals that include self preservation, cognitive enhancement, and resource acquisition. This range of goals, though wide, is nonetheless limited to goals of indefinite scope and duration. The AI-services model suggests that essentially all practical tasks are (or can be) directly and naturally bounded in scope and duration, while the orthogonality thesis suggests that superintelligent-level capabilities can be applied to such tasks. At a broad, systemic level, tropisms toward general instrumental subgoals seem universal, but such tropisms do not imply that a diffuse system has the characteristics of a willful superintelligent agent.

## *The thesis:* Any level of intelligence can be applied to any goal (more or less)

The orthogonality thesis (Bostrom 2014, 107) proposes that intelligence and final goals are orthogonal: “[…] more or less any level of intelligence can be combined with more or less any final goal.”

A natural consequence of the orthogonality thesis is that intelligence of any level can be applied to goals that correspond to tasks of bounded scope and duration.

## A wide range of goals will engender convergent instrumental subgoals

As Marvin Minsky noted in a conversation *ca.* 1990, a top-level goal of narrow scope (*e.g.*, playing the best possible game of chess) can be served by a subgoal of enormous scope (*e.g.*, converting all accessible resources into chess-playing machinery). The instrumental convergence (IC) thesis (Bostrom 2014, 109) generalizes this principle; it describes instrumental values that engender subgoals that, if accomplished,

> […] would increase the chances of the agent’s goal being realized for a wide range of final goals and a wide range of situations, implying that these instrumental values [or (sub)goals] are likely to be pursued by a broad spectrum of situated intelligent agents.

The explicitly considered IC subgoals are:

- ***Self preservation*** (to pursue long-term goals, an agent must continue to exist)

- ***Goal-content integrity*** (to pursue long-term goals, an agent must maintain them)

- ***Cognitive enhancement*** (gaining intelligence would expand an agent’s capabilities)

- ***Technological perfection*** (developing better technologies would expand an agent’s capabilities)

- ***Resource acquisition*** (controlling more resources would expand an agent’s capabilities)

Recognizing the broad scope of IC subgoals provides insight into potential behaviors of a system that pursues goals with a “superintelligent will” (Bostrom 2014, 105).

## Not all goals engender IC subgoals

As formulated, the IC thesis applies to “a wide range [implicitly, a limited range] of final goals”, and the subsequent discussion (Bostrom 2014, 109) suggests a key condition, that “an agent’s final goals concern the future”. This condition is significant: Google’s neural machine translation system, for example, has no goal beyond translating a given sentence, and the scope of this goal is independent of the level of intelligence that might be applied to achieve it.

In performing tasks of bounded scope and duration, the pursuit of longer-term IC subgoals would offer no net benefit, and indeed, would waste resources. Optimization pressure on task-performing systems can be applied to suppress not only wasteful, off-task actions, but off-task modeling and planning. [→ §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*]

## Not all intelligent systems are goal-seeking agents in the relevant sense

As formulated above, the IC thesis applies to “situated agents”, yet in many instances intelligent systems that perform tasks are neither agents nor situated in any conventional sense: Consider systems that prove theorems, translate books, or perform a series of design optimizations. Further, agents within the scope of the IC thesis are typically modeled as rational, utility-directed, and concerned with goals of broad scope, yet even situated agents need not display these characteristics (consider System 1 decision-making in humans).

## Comprehensive services can be implemented by systems with bounded goals

The AI-services model invites a functional analysis of service development and delivery, and that analysis suggests that practical tasks in the CAIS model are readily or naturally bounded in scope and duration. For example, the task of *providing a service* is distinct from the task of *developing a system to provide that service,* and tasks of both kinds must be completed without undue cost or delay. Metalevel tasks such as consulting users to identify application-level tasks and preferences, selecting and configuring systems to provide desired services, supplying necessary resources, monitoring service quality, aggregating data across tasks, and upgrading service-providers are likewise bounded in scope and duration. This brief sketch outlines a structure of generic, bounded tasks that could, by the orthogonality thesis, be implemented by systems that operate at a superintelligent level. It is difficult to identify bounded (*vs.* explicitly world-optimizing) human goals that could more readily be served by other means.

## IC goals naturally arise as tropisms and as intended services

The IC thesis identifies goals that, although though not of value in every context, are still of value at a general, systemic level. The IC goals arise naturally in an AI-services model, not as the result of an agent planning to manipulate world-outcomes in order to optimize an over-arching goal, but as system-level tropisms that emerge from local functional incentives:

- ***Self preservation:*** Typical service-providing systems act in ways that avoid self-destruction: Self-driving cars are an example, though missiles are an exception. AI systems, like other software, can best avoid being scrapped by providing valuable services while not disrupting their own operation.

- ***Goal-content integrity:*** For AI systems, as with other software, functional (implicitly, “goal”) integrity is typically critical. Security services that protect integrity are substantially orthogonal to functional services, however, and security services enable software upgrade and replacement rather than simply preserving what they protect.

- ***Cognitive enhancement:*** At a global level, AI-supported progress in AI technologies can enable the implementation of systems with enhanced levels of intelligence, but most AI R&D tasks are more-or-less orthogonal to application-level tasks, and are bounded in scope and duration.

- ***Technological perfection:*** At a global level, competition drives improvements in both hardware and software technologies; on inspection, one finds that this vast, multi-faceted pursuit resolves into a host of loosely-coupled R&D tasks that are bounded in scope and duration.

- ***Resource acquisition:*** AI systems typically acquire resources by providing value through competitive services (or disservices such as theft or fraud).

All these goals are pursued today by entities in the global economy, a prototypical diffuse intelligent system.

## Systems with tropisms are not equivalent to agents with “will”

The aggregate results of AI-enabled processes in society would tend to advance IC goals even in the absence of distinct AI agents that meet the conditions of the IC thesis. To regard systemic tropisms as manifestations of a “superintelligent will”, however, would be much like attributing a “will” to a global ecosystem or economy—a potentially useful perspective that does not reflect an equivalence.

The analogy between *tropisms* and *will* invites a “motte and bailey argument” that wrongly attributes the properties of willful rational agents to *all* systems in which strong aggregate capabilities provide wide-ranging services. Similarly, to argue that a diffuse system would itself undertake actions to *become* a willful agent in order to pursue IC subgoals is essentially circular.

## Further Reading

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

- §12 *AGI agents offer no compelling value*

- §28 *Automating biomedical R&D does not require defining human welfare*

- §38 *Broadly-capable systems coordinate narrower systems*

