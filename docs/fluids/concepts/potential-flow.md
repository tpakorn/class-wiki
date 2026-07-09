# Potential Flow

## Intuition

Suppose a flow has no "spin" anywhere — every little fluid blob translates and
stretches but never rotates. Then the whole velocity field collapses into a single
scalar function $\phi$, like a landscape whose slopes *are* the velocities. Add
incompressibility and $\phi$ obeys the friendliest PDE in physics — Laplace's equation —
whose solutions superpose. Suddenly you can *build* flows like Lego: uniform stream +
doublet = flow past a cylinder.

## Formal definition

A flow is a **potential flow** if it is irrotational:

$$\boldsymbol{\omega} = \nabla\times\mathbf{v} = 0
\quad\Longleftrightarrow\quad
\mathbf{v} = \nabla\phi$$

($\nabla\times\nabla\phi \equiv 0$ guarantees consistency). If also incompressible
([continuity](../equations/continuity-equation.md): $\nabla\cdot\mathbf{v} = 0$), then

$$\boxed{\,\nabla^2\phi = 0\,}$$

— [Laplace's equation](../equations/laplace-equation.md), shared with electrostatics
and gravity.

## The stream function

In 2-D, define $\psi$ by

$$u = \frac{\partial\psi}{\partial y}, \qquad v = -\frac{\partial\psi}{\partial x}$$

which satisfies continuity *identically*; irrotationality then gives $\nabla^2\psi = 0$
too. Contours of $\psi$ **are streamlines**, and the flow rate between two streamlines
equals $\Delta\psi$. $\phi$-lines and $\psi$-lines intersect at right angles.

## Elementary solutions (the Lego bricks)

| Flow | Potential $\phi$ |
|---|---|
| Uniform stream | $Ux + Vy$ |
| Source / sink (strength $Q$) | $\frac{Q}{2\pi}\ln r$ |
| Vortex (circulation $\Gamma$) | $-\frac{\Gamma}{2\pi}\theta$ |
| Doublet (strength $K$) | $\frac{K}{r}\cos\theta$ |

Because Laplace's equation is linear, **superposition** works:
*uniform + source* = flow past a blunt nose (Rankine half-body);
*uniform + doublet* = flow past a circular cylinder;
add a *vortex* = lifting cylinder (and, via
[conformal mapping](conformal-mapping-and-images.md), an airfoil).

With the velocity in hand, pressure follows from
[Bernoulli](bernoulli-principle.md) — which in irrotational flow holds with a *single
global constant*.

## Method of images

To satisfy the no-penetration condition at a solid wall, add fictitious mirror
singularities. A source $Q$ at $(a, 0)$ near a wall along the $x$-axis pairs with an
image source at $(-a, 0)$:

$$\phi = \frac{Q}{2\pi}\ln\sqrt{(x-a)^2 + y^2} + \frac{Q}{2\pi}\ln\sqrt{(x+a)^2 + y^2}$$

By symmetry the normal velocity on the wall vanishes — boundary condition satisfied
without solving anything. The same trick powers electrostatics and
[computational plasma boundary handling](../../comp-plasma/index.md).

## Limits of the theory

Potential flow ignores [viscosity](viscosity.md) entirely, so it predicts **zero
drag** for a cylinder in steady flow (d'Alembert's paradox) and misses boundary
layers, separation and [turbulence](turbulence.md). It remains outstandingly useful
*outside* boundary layers, for lift (with circulation), for waves, and as the skeleton
that viscous corrections dress up.

## Common mistakes

- **Assuming every incompressible flow has a $\phi$.** Only *irrotational* ones do.
  A shear flow $u(y)$ has vorticity and no potential.
- **Expecting drag predictions.** Potential flow gives pressure distributions and lift
  (with imposed circulation) but no viscous drag.
- **Confusing $\phi$ and $\psi$ roles:** $\phi$ exists in 3-D; the scalar $\psi$ as
  defined here is a 2-D device.

## Related concepts

- [Laplace's equation](../equations/laplace-equation.md) — the governing PDE
- [Conformal mapping & method of images](conformal-mapping-and-images.md) — solution technology
- [Bernoulli's principle](bernoulli-principle.md) — pressure recovery
- [Kelvin–Helmholtz instability](kelvin-helmholtz-instability.md) — perturbed potential flow at an interface

## Knowledge graph position

**Prerequisites:** [Continuity](../equations/continuity-equation.md), [Euler's equation](../equations/euler-equation.md), [Eulerian description](eulerian-vs-lagrangian.md).
**Leads to:** [Conformal mapping](conformal-mapping-and-images.md), [interface instabilities](kelvin-helmholtz-instability.md).

## Quiz

**Q1 (computational).** For the potential $\phi = Ux + \frac{Q}{2\pi}\ln r$, find the
stagnation point on the $x$-axis.

??? success "Answer"
    $u = U + \frac{Q}{2\pi x} = 0 \Rightarrow x = -\frac{Q}{2\pi U}$ — upstream of the
    source: the incoming stream is exactly cancelled there (Rankine half-body nose).

**Q2 (conceptual).** Why can solutions of potential flow be superposed, while solutions
of the full Navier–Stokes equation cannot?

??? success "Answer"
    Laplace's equation is linear; sums of solutions are solutions. Navier–Stokes
    contains the quadratic convective term $(\mathbf{v}\cdot\nabla)\mathbf{v}$, so the
    sum of two solutions generates cross terms that are not accounted for.

**Q3 (multiple choice).** Streamlines and equipotential lines in 2-D potential flow:

- (a) coincide  (b) are parallel  (c) are orthogonal  (d) never intersect

??? success "Answer"
    **(c).** $\nabla\phi \parallel \mathbf{v}$ and $\nabla\psi \perp \mathbf{v}$, so
    the two families cross at right angles (a consequence of the Cauchy–Riemann
    equations).
