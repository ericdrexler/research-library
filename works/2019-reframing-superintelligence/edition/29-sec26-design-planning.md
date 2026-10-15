# §26 Superintelligent-level systems can safely provide design and planning services

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 26 of 40. Source label: `design-planning`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Superintelligent-level AI systems can safely converse with humans, perform creative search, and propose designs for systems to be implemented and deployed in the world.

**Cites sections:** §20 *Collusion among superintelligent oracles can readily be avoided*; §22 *Machine learning can develop predictive models of human approval*; §24 *Human oversight need not impede fast, recursive AI technology improvement*

**Cited by sections:** §II, §3, §11, §14, §29, §32

---
## Summary

Design engineering provides a concrete example of a planning task that could benefit from superintelligent-level support, but interactive systems for performing such tasks match classic templates for emergent AI agency and risk. Nonetheless, examining design systems at the level of task requirements, component capabilities, and development processes suggests that classic AI-agent risks need not arise. In design engineering, effective human oversight is not an impediment, but a source of value. Superintelligent-level services can help solve (rather than create) AI-control problems; for example, strong models of human concerns and (dis)approval can be exploited to augment direct human oversight.

## Design engineering is a concrete example of a planning task

Planning tasks relate means to ends, and systems-level design engineering offers an illustrative example. Systems engineering tasks are characterized by complex physical and and causal structures that often involve complex and critical interactions with human concerns. As with most planning tasks, system-level design is intended to optimize the application of bounded means (finite materials, time, costs…) to achieve ends that are themselves bounded in space, time, and value.

## AI-based design systems match classic templates for emergent AI-agent risk

Classic models of potentially catastrophic AI risk involve the emergence (whether by design or accident) of superintelligent AI systems that pursue goals in the world. Some implementations of question-answering systems (“oracles”) could present dangers through their potential ability to recruit human beings to serve as unwitting tools (*Superintelligence,* Bostrom 2014); hazardous characteristics would include powerful capabilities for modeling the external world, formulating plans, and communicating with human beings.

Nonetheless, we can anticipate great demand for AI systems that have all of these characteristics. To be effective, AI-enabled design systems should be able to discuss what we want to build, explore candidate designs, assess their expected performance, and output and explain proposals.

The classic model proposes that these tasks be performed by a system with artificial general intelligence (an AGI agent) that, in response to human requests, will seek to optimize a corresponding utility function over states of the world. Because a fully-general AGI agent could by definition perform absolutely any task with superhuman competence, it requires no further thought to conclude that such an agent could provide engineering design services.

## High-level design tasks comprise distinct non-agent-like subtasks

Figure 9 diagrams an abstract, high-level task structure for the development and application of AI-enabled design systems.

> **Figure 9.** A task structure & architecture for interactive design engineering
> *(Image `fig7.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> The diagram lays out five main boxes left to right, connected by labeled arrows, with a large central box containing an internal sub-diagram of its own.
>
> At far left is a box labeled "Basic AI R&D (diverse tasks)". A double-headed pair of arrows connects it to the next box, "System development": one arrow labeled "tools" points right (from Basic AI R&D to System development), and one arrow labeled "feedback" points left (from System development back to Basic AI R&D). The "System development" box contains four stacked, identically labeled sub-boxes, each reading "component developer".
>
> "System development" connects to the large central box via another pair of opposed arrows: "upgrades" pointing right (into the central box) and "feedback" pointing left (back to System development).
>
> The large central box (unlabeled as a whole) represents the interactive design-engineering system and contains, from top to bottom:
- At the top, a double-headed arrow connects up to "Human users" (outside the box, above it) and down to "conversational interface: words & diagrams ⇔ abstractions".
- Below that, two side-by-side boxes: "specification generator" (left) and "specification explainer" (right), joined by a rightward arrow from specification generator to specification explainer. A downward arrow runs from the conversational interface to specification generator, and an upward arrow runs from specification explainer back to the conversational interface.
- Below those, two more side-by-side boxes: "design generator" (left) and "design tester" (right). A downward arrow runs from specification generator to design generator; an upward arrow runs from design tester to specification explainer. Between design generator and design tester is a pair of thick, heavy horizontal arrows pointing in both directions (design generator ⇔ design tester), indicating a tight, high-throughput iterative loop.
- Below design generator and design tester, two diagonal double-headed arrows lead down to a horizontal band at the bottom of the central box labeled (on two lines) "curation, indexing" over "shared design libraries" (separated by a horizontal rule). The arrow from design generator down to this library band is labeled "queries" (with the arrowhead pair indicating a two-way query/response exchange). The arrow from design tester down to the library band is labeled "new designs".
- To the right of design tester, outside the central box's main column but attached to it, is a separate box labeled "simulation servers", connected to design tester by a pair of diagonal double-headed arrows (design tester ⇔ simulation servers).
>
> Finally, the central box connects to a box at far right labeled "Production & application environments" via a pair of opposed arrows: "designs" pointing right (from the central box out to Production & application environments) and "feedback" pointing left (back into the central box).
>
> Overall the figure traces a left-to-right flow: basic AI research and tools feed system development (built from component-developer modules), which produces upgrades to the interactive design system; within that system, human users converse through an interface that hands off to a specification generator/explainer pair, which in turn drives a tightly coupled design generator/tester loop (supported by simulation servers and a shared, curated design library); finished designs flow out to production and application environments, with feedback returning at every stage (application environments to the design system, the design system to system development, and system development to basic AI R&D).

In this architecture:

- A top-level conversational interface translates between human language (together with sketches, gestures, references to previous designs, *etc.*) and abstract yet informal conceptual descriptions.

- A second level translates between informal conceptual descriptions and formal technical specifications, supporting iterative definition and refinement of objectives, constraints, and general design approach. General AI, *etc.* : Comprehensive AI Services (CAIS)

- The core of the design process operates by iterative generate-and-test, formulating, simulating, and scoring candidate designs with respect to objectives and constraints (including constraints that are tacit and general).

- To enable systems to build on previous results, novel designs can be abstracted, indexed, and cached in a shared library.

- Upstream from design tasks, the development and upgrade of AI-enabled design systems is itself a product of AI-enabled design that integrates progress in basic AI technologies with domain-specific application experience.

- Downstream from design tasks, design products that pass (AI-supported) screening and comparison with competing designs may be deployed and applied, generating application experience that can inform future design.

In considering the task structure outlined in Figure 9, is important to recognize that humans (today’s agents with general intelligence) organize system design tasks in the same general way. The system shown in

Figure 9 is *not* more complex than a black-box AGI agent that has acquired engineering competencies; instead, it *makes explicit* the kinds of tasks that must implemented, regardless of how those tasks might be implemented and packaged. Hiding requirements in a black box does not make them go away.

## Real-world task structures favor finer-grained task decomposition

As an aside, we should expect components of engineering systems to be more specialized than those diagrammed above: An any but the most abstract levels, design methods for integrated-circuit design are distinct from methods for aerospace structural engineering, organic synthesis, or AI system architecture, and methods for architecting systems built of diverse subsystems are substantially different from all of these. The degree of integration of components will be a matter of convenience, responsive to considerations that include the value of modularity in fault isolation and functional transparency.

## Use of task-oriented components minimizes or avoids classic AI risks

Consider the flow of optimization and selection pressures implicit in the architecture sketched in Figure 9:

- Systems for basic AI R&D are optimized and selected to produce diverse, high-performance tools (algorithms, generic building blocks…) to be used by AI systems that develop AI systems. Off-task activities will incur efficiency costs, and hence will be disfavored by (potentially superintelligent) optimization and selection pressures.

- AI systems that develop AI systems are optimized and selected to produce components and architectures that perform well in applications (here, engineering design). As with basic R&D, off-task activities will incur efficiency costs, and hence will be disfavored.

- All systems, including system-design systems, consist of stable, task-focused components subject to upgrade based on aggregated application experience.

Note that none of these components has a task that includes optimizing either its own structure or a utility function over states of the world.

## Effective human oversight is not an impediment, but a source of value

The role of human oversight it to get what people want, and as such, identifying and satisfying human desires is not an impediment to design, but part of the design process. Comprehensive AI services can include the service of supporting effective human oversight, however, as discussed in [safety-oriented requirements for human oversight of basic AI R&D (algorithms, architectures, *etc.*) are minimal](→§24), and need not slow progress.

In design, as in other applications of AI technologies, effective human oversight is not enough to avoid enormous problems, because even systems that provide what people think they want can have adverse outcomes. Perversely seductive behaviors could serve the purposes of bad actors, or could arise through competition to develop systems that gain market share (consider the familiar drive to produce news that goes viral regardless of truth, and foods that stimulate appetite regardless of health).

## SI-level systems could solve more AI-control problems than they create

We want intelligent systems that help solve important problems, and should consider how superintelligent-level competencies could be applied to solve problems arising from superintelligence. There is no barrier to using AI to help solve problems of AI control: [Deceptive collusion among intelligent problem-solving systems would require peculiar and fragile preconditions](→§20). (The popular appeal of “us *vs.* them” framings of AI control is perhaps best understood as a kind of anthropomorphic tribalism.)

## Models of human concerns and (dis)approval can augment direct oversight

In guiding design, key resources will be *language comprehension* and [modeling anticipated human (dis)approval](→§22). Among the points of potential leverage:

- Strong priors on human concerns to ensure that important considerations are not overlooked.

- Strong priors on human approval to ensure that standard useful features are included by default.

- Strong priors on human disapproval to ensure that options with predictable but excessively negative unintended effects are dropped.

- Building on the above, effective elicitation of human intentions and preferences through interactive questioning and explanation of design options.

- Thorough exploration and reporting (to users and regulators) of potential risks, failure modes, and perverse consequences of a proposal.

- Ongoing monitoring of deployed systems to track unanticipated behaviors, failures, and perverse consequences.

## The pursuit of superintelligent-level AI design services need not entail classic AI-agent risks

To understand alternatives to superintelligent-AGI-agent models, it is best to start with fundamentals—intelligence as problem solving capacity, problems as tasks, AI systems as products of development, and recursive improvement as a process centered on technologies rather than agents. Interactive design tasks provide a natural model of superintelligent-level, real-world problem solving, and within this framework, classic AI-agent problems arise either in bounded contexts, or as a consequence of reckless choices in AI-system development.

## Further Reading

- §12 *AGI agents offer no compelling value*

- §20 *Collusion among superintelligent oracles can readily be avoided*

- §22 *Machine learning can develop predictive models of human approval*

- §23 *AI development systems can support effective human guidance*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

