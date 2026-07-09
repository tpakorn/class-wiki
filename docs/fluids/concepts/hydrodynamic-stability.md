# Hydrodynamic Stability

## Intuition

A pencil balanced on its tip satisfies the equilibrium equations perfectly — and falls
anyway. Equilibrium is cheap; *stability* is the real question. Fluid mechanics asks it
constantly: smooth laminar solutions of [Navier–Stokes](../equations/navier-stokes-equation.md)
exist at every [Reynolds number](reynolds-number.md), but above some threshold the
tiniest perturbation grows exponentially and the flow tips over into something else —
waves, vortices, eventually [turbulence](turbulence.md).

## The perturbation recipe

1. **Find an equilibrium** $\bar{\mathbf{u}}(\mathbf{x}), \bar{P}(\mathbf{x})$
   (e.g. $\sum F = 0$, steady laminar profile)
2. **Perturb:** $\mathbf{u} = \bar{\mathbf{u}} + \delta\mathbf{u}'$,
   $p = \bar{p} + \delta p'$
3. **Expand** the governing equations in powers of $\delta$
4. **Linearize** — keep $O(\delta)$, drop $O(\delta^2)$
5. **Normal modes:** $\mathbf{u}' \sim \hat{\mathbf{u}}(y)\, e^{ikx + st}$
6. **Solve the eigenvalue problem** for the growth rate $s(k)$:
   - $\operatorname{Re}(s) < 0$ for all $k$ → **stable**
   - $\operatorname{Re}(s) > 0$ for some $k$ → **unstable**; the fastest-growing mode
     is what you see in experiments

The linearization decouples wavenumbers: each $k$ evolves independently, so
instability is diagnosed one Fourier mode at a time.

## Mechanical archetype

$$m\ddot{x} = \pm kx \qquad
\begin{cases}
-k\ (\text{valley}) & x \sim e^{\pm i\omega t}\ \text{— oscillates, stable} \\
+k\ (\text{hill}) & x \sim e^{\pm\sqrt{k/m}\,t}\ \text{— grows, unstable}
\end{cases}$$

Every fluid instability is this, dressed in field theory: the sign of the "restoring
force" for each mode determines its fate. (The inverted pendulum is the mechanical
soul of [Rayleigh–Taylor](rayleigh-taylor-instability.md).)

## Worked example: a toy reaction–diffusion model

$$\partial_t f = f - \frac{f^2}{\lambda} + \frac{1}{\lambda}\partial_y^2 f,
\qquad f(0) = f(1) = 0$$

Equilibrium: $f = 0$. Linearize ($f = 0 + \delta f'$):
$\partial_t f' = f' + \frac{1}{\lambda}\partial_y^2 f'$. Normal modes respecting the
boundary conditions: $f' = C\sin(n\pi y)\,e^{s t}$, giving

$$s_n = 1 - \frac{n^2\pi^2}{\lambda}$$

- Mode $n$ unstable iff $\lambda > n^2\pi^2$ — a clean **threshold** in the control
  parameter.
- For $\lambda = 500$: $n = 1$–$7$ unstable ($49\pi^2 \approx 483 < 500$), $n = 8$
  stable ($64\pi^2 \approx 632 > 500$).
- The **most unstable mode** ($n = 1$) grows fastest and dominates what you observe.

This little model rehearses every step used on the real linearized Navier–Stokes
system — including the emergence of thresholds and pattern selection.

## Linearized Navier–Stokes

For a unidirectional base flow $\bar{\mathbf{u}} = (\bar{u}_x(y), 0, 0)$, the
$O(\delta)$ momentum equation is

$$\rho\left[\partial_t \mathbf{u}' + (\bar{\mathbf{u}}\cdot\nabla)\mathbf{u}'
+ (\mathbf{u}'\cdot\nabla)\bar{\mathbf{u}}\right]
= -\nabla p' + \mu\nabla^2\mathbf{u}', \qquad \nabla\cdot\mathbf{u}' = 0$$

with no-slip $\mathbf{u}' = 0$ at walls. Normal modes turn this into the Orr–Sommerfeld
eigenvalue problem; its unstable eigenvalues mark the transition Reynolds numbers.

## Common mistakes

- **Confusing equilibrium with stability** — solving $\sum F = 0$ says nothing about
  what perturbations do.
- **Keeping quadratic perturbation terms** in a *linear* analysis (they matter later —
  for saturation — but not for onset).
- **Forgetting that linear theory only governs onset.** Once amplitudes grow, nonlinear
  terms take over; linear theory can't predict the final state.

## Related concepts

- [Kelvin–Helmholtz instability](kelvin-helmholtz-instability.md) — shear-driven application
- [Rayleigh–Taylor instability](rayleigh-taylor-instability.md) — buoyancy-driven application
- [Turbulence](turbulence.md) — the usual destination
- [Navier–Stokes equation](../equations/navier-stokes-equation.md) — the system being linearized

## Knowledge graph position

**Prerequisites:** [Navier–Stokes](../equations/navier-stokes-equation.md), [Material derivative](material-derivative.md), Fourier methods.
**Leads to:** [Kelvin–Helmholtz](kelvin-helmholtz-instability.md), [Rayleigh–Taylor](rayleigh-taylor-instability.md), [Turbulence](turbulence.md).

## Quiz

**Q1 (computational).** In the toy model, what is the critical $\lambda$ at which the
$n = 2$ mode first becomes unstable?

??? success "Answer"
    $\lambda = 4\pi^2 \approx 39.5$ (from $s_2 = 1 - 4\pi^2/\lambda = 0$).

**Q2 (conceptual).** Why does the *most unstable* mode, rather than all unstable modes
equally, dominate the observed pattern?

??? success "Answer"
    Amplitudes grow like $e^{s_n t}$; exponential separation means the largest $s_n$
    wins by an exponentially widening margin, until nonlinearity saturates it.

**Q3 (multiple choice).** Linear stability analysis can predict:

- (a) the fully developed turbulent state
- (b) the onset threshold and initially dominant wavelength
- (c) the final amplitude of the instability
- (d) nothing once viscosity is included

??? success "Answer"
    **(b).** Onset and pattern selection are linear questions; saturation and the end
    state are nonlinear.
