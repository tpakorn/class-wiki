# Leapfrog Method

## Intuition

Stagger the bookkeeping: keep velocity at *half-integer* times and position at
*integer* times, so each update uses information centered exactly where it's needed.
The scheme "leapfrogs" over itself — and this symmetry buys something no amount of
raw accuracy can: **exact conservation of a discrete energy**, forever. The workhorse
of plasma and N-body simulation.

## The scheme

$$\boxed{\;\frac{y_\text{new} - y_\text{old}}{\Delta t}
= f\!\left(\frac{y_\text{new} + y_\text{old}}{2},\ t\right)\;}$$

with $y_\text{new} = y(t + \Delta t/2)$, $y_\text{old} = y(t - \Delta t/2)$ — a
*centered* difference equated to a *midpoint* evaluation. Implicit in general, but for
the [Lorentz force](../equations/lorentz-force.md) it has a **closed-form solution**
(see the [leapfrog update equation page](../equations/leapfrog-update.md)):

$$\mathbf{v}_\text{new} = \frac{\mathbf{C} + \mathbf{A}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{A}\times\mathbf{C}}{1 + A^2},
\qquad \mathbf{x}_\text{new} = \mathbf{x}_\text{old} + \mathbf{v}_\text{new}\Delta t$$

with $\mathbf{A} = \frac{q\mathbf{B}}{m}\frac{\Delta t}{2}$ and
$\mathbf{C} = \mathbf{v}_\text{old} + \Delta t\left(\frac{q\mathbf{E}}{m} + \mathbf{v}_\text{old}\times\frac{q\mathbf{B}}{m}/2\right)$.
No iteration, no matrix solve — pure algebra. This is the ancestor of the **Boris
pusher** used in every serious [PIC code](pic-method.md).

## Kick–drift–kick form

The equivalent split-step version, standard in
[N-body simulation](n-body-simulation.md):

$$\mathbf{v}_{n+1/2} = \mathbf{v}_n + \tfrac{\Delta t}{2}\mathbf{a}_n \quad\text{(kick)}$$

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \Delta t\,\mathbf{v}_{n+1/2} \quad\text{(drift)}$$

$$\mathbf{v}_{n+1} = \mathbf{v}_{n+1/2} + \tfrac{\Delta t}{2}\mathbf{a}_{n+1} \quad\text{(kick)}$$

## Properties

- **Order 2** — global error $\mathcal{O}(\Delta t^2)$
- **Symplectic** — preserves phase-space volume; energy error stays *bounded*
  (oscillates) instead of drifting, even over millions of steps
- **Time-reversible** — run it backwards and you retrace your path exactly
- **Exact gyration** — for uniform $\mathbf{B}$ the orbit stays perfectly circular
  (the frequency is slightly off, the radius is not)

## Why symplecticity beats order for orbits

[RK4](runge-kutta-methods.md) makes a far smaller error per step — but each step's
error pushes energy the *same way*, accumulating secularly. Leapfrog's errors are
structure-preserving: the numerical trajectory is the *exact* orbit of a slightly
perturbed Hamiltonian, so energy oscillates within a fixed band. For a
three-orbit plot, use RK4; for a million-orbit tokamak or galaxy, use leapfrog.
Watch both live in the [integrator arena](../simulations/integrator-arena.md).

## Common mistakes

- **Mixing time levels.** Velocity lives at half-steps: initializing $v_0$ at $t=0$
  and treating it as $v_{1/2}$ costs you the second order (fix: half-kick to start).
- **Expecting exact energy.** Leapfrog conserves a *discrete* (shadow) energy; the
  physical energy oscillates with amplitude $\mathcal{O}(\Delta t^2)$.
- **Using leapfrog for dissipative systems.** Symplecticity assumes Hamiltonian
  dynamics; with drag, its magic evaporates.

## Related concepts

- [Leapfrog update (closed form)](../equations/leapfrog-update.md)
- [FDTD](fdtd-method.md) — leapfrog applied to Maxwell's equations (E and H staggered)
- [N-body simulation](n-body-simulation.md) · [PIC method](pic-method.md) — its habitats
- [Convergence and error](convergence-and-error.md)

## Knowledge graph position

**Prerequisites:** [Forward](forward-euler.md) & [Backward Euler](backward-euler.md).
**Leads to:** [FDTD](fdtd-method.md), [N-body](n-body-simulation.md), [PIC](pic-method.md).

## Quiz

**Q1 (conceptual).** Why is time-reversibility evidence of good long-time behavior?

??? success "Answer"
    A reversible scheme cannot have systematic dissipation or anti-dissipation — any
    energy gained forward would have to be lost backward, but the scheme is the same
    map. Errors must therefore oscillate rather than drift.

**Q2 (computational).** For the cross-field problem with $\Omega\Delta t = 0.2$, the
leapfrog velocity denominator is $1 + (\Omega\Delta t/2)^2$. By what fraction does the
scheme's effective gyration differ per step?

??? success "Answer"
    $(0.1)^2 = 0.01$ → denominators shift speeds at the 1% level per step, but
    *rotations* preserve $|v|$: the error appears as a ~1% phase (frequency) shift,
    not an energy change.

**Q3 (MCQ).** Which system should *not* be integrated with plain leapfrog?

- (a) a galaxy of stars  (b) a particle in a magnetic mirror
- (c) a damped oscillator  (d) two-stream instability particles

??? success "Answer"
    **(c).** Damping breaks the Hamiltonian structure that leapfrog is built to
    preserve.
