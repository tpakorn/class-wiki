# Concept Graph · Fluid Mechanics

Arrows mean *"understand this first"*. The machine-readable version lives in
[`graph/fluids_graph.json`](https://github.com/tpakorn/class-wiki/blob/main/graph/fluids_graph.json).

```mermaid
flowchart TD
    FLUID["What is a fluid?"] --> PRESS["Pressure"]
    FLUID --> EULAG["Eulerian vs Lagrangian"]
    FLUID --> VISC["Viscosity"]

    PRESS --> HYDRO["Hydrostatic equilibrium"]
    HYDRO --> BUOY["Buoyancy"]
    HYDRO --> FSURF["Force on submerged surfaces"]
    HYDRO --> RBM["Rigid-body motion"]

    EULAG --> MATD["Material derivative"]
    MATD --> RTT["Reynolds transport theorem"]
    RTT --> CONT["Continuity equation"]
    RTT --> EULER["Euler's equation"]
    RBM --> EULER
    MATD --> EULER

    CONT --> BERN["Bernoulli's principle"]
    EULER --> BERN
    PRESS --> BERN

    CONT --> POT["Potential flow"]
    EULER --> POT
    POT --> CONF["Conformal mapping & images"]

    VISC --> NS["Navier–Stokes equation"]
    EULER --> NS
    NS --> EXACT["Couette · Poiseuille"]

    DIM["Dimensional analysis"] --> PI["Buckingham Pi"]
    DIM --> RE["Reynolds number"]
    VISC --> RE
    PI --> RE

    BERN --> SHOCK["Shock waves"]
    CONT --> SHOCK
    SHOCK --> RH["Rankine–Hugoniot"]
    RH --> BLAST["Blast waves (Sedov–Taylor)"]
    DIM --> BLAST

    NS --> STAB["Hydrodynamic stability"]
    STAB --> KH["Kelvin–Helmholtz"]
    STAB --> RT["Rayleigh–Taylor"]
    POT --> KH
    BUOY --> RT
    BERN --> KH

    RE --> TURB["Turbulence"]
    STAB --> TURB
    NS --> TURB
    TURB --> CASC["Energy cascade (K41)"]
    DIM --> CASC
    TURB --> RANS["Reynolds averaging / RANS"]
    RANS --> TKE["TKE budget"]
    CASC --> TKE

    classDef statics stroke:#4a90a4,stroke-width:2.5px
    classDef kinematics stroke:#c8963e,stroke-width:2.5px
    classDef dynamics stroke:#8464a4,stroke-width:2.5px
    classDef advanced stroke:#c85454,stroke-width:2.5px
    class FLUID,PRESS,HYDRO,BUOY,FSURF,RBM statics
    class EULAG,MATD,RTT,CONT kinematics
    class EULER,BERN,POT,CONF,VISC,NS,EXACT dynamics
    class DIM,PI,RE,SHOCK,RH,BLAST,STAB,KH,RT,TURB,CASC,RANS,TKE advanced
```

## Reading the map

- **Blue (statics):** the force-balance world — no motion yet.
- **Amber (kinematics):** describing motion and the bookkeeping theorems.
- **Purple (dynamics):** the governing equations, inviscid and viscous.
- **Red (advanced):** scaling, compressibility, instability, turbulence.

**Deepest dependency chain:**
[What is a fluid?](concepts/what-is-a-fluid.md) →
[Eulerian/Lagrangian](concepts/eulerian-vs-lagrangian.md) →
[Material derivative](concepts/material-derivative.md) →
[RTT](concepts/reynolds-transport-theorem.md) →
[Euler](equations/euler-equation.md) →
[Navier–Stokes](equations/navier-stokes-equation.md) →
[Stability](concepts/hydrodynamic-stability.md) →
[Turbulence](concepts/turbulence.md) →
[Energy cascade](concepts/energy-cascade.md).
