# §36 Desiderata and directions for interim AI safety guidelines

*Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition). Section 36 of 40. Source label: `interim-desiderata`. Rendered PDF: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad*

**Thesis.** Interim AI safety guidelines should (and could) engage with present practice, place little burden on practitioners, foster future safety-oriented development, and promote an ongoing process of guideline development and adoption.

**Cites sections:** §15 *Development-oriented models align with deeply-structured AI systems*; §16 *Aggregated experience and centralized learning support AI-agent applications*; §35 *Predictable aspects of future knowledge can inform AI safety strategies*

**Cited by sections:** §II, §30

---
## Summary

Actionable, effective interim AI safety guidelines should:

- Clarify why current AI research is safe,

- Promote continued safety-enabling development practice, and

- Foster ongoing, collaborative guideline development and adoption.

Because current AI development work is, in fact, safe with respect to high-level risks, interim safety guidelines can clarify and codify safety-aligned characteristics of current work while placing little burden on practitioners. Good practice in current AI R&D tends to align with longer-term safety concerns: Examples include learning from the exploration of families of architectures and tasks, then pursuing task-oriented development, testing, and validation before building complex deployed systems. These practices can contribute to shaping and controlling AI capabilities across a range of potential development paths. Development and adoption of guidelines founded on current practice could help researchers answer public questions about the safety of their work while fostering ongoing, collaborative safety research and guideline extension to address potential longer-term, high-level risks.

## Desiderata

### *Desideratum:* Clarify why current AI research is safe

Current AI research is safe (in a classic x-risk sense), in part because current AI capabilities are limited, but also because of the way capabilities are developed and organized. Interim guidelines could clarify and codify aspects of current practice that promote foundational aspects of safety (see below), and thereby support efforts to identify safe paths to more powerful capabilities.

### *Desideratum:* Promote continued safety-enabling development practice

Guidelines that focus on safety-promoting aspects of current practice can be crafted to place little burden on what is already safety-compliant research; these same safety-promoting practices can contribute to (though not in themselves ensure) avoiding hazards in more challenging future situations.

### *Desideratum:* Foster ongoing, collaborative guideline development and adoption

Collaboration on actionable interim safety guidelines could promote closer links between development- and safety-oriented AI researchers, fostering ongoing collaborative, forward-looking guideline development. Beginning with readily-actionable guidelines can help to ensure that collaboration goes beyond theory and talk.

## Good practice in development tends to align with safety concerns

Fortunately (though unsurprisingly) good practice in AI development tends to align with safety concerns. In particular, developers seek to ensure that AI systems behave predictably, a characteristic that contributes to safety even when imperfect.

## Exploring families of architectures and tasks builds practical knowledge

In AI R&D, we see extensive exploration of families of architectures and tasks through which developers gain practical knowledge regarding the capabilities and (conversely) limitations of various kinds of systems; practical experience also yields an understanding of the kinds of surprises to be expected from these systems. Guidelines that highlight [the role of present and future practical knowledge](→§35) would clarify why current research is known to be safe, and how good development practice can contribute to future safety.

## Task-oriented development and testing improve both reliability and safety

Systems for practical applications perform bounded tasks and are subject to testing and validation before deployment. Task-oriented development, testing, and validation contribute to knowledge of capabilities and focus strongly-motivated attention on understanding potential failures and surprises. Guidelines that codify this aspect of current practice would again help to clarify conditions that contribute to current and future safety.

## Modular architectures make systems more understandable and predictable

Systems are more easily designed, developed, tested, and upgraded when they are composed of distinct parts, which is to say, when their architectures are modular rather than opaque and undifferentiated. This kind of structure is ubiquitous in complex systems. (And as noted in a recent paper from Google, “Only a small fraction of real-world ML systems is composed of the ML code […] The required surrounding infrastructure is vast and complex.” (Sculley et al. 2015)) In particular, the [distinction between AI development systems and their products](→§15) enables [a range of reliability (hence safety) oriented practices](→§16). The use of modular architectures in current practice again suggests opportunities for codification, explanation, and contributions to future safety.

## Interim safety guidelines can foster ongoing progress

The absence of current safety risks sets a low bar for the effectiveness of interim guidelines, yet guidelines organized around current practice can contribute to the development of guidelines that address more challenging future concerns. At a technical level, practices that support reliability in narrow AI components can provide foundations for the safe implementation of more capable systems. At an institutional level, linking current practice to longer-term concerns can foster safety-oriented research and development in several ways: by encouraging understanding and extension of what today constitutes good practice, by engaging the development community in ongoing guideline development, and by focusing greater research attention on the potential connections between development processes and safe outcomes. Interim guidelines cannot solve all problems, yet could help to set our work on a productive path.

## Further Reading

- §10 *R&D automation dissociates recursive improvement from AI agency*

- §12 *AGI agents offer no compelling value*

- §22 *Machine learning can develop predictive models of human approval*

- §23 *AI development systems can support effective human guidance*

- §24 *Human oversight need not impede fast, recursive AI technology improvement*

- §35 *Predictable aspects of future knowledge can inform AI safety strategies*

