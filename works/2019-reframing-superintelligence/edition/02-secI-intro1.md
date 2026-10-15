# §I Introduction: From R&D automation to comprehensive AI Services

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section I (introductory). Source label: `intro1`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Responsible development of AI technologies can provide an increasingly comprehensive range of superintelligent-level AI services—including the service of developing new services—and can thereby deliver the value of general-purpose AI while avoiding the risks associated with self-modifying AI agents.

**Cites sections:** §9 *Opaque algorithms are compatible with functional transparency and control*

---
## Summary

The emerging trajectory of AI development reframes AI prospects. Ongoing automation of AI R&D tasks, in conjunction with the expansion of AI services, suggests a tractable, non-agent-centric model of recursive AI technology improvement that can implement general intelligence in the form of comprehensive AI services (CAIS), a model that includes the service of developing new services. The CAIS model—which scales to superintelligent-level capabilities—follows software engineering practice in abstracting functionality from implementation while maintaining the familiar distinction between application systems and development processes. Language translation exemplifies a service that could incorporate broad, superintelligent-level world knowledge while avoiding classic AI-safety challenges both in development and in application. Broad world knowledge could likewise support predictive models of human concerns and (dis)approval, providing safe, potentially superintelligent-level mechanisms applicable to problems of AI alignment. Taken as a whole, the R&D-automation/CAIS model reframes prospects for the development and application of superintelligence, placing prospective AGI agents in the context of a broader range of intelligent systems while attenuating their marginal instrumental value.

## The trajectory of AI development reframes AI prospects

Past, present, and projected developments in AI technology can inform our understanding of prospects for superintelligent-level capabilities, providing a concrete anchor that complements abstract models of potential AI systems. A development-oriented perspective highlights path-dependent considerations in assessing potential risks, risk-mitigation measures, and safety-oriented research strategies. The current trajectory of AI development points to asymptotically recursive automation of AI R&D that can enable the emergence of general, asymptotically comprehensive AI services (CAIS). In the R&D-automation/CAIS model, recursive improvement and general AI capabilities need not be embodied in systems that act as AGI agents.

> **Figure 1.** Classes of intelligent systems
> *(Image `fig1.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> A large dotted-line rectangle labeled "Intelligent systems" at the top encloses the whole diagram, which contains two solid-outlined boxes stacked vertically inside it. The upper box is labeled "Collectively-general services" and contains two rounded rectangles connected by a downward block arrow: an upper rounded rectangle labeled "AI design & information services" and, below it, a rounded rectangle labeled "Task-oriented agents." The downward arrow runs from "AI design & information services" to "Task-oriented agents," indicating that AI design & information services produce or give rise to task-oriented agents. A second, wider downward block arrow originates from "AI design & information services" (running alongside/behind the "Task-oriented agents" box) and continues down past the boundary of the "Collectively-general services" box into the lower box, terminating at "AGI agents" — indicating that AI design & information services can also produce AGI agents directly, in parallel with task-oriented agents.
>
> The lower solid-outlined box is labeled "Individually-general agents" and contains two rounded rectangles side by side: "Humans" on the left and "AGI agents" on the right. Only the "AGI agents" rectangle receives the second downward arrow from "AI design & information services" above; "Humans" has no incoming arrow. Overall, the figure places "AI design & information services" as the source feeding into two downstream categories of agents (task-oriented agents, grouped under collectively-general services, and AGI agents, grouped under individually-general agents alongside humans), with humans and AGI agents both classified as individually-general agents while task-oriented agents and the design/information services that produce them are classified as collectively-general services, all nested within the broader category of intelligent systems.

## R&D automation suggests a *technology-centered* model of recursive improvement

Technology improvement proceeds through research and development, a transparent process that exposes component tasks to inspection, refactoring, and incremental automation. [fn: Note that [component-level opacity is compatible with effective system-level transparency](→§9).] If we take advanced AI seriously, then accelerating, asymptotically-complete R&D automation is a natural consequence:

- By hypothesis, advances in AI will enable incremental automation and speedup of all human tasks.

- As-yet unautomated AI R&D tasks are human tasks, hence subject to incremental automation and speedup.

- Therefore, advances in AI will enable incremental automation and speedup of all AI R&D tasks.

Today we see automation and acceleration of an increasing range of AI R&D tasks, enabled by the application of both conventional software tools and technologies in the AI spectrum. Past and recent developments in the automation of deep-learning R&D tasks include:

- Diverse mechanisms embodied in NN toolkits and infrastructures

- Black-box and gradient-free optimization for NN hyperparameter search (Jaderberg et al. 2017)

- RL search and discovery of superior NN gradient-descent algorithms (Bello et al. 2017)

- RL search and discovery of superior NN cells and architectures (Zoph et al. 2017)

Today, automation of search and discovery (a field that overlaps with “metalearning”) requires human definition of search spaces, and we can expect that the *definition of new search spaces*—as well as fundamental innovations in architectures, optimization methods, and the definition and construction of tasks—will remain dependent on human insight for some time to come. Nonetheless, increasing automation of even relatively narrow search and discovery could greatly accelerate the implementation and testing of advances based on human insights, as well as their subsequent integration with other components of the AI technology base. Exploring roles for new components (including algorithms, loss functions, and training methods) can be routine, yet important: as Geoff Hinton has remarked, “A bunch of slightly new ideas that play well together can have a big impact”.

Focusing exclusively on relatively distant prospects for *full* automation would distract attention from the potential impact of incremental research automation in accelerating automation itself.

## R&D automation suggests a *service-centered* model of general intelligence

AI deployment today is dominated by AI services such as language translation, image recognition, speech recognition, internet search, and a host of services buried within other services. Indeed, corporations that provide cloud computing now actively promote the concept of “AI as a service” to other corporations. Even applications of AI within autonomous systems (*e.g.*, self-driving vehicles) can be regarded as providing services (planning, perception, guidance) to other system components.

R&D automation can itself be conceptualized as a set of services that directly or indirectly enable the implementation of new AI services. Viewing service development through the lens of R&D automation, tasks for advanced AI include:

- Modeling human concerns

- Interpreting human requests

- Suggesting implementations

- Requesting clarifications

- Developing and testing systems

- Monitoring deployed systems

- Assessing feedback from users

- Upgrading and testing systems

CAIS functionality, which includes the service of developing stable, task-oriented AI agents, subsumes the instrumental functionality of proposed self-transforming AGI agents, and can present that functionality in a form that better fits the established conceptual frameworks of business innovation and software engineering.

## The services model abstracts *functionality* from *implementation*

Describing AI systems in terms of functional behaviors (“services”) aligns with concepts that have proved critical in software systems development. These include separation of concerns, functional abstraction, data abstraction, encapsulation, and modularity, including the use of client/server architectures—a set of mechanisms and design patterns that support effective program design, analysis, composition, reuse, and overall robustness.

Abstraction of functionality from implementation can be seen as a figure-ground reversal in systems analysis. Rather than considering a complex system and asking how it will behave, one considers a behavior and asks how it can be implemented. Desired behaviors can be described as services, and experience shows that complex services can be provided by combinations of more specialized service providers, some of which provide the service of aggregating and coordinating other service providers.

## The R&D automation model distinguishes *development* from *functionality*

The AI-services model maintains the distinction between AI *development* and AI *functionality*. In the development-automation model of advanced AI services, stable systems build stable systems, avoiding both the difficulties and potential dangers of building systems subject to open-ended self-transformation and potential instability.

Separating development from application has evident advantages. For one, task-focused applications need not themselves incorporate an AI-development apparatus—there is little reason to think that a system that provides online language translation or aerospace engineering design services should in addition be burdened with the tasks of an AI developer. Conversely, large resources of information, computation, and time can be dedicated to AI development, far beyond those required to perform a typical service. Likewise, in ongoing service application and upgrade, aggregating information from multiple deployed systems can provide decisive advantages to centralized development (for example, by enabling development systems for self-driving cars to learn from millions of miles of car-experience per day). Perhaps most important, stable products developed for specific purposes by a dedicated development process lend themselves to extensive pre-deployment testing and validation.

## Language translation exemplifies a safe, potentially superintelligent service

Language translation provides an example of a service best provided by superintelligent-level systems with broad world knowledge. Translation of written language maps input text to output text, a bounded, episodic, sequence-to-sequence task. Training on indefinitely large and broad text corpora could improve translation quality, as could deep knowledge of psychology, philosophy, history, geophysics, chemistry, and engineering. Effective optimization of a translation system for an objective that weights both quality and efficiency would focus computation solely on the application of this knowledge to translation.

The process of *developing* language translation systems is itself a service that can be formulated as an episodic task, and as with translation itself, effective optimization of translation-development systems for both quality and efficiency would focus computation solely on that task.

There is little to be gained by modeling stable, episodic service-providers as rational agents that optimize a utility function over future states of the world, hence a range of concerns involving utility maximization (to say nothing of self-transformation) can be avoided across a range of tasks. Even superintelligent-level world knowledge and modeling capacity need not in itself lead to strategic behavior.

## Predictive models of human (dis)approval can aid AI goal alignment

As noted by Stuart Russell, written (and other) corpora provide a rich source of information about human opinions regarding actions and their effects; intelligent systems could apply this information in developing predictive models of human approval, disapproval, and disagreement. Potential training resources for models of human approval include existing corpora of text and video, which reflect millions of person-years of both real and imagined actions, events, and human responses; these corpora include news, history, fiction, science fiction, advice columns, law, philosophy, and more, and could be augmented and updated with the results of crowd-sourced challenges structured to probe model boundaries.

Predictive models of human evaluations could provide strong priors and common-sense constraints to guide both the implementation and actions of AI services, including strategic advisory services to powerful actors. Predictive models are not themselves rational agents, yet models of this kind could contribute to the solution of agent-centered safety concerns. In this connection, separation of development from application can insulate such models from perverse feedback loops involving self-modification.

## The R&D-automation/CAIS model reframes prospects for superintelligence

From a broad perspective, the R&D-automation/CAIS model:

- Distinguishes recursive technology improvement from self-improving agents

- Shows how incremental automation of AI R&D can yield recursive improvement

- Presents a model of general intelligence centered on services rather than systems

- Suggests that AGI agents are not necessary to achieve instrumental goals

- Suggests that high-level AI services would precede potential AGI agents

- Suggests potential applications of high-level AI services to general AI safety

For the near term, the R&D-automation/CAIS model:

- Highlights opportunities for safety-oriented differential technology development

- Highlights AI R&D automation as a leading indicator of technology acceleration

- Suggests rebalancing AI research portfolios toward AI-enabled R&D automation

Today, we see strong trends toward greater AI R&D automation and broader AI services. We can expect these trends to continue, potentially bridging the gap between current and superintelligent-level AI capabilities. Realistic, path-dependent scenarios for the emergence of superintelligent-level AI capabilities should treat these trends both as an anchor for projections and as a prospective context for trend-breaking developments.

