---
title: "Explained"
math: true
notitle: true
---

## Artin–Schelter regular algebras

Let \(k\) be a field and let
\(A = \bigoplus_{i \geq 0} A_i\) be a connected graded \(k\)-algebra,
that is, \(A_0 = k\), and assume \(A\) is finitely generated.
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

These conditions were introduced by
[Artin–Schelter](/references/#ref-MR917738).

The algebra is **quadratic** if it is generated in degree \(1\) with all
defining relations in degree \(2\). Every family on this site is quadratic — in
fact *Koszul*, a stronger homological condition — so each is presented by four
generators and six quadratic relations.

The basic example is the **commutative polynomial ring**
\(k[x_1, \dots, x_d]\): it is AS-regular of dimension \(d\), and the
noncommutative AS-regular algebras are exactly the noncommutative analogues of
affine and projective space that this site is about. For \(d = 4\) the
quadratic ones are the noncommutative \(\mathbb{P}^3\)'s.

## Classification

In low dimensions the AS-regular algebras are completely understood.

- **\(d = 1\).** The only AS-regular algebra is the polynomial ring \(k[x]\).
- **\(d = 2\).** There are exactly two quadratic families on two generators:
  the *quantum plane* \(k\langle x, y\rangle/(yx - q\,xy)\) for \(q \in k^\times\),
  and the *Jordan plane* \(k\langle x, y\rangle/(yx - xy - x^2)\).
- **\(d = 3\).** The classification was begun by
  [Artin–Schelter](/references/#ref-MR917738) and completed, using the geometry
  of point schemes, by
  [Artin–Tate–Van den Bergh](/references/#ref-MR1086882). The generic algebras
  are governed by a triple \((E, \mathcal{L}, \sigma)\) of an elliptic curve
  with a line bundle and an automorphism; the quadratic case has three
  generators, the cubic case two.

In dimension \(d = 4\) no full classification is known. Restricting to algebras
**generated in degree \(1\)**, the minimal free resolution of the trivial module
\(k\) takes one of three shapes, labelled by the ranks of its terms:

- **\((1,4,6,4,1)\)** — \(4\) generators and \(6\) relations of degree \(2\), with
  Hilbert series \(\operatorname{h}_A(t) = \dfrac{1}{(1-t)^4}\). These are exactly
  the **quadratic** algebras (automatically Koszul): the noncommutative
  \(\mathbb{P}^3\)'s, and the families catalogued on this site.
- **\((1,3,4,3,1)\)** — \(3\) generators and \(4\) relations, two of degree \(2\)
  and two of degree \(3\), with
  \(\operatorname{h}_A(t) = \dfrac{1}{(1-t)^3(1-t^2)}\).
- **\((1,2,2,2,1)\)** — \(2\) generators and \(2\) relations, one of degree \(3\)
  and one of degree \(4\), with
  \(\operatorname{h}_A(t) = \dfrac{1}{(1-t)^2(1-t^2)(1-t^3)}\).

The two non-quadratic types are far less understood. The \((1,2,2,2,1)\) algebras
were largely classified by
[Lu–Palmieri–Wu–Zhang](/references/#ref-MR2309153) through the \(A_\infty\)-structure
on their Ext-algebra (with the underlying machinery developed in a
[companion paper](/references/#ref-MR2430869)). Unlike the quadratic case, these
two types carry no classical geometric interpretation — there is no point scheme
that parametrises their point modules — as discussed in
[Belmans, *On non-quadratic 4-dimensional Artin–Schelter regular algebras and 3-folds*](https://pbelmans.ncag.info/assets/non-quad-4-dim-as-regular.pdf).

Describing the known families of the quadratic type \((1,4,6,4,1)\) is the
subject of this website.
