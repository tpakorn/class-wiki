# Time Integration of ODEs

## Intuition

Physics hands you a rule for the *slope* — $d\mathbf{y}/dt = f(\mathbf{y}, t)$ — and an
initial state. A time integrator is a recipe for walking forward in small steps
$\Delta t$, reconstructing the trajectory from slopes alone:

$$\mathbf{y}_0 \longrightarrow \mathbf{y}_1 \longrightarrow \mathbf{y}_2 \longrightarrow \cdots$$

Every method in this course — from bouncing balls to
[PIC plasmas](pic-method.md) — is a variation on how cleverly you sample the slope
within each step.

## The four properties that matter

| Property | Question it answers |
|---|---|
| **Accuracy (order $p$)** | How fast does error shrink as $\Delta t \to 0$? (global error $\mathcal{O}(\Delta t^p)$) |
| **Stability** | Does the numerical solution stay bounded when the true one does? |
| **Cost** | How many evaluations of $f$ per step? |
| **Conservation** | Does the scheme respect energy/momentum/phase-space structure? |

No method wins all four — choosing an integrator is engineering, and the
right choice depends on the problem. For oscillatory plasma orbits, *conservation*
(symplecticity) turns out to matter more than raw order — the moral of
[Chapter 2](leapfrog-method.md).

## Explicit vs implicit

**Explicit:** the new state comes directly from known quantities —
$y_{n+1} = y_n + \Delta t\, f(t_n, y_n)$. Cheap per step, easy to code, but may demand
tiny $\Delta t$ for stability.

**Implicit:** the unknown appears on both sides —
$y_{n+1} = y_n + \Delta t\, f(t_{n+1}, y_{n+1})$. Requires solving an equation each
step, but is far more stable (essential for *stiff* systems with fast decaying modes).

## The benchmark problem

All methods are tested on the **cross-field cycloid**: a charged particle in
$\mathbf{E} = E\hat{\jmath}$, $\mathbf{B} = B\hat{k}$, whose exact solution is known
([cyclotron motion page](../equations/cyclotron-motion.md)):

$$x(t) = R(\omega t - \sin\omega t), \qquad y(t) = R(1 - \cos\omega t)$$

with $\omega = qB/m$ and $R = mE/qB^2$. A known answer turns "looks right" into
*measured error* — see [convergence and error](convergence-and-error.md).

## State-vector form

Any second-order equation becomes first-order by stacking position and velocity:
$\mathbf{z} = (\mathbf{x}, \mathbf{v}) \in \mathbb{R}^6$,

$$\frac{d\mathbf{z}}{dt} = \mathbf{F}(\mathbf{z}, t)
= \left(\mathbf{v},\ \frac{q}{m}(\mathbf{E} + \mathbf{v}\times\mathbf{B})\right)$$

One interface, `step(f, t, y, h)`, serves every method — the design of `methods.py`.

## The method menu

| Method | Order | Evals/step | Character |
|---|---|---|---|
| [Forward Euler](forward-euler.md) | 1 | 1 | explicit; gains energy on orbits |
| [Backward Euler](backward-euler.md) | 1 | (implicit) | stable; loses energy |
| Heun / RK2 | 2 | 2 | averaged Euler; much better |
| [Leapfrog](leapfrog-method.md) | 2 | 1 | symplectic; no energy drift |
| [RK3 / RK4](runge-kutta-methods.md) | 3 / 4 | 3 / 4 | high accuracy workhorses |

## Common mistakes

- **Judging a method by one step.** Local error is $\mathcal{O}(\Delta t^{p+1})$;
  what you feel after $N \sim 1/\Delta t$ steps is the global $\mathcal{O}(\Delta t^p)$.
- **Assuming smaller $\Delta t$ always fixes instability.** For Forward Euler on
  orbits, energy grows at *every* $\Delta t$ — slower, but always.
- **Using high-order RK for million-step orbit problems.** RK4's tiny per-step error
  still *drifts* secularly; [symplectic methods](leapfrog-method.md) don't.

## Related concepts

- [Forward Euler](forward-euler.md) · [Backward Euler](backward-euler.md) ·
  [Leapfrog](leapfrog-method.md) · [Runge–Kutta](runge-kutta-methods.md)
- [Convergence and error](convergence-and-error.md)
- [FDTD](fdtd-method.md) — the same leapfrog idea applied to fields

## Knowledge graph position

**Prerequisites:** [Why simulate plasmas?](simulation-driven-plasma-physics.md), calculus.
**Leads to:** all integrator pages, then [single-particle motion](guiding-center-drifts.md) and [PIC](pic-method.md).

## Quiz

**Q1 (conceptual).** Why is "order" defined by the *global* error rather than the
per-step error?

??? success "Answer"
    You take $N = T/\Delta t$ steps; local errors $\mathcal{O}(\Delta t^{p+1})$
    accumulate over $N$ steps into $\mathcal{O}(\Delta t^p)$ — that's the error you
    actually observe at fixed final time.

**Q2 (MCQ).** A stiff system (fast-decaying transients + slow dynamics of interest)
calls for:

- (a) forward Euler with large steps  (b) an implicit method  (c) RK4  (d) any method with tiny steps

??? success "Answer"
    **(b).** Implicit methods stay stable at step sizes set by the *slow* physics;
    explicit ones are stability-limited by the fastest mode even after it has decayed.
