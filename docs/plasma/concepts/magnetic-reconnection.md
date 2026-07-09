# Magnetic Reconnection

*Source lecture:* pc368_lec16_reconnection

## Intuition

Magnetic field lines are not rigid. When field lines of opposite polarity are
pushed together by plasma motions, they can break and reconnect, forming new
topologies. This process converts magnetic energy into particle acceleration,
heating, and turbulence. It powers solar flares, magnetospheric substorms, and
spheromak formation.

## Formal Definition

**Magnetic reconnection** is a topological rearrangement of magnetic flux in which
non-ideal terms ($\eta$, electron inertia, or kinetic effects) allow $\mathbf{E}_{\parallel} \neq 0$
in a localized diffusion region, changing the connectivity of field lines.

## Mathematical Formulation

Faraday’s law in resistive MHD:

$$\frac{\partial \mathbf{B}}{\partial t} = -\nabla\times\mathbf{E}$$

Ohm’s law:

$$\mathbf{E} + \mathbf{U}\times\mathbf{B} = \eta\mathbf{J}$$

Reconnection rate $V_{\text{rec}}$ is the speed at which magnetic flux is
transferred across the separator:

$$V_{\text{rec}} \sim v_A M_A$$

where $M_A = U_{\text{in}}/v_A$ is the inflow Alfvén Mach number.

## Derivation

1. Consider two antiparallel field regions pushed together at speed $U_{\text{in}}$.
2. In the inflow region ($\mathbf{U}\times\mathbf{B}$ dominates), plasma moves
   toward the current sheet.
3. Inside the sheet (resistive), $\eta\mathbf{J}$ permits $E_\parallel$.
4. Ampère’s law links current to field gradient; balance gives sheet thickness.
5. Mass conservation links inflow to outflow velocity.

## Worked Example

> **Sweet–Parker sheet:** For $S = \mu_0 v_A L/\eta = 10^8$ and $L = 10^6$ m,
> the sheet half-thickness is $\delta \sim L S^{-1/2} = 100$ m.
> The reconnection rate $M_A = S^{-1/2} = 10^{-4}$.
> This is extremely slow; observed reconnection in the corona is orders of
> magnitude faster, motivating Petschek and collisionless mechanisms.

## Common Mistakes

- **Reconnection is caused by resistivity alone.** Astrophysics needs fast
  reconnection, which requires localized anomalous resistivity or collisionless
  Hall effects.
- **Field lines “break” physically.** They are not physical ropes; their
  connectivity changes, not their substance.
- **Reconnection rate is universal.** It depends sensitively on geometry,
  boundary conditions, and kinetic physics.

## Related Concepts

- [Sweet–Parker Model](sweet-parker-model.md)
- [MHD](mhd.md)
- [Lundquist Number](../equations/lundquist-number.md)
- [Magnetic Islands](magnetic-islands.md)

## Quiz Questions

1. **Conceptual:** Why can reconnection occur in ideal MHD at a single line of
   zero width but not in a finite volume?
2. **Computational:** Derive the Sweet–Parker reconnection rate $M_A = S^{-1/2}$
   from force balance and mass continuity.
3. **MCQ:** The most important *non-ideal* term in Sweet–Parker reconnection is:
   - A) Electron inertia
   - B) Resistivity $\eta$
   - C) Hall term
   - D) Electron pressure gradient

## Further Reading

- E. Priest & T. Forbes, *Magnetic Reconnection*.
