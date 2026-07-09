# Continuity Equation

## Equation

$$\boxed{\;\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho\mathbf{v}) = 0\;}$$

Incompressible form: $\;\nabla\cdot\mathbf{v} = 0$.
Streamtube (1-D steady) form: $\;\dot m = \rho A v = \text{const}$, and for constant
density $A_1v_1 = A_2v_2$.

## Physical meaning

Mass is neither created nor destroyed. Whatever mass leaves a region must have flowed
out through its boundary. The incompressible version says fluid elements keep their
volume: squeeze a flow into a narrower channel and it *must* speed up.

## Variables

| Symbol | Meaning | SI unit |
|---|---|---|
| $\rho$ | density | kg m⁻³ |
| $\mathbf{v}$ | velocity field | m s⁻¹ |
| $\dot m$ | mass flow rate | kg s⁻¹ |
| $A$ | streamtube cross-section | m² |

## Assumptions

None beyond the [continuum hypothesis](../concepts/what-is-a-fluid.md) and no
mass sources/sinks. The *incompressible* form additionally requires $D\rho/Dt = 0$
(good for liquids generally, and for gases at Mach ≲ 0.3).

## Derivation

Fix a control volume $V$ with boundary $S$. Conservation of mass:

$$\frac{d}{dt}\int_V \rho\, dV + \oint_S \rho\mathbf{v}\cdot d\mathbf{S} = 0$$

Divergence theorem on the flux term:

$$\int_V \left[\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{v})\right] dV = 0$$

Arbitrary $V$ ⇒ the integrand vanishes pointwise. (Equivalently: set $f = \rho$ in the
[Reynolds transport theorem](../concepts/reynolds-transport-theorem.md).)

## Applications

- Nozzles and pipe networks ($A_1v_1 = A_2v_2$) — the first tool in every
  [Bernoulli](bernoulli-equation.md) problem
- The [necking of a falling water stream](../examples/necking-stream.md)
- Defining the [stream function](../concepts/potential-flow.md) in 2-D
- Deriving every other conservation law's differential form

## Limitations

Breaks only where the continuum itself breaks (free-molecular flow) — or if you apply
the incompressible form to genuinely compressible situations
([shocks](../concepts/shock-waves.md), high-Mach flight, acoustics).

## Related equations

- [Euler's equation](euler-equation.md) — momentum sibling
- [Navier–Stokes](navier-stokes-equation.md) — viscous momentum sibling
- [Laplace's equation](laplace-equation.md) — continuity + irrotationality
- [Rankine–Hugoniot](rankine-hugoniot-conditions.md) — its jump-condition avatar

## Quiz

**Q1 (computational).** Water enters a nozzle at 2 m/s through a 4 cm² section and
exits through 1 cm². Exit speed?

??? success "Answer"
    $v_2 = v_1 A_1/A_2 = 2\times 4 = 8$ m/s.

**Q2 (conceptual).** Show that steady flow ($\partial\rho/\partial t = 0$) does *not*
imply incompressible flow.

??? success "Answer"
    Steady gives $\nabla\cdot(\rho\mathbf{v}) = 0$, i.e.
    $\rho\nabla\cdot\mathbf{v} = -\mathbf{v}\cdot\nabla\rho$. If density varies along
    streamlines (e.g. a steady nozzle at Mach 2), $\nabla\cdot\mathbf{v} \neq 0$.
