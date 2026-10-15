# §39 Tiling task-space with AI services can provide general AI capabilities

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 39 of 40. Source label: `tiling-space`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Joint embedding of learned vector representations can be used to map tasks to services, enabling systems to provide general, extensible, seamlessly-integrated AI capabilities by exploiting the expertise of relatively narrow AI components.

**Cited by sections:** §II, §9

---
## Summary

Task-centered models of general AI capabilities highlight the importance of matching tasks to services, and current practice in deep learning suggests both conceptual models and concrete approaches. A surprisingly wide range of operations in deep-learning systems link “tasks” to “services” through what are—or can be construed as—proximity-based access operations in high-dimensional vector embedding spaces. Applications of proximity-based access include single-shot learning, situational memory in RL agents, mixture-of-experts models, and matching human queries to physical products across billion-scale product databases. In light of these diverse applications, it is natural to consider proximity in embedding spaces as a basis for scalable access to functional components at levels ranging from fine-grained perceptual tasks to integrated, high-level services visible to human users. Similar mechanisms could facilitate the implementation of new services both through adaptation of existing services and through development of new systems for novel tasks. Services can be seen tiles covering regions of task-space: Services of greater or lesser generality correspond to larger or smaller tiles, while services that adapt or develop services for novel tasks correspond to large tiles with greater initial latencies and task-specification requirements. The task-space model provides a conceptual, and perhaps practical, approach to implementing open-ended, asymptotically-comprehensive AI services as an effective form of general intelligence.

## Broad capabilities call for mechanisms that compose diverse competencies

Current AI systems are notoriously narrow, and expanding the scope of functionality of individual systems is a major focus of research. Despite progress, vision networks that recognize faces are still distinct from networks that classify images, which are distinct from networks that parse scenes into regions corresponding to objects of different kinds—to say nothing of the differences between any of these and networks architected and trained to play Go or translate languages or predict the properties of molecules. Because it would be surprising to find that any single network architecture will be optimal for proposing Go moves, *and* identifying faces, *and* translating English to French, it is natural to ask how diverse, relatively narrow systems could be composed to form systems that externally present broad, seamless competencies.

From this perspective, matching tasks (inputs and goals) to services (*e.g.*, trained networks) is central to developing broadly-applicable intelligent functionality, whether the required task-matching mechanisms provide coherence to services developed within a system through the differentiation of subtasks, or integrate services developed independently. This perspective equally applicable to “hard-wiring” task-to-service matching at development time and dynamic matching during process execution, and equally applicable to deep-learning approaches and services implemented by (for example) Google’s algorithm-agnostic AutoML. In practice, we should expect to see systems that exploit both static and dynamic matching, as well as specialized services implemented by relatively general service-development services (F.-F. Li and Li 2018). Algorithm selection has long been an active field (Kotthoff 2012; Mısır and Sebag 2017; Yang et al. 2018).

## The task-space concept suggests a model of integrated AI services

It is natural to think of services as populating task spaces in which similar services are neighbors and dissimilar services are distant, while broader services cover broader regions. This picture of services and task-spaces can be useful both as a *conceptual model* for thinking about broad AI competencies, and as a *potential mechanism* for implementing them.

1.  *As a conceptual model,* viewing services as tiling a high-dimensional task space provides a framework for considering the relationship between tasks and services: In the task-space model, the diverse properties that differentiate tasks are reflected in the high dimensionality of the task space, services of greater scope correspond to tiles of greater extent, and gaps between tiled regions correspond to services yet to be developed.

2.  *As an implementation mechanism,* jointly embedding task and service representations in high dimensional vector spaces could potentially facilitate matching of tasks to services, both statically during implementation and dynamically during execution. While there is good reason to think that joint embedding will be a useful implementation technique, the value of task spaces as a conceptual model would stand even if alternative implementation techniques prove to be superior.

The discussion that follows will explore the role of vector embeddings in modern AI systems, first, to support proposition (1) by illustrating the richness and generality of vector representations, and, second, to support proposition (2) by illustrating the range of areas in which proximity-based operations on vector representations already play fundamental roles in AI system implementation. With a relaxed notion of “space”, proposition (1) makes intuitive sense; the stronger proposition (2) requires closer examination.

## Embeddings in high-dimensional spaces provide powerful representations

This discussion will assume a general familiarity with the unreasonable effectiveness of high-dimensional vector representations in deep learning systems, while outlining some relevant developments. In brief, deep learning systems often encode complex and subtle representations of the objects of a domain (be it an image, video, text, product) as numerical vectors (“embeddings”) in spaces with tens to thousands of dimensions; the geometric relationships among embeddings encode relationships among the objects. In particular—given a successful embedding—similar objects (images of the same class, texts will similar meanings) map to vectors that are near neighbors in the embedding space.

Distances between vectors can be assigned in various ways: The most common in neural networks is cosine similarity, the inner product of vectors normalized to unit length; in high dimensional spaces, the cosine similarity between randomly-oriented vectors will, with high probability, be ≈0, while values substantially greater than 0 indicate relatively near neighbors. Distances in several other spaces have found use: The most common is Euclidian (L2) norm in conventional vector spaces, but more recent studies have employed Euclidian distance in toroidal spaces (placing bounds on distances while preserving translational symmetry (Ebisu and Ichise 2017)), and distances in hyperbolic spaces mapped onto the Poincare ball (the hyperbolic metric is particularly suited to a range of graph embeddings: it allows volume to grow exponentially with distance, much as the width of a balanced tree grows exponentially with depth) (Gülçehre et al. 2018; Tifrea, Bécigneul, and Ganea 2018). Spaces with different metrics and topologies (and their Cartesian products) may be suited to different roles, and individually-continuous spaces can of course be disjoint, and perhaps situated in a discrete taxonomic space.

## High-dimensional embeddings can represent semantically rich domains

In deep neural networks, every every vector that feeds into a fully-connected layer can be regarded as a vector-space embedding of some representation; examples include the top-level hidden layers in classifiers and intermediate encodings in encoder-decoder architectures. Applications of vector embedding have been extraordinarily broad, employing representations of:

- Images for classification tasks (Krizhevsky, Sutskever, and Hinton 2012)

- Images for captioning tasks (Vinyals et al. 2014)

- Sentences for translation tasks (Wu et al. 2016)

- Molecules for property-prediction tasks (Coley et al. 2017)

- Knowledge graphs for link-prediction tasks (Bordes et al. 2013)

- Products for e-commerce (J. Wang et al. 2018)

The successful application of vector embedding to diverse, semantically complex domains suggests that task-space models are not only coherent as a concept, but potentially useful in practice.

| **Encoding and decoding vector embeddings**                 |
|:------------------------------------------------------------|
| **Image classification:**                                   |
| Image → *CNN* → **embedding** → *projection matrix* → class |
| (Krizhevsky, Sutskever, and Hinton 2012)                    |
| **Image captioning:**                                       |
| Image → *CNN* → **embedding** → *RNN* → caption             |
| (Vinyals et al. 2014)                                       |
| **Language translation:**                                   |
| Sentence → *RNN* → **embedding** → *RNN* → translation      |
| (Wu et al. 2016)                                            |

## Proximity-based (application/activation/access) can deliver diverse services

Because applications may use neighborhood relationships to provide diverse functionality (here grouped under the elastic umbrella of “services”), the present discussion will refer to these collectively as “PBA operations”, where “PB” denotes “proximity-based”, and “A” can be interpreted as *application* of selected functions, *activation* of selected features, or more generically, *access* to (or retrieval of) selected entities. In each instance, PBA operations compute a measure of distance between a task representation embedding (“query”) and a pre-computed embedding (“key”) corresponding to the accessed feature, function, or entity (“value”). In other words, PBA operations employ key/value lookup of near neighbors in a vector space. As shorthand, one can speak of values has having positions defined by their corresponding keys.

PBA operations may access multiple entities; when these are (or produce) embedding vectors, it can be useful to weight and add them (*e.g.*, weighting by cosine similarity between query and key). Weighted PBA (wPBA) operations that discard distant values are PBAs in a strict sense, and assigning small weights to distant entities has a similar effect. The class of wPBA operations thus includes any matrix multiplication in which input and row (= query and key) vectors are actually or approximately normalized (see Salimans and Kingma (2016; C. Luo et al. 2017)), and the resulting activation vectors are sparse, *e.g.*, as a consequence of negatively biased ReLU units.

## PBA operations are pervasive in deep learning systems

PBA mechanisms should not be regarded as a clumsy add-on to neural computation; indeed, the above example shows that wPBA operations can be found at the heart of multilayer perceptrons. A wide range of deep learning systems apply (what can be construed as) PBA operations to access (what can be construed as) fine-grained “services” *within* a neural network computation. For example, wPBA mechanisms have been used implement not only mixture-of-experts models (Shazeer et al. 2017; Łukasz Kaiser, Gomez, et al. 2017), but also attention mechanisms responsible for wide-ranging advances in deep learning (Vaswani et al. 2017; Kool, van Hoof, and Welling 2018; Hudson and Manning 2018), including memories of past situations in RL agents (Wayne et al. 2018).

PBA mechanisms are prominent in single-shot learning in multiple domains (Łukasz Kaiser, Nachum, et al. 2017), including learning new image classes from a single example. In the latter application, networks are trained to map images to an embedding space that supports classification; single-shot learning is performed by mapping pairs of novel labels and embeddings to that same embedding space, enabling subsequent classification by retrieving the label of the best-matching embedding (“best-matching” means closeness, *e.g.*, cosine similarity) (Vinyals et al. 2016). In one implementation, this is accomplished by normalizing and inserting the embedding of a new example in a standard projection matrix (Qi, Brown, and Lowe 2017) (indeed, with suitable normalization, standard image classification architectures can be regarded as employing PBA).

## Joint embeddings can link related semantic domains

Embeddings can not only map similar entities to neighboring locations, but can also align distinct domains such that entities in one domain are mapped to locations near those of corresponding entities in the other (Frome et al. 2013; Y. Li et al. 2015; Baltrusaitis, Ahuja, and Morency 2017). Applications have been diverse:

- Text and images to enable image retrieval (K. Wang et al. 2016)

- Video and text to enable action recognition (X. Xu, Hospedales, and Gong 2017)

- Sounds and objects in video to learn cross-modal relationships (Arandjelović and Zisserman 2017)

- Images and recipes to retrieve one given the other (Salvador et al. 2017)

- Images and annotations to improve embeddings (Gong et al. 2014)

- Queries and factual statements to enable text-based question answering (Kumar et al. 2015)

- Articles and user-representations to recommend news stories (Okura et al. 2017)

- Product and user/query representations to recommend products (Zhang, Yao, and Sun 2017)

## PBA operations can help match tasks to candidate services at scale

The breadth of applications noted above suggests that AI services and tasks could be represented and aligned in vector embedding spaces. This observation shows that the task-space concept is (at the very least!) coherent, but also suggests that PBA operations are strong candidates for actually implementing task-service matching. This proposition is compatible with the use of disjoint embedding spaces for different classes of tasks, the application of further selection criteria not well represented by distance metrics, and the use of PBA operations in developing systems that hard-wire services to sources of streams of similar tasks.

In considering joint embeddings of tasks and services, one should imagine joint training to align the representations of both service-requesting and service-providing components. Such representations would encode the nature of the task (vision? planning? language?), domain of application (scene? face? animal?), narrower domain specifications (urban scene? desert scene? Martian scene?), kind of output (object classes? semantic segmentation? depth map? warning signal?), and further conditions and constraints (large model or small? low or high latency? low or high resolution? web-browsing or safety-critical application?).

Note that exploitation of specialized services by diverse higher-level systems is in itself a form of transfer learning: To train a service for a task in one context is to train it for similar tasks wherever they may arise. Further, the ability to find services that are near-matches to a task can provide trained networks that are candidates for fine-tuning, or (as discussed below) architectures that are likely to be well-suited to the task at hand (Vanschoren 2018).

The concept of joint task-to-service embeddings suggests directions for experimental exploration: How could embeddings of training sets contribute to embeddings of trained networks? Distributional shifts will correspond to displacement vectors in task space—could regularities in those shifts be learned and exploited in metalearning? Could relationships among task embeddings guide architecture search? Note that task-to-service relationships form a bipartite graph in which links can be labeled with performance metrics; in optimized embeddings, the distances between tasks and services will be predictive of performance.

PBA operations can be applied at scale: A recently developed graph-based, polylogarithmic algorithm running can return sets of 100 near neighbors from sets of \>10<sup>7</sup> vector embeddings with millisecond response times (single CPU) (Fu, Wang, and Cai 2017). Alibaba employs this algorithm for product recommendation at a scale of billions of items and customers (J. Wang et al. 2018).

## PBA operations can help match new tasks to service-development services

Fluid matching of tasks to services tends to blunt the urgency of maximizing the scope of individual models. Although models with more general capabilities correspond to broader tiles in task-space, the size of individual tiles does not determine the breadth of their aggregate scope. Advances in metalearning push in the same direction: A task that maps to a gap between tiles may still fall within the scope of a reliable metalearning process that can, on demand, fill that gap (Vanschoren 2018). A particular metalearning system (characterized by both architecture and training) would in effect constitute a broad but high-latency tile which has first-use costs that include both data and computational resources for training. Graphs representing deep learning architectures can themselves be embedded in continuous spaces (and, remarkably, can be optimized by gradient descent (R. Luo et al. 2018)); learning and exploiting joint embeddings of tasks and untrained architectures would be a natural step.

In an intuitive spatial picture, metalearning methods enable population of a parallel space of service-providing services, a kind of backstop for tasks that pass through gaps between tiles in the primary task-space. Taking this picture further, one can picture a deeper backstop characterized by yet broader, more costly tiles: This space would be populated by AI research and development systems applicable to broader domains; such systems might search spaces of architectures, training algorithms, and data sets in order to provide systems suitable for filling gaps in metalearning and primary-task spaces. AI R&D comprises many subtasks (architecture recommendation, algorithm selection, *etc.*) that can again be situated in appropriate task spaces; as with other high-level services, we should expect high-level AI-development services to operate by delegating tasks and coordinating other, narrower services.

One may speculate that systems that display flexible, general intelligence will, internally, link tasks to capabilities by mechanisms broadly similar those in today’s deep learning systems—which is to say, by mechanisms that can be construed as employing similarity of task and service embeddings in high-dimensional vector spaces. What is true of both multi-layer perceptrons and e-commerce recommendation systems is apt to be quite general.

## Integrated, extensible AI services constitute general artificial intelligence

The concept of “general intelligence” calls for a capacity to learn and apply an indefinitely broad range of knowledge and capabilities, including high-level capabilities such as engineering design, scientific inquiry, and long-term planning. The concept of comprehensive AI services is the same: The CAIS model calls for the capacity to develop and apply an indefinitely broad range of services that provide both knowledge and capabilities, again including high-level services such as engineering design, scientific inquiry, and long-term planning. In other words, broad, extensible, integrated CAIS in itself constitutes general artificial intelligence, differing from the familiar AGI picture chiefly in terminology, concreteness, and avoidance of the long-standing assumption that well-integrated general intelligence necessarily entails unitary agency.

## Further Reading

- §1 *R&D automation provides the most direct path to an intelligence explosion*

- §12 *AGI agents offer no compelling value*

