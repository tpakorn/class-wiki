# Viscosity

## Intuition

Drag a spoon through water, then through honey. Honey resists — not because it's
heavier (it barely is), but because its layers grip each other as they slide. Viscosity
is *internal friction between fluid layers in relative motion*: fast layers drag slow
ones forward, slow layers hold fast ones back, and mechanical energy quietly leaks into
heat.

## Formal definition

For simple shear (velocity $u(y)$ varying across the flow), **Newton's law of
viscosity**:

$$\boxed{\,\tau = \mu\,\frac{du}{dy}\,}$$

- $\tau$ — shear stress (Pa)
- $\mu$ — **dynamic viscosity** (Pa·s), a material property
- $du/dy$ — velocity gradient / shear rate (s⁻¹)

The **kinematic viscosity** $\nu = \mu/\rho$ (m²/s) is momentum's diffusion
coefficient — see the [Navier–Stokes equation](../equations/navier-stokes-equation.md)
and [Newton's law of viscosity](../equations/newtons-law-of-viscosity.md).

## Newtonian vs non-Newtonian

| Class | Behavior | Examples |
|---|---|---|
| **Newtonian** | $\mu$ constant; $\tau \propto du/dy$ | water, air, most oils |
| Shear-thinning (pseudoplastic) | $\mu$ falls with shear rate | paint, blood, ketchup |
| Shear-thickening (dilatant) | $\mu$ rises with shear rate | cornstarch + water |
| Viscoelastic | stores *and* dissipates | polymers, biological fluids |

This course stays Newtonian; the rich world beyond is rheology.

## What viscosity does to a flow

- **No-slip condition.** At a solid boundary the fluid velocity *equals* the wall
  velocity. This single boundary condition creates most of real-fluid physics.
- **Velocity gradients.** Layers must shear to reconcile no-slip walls with a moving
  interior — hence profiles like [Couette](../examples/couette-flow.md) (linear) and
  [Poiseuille](../examples/hagen-poiseuille-flow.md) (parabolic).
- **Boundary layers.** At high [Reynolds number](reynolds-number.md) viscosity retreats
  into thin layers near walls — but never disappears.
- **Dissipation.** Kinetic energy → heat, at rate $\sim \mu (du/dy)^2$ per unit volume;
  the endpoint of the turbulent [energy cascade](energy-cascade.md).

## Physical interpretation

Microscopically, molecules wander between layers, carrying their momentum with them
(gases) or drag each other via intermolecular forces (liquids). That's why gas
viscosity *rises* with temperature (faster wanderers) while liquid viscosity *falls*
(looser grip).

## Common mistakes

- **"Viscous fluid = dense fluid."** Mercury is dense but runny; pancake syrup is light
  but viscous. $\mu$ and $\rho$ are independent — that's why $\nu = \mu/\rho$ exists.
- **Dropping no-slip for "small viscosity".** However small $\mu$, the wall velocity
  matches exactly; the adjustment just happens in a thinner layer.
- **Applying inviscid results in the boundary layer** — d'Alembert's paradox (zero
  drag) is the famous punishment.

## Related concepts

- [Newton's law of viscosity](../equations/newtons-law-of-viscosity.md) — the constitutive equation
- [Navier–Stokes equation](../equations/navier-stokes-equation.md) — momentum with viscosity included
- [Reynolds number](reynolds-number.md) — inertia vs viscosity scorecard
- [Turbulence](turbulence.md) & [energy cascade](energy-cascade.md) — where dissipation ends up

## Knowledge graph position

**Prerequisites:** [What is a fluid?](what-is-a-fluid.md), [Eulerian description](eulerian-vs-lagrangian.md).
**Leads to:** [Navier–Stokes](../equations/navier-stokes-equation.md), [Reynolds number](reynolds-number.md), [Turbulence](turbulence.md).

## Quiz

**Q1 (computational).** Two plates 2 mm apart; the top one slides at 1 m/s. For water
($\mu = 10^{-3}$ Pa·s), what shear stress acts on each plate?

??? success "Answer"
    Linear (Couette) profile: $\tau = \mu U/h = 10^{-3}\times 1/0.002 = 0.5$ Pa.

**Q2 (conceptual).** Why does stirring cornstarch-in-water slowly work fine, but
punching it feels like hitting a solid?

??? success "Answer"
    It is shear-thickening: viscosity increases dramatically with shear rate. Slow
    stirring = low shear rate = low $\mu$; a punch = huge shear rate = enormous $\mu$.

**Q3 (multiple choice).** The no-slip condition states that at a stationary wall:

- (a) shear stress vanishes  (b) normal velocity vanishes only
- (c) the full fluid velocity vanishes  (d) pressure vanishes

??? success "Answer"
    **(c).** Both normal *and* tangential components match the wall (zero). Inviscid
    theory can only enforce (b) — that's why it misses drag.
