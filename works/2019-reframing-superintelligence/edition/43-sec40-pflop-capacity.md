# §40 Could 1 PFLOP/s systems exceed the basic functional capacity of the human brain?

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 40 of 40. Source label: `pflop-capacity`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Multiple comparisons between narrow AI tasks and narrow neural tasks concur in suggesting that PFLOP/s computational systems exceed the basic functional capacity of the human brain.

**Cited by sections:** §II, §21, §35

---
## Summary

Neurally-inspired AI systems implement a range of narrow yet recognizably human-like competencies, hence their computational costs and capabilities can provide evidence regarding the computational requirements of hypothetical systems that could deliver more general human-like competencies at human-like speeds. The present analysis relies on evidence linking task functionality to resource requirements in machines and biological systems, making no assumptions regarding the nature of neural structure or activity.

Comparisons in areas that include vision, speech recognition, and language translation suggest that affordable commercial systems (~1 PFLOP/s, costing $150,000 in 2017) may surpass brain-equivalent computational capacity, perhaps by a substantial margin. Greater resources can be applied to learning, and the associated computational costs can be amortized across multiple performance-providing systems; current experience suggests that deep neural network (DNN) training can be fast by human standards, as measured by wall-clock time. In light of these considerations, it is reasonable to expect that, given suitable software, affordable systems will be able to perform human-level tasks at superhuman speeds.

## Metrics and methodology

### AI-technology performance metrics include both task *competencies* and task *throughput*

Hypothetical AI software that could perform tasks with human-level (or better) competence, in terms of scope and quality, would be constrained by contemporaneous computational capacity, and hence might perform with less-than-human task throughput; if so, then restricted hardware capacity might substantially blunt the practical implications of qualitative advances in AI software. By contrast, if advanced competencies were developed in the context of better-than-human hardware capacity (“hardware overhang”), then the practical implications of qualitative advances in AI software could potentially be much greater. A better understanding of the computational requirements for human-level performance (considering both competence and throughput) would enable a better understanding of AI prospects.

### Ratios of hardware capacities and neural capacities (considered separately) compare apples to apples

The following analysis references an imperfect measure of real-world hardware capacity—floating-point performance—yet because it considers only *ratios* of capacity between broadly-similar systems applied to broadly-similar tasks, the analysis implicitly (though approximately) reflects cross-cutting considerations such as constraints on memory bandwidth. Thus, despite referencing an imperfect measure of hardware capacity, the present methodology compares apples to apples.

The neural side of the analysis is similar in this regard, considering only *ratios* of (estimates of) neural activity required for task performance relative to activity in the brain as a whole; these ratio-estimates are imperfect, but again compare apples to apples. Note that this approach avoids dubious comparisons of radically different phenomena such as synapse firing and logic operations, or axonal signaling and digital data transmission. Neural structure and function is treated as a black box (as is AI software).

In the end, the quantity of interest (an estimate of machine capacity/brain capacity) will be expressed as a ratio of dimensionless ratios.

### Laboratory-affordable AI hardware capacity reached ~1 PFLOP/s in 2017.

In 2017, NVIDIA introduced a 960 TFLOP/s “deep-learning supercomputer” (a 5.6× faster successor to their 2016 DGX-1 machine), at a price of

$150,000; a high-end 2017 supercomputer (Sunway TaihuLight) delivers ~100 PFLOP/s; a high-end 2017 gaming GPU delivers ~0.01 PFLOP/s. The following discussion will take 1 PFLOP/s as a reference value for current laboratory-affordable AI hardware capacity.

### The computational cost of machine tasks scaled to human-like throughput is reasonably well defined

Consider machine tasks that are narrow in scope, yet human-comparable in quality: For a given machine task and implementation (*e.g.*, of image classification), one can combine a reported computational cost (in FLOP/s) and reported throughput (*e.g.*, frames per second) to define a cost scaled to human-like task-throughput (*e.g.*, image classification at 10 frames per second). Call this the “machine-task cost”, which will be given as a fraction of a PFLOP/s.

### Narrow AI tasks provide points of reference for linking computational costs to neural resource requirements

AI technologies based on neurally-inspired DNNs have achieved human-comparable capabilities on narrow tasks in domains that include vision, speech recognition, and language translation. It is difficult to formulate accurate, quantitative comparisons that link the known computational costs of narrow AI tasks to the resource costs of similar (yet never equivalent) neural tasks, yet for any given task comparison, one can encapsulate the relevant ambiguities and uncertainties in a single dimensionless parameter, and can consider the implications of alternative assumptions regarding its value.

A key concept in the following will be “immediate neural activity” (INA), an informal measure of *potentially task-applicable* brain activity. As a measure of current neural activity *potentially* applicable to task performance, INA is to be interpreted in an abstract, information-processing sense that conceptually excludes the formation of long-term memories (as discussed below, human and machine learning are currently organized in fundamentally different ways).

The estimates of *task-applied* INA in this section employ cortical volumes that could be refined through closer study of the literature; a point of conservatism in these estimates is their neglect of the differential, task-focused patterns of neural activity that make fMRI informative (Heeger and Ress 2002). Differential activation of neural tissue for different tasks is analogous to the use of gated mixture-of-experts models in DNNs: In both cases, a managerial function selects and differentially activates task-relevant resources from a potentially much larger pool. In DNN applications (*e.g.*, language translation), a gated mixture-of-experts approach can increase model capacity by a factor of 100 to 1000 with little increase in computational cost (Shazeer et al. 2017).

### The concept of a “task-INA fraction” encapsulates the key uncertainties and ambiguities inherent in linking machine-task costs to brain capacity

The present discussion employs the concept of a “task-INA fraction” ($f_{INA}$), the ratio between the INA that would (hypothetically) be required for a neural system to perform a given machine task and the contemporaneous global INA of a human brain (which may at a given moment support vision, motor function, auditory perception, higher-level cognition, *etc.*). This ratio encapsulates the main ambiguities and uncertainties in the chain of inference that links empirical machine performance to estimates of the requirements for human-equivalent computation. These ambiguities and uncertainties are substantial: Because no actual neural system performs the same task as a machine, any comparison of machine tasks to neural tasks can at best be approximate.

For example, convolutional neural networks (CNNs) closely parallel the human visual system in extracting image features, but the functional overlap between machine and neural tasks dwindles and disappears at higher levels of processing that, in CNNs, may terminate with object segmentation and classification. Potentially quantifiable differences between CNN and human visual processing include field of view, resolution, and effective frame rate. More difficult to disentangle or quantify, however, is the portion of visual-task INA that should be attributed to narrow CNN-like feature extraction, given that even low-level visual processing is intertwined with inputs that include feedback from higher levels, together with more general contextual and attentional information (Heeger and Ress 2002).

Ambiguities and uncertainties of this kind increase when we consider tasks such as machine speech transcription (which is partially auditory and partially linguistic, but at a low semantic level), or language translation that is human-comparable in quality (Wu et al. 2016), yet employs a very limited representation of language-independent meaning (Johnson et al. 2016).

### Uncertainties and ambiguities regarding values of $f_{INA}$ are bounded

Despite these uncertainties and definitional ambiguities, there will always be bounds on plausible values of $f_{INA}$ for various tasks. For, example, given that visual cortex occupies ~20% of the brain and devotes substantial resources to CNN-like aspects of feature extraction, it would be difficult to argue that the value of $f_{INA}$ for CNN-like aspects of early visual processing is greater than 0.1 or less than 0.001. However, rather than emphasizing specific estimates of $f_{INA}$ for specific machine tasks, the method of analysis adopted here invites the reader to consider the plausibility of a range of values based on some combination of knowledge from the neurosciences, introspection, and personal judgment. As we will see, even loose bounds on values of $f_{INA}$ can support significant conclusions.

For a given task, a useful, empirically-based benchmark for comparison is the “PFLOP-parity INA faction” ($f_{PFLOP}$), which is simply the ratio of the empirical machine-task cost to a 1 PFLOP/s machine capacity. If the lowest plausible value of $f_{INA}$ lies above the PFLOP-parity INA-faction for that same task, this suggests that a 1 PFLOP/s machine exceeds human capacity by a factor of $R_{PFLOP} = \frac{f_{INA}}{f_{PFLOP}}$.

> **Figure 11.** Diagram of neural and computational costs as fractions of total resources (above), scaling the totals to align the fractions (below).
> *(Image `fig11.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)*
>
> The diagram has two stacked panels. In the upper panel, two long horizontal rectangular bars are shown one above the other, each representing a total resource with a labeled fraction marked off inside it. The top bar is introduced by the label "Machine task cost (a known quantity for a given task)," with a curved arrow pointing into the left end of the bar, where a small segment is marked off and labeled "f_PFLOP"; beneath the bar is the caption "Total reference-machine capacity (= 1 PFLOP/s)." The second bar, of the same length, is introduced by the label "'Equivalent task' INA (an uncertain estimate of a fuzzy quantity)," again with a curved arrow pointing into its left end, where a segment is marked off and labeled "f_INA"; this segment is drawn with a wavy/squiggly line (rather than a crisp boundary) to indicate its fuzziness, and beneath the bar is the caption "Total immediate neural activity (INA)."
>
> The lower panel, headed "Scaled to match:", repeats the two bars but rescaled so that the two marked-off fractions (f_PFLOP and f_INA) are drawn to the same absolute length as each other, even though the two full bars (total reference-machine capacity and total INA) are now of different lengths — the f_PFLOP bar is shown noticeably longer overall than the f_INA bar, illustrating that a larger total machine capacity is needed to match the (smaller, fuzzy) f_INA segment to the same absolute size as f_PFLOP. Below these two rescaled bars is the line "Implied capacity relationship:" followed by the equation f_INA / f_PFLOP = R_PFLOP = (Total machine capacity) / (Total neural capacity), where the right-hand ratio is written as a fraction with "Total machine capacity" over "Total neural capacity."

## Estimated ratios for specific machine tasks

*(Numbers in this section are rounded vigorously to avoid spurious implications of precision.)*

### Image-processing tasks vs. human vision tasks: 

Systems based on Google’s Inception architecture implement high-level feature extraction of a quality that supports comparable-to-human performance in discriminating among 1000 image classes. At a human-like 10 frames per second, the machine-task cost would be ~10 GFLOP/s (Szegedy et al. 2014), hence $f_{PFLOP} = ~10^{-5}$.

Turning to neural function, consider that visual cortex comprises

\>10% of the human brain. If Inception-like high-level feature extraction were to require the equivalent of ~1% of visual cortex, then $f_Z{INA} = ~10^{-3}$, and $R_{PFLOP} = ~100$.

#### Speech-recognition tasks vs. human auditory/linguistic tasks:

Baidu’s Deep Speech 2 system can approach or exceed human accuracy in recognizing and transcribing spoken English and Mandarin, and would require approximately 1 GFLOP/s per real-time speech stream (Amodei et al. 2015). For this roughly human-level throughput, $f_{PFLOP} = 10^{-6}$.

Turning to neural function again, consider that task-relevant auditory/semantic cortex probably comprises \>1% of the human brain. If the equivalent of the Deep Speech 2 speech-recognition task were to require 10% of that cortex, then $f_{INA} = ~10^{-3}$, and $R_{PFLOP} = ~1000$.

#### Language-translation tasks vs. human language comprehension tasks:

Google’s neural machine translation (NMT) systems have reportedly approached human quality (Wu et al. 2016). A multi-lingual version of the Google NMT model (which operates with the same resources) bridges language pairs through a seemingly language-independent representation of sentence meaning (Johnson et al. 2016), suggesting substantial (though unquantifiable) semantic depth in the intermediate processing. Performing translation at a human-like rate of one sentence per second would require approximately 100 GFLOP/s, and $f_{PFLOP} = 10^{-4}$.

It is *plausible* that (to the extent that such things can be distinguished) human beings mobilize as much as 1% of global INA at an “NMT task-level”—involving vocabulary, syntax, and idiom, but not broader understanding—when performing language translation. If so, then for “NMT-equivalent translation,” we can propose $f_{INA} = ~10^{-2}$, implying $R_{PFLOP} = ~100$.

#### Robotic vision vs. retinal visual processing:

Hans Moravec applies a different yet methodologically similar analysis (Moravec 1998) that can serve as a cross-check on the above values. Moravec noted that both retinal visual processing and functionally-similar robot-vision programs are likely to be efficiently implemented in their respective media, enabling a comparison between the computational capacity of digital and neural systems. Taking computational requirements for retina-level robot vision as a baseline, then scaling from the volume of the retina to the volume of the brain, Moravec derives the equivalent of $R_{PFLOP}$ = ~10 (if we take MIP/s ~ MFLOP/s). Thus, the estimates here overlap with Moravec’s. In the brain, however, typical INA per unit volume is presumably less that that of activated retina, and a reasonable adjustment for this difference would suggest $R_{PFLOP}$ \> 100.

### It seems likely that 1 PFLOP/s machines equal or exceed the human brain in raw computation capacity

In light of the above comparisons, all of which yield values of $R_{PFLOP}$ in the 10 to 1000 range, it seems likely that 1 PFLOP/s machines equal or exceed the human brain in raw computation capacity. To draw the opposite conclusion would require that the equivalents of a *wide range* of seemingly substantial perceptual and cognitive tasks would *consistently* require no more than an *implausibly small fraction* of total neural activity.

The functional-capacity approach adopted here yields estimates that differ substantially, and sometimes greatly, from estimates based on proposed correspondences between neural activity and digital computation. Sandberg and Bostrom (Sandberg and Bostrom 2008), for example, consider brain emulation at several levels: analog neural network populations, spiking neural networks, and neural electrophysiology; the respective implied $R_{PFLOP}$ values are 1, $10^{-3}$, and $10^{-7}$. Again based on a proposed neural-computational correspondence, Kurzweil suggests the equivalent of $R_{PFLOP} = 0.1$ (Kurzweil 2005).

## Even with current methods, training can be fast by human standards

The discussion above addresses only task performance, but DNN technologies also invite a comparisons of machine and human learning speeds.

Human beings require months to years to learn to recognize objects, to recognize and transcribe speech, and to learn vocabulary and translate languages. Given abundant data and 1 PFLOP/s of processing power, the deep learning systems referenced above could be trained in hours (image and speech recognition, ~10 exaFLOPs) to weeks (translation, ~1000 exaFLOPs). These training times are short by human standards, which suggests that future learning algorithms running on 1 PFLOP/s systems could rapidly learn task domains of substantial scope. A recent systematic study shows that the scale of efficient parallelism in DNN training increases as tasks grow more complex, suggesting that training times could remain moderate even as product capabilities increase (McCandlish et al. 2018).

## Large computational costs for training need not substantially undercut the implications of low costs for applications

Several considerations strengthen the practical implications of fast training, even if training for broad tasks were to require more extensive machine resources:

- More that 1 PFLOP/s can be applied to training for narrow AI tasks.

- Because broad capabilities can often be composed by coordinating narrower capabilities, parallel, loosely-coupled training processes may be effective in avoiding potential bottlenecks in learning broader AI tasks.

- In contrast to human learning, machine training costs can be amortized over an indefinitely large number of task-performing systems, hence training systems could be costly without undercutting the practical implications of high task-throughput with affordable hardware.

Human beings (unlike most current DNNs) can learn from single examples, and because algorithms with broad human-level competencies will (almost by definition) reflect solutions to this problem, we can expect the applicable training methods to be more efficient than those discussed above. Progress in “single-shot learning” is already substantial.

Note that hardware-oriented comparisons of speed do not address the qualitative shortcomings of current DNN training methods (*e.g.*, limited generalization, requirements for enormous amounts of training data). The discussion here addresses only quantitative measures (learning speed, task throughput).

## Conclusions

Many modern AI tasks, although narrow, are comparable to narrow capacities of neural systems in the human brain. Given an empirical value for the fraction of computational resources required to perform that task with human-like throughput on a 1 PFLOP/s machine, and an inherently uncertain and ambiguous—yet bounded—estimate of the fraction of brain resources required to perform “the equivalent” of that machine task, we can estimate the ratio of PFLOP/s machine capacity to brain capacity. What are in the author’s judgment plausible estimates for each task are consistent in suggesting that this ratio is ~10 or more. Machine learning and human learning differ in their relationship to costs, but even large machine learning costs can be amortized over an indefinitely large number of task-performing systems and application events.

In light of these considerations, we should expect that substantially superhuman computational capacity will accompany the eventual emergence of a software with broad functional competencies. On present evidence, scenarios that assume otherwise seem unlikely.

## Further Reading

- §12 *AGI agents offer no compelling value*

- §23 *AI development systems can support effective human guidance*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

- §36 *Desiderata and directions for interim AI safety guidelines*

