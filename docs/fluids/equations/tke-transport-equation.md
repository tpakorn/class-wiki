# Turbulence Kinetic Energy Transport Equation

## Equation

For $k = \tfrac12\overline{u_i' u_i'}$ (turbulent kinetic energy per unit mass):

$$\frac{\partial k}{\partial t} + \bar u_j\frac{\partial k}{\partial x_j}
= -\frac{1}{\rho}\frac{\partial}{\partial x_j}\overline{u_j' p'}
- \frac{1}{2}\frac{\partial}{\partial x_j}\overline{u_i' u_j' u_i'}
+ \nu\frac{\partial^2 k}{\partial x_j^2}
- \overline{u_i' u_j'}\frac{\partial \bar u_i}{\partial x_j}
- \nu\,\overline{\frac{\partial u_i'}{\partial x_j}\frac{\partial u_i'}{\partial x_j}}$$

## Physical meaning — the energy budget of turbulence

| Term | Name | Role |
|---|---|---|
| $\partial k/\partial t$ | rate of change | local storage |
| $\bar u_j\,\partial_j k$ | mean-flow convection | carried by the mean stream |
| $-\frac{1}{\rho}\partial_j\overline{u_j'p'}$ | pressure diffusion | redistribution by pressure fluctuations |
| $-\frac12\partial_j\overline{u_i'u_j'u_i'}$ | turbulent transport | eddies carrying their own energy |
| $\nu\,\partial_j^2 k$ | viscous transport | molecular diffusion of $k$ |
| $-\overline{u_i'u_j'}\,\partial_j\bar u_i$ | **production** $\mathcal{P}$ | extraction from mean shear via Reynolds stress |
| $-\nu\overline{(\partial_j u_i')^2}$ | **dissipation** $\varepsilon$ | conversion to heat at the [Kolmogorov scale](../concepts/energy-cascade.md) |

In steady homogeneous shear, the budget collapses to $\mathcal{P} \approx \varepsilon$:
what the mean flow feeds in, viscosity burns — through the
[energy cascade](../concepts/energy-cascade.md) in between.

## Variables

$k$ — TKE (m² s⁻²) · $\bar u_i$ — mean velocity · $u_i', p'$ — fluctuations ·
$\nu$ — kinematic viscosity · overbars — ensemble/time averages.

## Assumptions

Incompressible · Newtonian ·
[Reynolds decomposition](../concepts/reynolds-averaging.md) meaningful (statistically
steady or slowly varying flow).

## Derivation

Multiply the fluctuating momentum equation (full
[Navier–Stokes](navier-stokes-equation.md) minus its Reynolds average) by $u_i'$ and
average. Each nonlinearity contributes one budget term; the algebra is bookkeeping,
the physics is in the two sign-definite terms: production (usually $> 0$, since
$\overline{u'v'}$ opposes mean shear) and dissipation (always $> 0$).

## Applications

- The backbone of the $k$–$\varepsilon$ and $k$–$\omega$ turbulence models
  (they carry modeled versions of exactly these terms)
- Diagnosing simulations/experiments: where turbulence is born (production peaks near
  walls) and where it dies
- Atmospheric boundary-layer meteorology (add buoyancy production)

## Limitations

Averaged description only — no phase information, no coherent-structure detail; the
higher-order correlations inside transport terms are unclosed
(the [closure problem](../concepts/reynolds-averaging.md) again).

## Related equations

- [Navier–Stokes equation](navier-stokes-equation.md) — parent
- [Kolmogorov spectrum](../concepts/energy-cascade.md) — where $\varepsilon$ goes

## Quiz

**Q1 (conceptual).** Why is the production term usually positive in a shear flow?

??? success "Answer"
    In shear $\partial\bar u/\partial y > 0$, eddies moving up ($v' > 0$) carry slower
    fluid ($u' < 0$) and vice versa, so $\overline{u'v'} < 0$; then
    $-\overline{u'v'}\,\partial\bar u/\partial y > 0$. Turbulence taxes the mean flow.

**Q2 (multiple choice).** In steady, homogeneous turbulence with no mean shear, the TKE
equation reduces to:

- (a) $\mathcal{P} = \varepsilon$  (b) $dk/dt = -\varepsilon$ (decay)  (c) $k = $ const  (d) $\varepsilon = 0$

??? success "Answer"
    **(b).** With no production or transport, turbulence simply decays — grid
    turbulence in a wind tunnel is the classic realization.
