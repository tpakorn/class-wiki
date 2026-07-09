# Induction Equation

$$\frac{\partial \mathbf{B}}{\partial t} = \nabla\times(\mathbf{U}\times\mathbf{B}) + \eta \nabla^2\mathbf{B}$$

*Source lecture:* pc368_lec05_mhd

## Physical Meaning

The induction equation describes how magnetic field evolves due to advection by
the fluid and resistive diffusion. It is the MHD analog of the vorticity equation.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\mathbf{B}$ | Magnetic field | T |
| $\mathbf{U}$ | Fluid velocity | m s$^{-1}$ |
| $\eta$ | Magnetic diffusivity | m$^2$ s$^{-1}$ |

## Assumptions

- Ohm’s law: $\mathbf{E} + \mathbf{U}\times\mathbf{B} = \eta\mathbf{J}$.
- Ampère’s law: $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ (neglecting
  displacement current for low-frequency MHD).
- $\nabla\cdot\mathbf{B} = 0$ is preserved by induction.

## Derivation

Start with $\mathbf{E} = -\mathbf{U}\times\mathbf{B} + \eta\mathbf{J}$.
Use Faraday’s law:

$$\frac{\partial \mathbf{B}}{\partial t} = -\nabla\times\mathbf{E} = \nabla\times(\mathbf{U}\times\mathbf{B}) - \eta\nabla\times\mathbf{J}$$

Insert $\mathbf{J} = (1/\mu_0)\nabla\times\mathbf{B}$ and neglect displacement
current to obtain the induction equation.

## Applications

- **Dynamo theory:** $\eta \nabla^2\mathbf{B}$ amplifies field in stars/planets.
- **Reconnection:** Resistive term allows field-line topology change.
- **Flux conservation:** When $\eta=0$, ideal induction yields frozen-in theorem.

## Connections to Other Equations

- [Frozen-in Theorem](../concepts/frozen-in-theorem.md): $\eta=0$ limit.
- [Lundquist Number](../equations/lundquist-number.md): Ratio of advection to diffusion.
- [Sweet–Parker Model](../concepts/sweet-parker-model.md): Steady-state solution of induction
  with Ohmic diffusion.
