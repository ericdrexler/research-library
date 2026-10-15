# §28 Automating biomedical R&D does not require defining human welfare

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 28 of 40. Source label: `biomedical-agi`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Superintelligent-level support for tasks as broad as biomedical research need not incur the classic problems of AGI value alignment.

**Cites sections:** §10 *R&D automation dissociates recursive improvement from AI agency*; §12 *AGI agents offer no compelling value*; §20 *Collusion among superintelligent oracles can readily be avoided*; §21 *Broad world knowledge can support safe task performance*; §22 *Machine learning can develop predictive models of human approval*; §23 *AI development systems can support effective human guidance*; §24 *Human oversight need not impede fast, recursive AI technology improvement*

**Cited by sections:** §II, §5

---
## Summary

It has been suggested that assigning AGI agents tasks as broad as biomedical research (*e.g.*, “curing cancer”) would pose difficult problems of AI control and value alignment, yet a concrete, development-oriented perspective suggests that problems of *general* value alignment can be avoided. In a natural path forward, diverse AI systems would automate and coordinate diverse biomedical research tasks, while human oversight would be augmented by AI tools, including predictive models of human approval. Because strong task alignment does not require formal task specification, a range of difficult problems need not arise. In light of alternative approaches to providing general AI services, there are no obvious advantages to employing risky, general-purpose AGI agents to perform even extraordinarily broad tasks.

## Broad, unitary tasks could present broad problems of value alignment

(Soares 2018) opens with an example of a potential AGI problem: [fn: This quote comes from an earlier draft (*MIRI Technical report 2015–4*), available at <https://intelligence.org/files/obsolete/ValueLearningProblem.pdf>]

> Consider a superintelligent system, in the sense of Bostrom (2014), tasked with curing cancer […] without causing harm to the human (no easy task to specify in its own right). The resulting behavior may be quite unsatisfactory. Among the behaviors not ruled out by this goal specification are stealing resources, proliferating robotic laboratories at the expense of the biosphere, and kidnapping human test subjects.

The following sections will consider biomedical research (including cancer research tasks) from a general but more concrete, less unitary perspective, concluding that undertaking AI-driven biomedical research need not risk programs based on criminality (kidnapping, *etc.*) or catastrophic problems of value alignment. (I thank Shahar Avin for suggesting this topic as a case study.)

| **Diverse roles and tasks in biomedical research and applications:** |                         |
|:---------------------------------------------------------------------|:------------------------|
| **Scientific research:**                                             | **Research direction:** |
| Developing techniques                                                | Resource allocation     |
| Implementing experiments                                             | Project management      |
| Modeling biological systems                                          | Competitors, reviewers  |
| **Clinical practice:**                                               | **Oversight:**          |
| Patients                                                             | Citizen’s groups        |
| Physicians                                                           | Regulatory agencies     |
| Health service providers                                             | Legislatures            |

## Diverse AI systems could automate and coordinate diverse research tasks

Biomedical research and applications comprise extraordinarily diverse activities. Development of even a single diagnostic or therapeutic technology, for example, typically draws on many distinct areas of competence that support concept development, experimentation, and data analysis. At a higher level of research organization, project management and resource allocation call for [assessment of competing proposals](→§20) [→ §12 *AGI agents offer no compelling value*] in light of not only their technical merits, but of their costs and benefits to human beings.

Progress in implementing AI systems that provide diverse superhuman competencies could enable automation of a full range of technical and managerial tasks, and because [AI R&D is itself subject to automation](→§10), progress could be incremental, yet swift. By contrast, it is difficult to envision a development path in which AI developers would treat all aspects of biomedical research (or even cancer research) as a single task to be learned and implemented by a generic system. Prospects for radical improvements in physical tools (*e.g.*, through molecular systems engineering) do not change this general picture.

## Human oversight can be supported by AI tools

Within the scope of biomedical research, several areas—resource investments, *in-vivo* experimentation, and clinical applications—call for strong human oversight, and oversight is typically mandated not only by ethical concerns, but by law, regulation, and institutional rules. Human oversight is not optional (it is part of the task), yet AI applications could potentially make human oversight more effective. For example, systems that [describe research proposals](→§23) in terms of their anticipated human consequences would enable human oversight of complex research plans, while [robust predictive models of human concerns](→§22) could be applied to focus scarce human attention. Consultation with superintelligent-level advisors could presumable enable extraordinarily well-informed judgments by patients and physicians.

## Strong task alignment does not require formal task specification

[The example of language translation shows that task alignment need not require formal task specification](→§21), and a development-oriented perspective on concrete biomedical tasks suggests that this property may generalize quite widely. Although it is easy to envision both safe and unsafe configurations of task-performing systems, it is reasonable to expect that ongoing AI safety research (both theoretical and informed by ongoing experience) can enable thorough automation of research while avoiding both unacceptable costs and extraordinary risks stemming from emergent behaviors. If safety need not greatly impede development, then unsafe development is best viewed as a bad-actor risk.

## The advantages of assigning broad, unitary tasks to AGI agents are questionable

It has been persuasively argued (Bostrom 2014) that self-improving, general-purpose AGI agents cannot safely be tasked with broad goals, or with seemingly narrow goals that might motivate catastrophic actions. If [a full range of superintelligent-level AI capabilities can be provided efficiently by other means](→§12), then the advantages of developing risky AGI agents are questionable.

The argument that access to general, superintelligent-level AI capabilities need not incur the risks of superintelligent AGI agents includes the following points:

- [Recursive technology improvement](→§10) is a natural extension of current AI R&D, and does not entail recursive self improvement of distinct AI systems: Agents are products, not development tools.

- [Effective human oversight](→§24) need not substantially impede recursive improvement of *basic AI technologies,* while overseeing the development of *task-focused AI systems* is similar to (but less risky than) specifying tasks for an AGI system.

- [Models of human approval](→§22) can inform AI plans in bounded domains, while the use of AI systems to examine the scope and effects of proposed plans (in an [implicitly adversarial architecture](→§20)) scales to superintelligent proposers and critics.

It seems that there are no clear technical advantages to pursuing an AGI-agent approach to biomedical research, while a task-focused approach provides a natural path in which value-alignment problems are bounded and mitigated. Until general value-alignment problems are solved, it would be wise to avoid them.

## Further Reading

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §12 *AGI agents offer no compelling value*

- §20 *Collusion among superintelligent oracles can readily be avoided*

- §21 *Broad world knowledge can support safe task performance*

- §22 *Machine learning can develop predictive models of human approval*

- §23 *AI development systems can support effective human guidance*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

