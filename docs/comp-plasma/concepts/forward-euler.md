# Forward Euler Method

## Intuition

The most obvious idea in numerical analysis: stand at $(t_n, y_n)$, measure the slope,
walk straight along the tangent for time $\Delta t$. Repeat. It's the numerical method
you'd invent by accident — and its failure mode on plasma orbits (slow, systematic
energy gain) motivates everything that follows.

## The scheme

$$\boxed{\,y_{n+1} = y_n + \Delta t\, f(t_n, y_n)\,}$$

```python
def Euler_step(f, t, y, h):
    return y + h * f(t, y)
```

## Properties

- **Order 1:** local truncation error $\mathcal{O}(\Delta t^2)$, global error
  $\mathcal{O}(\Delta t)$ — halving the step halves the error.
- **Cost:** one evaluation of $f$ per step (cheapest possible).
- **Stability:** conditional; for oscillatory systems, effectively *never* stable —
  the amplitude grows every step.

## Why it spirals outward on orbits

For circular gyration, the exact motion curves; Euler walks along the *tangent*, which
always lands slightly *outside* the circle. Each step the radius (and kinetic energy)
grows by a factor $\sqrt{1 + (\omega\Delta t)^2}$. On the
[cross-field benchmark](../equations/cyclotron-motion.md), the trajectory visibly
spirals outward — see the [live comparison widget](../simulations/integrator-arena.md).

Backward Euler makes the mirror-image error (lands inside, spirals inward); their
average ([Heun's method](runge-kutta-methods.md)) cancels the leading error and jumps
to order 2 — the first hint that clever slope sampling pays.

## When to use it

Prototyping, non-oscillatory dissipative problems, and as the "kick" building block
inside better schemes ([kick–drift–kick leapfrog](leapfrog-method.md)). Never for
long-time orbital or wave problems.

## Common mistakes

- **"It's converging, so it's fine."** It converges as $\Delta t \to 0$ at fixed $T$,
  but at fixed $\Delta t$ the energy error grows *exponentially in time* for orbits.
- **Blaming the physics.** An outward-spiraling particle in a uniform magnetic field
  is a numerical artifact — magnetic forces do no work.

## Related concepts

- [ODE integration](ode-integration.md) — framework
- [Backward Euler](backward-euler.md) — the implicit mirror image
- [Leapfrog](leapfrog-method.md) — the fix for orbits
- [Convergence and error](convergence-and-error.md) — measuring the order

## Knowledge graph position

**Prerequisites:** [ODE integration](ode-integration.md).
**Leads to:** [Backward Euler](backward-euler.md), [Runge–Kutta](runge-kutta-methods.md).

## Quiz

**Q1 (computational).** For $\dot y = -y$, $y_0 = 1$, $\Delta t = 0.1$: what is $y$
after two Euler steps, and the exact answer?

??? success "Answer"
    $y_1 = 1 - 0.1 = 0.9$, $y_2 = 0.9(1 - 0.1) = 0.81$. Exact: $e^{-0.2} = 0.8187$.
    Error ≈ 0.009 — first-order behavior.

**Q2 (conceptual).** For $\dot y = -\lambda y$ ($\lambda > 0$), forward Euler gives
$y_{n+1} = (1 - \lambda\Delta t)y_n$. For which $\Delta t$ is it stable?

??? success "Answer"
    Need $|1 - \lambda\Delta t| \leq 1 \Rightarrow \Delta t \leq 2/\lambda$. Beyond
    that the iterates oscillate with growing amplitude — numerical explosion of a
    decaying solution.

**Q3 (MCQ).** On a charged-particle gyration problem, forward Euler:

- (a) conserves energy  (b) loses energy  (c) gains energy  (d) preserves the orbit radius

??? success "Answer"
    **(c).** Tangent steps always exit the circle outward: systematic energy gain.
