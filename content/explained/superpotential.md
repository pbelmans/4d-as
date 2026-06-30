---
title: "Superpotential"
summary: "the relations as the derivatives of one element"
math: true
---

Every family on this site is [Koszul](/explained/) — quadratic, with the trivial
module \(k\) resolved as economically as possible. For such an algebra the six
defining relations are not independent data: they are all encoded in a single
tensor, the **superpotential**.

## From relations to a potential

Let \(A = T(V)/(R)\) be a quadratic algebra on \(V = A_1\) (here \(\dim V = 4\)),
with relation space \(R \subseteq V \otimes V\) (here \(\dim R = 6\)). When \(A\)
is Artin–Schelter regular of global dimension \(d\) it is *\(m\)-Koszul* and its
Koszul dual \(A^{!}\) is a **Frobenius** algebra concentrated in degrees
\(0, \dots, d\). The one-dimensional top piece \(A^{!}_d\) is a nondegenerate
functional on \(A^{!}_d\)'s predecessors, and dualising it produces a distinguished
element
\[
  w \;\in\; V^{\otimes d},
\]
the **superpotential** of \(A\). For a quadratic algebra of global dimension
\(d = 4\) — a noncommutative \(\mathbb{P}^3\) — the superpotential lives in
\(V^{\otimes 4}\): it is a degree-\(4\) "noncommutative polynomial" in
\(x_1, x_2, x_3, x_4\).

The algebra is recovered from \(w\) by **differentiation**. Writing
\(\partial_\xi\) for contraction of the left-most tensor slot against
\(\xi \in V^{*}\), the relation space is
\[
  R \;=\; \partial^{\,d-2}(w) \;=\; \operatorname{span}\bigl\{\, \partial_\xi \partial_\eta\, w : \xi,\eta \in V^{*} \,\bigr\}
  \quad (d = 4),
\]
so that \(A = T(V)/(\partial^{d-2} w)\) is the *derivation-quotient algebra* of
\(w\). This is the point of view of
[Dubois-Violette](/references/#ref-MR2360146) and
[Bocklandt](/references/#ref-MR2355031): the relations are exactly the
"second partial derivatives" of one quartic potential. The superpotential is
unique up to a nonzero scalar.

The cleanest example is the **commutative** polynomial ring
\(k[x_1,x_2,x_3,x_4]\), whose superpotential is the fully antisymmetric tensor
\[
  w \;=\; \sum_{\sigma \in S_4} \operatorname{sgn}(\sigma)\,
  x_{\sigma(1)} x_{\sigma(2)} x_{\sigma(3)} x_{\sigma(4)},
\]
the noncommutative determinant; its derivatives are the commutators
\(x_i x_j - x_j x_i\).

## Twisted superpotentials

In general \(w\) is not invariant under cyclically rotating its four tensor
slots; it is only invariant up to a twist by a graded automorphism
\(\nu\) of \(A\):
\[
  w \;=\; (\nu \otimes \mathrm{id} \otimes \mathrm{id} \otimes \mathrm{id})\,(\tau\, w),
\]
where \(\tau\) is the cyclic permutation of the slots. This \(\nu\) is precisely
the [Nakayama automorphism](/explained/nakayama-automorphism/), and \(w\) is an
honest (untwisted, cyclically invariant) superpotential exactly when \(\nu\) is
trivial — that is, exactly when \(A\) is **Calabi–Yau**.

Because the superpotential is only defined up to scalar and its coefficients are
just a repackaging of the relations, it is not itself a useful "invariant" of a
family — it carries the parameters in the obvious way. The invariant worth
recording is its twist, the Nakayama automorphism.

## Computation

The superpotential and its twist are computed with the
[`AssociativeAlgebras`](https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/AssociativeAlgebras/html/_superpotential.html)
package in Macaulay2 (`superpotential` and
[`nakayamaAut`](https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/AssociativeAlgebras/html/_nakayama__Aut.html)),
which work through the Frobenius structure on the Koszul dual; see
[the Nakayama automorphism](/explained/nakayama-automorphism/) for the results
and reproduction details.

{{< overview-links >}}
