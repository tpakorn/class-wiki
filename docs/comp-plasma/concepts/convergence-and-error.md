# Convergence & Error Analysis

## Intuition

How do you trust a simulation? You *measure its error scaling*. Run the same problem
with $N$, $2N$, $4N$ steps; if error falls by the factor your method's order promises,
the implementation is correct and you know exactly what resolution buys. A straight
line on a log–log plot is the closest thing numerical analysis has to a signature.

## The procedure

1. Choose a benchmark with a known answer — here, the
   [cross-field cycloid](../examples/cross-field-benchmark.md).
2. Define the error at the final time:
   $\text{Error}(N) = |\mathbf{x}_\text{numerical}(T) - \mathbf{x}_\text{exact}(T)|$
3. Run each method with $N = 10, 20, 50, 100, \dots$ steps.
4. Plot $\log(\text{Error})$ vs $\log(N)$: the slope is $-p$, the method's order.

## Expected results

| Method | Slope | Doubling $N$ divides error by |
|---|---|---|
| [Forward/Backward Euler](forward-euler.md) | −1 | 2 |
| Heun / [Leapfrog](leapfrog-method.md) | −2 | 4 |
| RK3 | −3 | 8 |
| [RK4](runge-kutta-methods.md) | −4 | 16 |

## Reading the plot like a pro

- **Slope shallower than expected** → a bug (often an $\mathcal{O}(\Delta t)$
  inconsistency in initialization — e.g. leapfrog's half-step start).
- **Curve flattening at small $\Delta t$** → floating-point round-off has taken over;
  you've hit the accuracy floor (~$10^{-15}$ relative for float64).
- **Error growing with $N$** → instability, not truncation error; no amount of
  resolution fixes a scheme used outside its stability region.
- **Order ≠ long-time fidelity:** RK4's beautiful slope says nothing about its energy
  *drift* on Hamiltonian systems — see [leapfrog](leapfrog-method.md).

## Local vs global error

Local truncation error (one step): $\mathcal{O}(\Delta t^{p+1})$.
Number of steps to fixed time $T$: $N = T/\Delta t$.
Global error: $N \times \mathcal{O}(\Delta t^{p+1}) = \mathcal{O}(\Delta t^p)$.
The lost power of $\Delta t$ is the price of accumulation.

## Common mistakes

- **Benchmarking against another simulation** instead of an exact solution — you may
  be measuring the *other* code's error.
- **Testing convergence at one $N$.** Order is a *slope*; it needs several points.
- **Comparing methods at equal step count** rather than equal cost (RK4 does 4
  evaluations per step).

## Related concepts

- [ODE integration](ode-integration.md) — the properties framework
- [Cross-field benchmark](../examples/cross-field-benchmark.md) — the exact solution used
- [CFL condition](../equations/cfl-condition.md) — the stability side of the story for PDEs

## Knowledge graph position

**Prerequisites:** the integrator pages.
**Leads to:** trustworthy [field solvers](finite-difference-method.md) and [PIC](pic-method.md) diagnostics.

## Quiz

**Q1 (computational).** A mystery integrator gives errors $8\times10^{-3}$ at
$N = 100$ and $10^{-3}$ at $N = 200$. What's its order?

??? success "Answer"
    Error ratio 8 for a factor 2 in $N$ ⇒ $2^p = 8 \Rightarrow p = 3$. It's RK3-class.

**Q2 (conceptual).** Your leapfrog code shows slope −1 instead of −2. Most likely
cause?

??? success "Answer"
    A first-order inconsistency somewhere — classically, initializing the staggered
    velocity at $t = 0$ instead of $t = \Delta t/2$ (missing initial half-kick), or a
    non-centered force evaluation. One $\mathcal{O}(\Delta t)$ ingredient poisons the
    whole scheme's order.

**Q3 (MCQ).** At very small $\Delta t$, the measured error stops decreasing because:

- (a) the method's order saturates  (b) round-off error dominates
- (c) the exact solution is unknown  (d) Python loops are slow

??? success "Answer"
    **(b).** Truncation error shrinks below the float64 round-off floor; further
    refinement only accumulates more rounding.
