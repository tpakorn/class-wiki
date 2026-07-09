# Material Derivative

## Intuition

Stand on a riverbank with a thermometer: you record how the water temperature at *your
spot* changes. Now jump in and drift: you feel something different — the water around
you changes both because the river is cooling overall **and** because the current
carries you into warmer or colder patches. The material derivative $D/Dt$ is the rate
of change *experienced by a moving fluid particle*: local change plus the change you
"run into".

## Formal definition

For any field $f(\mathbf{x}, t)$ (scalar or vector):

$$\boxed{\,\frac{Df}{Dt} = \frac{\partial f}{\partial t} + (\mathbf{v}\cdot\nabla) f\,}$$

- $\partial f/\partial t$ — **local** (unsteady) change at a fixed point
- $(\mathbf{v}\cdot\nabla)f$ — **convective** change from being carried through spatial
  gradients

Applied to velocity itself, it gives the acceleration of a fluid particle:

$$\frac{D\mathbf{v}}{Dt} = \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v}\cdot\nabla)\mathbf{v}$$

— the left-hand side of both [Euler's equation](../equations/euler-equation.md) and
[Navier–Stokes](../equations/navier-stokes-equation.md). The convective term is
*nonlinear* in $\mathbf{v}$, and that single fact is the root of almost all difficulty
in fluid mechanics, from [instability](hydrodynamic-stability.md) to
[turbulence](turbulence.md).

## Worked example: acceleration in a converging nozzle

Incompressible, inviscid fluid enters a converging nozzle with speed $u$ through area
$A$ and leaves through area $\alpha < A$ over a length $\Delta x$. Find the axial
acceleration.

Steady flow ⇒ $\partial u/\partial t = 0$; on the axis only $u\,\partial u/\partial x$
survives:

$$a_x = u_\text{avg}\frac{\Delta u}{\Delta x}, \qquad
u_\text{avg} = \frac{u + v}{2}, \quad v = \frac{uA}{\alpha}\ \text{(continuity)}$$

$$\boxed{\,a_x = \frac{u^2}{2\Delta x}\left[\left(\frac{A}{\alpha}\right)^2 - 1\right]}$$

Nothing about the flow changes in time, yet particles accelerate hard — a pure
convective effect. (The lecture notes verify the same result with a direct $\Delta
u/\Delta t$ argument.)

## Physical interpretation

$D/Dt$ is the Lagrangian rate of change written in Eulerian variables — the
infinitesimal version of the
[Reynolds transport theorem](reynolds-transport-theorem.md). It lets us apply Newton's
laws (which follow *matter*) while computing with fields (which live on a grid).

## Common mistakes

- **Dropping the convective term in steady flow.** Steady means
  $\partial/\partial t = 0$, **not** $D/Dt = 0$.
- **Treating $(\mathbf{v}\cdot\nabla)\mathbf{v}$ as $\mathbf{v}(\nabla\cdot\mathbf{v})$.**
  The operator $\mathbf{v}\cdot\nabla = u\partial_x + v\partial_y + w\partial_z$ acts
  component-wise on the vector that follows.
- **Sign/order confusion:** it is $\mathbf{v}\cdot\nabla f$, the velocity dotted with
  the gradient — "how fast you move through the field's slope".

## Related concepts

- [Eulerian vs Lagrangian](eulerian-vs-lagrangian.md) — the two viewpoints it connects
- [Reynolds transport theorem](reynolds-transport-theorem.md) — the finite-volume version
- [Euler's equation](../equations/euler-equation.md), [Navier–Stokes equation](../equations/navier-stokes-equation.md) — where it appears

## Knowledge graph position

**Prerequisites:** [Eulerian vs Lagrangian](eulerian-vs-lagrangian.md).
**Leads to:** [Reynolds transport theorem](reynolds-transport-theorem.md), [Euler's equation](../equations/euler-equation.md).

## Quiz

**Q1 (computational).** In the 1-D steady field $u(x) = u_0(1 + x/L)$, what is the
acceleration of a particle at $x = L$?

??? success "Answer"
    $a = u\,\partial u/\partial x = u_0(1 + 1)\cdot(u_0/L) = 2u_0^2/L$.

**Q2 (conceptual).** Can $Df/Dt = 0$ while $\partial f/\partial t \neq 0$? Give an
example.

??? success "Answer"
    Yes — a "frozen" pattern advected by the flow: $f(x,t) = F(x - ut)$ satisfies
    $\partial f/\partial t = -u\,\partial f/\partial x \neq 0$ but $Df/Dt = 0$.
    Particles carry constant $f$; the field at a fixed point still changes as the
    pattern sweeps by.

**Q3 (multiple choice).** The nonlinearity of the Navier–Stokes equation comes from:

- (a) the viscous term $\mu\nabla^2\mathbf{v}$
- (b) the pressure gradient
- (c) the convective term $(\mathbf{v}\cdot\nabla)\mathbf{v}$
- (d) gravity

??? success "Answer"
    **(c).** It is quadratic in velocity; all other terms are linear in $\mathbf{v}$ or
    $P$.
