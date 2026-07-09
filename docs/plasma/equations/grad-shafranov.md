# Grad–Shafranov Equation

$$\Delta^* \psi + \mu_0 R^2 \frac{dp}{d\psi} + F \frac{dF}{d\psi} = 0$$

*Source lecture:* pc368_lec14_mhd_equilibrium

## Physical Meaning

The Grad–Shafranov equation is the fundamental PDE of axisymmetric MHD
equilibrium. It relates the poloidal flux $\psi$ to the pressure profile $p(\psi)$
and the toroidal field function $F(\psi) = R B_\phi$.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\psi(R,Z)$ | Poloidal magnetic flux | Wb |
| $p(\psi)$ | Plasma pressure | Pa |
| $F(\psi) = R B_\phi$ | Toroidal field stream function | T·m |
| $R$ | Major radius | m |
| $\mu_0$ | Vacuum permeability | N A$^{-2}$ |

## Assumptions

- Axisymmetry: $\partial/\partial \phi = 0$.
- Static or steady-state equilibrium.
- Toroidal current flows in flux surfaces.

## Derivation

1. Begin with $\mathbf{J}\times\mathbf{B} = \nabla p$ and $\mathbf{B} = \nabla\times\mathbf{A}$.
2. In axisymmetry, $\mathbf{A} = \psi(R,Z) \nabla\phi$.
3. Express $\mathbf{B}$ and $\mathbf{J}$ in terms of $\psi$ and $F$.
4. Substitute into force balance and separate poloidal/radial components.
5. The resulting equation is the Grad–Shafranov equation above.

## Applications

- **Tokamak design:** Equilibrium solvers (e.g., EFIT) use this equation.
- **Stellarators:** Flux-surface optimization.
- **Z-pinch and spheromak:** Axisymmetric equilibria.

## Connections to Other Equations

- [MHD Equilibrium](../concepts/mhd-equilibrium.md): The physical concept.
- [MHD Instability](../concepts/mhd-instability.md): $\delta W$ computed on GS equilibria.
- [Alfvén Speed](../equations/alfven-velocity.md): Sets characteristic wave speed.
