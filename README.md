# 4-dimensional Artin–Schelter regular algebras

This is the repository for a website dedicated to the classification and
properties of four-dimensional Artin–Schelter regular algebras.

The focus is mostly on the **quadratic** (Koszul) case: algebras presented by
four generators \(x_1, x_2, x_3, x_4\) and quadratic relations, i.e.
noncommutative analogues of \(\mathbb{P}^3\). The families and their invariants
follow [arXiv:2511.08390](https://arxiv.org/abs/2511.08390).

## Structure

- `data/families/*.yaml` — one file per family: generators, relations, the idea
  behind the construction, where it was introduced, and computed invariants
  (Hochschild cohomology, point-scheme dimension). See `data/README.md`.
- `data/references.bib` — the bibliography. Citation keys are MathSciNet MR
  numbers, or the arXiv identifier when not on MathSciNet.
- `content/`, `layouts/` — the Hugo site.

## Building

The bibliography is rendered to `data/refs.json` at build time with
[citation.js](https://citation.js.org) (a Node step), then Hugo builds the
static site:

```sh
npm install
npm run build      # = npm run bib && hugo --gc --minify
```

For local development, run `npm run bib` once, then `hugo server`.
