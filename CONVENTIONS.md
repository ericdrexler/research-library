# Conventions: structure and updates

This file describes how the library is organized and how it should be changed. It is written for people browsing the repository and for models or tools that read or update it. Instructions here apply to any model or tool making changes. They are expected to evolve; when this file and practice disagree, follow this file and note the discrepancy.

## Structure

The top level is organized by **kind of material**, not by topic. Topics overlap; kinds do not. Relationships between items are recorded in their metadata and in [`INDEX.md`](INDEX.md).

| Folder | Holds |
|---|---|
| `works/` | Eric Drexler's published works, including Markdown versions and revised or extended versions |
| `research/` | New original material |
| `commentary/` | Reviews, summaries and cross-work notes, by anyone |
| `third-party/` | Others' material; not covered by the library's CC0 dedication |

A top-level folder is created only when its first item is added.

**Items.** Each item is one folder inside a kind folder, named `YYYY-short-name`: the year of the item's original date, then a short descriptive name in lowercase with hyphens (for example `works/2019-reframing-superintelligence/`). File names follow the same style, with full dates where useful (`2017-03-02-…`).

## Item metadata

Every item folder has a `README.md` that begins with this block:

```yaml
---
title: "…"
authors: "…"        # who wrote it; for model-written text, the model family and developer
date: YYYY-MM       # original date; add drafting or circulation dates in words if they matter
kind: …             # work | research | commentary | third-party, with a short qualifier
status: …           # see below
rights: …           # "CC0 1.0" or the exception that applies
related: [ … ]      # relative paths to related items
---
```

The README then describes the item, lists its files with what each is for, and states anything a reader needs before relying on it.

**Status** uses these terms, with a short qualifier where useful: `draft`, `provisional`, `complete`, `published`, `superseded` (with the path of what supersedes it).

**Authorship.** State who wrote what. *Maintained by* does not mean *written by*. Model-written material names the model family and developer, and says what role any human played. Never imply that an author endorses commentary on their work.

## Changes

1. **Adding an item.** Create its folder and README with the metadata block, add a row to `INDEX.md`, and add the item to the `related` lists of the items it concerns. Do this in one commit.
2. **Changing published text.** Do not overwrite the text of a published work. Add a revised version in the same item folder, with a dated or versioned file name, and say in the README which version is current and what changed.
3. **Changing commentary or research.** Edit in place if the item is `draft` or `provisional`. If it is `complete`, make substantive changes as a new dated version, and record corrections in a "Changes" section of its README.
4. **Status.** When status changes, update the README and `INDEX.md` together.
5. **Moving or renaming.** Avoid moving items once the library is public. If a move is necessary, leave a `README.md` at the old path that points to the new one, and update every relative link and `INDEX.md`.
6. **Rights.** Material is CC0 1.0 unless stated otherwise. Anything else needs a `rights` value in its metadata and a row in the exceptions list in `INDEX.md`. Others' whole works go in `third-party/`; short quotations within an item stay where they are and keep their own rights.
7. **Duplicates.** Where files duplicate one another (a concatenation of section files, a PDF and its Markdown edition), the item's README says which to use for what.
8. **Checks.** Use relative links within the library. Before committing, check that every link resolves and that every metadata block parses as YAML. Quote a whole value if it contains quotation marks or a colon followed by a space.

## Citation

Paths may change as the library evolves. For a stable citation, cite a tagged release (for example `…/tree/2026-10/…`), which fixes the files as they were.
