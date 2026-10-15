# §7 Training agents in human-like environments can provide useful, bounded services

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 7 of 40. Source label: `human-like`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Training agents with curiosity and imagination to perform human-like tasks in human-like environments can yield systems that provide bounded, human-like services.

**Cites sections:** §2 *Standard definitions of “superintelligence” conflate learning with competence*; §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*; §14 *The AI-services model brings ample risks*; §16 *Aggregated experience and centralized learning support AI-agent applications*; §18 *Reinforcement learning systems are not equivalent to reward-seeking agents*; §19 *The orthogonality thesis undercuts the generality of instrumental convergence*; §30 *Risky AI can help develop safe AI*; §38 *Broadly-capable systems coordinate narrower systems*

**Cited by sections:** §II

---
## Summary

Training agents on ill-defined human tasks may seem to be in conflict with developing distinct services provided by agents with bounded goals. Perceptions of conflict, however, seem rooted in anthropomorphic intuitions regarding connections between human-like skills and human-like goal structures, and more fundamentally, between learning and competence. These considerations are important to untangle because human-like training is arguably necessary to the achievement of important goals in AI research and applications, including adaptive physical competencies and perhaps general intelligence itself. Although performing safely-bounded tasks by applying skills learned through loosely-supervised exploration appears tractable, human-like world-oriented learning nonetheless brings unique risks.

## Does training on human-like tasks conflict with the AI-services model?

Discussions suggest that many researchers see training on human-like tasks as a critical goal that is potentially in conflict with the AI-services model of general intelligence. Human-like tasks in natural environments (whether real or simulated) are often ill-defined and open-ended; they call for exploration of possibilities and creative planning that goes beyond traditional reinforcement learning based on clearly-defined reward functions. The AI-services model, by contrast, emphasizes the role of focused skills applied to bounded goals aligned with human purposes.

An examination of the distinction between human-like skills and human-like goal structures reduces the this apparent conflict. Critical differences emerge through the distinction between [*intelligence as learning* and *intelligence as competence*](→§2),, the power of development architectures based on [aggregated experience and centralized learning](→§16), and the role of [application architectures in which tasks are naturally bounded](→§38).

## Human-like learning may be essential to developing general intelligence

General intelligence, in the sense of *general competence,* obviously includes human-like world-oriented knowledge and skills, and it would be surprising if these could be gained without human-like world-oriented learning. The practical value of human-like abilities is a major driving force behind AI research.

A more interesting question is whether human-like learning from human-like experience is essential to the development of general intelligence in the sense of *general learning ability.* This is a plausible hypothesis: Human intelligence is the only known example of what we consider to be general intelligence, and it emerged from open-ended interaction of humans with the world over the time spans of genetic, cultural, and individual development. Some researchers aim to reproduce this success by imitation.

Beyond the practical value of human-like learning, and the hypothesis that is may be essential to the development of general intelligence, there is a third reason to expect AI research to continue in this direction: Since Turing (1950), AI researchers have defined their objectives in terms of matching human capabilities in a broad sense, and have looked toward human-like learning, starting with child-like experience, as a natural path toward this goal.

## Current methods build curious, imaginative agents

In pursuit of AI systems that can guide agents in complex worlds (to date, usually simulated), researchers have developed algorithms that build abstracted models of the world and use these as a basis for “imagination” to enable planning, reducing the costs of learning from trial and error (Weber et al. 2017; Nair et al. 2018; Ha and Schmidhuber 2018; Wayne et al. 2018). Reinforcement-learning agents have difficulty learning complex sequences of actions guided only by end-state goals; an effective approach has been development of algorithms that have “curiosity”, seeking novel experiences and exploring actions of kinds that might be relevant to any of a range of potential goals (Pathak et al. 2017; Burda et al. 2018). Search guided by curiosity and imagination can adapt to novel situations and find unexpected solutions. Agents can also learn by observation of the real world, whether guided by demonstrations offered by human beings, or by imitating actions in relevant videos downloaded from the internet (Duan et al. 2017; Peng et al. 2018).

## Human-like competencies do not imply human-like goal structures

Human beings learn human goal structures, but full human goal structures—life goals, for example—do not emerge directly or naturally from applying curiosity, imagination, and imitation to learning even an unbounded range of bounded tasks. The idea that human-like problem-solving is tightly linked to human-like goals may stem from what are [tacitly biological background assumptions](→unresolved:tacitly-biological), [fn: [unresolved cross-reference in source: `tacitly-biological`]] including evolution under competition, learning from individual experience, unitary functionality, and even physical continuity. The abstraction of AI systems as rational utility-directed agents also proves, on examination, to draw on [tacitly anthropomorphic assumptions](→§5).

Even speaking of “agents learning”, as does the preceding section, is subject to this criticism. Humans learn by acting, but standard “reinforcement learning” methods sever this link: “Reinforcement learning” means training by a reinforcement learning algorithm, yet [this algorithm performs no actions, while a trained agent learns nothing by acting](→§18). Learning and action can of course be fused in a single system, yet they need not be, and [learning can be more effective when they are separate](→§16). Again, it is a mistake to [conflate *intelligence as learning capacity* with *intelligence as competence*](→§2).

## Open-ended learning can develop skills applicable to bounded tasks

In light of these considerations, it is natural and not necessarily problematic to pursue systems with general, human-like learning abilities as well as systems with collectively-general human-like competencies. Open-ended learning processes and general competencies do not imply problematic goals—and in particular, [do not necessarily engender convergent instrumental goals](→§19).

Even if the development of general intelligence though open-ended learning-to-learn entailed the development of opaque, unitary, problematic agents, [their capabilities could be applied to the development of compact systems](→§30) that retain general learning capabilities while lacking the kinds of information, competencies, and goals that fit the profile of a dangerous AGI agent. Note that extracting and refining skills from a trained system can be a less challenging development task than learning equivalent skills from experience alone.

## Human-like world-oriented learning nonetheless brings unique risks

These considerations suggest that there need be no direct line from human-like competencies to problematic goals, yet some human-like competencies are more problematic than, for example, expertise tightly focused on theorem proving or engineering design. Flexible, adaptive action in the physical world can enable disruptive competition in arenas that range from industrial parks to the battlefields. Flexible, adaptive action in the world of human information can support interventions that range from political manipulation to sheer absorption of human attention; the training objectives of the chatbot XiaoIce, for example, include engaging humans in supportive emotional relationships while maximizing the length of conversational exchanges (Zhou et al. 2018). She does this very well, and is continuing to learn.

[Adherence to the AI services model by no means guarantees benign behaviors or favorable world outcomes](→§14), even when applied with good intentions. Because of their potential for direct engagement with the world, however, human-like learning and capabilities present a special range of risks.

## Further Reading

- §2 *Standard definitions of “superintelligence” conflate learning with competence*

- §5 *Rational-agent models place intelligence in an implicitly anthropomorphic frame*

- §14 *The AI-services model brings ample risks*

- §16 *Aggregated experience and centralized learning support AI-agent applications*

- §17 *End-to-end reinforcement learning is compatible with the AI-services model*

- §21 *Broad world knowledge can support safe task performance*

