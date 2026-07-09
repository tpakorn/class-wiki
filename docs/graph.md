# The Knowledge Map

How the seven courses fit together — each node below is a whole course region;
arrows mean *"builds on"*. Every course also has its own detailed dependency graph:
[SC133](physics1/concept-graph.md) ·
[SC134](sc134/concept-graph.md) ·
[PC316](fluids/concept-graph.md) ·
[PC368](plasma/concept-graph.md) ·
[PHY621](phy621/concept-graph.md) ·
[PHY622](phy622/concept-graph.md) ·
[PHY653](comp-plasma/concept-graph.md).

```mermaid
flowchart TD
    subgraph SC133 ["SC133 · Physics for Engineers I"]
        MECH["Mechanics<br/>kinematics · Newton · energy"]
        FLU0["Intro fluids<br/>Archimedes · Bernoulli"]
        OSC["Oscillations & waves"]
        THERMO["Thermodynamics"]
    end

    subgraph SC134 ["SC134 · Physics for Engineers II"]
        EFIELD["Electrostatics<br/>Coulomb · Gauss · potential"]
        CIRC["Circuits<br/>DC · RC · RLC"]
        MAG["Magnetism & induction"]
        MAXW["Maxwell → EM waves"]
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

    subgraph PHY621 ["PHY621 · Math Methods I"]
        LINALG["Linear algebra & eigenmodes"]
        TRANS["Fourier & Laplace transforms"]
        DEQ["ODEs · PDEs · Green's functions"]
    end

    subgraph PHY622 ["PHY622 · Math Methods II"]
        VARC["Calculus of variations"]
        CPLX["Complex analysis"]
        GRP["Group theory"]
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

    MECH --> EFIELD
    EFIELD --> CIRC
    EFIELD --> MAG
    MAG --> MAXW
    OSC --> MAXW

    MECH --> SPM
    MAG --> SPM
    OSC --> WAV
    NS --> MHD
    MAXW --> MHD

    LINALG --> DEQ
    TRANS --> DEQ
    DEQ --> WAV
    LINALG -. "normal modes" .-> INST
    CPLX -. "contours" .-> WAV
    CPLX -. "conformal maps" .-> NS
    VARC -. "action principles" .-> MECH

    SPM --> ORBIT
    MECH --> INTEG
    INTEG --> ORBIT
    INTEG --> FIELDS
    MAXW --> FIELDS
    DEQ --> FIELDS
    FIELDS --> PIC
    ORBIT --> PIC
    WAV -. "verified by" .-> PIC
    INST -. "same method:<br/>perturb · linearize · grow" .-> WAV

    classDef intro stroke:#4a90a4,stroke-width:2.5px
    classDef em stroke:#54a06a,stroke-width:2.5px
    classDef fluid stroke:#c8963e,stroke-width:2.5px
    classDef plasma stroke:#8464a4,stroke-width:2.5px
    classDef math stroke:#a08b54,stroke-width:2.5px
    classDef comp stroke:#c85454,stroke-width:2.5px
    class MECH,FLU0,OSC,THERMO intro
    class EFIELD,CIRC,MAG,MAXW em
    class STAT,NS,DIMA,SHK,INST fluid
    class SPM,MHD,WAV plasma
    class LINALG,TRANS,DEQ,VARC,CPLX,GRP math
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
