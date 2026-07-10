# Physics Class Wiki

Lecture notes, re-engineered. Seven physics courses taught at **Thammasat University**
by Pakorn Wongwaitayakornkul, rebuilt as cross-linked knowledge systems: every concept
explained from intuition to derivation, every equation dissected, every page quizzed —
built for studying, not just reading.

<div class="cw-cards" markdown>
<div class="cw-card" markdown>
<span class="cw-code">SC133 · Year 1</span>
### [Physics for Engineers I](physics1/index.md)
Mechanics from vectors to gravitation, fluids, oscillations, waves and
thermodynamics — fully rebuilt.
<span class="cw-meta">36 concepts · 30 lectures · 4 live demos</span>
</div>
<div class="cw-card" markdown>
<span class="cw-code">SC134 · Year 1</span>
### [Physics for Engineers II](sc134/index.md)
Electromagnetism from charge to light: fields, circuits, induction, Maxwell's
equations.
<span class="cw-meta">25 concepts · live field explorer & circuit lab</span>
</div>
<div class="cw-card" markdown>
<span class="cw-code">PC316 · Year 3</span>
### [Fluid Mechanics](fluids/index.md)
Continuum to turbulence: statics, kinematics, Navier–Stokes, dimensional analysis,
shocks and instabilities.
<span class="cw-meta">23 concepts · 9 equations · live potential-flow lab</span>
</div>
<div class="cw-card" markdown>
<span class="cw-code">PC368 · Year 3</span>
### [Introduction to Plasma Physics](plasma/index.md)
Debye shielding, single-particle drifts, MHD, waves, Landau damping and
reconnection.
<span class="cw-meta">≈ 26 concepts · 17 lectures · quizzes & widgets</span>
</div>
<div class="cw-card" markdown>
<span class="cw-code">PHY621 · Graduate</span>
### [Mathematical Methods I](phy621/index.md)
Linear algebra, Fourier & Laplace transforms, ODEs, PDEs and Green's functions.
<span class="cw-meta">19 concepts · live Fourier builder</span>
</div>
<div class="cw-card" markdown>
<span class="cw-code">PHY622 · Graduate</span>
### [Mathematical Methods II](phy622/index.md)
Calculus of variations, complex analysis, and group theory — with SU(2) → SO(3).
<span class="cw-meta">18 concepts · live conformal explorer</span>
</div>
<div class="cw-card" markdown>
<span class="cw-code">PHY653 · Graduate</span>
### [Computational EM & Plasma](comp-plasma/index.md)
From `import numpy` to particle-in-cell: integrators, drift orbits, field solvers,
N-body and the two-stream instability.
<span class="cw-meta">16 concepts · 8 equations · live integrator arena</span>
</div>
</div>

Every course has a **Lecture Timeline** page — the wiki in teaching order, lecture by
lecture — first entry in its sidebar (e.g. [SC133's 30 lectures](physics1/lectures.md),
[PC368's 17](plasma/lectures.md)).

## How this wiki works

- **Concepts** teach — intuition first, then formalism, derivation, worked example,
  common mistakes, and a quiz.
- **Equations** are reference cards — variables, assumptions, derivation, limitations.
- **Concept graphs** map prerequisites, per course and
  [across the whole curriculum](graph.md).
- **Search** (press ++s++ or ++slash++) reaches every page, term, and equation.

## Cross-course threads

Some ideas refuse to stay in one course — follow them across the curriculum:

| Thread | Trail |
|---|---|
| **Fluids, twice** | [Bernoulli for engineers](physics1/concepts/bernoulli.md) → [the real derivation](fluids/concepts/bernoulli-principle.md) → [MHD as a conducting fluid](plasma/concepts/mhd.md) |
| **Instability, three ways** | [Kelvin–Helmholtz](fluids/concepts/kelvin-helmholtz-instability.md) → [MHD instabilities](plasma/concepts/mhd-instability.md) → [two-stream, simulated](comp-plasma/concepts/two-stream-instability.md) |
| **Drift motion** | [theory in PC368](plasma/concepts/drift-motion.md) → [computed in PHY653](comp-plasma/concepts/guiding-center-drifts.md) |
| **Waves everywhere** | [waves on a string](physics1/concepts/waves.md) → [surface waves](fluids/equations/interface-dispersion-relation.md) → [plasma waves](plasma/concepts/plasma-waves.md) → [FDTD wave simulation](comp-plasma/concepts/fdtd-method.md) |
| **Conservation laws** | [energy & momentum](physics1/concepts/conservation-of-energy.md) → [Reynolds transport theorem](fluids/concepts/reynolds-transport-theorem.md) → [shock jump conditions](fluids/equations/rankine-hugoniot-conditions.md) |
| **Fields → field theory** | [E&M in SC134](sc134/concepts/maxwell-equations.md) → [vector calculus made rigorous](phy621/concepts/gradient-divergence-curl.md) → [Maxwell solved numerically](comp-plasma/concepts/fdtd-method.md) |
| **Complex analysis at work** | [contours & residues](phy622/concepts/residue-theorem.md) → [conformal maps](phy622/concepts/conformal-mapping.md) → [airfoils](fluids/concepts/conformal-mapping-and-images.md) & [Landau damping](plasma/concepts/landau-damping.md) |
| **Eigenmodes everywhere** | [eigenvalues](phy621/concepts/eigenvalues-eigenvectors.md) → [normal-mode stability](fluids/concepts/hydrodynamic-stability.md) → [plasma dispersion relations](plasma/concepts/plasma-waves.md) |

---

*Maintained alongside the courses each academic year. Found an error? Tell your
lecturer — it improves the wiki for everyone.*
