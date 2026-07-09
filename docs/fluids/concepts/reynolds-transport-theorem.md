# Reynolds Transport Theorem

## Intuition

Newton's laws apply to a *fixed lump of matter* — but the lump of fluid you care about
this second is somewhere else next second. Engineers would much rather do bookkeeping
on a *fixed region of space* (a control volume: the inside of a jet engine, a pipe
section). The Reynolds transport theorem (RTT) is the exchange rate between the two
kinds of accounting: **change following the matter = change inside the region + flux
through its boundary**.

## Formal statement

For a quantity with density $f$ per unit volume, carried by a flow $\mathbf{v}$ through
a volume $\Omega(t)$ with boundary $\partial\Omega(t)$ and outward normal $\mathbf{n}$:

$$\boxed{\;\frac{D}{Dt}\int_{\Omega(t)} f\, dV
= \int_{\Omega(t)} \frac{\partial f}{\partial t}\, dV
+ \oint_{\partial\Omega(t)} f\,\mathbf{v}\cdot\mathbf{n}\, dS\;}$$

It is the finite-volume sibling of the
[material derivative](material-derivative.md): the same Lagrangian→Eulerian
translation, integrated over a region. (The analogy in thermodynamics: *system* vs
*control volume*.)

## What you get by choosing $f$

| Choice of $f$ | Conservation law it yields |
|---|---|
| $\rho$ | mass — the [continuity equation](../equations/continuity-equation.md) |
| $\rho\mathbf{v}$ | momentum — [Euler](../equations/euler-equation.md) / [Navier–Stokes](../equations/navier-stokes-equation.md) with the stress tensor $\mathbf{T}$ |
| $\rho e$ | energy — heat flux and work terms |
| $\rho\,\mathbf{r}\times\mathbf{v}$ | angular momentum — turbomachinery analysis |

For momentum, the theorem reads

$$\frac{D}{Dt}\int_{\Omega} \rho\mathbf{v}\, dV
= \int_{\Omega} \rho\mathbf{f}\, dV + \oint_{\partial\Omega} \mathbf{T}\cdot\mathbf{n}\, dS$$

where $\mathbf{f}$ is body force per unit volume and $\mathbf{T}$ the stress tensor —
the integral form from which the differential equations of motion are extracted.

## Derivation sketch (mass)

The mass of a material volume is $m(t) = \int_{\Omega(t)}\rho\,dV$. Its rate of change
has two contributions: the density changing *inside* ($\partial\rho/\partial t$), and
the boundary moving with the fluid, sweeping volume at rate $\mathbf{v}\cdot\mathbf{n}$
per unit area. Summing:

$$\frac{Dm}{Dt} = \int_{\Omega} \frac{\partial\rho}{\partial t}\,dV + \oint_{\partial\Omega}\rho\,\mathbf{v}\cdot\mathbf{n}\,dS$$

Setting $Dm/Dt = 0$ (mass is conserved) and applying the divergence theorem gives the
[continuity equation](../equations/continuity-equation.md).

## Common mistakes

- **Forgetting the flux term** when the control volume is fixed but fluid crosses its
  boundary — that term is usually the whole point.
- **Wrong normal direction:** $\mathbf{n}$ points *outward*; inflow contributes
  negatively.
- **Applying RTT to a quantity per unit *mass*.** The theorem as written wants $f$ per
  unit *volume* (use $\rho\times$ specific quantity).

## Related concepts

- [Material derivative](material-derivative.md) — infinitesimal version
- [Continuity equation](../equations/continuity-equation.md) — first payoff
- [Euler's equation](../equations/euler-equation.md) — second payoff
- [Rankine–Hugoniot conditions](../equations/rankine-hugoniot-conditions.md) — RTT bookkeeping across a shock

## Knowledge graph position

**Prerequisites:** [Material derivative](material-derivative.md), [Eulerian vs Lagrangian](eulerian-vs-lagrangian.md).
**Leads to:** [Continuity](../equations/continuity-equation.md), [Euler](../equations/euler-equation.md), [Navier–Stokes](../equations/navier-stokes-equation.md).

## Quiz

**Q1 (conceptual).** A rocket engine test stand encloses the engine in a fixed control
volume. Steady operation: nothing inside changes in time. Where does the thrust show up
in the RTT?

??? success "Answer"
    Entirely in the flux term: momentum leaves through the nozzle exit at rate
    $\dot m v_e$ (plus a pressure–area term). The surface integral of momentum flux
    equals the force on the stand.

**Q2 (multiple choice).** Setting $f = \rho$ and $D/Dt \int \rho\, dV = 0$ in the RTT
gives:

- (a) Bernoulli's equation  (b) the continuity equation  (c) the Navier–Stokes equation  (d) Archimedes' principle

??? success "Answer"
    **(b).** Mass conservation is the simplest application.

**Q3 (conceptual).** Why is the RTT called a bridge between Lagrangian and Eulerian
descriptions?

??? success "Answer"
    The left side is Lagrangian (follows a material volume); the right side is Eulerian
    (a fixed-region volume integral plus boundary flux). It converts statements about
    matter into statements about fields in space.
