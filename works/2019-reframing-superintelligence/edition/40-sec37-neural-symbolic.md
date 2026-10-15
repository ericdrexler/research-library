# §37 How do neural and symbolic technologies mesh?

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 37 of 40. Source label: `neural-symbolic`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Neural networks and symbolic/algorithmic AI technologies are complements, not alternatives; they are being integrated in multiple ways at levels that range from components and algorithms to system architectures.

---
## Summary

Neural network (NN) and symbolic/algorithmic (S/A) AI technologies offer complementary strengths, and these strengths can be combined in multiple ways. A loosely-structured taxonomy distinguishes several levels of organization (components, algorithms, and architectures), and within each of these, diverse modes of integration—various functional relationships among components, patterns of use in applications, and roles in architectures. The complexity and fuzziness of the taxonomy outlined below emphasizes the breadth, depth, and extensibility of current and potential NN–S/A integration.

## Motivation

One might imagine that neural network and symbolic/algorithmic technologies are in competition, and ask whether NNs can fulfill the grand promise of artificial intelligence when S/A methods have failed—will NN technologies also fall short?

On closer examination, however, the situation looks quite different: NN and S/A technologies are not merely in competition, they are complementary, compatible, and increasingly integrated in research and applications. To formulate a realistic view of AI prospects requires a general sense of the relationship between NN and S/A technologies. Discussions in this area are typically more narrow: They either focus on a problem domain and explore applicable NN–S/A techniques, or they focus on a technique and explore potential applications. The discussion here will instead outline the *expanding range of techniques and applications,* surveying patterns of development that may help us to better anticipate technological opportunities and the trajectory of AI development.

## A crisp taxonomy of NN and S/A systems is elusive and unnecessary

There is no sharp and natural criterion that distinguishes NN from S/A techniques. For purposes of discussion, one can regard a technique as NN-style to the extent that it processes numerical, semantically-opaque vector representations through a series of transformations in which operations and data-flow patterns are fixed. Conversely, one can regard a technique as S/A-style to the extent that it relies on entities and operations that have distinct meanings and functions, organized in space and time in patterns that manifestly correspond to the structure of the problem at hand—patterns comprising data structures, memory accesses, control flow, and so on.

Note that S/A *implementation mechanisms* should not be mistaken for S/A *systems:* S/A code can implement NN systems much as hardware implements software, and just as code cannot usefully be reduced to hardware, so NNs cannot usefully be reduced to code. In the present context, however, the systems of greatest interest are those that deeply integrate NN- and S/A-style mechanisms, or that blur the NN–S/A distinction itself. If taxonomy were clean and easily constructed, prospects for NN–S/A integration would be less interesting.

## NN and S/A techniques are complementary

The contrasting strengths of classic S/A techniques and emerging NN techniques are well known: S/A-style AI techniques have encountered difficulties in perception and learning, areas in which NN techniques excel; NN–style AI techniques, by contrast, often struggle with tasks like logic-based reasoning—and even counting—that are trivial for S/A systems.

In machine translation, for example, algorithms based on symbolic representations of syntax and semantics fell short of their promise (even when augmented by statistical methods applied to large corpora); more recently, neural machine translation systems with soft, opaque representations have taken the lead, yet often struggle with syntactic structure and the semantics of logical entailment.

S/A systems are relatively transparent, in part because S/A systems embody documentable, human-generated representations and algorithms, while NN systems instead discover and process opaque representations in ways that do not correspond to interpretable algorithms. The integration of NN techniques with S/A systems can sometimes facilitate interpretability, however: For example, NN operations may be more comprehensible when considered as functional blocks in S/A architectures, while (in sometimes amounts to a figure-ground reversal) comprehensible S/A systems can operate on NN outputs distilled into symbols or meaningful numerical values.

## AI-service development can scale to comprehensive, SI-level services

In discussing how NN and S/A techniques mesh, it will be convenient to draw rough distinctions between three levels of application:

#### Components and mechanisms,

where NN and S/A building blocks interact at the level of relatively basic programming constructs (*e.g.*, data access, function calls, branch selection).

#### Algorithmic and representational structures,

where NN and S/A techniques are systematically intwined to implement complex representations or behaviors (*e.g.*, search, conditional computation, message-passing algorithms, graphical models, logical inference).

#### Systems and subsystems,

where individually-complex NN and S/A subsystems play distinct and complementary roles at an architectural level (*e.g.*, perception and reasoning, simulation and planning).

The discussion below outlines several modes of NN–S/A integration at each level, each illustrated by an unsystematic sampling of examples from the literature. No claim is made that the modes are sharply defined, mutually exclusive, or collectively exhaustive, or that particular examples currently outperform alternative methods. The focus here is on patterns of integration and proofs of concept.

## Integration at the level of components and mechanisms

What are conceptually low-level components may have downward- or upward-facing connections to complex systems: Components that perform simple functions may encapsulate complex NN or S/A mechanisms, while simple functions may serve as building blocks in higher-level algorithmic and representational structures (as discussed in the following section).

### NNs can provide representations processed by S/A systems:

Classic AI algorithms manipulate representations based on scalars or symbolic tokens; in some instances (discussed below), systems can retain the architecture of these algorithms—patterns of control and data flow—while exploiting richer NN representations. For example, the modular, fully-differentiable visual question answering architecture of (Hu et al. 2018) employs S/A-style mechanisms (sets of distinct, compositional operators that pass data on a stack), but the data-objects are patterns of soft attention over an image.

### NNs can direct S/A control and data flow:

In AI applications, S/A algorithms often must select execution paths in an “intelligent” way. NNs can process rich information (*e.g.*, large sets of conventional variables, or NN vector embeddings computed upstream), producing Boolean or integer values that can direct these S/A choices. NN-directed control flow is fundamental to the NN-based search and planning algorithms noted below.

### S/A mechanisms can direct NN control and data flow:

Conversely, S/A mechanisms can structure NN computations by choosing among alternative NN components and operation sequences. Conditional S/A-directed NN operations enable a range of NN–S/A integration patterns discussed below.

### NNs can learn heuristics for S/A variables:

Reinforcement learning ML mechanisms be applied to what are essentially heuristic computations (*e.g.*, binary search, Quicksort, and cache replacement) by computing a value base on a observations (the values of other variables). This approach embeds ML in a few lines of code to “integrate ML tightly into algorithms whereas traditional ML systems are build around the model” (Carbune et al. 2017).

### NNs can replace complex S/A functions:

Conventional algorithms may call functions that perform costly numerical calculations that give precise results when approximate results would suffice. In the so-called “parrot transformation” (Esmaeilzadeh et al. 2012), an NN is trained to mimic and replace the costly function. NNs that (approximately) model the trajectories of physical systems (Ehrhardt et al. 2017) could play a similar role by replacing costly simulators.

### NNs can employ complex S/A functions:

Standard deep learning algorithms learn by gradient descent on linear vector transformations composed with simple, manifestly-differentiable element-wise functions (ReLU, tanh, *etc.*), yet complex, internally non-differentiable algorithms can also implement differentiable functions. These functions can provide novel functionality: For example, a recent deep-learning architecture (OptNet) treats constrained, exact quadratic optimization as a layer, and can learn to solve Sudoku puzzles from examples (Amos and Kolter 2017). When considered as functions, the outputs of complex numerical models of physical systems can have a similar differentiable character.

### S/A algorithms can extend NN memory:

Classic NN algorithms have limited representational capacity, a problem that becomes acute for recurrent networks that must process long sequences of inputs or represent an indefinitely large body of information. NNs can be augmented with scalable, non-differentiable (hard-attention) or structured memory mechanisms (Sukhbaatar et al. 2015; Chandar et al. 2016) that enable storage and retrieval operations in an essentially S/A style.

### S/A data structures can enable scaling of NN representations:

Data structures developed to extend the scope of practical representations in S/A systems can be adapted to NN systems. Hash tables and tree structures can support sparse storage for memory networks, for example, and complex data structures (octrees) enable generative convolutional networks to output fine-grained 3D representations that would otherwise require impractically large arrays (Tatarchenko, Dosovitskiy, and Brox 2017); access to external address spaces has proved critical to solving complex, structured problems (Graves et al. 2016). Brute-force nearest-neighbor lookup (*e.g.*, in NN embedding spaces) is widely used in single-shot and few-shot learning (see below); recent algorithmic advances based on neighbor graphs enable retrieval of near neighbors from billion-scale data sets in milliseconds (Fu, Wang, and Cai 2017).

### S/A mechanisms can template NN mechanisms:

In a more abstract relationship between domains, S/A-style mechanisms can be implemented in a wholly differentiable, NN form. Examples include pointer networks (Vinyals, Fortunato, and Jaitly 2015) that (imperfectly) solve classic S/A problems such as Traveling Salesman and Delaunay triangulation, as well as differentiable stacks that can perform well on NLP problems (e.g., syntactic transformations (Grefenstette et al. 2015) and dependency parsing (Dyer et al. 2015)) commonly addressed by recursive, tree-structured algorithms in S/A systems.

## Integration at the level of algorithmic and representational structures

Higher-level integration of NN and S/A mechanisms can typically be viewed as patterns of interleaved NN and S/A operations, sometimes with substantial, exposed complexity in one or both components.

### S/A algorithms can extend NN inference mechanisms:

S/A mechanisms are often applied to decode NN outputs. For example, beam search in is a classic algorithm in symbolic AI, and is applied in neural machine translation systems to select sequences of symbols (*e.g.*, words) based on soft distributions over potential sequence elements. In another class of algorithms, S/A algorithms are applied to find near-neighbors among sets of vector outputs stored in external memory, supporting one- and few-shot learning in classifiers (Vinyals et al. 2016; Snell, Swersky, and Zemel 2017).

### NNs can guide S/A search:

Both search over large spaces of choices (Go play) and large bodies of data (the internet ) and are now addressed by traditional S/A methods (Monte Carlo tree search (Silver et al. 2016), large-scale database search (Clark 2015)) guided by NN choices. Recent work has integrated tree-based planning methods with NN “intuition” and end-to-end learning to guide agent behaviors (Anthony, Tian, and Barber 2017; Farquhar et al. 2017; Guez et al. 2018).

### S/A graphical models can employ NN functionality:

An emerging class of graphical models—message-passing NNs—represents both node states and messages as vector embeddings. Message-passing NNs share the discrete, problem-oriented structures of probabilistic graphical models, but have found a far wider range of applications, including the prediction of molecular properties (Gilmer et al. 2017), few-shot learning (Garcia and Bruna 2017), and inferring structured representations (Johnson et al. 2016), as well as algorithms that outperform conventional loopy belief propagation (Yoon et al. 2018), and others that can *infer causality from statistical data* beyond the limits that might be suggested by Pearl’s formalism (Goudet et al. 2017). Vicarious has demonstrated integration of perceptual evidence through a combination of NN-level pattern recognition and loopy graphical models: “Recursive Cortical Networks” can generalize far better than conventional NNs, and from far less training data (George et al. 2017).

### S/A mechanisms can structure NN computation:

S/A mechanisms are used both to construct specified graphs and to execute corresponding message-passing algorithms, while *specification* of graph-structured NNs is a task well-suited to mixed NN and S/A mechanisms. For example, S/A and NN mechanisms have been interleaved to compose and search over alternative tree-structured NNs that implement generative models of 3D structures (Jun Li et al. 2017). In a very different example (a visual question-answering task), an S/A parsing mechanism directs the assembly of question-specific deep networks from smaller NN modules (Hu et al. 2018); see also Andreas et al. (2016). A similar strategy is employed in the Neural Rule Engine (S. Li, Xu, and Lu 2018), while Yi et al. (2018) employs NN mechanisms to parse scenes and questions into symbolic representations that drive a symbolic execution engine.

### NNs can produce and apply S/A representations:

NN mechanisms can learn discrete, symbol-like representations useful in reasoning, planning, and predictive learning (Oord, Vinyals, and Kavukcuoglu 2017; Raiman and Raiman 2018), including string encodings of molecular-structure graphs for chemical synthesis (Segler, Preuß, and Waller 2017) and drug discovery (Merk et al. 2018). S/A representations can enforce a strong inductive bias toward generalization; for example, deep RL systems can formulate and apply symbolic rules (Garnelo, Arulkumaran, and Shanahan 2016), and NN techniques can be combined with inductive logic programming to enable the inference of universal rules from noisy data (Evans and Grefenstette 2018).

### S/A algorithms can template NN algorithms:

S/A representations can readily implement geometric models with parts, wholes, and relationships among distinct objects. In recent NN architectures, “capsules” (Sabour, Frosst, and Hinton 2017) and similar components (Liao and Poggio 2017) can both support image recognition and play a symbol-like role in representing part-whole relationships; architectures that embody relation-oriented priors can both recognize objects and reason about their relationships (Hu et al. 2018) or model their physical interactions (Battaglia et al. 2016; Chang et al. 2016). The neural architectures that accomplish these tasks follow (though not closely!) patterns found in S/A information processing. More broadly, there is a recognized trend of learning differentiable versions of familiar algorithms (Guez et al. 2018).

### NNs can learn S/A algorithms:

In neural program induction, NNs are trained to replicate the input-output behavior of S/A programs. Several architectures (e.g., the Neural Turing Machine (Graves, Wayne, and Danihelka 2014), Neural GPU (Ł. Kaiser and Sutskever 2015), and Neural Programmer (Neelakantan, Le, and Sutskever 2015); reviewed in Kant (2018)) have yielded substantial success on simple algorithms, with (usually imperfect) generalization to problem-instances larger than those in the training set.

### NNs can aid S/A program synthesis:

Automatic programming is a long-standing goal in AI research, but progress has been slow. Mixed S/A–NN methods have been applied to program synthesis (Yin and Neubig 2017; Singh and Kohli 2017; Abolafia et al. 2018), with increasing success (reviewed in (Kant 2018)). Potential low-hanging fruit includes adaptation of existing source code (Allamanis and Brockschmidt 2017) and aiding human programmers by code completion (Jian Li et al. 2017); automating the development of glue code would facilitate integration of existing S/A functionality with other S/A and NN components.

We can anticipate that advances in graph NNs will facilitate the exploitation of richer structures in code, which has traditionally centered on narrower syntactic representations. Structures latent in S/A code, but to date not explored *in conjunction,* include not only abstract syntax trees, data types, and function types, but control and data flow graphs *(May 2018 update: see Allamanis, Brockschmidt, and Khademi (2018)).*

### NNs can aid automated theorem proving:

Automated theorem proving systems perform heuristic search over potential proof trees, and deep-learning methods have been applied to improve premise selection (Irving et al. 2016; Kaliszyk, Chollet, and Szegedy 2017). Progress in automated theorem proving (and proof assistants) could facilitate the development of provably correct programs and operating systems (Klein et al. 2014).

### S/A mechanisms can support NN architecture and hyperparameter search:

New tools for architecture and hyperparameter search are accelerating NN development by discovering new architectures (Zoph and Le 2016; Pham et al. 2018) and optimizing hyperparameters (Jaderberg et al. 2017) (a key task in architecture development). Leading methods in architecture search apply NN or evolutionary algorithms to propose candidate architectures, while using an S/A infrastructure to construct and test them.

## Integration at the level of systems and subsystems

Integration at the level of systems and subsystems extends the patterns already discussed, combining larger blocks of NN and S/A functionality.

### NNs can support and ground S/A models:

Perceptual processing has been chronically weak in S/A artificial intelligence, and NN techniques provide a natural complement. NN-based machine vision applications in robotics and vehicle automation are expanding (Steger, Ulrich, and Wiedemann 2007), and NN-based modeling can go beyond object recognition by, for example, enabling the inference of physical properties of objects from video (Watters et al. 2017). With the integration of NN perception and symbolic representations, symbol-systems can be grounded.

### S/A representations can direct NN agents:

In recent work, deep RL has been combined with symbolic programs, enabling the implementation of agents that learn correspondences between programs, properties, and objects through observation and action; these capabilities can be exploited in systems that learn to ground and execute explicit, human-written programs (Denil et al. 2017). The underlying principles should generalize widely, improving human abilities to inform, direct, and understand behaviors that exploit the strengths of deep RL.

### NNs can exploit S/A models and tools:

Looking forward, we can anticipate that NN systems, like human beings, will be able to employ state-of-the-art S/A computational tools, for example, using conventional code that implements physical models, image rendering, symbolic mathematics and so on. NN systems can interact with S/A systems though interfaces that are, at worst, like those we use today.

### NN and S/A models can be integrated in cognitive architectures:

At a grand architectural level, AI researchers have long envisioned and proposed “cognitive architectures” (Soar, LIDA, ACT-R, CLARION…) intended to model much of the functionality of the human mind. A recent review (Kotseruba, Gonzalez, and Tsotsos 2016) identifies 84 such architectures, including 49 that are still under active development. Recent work in cognitive architectures has explored the integration of S/A and NN mechanisms (Besold et al. 2017), an approach that could potentially overcome difficulties that have frustrated previous efforts.

## Integration of NN and S/A techniques is a rich and active research frontier

An informal assessment suggests robust growth in the literature on integration of NN and S/A techniques. It is, however, worth noting that there are incentives to focus research efforts primarily on one or the other. The most obvious incentive is intellectual investment: Crossover research requires the application of disparate knowledge, while more specialized knowledge is typically in greater supply for reasons of history, institutional structure, and personal investment costs. These considerations tend to suggest an undersupply of crossover research.

There is, however, good reason to focus extensive effort on NN systems that that *do not* integrate S/A techniques in a strong, algorithmic sense: We do not yet know the limits of NN techniques, and research that applies NNs in a relatively pure form—end-to-end, *tabula rasa* training with S/A code providing only infrastructure or framework elements—seems the best way to explore the NN frontier. Even if one expects integrated systems to dominate the world of applications, relatively pure NN research may be the most efficient way to develop the NN building blocks for those applications.

As in many fields of endeavour, it is important to recognize the contrasts between effective methodologies in research and engineering: In particular, good basic research explores systems that are novel, unpredictable, and (preferably) simple, while good engineering favors known, reliable building blocks to construct systems that are as complex as a task may require. Accordingly, as technologies progress from research to applications, we can expect to see increasing—and increasingly eclectic—integration of NN and S/A techniques, providing capabilities that might otherwise be beyond our reach.

## Further Reading

- §I *Introduction: From R&D automation to comprehensive AI Services*

- §II *Overview: Questions, propositions, and topics*

