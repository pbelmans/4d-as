---
title: "Explained"
math: true
notitle: true
---

## Artin–Schelter regular algebras

Let \(k\) be a field and let
\(A = \bigoplus_{i \geq 0} A_i\) be a connected graded \(k\)-algebra,
that is, \(A_0 = k\) and \(A\) is finitely generated in degree \(1\).
Write \(k = A/A_{\geq 1}\) for the trivial module.

The algebra \(A\) is **Artin–Schelter regular** (or *AS-regular*) of
dimension \(d\) if:

1. \(A\) has finite global dimension \(d\);
2. \(A\) has finite Gelfand–Kirillov dimension, i.e. polynomial growth;
3. \(A\) is **Gorenstein**: there is an integer \(\ell\) such that
   \[
   \operatorname{Ext}^i_A(k, A) \cong
   \begin{cases} k(\ell) & i = d, \\ 0 & i \neq d. \end{cases}
   \]

## Classification

In low dimensions the AS-regular algebras are completely understood.

- **\(d = 1\).** The only AS-regular algebra is the polynomial ring \(k[x]\).
- **\(d = 2\).** There are exactly two quadratic families on two generators:
  the *quantum plane* \(k\langle x, y\rangle/(yx - q\,xy)\) for \(q \in k^\times\),
  and the *Jordan plane* \(k\langle x, y\rangle/(yx - xy - x^2)\).
- **\(d = 3\).** The classification was begun by Artin–Schelter and completed,
  using the geometry of point schemes, by
  [Artin–Tate–Van den Bergh](/references/#ref-MR1086882). The generic algebras
  are governed by a triple \((E, \mathcal{L}, \sigma)\) of an elliptic curve
  with a line bundle and an automorphism; the quadratic case has three
  generators, the cubic case two.

In dimension \(d = 4\) no full classification is known. Describing the known
families is the subject of this website.
