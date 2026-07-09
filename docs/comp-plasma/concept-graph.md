# Concept Graph · Computational EM & Plasma

Arrows mean *"understand this first"*. Machine-readable version:
[`graph/comp-plasma_graph.json`](https://github.com/tpakorn/class-wiki/blob/main/graph/comp-plasma_graph.json).

```mermaid
flowchart TD
    WHY["Why simulate plasmas?"] --> LORENTZ["Lorentz force"]
    WHY --> ODE["ODE integration framework"]
    LORENTZ --> CYC["Cyclotron motion (benchmark)"]

    ODE --> FE["Forward Euler"]
    FE --> BE["Backward Euler"]
    FE --> RK["Runge–Kutta (RK3/RK4)"]
    BE --> LF["Leapfrog (symplectic)"]
    FE --> CONV["Convergence & error"]
    RK --> CONV
    LF --> CONV
    CYC --> CONV

    LORENTZ --> GC["Guiding center & drifts"]
    LF --> GC
    CYC --> GC
    GC --> EXB["E×B drift"]
    GC --> GBC["Grad-B & curvature drifts"]
    GC --> MIRROR["Magnetic mirror"]
    MIRROR --> FERMI["Fermi acceleration"]

    ODE --> FDM["Finite difference method"]
    FDM --> POIS["Poisson solvers"]
    FDM --> FDTD["FDTD (Maxwell)"]
    LF --> FDTD
    FDTD --> CFL["CFL condition"]

    LF --> NBODY["N-body simulation"]
    NBODY --> PIC["Particle-in-cell"]
    POIS --> PIC
    PIC --> TWOSTREAM["Two-stream instability"]

    classDef found stroke:#4a90a4,stroke-width:2.5px
    classDef integ stroke:#c8963e,stroke-width:2.5px
    classDef orbit stroke:#8464a4,stroke-width:2.5px
    classDef field stroke:#54a06a,stroke-width:2.5px
    classDef many stroke:#c85454,stroke-width:2.5px
    class WHY,LORENTZ,CYC found
    class ODE,FE,BE,LF,RK,CONV integ
    class GC,EXB,GBC,MIRROR,FERMI orbit
    class FDM,POIS,FDTD,CFL field
    class NBODY,PIC,TWOSTREAM many
```

## Reading the map

- **Blue (foundations):** the physics being computed.
- **Amber (integrators):** Chapter 2 — how to march ODEs in time.
- **Purple (orbits):** Chapter 3 — single-particle motion and drift theory.
- **Green (fields):** Chapter 4 — grid-based solvers for potentials and waves.
- **Red (many-body):** Chapter 5 — the synthesis: self-consistent simulation.

**The spine of the course:**
[Lorentz force](equations/lorentz-force.md) →
[leapfrog](concepts/leapfrog-method.md) →
[drifts verified numerically](concepts/guiding-center-drifts.md) →
[Poisson on a grid](concepts/poisson-solvers.md) →
[PIC](concepts/pic-method.md) →
[two-stream instability](concepts/two-stream-instability.md).
