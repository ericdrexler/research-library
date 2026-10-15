# §17 End-to-end reinforcement learning is compatible with the AI-services model

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 17 of 40. Source label: `e2e-reinforcement`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** End-to-end training and reinforcement learning fit naturally within integrated AI-service architectures that exploit differentiated AI components.

**Cites sections:** §2 *Standard definitions of “superintelligence” conflate learning with competence*; §9 *Opaque algorithms are compatible with functional transparency and control*; §10 *R&D automation dissociates recursive improvement from AI agency*; §12 *AGI agents offer no compelling value*; §15 *Development-oriented models align with deeply-structured AI systems*; §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*; §24 *Human oversight need not impede fast, recursive AI technology improvement*; §38 *Broadly-capable systems coordinate narrower systems*

**Cited by sections:** §II

---
## Summary

Advances in deep reinforcement learning and end-to-end training have raised questions regarding the likely nature of advanced AI systems. Does progress in deep RL naturally lead to undifferentiated, black-box AI systems with broad capabilities? Several considerations suggest otherwise, that RL techniques will instead provide task-focused competencies to heterogeneous systems. General AI services must by definition encompass broad capabilities, performing not a single task trained end-to-end, but many tasks that serve many ends and are trained accordingly. Even within relatively narrow tasks, we typically find a range of distinct subtasks that are best learned in depth to provide robust functionality applicable in a wider range of contexts. We can expect to see RL applied to the development of focused systems (whether base-level or managerial) with functionality that reflects the natural diversity and structure of tasks.

## RL and end-to-end training tend to produce black-box systems

Methods that employ end-to-end training and deep reinforcement learning (here termed simply “deep RL”) have produced startling advances in areas that range from *game play* (Mnih et al. 2015) to *locomotion* (Heess et al. 2017) to *neural-network design* (Zoph and Le 2016). In deep RL, what are effectively black-box systems learn to perform challenging tasks directly from reward signals, bypassing standard development methods. Advances in deep RL have opened fruitful directions for current research, but also raise questions regarding the likely nature (and safety) of advanced AI systems with more general competencies.

## RL and end-to-end training are powerful, yet bounded in scope

Complex products (both hardware and software) have generally been built of components with differentiated competencies. End-to-end training challenges this model: Although systems are commonly differentiated in some respects (*e.g.*, convolutional networks for visual processing, recurrent neural networks for sequential processing, external memories for long-term representation), these system components and their learned content do not align with distinct tasks at an application level. Functional competencies are (at least from an external perspective) undifferentiated, a confronting us with black-box systems.

Will end-to-end training of black-box systems scale to the development of AI systems with extremely broad capabilities? If so—and if such methods were to be both efficient by metrics of development cost and effective by metrics of product quality—then advanced AI systems might be expected to lack the engineering affordances provided by differentiated systems. In particular, component functionalities might not be identifiable, separable, and subject to intensive training and testing.

There is, however, reason to expect that broad AI systems will comprise patterns of competencies that reflect (and [expose](→§9)) the [natural structure of complex tasks](→§38). The reasons include both constraints (the nature of training and bounded scope of transfer learning) and opportunities (the greater robustness and generalization capabilities of systems that exploit robust and general components).

## General capabilities comprise many tasks and end-to-end relationships

What would it even mean to apply end-to-end training to a system with truly general capabilities? Consider a hypothetical system intended to perform a comprehensive range of diverse tasks, including conversation, vehicle guidance, [AI R&D](→§10), and much more. What input information, internal architecture, output modalities, and objective functions would ensure that each task is trained efficiently and well? Given the *challenges of transfer learning* (Teh et al. 2017) even across a range of similar games, why would one expect to find a compelling advantage in learning a comprehensive range of radically different tasks through end-to-end training of a single, undifferentiated system?

Diverse tasks encompass many end-to-end relationships. A general system might provide services that include witty conversation and skillful driving, but it is implausible that these services could best be developed by applying deep RL to a single system. Training a general system to exploit differentiated resources (providing knowledge of vehicle dynamics, scene interpretation, predictions of human road behavior; linked yet distinct resources for conversing with passengers about travel and philosophy) seems more promising than attempting to treat all these tasks as one.

## Broad capabilities are best built by composing well-focused competencies

Systems that draw on (and perhaps adapt) distinct subtask competencies will often support more robust and general performance. For example, to interact with human beings well calls for a model of many aspects of human concerns, capabilities, intentions, and responses to situations—aspects that are unlikely to be thoroughly explored through deep RL within the scope of any particular task. For example, a model of an open task environment, such as a road, may fail to model child ball-chasing events that are rare on roads, but common on playgrounds. Similarly, a system intended to explore theoretical physics might struggle to discover mathematical principles that might better be provided through access to a system with strong, specifically mathematical competencies. The use of focused, broadly-applicable competencies in diverse contexts constitutes a powerful form of transfer learning.

Narrow components can support—and strengthen—broad capabilities, and are best learned in depth and with cross-task generality, not within the confines of a particular application. Note that components can be [distinct, yet deeply integrated](→§9) at an algorithmic and representational level.

## Deep RL can contribute to R&D automation within the CAIS model of general AI

Reinforcement learning fits naturally with the [R&D automation model of comprehensive AI services](→§12). Deep RL has already been applied to *develop state-of-the art neural networks* (Zoph and Le 2016), including *scalable modular systems* (Zoph et al. 2017), and deep RL has been applied to *optimizing deep RL systems*. Increasing automation of AI R&D will facilitate the development of task-oriented systems of all kinds, and will naturally result in [deeply-structured systems](→§15).

In considering RL in the context of AI control and safety, in is important to keep in mind that [RL systems are not utility-maximizing agents](→§18), that [learning is separable from performance](→§2), that [human oversight need not impede rapid progress](→§24), and that component-level algorithmic opacity is [compatible with system-level functional transparency](→§9). Because efficiency, quality, reliability, and safety all favor the development of functionally differentiated AI services, powerful RL techniques are best regarded as tools for implementing and improving AI services, not as harbingers of omnicompetent black-box AI.

## Further Reading

- §7 *Training agents in human-like environments can provide useful, bounded services*

- §9 *Opaque algorithms are compatible with functional transparency and control*

- §12 *AGI agents offer no compelling value*

- §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*

- §38 *Broadly-capable systems coordinate narrower systems*

