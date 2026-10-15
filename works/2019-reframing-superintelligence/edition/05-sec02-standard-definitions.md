# §2 Standard definitions of “superintelligence” conflate learning with competence

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 2 of 40. Source label: `standard-definitions`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** By implicitly conflating learning with competence, standard definitions of “superintelligence” fail to capture what we mean by “intelligence” and obscure much of the potential solution space for AI control problems.

**Cites sections:** §12 *AGI agents offer no compelling value*; §16 *Aggregated experience and centralized learning support AI-agent applications*; §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*; §20 *Collusion among superintelligent oracles can readily be avoided*

**Cited by sections:** §II, §6, §7, §9, §17, §30

---
## Summary

Since Good (1966), superhuman intelligence has been equated with superhuman intellectual competence, yet this definition misses what we mean by *human* intelligence. A child is considered intelligent because of learning capacity, not competence, while an expert is considered intelligent because of competence, not learning capacity. Learning capacity and competent performance are distinct characteristics in human beings, and are routinely separated in AI development. Distinguishing *learning* from *competence* is crucial to understanding both prospects for AI development and potential mechanisms for controlling superintelligent-level AI systems.

## Superintelligence has been defined in terms of adult human competence

Good (1966) defined “ultraintelligence” in terms of distinct, highly competent entities:

> Let an ultraintelligent machine be defined as a machine that can far surpass all the intellectual activities of any man however clever.

The standard definition of “superintelligence” today (Bostrom 2014) parallels Good (1966), yet to define *superintelligence* in terms of adult intellectual competence fails to capture what we mean by *human* intelligence.

## “Intelligence” often refers instead to learning capacity

Consider what we mean when we call a person intelligent:

- A child is considered “intelligent” because of learning capacity, not competence.

- An expert is considered “intelligent” because of competence, not learning capacity.

We can overlook this distinction in the human world because learning and competence are deeply intertwined in human intellectual activities; in considering prospects for AI, by contrast, regarding “intelligence” as entailing both learning and competence invites deep misconceptions.

## Learning and competence are separable in principle and practice

A human expert in science, engineering, or AI research might provide brilliant solutions to problems, and even if a drug or neurological defect blocked the expert’s formation of long-term memories, we would recognize the expert’s intelligence. Thus, even in humans, competence can in principle be dissociated from ongoing learning, while in AI technology, this separation is simply standard practice. Regardless of implementation technologies, each released version of an AI system can be a fixed, stable software object.

Reinforcement learning agents illustrate the separation between learning and competence: Reinforcement “rewards” are signals that shape learned behavior, yet play no role in performance. [Trained RL agents exercise their competencies without receiving reward](→§18).

## Patterns of AI learning and competence differ radically from humans’

AI systems and human beings differ radically in how learning, knowledge transfer, competence, and experience are connected:

| **Aspect**                  | **In humans**          | **In AI systems**    |
|:----------------------------|:-----------------------|:---------------------|
| *Performance and learning:* | Unified                | Separable            |
| *Nature of experience:*     | Individual, sequential | Aggregated, parallel |
| *Learning from experience:* | Inherent               | Optional             |
| *Knowledge transfer:*       | Instruction, study     | Download             |

In short, AI systems can act without learning, learn without acting, and transfer knowledge without instruction or study; further, machine learning can draw on the [aggregated, parallel experience](→§16) of indefinitely large numbers of performing systems, which can then be upgraded by downloading new software.

## Distinguishing learning from competence is crucial to understanding potential AI control strategies

Ensuring relatively predictable, constrained behavior is fundamental to AI control. The tacit assumption that the exercise of competence entails learning implies that an intelligent system must be mutable, which is to say, potentially unstable. Further, the tacit assumption that intelligence entails both learning and competence invites the misconception that AI systems capable of learning will necessarily have complex states and capabilities that might be poorly understood.

As this might suggest, conflating intelligence, competence, and learning obscures much of the potential solution space for of AI control problems (*e.g.*, approaches to architecting [trustworthy composite oracles](→§20)). [→ §20 *Collusion among superintelligent oracles can readily be avoided*] This problematic, subtly anthropomorphic model of intelligence is deeply embedded in current discussion of AI prospects. If we are to think clearly about AI control problems, then even [comprehensive, superintelligent-level AI capabilities](→§12) must not be equated with “superintelligence” as usually envisioned.

## Further Reading

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §7 *Training agents in human-like environments can provide useful, bounded services*

- §15 *Development-oriented models align with deeply-structured AI systems*

- §16 *Aggregated experience and centralized learning support AI-agent applications*

- §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*

- §21 *Broad world knowledge can support safe task performance*

- §30 *Risky AI can help develop safe AI*

