---
title: "The Kodaira–Spencer map"
summary: "how a family of algebras meets a component of the moduli stack"
math: true
---

Hochschild cohomology controls deformations of an algebra: for an
Artin–Schelter regular algebra \(A\) the degree-zero part \(\mathrm{HH}^2_0(A)\)
is the space of first-order graded deformations, and is identified with the
Zariski tangent space of the moduli stack \(\mathcal{A}_4\) of four-dimensional
Koszul AS-regular algebras at the point \([A]\).

Given a flat family of such algebras over a base scheme \(S\), with fibre
\(A_p\) at a point \(p\), the **Kodaira–Spencer map** sends a tangent vector
\(v \in T_p S\) to the class in \(\mathrm{HH}^2_0(A_p)\) of the first-order
deformation that \(v\) induces. It measures how moving in the base deforms the
fibre.

Following {{< arxiv "2511.08390" >}}, this gives a
criterion for recognising components of the moduli stack:

- if the Kodaira–Spencer map at \(p\) is **surjective**, the closure of the
  image of \(S \to \mathcal{A}_4\) is an irreducible **component** of the moduli
  stack;
- if it is a **bijection**, the map to the moduli stack is generically finite.

Computing \(\mathrm{HH}^2_0\) and this map for each known family is how the paper
identifies which families sweep out components of \(\mathcal{A}_4\). The columns
\(\mathrm{HH}^i_0\) in the [table](/) are exactly these Hochschild dimensions.
