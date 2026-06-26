---
title: "Normal elements"
summary: "normal elements in low degrees"
math: true
---

A homogeneous element \(n\) of a graded algebra \(A\) is **normal** if
\(nA = An\) — the two-sided analogue of a central element (every central element
is normal). Normal elements of degree \(1\) cut out hyperplanes that are again
"coordinate" subalgebras, and degree-\(2\) normal elements include the central
quadrics; they control much of the ring-theoretic geometry.

Normality is a determinantal condition, so the normal elements of a fixed degree
\(d\) form a Zariski-closed **cone** in \(A_d\). They do **not** in general form a
linear subspace: a sum of two normal elements need not be normal, and our
computation (the rank of a parameter-dependent map) determines only the
*dimension* of this locus — it does not establish linearity. The table gives the
**projective dimension** of the normal locus in \(\mathbb{P}(A_d)\) at the
generic point, for \(d = 1, 2\):

- \(-1\): no normal element in that degree;
- \(0\): a finite set of normal directions;
- \(1, 3, \dots\): a positive-dimensional family of normal elements.

When the normal locus happens to coincide with the (linear) space of central
elements it *is* a linear subspace — for [Sklyanin](/families/sklyanin/) the
degree-2 locus is the central pencil \(\langle \Omega_1, \Omega_2 \rangle\), and
for [Clifford](/families/clifford/) it is the \(\mathbb{P}^3\) of central squares
— but this is special to those families.

{{< family-table "normal" >}}

Computed at generic parameters over \(\mathrm{GF}(p)\) (\(p \equiv 1 \bmod 12\)),
confirmed at two primes. The validation \(\dim_{\mathbb{P}}(\text{normal}_2) \ge
\dim \operatorname{Z}(A)_2 - 1\) (central ⊆ normal) holds throughout.
[Generalized Clifford 3](/families/generalized-clifford-3/) is omitted: it is regular
only on its constraint variety, where a generic parameter point does not land.
