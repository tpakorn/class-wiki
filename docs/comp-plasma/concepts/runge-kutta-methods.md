# Runge–Kutta Methods

## Intuition

One slope sample per step limits you to first order. So sample the slope at *several
cleverly chosen points* inside the step and take a weighted average — each extra,
well-placed sample cancels another term of the Taylor error. That escalation is the
Runge–Kutta family; RK4, with four samples for fourth order, is the classic sweet spot
and the general-purpose workhorse of scientific computing.

## The family

$$y_{n+1} = y_n + \Delta t\sum_{i=1}^{s} b_i k_i,
\qquad k_i = f(\text{strategic point } i)$$

| Method | Evals | Order | Note |
|---|---|---|---|
| RK1 | 1 | 1 | = [forward Euler](forward-euler.md) |
| RK2 (midpoint) / Heun | 2 | 2 | first "free lunch" |
| RK3 | 3 | 3 | good cost/accuracy compromise |
| **RK4** | 4 | 4 | the classic |

## RK4

$$k_1 = h f(t_n, y_n) \qquad
k_2 = h f\!\left(t_n + \tfrac h2,\ y_n + \tfrac{k_1}2\right)$$

$$k_3 = h f\!\left(t_n + \tfrac h2,\ y_n + \tfrac{k_2}2\right) \qquad
k_4 = h f(t_n + h,\ y_n + k_3)$$

$$\boxed{\;y_{n+1} = y_n + \frac{k_1 + 2k_2 + 2k_3 + k_4}{6}\;}$$

Weights $\frac16(1,2,2,1)$ — Simpson's rule in disguise: two midpoint samples count
double.

```python
def RK4_step(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + 0.5*h, y + 0.5*h*k1)
    k3 = f(t + 0.5*h, y + 0.5*h*k2)
    k4 = f(t + h, y + h*k3)
    return y + h*(k1 + 2*k2 + 2*k3 + k4) / 6
```

(RK3 uses $k_3 = f(t+h,\ y + h(2k_2 - k_1))$ and weights $\frac16(1,4,1)$; see
[the equation page](../equations/rk4-scheme.md) for both.)

## Order vs conservation

RK4's global error $\mathcal{O}(\Delta t^4)$ makes it spectacularly accurate over
short-to-medium horizons — on the
[cross-field benchmark](../equations/cyclotron-motion.md) it is visually
indistinguishable from the exact cycloid. But RK methods are **not symplectic**: on
Hamiltonian systems their tiny per-step energy error drifts monotonically. Rule of
thumb: RK4 for accuracy over finite times, [leapfrog](leapfrog-method.md) for fidelity
over long times.

## Common mistakes

- **Halving $h$ when you meant to halve error.** Halving $h$ cuts RK4 error by
  16× — check the [convergence page](convergence-and-error.md) before over-resolving.
- **Counting steps, not evaluations.** RK4 costs 4 evaluations per step; at equal
  *cost*, compare RK4 with step $h$ against Euler with step $h/4$.
- **Reusing $k_1$ across steps incorrectly** — each stage belongs to its own step
  (unless you implement FSAL variants deliberately).

## Related concepts

- [ODE integration](ode-integration.md) — framework
- [Leapfrog](leapfrog-method.md) — the conservation-first alternative
- [Convergence and error](convergence-and-error.md) — verifying the order-4 slope

## Knowledge graph position

**Prerequisites:** [Forward Euler](forward-euler.md), [Backward Euler](backward-euler.md).
**Leads to:** production ODE solving; contrast with [leapfrog](leapfrog-method.md).

## Quiz

**Q1 (computational).** RK4 with $N = 100$ steps gives error $10^{-4}$. Estimate the
error with $N = 200$.

??? success "Answer"
    $\mathcal{O}(\Delta t^4)$: doubling $N$ divides error by $2^4 = 16$ →
    $\approx 6\times10^{-6}$.

**Q2 (conceptual).** Why do the RK4 weights sum to 1 (after the $\frac16$ factor)?

??? success "Answer"
    Consistency: for $f = $ const the step must reduce to $y + h f$ exactly;
    $\frac{1+2+2+1}{6} = 1$ guarantees it.

**Q3 (MCQ).** At equal computational cost, which usually wins on a *smooth,
non-Hamiltonian* problem?

- (a) forward Euler  (b) Heun  (c) RK4  (d) they tie

??? success "Answer"
    **(c).** Higher order wins whenever the solution is smooth: the error constant is
    similar but the power of $\Delta t$ is far better.
