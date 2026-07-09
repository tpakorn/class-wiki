# Laplace's Equation (Potential Flow)

## Equation

$$\boxed{\,\nabla^2\phi = 0\,} \qquad \text{and in 2-D also}\quad \nabla^2\psi = 0$$

## Physical meaning

The governing equation of [potential flow](../concepts/potential-flow.md): a velocity
field that is both irrotational ($\mathbf{v} = \nabla\phi$) and incompressible
($\nabla\cdot\mathbf{v} = 0$) must have a harmonic potential. The same equation rules
electrostatics and Newtonian gravity — one PDE, three physical theories, and every
solution technique transfers.

## Variables

| Symbol | Meaning | SI unit |
|---|---|---|
| $\phi$ | velocity potential ($\mathbf{v} = \nabla\phi$) | m² s⁻¹ |
| $\psi$ | stream function ($u = \partial_y\psi$, $v = -\partial_x\psi$) | m² s⁻¹ |

## Assumptions

Irrotational ($\nabla\times\mathbf{v}=0$) + incompressible ($\nabla\cdot\mathbf{v}=0$).
Away from boundaries and wakes at high [Reynolds number](../concepts/reynolds-number.md),
these hold remarkably well.

## Derivation

$$\nabla\cdot\mathbf{v} = \nabla\cdot(\nabla\phi) = \nabla^2\phi = 0$$

For $\psi$: the definition satisfies continuity identically, and irrotationality
$\partial_x v - \partial_y u = 0$ gives $\nabla^2\psi = 0$.

## Properties that do all the work

- **Linearity → superposition:** build flows from
  [elementary solutions](../concepts/potential-flow.md#elementary-solutions-the-lego-bricks)
  (uniform, source, vortex, doublet)
- **Maximum principle:** no interior velocity extrema — stagnation points live on
  boundaries
- **Uniqueness:** boundary conditions determine the flow
- **Conformal invariance:** solutions map to solutions —
  [Joukowski airfoils](../concepts/conformal-mapping-and-images.md)

## Applications

Airfoil lift (with circulation), flow around cylinders/half-bodies, groundwater flow,
[surface-wave theory](interface-dispersion-relation.md) (the perturbation potentials
solve Laplace), and the [Poisson-equation solvers](../../comp-plasma/index.md) of
computational physics (Laplace = Poisson with zero source).

## Limitations

No viscosity ⇒ no drag, no boundary layers, no separation. Wakes and lift require
injecting circulation/vortex sheets by hand.

## Related equations

- [Continuity equation](continuity-equation.md) — one of its two parents
- [Bernoulli's equation](bernoulli-equation.md) — recovers pressure after solving
- [Interface dispersion relation](interface-dispersion-relation.md) — Laplace + boundary conditions

## Quiz

**Q1 (conceptual).** Why does $\phi$ exist only for irrotational flows, while $\psi$
(2-D) exists for any incompressible flow?

??? success "Answer"
    $\mathbf{v} = \nabla\phi$ *forces* $\nabla\times\mathbf{v} = 0$, so a rotational
    flow can't have a $\phi$. The stream function only encodes
    $\nabla\cdot\mathbf{v} = 0$; $\psi$ exists for shear flows too — it just isn't
    harmonic unless the flow is also irrotational.

**Q2 (computational).** Verify that $\phi = \frac{Q}{2\pi}\ln r$ solves
$\nabla^2\phi = 0$ for $r \neq 0$.

??? success "Answer"
    In polar coordinates $\nabla^2\phi = \frac{1}{r}\partial_r(r\,\partial_r\phi) =
    \frac{1}{r}\partial_r\left(r\cdot\frac{Q}{2\pi r}\right) = \frac{1}{r}\partial_r\left(\frac{Q}{2\pi}\right) = 0$.
    The singularity at $r=0$ is the source itself.
