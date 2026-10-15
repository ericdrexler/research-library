# §18 Reinforcement learning systems are not equivalent to reward-seeking agents

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 18 of 40. Source label: `reinforcement-not-reward`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** RL systems are (sometimes) used to train agents, but are not themselves agents that seek utility-like RL rewards.

**Cites sections:** §15 *Development-oriented models align with deeply-structured AI systems*; §16 *Aggregated experience and centralized learning support AI-agent applications*

**Cited by sections:** §II, §2, §6, §7, §17

---
## Summary

Reward-seeking reinforcement-learning agents can in some instances serve as models of utility-maximizing, self-modifying agents, but in current practice, RL systems are typically distinct from the agents they produce, and do not always employ utility-like RL rewards. In multi-task RL systems, for example, RL “rewards” serve not as sources of value to agents, but as signals that guide training, and unlike utility functions, RL “rewards” in these systems are neither additive nor commensurate. RL systems *per se* are not reward-seekers (instead, they *provide* rewards), but are instead running instances of algorithms that can be seen as evolving in competition with others, with implementations subject to variation and selection by developers. Thus, in current RL practice, developers, RL systems, and agents have distinct purposes and roles.

## Reinforcement learning systems differ sharply from utility-directed agents

Current AI safety discussions sometimes treat RL systems as agents that seek to maximize reward, and regard RL “reward” as analogous to a utility function. Current RL practice, however, diverges sharply from this model: RL systems comprise often-complex training mechanisms that are fundamentally distinct from the agents they produce, and RL rewards are not equivalent to utility functions.

## RL systems are neither trained agents nor RL-system developers

In current practice, RL systems and task-performing agents often do not behave as unitary “RL agents”; instead, trained agents are products of RL systems, while RL systems are products of a development process. Each of these levels (development processes, RL systems, and task-performing agents) is distinct in its implementation and implicit goals.

## RL systems do not seek RL rewards, and need not produce agents

RL-system actions include running agents in environments, recording results, and running RL algorithms to generate improved agent-controllers. These RL-system actions are not agent-actions, and rewards to agents are not rewards to RL systems. Running agents that collect rewards is a training cost, not a source of reward to the training system itself.

Note that the products of RL systems *need not be agents:* For example, researchers have applied RL systems to train mechanisms for attention in vision networks (K. Xu et al. 2015), to direct memory access in memory-augmented RNNs (Gülçehre, Chandar, and Bengio 2017), and (in meta-learning) to develop RL algorithms in RL systems (Duan et al. 2016; J. X. Wang et al. 2016). RL systems have also been used to design architectures for convolutional neural networks (Baker et al. 2016; Zoph and Le 2016) and LSTM-like recurrent cells for natural-language tasks (Zoph and Le 2016).

## RL rewards are not, in general, treated as increments in utility

“Reward” must not be confused with utility. In DeepMind’s work on multi-task learning, for example, agents are trained to play multiple Atari games with incommensurate reward-scores. Researchers have found that these heterogeneous “rewards” cannot be scaled and summed over tasks as if they were measures of utility, but must instead be adaptively adjusted to provide learning signals that are effective across different games and stages of training [ref]. RL rewards are sources of information and direction for RL systems, but are not sources of value for agents. Researchers often employ “reward shaping” to direct RL agents toward a goal, but the rewards used shape the agent’s behavior are conceptually distinct from the value of achieving the goal. [fn: For example, an RL system can learn a predictive model of a human observer’s approval at the level of actions, learning to perform difficult tasks without a specified goal or reward: see Christiano et al. (2017).]

## Experience aggregation blurs the concept of individual reward

Modern RL systems typically [aggregate experience](→§16) across multiple instances of agents that run in parallel in different environments. An agent-instance does not learn from “its own” experience, and aggregated experience may include off-policy actions that improve learning, yet impair reward-maximization for any given instance.

## RL algorithms implicitly compete for approval

RL algorithms have improved over time, not in response to RL rewards, but through research and development. If we adopt an agent-like perspective, RL algorithms can be viewed as competing in an evolutionary process where success or failure (being retained, modified, discarded, or published) depends on developers’ approval (not “reward”), which will consider not only current performance, but also assessed novelty and promise.

## Distinctions between system levels facilitate transparency and control

The patterns and distinctions described above (developer *vs.* learning system *vs.* agent) are not specific to RL, and from a development-oriented perspective, they seem generic. Although we can sometimes benefit from dropping these distinctions and exploring models of agent-like RL systems that seek utility-like rewards, current and future RL systems need not conform to those models. AI development practice suggests that we also consider how AI components and systems are architected, trained, combined, and applied. A [development-oriented perspective](→§15) focuses attention on structured processes, structured architectures, and potential points of control that may prove useful in developing safe applications of advanced AI technologies.

## RL-driven systems remain potentially dangerous

It should go without saying that RL algorithms could serve as engines driving perverse behavior on a large scale. For an unpleasantly realistic example, consider the potential consequences of giving an RL-driven system read/write access to the internet—including access to contemporaneous AI services—with the objective of maximizing the net flow of money into designated accounts. In this scenario, consider how the value of a short position could be increased by manipulating news or crashing a power grid. Distinctions between system levels offer affordances for control, yet levels can be collapsed, and having affordances for control in itself precludes neither accidents nor abuse.

## Further Reading

- §7 *Training agents in human-like environments can provide useful, bounded services*

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §16 *Aggregated experience and centralized learning support AI-agent applications*

- §35 *Predictable aspects of future knowledge can inform AI safety strategies*

- §36 *Desiderata and directions for interim AI safety guidelines*

- §40 *Could 1 PFLOP/s systems exceed the basic functional capacity of the human brain?*

