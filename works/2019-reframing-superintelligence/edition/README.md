# README — Reframing Superintelligence: Comprehensive AI Services as General Intelligence — K. Eric Drexler, FHI Technical Report #2019-1 (Markdown edition)

This folder is a model-friendly Markdown edition of the FHI technical report, converted mechanically from the author's LaTeX source (`main.tex`, 2019; 42 sections, 192 footnotes, ~54,000 words). The rendered PDF is authoritative for typography and page references: https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad (Oxford Research Archive).

## Files

- `README.md` — this file.
- `index.md` — table of contents with each section's thesis, figure list, and a ranking of most-cited sections.
- `NN-secMM-label.md` — one file per section (NN = file sequence, MM = section number as printed in the PDF; sections I and II are the introduction and overview; 1–40 are the topical sections). Front and back matter (abstract, preface, afterword, acknowledgements) have their own files.
- `references.md` — the works cited, Chicago author-date, as in the PDF.
- `full.md` — all of the above concatenated in reading order, for single-file upload (~474 KB).

## Conventions

- **Headers.** Each section file opens with an edition line, the section's **Thesis** (the author's one-sentence summary, set as an epigraph in the PDF), **Cites sections** (sections this one cross-references in its body), and **Cited by sections** (sections whose bodies cross-reference this one). Further Reading lists at section ends are the author's and are excluded from these counts.
- **Cross-references.** The PDF hyperlinks a phrase to another section and adds a footnote naming it. Here the phrase is written `[phrase](→§N)`; the footnote is dropped when it only repeats the target. A bare cross-reference footnote (no linked phrase) appears as `[→ §N *Title*]`.
- **Footnotes** are inlined at their point of attachment as `[fn: …]`, so a section file is self-contained.
- **Citations** are inline author–date, e.g. (Bostrom 2014, 107); full entries are in `references.md`.
- **Figures.** Images are not included. Each figure appears as a blockquote with its number (as in the PDF) and caption, followed by an italic line giving the source image filename and marking what follows as editorial: *"(Image `figN.png` in the source; not reproduced here. The description below is editorial — a model-written first pass — not the author's text.)"* The description paragraphs follow in the same blockquote. Image filenames do not always match figure numbers (for example, Figure 6 is `fig8.png`). Descriptions are interpretive aids, not the author's text. Figure 5 is text-only in the source; its content is reproduced verbatim above the caption, which is followed instead by *"(Text-only figure; content reproduced above.)"*
- **§36** lacks the thesis epigraph formatting in the source (the sentence is a plain first paragraph in the PDF); it is placed in the header here like the others.
- **Section numbering** follows the PDF (I, II, then 1–40); subsection headings are unnumbered, as in the source.
- **Emphasis, quotation marks, tables, and math** follow the source; a few LaTeX math expressions remain in `$…$` notation.

## Known source issues (present in the PDF too)

- unresolved \SecRef{tacitly-biological} (no such section in source; renders as 'Section ??' in PDF)
- unresolved \hyperref[tacitly-biological]
- Figure references in §16 use numbering that does not match the report's figures. The §16 text "along the lines suggested by Fig. 1" and the Figure 7 caption "In a naïve scale-up of the scheme outlined in Fig. 1" both refer to the individual-agent learning diagram that this edition numbers Figure 6, not to Figure 1 ("Classes of intelligent systems", §I). This is probably numbering left over from drafts. The author's text is left unchanged. On the same pattern, the §16 sentence "Naïve scaling of the individual-agent model to multiple agents does not fundamentally alter this picture (Fig 2)" appears to refer to Figure 7. (Checked against this edition's text; the rendered PDF was not re-checked for these items.)

## Provenance

Converted with pandoc 3.1.3 plus custom pre/post-processing; verified by sentence-level comparison against the LaTeX source (see `VERIFICATION.md`). Conversion scripts are retained by the editor.
