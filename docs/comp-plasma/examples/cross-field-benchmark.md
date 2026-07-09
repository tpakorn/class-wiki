# Example · The Cross-Field Cycloid Benchmark

## Problem statement

A charged particle starts at rest at the origin in crossed uniform fields
$\mathbf{E} = E\hat\jmath$, $\mathbf{B} = B\hat k$ (normalized $q = m = E = B = 1$).
Integrate its motion for 7 gyration periods with forward Euler, backward Euler,
Heun, and leapfrog, and compare each against the exact solution.

## Given information

- Exact solution ([cyclotron motion](../equations/cyclotron-motion.md)):
  $x(t) = R(\omega t - \sin\omega t)$, $y(t) = R(1 - \cos\omega t)$
- $\omega = qB/m = 1$, $R = mE/qB^2 = 1$, $T_\text{max} = 14\pi$, $N = 1000$ steps

## Solution strategy

Cast the [Lorentz force](../equations/lorentz-force.md) as a 4-component state system
$\mathbf{y} = (x, y, v_x, v_y)$ with

$$\dot{\mathbf{y}} = \left(v_x,\ v_y,\ \tfrac{q}{m}(E_x - v_y B),\ \tfrac{q}{m}(E_y + v_x B)\right)$$

and march each method with the same $\Delta t = T_\text{max}/N$.

## Results

| Method | Trajectory | Energy behavior |
|---|---|---|
| [Forward Euler](../concepts/forward-euler.md) | spirals **outward** off the cycloid | grows every step |
| [Backward Euler](../concepts/backward-euler.md) | spirals **inward** | decays every step |
| Heun (average) | hugs the cycloid closely | leading errors cancel |
| [Leapfrog](../concepts/leapfrog-method.md) | on the cycloid; tiny phase lag | bounded oscillation |
| [RK4](../concepts/runge-kutta-methods.md) | indistinguishable from exact | slow secular drift (invisible here) |

## Convergence measurement

Final-position error vs step count $N$ on a log–log plot gives slopes −1 (Euler),
−2 (Heun/leapfrog), −3 (RK3), −4 (RK4) — the definitive check that each
implementation matches its theoretical order. Details and diagnosis heuristics:
[convergence & error](../concepts/convergence-and-error.md).

## Key takeaways

- An exact solution converts vague "looks right" into measured error — always
  benchmark before trusting a solver on unknown problems.
- First-order methods don't just err — they err *systematically* (energy gain/loss),
  which is fatal for oscillatory physics.
- This exact configuration is also the physics of the
  [E×B drift](../equations/exb-drift.md): benchmark and drift theory in one problem.

## Try it live

The [integrator arena widget](../simulations/integrator-arena.md) runs this exact
benchmark in your browser.
