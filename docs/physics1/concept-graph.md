# Concept Graph · Physics I

Arrows mean *"understand this first"*. Machine-readable version:
[`graph/physics1_graph.json`](https://github.com/tpakorn/class-wiki/blob/main/graph/physics1_graph.json).

```mermaid
flowchart TD
    MEAS["Measurement & units"] --> KIN["Kinematics (1-D)"]
    MEAS --> VEC["Vectors"]
    KIN --> PROJ["Projectile motion"]
    VEC --> PROJ
    VEC --> REL["Relative motion"]
    KIN --> CIRC["Circular motion"]
    VEC --> CIRC

    KIN --> NEWT["Newton's laws"]
    VEC --> NEWT
    NEWT --> FRIC["Friction & drag"]
    NEWT --> WKE["Work & kinetic energy"]
    WKE --> PE["Potential energy"]
    PE --> COE["Conservation of energy"]

    NEWT --> CM["Center of mass"]
    NEWT --> MOM["Linear momentum"]
    MOM --> COLL["Collisions & impulse"]
    CM --> COLL

    NEWT --> ROT["Rotation"]
    CIRC --> ROT
    ROT --> MOI["Moment of inertia"]
    ROT --> TRQ["Torque"]
    VEC --> TRQ
    MOI --> ROLL["Rolling & angular momentum"]
    TRQ --> ROLL
    COE --> ROLL
    TRQ --> EQ["Equilibrium & elasticity"]

    NEWT --> GRAV["Gravitation"]
    CIRC --> GRAV
    PE --> GRAV
    GRAV --> KEP["Kepler's laws & orbits"]
    ROLL --> KEP

    EQ --> FLU["Fluid statics"]
    FLU --> BER["Continuity & Bernoulli"]
    COE --> BER

    PE --> SHM["Simple harmonic motion"]
    CIRC --> SHM
    SHM --> PEND["Pendulum"]
    TRQ --> PEND
    SHM --> DAMP["Damping & resonance"]
    FRIC --> DAMP
    SHM --> WAV["Traveling waves"]
    WAV --> SUP["Superposition & standing waves"]
    WAV --> SND["Sound waves"]
    SUP --> BEAT["Beats"]
    SND --> BEAT
    SND --> SHK["Shock waves"]

    COE --> TEMP["Temperature & heat"]
    TEMP --> FIRST["First law"]
    COLL --> IG["Ideal gas"]
    TEMP --> IG
    IG --> MB["Molecular speeds"]
    FIRST --> SECOND["Second law & entropy"]
    IG --> SECOND
    MB --> SECOND

    classDef motion stroke:#4a90a4,stroke-width:2.5px
    classDef dynamics stroke:#c8963e,stroke-width:2.5px
    classDef conserved stroke:#54a06a,stroke-width:2.5px
    classDef rot stroke:#8464a4,stroke-width:2.5px
    classDef contin stroke:#c85454,stroke-width:2.5px
    classDef thermo stroke:#a08b54,stroke-width:2.5px
    class MEAS,KIN,VEC,PROJ,REL,CIRC motion
    class NEWT,FRIC,GRAV,KEP dynamics
    class WKE,PE,COE,CM,MOM,COLL conserved
    class ROT,MOI,TRQ,ROLL,EQ rot
    class FLU,BER,SHM,PEND,DAMP,WAV,SUP,SND,BEAT,SHK contin
    class TEMP,FIRST,IG,MB,SECOND thermo
```

## Reading the map

- **Blue:** describing motion (kinematics & vectors)
- **Amber:** forces — Newton's program
- **Green:** the conservation laws (energy, momentum)
- **Purple:** rotation
- **Red:** continuous matter — fluids, oscillations, waves
- **Gold:** thermodynamics

**The spine:** [kinematics](concepts/kinematics.md) →
[Newton's laws](concepts/newtons-laws.md) →
[energy](concepts/conservation-of-energy.md) &
[momentum](concepts/linear-momentum.md) →
[rotation](concepts/rotation.md) → [SHM](concepts/simple-harmonic-motion.md) →
[waves](concepts/waves.md) → [entropy](concepts/second-law-of-thermodynamics.md).
