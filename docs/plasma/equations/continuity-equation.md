# Continuity Equation

$$\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{U}) = 0$$

*Source lecture:* pc368_lec05_mhd

## Physical Meaning

Mass (or particle number) is conserved. The continuity equation states that the
change in density at a point equals the net flux of fluid into that point.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\rho$ | Mass density | kg m$^{-3}$ |
| $\mathbf{U}$ | Fluid velocity | m s$^{-1}$ |
| $t$ | Time | s |

## Assumptions

- Single-species or multi-species with negligible inter-species diffusion.
- Fluid description valid (continuum limit).

## Derivation

Integrate the zeroth velocity moment of the Boltzmann equation over velocity
space:

$$\int \Bigl(\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}\mathbf{F}\cdot\frac{\partial f}{\partial \mathbf{v}} + C[f]\Bigr) d^3v = 0$$

For collisionless evolution or when collisional terms conserve particles, the
integral yields:

$$\frac{\partial}{\partial t}\int f d^3v + \nabla\cdot\int \mathbf{v} f d^3v = 0$$

Define $n = \int f d^3v$ and $\Gamma = n\mathbf{U} = \int \mathbf{v} f d^3v$ to obtain
the continuity equation.

## Applications

- **Mass balance** in compressible flows.
- **Source terms** for ionization.
- **Radial transport** in tokamaks.

## Connections to Other Equations

- [Momentum Equation](../equations/momentum-equation.md): Coupled with continuity in MHD.
- [Induction Equation](../equations/induction-equation.md): Completes the MHD system.
