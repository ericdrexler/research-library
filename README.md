# research-library

A machine-oriented knowledge and research corpus maintained by Eric Drexler.

The repository contains original research, Markdown versions of previously published work, revised and extended material, commentary, summaries, metadata, cross-references, and other derived research material. It is intended primarily for retrieval, interpretation, synthesis, and reuse by language models, agentic workflows, and related tools.

The repository is optimized for machine use. Human-facing publication may use other representations or venues.

Authorship is stated in each item's metadata; *maintained by* does not mean *written by*. Some items were written by AI models, and their metadata says so.

## Use

Start with [`INDEX.md`](INDEX.md), which lists every item with its authors, date and status. [`CONVENTIONS.md`](CONVENTIONS.md) describes the structure and the rules for changes, and serves as instructions for models and tools that update the library.

Repository structure provides coarse organization: the top level is organized by kind of material (`works/`, `research/`, `commentary/`, `third-party/`), and each item is a folder with its own `README.md`. Guide files, metadata, and cross-references provide richer information about relationships among documents, concepts, versions, and derived material.

These conventions are expected to evolve. Models and tools should treat guide and metadata files as part of the corpus rather than as ancillary documentation.

## Status

Material may be provisional, revised, superseded, reorganized, or extended over time. Files may move as repository structure evolves.

Where document status, provenance, or version identity matters, it should be stated in the document or associated metadata. Git history records repository revisions; for a stable citation, cite a tagged release. Stronger archival and versioning mechanisms may be added where useful.

## Rights and reuse

Unless explicitly stated otherwise, material in this repository is dedicated to the public domain under the **Creative Commons CC0 1.0 Universal Public Domain Dedication**.

It may be copied, modified, redistributed, analyzed, mined, incorporated into other works, and used for machine learning or model training, commercially or non-commercially, without permission or attribution.

Attribution is appreciated where customary, but is not required.

### Third-party material

CC0 applies only to material for which the repository author has the authority to make this dedication.

Quotations, cited or linked material, and other third-party content remain subject to any rights that apply to them. Material in this repository that is not covered by CC0 will be explicitly identified as an exception, either locally or in associated metadata. Others' whole works are kept in `third-party/`, and every exception is listed in [`INDEX.md`](INDEX.md).

The full CC0 1.0 legal text is provided in `LICENSE`.
