# §9 Opaque algorithms are compatible with functional transparency and control

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 9 of 40. Source label: `opaque-algorithms`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Although transparency is desirable, opacity at the level of algorithms and representations need not greatly impair understanding of AI systems at higher levels of functionality.

**Cites sections:** §2 *Standard definitions of “superintelligence” conflate learning with competence*; §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*; §35 *Predictable aspects of future knowledge can inform AI safety strategies*; §39 *Tiling task-space with AI services can provide general AI capabilities*

**Cited by sections:** §I, §II, §17

---
## Summary

Deep-learning methods employ opaque algorithms that operate on opaque representations, and it would be unwise to assume pervasive transparency in future AI systems of any kind. Fortunately, opacity at the level of algorithms and representations is compatible with transparency at higher levels of system functionality. We can shape information inputs and training objectives at component boundaries, and can, if we choose, also shape and monitor information flows among opaque components in larger systems. Thus, substantial high-level understanding and control is compatible with relaxed understanding of internal algorithms and representations. As always, the actual *application* of potential control measures can be responsive to future experience and circumstances.

## Deep-learning methods are opaque and may remain so

The products of deep learning are notoriously opaque: Numerical transformations produce numerical vectors that can be decoded into useful results, but the encodings themselves are often incomprehensible. Opacity is the norm, and interpretability is the exception. In considering problems of AI control and safety, it would be unwise to assume pervasive transparency.

## The scope of information and competencies can be fuzzy, yet bounded

Although we may lack knowledge of how a deep learning system represents information and algorithms, we can have substantial knowledge of the scope of its information and competencies. For example, information that is absent from a system’s inputs (in both training and use) will be absent from its algorithms, state, and outputs. Inference capabilities may blur the scope of given information, but only within limits: A Wikipedia article cannot be inferred from language-free knowledge of physics. Likewise, while the scope of a system’s competencies may be fuzzy, competencies far from a system’s task focus (*e.g.*, theorem-proving competencies in a vision system, or vehicle-guidance competencies in a language-translation system) will be reliably absent. Bounds on information and competencies are natural and inevitable, and can be applied to help us understand and constrain AI-system functionality.

## Restricting resources and information at boundaries constrains capabilities

Several obvious affordances for control are available at the boundaries of AI systems. For example, tasks that require absent information cannot be performed, and the distinct role of physical memory in digital systems enables a [clean separation of episodic task performance from cumulative learning](→§2). Controls at boundaries have transitive effects within systems of collaborating components: A component cannot transfer information that it does not have, regardless of how internal communications are encoded.

Further, competitive systems must deliver results in bounded times and with bounded resources. Optimization pressures (*e.g.*, on model capacity, training time, and execution cost) will tend to exclude investments in off-task capacities and activities, and [stronger optimization will tend to strengthen, not weaken, those constraints](→§8). A system trained to provide services to other systems might perform unknown tasks, yet those tasks will not be *both* costly and irrelevant to external objectives.

These considerations are fundamental: They apply regardless of whether an AI system is implemented on digital, analog, or quantum computational hardware, and regardless of whether its algorithms are neural and trained, or symbolic and programmed. They scale to task domains of any scope, and to systems of any level of intelligence and competence.

## Providing *external* capabilities can constrain *internal* capabilities

Under appropriate optimization pressures, a system trained with access to an efficient resource with particular capabilities [→ §39 *Tiling task-space with AI services can provide general AI capabilities*] will not itself develop equivalent capabilities, and use of those particular capabilities will then involve use of an identifiable resource. This mechanism provides an affordance for shaping the organization of task-relevant capabilities in the development of piecewise-opaque systems. Potential advantages include not only functional transparency, but opportunities to ensure that components (vision systems, physical models, *etc.*) are well-trained, well-tested, and capable of good generalization within their domains.

## Deep learning can help interpret internal representations

Deep learning techniques can sometimes provide insight into the content of opaque, learned representations. To monitor the presence or absence of a particular kind of information in an opaque (but not *adversarially* opaque) representation, deep learning can be applied to attempt to extract and apply that information. For example, a representation may be opaque to humans, but if it supports an image-recognition task, then the representation must contain image information; if not, then it likely doesn’t.

## Task-space models can enable a kind of “mind reading”

The [task-space model](→§39) of general intelligence suggests that the subtasks engaged by problem-solving activities can (both in principle and in practice) be associated with regions in semantic spaces. Different high-level tasks will generate different footprints of activity in the space of subtasks, and one need not understand how every subtask is represented or performed to understand *what the task is about.*

Restricting the range of task-space accessible to a system could potentially provide a mechanism for constraining its actions, while observing access patterns could potentially provide the ability to monitor the considerations that go into a particular action. For example, it would be unremarkable for a system that organizes food production to access services applicable to food preparation and delivery, while a system that accesses services applicable to synthesizing neurotoxins for delivery in food might trigger a warning. Such insights (a kind of “mind reading”) could be useful both in advancing AI safety and in solving more prosaic problems of system development and debugging.

## The application of control measures can be adapted to experience and circumstances

Whether any particular set of control measures should be applied, and to what extent, is a question best answered by the AI community as circumstances arise. [Experience will provide considerable knowledge](→§35) of which kinds of systems are reliable, which fail, and which produce surprising (perhaps *disturbingly* surprising) results. Along the way, conventional concerns regarding safety and reliability will drive efforts to make systems better understood and more predictable.

To catalog a range of potential control measures (*e.g.*, attention to information content, task focus, and optimization pressures) is not to assert that any particular measure or intensity of application will be necessary or sufficient. The value of inquiry in this area is to explore mechanisms that *could* be applied in response to future experience and circumstances, and that may deserve attention today as safety-relevant components of general AI research.

## Further Reading

- §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

- §35 *Predictable aspects of future knowledge can inform AI safety strategies*

- §38 *Broadly-capable systems coordinate narrower systems*

- §39 *Tiling task-space with AI services can provide general AI capabilities*

