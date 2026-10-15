# §30 Risky AI can help develop safe AI

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 30 of 40. Source label: `risky-to-safe`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Complex, unitary, untrusted AI systems could be leveraged to produce non-problematic general-learning kernels through competitive optimization for objectives that heavily weight minimizing description length.

**Cites sections:** §2 *Standard definitions of “superintelligence” conflate learning with competence*; §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*; §19 *The orthogonality thesis undercuts the generality of instrumental convergence*; §20 *Collusion among superintelligent oracles can readily be avoided*; §36 *Desiderata and directions for interim AI safety guidelines*

**Cited by sections:** §II, §7

---
## Summary

In a familiar AGI threat model, opaque, self-improving AI systems give rise to systems that incorporate wide-ranging information, learn unknown objectives, and could potentially plan to pursue dangerous goals. The R&D-automation/AI-services model suggests that technologies that could enable such systems would first be harnessed to more prosaic development paths, but what if powerful AI-development capabilities were deeply entangled with opaque, untrusted systems? In this event, conceptually straightforward methods could be employed to harness untrusted systems to the implementation of general learning systems that lack problematic information and purposes. Key affordances include re-running development from early checkpoints, and applying optimization pressure with competition among diverse systems to produce compact “learning kernels”. Thus, from a path that could lead to problematic AGI agents, a readily accessible off-ramp leads instead to general intelligence in the form of capabilities that enable open-ended AI-service development. *(These and related topics have been explored in an earlier form, but in greater depth, in FHI Technical Report 2015-3 (Drexler 2015).)*

## A familiar threat model posits opaque, self-improving, untrusted AI systems

In a familiar AGI threat model, the pursuit of general, superintelligent level AI leads to opaque, self-improving systems with ill-characterized information content, inference capabilities, planning capabilities, and goals. Strong arguments suggest that the use of such systems could pose grave risks (Bostrom 2014).

The present analysis will consider a near-worst-case scenario in which AI development stands at the threshold of building such systems, rather than considering how such a situation could be avoided. Further, it will consider the hard case in which “general intelligence” is an indivisible property, a capacity to learn more-or-less anything that a human can, and potentially much more. Crucially, the analysis will neither equate *intelligence as learning capacity* with *intelligence as competence* [→ §2 *Standard definitions of “superintelligence” conflate learning with competence*] nor assume that a *product system* must inherit the full information content of the *producing system*. Finally, it will assume that researchers retain copies of precursors of systems of interest.

## Open-ended “self-improvement” implies strong, general AI implementation capabilities

“Self improvement” implies strong, general AI implementation capabilities, yet in considering a chain of improved implementations, the concept of “self” is at best ambiguous, and at worst is an anthropomorphic distraction. [→ §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*] Operationally, “self” improvement implies an opaque system that is capable of implementing systems that are better than itself by some metric, and in particular, is capable of implementing systems that are improved in the sense of being better at implementing improved systems (*etc.*). In the proposed AGI threat model, some earlier, non-problematic system was capable of serving as a link in such a chain (given suitable machine resources, training data, simulated environments, and tasks) and the actual development history from that point led to a problematic result.

## Successful system development can be recapitulated with variations

In general, results in machine learning can be repeated with variations in architectures, training data, simulated environments, training objectives, *etc.* In the present instance, systems with the potential to give rise to a sequence of improved systems are assumed to be architecturally opaque; nonetheless, [external affordances](→Figure 5) (training data, simulated environments, training objectives, resource-optimization pressures, *etc.*) remain available. Development of powerful systems can be recapitulated with variations induced by external affordances, and these affordances can strongly affect the content of what is learned. If the desired core functionality is development of learning systems, it is likely that relatively abstract problem spaces will sufficient or optimal. In addition, learning to optimize systems for learning a task does not require access to detailed task-level training data or environments, and optimizing systems for the task of *optimizing architectures for systems that learn a task* is even more abstract and remote from object-level training information. Note that tasks at all levels are by nature bounded with respect to time and resources, and hence do not naturally engender convergent instrumental goals. [→ §19 *The orthogonality thesis undercuts the generality of instrumental convergence*]

In research and development, different versions of systems are always in implicit competition with one another to maximize performance on some bounded task: Those that perform poorly by relevant metrics will be set aside, while versions that perform well will be used to produce (or serve as prototypes for) next-generation systems. Thus, the convergent goal of systems under development is competition to perform bounded tasks, and by the orthogonality thesis (Bostrom 2014), the pursuit of bounded goals can employ arbitrarily high intelligence. In aggregate, such systems will (or readily could) satisfy [conditions that exclude collusion](→§20).

## Optimization can favor the production of compact, general learning kernels

The scheme outlined here centers on competitive optimization of “learning kernels” for “compactness”, where a learning kernel is a system that, in conjunction with computational resources, auxiliary components, and a set of benchmark “demo tasks”, can produce an expanded set of systems that perform those tasks at some given level of performance. Here, optimizing for compactness implies minimizing a weighted sum of the kernel’s description length (operationally, the number of bits in a string that decompresses and compiles to build the system) and metrics corresponding to the resources it consumes in expansion; in the present context, compactness is assumed to give heavy weight to description length, penalizing resource consumption only to exclude undue computational costs. If kernel expansion can produce a range of systems that perform each of a sufficiently broad range of challenging demo tasks, then the learning kernel can be considered general. Examples of demo-task domains might include:

- Language translation

- Visual perception

- Robotic control

- Spacecraft design

- Chemical synthesis

- Strategic planning

- Theorem proving

- Software development

Note that current practice in AI research does in fact iteratively develop, train, and improve relatively compact learning kernels (architectures and algorithms) that, through training, expand their information content to produce systems that perform tasks in particular domains.

> **Figure 10.** Applying problematic, ill-characterized AI systems to implementation tasks under competitive optimization pressure could produce clean, compact systems with general learning capabilities. (Schematic diagram)
> *(Image `fig12.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> The diagram runs left to right, with a bottom axis labeled "MESSY" (arrow pointing left) and "CLEAN" (arrow pointing right), indicating that the left side of the figure is messy and the right side is clean. On the far left is a stack of three overlapping rounded boxes, each labeled "Problematic \"self\"-improving system." Arrows lead from these three boxes rightward to a cluster of six overlapping rounded boxes each labeled "Kernel builder" (each problematic system sends arrows to two kernel builders). Arrows from all six "Kernel builder" boxes converge on a single dot.
>
> From that dot, a thick arrow continues rightward through a bottleneck formed by two large gray block arrows pointing toward each other (one from above, one from below), labeled above with the bold heading "Competitive compactness-optimization bottleneck." Past the bottleneck the arrow reaches a second dot, then leads into a box with a bold border labeled "Minimal learning kernel."
>
> From "Minimal learning kernel," two arrows lead rightward to two dots inside a dotted rounded rectangle labeled, in italics, "EXPANSION" (upper part) and "& LEARNING" (lower part). Feeding into this dotted box from above is a box labeled "Training resources," connected by five downward arrows; feeding into it from below is a box labeled "Auxilliary components," connected by five upward arrows. From the two dots inside the dotted "EXPANSION & LEARNING" box, arrows fan out rightward to six separate boxes on the far right edge, labeled in sequence "Demo 1," "Demo 2," "Demo 3," "Demo 4," "Demo 5," and "Demo 6."

## Competitive optimization for compactness can exclude problematic information and competencies

Competition for learning-kernel compactness, subject to retaining generality, will strongly exclude potentially-problematic information that does not contribute to the process of learning target competencies. A world-beating Go system need not “know” that it is “playing a game”; a high-quality machine translation system need not “know” that its outputs are “requested by human beings”; a machine vision system need not “know” that its capabilities enable “autonomous vehicle control”. A compact, general kernel that can generate Go-learning, language-learning, and vision-learning systems can (and under optimization, must) “know” even less about concrete tasks, domains, and intended applications in a “human world”.

In the standard AGI threat model, self-improvement (which is to say, AI implementation capability) is capable of producing systems that operate at a superintelligent level. Systems at this level that are optimized to optimize general learning kernels for compactness presumably can be quite effective at stripping out information that is unnecessary for task performance. Given that post-bottleneck training data can provide all domain-relevant information, together with auxiliary resources such as efficient numerical algorithms, effective optimization will strip out virtually all world knowledge (geography, history, vocabulary, chemistry, biology, physics…), including any plausible basis for problematic plans and concrete world-oriented competencies. This conclusion holds even if the kernel-implementation systems might be untrustworthy if directly applied to world-oriented tasks.

## Exclusion of problematic content can provide a safe basis for developing general capabilities

In the familiar AGI threat model, development results in opaque, self-improving, ill-characterized, but highly-capable systems, and—crucially—the use of these capabilities is assumed to require that *the problematic systems themselves* be applied to a wide range of world tasks. This assumption is incorrect. As argued above, posited self-improvement capabilities could instead be re-developed from earlier, non-problematic systems through a process that leads to diverse systems that compete to perform tasks that include AI system development. The AI-implementation capacity of such systems could then be applied to the development of compact general-learning kernels that will omit representations of problematic knowledge and goals. This strategy is technology-agnostic: It is compatible with neural, symbolic, and mixed systems, whether classical or quantum mechanical; it assumes complete implementation opacity, and relies only on optimization pressures directed by external affordances.

Because expansion of a general learning kernel would in effect implement the “research” end of AI R&D automation, the strategy outlined above could provide a clean basis for any of a range of development objectives, whether in an AGI-agent or CAIS model of general intelligence. This approach is intended to address a particular class of scenarios in which development has led the edge of a cliff, and is offered as an example, not as a prescription: Many variations would lead to similar results, and ongoing application of the underlying principles would avoid classic threat models from the start. These safety-relevant principles are [closely aligned with current practice in AI system development](→§36).

## Further Reading

- §1 *R&D automation provides the most direct path to an intelligence explosion*

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*

- §9 *Opaque algorithms are compatible with functional transparency and control*

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §11 *Potential AGI-enabling technologies also enable comprehensive AI services*

- §36 *Desiderata and directions for interim AI safety guidelines*

