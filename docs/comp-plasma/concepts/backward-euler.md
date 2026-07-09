# Backward Euler Method

## Intuition

Forward Euler uses the slope where you *are*; backward Euler uses the slope where you
*will be*:

$$\boxed{\,y_{n+1} = y_n + \Delta t\, f(t_{n+1}, y_{n+1})\,}$$

The unknown appears on both sides — an **implicit** method. That single change flips
every property: unconditional stability, but energy *dissipation* on orbits.

## Solving the implicit equation

For linear $f$ you can solve algebraically. In practice the course uses a
**predictor–corrector** approximation:

$$\tilde y_{n+1} = y_n + \Delta t\, f(t_n, y_n) \quad\text{(predict with forward Euler)}$$

$$y_{n+1} = y_n + \Delta t\, f(t_{n+1}, \tilde y_{n+1}) \quad\text{(correct)}$$

```python
# predictor-corrector backward Euler
state += state_dot(state + state_dot(state)*dt) * dt
```

## Properties

- **Order 1** — same accuracy class as forward Euler.
- **A-stable:** for decaying problems, stable at *any* $\Delta t$ — the tool of choice
  for stiff systems.
- **On orbits:** lands slightly *inside* the circle each step → spirals inward,
  **losing** energy — overdamped, the mirror image of
  [forward Euler](forward-euler.md)'s gain.

## The averaging insight

Forward gains what backward loses, to leading order. Their average is **Heun's
method** (trapezoidal rule):

```python
def Heun_step(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)
    return y + 0.5 * h * (k1 + k2)
```

— second-order accurate, with the leading energy errors cancelled. This
"sample-and-average" idea, pushed further, becomes the whole
[Runge–Kutta family](runge-kutta-methods.md).

## Common mistakes

- **Thinking stability = accuracy.** Backward Euler never blows up — it serenely
  damps your plasma to zero. A stable *wrong* answer is still wrong.
- **Forgetting the implicit solve.** The predictor–corrector shortcut is an
  approximation to true backward Euler; for stiff problems you may need a real
  (Newton) solve.

## Related concepts

- [Forward Euler](forward-euler.md) — the explicit twin
- [Leapfrog](leapfrog-method.md) — implicit for the Lorentz force, yet solvable in closed form
- [ODE integration](ode-integration.md) — explicit vs implicit trade-offs

## Knowledge graph position

**Prerequisites:** [Forward Euler](forward-euler.md).
**Leads to:** [Leapfrog](leapfrog-method.md), [Runge–Kutta](runge-kutta-methods.md).

## Quiz

**Q1 (computational).** For $\dot y = -\lambda y$, backward Euler gives
$y_{n+1} = y_n/(1 + \lambda\Delta t)$. Is this stable for large $\Delta t$?

??? success "Answer"
    Yes: $|1/(1+\lambda\Delta t)| < 1$ for every $\Delta t > 0$ — unconditional
    (A-) stability. Compare forward Euler's $\Delta t \leq 2/\lambda$ limit.

**Q2 (conceptual).** Why does averaging the forward and backward Euler steps raise the
order from 1 to 2?

??? success "Answer"
    Their leading error terms are equal and opposite ($\pm\frac{\Delta t^2}{2}y''$):
    the average is the trapezoidal rule, whose error starts at $\mathcal{O}(\Delta t^3)$
    per step — second order globally.

**Q3 (MCQ).** On the gyration benchmark, backward Euler produces a trajectory that:

- (a) spirals outward  (b) spirals inward  (c) stays exactly circular  (d) drifts linearly

??? success "Answer"
    **(b).** Numerical dissipation: the chord to the future point cuts inside the
    circle.
