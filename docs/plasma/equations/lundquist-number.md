# Lundquist Number

$$S = \frac{\mu_0 v_A L}{\eta}$$

*Source lecture:* pc368_lec17_sweetparker

## Physical Meaning

The Lundquist number is the ratio of magnetic advection time to magnetic diffusion
time. It is the magnetic Reynolds number in MHD.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\mu_0$ | Vacuum permeability | N A$^{-2}$ |
| $v_A$ | Alfvén speed | m s$^{-1}$ |
| $L$ | Characteristic length | m |
| $\eta$ | Magnetic diffusivity | m$^2$ s$^{-1}$ |

## Assumptions

- Single-fluid resistive MHD.
- Global scale $L$ is much larger than resistive dissipation scale.

## Derivation

Advection time: $\tau_A = L/v_A$.

Diffusion time: $\tau_\eta = \mu_0 L^2/\eta$.

Ratio:

$$S = \frac{\tau_\eta}{\tau_A} = \frac{\mu_0 v_A L}{\eta}$$

## Applications

- **Sweet–Parker sheet:** $M_A \sim S^{-1/2}$.
- **CRM:** Fast reconnection requires $S$ locally to drop or kinetic processes.
- **Dynamo:** Field sustains if $S \gg 1$ and the flow has suitable helicity.

## Connections to Other Equations

- [Alfvén Speed](../equations/alfven-velocity.md): Appears in numerator.
- [Sweet–Parker Model](../concepts/sweet-parker-model.md): Reconnection rate $\sim S^{-1/2}$.
