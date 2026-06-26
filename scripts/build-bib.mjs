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
  const html = new Cite(entry).format('bibliography', {
    format: 'html',
    template: 'apa',
    lang: 'en-US',
  })
  // sort key: first author's family name (fallback: title), lowercased
  const first = entry.author && entry.author[0]
  const author = ((first && (first.family || first.literal)) || entry.title || '')
    .toLowerCase()
  refs[entry.id] = { key: entry.id, html: html.trim(), DOI: entry.DOI || null, author }
}

writeFileSync('data/refs.json', JSON.stringify(refs, null, 2) + '\n')
console.log(`wrote data/refs.json with ${Object.keys(refs).length} entries`)
