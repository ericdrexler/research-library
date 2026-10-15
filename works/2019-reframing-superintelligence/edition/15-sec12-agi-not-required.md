# §12 AGI agents offer no compelling value

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 12 of 40. Source label: `agi-not-required`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Because general AI-development capabilities can provide stable, comprehensive AI services, there is no *compelling, practical motivation* for undertaking the more difficult and potentially risky implementation of self-modifying AGI agents.

**Cites sections:** §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*; §15 *Development-oriented models align with deeply-structured AI systems*; §20 *Collusion among superintelligent oracles can readily be avoided*

**Cited by sections:** §II, §1, §2, §4, §5, §11, §14, §17, §21, §28, §29, §32

---
## Summary

Practical incentives for developing AGI agents appear surprisingly weak. Providing comprehensive AI services calls for diverse, open-ended AI capabilities (including stable agent services), but their development does not require agents in any conventional sense. Although both the AGI and AI-service models can deliver general capabilities, their differences have a range of consequences; for example, by enabling access to stable AI components, competing implementations, and adversarial checking mechanisms, the CAIS model offers safety-relevant affordances that the classic AGI model does not. Both the CAIS and AGI models propose recursive improvement of AI technologies, yet they differ in their accessibility: While CAIS models anticipate accelerating R&D automation that extends conventional development methodologies, AGI models look toward conceptual breakthroughs to enable self-improvement and subsequent safe application. Because AI development services could be used to implement AGI agents, the CAIS model highlights the importance of classic AGI-safety problems, while access to SI-level services could potentially mitigate those same problems.

## Would AGI development deliver compelling value?

It is widely believed that the quest to maximize useful AI capabilities will necessarily culminate in artificial general intelligence (AGI), which is taken to imply AI agents that would be able to self-improve to a superintelligent level, potentially gaining great knowledge, capability, and power to influence the world. It has been suggested AGI may be effectively unavoidable either because:

1.  Self-improving AI may almost unavoidably generate AGI agents, or

2.  AGI agents would provide unique and compelling value, making their development almost irresistibly attractive.

However, the non-agent-based undercuts claim (1), while the prospective result of ongoing R&D automation, general AI development services, undercuts claim (2).

## AI systems deliver value by delivering services

In practical terms, we value potential AI systems for what they could do, whether driving a car, designing a spacecraft, caring for a patient, disarming an opponent, proving a theorem, or writing a symphony. Scientific curiosity and long-standing aspirations will encourage the development of AGI agents with open-ended, self-directed, human-like capabilities, but the more powerful drives of military competition, economic competition, and improving human welfare do not in themselves call for such agents. What matters in practical terms are the concrete AI services provided (their scope, quality, and reliability) and the ease or difficulty of acquiring them (in terms of time, cost, and human effort).

## Providing diverse AI services calls for diverse AI capabilities

Diverse AI services resolve into diverse tasks, some shared across many domains (*e.g.*, applying knowledge of physical principles, of constraints on acceptable behavior, *etc.*), while other tasks are specific to a narrower range of domains. Reflection on the range of potential AI services (driving a car, proving a theorem…) suggests the diversity of underlying AI tasks and competencies. We can safely assume that:

- No particular AI service will require all potential AI competencies.

- Satisfying general demands for new AI services will require a general ability to expand the scope of available competencies.

## Expanding AI-application services calls for AI-development services

Developing a new AI service requires understanding its purpose (guided by human requests, inferred preferences, feedback from application experience, *etc.*), in conjunction with a process of design, implementation, and adaptation that produces and improves the required AI capabilities. Capability-development tasks can be cast in engineering terms: They include function definition, design and implementation, testing and validation, operational deployment, in-use feedback, and ongoing upgrades.

## The AGI and CAIS models organize similar functions in different ways

In the CAI-services model, capability-development functions are explicit, exposed, and embodied in AI system components having suitable capacities and functional relationships. In the CAIS model, AI-enabled products are distinct from AI-enabled development systems, and the CAIS model naturally emerges from incremental R&D automation.

In the classic AGI-agent model, by contrast, capability-development functions are implicit, hidden, and embodied in a single, conceptually-opaque, self-modifying agent that pursues (or is apt to pursue) world-oriented goals. Thus, capability development is internal to an agent that embodies both the development mechanism and its product. Implementation of the AGI model is widely regarded as requiring conceptual breakthroughs.

## The CAIS model provides additional safety-relevant affordances

The CAIS model both exemplifies and naturally produces [deeply structured AI systems](→§15) based on identifiable, functionally-differentiated components. Structured architectures provide affordances for both component- and system-level testing, and for the re-use of stable, well-tested components (*e.g.*, for vision, motion planning, language understanding…) in systems that are adapted to new purposes. These familiar features of practical product development and architecture can contribute to reliability in a conventional sense, but also to AI safety in the context of superintelligent-level competencies.

In particular, the CAIS model offers component and system-level affordances for structuring information inputs and retention, mutability and stability, computational resource allocation, functional organization, component redundancy, and internal process monitoring; these features distance the CAIS from opaque, self-modifying agents, as does the fundamental separation of AI products from AI development processes. In the CAIS context, components (*e.g.*, predictive models of human preferences) can be tested separately (or in diverse testbed contexts) without the ambiguities introduced by embedding similar functionality in systems with agent-level goals and potential incentives for deception.

> *Constraining AI systems through external, structural affordances:*
>
> **Knowledge metering** to bound information scope
>
> **Model distillation** to bound information quantity
>
> **Checkpoint/restart** to control information retention
>
> **Focused curricula** to train task specialists
>
> **Specialist composition** to address complex tasks
>
> **Optimization** applied as a constraint

> **Figure 5.** AI development processes provide affordances for constraining AI systems that can be effective without insights into their internal representations. Points of control include information inputs, model size, (im)mutability, loss functions, functional specialization and composition, and [optimization pressures](→§8) that tend to become sharper as implementation technologies improve. *(Adapted from Drexler (2015))*
> *(Text-only figure; content reproduced above.)*

## The CAIS model enables competition and adversarial checks

In developing complex systems, it is common practice to apply multiple analytical methods to a proposed implementation, to seek and compare multiple proposals, to submit proposals to independent review, and where appropriate, to undertake adversarial red-team/blue-team testing. Each of these measures can contribute to reliability and safety, and each implicitly depends on the availability of independent contributors, evaluators, testers, and competitors. Further, each of these essentially adversarial services scales to the superintelligent limit.

In the CAIS model, it is natural to produce diverse, independent, task-focused AI systems that provide adversarial services. By contrast, it has been argued that, in the classic AGI model, strong convergence (through shared knowledge, shared objectives, and strong utility optimization under shared decision theories) would render multiple agents effectively equivalent, undercutting methods that would rely on their independence. Diversity among AI systems is essential to providing independent checks, and can enable the [prevention of potential collusive behaviors](→§20).

## The CAIS model offers generic advantages over classic AGI models

- *CAIS (like AGI)* encompasses recursive improvement of AI technologies, and hence could enable full-spectrum AI services that operate at a superintelligent level.

- *CAIS (but not AGI)* grows out of incremental R&D automation within the architecture of established development methodologies.

- *AGI (but not CAIS)* calls for conceptual breakthroughs to enable both implementation and subsequent safe application.

- *CAIS (but not AGI)* offers structural affordances for increasing reliability and safety, including diverse adversarial checks that scale to superintelligent systems.

## CAIS affordances mitigate but do not solve AGI-control problems

Because systems that can implement AI functionality at a superintelligent level can presumably be used to implement classic AGI systems, CAI services would lower barriers to the development of AGI. Given the widespread desire to realize the dream of AGI, it seems likely that AGI will, in fact, be realized unless actively prevented. Nonetheless, in a world potentially stabilized by security-oriented applications of superintelligent-level AI capabilities, prospects for the emergence of AGI systems may be less threatening. [Superintelligent-level aid in understanding and implementing solutions to the AGI control problem](→§20) and could greatly improve our strategic position.

There is no bright line between safe CAI services and unsafe AGI agents, and AGI is perhaps best regarded as a potential branch from an R&D-automation/CAIS path. To continue along safe paths from today’s early AI R&D automation to superintelligent-level CAIS calls for an improved understanding of the preconditions for AI risk, while for any given level of safety, a better understanding of risk will widen the scope of known-safe system architectures and capabilities.

The analysis presented above suggests that CAIS models of the *emergence of superintelligent-level AI capabilities,* including AGI, should be given substantial and arguably predominant weight in considering questions of AI safety and strategy.

## Further Reading

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §7 *Training agents in human-like environments can provide useful, bounded services*

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §15 *Development-oriented models align with deeply-structured AI systems*

- §23 *AI development systems can support effective human guidance*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

