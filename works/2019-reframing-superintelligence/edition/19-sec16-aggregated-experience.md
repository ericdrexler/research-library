# §16 Aggregated experience and centralized learning support AI-agent applications

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 16 of 40. Source label: `aggregated-experience`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Centralized learning based on aggregated experience has strong advantages over local learning based on individual experience, and will likely dominate the development of advanced AI-agent applications.

**Cited by sections:** §II, §1, §2, §3, §5, §7, §14, §18, §23, §29, §36

---
## Summary

Since Turing, discussions of advanced AI have tacitly assumed that agents will learn and act as individuals; naïve scaling to multi-agent systems retains a human-like model centering on individual experience and learning. The development of self-driving vehicles, however, illustrates a sharply contrasting model in which aggregation of information across *N* agents (potentially thousands to millions) speeds the acquisition of experience by a factor of *N*, while centralized, large-scale resources are applied to training, and amortization reduces a range of per-agent costs by a factor of 1/*N*. In addition to advantages in speed and amortization, centralized learning enables pre-release testing for routinely encountered errors and ongoing updates in response to rarely-encountered events. The strong, generic advantages of aggregated experience and centralized learning have implications for our understanding of prospective AI-agent applications.

## Discussions often assume learning centered on individual agents

Advanced AI agents are often modeled as individual machines that learn tasks in an environment, perhaps with human supervision, along the lines suggested by Fig. 1. In human experience, human beings have been the sole intelligent agents in the world, a circumstance that powerfully reinforces our habit of identifying experience and learning with individual agents.

> **Figure 6.** Individual agents capable of open-ended learning would plan, act, and adapt their actions to a particular task environment, while building on individual experience to learn better methods for planning, acting, and adaptation (generic task learning).
> *(Image `fig8.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> The figure shows a single rounded-rectangle box on the left containing two columns of smaller rounded-rectangle boxes, three rows each. The left column, top to bottom, reads "Learning to plan," "Learning to act," and "Learning to adapt." The right column, aligned with the same three rows, reads "Planning," "Acting," and "Adapting." All six boxes sit inside the one outer enclosure, indicating they belong to a single agent.
>
> To the right of this enclosure is a separate box labeled "Environment." Two curved arrows connect the agent box to the Environment box: one arrow points from the agent (from the region of the "Planning"/"Acting" boxes) toward Environment and is labeled "Actions"; a second arrow points from Environment back toward the agent (toward the "Adapting" box) and is labeled "Observations." The layout thus depicts a closed loop in which the agent's planning, acting, and adapting processes drive actions on the environment, and observations from the environment feed back into the agent, while the paired "Learning to plan," "Learning to act," and "Learning to adapt" boxes represent the individual agent's own learning processes that improve each of those three capabilities from its own accumulated experience.

## Naïve scaling to multi-agent systems replicates individual agents

Naïve scaling of the individual-agent model to multiple agents does not fundamentally alter this picture (Fig 2). One can extend the environment of each agent to include other AI agents while retaining a human-like model of learning: Other agents play a role like that of other human beings.

> **Figure 7.** In a naïve scale-up of the scheme outlined in Fig. 1, *N* agents would plan, act, and adapt their actions to a range of similar task environments while learning from experience independently; both costs and benefits scale as *N*, and the time required to learn tasks remains unchanged.
> *(Image `fig9.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> The diagram shows a stack of identical, overlapping boxes (rendered as several overlapping card outlines with dotted corners top and bottom, indicating many repeated copies of a single agent structure), representing *N* separate agents each built on the same internal design. The front card of the stack is shown in full detail. Inside it are two columns of three rounded-rectangle boxes each. The left column, from top to bottom, reads "Learning to plan," "Learning to act," and "Learning to adapt." The right column, aligned beside them, reads "Planning," "Acting," and "Adapting." To the right of this pair of columns is a separate box labeled "Environment." An arrow labeled "Actions" runs from the "Planning"/"Acting"/"Adapting" column to "Environment," and a second arrow labeled "Observations" runs back from "Environment" to that column, showing the agent's action-observation loop with its task environment. Each agent's learning boxes ("Learning to plan," "Learning to act," "Learning to adapt") feed into its own corresponding action boxes ("Planning," "Acting," "Adapting") within that same card, indicating that learning is internal and local to each individual agent rather than shared across the stack.
>
> To the left of the stack, a list of four terms — "Individual experience," "Local training resources," "Per-unit learning costs," "In-use trials, errors" — labels the resources and experience associated with each individual agent in the stack. To the right of the stack, under the heading "Naïve scaling (*e.g.*, 10⁶ units):", three lines give the consequence of this design for a population of a million agents: "10⁶ independent agents," "10⁶ × trials, errors," and "10⁶ × learning cost." This indicates that because each agent's learning, training resources, and trial-and-error experience are separate and unshared, scaling up the number of agents multiplies these costs and requirements proportionally, in contrast to an aggregated-learning scheme.

## Self-driving vehicles illustrate the power of aggregating experience

Self-driving cars are agents that follow a quite different model: They do not learn as individuals, but instead deliver improved competencies through a centralized R&D process that draws on the operational experience of many vehicles. Tesla today produces cars with self-driving hardware at a rate of approximately 100,000 per year, steadily accelerating the accumulation of driving experience (termed “fleet learning”). Vehicle-agents that learned only from individual experience could not compete in performance or safety.

## Efficiently organized machine learning contrasts sharply with human learning

Machine learning contrasts sharply with human learning in its potential for efficiently aggregating experience, amortizing learning, applying population-based exploration (Conti et al. 2017), and reproducing and distributing competencies.

> **Experience can be aggregated.**  
> Among human beings, the ability to share detailed experiences is limited, and learning from others competes with learning from experience. In machine learning, by contrast, experience can be aggregated, and learning from aggregated experience need not compete with the acquisition of further experience.  
> **Learning can be accelerated and amortized.**  
> Among human beings, applying a thousand brains to learning does not reduce individual learning time or cost. In machine learning, by contrast, applying increasing computational capacity can reduce learning time, and computational costs can be amortized across an indefinitely large number of current and future systems.  
> **Competencies can be reproduced.**  
> Among human beings, training each additional individual is costly because competencies cannot be directly reproduced (hence learning elementary mathematics absorbs millions of person-years per year). In machine learning, learned competencies can be reproduced quickly at the cost of a software download.

> **Figure 8.** In large-scale agent applications, *N* agents (*e.g.* a thousand or a million) would independently plan, act, and adapt in a range of similar task environments, while aggregation of the resulting task experience enables data-rich learning supported by centralized development resources. Centralized learning enables upgraded agent software to be tested before release.
> *(Image `fig10.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> On the left, a box labeled with the text "Aggregated experience / Central training resources / Amortized learning costs / Pre-release trials, errors" stands beside a rounded rectangle containing three stacked sub-boxes: "Learning to plan," "Learning to act," and "Learning to adapt." Two thick gray arrows connect this central-learning box to a stack of agent diagrams at the upper right: one arrow points rightward from the learning box to the agent stack and is labeled "Software updates," and a second arrow points leftward from the agent stack back to the learning box, labeled "In-use experience."
>
> The upper-right cluster is a stack of overlapping identical diagrams (indicated by a trailing ellipsis, showing many repeated copies) representing agents in use. Each copy contains three sub-boxes, "Planning," "Acting," and "Adapting," alongside a separate "Environment" box; a black arrow labeled "Actions" runs from the Planning/Acting/Adapting group to the Environment box, and a second black arrow labeled "Observations" runs back from the Environment box to the Planning/Acting/Adapting group. Below this stack is the text "10^6 agents in use / 10^6 × experience per unit time."
>
> A second, similar stack of overlapping agent diagrams appears at the lower right, structured identically (Planning, Acting, Adapting boxes with Actions/Observations arrows to and from an Environment box), representing agents in testing; below it is the text "10^4 × agents in testing / 10^4 × experience per unit time." This lower-right testing stack connects to the central learning box via two vertical gray arrows: a downward arrow labeled "Test versions" pointing from the learning box down to the testing stack, and an upward arrow labeled "Testing results" pointing from the testing stack back up to the learning box.
>
> Compared to Figure 7, which shows N agents learning independently from their own experience with both costs and benefits scaling as N, this figure adds the central learning box that aggregates in-use experience from the large population of deployed agents (10^6) to drive centralized learning, and adds a separate, smaller population of agents in testing (10^4) that receive test versions of updated software and report testing results back to the central learning process before those updates are pushed out as software updates to the full deployed population.

## Aggregated learning speeds development and amortizes costs

With learning aggregated from *N* agents, the time required to gain a given quantity of experience scales as 1/*N,* potentially accelerating development of competencies. Further, the computation costs of training can be amortized over *N* agents, yielding a per-agent cost that scales as 1/*N*.

If common situations each require human advice when first encountered, the burden of supervising an independent agent might be intolerable, yet acceptably small when employing an agent trained with ongoing experience aggregated from a large-*N* deployment. Similarly, if the causes of novel errors can be promptly corrected, the per-agent probability of encountering a given error will be bounded by 1/*N.*

## The advantages of aggregated, amortized learning have implications for prospective AI-agent applications

The advantages of richer data sets, faster learning, and amortization of the costs of training and supervision all strongly favor development approaches that employ centralized, aggregated learning across deployments of agents that share similar tasks. These considerations highlight the importance of development-oriented models in understanding prospects for the emergence of broad-spectrum AI-agent applications.

## Further Reading

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §7 *Training agents in human-like environments can provide useful, bounded services*

- §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*

- §23 *AI development systems can support effective human guidance*

- §36 *Desiderata and directions for interim AI safety guidelines*

