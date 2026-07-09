# The Navier–Stokes Equation

## Equation

For an incompressible Newtonian fluid:

$$\boxed{\;\rho\left[\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}\right]
= -\nabla p + \mu\nabla^2\mathbf{v} + \mathbf{f}\;}
\qquad \nabla\cdot\mathbf{v} = 0$$

## Physical meaning — term by term

| Term | Reading |
|---|---|
| $\rho\,\partial\mathbf{v}/\partial t$ | unsteady acceleration |
| $\rho(\mathbf{v}\cdot\nabla)\mathbf{v}$ | convective acceleration — *the* nonlinearity |
| $-\nabla p$ | pressure-gradient force |
| $\mu\nabla^2\mathbf{v}$ | viscous diffusion of momentum |
| $\mathbf{f}$ | body forces (gravity, EM, …) |

It is [Euler's equation](euler-equation.md) plus momentum diffusion: fast regions leak
momentum to slow neighbors at rate set by [viscosity](../concepts/viscosity.md).

## Variables

$\rho$ — density (kg m⁻³) · $\mathbf{v}$ — velocity (m s⁻¹) · $p$ — pressure (Pa) ·
$\mu$ — dynamic viscosity (Pa·s) · $\mathbf{f}$ — body force density (N m⁻³).

## Assumptions

Continuum · Newtonian
([stress ∝ strain rate](newtons-law-of-viscosity.md)) · incompressible in this form ·
constant $\mu$. Compressible and non-Newtonian generalizations exist but are beyond
PC316.

## Derivation sketch

Apply the [Reynolds transport theorem](../concepts/reynolds-transport-theorem.md) to
momentum with the full stress tensor
$T_{ij} = -p\,\delta_{ij} + \mu\left(\partial_i v_j + \partial_j v_i\right)$
(Newtonian constitutive law). The divergence of the viscous part, with
$\nabla\cdot\mathbf{v} = 0$, collapses to $\mu\nabla^2\mathbf{v}$.

## Exact solutions

Rare and precious — found by symmetry + assumptions + boundary conditions:

- **[Couette flow](../examples/couette-flow.md):** linear profile between sliding plates
- **[Hagen–Poiseuille](../examples/hagen-poiseuille-flow.md):** parabolic pipe profile, $Q \propto R^4$
- **[Two-layer inclined film](../examples/two-layer-incline.md):** stacked viscous films

Almost everything else — including whether smooth 3-D solutions always *exist* — is
open. That existence-and-smoothness question is one of the Clay Millennium Prize
Problems (US$1M).

## Applications

All of real fluid dynamics: aerodynamics, hemodynamics, meteorology, oceanography,
lubrication, microfluidics, [turbulence](../concepts/turbulence.md) (by direct
simulation at modest $Re$, by [RANS modeling](../concepts/reynolds-averaging.md)
beyond).

## Limitations

Continuum only (no rarefied gases); Newtonian only; numerically brutal at high
[Reynolds number](../concepts/reynolds-number.md) (resolution cost $\sim Re^{9/4}$ —
see the [energy cascade](../concepts/energy-cascade.md)).

## Related equations

- [Euler's equation](euler-equation.md) — the $\mu \to 0$ limit
- [Newton's law of viscosity](newtons-law-of-viscosity.md) — the constitutive input
- [Continuity equation](continuity-equation.md) — solved simultaneously
- [TKE transport equation](tke-transport-equation.md) — its averaged energy shadow

## Quiz

**Q1 (conceptual).** Nondimensionalize Navier–Stokes with scales $U, L$. What single
parameter remains, and where?

??? success "Answer"
    $\frac{\partial\mathbf{v}^*}{\partial t^*} + (\mathbf{v}^*\cdot\nabla^*)\mathbf{v}^*
    = -\nabla^* p^* + \frac{1}{Re}\nabla^{*2}\mathbf{v}^*$ — the
    [Reynolds number](../concepts/reynolds-number.md), multiplying (inversely) the
    viscous term. Dynamic similarity follows immediately.

**Q2 (multiple choice).** Which term makes superposition of solutions fail?

- (a) $-\nabla p$  (b) $\mu\nabla^2\mathbf{v}$  (c) $(\mathbf{v}\cdot\nabla)\mathbf{v}$  (d) $\mathbf{f}$

??? success "Answer"
    **(c)** — quadratic in $\mathbf{v}$; all other terms are linear.

**Q3 (computational).** For fully developed flow between fixed plates driven by
$dp/dx = -G$ (gap $2h$, centered at $y=0$), find $u(y)$.

??? success "Answer"
    $\mu\,u'' = -G \Rightarrow u = \frac{G}{2\mu}(h^2 - y^2)$ — the plane-Poiseuille
    parabola, by direct double integration with no-slip at $y = \pm h$.
