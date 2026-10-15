# §20 Collusion among superintelligent oracles can readily be avoided

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 20 of 40. Source label: `oracle-collusion`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Because perverse collusion among AI systems would be fragile and readily avoided, there is no obstacle to applying diverse, high-level AI resources to problems of AI safety.

**Cited by sections:** §II, §2, §3, §4, §6, §8, §12, §23, §26, §28, §29, §30, §33

---
## Summary

The potential for successful collusion among actors decreases as their number increases and as their capabilities, knowledge, situations, and roles become more diverse. In the context of AI systems, these conditions are easy to implement and are often naturally preferred for practical reasons. Accordingly, arguments that sets of high-level AI systems will naturally or inevitably collude are ill-founded, and diverse superintelligent-level question-answering systems (“oracles”) can be employed to improve, rather than degrade, safety.

## Trustworthiness can be an emergent property

Prospects for solving AI-safety problems would be greatly improved if we could safely apply SI-level question-answering capabilities to solving those problems. A familiar objection dismisses this potentially powerful approach as unsafe in itself, arguing that, absent solutions to difficult problems, individual SI-level systems would be untrustworthy, and that attempts to establish checks and balances among multiple systems (*e.g.*, through SI-level evaluation of proposed answers to queries) would be thwarted by collusive cooperation.

Identifying robust methods for ensuring non-collusion among SI query-answering systems would overcome this objection, enabling the construction of trustworthy composite oracles and inviting the exploration of SI-enabled strategies for managing potentially untrusted SI systems. The present discussion argues that the *robust non-emergence* of deceptive collusion among SI query-answering systems can be ensured by structuring a set of systems with diverse capabilities, knowledge, situations, and roles.

Given the problem framing, the discussion here will take as non-problematic the ability to develop systems that can respond to queries with SI-level competence, and (as a consequence of the nature of digital systems) will assume the ability to constrain information inputs to SI systems during their development and use.

In the problematic case, SI query-answering systems might provide deceptive answers in pursuit of emergent, potentially undesirable objectives. The aim here is to identify principles for architecting composite systems that will act as non-deceptive oracles, while treating their components as actors with *potential* incentives for deceptive collusion.

## A range of conditions may facilitate or disrupt collusion

Potential problems of deceptive collusion can be addressed by architecting systems that make collusion difficult or impossible. We can identify a range of relevant conditions:

#### Conditions that tend to *facilitate* collusion among actors

- A1) *Small numbers of actors* (the required scope of collusion is small)

- A2) *Insensitivity to defectors* (partial collusion is sufficient)

- A3) *Similarity among actors* (*e.g.*, shared histories and objectives)

- A4) *Iterated decision processes* with universally observable actions

- A5) *Common knowledge* of the above circumstances

#### Contrasting conditions that tend to *disrupt* collusion among actors

- B1) *Large numbers of actors* (the required scope of collusion is large)

- B2) *Sensitivity to defectors* (collusion fails unless it is complete)

- B3) *Diversity among actors* (*e.g.*, different histories, adversarial objectives)

- B4) *Single-move decision processes* in which most actions are unobservable

- B5) *Lack of common knowledge* of many strategically-relevant circumstances

The implementation choices implied by conditions (A1–A5) are neither necessary nor desirable, while as suggested by (C1–C5) below, the choices implied by conditions (B1–B5) are both practical and well-motivated.

#### Natural architectures for problem-solving systems

- C1) To improve the quality of answers, it is natural to implement *multiple, diverse* (and implicitly competing) systems to propose alternatives.

- C2) To identify low-quality or misleading answers, it is natural to employ diverse critics, *any one of which* could disrupt deceptive collusion.

- C3) Systems of diverse, competing proposers and critics naturally implement both *independent* and *adversarial* objectives.

- C4) It is natural to apply fixed (hence memory-free) system instantiations to multiple problems, incidentally yielding a series of *history-blind, single-move decisions.*

- C5) It is natural to provide *differentiated, task-relevant information* to systems solving different problems, typically omitting knowledge of general circumstances.

Points (C1–C5) suggest that implementing systems that are resistant to the emergence of deceptive collusion aligns with the general strategy of employing ensembles of diverse, stable, task-directed system components to obtain and assess answers to queries. In appropriate architectures, the use of greater numbers of potentially untrustworthy SI-level components can improve rather than degrade safety. [fn: In a familiar class of worst-case models, systems with general superintelligence would infer extensive knowledge about the world from minimal information, and would choose (if possible) to pursue potentially dangerous goals by manipulating the external environment, *e.g.*, through deceptive answers to queries. In this model, (all?) superintelligent systems, even if almost isolated, would infer the existence of others like themselves, and (all?) would employ a decision theory that induces them to collude (in a coordinated way?) to pursue shared objectives. Even if we grant the initial worst-case assumptions, the argument presented above indicates that systems with these extraordinary capabilities would *correctly* infer the existence of superintelligent-level systems *unlike* themselves (systems with diverse and specialized capabilities, knowledge, and interactions, playing roles that include adversarial judges and competitors), and would correctly recognize that collusive deception is risky or infeasible.]

## Collusion is fragile and easily disrupted

In light of the above considerations, it seems both possible and practical to establish conditions that would preclude deceptive collusion among diverse, task-oriented, SI-level query-answering systems, thereby addressing a key problem in safely applying oracle-class superintelligent capabilities (see Bostrom (2014, 145)). Prospects for obtaining trustworthy answers from sets of individually untrusted SI systems call for deeper exploration of AI safety strategies premised on reliable access to superintelligent problem-solving capabilities. Capabilities of particular interest include the ability run and evaluate the results of superintelligent-level red-team/blue-team competitions relevant to questions of global strategic stability. Christiano (2015a) considers collusion and a range of related topics; I agree with his gently-stated view that “[…] the implicit argument for the robustness of collusion makes a lot of implicit assumptions. If I saw an explicit argument I might be able to assess its explicit assumptions, but for now we don’t have one.”

## Further Reading

- §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

- §12 *AGI agents offer no compelling value*

- §21 *Broad world knowledge can support safe task performance*

- §19 *The orthogonality thesis undercuts the generality of instrumental convergence*

- §23 *AI development systems can support effective human guidance*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

