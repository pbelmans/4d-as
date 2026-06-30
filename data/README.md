# `data/` — the families of 4-dimensional AS-regular algebras

Each YAML file describes one family of quadratic (Koszul) Artin–Schelter
regular algebras of global dimension 4 — i.e. a "noncommutative `P^3`".

## Conventions

- **Generators** are written `x_1, x_2, x_3, x_4` (four generators), never
  `x, y, z, w`. In central-extension families `x_4` is the central generator.
- **Relations** are quadratic expressions understood to be equal to `0`.
  Monomials are written in the order they appear, e.g. `x_3 x_1 - h x_1 x_3`
  means `x_3 x_1 - h·x_1 x_3 = 0`.
- The families and their invariants are from **arXiv:2511.08390**.

## Schema

```yaml
name: "Sklyanin"            # display name
kind: "named"              # "double-Ore" (A–Z) or "named"
generators: ["x_1", "x_2", "x_3", "x_4"]
quadratic: true
num_parameters: 2          # number of scalar parameters
hh0: [1, 2, 9]             # graded HH^*_0 in degrees 1, 2, 3 (arXiv:2511.08390)
hh_qgr: [1, 0, 2, 7]       # directly computed HH^*(qgr A) in degrees 0–3 (optional)
point_scheme_dim: 1        # dimension of the point scheme
point_scheme: "..."        # succinct description of the point scheme
year: 1982                 # year of first definition (the introducing work)
slug: "sklyanin"           # URL slug under /families/ (ore-a, ore-b, … for A–Z)
sortkey: "1982 sklyanin"   # "<year> <slug>"; drives the default table order
ks_rank: 2                 # rank of the Kodaira–Spencer map
ks_inj: true               # is it injective?
ks_surj: true              # is it surjective?
centre_z2: 2               # dim Z(A)_2 (central quadrics)
centre_z3: 0               # dim Z(A)_3 (central cubics)
normal_1: -1               # proj. dim of the normal locus in degree 1 (-1 = none)
normal_2: 1                # proj. dim of the normal locus in degree 2
calabi_yau: true           # is A Calabi-Yau? (Nakayama automorphism nu = id)
nakayama: "\\mathrm{id}"   # the Nakayama automorphism nu on A_1, as LaTeX
nakayama_type: "identity"  # identity | scalar | diagonal | monomial | unipotent | general
nakayama_constant: true    # is nu constant over the parameter space? (omit if no params)
homological_det: 1         # det nu (the homological determinant): 1, -1, or "i"
nakayama_field: "qq"       # provenance: qq | gf-params | gf | gf-sample
parameters:                # symbols + constraints
  - symbol: "β, γ"
    description: "..."
introduced:                # where the family was first constructed
  reference: "..."         # citation key (MRxxxxxxx or arXiv id)
  note: "..."
construction: >            # the idea behind the construction
  ...
relations:                 # each expression = 0
  - "..."
code_derive:               # parameters fixed by a constraint, in code form (optional)
  - "alpha = -(beta + gamma)/(1 + beta*gamma)"
references:                # further literature (citation keys)
  - "..."
notes: "..."               # other remarks, e.g. a parameter constraint (optional)
```

Computed invariants (`hh0`, `hh_qgr`, `point_scheme_dim`, `centre_z*`,
`normal_*`, the `ks_*` fields) come from arXiv:2511.08390 and from the
reproduction scripts in `code/`. The Nakayama fields (`calabi_yau`, `nakayama`,
`nakayama_type`, `nakayama_constant`, `homological_det`, `nakayama_field`) come
from `code/nakayama.m2`, and the point schemes of the seven families they were
missing for from `code/point_scheme_extra.m2`. Fields that are absent (e.g. an
un-computed `point_scheme_dim`) render as `?`.
