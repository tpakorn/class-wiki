# Euler's Equation

## Equation

$$\boxed{\;\rho\frac{D\mathbf{v}}{Dt} = \rho\left[\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}\right] = -\nabla p + \rho\mathbf{g}\;}$$

## Physical meaning

Newton's second law for an **inviscid** fluid element: mass × acceleration (following
the particle — hence the [material derivative](../concepts/material-derivative.md)) =
pressure-gradient force + body force. Fluid accelerates from high toward low pressure,
and falls under gravity, and that is all — no friction.

## Variables

| Symbol | Meaning | SI unit |
|---|---|---|
| $\rho$ | density | kg m⁻³ |
| $\mathbf{v}$ | velocity field | m s⁻¹ |
| $p$ | pressure | Pa |
| $\mathbf{g}$ | body force per unit mass | m s⁻² |

## Assumptions

- Inviscid: $\mu = 0$ (no shear stresses) — valid far from walls at high
  [Reynolds number](../concepts/reynolds-number.md)
- Continuum; pair with [continuity](continuity-equation.md) (and an energy/state
  equation if compressible) for a closed system

## Derivation

For a fluid element, the surface force is the net pressure push. Component $z$ across a
box $dx\,dy\,dz$: $\left(p - \frac{\partial p}{\partial z}\frac{dz}{2}\right)dxdy -
\left(p + \frac{\partial p}{\partial z}\frac{dz}{2}\right)dxdy = -\frac{\partial p}{\partial z}dV$.
Collecting components: $\delta\mathbf{F}_S = -\nabla p\, dV$. Adding weight
$\rho\mathbf{g}\,dV$ and equating to $(\rho\,dV)\,D\mathbf{v}/Dt$ gives the equation.
Equivalently: momentum via the
[Reynolds transport theorem](../concepts/reynolds-transport-theorem.md) with stress
tensor $\mathbf{T} = -p\mathbf{I}$.

## Special cases

- **Hydrostatics** ($\mathbf{v} = 0$): $\nabla p = \rho\mathbf{g}$ →
  [hydrostatic equilibrium](../concepts/hydrostatic-equilibrium.md), $p = p_0 - \rho g z$.
- **Rigid-body motion:** $\nabla p + \rho g\hat k = -\rho\mathbf{a}$ →
  [tilted and parabolic free surfaces](../concepts/fluid-in-rigid-body-motion.md).
- **Steady flow along a streamline:** integrates to
  [Bernoulli's equation](bernoulli-equation.md).
- **Irrotational flow:** $\mathbf{v} = \nabla\phi$ →
  [potential flow](../concepts/potential-flow.md) with a global Bernoulli constant.

## Worked example: converging nozzle

Steady horizontal nozzle, sections 1 → 2. Euler along the streamline reduces to
Bernoulli: $p_1 - p_2 = \frac{\rho}{2}(v_2^2 - v_1^2)$; with
[continuity](continuity-equation.md) $v_2 = v_1 A_1/A_2 > v_1$, so $p_2 < p_1$ —
pressure falls in the direction of acceleration, exactly as the equation's
$-\nabla p$ demands.

## Limitations

No boundary layers, no drag (d'Alembert's paradox), no
[dissipation](../concepts/viscosity.md) — add $\mu\nabla^2\mathbf{v}$ to get
[Navier–Stokes](navier-stokes-equation.md). Across [shocks](../concepts/shock-waves.md)
the differential form fails; use [jump conditions](rankine-hugoniot-conditions.md).

## Related equations

- [Navier–Stokes equation](navier-stokes-equation.md) — Euler + viscosity
- [Bernoulli's equation](bernoulli-equation.md) — first integral
- [Continuity equation](continuity-equation.md) — always solved alongside

## Quiz

**Q1 (conceptual).** Euler's equation contains no viscosity, yet predicts pressure
perfectly well in a static fluid. Why is the inviscid assumption harmless there?

??? success "Answer"
    Viscous stress is proportional to *velocity gradients*; at rest they vanish
    identically, so the viscous term would contribute nothing anyway.

**Q2 (multiple choice).** In steady flow, a fluid particle in a horizontal plane
accelerates only if:

- (a) $\partial\mathbf{v}/\partial t \neq 0$  (b) a pressure gradient (or body force) acts
- (c) the flow is compressible  (d) vorticity is nonzero

??? success "Answer"
    **(b).** $D\mathbf{v}/Dt = -\nabla p/\rho + \mathbf{g}$: convective acceleration
    requires a force just like any other acceleration.
