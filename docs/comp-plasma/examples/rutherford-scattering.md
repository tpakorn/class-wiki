# Example · Rutherford Scattering

## Problem statement

Simulate an alpha particle scattering off a gold nucleus and verify the classic
relation between impact parameter $b$ and scattering angle $\theta$:

$$\tan\left(\frac{\theta}{2}\right) = \frac{q_1 q_2}{4\pi\varepsilon_0\,\mu\, b\, v_\infty^2}$$

## Given information

- Coulomb field of the nucleus:
  $\mathbf{E} = \dfrac{q_2}{4\pi\varepsilon_0 r^2}\hat{\mathbf{r}}$ — the first
  *non-uniform* field of the course
- Alpha particle arrives from far away with speed $v_\infty$ and perpendicular offset
  (impact parameter) $b$; $\mu$ = reduced mass

## Solution strategy

1. Write the acceleration $\mathbf{a}(\mathbf{x}) = \frac{q_1}{m}\mathbf{E}(\mathbf{x})$
   as a state-space function.
2. Integrate with [RK4](../equations/rk4-scheme.md) (accuracy matters near closest
   approach; no long-time issues here).
3. Start far upstream ($r \gg b$); run until far downstream; measure
   $\theta = \arctan(v_y/v_x)\big|_\text{out}$.
4. Sweep $b$ over a range and plot $\theta(b)$ against the formula.

## Result

The simulated points fall on the theoretical hyperbola-scattering curve across the
sweep — small $b$ → near-backscatter ($\theta \to 180°$), large $b$ → gentle
deflection. The historic conclusion, re-derived numerically: only a *concentrated*
positive charge (a nucleus) produces large-angle scattering; Thomson's smeared
"pudding" cannot.

## Key takeaways

- The step from uniform to $1/r^2$ fields costs nothing in the code — the field
  function is just swapped ([the whole design of the course solver](../concepts/simulation-driven-plasma-physics.md)).
- Energy conservation is the run's health check: the Coulomb force is conservative,
  so $\frac12\mu v^2 + \frac{q_1q_2}{4\pi\varepsilon_0 r}$ must return to its initial
  value downstream.
- Watch the step size near perihelion: fast force variation is where fixed-step
  integrators bleed accuracy (motivation for adaptive stepping — and for
  [softening](../concepts/n-body-simulation.md) when many bodies are involved).

## Related

[Lorentz force](../equations/lorentz-force.md) ·
[RK4](../equations/rk4-scheme.md) ·
[N-body simulation](../concepts/n-body-simulation.md)
