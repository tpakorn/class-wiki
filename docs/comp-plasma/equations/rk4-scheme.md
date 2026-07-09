# RK4 (and RK3) Schemes

## Equations

**RK4** — four slope samples, Simpson-weighted:

$$k_1 = h f(t_n, y_n) \qquad
k_2 = h f(t_n + \tfrac h2, y_n + \tfrac{k_1}2) \qquad
k_3 = h f(t_n + \tfrac h2, y_n + \tfrac{k_2}2) \qquad
k_4 = h f(t_n + h, y_n + k_3)$$

$$\boxed{\,y_{n+1} = y_n + \frac{k_1 + 2k_2 + 2k_3 + k_4}{6}\,}$$

**RK3** — three samples:

$$k_1 = f(t_n, y_n), \quad
k_2 = f(t_n + \tfrac h2, y_n + \tfrac h2 k_1), \quad
k_3 = f(t_n + h, y_n + h(2k_2 - k_1))$$

$$\boxed{\,y_{n+1} = y_n + \frac{h}{6}(k_1 + 4k_2 + k_3)\,}$$

## Physical meaning

Numerical quadrature applied to slopes: probe the derivative at the start, middle
(twice), and end of the step, then average with Simpson-like weights so the Taylor
errors cancel through 4th (3rd) order. See the
[Runge–Kutta concept page](../concepts/runge-kutta-methods.md) for the family logic.

## Variables

$h = \Delta t$ — step size · $k_i$ — stage slopes (note RK4's $k_i$ include the $h$
factor as written; RK3's do not — follow one convention in code!).

## Properties

| | RK3 | RK4 |
|---|---|---|
| Global error | $\mathcal{O}(h^3)$ | $\mathcal{O}(h^4)$ |
| Evaluations/step | 3 | 4 |
| Halving $h$ divides error by | 8 | 16 |
| Symplectic? | no | no |

## Applications & limitations

The default for smooth, non-Hamiltonian ODEs and moderate horizons: benchmark
trajectories, [Rutherford scattering](../examples/rutherford-scattering.md), field-line
tracing (also the streamline tracer in the
[fluids potential-flow widget](../../fluids/simulations/potential-flow-builder.md)).
For long-time orbital dynamics, its non-symplectic energy drift loses to
[leapfrog](leapfrog-update.md); for stiff systems, explicit RK stability limits bite —
use implicit methods.

## Related equations

- [Leapfrog update](leapfrog-update.md) — conservation-first alternative
- [CFL condition](cfl-condition.md) — the analogous stability constraint for PDEs

## Quiz

**Q1 (computational).** One RK4 step for $\dot y = y$, $y_0 = 1$, $h = 1$: compute
$y_1$ and compare with $e = 2.71828$.

??? success "Answer"
    $k_1 = 1$, $k_2 = 1.5$, $k_3 = 1.75$, $k_4 = 2.75$;
    $y_1 = 1 + (1 + 3 + 3.5 + 2.75)/6 = 1 + 10.25/6 = 2.7083$. Error 0.01 with a
    *huge* step — that's 4th order for you.

**Q2 (MCQ).** RK4's four stages per step mean that at equal *cost*, comparing with
forward Euler at step $h/4$, RK4's error advantage is roughly a factor of:

- (a) 4  (b) $h$  (c) $h^{-3}/64$... hard to say without $h$  (d) none

??? success "Answer"
    **(c)** — the honest answer: Euler at $h/4$ has error $\mathcal{O}(h/4)$, RK4 has
    $\mathcal{O}(h^4)$; the ratio $\sim h^3/4^{-1}$ depends on $h$, overwhelmingly
    favoring RK4 once $h$ is small. Order comparisons must be made at stated cost and
    step size.
