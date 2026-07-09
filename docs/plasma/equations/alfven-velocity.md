# Alfvén Speed

$$v_A = \frac{B}{\sqrt{\mu_0 \rho}}$$

*Source lecture:* pc368_lec05_mhd, pc368_lec17_sweetparker

## Physical Meaning

The Alfvén speed is the characteristic speed at which transverse MHD
disturbances propagate along magnetic field lines. It is the “speed of sound”
for magnetic tension.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $B$ | Magnetic field strength | T |
| $\rho$ | Mass density | kg m$^{-3}$ |
| $\mu_0$ | Vacuum permeability | N A$^{-2}$ |

## Assumptions

- Uniform, straight magnetic field.
- Single-fluid MHD.
- Low-frequency perturbation ($\omega \ll \omega_{ci}$).

## Derivation

From the linearized ideal MHD momentum and induction equations for a perturbation
$\delta \mathbf{B}$ along a uniform field $\mathbf{B}_0 = B_0 \hat{z}$:

$$\rho_0 \frac{\partial^2 \boldsymbol{\xi}}{\partial t^2} = \frac{(\mathbf{B}_0\cdot\nabla)(\mathbf{B}_0\cdot\nabla\boldsymbol{\xi}) - B_0^2 \nabla^2\boldsymbol{\xi}}{\mu_0}$$

For a transverse wave $\propto e^{i(kz - \omega t)}$: $\omega^2 = k^2 v_A^2$
with $v_A = B/\sqrt{\mu_0\rho}$.

## Applications

- **Tokamak stability:** $v_A$ sets the Alfvén transit time and Alfvén eigenmodes.
- **Reconnection rate:** Inflow speed $U_{in} \sim v_A M_A$.
- **Solar wind:** Observations match $v_A$ at 1 AU.

## Connections to Other Equations

- [Lundquist Number](../equations/lundquist-number.md): $S = \mu_0 v_A L / \eta$.
- [Sweet–Parker Model](../concepts/sweet-parker-model.md): Rate expressed via $v_A$.
- [Magnetized Waves](../concepts/magnetized-waves.md): Shear Alfvén branch.
