---
title: "Nakayama automorphism"
summary: "the twist of the superpotential, and when the algebra is Calabi–Yau"
math: true
---

A noncommutative \(\mathbb{P}^3\) is in particular *skew Calabi–Yau*: there is a
graded algebra automorphism \(\nu\) of \(A\), the **Nakayama automorphism**, and
an integer \(\ell\) with a bimodule isomorphism
\[
  \operatorname{Ext}^{d}_{A^{e}}(A, A^{e}) \;\cong\; {}^{1}\!A^{\nu}(\ell),
  \qquad d = \operatorname{gldim} A = 4,
\]
where \({}^{1}\!A^{\nu}\) is \(A\) as a bimodule with the right action twisted by
\(\nu\). Equivalently, \(\nu\) is the twist that makes the
[superpotential](/explained/superpotential/) cyclically invariant. The
automorphism is the obstruction to \(A\) being **Calabi–Yau**:
\[
  A \text{ is Calabi–Yau} \quad\Longleftrightarrow\quad \nu = \mathrm{id}.
\]
It was put on a systematic footing — together with the homological identities it
satisfies — by [Reyes–Rogalski–Zhang](/references/#ref-MR3250287).

Since \(A\) is connected graded and generated in degree \(1\), the Nakayama
automorphism is graded, so it is determined by its action on
\(A_1 = \langle x_1, x_2, x_3, x_4\rangle\): a single invertible \(4 \times 4\)
matrix \(N\), with \(\nu(x_j) = \sum_i N_{ij}\,x_i\). Its determinant
\(\det \nu\) — the **homological determinant** of the Nakayama automorphism — is
a finer numerical invariant.

## What happens across the catalogue

Computing \(\nu\) for every family (see [below](#how-it-was-computed)) turns up a
clean picture.

- **\(\nu\) is almost always a monomial matrix** — a diagonal matrix or a signed
  permutation — the only exception being [Jordan](/families/jordan/), whose
  Nakayama automorphism is **unipotent**.
- **Calabi–Yau families.** \(\nu = \mathrm{id}\) holds, for *all* parameter values,
  for the [commutative](/families/commutative/) ring, the
  [Sklyanin](/families/sklyanin/) algebra and its
  [twist](/families/sklyanin-twist/), [Caines](/families/caines/),
  [generalized Clifford 1](/families/generalized-clifford-1/),
  [Shelton–Tingey](/families/shelton-tingey/), the
  [Ore extension of the commutative ring](/families/ore-extension-of-commutative/),
  and the [central extension of Sklyanin](/families/central-extension/).
- **Is it constant over the parameter space?** For the parametrised families the
  answer splits almost evenly. About a quarter have a Nakayama automorphism that
  does *not* move with the parameters — the Calabi–Yau ones above, and a second
  group with \(\nu = -\mathrm{id}\) (the three
  [Goetz–Kirkman–Moore–Vashaw](/families/goetz-kirkman-moore-vashaw-r/) algebras,
  the [\(\mathrm{S}_\infty\)](/families/s-infinity/) pair,
  [generalized Clifford 2](/families/generalized-clifford-2/),
  [Clifford](/families/clifford/), the
  [central-extension twist](/families/central-extension-twist/)). For the rest —
  the double-Ore families, [Vancliff](/families/vancliff/), the
  [deformed skew](/families/deformed-skew-1/) and [skew](/families/skew/) families
  — \(\nu\) genuinely depends on the parameters.
- **But the determinant never does.** Even where \(\nu\) moves, it moves only by a
  *torus scaling* whose contribution cancels in the determinant: \(\det\nu\) is
  **constant over the parameter space of every family**, always landing in
  \(\{1, -1, i\}\) (it is \(-1\) for a handful of double-Ore families and
  [generalized Clifford 3](/families/generalized-clifford-3/), and \(i\) for the
  [\(\mathrm{A}_5\)](/families/a5/) family).

So the Nakayama automorphism is a genuinely *moving* invariant on these moduli,
while its determinant is rigid. The determinant appears as its own column in the
[main table](/families/); the full automorphism is recorded on each family's page.

## Every family

The type of \(\nu\), whether the algebra is Calabi–Yau, whether \(\nu\) is
constant across the parameters, and \(\det\nu\):

{{< family-table "nakayama" >}}

## How it was computed

The Nakayama automorphism is computed from the
[superpotential](/explained/superpotential/) with the
[`AssociativeAlgebras`](https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/AssociativeAlgebras/html/_nakayama__Aut.html)
package in Macaulay2 (`superpotential`, then `nakayamaAut`), extracting the
\(4 \times 4\) matrix \(N\) on \(A_1\). The base field is chosen per family, and
the **constancy** verdict is in every case cross-checked by computing \(\nu\) at
two independent generic parameter points over \(\mathrm{GF}(60013)\) and comparing
the matrices (a Nakayama automorphism that depended on the parameters would differ
at two random points).

- **Exactly over \(\mathbb{Q}(\text{params})\)** for the families whose structure
  constants are rational — the closed forms on their pages (e.g.
  \(\operatorname{diag}(h^{-2}, h^{-2}, h^{2}, h^{2})\) for
  [double Ore A](/families/ore-a/)) are genuine identities of rational functions,
  so "constant?" is read off directly.
- **Exactly over \(\mathbb{F}_{60013}(\text{params})\)** for the families whose
  *definition* uses a root of unity (\(i\) or a primitive cube root \(\omega\)) —
  the prime \(60013 \equiv 1 \bmod 12\) supplies both. (A genuine
  characteristic-zero computation would need \(\mathbb{Q}(i)\) or
  \(\mathbb{Q}(\omega)\), but the package requires its coefficient ring to be one
  of \(\mathbb{Z}/n\), \(\mathbb{Z}\), \(\mathbb{Q}\) or \(\mathrm{GF}\); the
  resulting matrix is field-independent, so this is the generic value.)
- **At a generic point of \(\mathbb{F}_{60013}\)** for the three families where a
  function-field Gröbner basis does not terminate — the
  [central extension](/families/central-extension/) (\(12\) parameters),
  [Clifford](/families/clifford/) (\(24\)), and the
  [Ore extension of the commutative ring](/families/ore-extension-of-commutative/)
  — with constancy confirmed by sampling two independent points (the same method
  the rest of the site uses for many-parameter families).

Parameter-free families are computed over their field of definition
(\(\mathbb{Q}\), or \(\mathbb{F}_{60013}\) when a root of unity appears). The
reproduction script is `code/nakayama.m2`.

{{< overview-links >}}
