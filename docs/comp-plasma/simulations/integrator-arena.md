# Integrator Arena

## Learning goal

*See* the defining pathologies of each
[time integrator](../concepts/ode-integration.md) on the
[cross-field benchmark](../examples/cross-field-benchmark.md):
[forward Euler](../concepts/forward-euler.md) spiraling out,
[backward Euler](../concepts/backward-euler.md) spiraling in,
[leapfrog](../concepts/leapfrog-method.md) locked on the cycloid, and
[RK4](../concepts/runge-kutta-methods.md) near-exact.

<iframe src="../../assets/integrator-arena.html" width="100%" height="620"
        style="border:none;" title="Integrator arena"></iframe>

## Things to try

1. **Slide steps-per-period down to ~10.** Watch Euler's spiral blow up while
   leapfrog merely lags in phase — stability vs accuracy, dissociated before your
   eyes.
2. **Increase the number of periods.** First-order errors *compound*; the gap between
   methods widens with simulation length.
3. **Turn on RK4 at very coarse steps.** Even 4th-order accuracy eventually loses the
   phase — high order is not a substitute for resolving the gyration.
4. **Compare backward Euler and forward Euler at the same settings** — mirror-image
   energy errors, exactly as the [averaging argument](../concepts/backward-euler.md)
   predicts.

## Related

[ODE integration](../concepts/ode-integration.md) ·
[Convergence & error](../concepts/convergence-and-error.md) ·
[Leapfrog update equations](../equations/leapfrog-update.md)
