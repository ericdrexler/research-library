# §25 Optimized advice need not be optimized to induce its acceptance

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 25 of 40. Source label: `optimized-advice`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Advice optimized to produce *results* may be manipulative, optimized to induce a client’s acceptance; advice optimized to produce results *conditioned on its acceptance* will be neutral in this regard.

**Cites sections:** §10 *R&D automation dissociates recursive improvement from AI agency*; §22 *Machine learning can develop predictive models of human approval*

**Cited by sections:** §II, §27, §29

---
## Summary

To optimize advice to produce a result entails optimizing the advice to ensure its acceptance, and hence to manipulate the clients’ choices. Advice can instead be optimized to produce a result *conditioned on the advice being accepted;* because the expected value of an outcome conditioned on an action is independent of the probability of the action, there is then no value in manipulating clients’ choices. In an illustrative (and practical) case, a client may request advice on options that offer different trade-offs between expected costs, benefits, and risks; optimization of these options does not entail optimization to manipulate a client’s choice among them. Manipulation remains a concern, however: In a competitive situation, the most popular systems may optimize advice for seduction rather than value. Absent effective counter-pressures, competition often will (as it already does) favor the deployment of AI systems that strongly manipulate human choices.

## Background (1): Classic concerns

“Oracles” (Bostrom 2014) are a proposed class of high-level AI systems that would provide answers in response to queries by clients; in the present context, oracles that provide advice on how to achieve goals are of particular interest. It has sometimes been suggested that oracles would be safer than comparable agents that act in the world directly, but because oracles inevitably affect the world through their clients’ actions, the oracle/agent distinction *per se* can blur. To clarify this situation, it is important to consider (without claiming novelty of either argument or result) whether optimizing oracles to produce effective advice entails their optimizing advice to affect the world.

## Background (2): Development-oriented models

In [the RDA-process model](→§10), *research* produces basic components and techniques, *development* produces functional systems, and *application* produces results for users. In AI development, an advisory oracle will be optimized for some purpose by a chain of systems that are each optimized for a purpose:

- ***AI research*** optimizes components and techniques to enable development of diverse, effective AI systems.

- ***Advisory-oracle development*** optimizes systems to suggest options for action across some range of situations and objectives.

- ***Advisory-oracle application*** suggests actions optimized to achieve given objectives in specific situations.

Each stage in an RDA process yields products (components, oracles, advice) optimized with respect to performance metrics (a.k.a. loss functions).

## Optimization *for results* favors manipulating clients’ decisions

Giving advice may itself be an action intended to produce results in the world. To optimize advice to produce a result, however, entails optimizing the advice to ensure that the advice is applied. In current human practice, advice is often intended to manipulate a client’s behavior to achieve the advisor’s objective, and a superintelligent-level AI advisor could potentially do this very well. At a minimum, an oracle that optimizes advice to produce results can be expected to distort assessments of costs, benefits, and risks to encourage fallible clients to implement supposedly “optimal” policies. A range of standard AI-agent safety problems (*e.g.*, perverse instantiation and pursuit of convergent instrumental goals) then arise with full force.

Optimizing oracles to produce advice intended to produce results seems like a bad idea. We want to produce oracles that are not designed to deceive.

## Optimization for results *conditioned on actions* does not entail optimization to manipulate clients’ decisions

Oracles could instead be optimized to offer advice that in turn is optimized, not to produce results, but to produce results contingent on the advice being applied. Because the expected value of an outcome conditioned on an action is independent of the probability of the action, optimal advice will not be optimized to manipulate clients’ behavior.

## Oracles can suggest options with projected costs, benefits, and risks

Because human beings have preferences that are not necessarily reducible to known or consistent utility functions, it will be natural to ask advisory-oracles to suggest and explain sets of options that offer different, potentially incommensurate combinations of costs, benefits, and risks; thus, useful advice need not be optimized to maximize a predefined utility function, but can instead be judged by Pareto-optimality criteria. With optimization of outcomes conditioned on acceptance, the quality of assessment of costs, benefits, and risks will be limited by AI competencies, undistorted by a conflicting objective to manipulate clients’ choices among alternatives. (Note that the burden of avoiding options that perversely instantiate objectives rests on [the quality of the options and their assessment](→§22), not on the avoidance of choice-manipulation.)

## Competitive pressures may nonetheless favor AI systems that produce perversely appealing messages

If multiple AI developers (or development systems) are in competition, and if their success is measured by demand for AI systems’ outputs, then the resulting incentives are perverse: Advice that maximizes appeal will often be harmful, just as news stories that maximize attention often are false.

Because AI-enabled communications will permit radical scaling of deception in pursuit of profit and power, it seems likely that *human-driven* applications of these capabilities will be the leading concern as we move forward in AI technology. It seems likely that effective countermeasures will likewise require AI-enabled communication that influences large audiences.

## Further Reading

- §20 *Collusion among superintelligent oracles can readily be avoided*

- §21 *Broad world knowledge can support safe task performance*

- §22 *Machine learning can develop predictive models of human approval*

- §23 *AI development systems can support effective human guidance*

