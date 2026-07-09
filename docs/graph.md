# The Knowledge Map

How the four courses fit together — each node below is a whole course region;
arrows mean *"builds on"*. Every course also has its own detailed dependency graph:
[SC133](physics1/concept-graph.md) ·
[PC368](plasma/concept-graph.md) ·
[PC316](fluids/concept-graph.md) ·
[PHY653](comp-plasma/concept-graph.md).

```mermaid
flowchart TD
    subgraph SC133 ["SC133 · Physics for Engineers I"]
        MECH["Mechanics<br/>kinematics · Newton · energy"]
        FLU0["Intro fluids<br/>Archimedes · Bernoulli"]
        OSC["Oscillations & waves"]
        THERMO["Thermodynamics"]
    end

    subgraph PC316 ["PC316 · Fluid Mechanics"]
        STAT["Fluid statics & kinematics"]
        NS["Euler → Navier–Stokes"]
        DIMA["Dimensional analysis"]
        SHK["Shocks"]
        INST["Instabilities & turbulence"]
    end

    subgraph PC368 ["PC368 · Plasma Physics"]
        SPM["Single-particle motion"]
        MHD["MHD"]
        WAV["Plasma waves & kinetics"]
    end

    subgraph PHY653 ["PHY653 · Computational EM & Plasma"]
        INTEG["Time integrators"]
        ORBIT["Orbit simulation & drifts"]
        FIELDS["Field solvers (Poisson · FDTD)"]
        PIC["N-body & PIC"]
    end

    MECH --> STAT
    FLU0 --> STAT
    STAT --> NS
    NS --> INST
    NS --> SHK
    DIMA --> INST
    THERMO --> SHK

    MECH --> SPM
    OSC --> WAV
    NS --> MHD
    SHK -. "MHD shocks" .-> MHD

    SPM --> ORBIT
    MECH --> INTEG
    INTEG --> ORBIT
    INTEG --> FIELDS
    FIELDS --> PIC
    ORBIT --> PIC
    WAV -. "verified by" .-> PIC
    INST -. "same method:<br/>perturb · linearize · grow" .-> WAV

    classDef intro fill:#e8f4f8,stroke:#4a90a4
    classDef fluid fill:#fdf2e0,stroke:#c8963e
    classDef plasma fill:#efe8f8,stroke:#8464a4
    classDef comp fill:#fde8e8,stroke:#c85454
    class MECH,FLU0,OSC,THERMO intro
    class STAT,NS,DIMA,SHK,INST fluid
    class SPM,MHD,WAV plasma
    class INTEG,ORBIT,FIELDS,PIC comp
```

## The through-lines

**Continuum mechanics.** [SC133's fluids](physics1/concepts/fluids.md) preview
[PC316](fluids/index.md), which culminates in
[Navier–Stokes](fluids/equations/navier-stokes-equation.md); add electromagnetic
forces and a conducting fluid and you have [MHD in PC368](plasma/concepts/mhd.md).

**The perturbation method.** Equilibrium → perturb → linearize → normal modes →
growth rate. Learned in [PC316 stability theory](fluids/concepts/hydrodynamic-stability.md),
reused for [MHD instabilities](plasma/concepts/mhd-instability.md) and
[plasma waves](plasma/concepts/plasma-waves.md), then *measured numerically* in the
[PHY653 two-stream simulation](comp-plasma/concepts/two-stream-instability.md).

**Particles in fields.** [Newton's laws](physics1/concepts/newtons-laws.md) →
[drift theory in PC368](plasma/concepts/drift-motion.md) →
[computed orbits in PHY653](comp-plasma/concepts/guiding-center-drifts.md), where the
theory is checked against direct integration.

**Theory ↔ computation.** PC368 derives what PHY653 simulates: compare
[Landau damping](plasma/concepts/landau-damping.md) (kinetic theory) with the
[PIC method](comp-plasma/concepts/pic-method.md) sampling the same
[Vlasov equation](plasma/concepts/vlasov-equation.md).

## Machine-readable graphs

Per-course JSON dependency graphs live in the repo's
[`graph/`](https://github.com/tpakorn/class-wiki/tree/main/graph) directory —
nodes (concepts and equations, with aliases) and typed edges
(`prerequisite` / `related`), one file per course.
