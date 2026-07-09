# Reynolds Averaging & the Closure Problem

## Intuition

If turbulent details are unpredictable, stop predicting them. Engineers usually want
the *mean* flow — average velocity in a pipe, mean lift on a wing. Reynolds' move:
split every field into mean + fluctuation, average the equations, and hope the
fluctuations' effect on the mean can be modeled. It *almost* works: the averaged
equations are exact but contain one new unknown — the Reynolds stress — and modeling it
is the famous **closure problem**, still the day job of turbulence modeling a century
later.

## Reynolds decomposition

$$u_i = \bar{u}_i + u_i', \qquad p = \bar{p} + p'$$

with the mean defined as a long-time (or ensemble) average
$\bar{u}_i = \frac{1}{T}\int_0^T u_i\,dt$, so that $\overline{u_i'} = 0$ but — crucially —

$$\overline{u_i u_j} = \bar{u}_i\bar{u}_j + \overline{u_i' u_j'}$$

The quadratic nonlinearity of [Navier–Stokes](../equations/navier-stokes-equation.md)
means fluctuations do **not** average away.

## The RANS equations

Averaging incompressible Navier–Stokes:

$$\frac{\partial \bar{u}_i}{\partial t} + \bar{u}_j\frac{\partial \bar{u}_i}{\partial x_j}
+ \frac{\partial \overline{u_i' u_j'}}{\partial x_j}
= -\frac{1}{\rho}\frac{\partial \bar{p}}{\partial x_i} + \nu\frac{\partial^2 \bar{u}_i}{\partial x_j \partial x_j},
\qquad \frac{\partial \bar{u}_i}{\partial x_i} = 0$$

Identical to the laminar equations except for one intruder:

$$R_{ij} = \overline{u_i' u_j'}$$

the **Reynolds stress tensor** — the mean momentum flux carried by fluctuations. Six
new unknowns, zero new equations: the system no longer closes. (Writing an equation for
$R_{ij}$ just summons triple correlations $\overline{u'u'u'}$, and so on forever.)

## Boussinesq's eddy viscosity

The oldest closure models Reynolds stress like a molecular stress:

$$R_{ij} = -\nu_t\left(\frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial \bar{u}_j}{\partial x_i}\right) + \frac{2}{3}k\,\delta_{ij}$$

with **eddy viscosity** $\nu_t$ (a property of the *flow*, not the fluid — usually
$\nu_t \gg \nu$) and turbulent kinetic energy $k = \frac{1}{2}\overline{u_i' u_i'}$.
Industrial models ($k$–$\varepsilon$, $k$–$\omega$, …) supply transport equations for
$\nu_t$'s ingredients.

## The turbulent kinetic energy budget

Multiplying the momentum equation by $u_i'$ and averaging yields the
[TKE transport equation](../equations/tke-transport-equation.md):

$$\frac{\partial k}{\partial t} + \bar{u}_j\frac{\partial k}{\partial x_j}
= \underbrace{-\overline{u_i'u_j'}\frac{\partial \bar u_i}{\partial x_j}}_{\text{production}}
\;\underbrace{-\;\nu\overline{\frac{\partial u_i'}{\partial x_j}\frac{\partial u_i'}{\partial x_j}}}_{\text{dissipation}}
\;+\;\text{(transport terms)}$$

Production extracts energy from mean-flow shear; dissipation hands it to heat at the
[Kolmogorov scale](energy-cascade.md); pressure, turbulent and viscous transport
shuffle it in space. This budget is the accounting sheet behind every RANS model.

## Common mistakes

- **Assuming averaging removes fluctuations' influence.** The whole difficulty is that
  it doesn't — $\overline{u'u'} \neq 0$.
- **Treating $\nu_t$ as a fluid property.** It varies point-to-point and flow-to-flow;
  tabulating it like $\mu$ is meaningless.
- **Confusing $k$ (turbulent kinetic energy) with wavenumber $k$** in the
  [spectrum](energy-cascade.md) — regrettable but standard notation clash.

## Related concepts

- [Turbulence](turbulence.md) — why we're here
- [Energy cascade](energy-cascade.md) — where the dissipation term sends energy
- [Navier–Stokes equation](../equations/navier-stokes-equation.md) — the unaveraged truth
- [TKE transport equation](../equations/tke-transport-equation.md) — full term-by-term form

## Knowledge graph position

**Prerequisites:** [Turbulence](turbulence.md), [Navier–Stokes](../equations/navier-stokes-equation.md), statistics basics.
**Leads to:** CFD turbulence models, [TKE equation](../equations/tke-transport-equation.md).

## Quiz

**Q1 (conceptual).** Where exactly in the averaging does the Reynolds stress come from?

??? success "Answer"
    From averaging the convective term:
    $\overline{u_j\partial_j u_i} = \bar u_j \partial_j \bar u_i + \partial_j\overline{u_i'u_j'}$.
    The quadratic nonlinearity correlates fluctuations with themselves.

**Q2 (multiple choice).** The closure problem refers to:

- (a) boundary conditions being unknown
- (b) more unknowns than equations after averaging
- (c) numerical instability of RANS solvers
- (d) the finite size of computational domains

??? success "Answer"
    **(b).** Each attempt to derive equations for the new correlations generates
    higher-order ones.

**Q3 (conceptual).** In a pipe, the mean velocity profile is much flatter in turbulent
flow than the laminar parabola. Explain via Reynolds stress.

??? success "Answer"
    Turbulent eddies transport fast core fluid toward the walls and slow wall fluid
    into the core ($\overline{u'v'} < 0$), acting like a huge extra viscosity that
    evens out the profile — steep gradients survive only in the thin near-wall layer.
