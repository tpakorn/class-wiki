# Momentum Equation

$$\rho \frac{D\mathbf{U}}{Dt} = -\nabla p + \mathbf{J}\times\mathbf{B} + \mu \nabla^2\mathbf{U}$$

*Source lecture(s):* [pc368_lec05_mhd](../lectures.md)

## Physical Meaning

The momentum equation balances the rate of change of fluid momentum with forces:
pressure gradients, electromagnetic Lorentz force, and viscous stress.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\rho$ | Fluid mass density | kg m$^{-3}$ |
| $\mathbf{U}$ | Fluid velocity | m s$^{-1}$ |
| $p$ | Fluid pressure | Pa |
| $\mathbf{J}$ | Current density | A m$^{-2}$ |
| $\mathbf{B}$ | Magnetic field | T |
| $\mu$ | Dynamic viscosity | Pa·s |

## Assumptions

- Single MHD fluid.
- Scalar, isotropic pressure.
- Ohmic dissipation via $\mathbf{E} + \mathbf{U}\times\mathbf{B} = \eta\mathbf{J}$.

## Derivation

Take the first velocity moment of the Boltzmann equation with collision operator
that conserves momentum. The Lorentz force appears as $\int (q/m)\mathbf{E} f d^3v +
\int (q/m)\mathbf{v}\times\mathbf{B} f d^3v = \rho_c \mathbf{E} + \mathbf{J}\times\mathbf{B}$.

## Applications

- **Z-pinch equilibrium:** $dp/dr = B_\theta^2/\mu_0$.
- **Tokamak force balance:** Toroidal/poloidal field stresses.
- **Alfvén waves:** Inertial term $\rho \partial \mathbf{U}/\partial t$ vs.
  magnetic tension.

## Connections to Other Equations

- [MHD](../concepts/mhd.md): Part of the MHD system.
- [Alfvén Speed](../equations/alfven-velocity.md): Derived from momentum + induction.
