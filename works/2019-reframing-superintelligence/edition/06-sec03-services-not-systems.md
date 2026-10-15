# §3 To understand AI prospects, focus on services, not implementations

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 3 of 40. Source label: `services-not-systems`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Shifting the focus of attention from AI systems to AI services yields a more uniform and tractable model of artificial general intelligence that reframes the problem of aligning superintelligent-level AI functionality with human purposes.

**Cites sections:** §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*; §10 *R&D automation dissociates recursive improvement from AI agency*; §16 *Aggregated experience and centralized learning support AI-agent applications*; §20 *Collusion among superintelligent oracles can readily be avoided*; §22 *Machine learning can develop predictive models of human approval*; §23 *AI development systems can support effective human guidance*; §26 *Superintelligent-level systems can safely provide design and planning services*; §29 *The AI-services model reframes the potential roles of AGI agents*

**Cited by sections:** §II, §4

---
## Summary

From an instrumental perspective, intelligence centers on capabilities rather than systems, yet models of advanced AI commonly treat the key capability of *general intelligence*—the ability to develop novel capabilities—as a black-box mechanism embedded in a particular kind of system, an AGI agent. Service-oriented models of general intelligence instead highlight the *service of developing new services* as a computational action, and place differentiated task functionality (rather than unitary, general-purpose systems) at the center of analysis, linking models to the richly-developed conceptual framework of software engineering. Service-oriented models reframe the problem of aligning AI functionality with human goals, providing affordances absent from opaque-agent models.

## The instrumental function of AI technologies is to provide services

In the present context, “services” are tasks performed to serve a client. AI systems may provide services to humans more-or-less directly (driving, designing, planning, conversing…), but in a software engineering context, one may also refer to clients and service-providers (servers) when both are computational processes.

Not every action performs a service. As with human intelligence, intelligence embodied in autonomous systems might not serve the instrumental goals of any external client; in considering actions of the system itself, the concept of goals and utility functions would then be more appropriate than the concept of services.

## General intelligence is equivalent to general capability development

General intelligence requires an open-ended ability to develop novel capabilities, and hence to perform novel tasks. For instrumental AI, *capabilities* correspond to *potential services,* and general artificial intelligence can be regarded as an open-ended service able to provide new AI services by developing new capabilities.

## The *ability to learn* is a capability

In humans (with their opaque skulls and brains), it is natural to distinguish internal capabilities (*e.g.*, learning to program) from external capabilities (*e.g.*, programming a machine), and to treat these as different in kind. In computational systems, however, there need be no such distinction: To develop a capability is to implement a system that provides that capability, a process that need not modify the system that performs the implementation. Removing artificial distinctions between kinds of capabilities improves the scope, generality, and homogeneity of models of artificial general intelligence.

## Implementing new capabilities does not require “self modification”

An incremental computational process may extend the capabilities of a computational system. If the resulting code automatically replaces the previous version, and if it is convenient to regard that process as internal to the system, then it may be natural to call the process “self modification”. In many practical applications, however, a different approach will produce better results: Data can be aggregated from many instances of a system, then combined through a centralized, perhaps computationally-intensive development service to produce upgraded systems that are then tested and deployed. The [strong advantages of data aggregation and centralized development](→§16) [fn: §16 *Aggregated experience and centralized learning support AI-agent applications*.] suggest that it would be a mistake to adopt “self modification” as a default model of system improvement.

## Service-centered models highlight differentiated, task-focused functionality

Services have structure: Across both human and computational worlds, we find that high-level services are provided by employing and coordinating lower-level services. We can expect that services of different kinds (*e.g.*, language translation, theorem proving, aircraft design, computer hacking, computer security, military strategy) will or readily could be developed and implemented as substantially distinct computational systems, each operating not only as a server, but as a client that itself employs a range of narrower services. It is safe to assert that the architecture of complex services and service-providers will be neither atomized nor monolithic.

## Service-centered models harmonize with practice in software engineering

AI services are being developed and deployed in the context of other software services. Decades of research, billions of dollars, and enormous intellectual effort have been invested in organizing the development of increasingly complex systems, and universal patterns have emerged; in particular, system architectures are defined by their functions and interfaces—by service provided and means of employing them. The art of decomposing high-level functions into lower-level functions has been essential to making systems comprehensible, implementable, and maintainable. Modern software services are both the technological milieu of modern AI and a model for how complex information services emerge and evolve.

Perhaps the most fundamental principles are modularity and abstraction: partitioning functionality and then decoupling functionality from implementation. We can expect that these extraordinarily general abstractions can and will scale to systems implemented by (and to provide) superintelligent-level services.

## Service-centered AI architectures can facilitate AI alignment

A system-centric model would suggest that general-purpose artificial intelligence must be a property of general-purpose AI systems, and that a fully-general AI system, to perform its functions, must be a powerful superintelligent agent. From this model and its conclusion, profound challenges follow.

A service-centric model, by contrast, proposes to satisfy general demands for intelligent services through a general capacity to develop services. This general capacity is not itself a thing or an agent, but a pool of functionality that can be provided by coordination of AI-development services. In this model, even [highly-capable agents implemented at a superintelligent level](→§29) [fn: §29 *The AI-services model reframes the potential roles of AGI agents*.] can be stable, and need not themselves embody AI-development functionality. This model suggests that a range of profound challenges, if recognized, can also be avoided.

Diverse, potentially superintelligent-level AI services could be coordinated to provide the service of developing new AI services. Potential components and functions include:

- [Predictive models of human approval, disapproval, and controversies](→§22). [fn: §22 *Machine learning can develop predictive models of human approval*.]

- [Consulting services that propose and discuss potential products and services](→§23). [fn: §23 *AI development systems can support effective human guidance*.]

- [Design](→§26), [fn: §26 *Superintelligent-level systems can safely provide design and planning services*.] [implementation](→§10), [fn: §10 *R&D automation dissociates recursive improvement from AI agency*.] and [optimization services](→§8). [fn: §8 *Strong optimization can strongly constrain AI capabilities, behavior, and effects*.]

- [Specialists in technical security and safety measures](→§26). [fn: §26 *Superintelligent-level systems can safely provide design and planning services*.].

- [Evaluation through criticism and red-team/blue-team competitions](→§20). [fn: §20 *Collusion among superintelligent oracles can readily be avoided*.]

- [Pre-deployment testing and post-deployment assessment](→§16). [fn: §16 *Aggregated experience and centralized learning support AI-agent applications*.]

- [Iterative, experience-based upgrades to products and services](→§16). [fn: §16 *Aggregated experience and centralized learning support AI-agent applications*.]

Each of the above corresponds to one or more high-level services that would typically rely on others, whether these are narrower (*e.g.*, language understanding and technical domain knowledge) or at a comparable level (*e.g.*, predictive models of human (dis)approval). Some services (*e.g.*, criticism and red-team/blue-team competitions) by nature interact with others that are adversarial and operationally distinct. Taken together, these services suggest a range of alignment-relevant affordances that are (to say the least) not salient in models that treat general intelligence as a black-box mechanism that is embedded in a general-purpose agent.

## Further Reading

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §11 *Potential AGI-enabling technologies also enable comprehensive AI services*

- §12 *AGI agents offer no compelling value*

- §16 *Aggregated experience and centralized learning support AI-agent applications*

- §29 *The AI-services model reframes the potential roles of AGI agents*

- §38 *Broadly-capable systems coordinate narrower systems*

