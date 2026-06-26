// Render data/references.bib into data/refs.json at build time using citation.js.
// Hugo then reads site.Data.refs to display formatted citations. Keeping this a
// build step (rather than shipping citation.js to the browser) keeps the site
// fully static.
import { Cite } from '@citation-js/core'
import '@citation-js/plugin-bibtex'
import '@citation-js/plugin-csl'
import { readFileSync, writeFileSync } from 'node:fs'

const bib = readFileSync('data/references.bib', 'utf8')
const cite = new Cite(bib)

const refs = {}
for (const entry of cite.data) {
  // Format without URL/DOI so no plaintext link (e.g. numdam, doi) ends up in
  // the citation; we render our own MR/arXiv/DOI links separately.
  const bare = { ...entry }
  delete bare.URL
  delete bare.DOI
  const html = new Cite(bare).format('bibliography', {
    format: 'html',
    template: 'apa',
    lang: 'en-US',
  })
  // sort key: first author's family name (fallback: title), lowercased
  const first = entry.author && entry.author[0]
  const author = ((first && (first.family || first.literal)) || entry.title || '')
    .toLowerCase()
  // citation.js leaves a few TeX bits in titles (e.g. $\mathbb{P}^3$); tidy them.
  const tidy = html
    .replace(/\$?\\(?:mathbb|mathbf|bold|bf)\s*\{?P\}?(?:\^?\{?3\}?|<sup>3<\/sup>)\$?/g, "ℙ³")
    .replace(/\$([^$]*)\$/g, "$1")
    .trim()
  refs[entry.id] = { key: entry.id, html: tidy, DOI: entry.DOI || null, author }
}

writeFileSync('data/refs.json', JSON.stringify(refs, null, 2) + '\n')
console.log(`wrote data/refs.json with ${Object.keys(refs).length} entries`)
