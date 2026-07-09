# PHY653 · Computational EM & Plasma Physics

**A knowledge wiki for PHY653: Computational Electromagnetics and Plasma Physics** —
Thammasat University graduate course. From `import numpy` to a working
particle-in-cell plasma simulation, in five chapters — rebuilt here as a cross-linked
knowledge system.

## The course in one paragraph

Plasma physics is the study of a self-consistent feedback loop: charged particles move
according to the [Lorentz force](equations/lorentz-force.md), and their motion creates
the very fields that push them (Maxwell's equations). This course builds the
computational machinery for both halves — first
[time integrators](concepts/ode-integration.md) for particle motion (from
[forward Euler](concepts/forward-euler.md) to the symplectic
[leapfrog](concepts/leapfrog-method.md)), then the
[drift theory](concepts/guiding-center-drifts.md) they let us verify, then
[finite-difference field solvers](concepts/finite-difference-method.md)
([Poisson](concepts/poisson-solvers.md) and [FDTD](concepts/fdtd-method.md)), and
finally the synthesis: [N-body](concepts/n-body-simulation.md) and
[particle-in-cell](concepts/pic-method.md) simulation of the
[two-stream instability](concepts/two-stream-instability.md).

## Learning path

| Chapter | Topics |
|---|---|
| **1 · Foundations** | [Why simulate plasmas?](concepts/simulation-driven-plasma-physics.md) · [Lorentz force](equations/lorentz-force.md) · [Rutherford scattering](examples/rutherford-scattering.md) |
| **2 · Time integration** | [ODE framework](concepts/ode-integration.md) → [Forward Euler](concepts/forward-euler.md) → [Backward Euler](concepts/backward-euler.md) → [Leapfrog](concepts/leapfrog-method.md) → [Runge–Kutta](concepts/runge-kutta-methods.md) → [Convergence](concepts/convergence-and-error.md) |
| **3 · Single-particle motion** | [Guiding center & drifts](concepts/guiding-center-drifts.md) → [E×B](equations/exb-drift.md) · [∇B & curvature](equations/grad-b-curvature-drift.md) → [Magnetic mirror](concepts/magnetic-mirror.md) → [Fermi acceleration](concepts/fermi-acceleration.md) |
| **4 · Field solvers** | [Finite differences](concepts/finite-difference-method.md) → [Poisson solvers](concepts/poisson-solvers.md) → [FDTD](concepts/fdtd-method.md) → [Double slit](examples/double-slit-fdtd.md) |
| **5 · Many-particle systems** | [N-body](concepts/n-body-simulation.md) → [PIC method](concepts/pic-method.md) → [Two-stream instability](concepts/two-stream-instability.md) |

## Jump in

- **[Concept graph](concept-graph.md)** — dependency map of the course
- **[Glossary](glossary.md)** — every technical term
- **[Worked examples](examples/index.md)** — benchmark problems, fully solved
- **[Quizzes](quizzes.md)** — three difficulty levels
- **[Simulations](simulations/index.md)** — including a live integrator-comparison widget

!!! tip "Companion courses"
    The physics behind these algorithms lives in the
    [PC368 plasma wiki](../plasma/index.md) (drifts, waves, instabilities from theory)
    and the numerical fluid connection in the [PC316 fluids wiki](../fluids/index.md).
