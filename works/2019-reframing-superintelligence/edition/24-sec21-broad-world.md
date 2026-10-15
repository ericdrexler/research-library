# §21 Broad world knowledge can support safe task performance

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 21 of 40. Source label: `broad-world`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Broad, deep knowledge about the world is compatible with safe, stable, high-level task performance, including applications that support AI safety.

**Cites sections:** §10 *R&D automation dissociates recursive improvement from AI agency*; §12 *AGI agents offer no compelling value*; §15 *Development-oriented models align with deeply-structured AI systems*; §22 *Machine learning can develop predictive models of human approval*; §24 *Human oversight need not impede fast, recursive AI technology improvement*; §40 *Could 1 PFLOP/s systems exceed the basic functional capacity of the human brain?*

**Cited by sections:** §II, §5, §6, §28

---
## Summary

Is strongly-bounded world knowledge necessary to ensure strongly-bounded AI behavior? Language translation shows otherwise: Machine translation (MT) systems are trained on general text corpora, and would ideally develop and apply extensive knowledge about the world, yet MT systems perform a well-bounded task, serving as functions of type T :: string → string. Broad knowledge and linguistic competencies can support (rather than undermine) AI safety by enabling systems to learn predictive models of human approval from large corpora.

## Bounding task focus does not require bounding world knowledge

Placing tight bounds on knowledge could be used to restrict AI competencies, and dividing broad AI tasks among components with restricted competencies could help to ensure AI safety (as discussed in Drexler (2015)), yet some tasks may require broad, integrated knowledge of the human world. General-purpose machine translation (MT) exemplifies a task that calls for integrated knowledge of indefinite scope, but also illustrates another, distinct mechanism for restricting competencies: Task-focused training (also discussed in Drexler (2015)).

## Extensive world knowledge can improve (*e.g.*) translation

Fully-general human-quality machine translation would require understanding diverse domains, which in turn would require knowledge pertaining to human motivations, cultural references, sports, technical subjects, and much more. As MT improves, there will be strong incentives to incorporate broader and deeper world knowledge.

## Current MT systems are trained on open-ended text corpora

Current neural machine translation (NMT) systems gain what is, in effect, knowledge of limited kinds yet indefinite scope through training on large, general text corpora. Google’s GNMT architecture has been trained on tens of millions of sentence pairs for experiments and on Google-internal production datasets for on-line application; the resulting trained systems established a new state-of-the-art, approaching the quality of “average human translators” (Wu et al. 2016).

Surprisingly, Google’s NMT architecture has been successfully trained, with little modification, to perform bidirectional translation for 12 language pairs (Johnson et al. 2016).

Although the system used no more parameters than the single-pair model (278 million parameters), the multilingual model achieves a performance “reasonably close” to the best single-pair models. Subsequent work (below) developed efficient yet greatly expanded multilingual models that improve on previous single-model performance.

## Current systems develop language-independent representations of meaning

NMT systems encode text into intermediate representations that are decoded into a target language. In Google’s multilingual systems, one can compare intermediate representations generated in translating sentences from multiple source languages to multiple targets. Researchers find that, for a given set of equivalent sentences (paired with multiple target languages), encodings cluster closely in the space of representations, while these clusters are well-separated from similar clusters that represent sets of equivalent sentences with a different meaning. The natural interpretation of this pattern is that sentence-encodings represent meaning in a form that is substantially independent of any particular language.

(It may prove fruitful to train similar NMT models on sets of pairs of equivalent sentences while providing an auxiliary loss function that pushes representations within clusters toward closer alignment. One would expect training methods with this auxiliary objective to produce higher-quality language-independent representations of sentence meaning, potentially providing an improved basis for learning abstract relationships.)

## Scalable MT approaches could potentially exploit extensive world knowledge

NMT systems can represent linguistic knowledge in sets of specialized “experts”, and Google’s recently described “Sparsely-Gated Mixture-of-Experts” (MoE) approach (Shazeer et al. 2017) employs sets of sets of experts, in effect treating sets of experts as higher-order experts. Human experience suggests that hierarchical organizations of experts could in principle (with suitable architectures and training methods) learn and apply knowledge that extends beyond vocabulary, grammar, and idiom to history, molecular biology, and mathematics.

Notably, Google’s MoE system, in which “different experts tend to become highly specialized based on syntax and semantics” has enabled efficient training and application of “outrageously large neural networks” that achieve “greater than 1000× improvements in model capacity [137 billion parameters] with only minor losses in computational efficiency on modern GPU clusters”. ([There is reason to think that these systems exceed the computational capacity of the human brain.](→§40))

## Specialized modules can be trained on diverse, overlapping domains

As suggested by the MoE approach in NMT, domain-specialized expertise can be exploited without seeking to establish clear domain boundaries that might support safety mechanisms. For example, it is natural to expect that efficient and effective training will focus on the learning the concepts and language of chemistry (for training some modules), of history (for training others), and of mathematics (for yet others). It is also natural to expect that training modules for expertise in translating chemistry textbooks would benefit from allowing them to exploit models trained on math texts, while performance in the history of chemistry would benefit from access to models trained on chemistry and on general history. [Current practice and the structure of prospective task domains](→§15) suggests that optimal partitioning of training and expertise would be soft, and chosen to improve efficiency and effectiveness, not to restrict the capabilities of any part.

## Safe task focus is compatible with broad, SI-level world knowledge

Machine translation systems today are not agents in any conventional sense of the word, and are products of advances in an AI-development infrastructure, not of open-ended “self improvement” of any distinct system. As we have seen, domain-specific task focus is, in this instance, a robust and natural consequence of optimization and training for a specific task, while high competence in performing that task, employing open-ended knowledge, does not impair the stability and well-bounded scope of the translation task.

It is reasonable to expect that [a wide range of other tasks can follow the same basic model](→§12), though the range of tasks that would naturally (or could potentially) have this character is an open question. We can expect that broad knowledge will be valuable and (in itself) non-threatening when applied to tasks that range in scope from driving automobiles to engineering urban transportation systems.

Further, broad understanding based on large corpora could contribute to [predictive models of human approval](→§22) that provide rich priors for assessing the desirability (or acceptability) of proposed plans for action by agent, helping to solve a range of problems in aligning AI behaviors with human values. By contrast, similar understanding applied to, for example, unconstrained profit maximization by autonomous corporations, could engender enormous risks.

## Strong task focus does not require formal task specification

The MT task illustrates how a development-oriented perspective can reframe fundamental questions of task specification. In MT development, we find systems (now [significantly automated](→§10) (Britz et al. 2017)) that develop MT architectures, systems that train those architectures, and ([providing services outside R&D labs](→§24)) the trained-and-deployed MT systems themselves. The nature and scope of the MT task is implicit in the associated training data, objective functions, resource constraints, efficiency metrics, *etc.*, while tasks of the systems that develop MT systems are indirectly implicit in that same MT task (together with metalevel resource constraints, efficiency metrics, *etc.*). Nowhere in this task structure is there a formal specification of what it means to translate a language, or a need to formally circumscribe and limit the task.

## Further Reading

- §2 *Standard definitions of “superintelligence” conflate learning with competence*

- §7 *Training agents in human-like environments can provide useful, bounded services*

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §22 *Machine learning can develop predictive models of human approval*

- §23 *AI development systems can support effective human guidance*

- §35 *Predictable aspects of future knowledge can inform AI safety strategies*

