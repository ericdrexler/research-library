# §38 Broadly-capable systems coordinate narrower systems

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 38 of 40. Source label: `broadly-competent`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** In both human and AI systems, we see broad competencies built on narrower competencies; this pattern of organization is a robust feature of intelligent systems, and scales to systems that deliver broad services at a superhuman level.

**Cited by sections:** §II, §7, §17, §29

---
## Summary

In today’s world, superhuman competencies reside in structured organizations with extensive division of knowledge and labor. The reasons for this differentiated structure are fundamental: Specialization has robust advantages both in learning diverse competencies and in performing complex tasks. Unsurprisingly, current AI services show strong task differentiation, but perhaps more surprisingly, AI systems trained on seemingly indivisible tasks (*e.g.*, translating sentences) can spontaneously divide labor among “expert” components. In considering potential SI-level AI systems, black-box abstractions may sometimes be useful, but these abstractions set aside our general knowledge of the differentiated architecture of intelligent systems.

## Today’s superhuman competencies reside in organizational structures

It is a truism that human organizations can achieve tasks beyond individual human competence by employing, not just many individuals, but individuals who perform differentiated tasks using differentiated knowledge and skills. Adam Smith noted the advantages of division of labor (even in making pins), and in modern corporations, division of labor among specialists is a necessity.

## Specialization has robust advantages in learning diverse competencies

The structure of knowledge enables parallel training: Learning competencies in organic chemistry, financial management, mechanical engineering, and customer relations, for example, is accomplished by individuals who work in parallel to learn the component tasks. This pattern of parallel, differentiated learning works well because many blocks of specialized knowledge have little mutual dependence. The limited pace of human learning and vast scope of human knowledge make parallel training mandatory in the human world, and in machine learning analogous considerations apply. Loosely-coupled bodies of knowledge call for loosely-coupled learning processes that operate in parallel.

## Division of knowledge and labor is universal in performing complex tasks

As with learning, parallel, specialized efforts have great advantages in performing tasks. Even setting aside human constraints on bandwidth and representational power, there would be little benefit in attempting to merge day-to-day tasks in the domains of organic chemistry, financial management, mechanical engineering, and customer relations. Both information flow and knowledge naturally cluster in real-world task structures, and the task of cross-task management (*e.g.*, in developing and operating a chemical-processing system) has only limited overlap with the information flows and knowledge that are central to the tasks that must be coordinated. To implement a complex, inherently differentiated task in a black-box system is to reproduce the task structure inside the box while making its organization opaque.

## Current AI services show strong task differentiation

It goes without saying that current AI systems are specialized: Generality is a challenge, not a default. Even in systems that provide strong generalization *capacity,* we should expect to see diminishing returns from attempts to apply *single-system* generalization capacity to the full scope and qualitative diversity of human knowledge. Indeed, considering the nature of training and computation, it is difficult to imagine what “single-system generalization” could even mean on that scale.

## AI systems trained on seemingly indivisible tasks learn to divide labor

Task specialization can emerge spontaneously in machine learning systems. A striking recent example is a mixture-of-experts model employed in a then state-of-the art neural machine translation system to enable 1000x improvements in model capacity (Shazeer et al. 2017). In this system, a managerial component delegates the processing of sentence fragments to “experts” (small, architecturally undifferentiated networks), selecting several from a pool of thousands. During training, experts spontaneously specialize in peculiar, semantically- and syntactically-differentiated aspects of text comprehension. The incentives for analogous specialization and task delegation can only grow as tasks become wider in scope and less tightly coupled.

## Black-box abstractions discard what we know about the architecture of systems with broad capabilities

Appropriate levels of abstraction depend on both our knowledge and our purpose. If we want to model the role of Earth in the dynamics of the Solar System, it can be treated as a point mass. If we want to model Earth as a context for humanity, however, we also care about its radius, geography, geology, climate, and more—and we have substantial, useful knowledge of these. Likewise, for some purposes, it can be appropriate to model prospective AI systems as undifferentiated, black-box pools of capabilities. If we want to understand prospective AI systems in the context of human society, however, we have strong practical reasons to apply what we know about the general architecture of systems that perform broad tasks.

## Further Reading

- §12 *AGI agents offer no compelling value*

- §15 *Development-oriented models align with deeply-structured AI systems*

- §21 *Broad world knowledge can support safe task performance*

- §28 *Automating biomedical R&D does not require defining human welfare*

- §39 *Tiling task-space with AI services can provide general AI capabilities*

