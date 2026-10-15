# §8 Strong optimization can strongly constrain AI capabilities, behavior, and effects

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 8 of 40. Source label: `strong-optimization`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Strong (even superintelligent-level) optimization can be applied to increase AI safety by strongly constraining the capabilities, behavior, and effects of AI systems.

**Cites sections:** §20 *Collusion among superintelligent oracles can readily be avoided*; §22 *Machine learning can develop predictive models of human approval*; §24 *Human oversight need not impede fast, recursive AI technology improvement*

**Cited by sections:** §II, §3, §9, §11, §12, §19

---
## Summary

Strong “optimization power” has often been assumed to increase AI risks by increasing the scope of a system’s capabilities, yet task-focused optimization can have the opposite effect. Optimization of any system for a task constrains its structure and behavior, implicitly constraining its off-task capabilities: A competitive race car cannot transport a load of passengers, and a bus will never set a land speed record. In an AI context, optimization will tend to constrain capabilities and decrease risks when objectives are bounded in space, time, and scope, and when objective functions assign costs to both resource consumption and off-task effects. Fortunately, these are natural conditions for AI services. Optimizing AI systems for bounded tasks is itself a bounded task, and some bounded tasks (*e.g.*, predicting human approval) can contribute to general AI safety. These considerations indicate that strong, even SI-level optimization can both improve and constrain AI performance.

## Strong optimization power need not increase AI capability and risk

“Optimization power” is widely regarded as a source of both AI capabilities and risks, but this concern is usually expressed in the context of open-ended objectives pursued with weak resource constraints. For tasks with bounded, cost-sensitive objectives, however, increasing optimization can have the opposite effect.

## Strong optimization is a strong constraint

Full optimization of a system with respect to a value function typically yields not only a unique, maximal expected value, but robust constraints on the system itself. In practice, even approximate optimization strongly constrains both the structure and behavior of a system, thereby constraining its capabilities. In physical engineering, a race car cannot transport a load of passengers, and a bus will never set a land speed record; in AI development, an efficient text-translation system will never plan a vehicle path, and an efficient path-planning system will never provide translation services. Because off-task capabilities are costly, they will be excluded by cost-sensitive optimization.

> **Figure 2.** Optimization pressures during AI system development focus resources on tasks and enable further development based on task-focused components.
> *(Image `fig5.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> The diagram shows a left-to-right pipeline of two stacked-box stages connected by block arrows, with a feedback loop running back underneath. At upper left, the heading "Optimization pressures:" labels three downward arrows in the figure that inject pressures into the pipeline.
>
> The first stage is a stack of overlapping rounded-rectangle boxes (indicating multiple parallel instances) labeled "AI-system builders." A downward arrow feeds into this stack carrying the italic labels "Throughput," "Resource efficiency," and "Product-system performance." A wide gray block arrow points rightward from the "AI-system builders" stack to the second stage.
>
> The second stage is likewise a stack of overlapping boxes labeled "Application AI systems." A downward arrow feeds into it carrying the italic labels "Throughput," "Resource efficiency," and "Output quality." A wide gray block arrow points rightward from "Application AI systems" to a bracketed list of outputs on the right: "Steering actions," "Vehicle designs," "Translations," "Stock trades," "Theorems," "AI components," followed by an ellipsis ("…").
>
> From the "AI components" item in that output list, a dashed line runs down and then leftward, back underneath both stages, to a dashed upward-pointing arrow feeding into the "AI-system builders" stack — closing a feedback loop. This return path is labeled in italics "Recursive optimization enablement," indicating that AI components produced by the application AI systems feed back in to build or enable further AI-system builders.

## Optimization of AI systems can reduce unintended consequences

Optimization will tend to reduce risks when task objectives are bounded in space, time, and scope, and when the value-function assigns costs to both resource use and unintended human-relevant effects. With bounded objectives, remote and long-term effects will contribute no value and hence will be unintended, not actively optimized, and likewise for off-task consequences that are local and near-term. Going further, when costs are assessed for resource consumption and unintended, [human-relevant effects](→§22), stronger optimization will tend to actively reduce unwanted consequences (see Armstrong and Levinstein (2017) for a concept of *reduced-impact AI*).

## Strong external optimization can strongly constrain internal capabilities

If the costs of appropriate computational resources are given substantial weight, strong optimization of an AI system can act as a strong constraint on its inputs and model capacity, and on the scope of its mechanisms for off-task inference, modeling, and planning. The weighting of computational-cost components need not reflect external economic costs, but can instead be chosen to shape the system under development.

A major concern regarding strong AI capabilities is the potential for poorly-defined goals and powerful optimization to lead to perverse plans that (for example) act through unexpected mechanisms with surprising side-effects. Optimization to minimize a system’s off-task information, inference, modeling, and planning, however, can constrain the scope for formulating perverse plans, because the planning itself may incur substantial costs or require resources that have been omitted in the interest of efficiency. Optimization for on-task capabilities can thereby avoid a range of risks that have never been considered.

## Optimizing an AI system for a bounded task is itself a bounded task

Optimizing a system for a bounded AI task can itself be framed as a bounded AI task. The task of designing and optimizing an AI system for a given task using given machine resources within an acceptably short time does not entail open-ended, world-affecting activity, and likewise for designing and optimizing AI systems for the tasks involved in designing and optimizing AI systems for the tasks of designing and optimizing AI systems.

## Superintelligent-level optimization can contribute to AI safety

Given that optimization can be used to shape AI systems that perform a range of tasks with little or no catastrophic risk, it may be useful to seek tasks that, in composition with systems that perform other tasks, directly reduce the risks of employing systems with powerful capabilities. A leading example is the development of predictive models of human relevance and human approval based on large corpora of human opinions and crowd-sourced challenges. Ideally, such models would have access to general world knowledge and be able to engage in general reasoning about cause, effect, and the range of potential human reactions. [Predictive models of human approval](→§22) would be useful for [augmenting human oversight](→§24), [flagging potential concerns](→§20), and [constraining the actions of systems with different capabilities](→§20). These and similar applications are attractive targets for shaping AI outcome through differential technology development.

Bad actors could of course apply strongly optimized AI technologies—even approval modeling—to bad or risky ends (*e.g.*, open-ended exploitation of internet access for wealth maximization). Bad actors and bad actions are a crucial concern in considering strategies for managing a safe transition to a world with superintelligent-level AI, yet effective countermeasures may themselves require strong, safe optimization of AI systems for strategically important tasks. The development of strong optimization power is a given, and we should not shy away from considering how strongly optimized AI systems might be used to solve problems.

## Further Reading

- §2 *Standard definitions of “superintelligence” conflate learning with competence*

- §12 *AGI agents offer no compelling value*

- §20 *Collusion among superintelligent oracles can readily be avoided*

- §21 *Broad world knowledge can support safe task performance*

- §22 *Machine learning can develop predictive models of human approval*

- §30 *Risky AI can help develop safe AI*

