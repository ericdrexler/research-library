# Verification record — Phase 1 (mechanical conversion)

Checks applied to this edition, 2026-09-10.

1. **Structure counts.** Source: 42 numbered `\section` + 4 unnumbered (Preface, Abstract, Afterword, Acknowledgements) → 46 section files. 192 `\fn` footnotes in the source: 33 substantive footnotes inlined as `[fn: …]`; 159 were bare section cross-references, of which 151 duplicated an adjacent `[phrase](→§N)` link and were dropped, 8 are rendered as `[→ §N *Title*]`. 11 figure environments → 11 figure blocks (10 images described, 1 text-only reproduced). 5 tables → 5 Markdown tables. 143 distinct citation keys → 143 entries in `references.md`.
2. **Sentence-level presence.** Every sentence of ≥8 words in the de-TeXed source was checked for presence in the edition by 5-word-window coverage (1,673 sentences). All sentences ≥50% covered; the five lowest-coverage cases were inspected and are link-dense sentences that are fully present.
3. **Macro residue.** No unresolved LaTeX commands remain except `\frac` inside one intentionally retained math expression (§40).
4. **Cross-reference resolution.** All `\SecRef`/`\hyperref` targets resolve to PDF section numbers, except the source's own dangling reference to a nonexistent section `tacitly-biological` (§7; noted in README).
5. **Model fidelity review (Sonnet), three sections compared paragraph-by-paragraph against the LaTeX:** §II (list-heavy overview) — one formatting defect found and fixed (nested emphasis in a cited title); §20 (footnotes, labeled lists) — one content loss found and fixed (pandoc had dropped the A1)–C5) list labels that the prose refers back to); §40 (math, numbers, tables, URLs) — clean. Both defects were systemic classes, fixed in the converter, and all sections regenerated.
6. **Figure descriptions** are single-pass model output from the image plus section context; they have not yet been cross-checked against each other or the text (not done).

Not done: independent per-section fidelity review of all 46 files; multi-sample figure descriptions; typo audit against the source (source typos such as "perform perform", "could could", "the ability run" are preserved verbatim here, as they are in the PDF).
