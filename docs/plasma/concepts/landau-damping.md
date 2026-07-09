# Landau Damping

*Source lecture(s):* [pc368_lec12_landau_damping](../lectures.md)

## Intuition

A wave propagating in a collisionless plasma can decay even without collisions.
Resonant particles—those moving at the wave’s phase velocity—exchange energy with
the wave. If the slope of the equilibrium distribution at $v_\phi$ is negative,
the wave damps; if positive, it is driven. This was Landau’s famous insight in
1946: collisions are not needed for dissipation.

## Formal Definition

**Landau damping** is the collisionless damping of a plasma wave due to resonant
wave–particle interactions. The dielectric function is evaluated on the Landau
contour in the complex $v$-plane.

## Mathematical Formulation

For a one-dimensional electrostatic perturbation, the dielectric function is:

$$\varepsilon(\omega, k) = 1 + \frac{1}{k^2 \lambda_D^2} \Biggl[ 1 + \zeta Z(\zeta) \Biggr] = 0$$

where $\zeta = \frac{\omega/k}{\sqrt{2} v_{te}}$ and $Z(\zeta)$ is the plasma
dispersion function. For small $k\lambda_D$, the damping rate is:

$$\gamma \approx -\frac{\pi}{2} \frac{\omega}{k \lambda_D} \left(\frac{\omega/k}{v_{te}}\right)^2 \exp\!\Bigl[-\Bigl(\frac{\omega/k}{\sqrt{2} v_{te}}\Bigr)^2\Bigr]$$

provided $\partial f_0/\partial v < 0$ at $v_\phi = \omega/k$.

## Derivation

1. Laplace transform the Vlasov equation: assume $\propto e^{-i\omega t}$ with
   $\operatorname{Im}(\omega) > 0$ for causality.
2. The velocity integral of the perturbed distribution picks up contributions
   from the pole at $\omega - kv = 0$.
3. To avoid the pole on the real axis, deform the integration contour below the
   pole (Landau contour).
4. The integral gives the $Z(\zeta)$ function.
5. The imaginary part yields the physical damping/growth rate.

## Worked Example

> A Langmuir wave with $k\lambda_D = 0.2$ propagates through a Maxwellian plasma.
> Estimate the Landau damping rate.
> Using the weak-damping formula: $\zeta = \omega/(k\sqrt{2}v_{te}) \approx 1$. $Z(\zeta) \approx -\pi^{1/2} + i\sqrt{\pi}$.
> The imaginary part gives $\gamma/\omega \sim -(\pi/2)(k\lambda_D)^2 \approx -0.06$.
> The wave loses ~6% of its energy per oscillation period.

## Common Mistakes

- **Landau damping needs collisions.** No—it is purely collisionless, arising from
  resonant trapping in $v$-space.
- **Damping means energy is lost to heat.** It is transferred to resonant
  particles, not randomized by collisions.
- **All Langmuir waves are damped.** Only if $\partial f_0/\partial v < 0$ at
  $v_\phi$; otherwise the wave is driven.

## Related Concepts

- [Vlasov Equation](../equations/vlasov-equation.md)
- [Plasma Waves](plasma-waves.md)
- [Streaming Instability](streaming-instability.md)

## Quiz Questions

1. **Conceptual:** Explain why a perturbation with equal numbers of resonant
   particles on either side of $v_\phi$ sees no net Landau damping.
2. **Computational:** For a bump-on-tail distribution with a local maximum,
   explain why Landau predicts growth.
3. **MCQ:** Landau damping is fundamentally:
   - A) A collisional effect
   - B) A resonant wave–particle effect
   - C) A numerical artifact
   - D) Caused by resistivity

## Further Reading

- E. Centroni & P. P., *Landau’s 1946 Paper Revisited*.
