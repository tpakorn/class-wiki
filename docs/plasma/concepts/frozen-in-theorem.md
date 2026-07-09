# Frozen-in Theorem

*Source lecture:* pc368_lec05_mhd

## Intuition

In a perfectly conducting fluid, magnetic field lines cannot end; they must move
together with the plasma. Imagine drawing field lines on a rubber sheet and
stretching the sheet—the lines go wherever the material goes. This is the
**frozen-in** property of ideal MHD.

## Formal Definition

Let $\mathbf{B}/\rho$ be the magnetic flux per unit mass. In an ideal,
incompressible conductor:

$$\frac{D}{Dt}\left(\frac{\mathbf{B}}{\rho}\right) = 0$$

For incompressible flow ($\rho=$ const), the field lines are simply advected:

$$\frac{\partial \mathbf{B}}{\partial t} = \nabla\times(\mathbf{U}\times\mathbf{B})$$

## Mathematical Formulation

Start with ideal Ohm’s law:

$$\mathbf{E} + \mathbf{U}\times\mathbf{B} = 0$$

Combine with Faraday’s law $\partial \mathbf{B}/\partial t = -\nabla\times\mathbf{E}$:

$$\frac{\partial \mathbf{B}}{\partial t} = \nabla\times(\mathbf{U}\times\mathbf{B})$$

For an incompressible fluid, this implies that magnetic flux $\oint \mathbf{B}\cdot d\mathbf{S}$
through any fluid element is conserved in time.

## Derivation

1. Write Faraday’s law: $\partial \mathbf{B}/\partial t = -\nabla\times\mathbf{E}$.
2. Insert ideal Ohm’s law: $\mathbf{E} = -\mathbf{U}\times\mathbf{B}$.
3. Use vector identity: $\nabla\times(\mathbf{U}\times\mathbf{B}) =
   (\mathbf{B}\cdot\nabla)\mathbf{U} - (\mathbf{U}\cdot\nabla)\mathbf{B} - \mathbf{B}(\nabla\cdot\mathbf{U})
   + \mathbf{U}(\nabla\cdot\mathbf{B})$.
4. With $\nabla\cdot\mathbf{B}=0$, this becomes the induction equation.
5. Interpret $\partial \mathbf{B}/\partial t$ as the change of $\mathbf{B}$
   seen by an observer moving with velocity $\mathbf{U}$.

## Worked Example

> **Solar corona:** A coronal loop is a bundle of field lines “frozen” into the
> plasma. If photospheric motions twist the footpoints, the loop twists like a
> rope. Reconnection can release the magnetic energy in a flare.

Mathematically: if $B_\phi(r)$ grows with twist, the magnetic helicity
$K = \int \mathbf{A}\cdot\mathbf{B}\, dV$ is conserved until a
non-ideal event breaks the topology.

## Common Mistakes

- **Frozen-in is exact at all scales.** No; reconnection breaks it when $\eta
  \neq 0$ or at kinetic scales where electron inertia matters.
- **Field lines are material strings.** They are topological constructs; they do
  not have a finite “thickness” or rest mass.
- **Incompressibility is required.** The frozen-in theorem holds more generally
  as flux conservation even in compressible flows.

## Related Concepts

- [MHD](mhd.md)
- [Magnetic Reconnection](magnetic-reconnection.md)
- [Lundquist Number](../equations/lundquist-number.md)

## Quiz Questions

1. **Conceptual:** Explain in one sentence why an perfect conductor cannot
   allow magnetic flux to pass through its interior if it was initially excluded.
2. **Computational:** Show that $\nabla\cdot\mathbf{B}=0$ is preserved by
   the induction equation.
3. **MCQ:** The frozen-in property fails when:
   - A) $\eta = 0$
   - B) $\eta \neq 0$ and $\nabla\times\mathbf{E} \neq -\mathbf{U}\times\mathbf{B}$
   - C) The plasma is collisionless
   - D) $\mathbf{U} = 0$

## Further Reading

- E. Priest, *Solar Magnetohydrodynamics*.
