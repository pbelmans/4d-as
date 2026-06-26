# `data/` — the families of 4-dimensional AS-regular algebras

Each YAML file describes one family of (mostly quadratic, Koszul) Artin–Schelter
regular algebras of global dimension 4 — i.e. a "noncommutative `P^3`".

## Conventions

- **Generators** are written `x_1, x_2, x_3, x_4` (four generators), never
  `x, y, z, w`. In central-extension families `x_4` is the central generator.
- **Relations** are quadratic expressions understood to be equal to `0`.
  Monomials are written in the order they appear, e.g. `x_3 x_1 - h x_1 x_3`
  means `x_3 x_1 - h·x_1 x_3 = 0`.
- The families and their invariants are from **arXiv:2511.08390**
  (Bhatoy–Ingalls–LaRoche–Nookala).

## Schema

```yaml
name: "Sklyanin"            # display name
kind: "named"              # "iterated-Ore" (A–Z) or "named"
generators: ["x_1", "x_2", "x_3", "x_4"]
quadratic: true
num_parameters: 2          # number of scalar parameters
hh0: [1, 2, 9]             # graded HH^*_0 in degrees 1, 2, 3 (arXiv:2511.08390)
hh_qgr: [1, 0, 2, 7]       # directly computed HH^*(qgr A), where known (optional)
point_scheme_dim: 1        # dimension of the point scheme
parameters:                # symbols + constraints
  - symbol: "β, γ"
    description: "..."
introduced:                # where the family was first constructed
  reference: "..."
  note: "..."
construction: >            # the idea behind the construction
  ...
relations:                 # each expression = 0
  - "..."
references:                # further literature
  - "..."
notes: "..."               # geometry: point scheme, centre, ... (optional)
```
